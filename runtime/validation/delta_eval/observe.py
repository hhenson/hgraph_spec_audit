"""Observe prewritten pass-through deltas using each engine's real eval_node graph."""
import argparse
import contextlib
from datetime import date, datetime, time, timedelta, timezone
import hashlib
import importlib.metadata
import inspect
import io
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
CORPUS = HERE / 'reasoned.json'

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def identity():
    import hgraph
    from hgraph.test import eval_node
    sys.path.insert(0, str(HERE.parent / 'fixed'))
    from reference_identity import reference_identity
    from native_identity import native_hashes
    distribution = importlib.metadata.distribution('hgraph')
    package = reference_identity(hgraph, distribution)
    # Do not publish direct_url.json contents or private machine paths.
    native = sys.modules.get('_hgraph') or sys.modules.get('hgraph._hgraph')
    loaded = {}
    maps = Path('/proc/self/maps')
    if maps.exists():
        for line in maps.read_text().splitlines():
            path = Path(line.split()[-1])
            if path.is_absolute() and path.is_file() and 'hgraph' in path.name and '.so' in path.name:
                loaded[path.name] = sha(path)
    return {'python':sys.version.split()[0], 'hgraph':distribution.version,
            'native':native is not None, 'package':package,
            'eval_node_module':eval_node.__module__, 'eval_node_source_sha256':sha(inspect.getfile(eval_node)),
            'native_artifacts':native_hashes(Path(native.__file__)) if native else {},
            'loaded_hgraph_libraries':loaded}

def scalar_decode(value):
    if not isinstance(value,dict): return value
    if 'date' in value: return date.fromisoformat(value['date'])
    if 'time' in value: return time.fromisoformat(value['time'])
    if 'datetime' in value: return datetime.fromisoformat(value['datetime'])
    if 'duration_us' in value: return timedelta(microseconds=value['duration_us'])
    raise ValueError('unsupported scalar encoding')

def encode(value):
    from hgraph import REMOVE
    if value is REMOVE: return {'remove':True}
    if value is None: return None
    if isinstance(value,datetime): return {'datetime':value.isoformat()}
    if isinstance(value,date): return {'date':value.isoformat()}
    if isinstance(value,time): return {'time':value.isoformat()}
    if isinstance(value,timedelta): return {'duration_us':(value.days*86400+value.seconds)*1000000+value.microseconds}
    if hasattr(value,'added') and hasattr(value,'removed'):
        return {'added':sorted(encode(v) for v in value.added),'removed':sorted(encode(v) for v in value.removed)}
    if hasattr(value,'items'): return {str(k):encode(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)): return [encode(v) for v in value]
    if isinstance(value,(set,frozenset)): return sorted(encode(v) for v in value)
    if isinstance(value,(bool,int,float,str)): return value
    raise TypeError('unhandled observed value type '+type(value).__name__)

def observe(case):
    from hgraph import TS,TSS,TSL,TSB,TSD,Size,TimeSeriesSchema,compute_node,Removed,REMOVE
    from hgraph.test import eval_node
    scalar_types = {'bool':bool,'i64':int,'f64':float,'str':str,'date':date,'time':time,'datetime':datetime,'duration':timedelta}
    kind=case['type']
    if kind in scalar_types:
        schema=TS[scalar_types[kind]]
        samples=[scalar_decode(v) for v in case['inputs']]
    elif kind.startswith('tss_'):
        schema=TSS[bool if kind=='tss_bool' else int]
        samples=[None if v is None else set(v['added'])|{Removed(x) for x in v['removed']} for v in case['inputs']]
    elif kind=='tsl':
        schema=TSL[TS[int],Size[2]]
        samples=[None if v is None else {int(k):x for k,x in v.items()} for v in case['inputs']]
    elif kind=='tsd':
        schema=TSD[int,TS[int]]
        samples=[None if v is None else {int(k):REMOVE if x=={'remove':True} else x for k,x in v.items()} for v in case['inputs']]
    elif kind=='tsb':
        class DeltaEvalQuote(TimeSeriesSchema):
            bid: TS[int]
            ask: TS[int]
        schema=TSB[DeltaEvalQuote]
        samples=case['inputs']
    else: raise ValueError(kind)
    # A runtime compute with its own output. Graph identity would bypass this operation.
    def pass_through(ts):
        return ts.delta_value
    pass_through.__annotations__={'ts':schema,'return':schema}
    node=compute_node(pass_through)
    output=eval_node(node,samples)
    raw=encode(output)
    # Preserve the untouched engine result separately. Padding is solely the input horizon.
    dense=[] if raw is None else list(raw)
    dense += [None]*max(0,len(samples)-len(dense))
    return {'raw_eval_node':raw,'input_horizon':len(samples),'dense_from_input_horizon':dense,
            'padding_added':max(0,len(samples)-(0 if raw is None else len(raw)))}

def probe():
    before=identity()
    observations={}
    for case in json.loads(CORPUS.read_text())['cases']:
        try:
            with contextlib.redirect_stdout(io.StringIO()),contextlib.redirect_stderr(io.StringIO()):
                observations[case['id']]=observe(case)
        except Exception as exc:
            # Preserve error class/message; strip any local checkout paths from messages.
            message=str(exc)
            for prefix in (str(HERE.parents[3]), str(Path.home())):
                message=message.replace(prefix,'<private-path>')
            observations[case['id']]={'error_type':type(exc).__name__,'error':message}
    after=identity()
    if before!=after: raise RuntimeError('engine artifacts changed during observation')
    return {'identity':before,'observations':observations}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--probe',action='store_true')
    parser.add_argument('--python',type=Path)
    parser.add_argument('--cpp',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    if args.probe:
        print(json.dumps(probe(),sort_keys=True)); return
    if not args.python or not args.cpp or not args.output or args.output.exists():
        parser.error('supply --python, --cpp and a new --output file')
    corpus_hash=sha(CORPUS)
    corpus=json.loads(CORPUS.read_text())
    evidence={'measured_at':datetime.now(timezone.utc).isoformat(),'reasoned_sha256':corpus_hash,
              'harness_sha256':sha(__file__),'repeats':3,'engines':{}}
    for name,exe,native in [('python',args.python,False),('cpp',args.cpp,True)]:
        runs=[json.loads(subprocess.check_output([str(exe.absolute()),__file__,'--probe'],text=True).strip().splitlines()[-1]) for _ in range(3)]
        if any(run!=runs[0] for run in runs): raise RuntimeError(name+' fresh-process observations are unstable')
        if runs[0]['identity']['native']!=native: raise RuntimeError(name+' has wrong engine identity')
        if sha(CORPUS)!=corpus_hash: raise RuntimeError('expectations changed during execution')
        result=runs[0]
        result['assessment']={case['id']:('error' if 'error_type' in result['observations'][case['id']] else
               'match' if result['observations'][case['id']]['dense_from_input_horizon']==case['expected'] else 'divergence') for case in corpus['cases']}
        evidence['engines'][name]=result
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(evidence,indent=2,sort_keys=True)+'\n')
    for name,data in evidence['engines'].items():
        from collections import Counter
        print(name,dict(Counter(data['assessment'].values())))

if __name__=='__main__': main()
