"""Measure declared enum delta publications with each actual eval recorder."""
import argparse
import contextlib
from datetime import datetime, timezone
from enum import Enum
import io
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import identity, sha


class Mode(Enum):
    first = -7
    second = 11
    third = 9223372036854775807


class OtherMode(Enum):
    first = -7


def snapshot(value):
    if value is None:
        return None
    if isinstance(value, list):
        return [snapshot(v) for v in value]
    if isinstance(value, Enum):
        return {'type': type(value).__qualname__, 'name': value.name, 'number': value.value}
    raise TypeError(type(value).__qualname__)


def probe():
    import hgraph as hg
    from hgraph.test import eval_node
    before = identity()
    reasoned = json.loads((HERE / 'reasoned.json').read_text())
    observed = {'controls': {'same_member_equal': Mode.first == Mode.first,
                            'different_member_equal': Mode.first == Mode.second,
                            'other_enum_equal': Mode.first == OtherMode.first,
                            'integer_equal': Mode.first == -7}, 'cases': {}}
    for name, tokens in reasoned['patterns'].items():
        samples = [None if t is None else Mode[t] for t in tokens]
        received = []
        def forward(value):
            received.append({'value': snapshot(value.value), 'delta': snapshot(value.delta_value)})
            return value.delta_value
        forward.__annotations__ = {'value': hg.TS[Mode], 'return': hg.TS[Mode]}
        try:
            node = hg.compute_node(forward)
            raw = eval_node(node, samples)
            saved = snapshot(raw)
            first_received = list(received)
            received.clear()
            second = eval_node(node, samples)
            observed['cases'][name] = {'raw': saved, 'received': first_received,
                                       'second_raw': snapshot(second),
                                       'second_received': received,
                                       'first_after_second': snapshot(raw)}
        except Exception as exc:
            message = str(exc).replace(str(HERE.parents[2]), '<audit-root>')
            message = message.replace(sys.prefix, '<environment>').replace(str(Path.home()), '<private-home>')
            observed['cases'][name] = {'error_type': type(exc).__name__, 'error': message}
    assert before == identity()
    return {'identity': before, 'observations': observed}


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
        runs = [json.loads(subprocess.check_output([str(executable), __file__, '--probe'],
                                                   text=True, timeout=30)) for _ in range(3)]
        assert all(run == runs[0] for run in runs), 'unstable observations'
        assert runs[0]['identity']['native'] == (engine == 'cpp')
        evidence['engines'][engine] = runs[0]
        print(engine, json.dumps(runs[0]['observations'], sort_keys=True))
    assert evidence['reasoned_sha256'] == sha(HERE / 'reasoned.json')
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')


if __name__ == '__main__':
    main()
