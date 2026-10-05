"""Observe finite direct and mutual recursive atomic values without substitute types."""
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

    def snapshot(value):
        if value is None:
            return None
        if isinstance(value, (list, tuple)):
            return [snapshot(x) for x in value]
        if type(value) is int:
            return value
        fields = value.__dataclass_fields__
        return {'type': type(value).__name__, **{name: snapshot(getattr(value, name)) for name in fields}}

    def error(exc):
        message = str(exc).replace(str(HERE.parents[2]), '<audit-root>')
        message = message.replace(sys.prefix, '<environment>').replace(str(Path.home()), '<private-home>')
        return {'error_type': type(exc).__name__, 'error': message}

    observations = {}
    try:
        @dataclass(frozen=True)
        class Chain(hg.CompoundScalar):
            values: list[int]
            next: 'Chain' = None
        globals()['Chain'] = Chain
    except Exception as exc:
        observations['self_declaration'] = error(exc)
    else:
        for case in ('self_snapshots', 'self_retention'):
            received = []
            phase = 'schema'
            try:
                def forward(value):
                    received.append(snapshot(value.delta_value))
                    return value.delta_value
                forward.__annotations__ = {'value': hg.TS[Chain], 'return': hg.TS[Chain]}
                node = hg.compute_node(forward)
                tail = Chain([3])
                root = Chain([1], Chain([2], tail))
                leaf = Chain([9])
                samples = [root, root, None, leaf] if case == 'self_snapshots' else [root, None, root]
                phase = 'eval'
                raw = eval_node(node, samples)
                result = {'input': snapshot(samples), 'raw': snapshot(raw), 'received': list(received)}
                if case == 'self_retention':
                    tail.values.append(4)
                    result['first_after_source_mutation'] = snapshot(raw)
                received.clear()
                second = eval_node(node, samples)
                result.update(second_raw=snapshot(second), first_after_second=snapshot(raw),
                              second_received=list(received), empty=snapshot(eval_node(node, [])),
                              silent=snapshot(eval_node(node, [None, None])))
                if case == 'self_retention':
                    phase = 'capture_mutation'
                    raw[0].next.next.values.append(5)
                    result.update(first_after_capture_mutation=snapshot(raw),
                                  second_after_capture_mutation=snapshot(second), source_after_capture_mutation=snapshot(root))
                observations[case] = result
            except Exception as exc:
                observations[case] = {**error(exc), 'phase': phase, 'received': received}
    received = []
    phase = 'declaration'
    try:
        @dataclass(frozen=True)
        class MutualA(hg.CompoundScalar):
            value: int
            other: 'MutualB' = None
        globals()['MutualA'] = MutualA
        @dataclass(frozen=True)
        class MutualB(hg.CompoundScalar):
            value: int
            other: 'MutualA' = None
        globals()['MutualB'] = MutualB
        phase = 'schema'
        def forward_mutual(value):
            received.append(snapshot(value.delta_value))
            return value.delta_value
        forward_mutual.__annotations__ = {'value': hg.TS[MutualA], 'return': hg.TS[MutualA]}
        node = hg.compute_node(forward_mutual)
        samples = [MutualA(1, MutualB(2, MutualA(3))), None, MutualA(9)]
        phase = 'eval'
        raw = eval_node(node, samples)
        observations['mutual_snapshots'] = {'input': snapshot(samples), 'raw': snapshot(raw), 'received': received}
    except Exception as exc:
        observations['mutual_snapshots'] = {**error(exc), 'phase': phase, 'received': received}
    assert before == identity()
    return {'identity': before, 'observations': observations}


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
