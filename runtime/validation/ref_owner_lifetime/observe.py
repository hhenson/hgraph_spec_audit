"""Observe a saved nested-producer reference without extending its logical lifetime."""
import argparse
import contextlib
from dataclasses import dataclass
from datetime import datetime, timezone
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('support',HERE.parent/'delta_eval/observe.py')
support=importlib.util.module_from_spec(spec);spec.loader.exec_module(support)


def probe(control=False):
    import hgraph as hg
    from hgraph.test import eval_node
    identity=support.identity()
    corpus=json.loads((HERE/'reasoned.json').read_text())
    events=[]
    @hg.compute_node
    def producer(value:hg.TS[int])->hg.TS[int]:
        return value.delta_value
    @hg.compute_node
    def relay(value:hg.REF[hg.TS[int]])->hg.REF[hg.TS[int]]:
        return value.value
    @hg.graph
    def branch(value:hg.TS[int])->hg.REF[hg.TS[int]]:
        return relay(value) if control else relay(producer(value))
    @dataclass
    class Captured:
        done:bool=False
    @hg.compute_node
    def first(value:hg.REF[hg.TS[int]], state:hg.STATE[Captured]=None)->hg.REF[hg.TS[int]]:
        if not state.done:
            state.done=True
            return value.value
    @hg.compute_node(valid=('step',),active=('step',))
    def observe(reference:hg.REF[hg.TS[int]],data:hg.TS[int],step:hg.TS[int])->hg.TS[str]:
        row={'reference_valid':reference.valid,'reference_modified':reference.modified,
             'data_valid':data.valid,'data_modified':data.modified,
             'value':data.value if data.valid else None}
        events.append(row)
        return json.dumps(row,sort_keys=True)
    @hg.graph
    def graph(key:hg.TS[str],value:hg.TS[int],step:hg.TS[int])->hg.TS[str]:
        selected=hg.switch_(key,{'a':branch,'b':branch},value=value)
        held=first(selected)
        return observe(held,held,step)
    result={'identity':identity}
    try:
        with contextlib.redirect_stdout(io.StringIO()),contextlib.redirect_stderr(io.StringIO()):
            raw=eval_node(graph,corpus['keys'],corpus['values'],[1]*len(corpus['keys']))
        result['raw']=raw
        result['events']=events
    except Exception as exc:
        result.update(error_type=type(exc).__name__,message=str(exc).replace(str(Path.home()),'<private-home>').replace(sys.prefix,'<environment>').replace(str(HERE.parents[2]),'<audit-root>'),events=events)
    assert support.identity()==identity
    return result


def identity_probe():
    import hgraph as hg
    from hgraph.test import eval_node
    identity=support.identity()
    @hg.compute_node
    def relay(value:hg.REF[hg.TS[int]])->hg.REF[hg.TS[int]]:
        return value.value
    @hg.compute_node
    def compare(first:hg.REF[hg.TS[int]],same:hg.REF[hg.TS[int]],distinct:hg.REF[hg.TS[int]])->hg.TS[str]:
        return json.dumps({'same_endpoint':first.value==same.value,'distinct_equal_endpoints':first.value==distinct.value},sort_keys=True)
    @hg.graph
    def graph(first:hg.TS[int],second:hg.TS[int])->hg.TS[str]:
        a=relay(first);b=relay(second)
        return compare(a,a,b)
    with contextlib.redirect_stdout(io.StringIO()),contextlib.redirect_stderr(io.StringIO()):
        raw=eval_node(graph,[7],[7])
    assert support.identity()==identity
    return {'identity':identity,'reference_identity':json.loads(raw[0]),
            'bool_operations':{'false_before_true':False<True,'equal_false_hash':hash(False)==hash(False)}}


def main():
    p=argparse.ArgumentParser();p.add_argument('--probe',action='store_true');p.add_argument('--python',type=Path);p.add_argument('--cpp',type=Path);p.add_argument('--output',type=Path);args=p.parse_args()
    if args.probe:
        print(json.dumps({'owned':probe(),'outer_owner_control':probe(True),'scalar_and_reference_identity':identity_probe()},sort_keys=True));return
    if not args.python or not args.cpp or not args.output or args.output.exists():p.error('Independent interpreters and a new output path required')
    sources={name:support.sha(HERE/name) for name in ('reasoned.json','observe.py')}
    result={'measured_at':datetime.now(timezone.utc).isoformat(),'sources_sha256':sources,'repeats':3,'engines':{}}
    for name,executable,native in [('python',args.python,False),('cpp',args.cpp,True)]:
        runs=[json.loads(subprocess.check_output([str(executable.absolute()),__file__,'--probe'],text=True).strip().splitlines()[-1]) for _ in range(3)]
        assert all(run==runs[0] for run in runs) and all(v['identity']['native']==native for v in runs[0].values())
        identity=runs[0]['owned']['identity']
        assert all(run['identity']==identity for run in runs[0].values())
        cases={case:{k:v for k,v in run.items() if k!='identity'} for case,run in runs[0].items()}
        result['engines'][name]={'identity':identity,'cases':cases}
        print(name,cases)
    assert sources=={name:support.sha(HERE/name) for name in sources}
    args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')

if __name__=='__main__':main()
