"""Bounded lifecycle and retained-delta measurements, separate from horizon padding."""
import argparse
import contextlib
import gc
import io
import json
from pathlib import Path
import subprocess
import sys
from datetime import datetime,timezone
from observe import identity,encode,sha
HERE=Path(__file__).resolve().parent

def probe():
    import hgraph as hg
    from hgraph.test import eval_node
    before=identity(); native=before['native']
    key='eval_node::out' if native else 'nodes.record.out'
    def capture(gs):
        present=key in gs
        return {'present':present,'entries':len(gs[key]) if present else None}
    class Observer(hg.EvaluationLifeCycleObserver):
        def __init__(self,gs): self.gs=gs; self.events=[]
        def name(self,node): return node.label if native else node.signature.name
        def on_after_start_node(self,node):
            name=self.name(node)
            if 'record' in name:self.events.append({'event':'recorder_started','name':name,'external_capture':capture(self.gs)})
        def on_after_stop_node(self,node):
            name=self.name(node)
            if 'record' in name:self.events.append({'event':'recorder_stopped','name':name,'external_capture':capture(self.gs)})
        def on_after_start_graph(self,graph):self.events.append({'event':'graph_started','external_capture':capture(self.gs)})
        def on_after_stop_graph(self,graph):self.events.append({'event':'graph_stopped','external_capture':capture(self.gs)})
    @hg.compute_node
    def passthrough(ts:hg.TS[int])->hg.TS[int]:return ts.delta_value
    observations={}
    for name,values in [('empty',[]),('all_silent',[None,None,None])]:
        gs=hg.GlobalState(); observer=Observer(gs)
        with gs:
            result=eval_node(passthrough,values,__observers__=[observer])
            post=capture(gs)
            observer.events.append({'event':'eval_returned','external_capture':post})
        observations[name]={'raw':encode(result),'record_present_after_eval':post['present'],
            'record_entries_after_eval':post['entries'],
            'recorder_start_callbacks':sum(x['event']=='recorder_started' for x in observer.events),
            'recorder_stop_callbacks':sum(x['event']=='recorder_stopped' for x in observer.events),'events':observer.events}
    gs=hg.GlobalState()
    with gs:
        first=eval_node(passthrough,[1,2]);second=eval_node(passthrough,[3]);third=eval_node(passthrough,[None,None])
        observations['isolation']={'first':encode(first),'second':encode(second),'third_raw':encode(third),
            'third_dense':[None,None] if third is None else encode(third),
            'retained_first_after_second_and_third':encode(first),'capture_after_third':capture(gs)}
    shared={}
    @hg.compute_node
    def publish(ts:hg.TS[int])->hg.TSD[int,hg.TS[int]]:
        shared.clear();shared[1]=ts.value;return shared
    recorded=eval_node(publish,[10,20,30]);after=encode(recorded)
    shared.clear();shared[1]=999;shared[2]=777;gc.collect()
    observations['mutable_delta']={'after_eval':after,'after_source_mutation_and_collection':encode(recorded),'mutated_source':encode(shared)}
    after_identity=identity()
    if before!=after_identity:raise RuntimeError('engine identity changed')
    return {'identity_sha256':before['package']['identity_sha256'],'native':native,'observed':observations}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--probe',action='store_true');parser.add_argument('--python',type=Path);parser.add_argument('--cpp',type=Path);parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    if args.probe:
        with contextlib.redirect_stdout(io.StringIO()),contextlib.redirect_stderr(io.StringIO()):result=probe()
        print(json.dumps(result,sort_keys=True));return
    if not args.python or not args.cpp or not args.output or args.output.exists():parser.error('independent interpreters and new output required')
    corpus=HERE/'lifecycle_reasoned.json';corpus_hash=sha(corpus);expected=json.loads(corpus.read_text())['expectations']
    evidence={'reasoned_sha256':corpus_hash,'harness_sha256':sha(__file__),'measured_at':datetime.now(timezone.utc).isoformat(),'repeats':3,'engines':{}}
    for name,exe in [('python',args.python),('cpp',args.cpp)]:
        runs=[json.loads(subprocess.check_output([str(exe.absolute()),__file__,'--probe'],text=True).strip().splitlines()[-1]) for _ in range(3)]
        if any(r!=runs[0] for r in runs):raise RuntimeError('unstable '+name)
        result=runs[0]
        result['assessment']={case:{field:'match' if result['observed'][case][field]==value else 'divergence' for field,value in fields.items()} for case,fields in expected.items()}
        evidence['engines'][name]=result
    if sha(corpus)!=corpus_hash:raise RuntimeError('expectations changed')
    args.output.write_text(json.dumps(evidence,indent=2,sort_keys=True)+'\n')
    for name,result in evidence['engines'].items():print(name,result['assessment'])
if __name__=='__main__':main()
