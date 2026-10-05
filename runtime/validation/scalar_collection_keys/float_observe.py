"""Observe IEEE key boundaries without inferring a NaN source contract."""
import argparse
import contextlib
from datetime import datetime, timezone
import io
import json
import math
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import identity, sha


def key(v):
    assert type(v) is float
    if math.isnan(v):
        return 'nan'
    if math.isinf(v):
        return '+inf' if v > 0 else '-inf'
    assert v == 0.0
    return '-0' if math.copysign(1.0, v) < 0 else '+0'


def probe():
    import hgraph as hg
    from hgraph.test import eval_node
    before = identity()
    observations = {}
    for case in ('signed_zero', 'infinities', 'nan'):
        observations[case] = {}
        for family in ('set', 'map'):
            a, b = (0.0, -0.0) if case == 'signed_zero' else ((float('inf'), float('-inf')) if case == 'infinities' else (float('nan'), float('nan')))
            received = []
            observations[case]['a_equals_b'] = a == b
            observations[case]['a_equals_self'] = a == a
            observations[case]['equal_hashes'] = hash(a) == hash(b)
            try:
                if family == 'set':
                    schema = hg.TSS[float]
                    samples = [{a}, {b}, {hg.Removed(a)}] if case == 'signed_zero' else [{a, b}, {hg.Removed(a)}]
                    def encode(v):
                        if v is None:
                            return None
                        return {'add': sorted(key(x) for x in v.added), 'remove': sorted(key(x) for x in v.removed)}
                    def held(v):
                        return sorted(key(x) for x in v)
                else:
                    schema = hg.TSD[float, hg.TS[int]]
                    samples = [{a: 10}, {b: 20}, {a: hg.REMOVE}] if case == 'signed_zero' else [{a: 10, b: 20}, {a: hg.REMOVE}]
                    def encode(v):
                        if v is None:
                            return None
                        return {'upsert': sorted([key(k), x] for k, x in v.items() if x is not hg.REMOVE),
                                'remove': sorted(key(k) for k, x in v.items() if x is hg.REMOVE)}
                    def held(v):
                        return sorted([key(k), x] for k, x in v.items())
                def forward(value):
                    received.append({'delta': encode(value.delta_value), 'held': held(value.value)})
                    return value.delta_value
                forward.__annotations__ = {'value': schema, 'return': schema}
                raw = eval_node(hg.compute_node(forward), samples)
                observations[case][family] = {'raw': None if raw is None else [encode(v) for v in raw], 'received': received}
            except Exception as exc:
                message = str(exc).replace(str(HERE.parents[2]), '<audit-root>').replace(sys.prefix, '<environment>').replace(str(Path.home()), '<private-home>')
                observations[case][family] = {'error_type': type(exc).__name__, 'error': message, 'received': received}
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
                'reasoned_sha256': sha(HERE / 'float_reasoned.json'), 'harness_sha256': sha(__file__),
                'identity_helper_sha256': sha(HERE.parent / 'delta_eval/observe.py'), 'engines': {}}
    for engine, executable in [('python', args.python), ('cpp', args.cpp)]:
        runs = [json.loads(subprocess.check_output([str(executable), __file__, '--probe'], text=True, timeout=30)) for _ in range(3)]
        assert all(run == runs[0] for run in runs), 'unstable observations'
        assert runs[0]['identity']['native'] == (engine == 'cpp')
        evidence['engines'][engine] = runs[0]
        print(engine, json.dumps(runs[0]['observations'], sort_keys=True))
    assert evidence['reasoned_sha256'] == sha(HERE / 'float_reasoned.json')
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')


if __name__ == '__main__':
    main()
