"""Observe tuple and concrete-struct keys using actual set/map graph operations."""
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
    import hgraph as hg
    from hgraph.test import eval_node

    @dataclass(frozen=True)
    class Key(hg.CompoundScalar):
        number: int
        label: str
    globals()['Key'] = Key

    def key(value):
        if isinstance(value, tuple): return {'tuple': list(value)}
        return {'type': type(value).__name__, 'number': value.number, 'label': value.label}
    def ordered(values): return sorted(values, key=lambda x: json.dumps(x, sort_keys=True))
    def snapshot(value):
        if value is None: return None
        if isinstance(value, (list, tuple)): return [snapshot(x) for x in value]
        if hasattr(value, 'added') and hasattr(value, 'removed'):
            return {'added': ordered([key(k) for k in value.added]), 'removed': ordered([key(k) for k in value.removed])}
        return ordered([{'key': key(k), 'value': {'remove': True} if v is hg.REMOVE else v} for k,v in value.items()])
    def error(exc):
        message = str(exc).replace(str(HERE.parents[2]), '<audit-root>')
        message = message.replace(sys.prefix, '<environment>').replace(str(Path.home()), '<private-home>')
        return {'error_type': type(exc).__name__, 'error': message}
    observations = {}
    for shape, ty, make in [('tuple', tuple[int, str], lambda i,s: (i,s)), ('struct', Key, Key)]:
        for family in ('set', 'map'):
            received=[]
            phase='schema'
            try:
                first, equal, second = make(1, 'a'), make(1, 'a'), make(2, 'b')
                schema=hg.TSS[ty] if family == 'set' else hg.TSD[ty, hg.TS[int]]
                def forward(value):
                    received.append(snapshot(value.delta_value))
                    return value.delta_value
                forward.__annotations__={'value':schema, 'return':schema}
                node=hg.compute_node(forward)
                samples=([{first}, {equal,second}, None, {hg.Removed(equal)}, {first}] if family=='set' else
                         [{first:1}, {equal:1,second:2}, None, {equal:hg.REMOVE}, {first:3}])
                phase='eval'
                raw=eval_node(node,samples)
                original=snapshot(raw)
                observations[shape+'_'+family]={'raw':original, 'received':list(received),
                    'second_raw':snapshot(eval_node(node,samples)), 'first_after_second':snapshot(raw),
                    'empty':snapshot(eval_node(node,[])), 'silent':snapshot(eval_node(node,[None,None]))}
            except Exception as exc:
                observations[shape+'_'+family]={**error(exc),'phase':phase,'received':received}
    assert before == identity()
    return {'identity':before,'observations':observations}

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
