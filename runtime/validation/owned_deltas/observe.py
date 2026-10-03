"""Measure retained sparse deltas from real source/compute/record graphs."""
import argparse
import contextlib
import copy
from datetime import datetime, timezone
import gc
import io
import json
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'delta_eval'))
from observe import encode,identity,sha


def observe(name):
    import hgraph as hg
    from hgraph.test import eval_node
    class Quote(hg.TimeSeriesSchema):
        bid: hg.TS[int]
        ask: hg.TS[int]
    schemas={'set_i64':hg.TSS[int], 'fixed_list':hg.TSL[hg.TS[int],hg.Size[3]],
             'named_bundle':hg.TSB[Quote], 'map':hg.TSD[int,hg.TS[int]],
             'nested_map':hg.TSD[int,hg.TSD[int,hg.TS[int]]],
             'list_of_maps':hg.TSL[hg.TSD[int,hg.TS[int]],hg.Size[2]]}
    traces={'set_i64':[{1,2},{hg.Removed(1)},{hg.Removed(2)}],
            'fixed_list':[{0:10,2:30},{0:11},{2:31}],
            'named_bundle':[{'bid':10,'ask':20},{'bid':11},{'ask':21}],
            'map':[{1:10,2:20},{1:11},{2:hg.REMOVE}],
            'nested_map':[{7:{1:10,2:20}},{7:{1:11}},{7:{2:hg.REMOVE}}],
            'list_of_maps':[{0:{1:10,2:20}},{0:{1:11}},{0:{2:hg.REMOVE}}]}
    schema=schemas[name]
    reused=set() if name=='set_i64' else {}
    def source():
        for i,value in enumerate(traces[name]):
            reused.clear()
            reused.update(value)
            yield hg.MIN_ST+i*hg.MIN_TD,reused
        reused.clear()
    source.__annotations__={'return':schema}
    source_node=hg.generator(source)
    def delta_pass(ts):
        return ts.delta_value
    delta_pass.__annotations__={'ts':schema,'return':schema}
    pass_node=hg.compute_node(delta_pass)
    def composition():
        return pass_node(source_node())
    composition.__annotations__={'return':schema}
    result=eval_node(hg.graph(composition))
    before=encode(result)
    reused.clear()
    gc.collect()
    after=encode(result)
    return {'before_owner_cleanup':before,'after_owner_cleanup':after,'unchanged':before==after}


def probe():
    before=identity();results={}
    for name in json.loads((HERE/'reasoned.json').read_text())['expected']:
        try:
            with contextlib.redirect_stdout(io.StringIO()),contextlib.redirect_stderr(io.StringIO()):
                results[name]=observe(name)
        except Exception as exc:
            results[name]={'error_type':type(exc).__name__,'error':str(exc).replace(str(Path.home()),'<private-home>')}
    if before!=identity():raise RuntimeError('engine changed during observation')
    return {'identity':before,'observations':results}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--probe',action='store_true');p.add_argument('--python',type=Path);p.add_argument('--cpp',type=Path);p.add_argument('--output',type=Path)
    a=p.parse_args()
    if a.probe:
        print(json.dumps(probe(),sort_keys=True));return
    if not a.python or not a.cpp or not a.output or a.output.exists():p.error('independent interpreters and new output required')
    corpus=HERE/'reasoned.json';before=sha(corpus);expected=json.loads(corpus.read_text())['expected']
    evidence={'measured_at':datetime.now(timezone.utc).isoformat(),'reasoned_sha256':before,'harness_sha256':sha(__file__),'identity_helper_sha256':sha(HERE.parent/'delta_eval/observe.py'),'repeats':3,'engines':{}}
    for name,executable,native in [('python',a.python,False),('cpp',a.cpp,True)]:
        runs=[json.loads(subprocess.check_output([str(executable),__file__,'--probe'],text=True)) for _ in range(3)]
        if any(run!=runs[0] for run in runs) or runs[0]['identity']['native']!=native:raise RuntimeError('unstable or incorrect engine '+name)
        result=runs[0];result['assessment']={}
        for case,want in expected.items():
            observed=result['observations'][case]
            result['assessment'][case]='error' if 'error' in observed else 'match' if observed['before_owner_cleanup']==want and observed['after_owner_cleanup']==want else 'divergence'
        evidence['engines'][name]=result;print(name,result['assessment'])
    if sha(corpus)!=before:raise RuntimeError('expectations changed')
    a.output.write_text(json.dumps(evidence,indent=2,sort_keys=True)+'\n')

if __name__=='__main__':main()
