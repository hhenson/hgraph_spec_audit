"""Measure canonical ZonedTime availability, without substitute graph values."""
import argparse
from datetime import datetime, timezone
import importlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import identity, sha


def probe():
    before = identity()
    observations = {}
    for name in ('hgraph', 'hgraph.temporal', '_hgraph'):
        try:
            module = importlib.import_module(name)
        except ModuleNotFoundError as exc:
            # Do not misclassify a broken dependency as an absent surface.
            assert exc.name == name
            observations[name] = {'module_available': False}
        else:
            observations[name] = {'module_available': True,
                                  'ZonedTime_exported': hasattr(module, 'ZonedTime')}
    assert before == identity()
    return {'identity': before, 'surfaces': observations,
            'graph_cases_executed': False}


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
        parser.error('two interpreters and a new output path required')
    evidence = {'measured_at': datetime.now(timezone.utc).isoformat(), 'repeats': 3,
                'reasoned_sha256': sha(HERE / 'reasoned.json'),
                'harness_sha256': sha(__file__),
                'identity_helper_sha256': sha(HERE.parent / 'delta_eval/observe.py'),
                'engines': {}}
    for engine, executable in [('python', args.python), ('cpp', args.cpp)]:
        runs = [json.loads(subprocess.check_output([str(executable), __file__, '--probe'],
                                                   text=True, timeout=30)) for _ in range(3)]
        assert all(run == runs[0] for run in runs), 'unstable observations'
        assert runs[0]['identity']['native'] == (engine == 'cpp')
        evidence['engines'][engine] = runs[0]
    assert evidence['reasoned_sha256'] == sha(HERE / 'reasoned.json')
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')
    print('Six fresh-process availability probes; zero graph cases executed.')


if __name__ == '__main__':
    main()
