"""Compare the accepted empty-application rule with public reference engines."""
import argparse
import contextlib
from datetime import datetime, timezone
import importlib.util
import io
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
BASE = HERE.parent / 'publication_boundaries' / 'observe.py'
spec = importlib.util.spec_from_file_location('empty_boundary_support', BASE)
support = importlib.util.module_from_spec(spec)
spec.loader.exec_module(support)


def probe():
    before = support.identity()
    observations = {}
    for case in json.loads((HERE / 'reasoned.json').read_text())['cases']:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            observations[case['id']] = support.observe(case)
    if support.identity() != before:
        raise RuntimeError('Engine identity changed during observation')
    return {'identity': before, 'observations': observations}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--probe', action='store_true')
    parser.add_argument('--python', type=Path)
    parser.add_argument('--cpp', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.probe:
        print(json.dumps(probe(), sort_keys=True))
        return
    if not args.python or not args.cpp or not args.output or args.output.exists():
        parser.error('Supply independent interpreters and a new output file')
    paths = {'reasoned_sha256': HERE / 'reasoned.json',
             'harness_sha256': Path(__file__), 'boundary_support_sha256': BASE,
             'identity_support_sha256': HERE.parent / 'delta_eval' / 'observe.py'}
    hashes = {key: support.sha(path) for key, path in paths.items()}
    evidence = {'measured_at': datetime.now(timezone.utc).isoformat(), **hashes,
                'repeats': 3, 'engines': {}}
    cases = json.loads((HERE / 'reasoned.json').read_text())['cases']
    for name, executable, native in [('python', args.python, False), ('cpp', args.cpp, True)]:
        runs = [json.loads(subprocess.check_output([str(executable.absolute()), __file__, '--probe'],
                     text=True).strip().splitlines()[-1]) for _ in range(3)]
        if any(run != runs[0] for run in runs) or runs[0]['identity']['native'] != native:
            raise RuntimeError(name + ': unstable observations or wrong engine')
        result = runs[0]
        result['assessment'] = {case['id']: support.assess(case, result['observations'][case['id']])
                                for case in cases}
        evidence['engines'][name] = result
        print(name, {case['id']: result['observations'][case['id']]['capability']
                     for case in cases})
    if hashes != {key: support.sha(path) for key, path in paths.items()}:
        raise RuntimeError('Evidence inputs changed during execution')
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')


if __name__ == '__main__':
    main()
