"""Measure complete ordinary set/map publication and retained ownership."""
import argparse
import contextlib
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import identity, sha


def snapshot(v):
    if v is None:
        return None
    if isinstance(v, dict):
        return {'map': [[k, snapshot(x)] for k, x in sorted(v.items())]}
    if isinstance(v, (set, frozenset)):
        return {'set': sorted(v)}
    if isinstance(v, list):
        return [snapshot(x) for x in v]
    assert type(v) is int
    return v


def probe():
    import hgraph as hg
    from hgraph.test import eval_node
    before = identity()
    observations = {}
    for case in json.loads((HERE / 'reasoned.json').read_text())['cases']:
        received = []
        if case == 'set_snapshots':
            scalar, samples = set[int], [{1, 2}, set(), None, set(), {3}]
        elif case == 'map_snapshots':
            scalar, samples = dict[str, int], [{'a': 1, 'b': 2}, {}, None, {}, {'a': 3}]
        elif case == 'set_retention':
            shared = {1}
            scalar, samples = set[int], [shared, None, shared]
        else:
            shared = {'a': [1]}
            scalar, samples = dict[str, list[int]], [shared, None, shared]
        def forward(value):
            received.append({'value': snapshot(value.value), 'delta': snapshot(value.delta_value)})
            return value.delta_value
        forward.__annotations__ = {'value': hg.TS[scalar], 'return': hg.TS[scalar]}
        try:
            node = hg.compute_node(forward)
            observed = {'input': snapshot(samples)}
            raw = eval_node(node, samples)
            observed.update(raw=snapshot(raw), received=list(received))
            if case.endswith('retention'):
                if case == 'set_retention':
                    shared.add(2)
                else:
                    shared['a'].append(2)
                    shared['b'] = [3]
                observed['first_after_source_mutation'] = snapshot(raw)
            received.clear()
            second = eval_node(node, samples)
            observed.update(second_raw=snapshot(second), second_received=list(received),
                            first_after_second=snapshot(raw))
            if case.endswith('retention'):
                if case == 'set_retention':
                    try:
                        raw[0].add(4)
                    except AttributeError as exc:
                        observed['capture_mutation_error'] = {'error_type': type(exc).__name__, 'error': str(exc)}
                else:
                    raw[0]['a'].append(4)
                observed.update(first_after_capture_mutation=snapshot(raw),
                                second_after_capture_mutation=snapshot(second),
                                source_after_capture_mutation=snapshot(shared))
            observations[case] = observed
        except Exception as exc:
            message = str(exc).replace(str(HERE.parents[2]), '<audit-root>').replace(sys.prefix, '<environment>').replace(str(Path.home()), '<private-home>')
            observations[case] = {'error_type': type(exc).__name__, 'error': message, 'received': received}
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
