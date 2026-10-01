"""Observe ordinary Python values, keyed state and timed replay; preserve failures."""
import argparse
import contextlib
import copy
from datetime import datetime,timedelta,timezone
import gc
import io
import json
from pathlib import Path
import subprocess
import sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'delta_eval'))
from observe import identity,encode,sha

def attempt(fn):
    try:return {'status':'observed','value':fn()}
    except Exception as exc:
        message=str(exc).replace(str(Path.home()),'<private-home>')
        return {'status':'error','error_type':type(exc).__name__,'message':message}

def probe():
    import hgraph as hg
    from hgraph.test import eval_node
    before=identity();native=before['native']
    result={}
    source=[[1],[2]];alias=source;shallow=source.copy();owned=copy.deepcopy(source);entry=(hg.MIN_ST,source)
    source[0].append(9);source.append([3])
    result['ordinary_python']={'source':copy.deepcopy(source),'assignment':copy.deepcopy(alias),'shallow_copy':copy.deepcopy(shallow),
        'deepcopy':owned,'tuple_nested_alias':copy.deepcopy(entry[1]),'length':len(source),'index_1':copy.deepcopy(source[1])}
    def state_aliasing():
        gs=hg.GlobalState();source=[[1],[2]]
        with gs:
            gs['ordinary.list']=source
            after_set=encode(gs['ordinary.list'])
            source[0].append(9);source.append([3])
            after_source_mutation=encode(gs['ordinary.list'])
            retrieved=gs['ordinary.list'];retained=copy.deepcopy(retrieved)
            mutation=attempt(lambda:(retrieved[1].append(8),retrieved.append([4]),None)[-1])
            after_get_mutation=encode(gs['ordinary.list'])
            gs['ordinary.list']=[[7]]
            after_replacement=encode(gs['ordinary.list'])
        gc.collect()
        return {'after_set':after_set,'after_source_mutation':after_source_mutation,'retrieval_type':type(retrieved).__name__,
            'retrieved_mutation':mutation,'after_get_mutation':after_get_mutation,'retained_deepcopy':encode(retained),
            'retrieved_after_replacement':encode(retrieved),'replacement':after_replacement}
    result['global_state_aliasing']=attempt(state_aliasing)
    data=[(hg.MIN_ST,0),(hg.MIN_ST+3*hg.MIN_TD,-7),(hg.MIN_ST+6*hg.MIN_TD,-7)]
    @hg.compute_node
    def pass_through(ts:hg.TS[int])->hg.TS[int]:return ts.delta_value
    def timed_direct(container):
        def timed_source(data):yield from data
        timed_source.__annotations__={'data':list[tuple[datetime,int]] if container=='list' else tuple[tuple[datetime,int],...],'return':hg.TS[int]}
        source=hg.generator(timed_source)
        @hg.graph
        def run()->hg.TS[int]:return pass_through(source(data if container=='list' else tuple(data)))
        return encode(eval_node(run))
    result['timed_direct_list']=attempt(lambda:timed_direct('list'))
    result['timed_direct_tuple']=attempt(lambda:timed_direct('tuple'))
    def timed_keyed():
        if native:
            # Existing sparse replay uses ordinary timestamped entries under the fully qualified key.
            @hg.graph
            def run()->hg.TS[int]:return pass_through(hg.replay('data',hg.TS[int],recordable_id='ordinary'))
            with hg.GlobalState() as gs:
                gs[':memory:ordinary.data']=data
                return encode(eval_node(run))
        from hgraph._impl._operators._record_replay_in_memory import set_replay_values,replay_from_memory
        @hg.graph
        def run()->hg.TS[int]:return pass_through(replay_from_memory('data',hg.TS[int]))
        with hg.GlobalState():
            set_replay_values('data',data)
            return encode(eval_node(run))
    result['timed_keyed_list']=attempt(timed_keyed)
    def retained_record():
        shared={}
        @hg.compute_node
        def publisher(ts:hg.TS[int])->hg.TSD[int,hg.TS[int]]:
            shared.clear();shared[1]=ts.value;return shared
        records=eval_node(publisher,[10,20,30]);shared.clear();shared[2]=99;gc.collect()
        return encode(records)
    result['retained_record_snapshots']=attempt(retained_record)
    if before!=identity():raise RuntimeError('engine changed')
    return {'identity':before,'observed':result}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--probe',action='store_true');p.add_argument('--python',type=Path);p.add_argument('--cpp',type=Path);p.add_argument('--output',type=Path);a=p.parse_args()
    if a.probe:
        with contextlib.redirect_stdout(io.StringIO()),contextlib.redirect_stderr(io.StringIO()):result=probe()
        print(json.dumps(result,sort_keys=True));return
    if not a.python or not a.cpp or not a.output or a.output.exists():p.error('independent interpreters and new output required')
    corpus=HERE/'reasoned.json';corpus_hash=sha(corpus);expected=json.loads(corpus.read_text())['expected']
    evidence={'reasoned_sha256':corpus_hash,'harness_sha256':sha(__file__),'identity_helper_sha256':sha(HERE.parent/'delta_eval/observe.py'),'measured_at':datetime.now(timezone.utc).isoformat(),'repeats':3,'engines':{}}
    for name,exe in [('python',a.python),('cpp',a.cpp)]:
        runs=[json.loads(subprocess.check_output([str(exe.absolute()),__file__,'--probe'],text=True).strip().splitlines()[-1]) for _ in range(3)]
        if any(r!=runs[0] for r in runs):raise RuntimeError('unstable '+name)
        result=runs[0]
        if result['identity']['native']!=(name=='cpp'):raise RuntimeError('wrong engine')
        result['assessment']={key:('error' if result['observed'][key]['status']=='error' else 'match' if result['observed'][key]['value']==expected[key] else 'divergence') for key in ('timed_direct_list','timed_direct_tuple','timed_keyed_list','retained_record_snapshots')}
        result['assessment']['python_explicit_deepcopy']='match' if result['observed']['ordinary_python']['deepcopy']==expected['python_explicit_deepcopy'] else 'divergence'
        evidence['engines'][name]=result
    if sha(corpus)!=corpus_hash:raise RuntimeError('reasoning changed')
    a.output.write_text(json.dumps(evidence,indent=2,sort_keys=True)+'\n')
    for name,result in evidence['engines'].items():print(name,result['assessment'])
if __name__=='__main__':main()
