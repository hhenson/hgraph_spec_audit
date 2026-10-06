"""Measure dynamic TSL delta forwarding without substituting fixed lists."""
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
    import hgraph as hg
    if v is None:
        return None
    if v is hg.REMOVE:
        return {'remove': True}
    if isinstance(v, dict):
        return {str(k): snapshot(x) for k, x in v.items()}
    if isinstance(v, (set, frozenset)):
        return sorted(v)
    if isinstance(v, (list, tuple)):
        return [snapshot(x) for x in v]
    if type(v) in (int, bool, str):
        return v
    raise TypeError(type(v).__name__)


def probe():
    import hgraph as hg
    from hgraph.test import eval_node
    before = identity()
    observations = {}
    for case, samples in json.loads((HERE / 'reasoned.json').read_text())['cases'].items():
        received = []
        try:
            size = hg.Size[-1] if before['native'] else hg.Size
            schema = hg.TSL[hg.TS[int], size]
            def forward(value):
                delta = value.delta_value
                received.append({'value': snapshot(value.value), 'delta': snapshot(delta),
                                 'valid': value.valid, 'all_valid': value.all_valid})
                return delta
            forward.__annotations__ = {'value': schema, 'return': schema}
            raw = eval_node(hg.compute_node(forward), samples)
            observations[case] = {'raw': snapshot(raw), 'received': received}
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
