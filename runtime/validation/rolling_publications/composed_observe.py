"""Measure actual to_window then TSW pass-through and scalar observation."""
import argparse
import contextlib
from collections import deque
from datetime import datetime, timedelta, timezone
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
    if hasattr(v, 'tolist'):
        return snapshot(v.tolist())
    if isinstance(v, (list, tuple, deque)):
        return [snapshot(x) for x in v]
    if isinstance(v, datetime):
        return v.isoformat()
    if type(v) in (int, float, bool, str):
        return v
    raise TypeError(type(v).__name__)


def probe():
    import hgraph as hg
    from hgraph.test import eval_node
    before = identity()
    observations = {}
    for case, data in json.loads((HERE / 'composed_reasoned.json').read_text())['cases'].items():
        received = []
        try:
            maximum = data['max'] if 'max' in data else timedelta(microseconds=data['max_us'])
            minimum = data['min'] if 'min' in data else timedelta(microseconds=data['min_us'])
            schema = hg.TSW[int, hg.WindowSize[maximum], hg.WindowSize[minimum]]
            def capture(label, value):
                received.append({'endpoint': label, 'value': snapshot(value.value),
                                 'delta': snapshot(value.delta_value),
                                 'valid': value.valid, 'all_valid': value.all_valid,
                                 'value_times': snapshot(value.value_times)})
            def forward(value):
                capture('input', value)
                return value.delta_value
            forward.__annotations__ = {'value': schema, 'return': schema}
            node = hg.compute_node(forward)
            def consume(value):
                capture('output', value)
                return value.delta_value
            consume.__annotations__ = {'value': schema, 'return': hg.TS[int]}
            consumer = hg.compute_node(consume)
            def pipeline(value):
                window = hg.to_window(value, period=maximum, min_window_period=minimum)
                return consumer(node(window))
            pipeline.__annotations__ = {'value': hg.TS[int], 'return': hg.TS[int]}
            raw = eval_node(hg.graph(pipeline), data['inputs'])
            observations[case] = {'raw': snapshot(raw), 'received': received}
        except Exception as exc:
            message = str(exc).replace(str(HERE.parents[2]), '<audit-root>').replace(sys.prefix, '<environment>').replace(str(Path.home()), '<private-home>')
            cause = "Expected <class 'int'>, got <class 'numpy.int64'>"
            if cause in message:
                # Native repr includes process-specific subscriber IDs and
                # uninitialized unused numpy slots. Retain the exact type
                # mismatch and phase, not that volatile diagnostic repr.
                message = 'TSW output application: ' + cause
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
                'reasoned_sha256': sha(HERE / 'composed_reasoned.json'), 'harness_sha256': sha(__file__),
                'identity_helper_sha256': sha(HERE.parent / 'delta_eval/observe.py'), 'engines': {}}
    for engine, executable in [('python', args.python), ('cpp', args.cpp)]:
        runs = [json.loads(subprocess.check_output([str(executable), __file__, '--probe'], text=True, timeout=30)) for _ in range(3)]
        assert all(run == runs[0] for run in runs), 'unstable observations'
        assert runs[0]['identity']['native'] == (engine == 'cpp')
        evidence['engines'][engine] = runs[0]
        print(engine, json.dumps(runs[0]['observations'], sort_keys=True))
    assert evidence['reasoned_sha256'] == sha(HERE / 'composed_reasoned.json')
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')


if __name__ == '__main__':
    main()
