"""Observe publication effects of nullable replay slots, not HGL source syntax."""
import argparse
import contextlib
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import subprocess
from observe import identity, observe, sha

HERE = Path(__file__).resolve().parent
CORPUS = HERE / 'indexing_reasoned.json'


def probe():
    before = identity()
    observations = {}
    for case in json.loads(CORPUS.read_text())['cases']:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            observations[case['id']] = observe(case)
    if before != identity():
        raise RuntimeError('engine identity changed during observation')
    return {'identity_sha256': before['package']['identity_sha256'],
            'native': before['native'], 'observations': observations}


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
        parser.error('independent interpreters and a new output are required')
    corpus_hash = sha(CORPUS)
    cases = json.loads(CORPUS.read_text())['cases']
    evidence = {'measured_at': datetime.now(timezone.utc).isoformat(),
                'reasoned_sha256': corpus_hash, 'harness_sha256': sha(__file__),
                'observer_sha256': sha(HERE / 'observe.py'), 'repeats': 3, 'engines': {}}
    for name, executable, native in [('python', args.python, False), ('cpp', args.cpp, True)]:
        runs = [json.loads(subprocess.check_output([str(executable.absolute()), __file__, '--probe'],
                        text=True).strip().splitlines()[-1]) for _ in range(3)]
        if any(run != runs[0] for run in runs) or runs[0]['native'] != native:
            raise RuntimeError(name + ': unstable observations or incorrect engine')
        result = runs[0]
        result['assessment'] = {case['id']: 'match' if
            result['observations'][case['id']]['dense_from_input_horizon'] == case['expected']
            else 'divergence' for case in cases}
        evidence['engines'][name] = result
    if sha(CORPUS) != corpus_hash:
        raise RuntimeError('expectations changed during observation')
    args.output.write_text(json.dumps(evidence, sort_keys=True, indent=2) + '\n')
    for name, result in evidence['engines'].items():
        print(name, result['assessment'])


if __name__ == '__main__':
    main()
