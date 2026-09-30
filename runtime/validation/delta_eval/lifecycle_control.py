"""Positive control for the exact external capture key used by lifecycle.py."""
import argparse
import contextlib
import io
import json
from pathlib import Path
import subprocess
from datetime import datetime,timezone
from observe import identity,encode,sha
HERE=Path(__file__).resolve().parent

def probe():
    import hgraph as hg
    from hgraph.test import eval_node
    before=identity();key='eval_node::out' if before['native'] else 'nodes.record.out'
    def capture(gs):return {'present':key in gs,'entries':len(gs[key]) if key in gs else None}
    @hg.compute_node
    def pass_through(ts:hg.TS[int])->hg.TS[int]:return ts.delta_value
    gs=hg.GlobalState()
    with gs:
        positive=eval_node(pass_through,[1,2]);positive_capture=capture(gs)
        positive_keys=sorted(gs.keys())
        silent=eval_node(pass_through,[None,None]);silent_capture=capture(gs)
    if before!=identity():raise RuntimeError('identity changed')
    return {'identity_sha256':before['package']['identity_sha256'],'native':before['native'],
            'capture_key':key,'observed':{'positive_raw':encode(positive),'positive_capture':positive_capture,
              'positive_global_keys':positive_keys,'after_silent_raw':encode(silent),'after_silent_capture':silent_capture}}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--probe',action='store_true');p.add_argument('--python',type=Path);p.add_argument('--cpp',type=Path);p.add_argument('--output',type=Path);a=p.parse_args()
    if a.probe:
        with contextlib.redirect_stdout(io.StringIO()),contextlib.redirect_stderr(io.StringIO()):r=probe()
        print(json.dumps(r,sort_keys=True));return
    if not a.python or not a.cpp or not a.output or a.output.exists():p.error('independent interpreters and new output required')
    corpus=HERE/'lifecycle_control_reasoned.json';corpus_hash=sha(corpus);expected=json.loads(corpus.read_text())['expected']
    evidence={'reasoned_sha256':corpus_hash,'harness_sha256':sha(__file__),'measured_at':datetime.now(timezone.utc).isoformat(),'repeats':3,'engines':{}}
    for name,exe in [('python',a.python),('cpp',a.cpp)]:
        runs=[json.loads(subprocess.check_output([str(exe.absolute()),__file__,'--probe'],text=True).strip().splitlines()[-1]) for _ in range(3)]
        if any(r!=runs[0] for r in runs):raise RuntimeError('unstable '+name)
        result=runs[0];result['assessment']={k:'match' if result['observed'][k]==v else 'divergence' for k,v in expected.items()};evidence['engines'][name]=result
    if sha(corpus)!=corpus_hash:raise RuntimeError('expectations changed')
    a.output.write_text(json.dumps(evidence,indent=2,sort_keys=True)+'\n')
    for name,r in evidence['engines'].items():print(name,r['observed'])
if __name__=='__main__':main()
