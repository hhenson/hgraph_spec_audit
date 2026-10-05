"""Observe finite optional ordinary fields through atomic TS authoring."""
import argparse
import contextlib
from datetime import datetime, timezone
import io
from pathlib import Path
import subprocess
import sys
import json

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import identity, sha

def probe():
    before = identity()
    from dataclasses import dataclass
    import json
    from typing import Optional
    import hgraph as hg
    from hgraph.test import eval_node
    
    @dataclass(frozen=True)
    class OptionalRecord(hg.CompoundScalar):
        name: str
        value: Optional[int] = None
    
    @dataclass(frozen=True)
    class DefaultNoneRecord(hg.CompoundScalar):
        name: str
        value: int = None
    
    @dataclass(frozen=True)
    class OptionalList(hg.CompoundScalar):
        values: Optional[list[int]] = None
    
    def snapshot(x):
        if isinstance(x, (OptionalRecord, DefaultNoneRecord)):
            return {'type': type(x).__name__, 'name': x.name, 'value': x.value}
        if isinstance(x, OptionalList):
            return {'type': type(x).__name__, 'values': snapshot(x.values)}
        if isinstance(x, (list, tuple)): return [snapshot(y) for y in x]
        return x
    out={}
    for kind in (OptionalRecord, DefaultNoneRecord, OptionalList):
        received=[]
        def forward(value):
            received.append(snapshot(value.delta_value))
            return value.delta_value
        forward.__annotations__={'value':hg.TS[kind], 'return':hg.TS[kind]}
        try:
            node=hg.compute_node(forward)
            if kind is OptionalList:
                shared=[1]
                samples=[kind(),kind(shared),None,kind([]),kind()]
            else:
                samples=[kind('a'),kind('a',0),None,kind('b',7),kind('a')]
            raw=eval_node(node,samples)
            result={'input':snapshot(samples),'raw':snapshot(raw),'received':received[:],'empty':snapshot(eval_node(node,[])),'silent':snapshot(eval_node(node,[None,None]))}
            if kind is OptionalList:
                shared.append(2)
                result['after_source']=snapshot(raw)
            out[kind.__name__]=result
        except Exception as e:
            out[kind.__name__]={'error_type':type(e).__name__,'error':str(e),'received':received}
    assert before == identity()
    return {"identity": before, "observations": out}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--probe', action='store_true')
    parser.add_argument('--python', type=Path)
    parser.add_argument('--cpp', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.probe:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            result = probe()
        print(json.dumps(result, sort_keys=True))
        return
    if not args.python or not args.cpp or not args.output or args.output.exists():
        parser.error('two interpreters and a new output path required')
    evidence = {'measured_at': datetime.now(timezone.utc).isoformat(), 'repeats': 3,
                'reasoned_sha256': sha(HERE / 'reasoned.json'), 'harness_sha256': sha(__file__),
                'identity_helper_sha256': sha(HERE.parent / 'delta_eval/observe.py'), 'engines': {}}
    for engine, executable in [('python', args.python), ('cpp', args.cpp)]:
        runs = [json.loads(subprocess.check_output([str(executable), __file__, '--probe'], text=True, timeout=30)) for _ in range(3)]
        assert all(run == runs[0] for run in runs), 'unstable observations'
        assert runs[0]['identity']['native'] == (engine == 'cpp')
        evidence['engines'][engine] = runs[0]
        print(engine, json.dumps(runs[0]['observations'], sort_keys=True))
    assert evidence['reasoned_sha256'] == sha(HERE / 'reasoned.json')
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')

if __name__ == '__main__':
    main()
