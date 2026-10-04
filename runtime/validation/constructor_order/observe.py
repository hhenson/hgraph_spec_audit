"""Measure Python CompoundScalar constructor argument order, preserving failures."""
import argparse
import contextlib
from dataclasses import dataclass
from datetime import datetime, timezone
import inspect
import io
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import identity, sha


def probe():
    from hgraph import CompoundScalar
    before = identity()

    @dataclass
    class Pair(CompoundScalar):
        left: int
        right: int

    trace = []

    def mark(value):
        trace.append(value)
        return value

    pair = Pair(right=mark(2), left=mark(1))
    result = {'reversed_keywords': {'trace': list(trace), 'left': pair.left, 'right': pair.right}}
    trace.clear()

    def fail(value):
        trace.append(value)
        raise ValueError('first argument failed')

    try:
        Pair(right=fail(2), left=mark(1))
        result['first_argument_failure'] = {'trace': list(trace), 'constructed': True}
    except Exception as exc:
        result['first_argument_failure'] = {
            'trace': list(trace), 'constructed': False,
            'error_type': type(exc).__name__, 'error': str(exc)}
    if identity() != before:
        raise RuntimeError('engine artifacts changed during observation')
    return {'identity': before, 'compound_scalar_module': CompoundScalar.__module__,
            'compound_scalar_source_sha256': sha(inspect.getfile(CompoundScalar)), 'observed': result}


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
        parser.error('supply independent interpreters and a new output destination')
    corpus = HERE / 'reasoned.json'
    corpus_hash = sha(corpus)
    expected = json.loads(corpus.read_text())['expected']
    evidence = {'measured_at': datetime.now(timezone.utc).isoformat(), 'repeats': 3,
                'reasoned_sha256': corpus_hash, 'harness_sha256': sha(__file__),
                'identity_helper_sha256': sha(HERE.parent / 'delta_eval/observe.py'), 'engines': {}}
    for name, exe in [('python', args.python), ('cpp', args.cpp)]:
        runs = [json.loads(subprocess.check_output(
            [str(exe.absolute()), __file__, '--probe'], text=True).strip().splitlines()[-1]) for _ in range(3)]
        if any(run != runs[0] for run in runs):
            raise RuntimeError(name + ' fresh-process observations are unstable')
        result = runs[0]
        if result['identity']['native'] != (name == 'cpp'):
            raise RuntimeError(name + ' has wrong engine identity')
        result['assessment'] = {key: 'match' if result['observed'][key] == value else 'divergence'
                                for key, value in expected.items()}
        evidence['engines'][name] = result
    if sha(corpus) != corpus_hash:
        raise RuntimeError('expectations changed during measurement')
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')
    for name, result in evidence['engines'].items():
        print(name, result['assessment'])


if __name__ == '__main__':
    main()
