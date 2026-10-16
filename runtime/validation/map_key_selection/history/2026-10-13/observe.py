"""Capture graph map-selection metadata using independent installed engines."""
import argparse
import contextlib
from datetime import datetime, timezone
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
SUPPORT = ('delta_eval/observe.py', 'fixed/reference_identity.py', 'fixed/native_identity.py')
spec = importlib.util.spec_from_file_location('support', HERE.parent / SUPPORT[0])
support = importlib.util.module_from_spec(spec)
spec.loader.exec_module(support)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def measure(case):
    import hgraph as hg
    from hgraph.test import eval_node

    events = []

    @hg.compute_node(valid=('step',), active=('step',))
    def observe(reference: hg.REF[hg.TS[int]], data: hg.TS[int], step: hg.TS[int]) -> hg.TS[str]:
        row = [reference.valid, reference.modified, data.valid, data.modified,
               data.value if data.valid else None]
        events.append(row)
        return json.dumps(row)

    @hg.graph
    def select(values: hg.TSD[str, hg.TS[int]], key: hg.TS[str], step: hg.TS[int]) -> hg.TS[str]:
        selected = values[key]
        return observe(selected, selected, step)

    values = [None if row is None else
              {key: hg.REMOVE if value == {'remove': True} else value
               for key, value in row.items()} for row in case['map']]
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        raw = eval_node(select, values, case['key'], [1] * len(case['map']))
    return {'raw': raw, 'events': events}


def probe():
    identity = support.identity()
    corpus = json.loads((HERE / 'reasoned.json').read_text())
    cases = {name: measure(case) for name, case in corpus['cases'].items()}
    mapping = {'bid': 10}
    try:
        mapping['missing']
    except KeyError as error:
        missing_error = type(error).__name__
    scalar = {'present': mapping['bid'], 'missing_error': missing_error,
              'missing_default': mapping.get('missing', None)}
    assert identity == support.identity(), 'Installed engine changed during observation'
    return {'identity': identity, 'cases': cases, 'scalar_dictionary': scalar}


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
        parser.error('Independent interpreters and a new output destination are required')
    sources = {name: support.sha(HERE / name) for name in ('reasoned.json', 'observe.py')}
    dependencies = {name: support.sha(HERE.parent / name) for name in SUPPORT}
    result = {'measured_at': datetime.now(timezone.utc).isoformat(), 'repeats': 3,
              'sources_sha256': sources, 'support_sha256': dependencies, 'engines': {}}
    corpus = json.loads((HERE / 'reasoned.json').read_text())
    for name, executable, native in [('python', args.python, False), ('cpp', args.cpp, True)]:
        runs = [json.loads(subprocess.check_output(
            [str(executable.absolute()), __file__, '--probe'], text=True, timeout=120)
            .strip().splitlines()[-1]) for _ in range(3)]
        assert all(run == runs[0] for run in runs), 'Fresh processes disagree'
        assert runs[0]['identity']['native'] == native, 'Wrong engine artifact'
        assessments = {key: 'match' if value['events'] == corpus['cases'][key]['expected']
                       else 'divergence' for key, value in runs[0]['cases'].items()}
        result['engines'][name] = {**runs[0], 'runs_sha256': [digest(run) for run in runs],
                                   'assessment': assessments}
        print(name, assessments)
    assert sources == {name: support.sha(HERE / name) for name in sources}
    assert dependencies == {name: support.sha(HERE.parent / name) for name in dependencies}
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + '\n')


if __name__ == '__main__':
    main()
