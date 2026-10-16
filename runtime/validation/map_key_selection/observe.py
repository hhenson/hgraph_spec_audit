"""Observe frozen map selection rules through independent installed engines."""
import argparse
import contextlib
from datetime import datetime, timezone
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
SUPPORT = ('delta_eval/observe.py', 'fixed/reference_identity.py', 'fixed/native_identity.py')
spec = importlib.util.spec_from_file_location('support', HERE.parent / SUPPORT[0])
support = importlib.util.module_from_spec(spec)
spec.loader.exec_module(support)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def error_detail(error):
    message = str(error)
    for prefix in (str(HERE.parents[3]), sys.prefix, str(Path.home())):
        message = message.replace(prefix, '<private-path>')
    return {'error_type': type(error).__name__, 'error': message}


def selection(case):
    import hgraph as hg
    from hgraph.test import eval_node
    events = []

    @hg.compute_node(valid=('step',), active=('step',))
    def observe(reference: hg.REF[hg.TS[int]], data: hg.TS[int],
                book: hg.TSD[str, hg.TS[int]], key: hg.TS[str], step: hg.TS[int]) -> hg.TS[str]:
        row = [reference.valid, reference.modified, data.valid, data.modified,
               data.value if data.valid else None, bool(book.key_set.valid and key.value in book.key_set.value)]
        events.append(row)
        return json.dumps(row)

    @hg.compute_node(valid=('step',), active=('step',))
    def observe_held(reference: hg.REF[hg.TS[int]], data: hg.TS[int],
                     held: hg.TS[int], book: hg.TSD[str, hg.TS[int]],
                     key: hg.TS[str], step: hg.TS[int]) -> hg.TS[str]:
        row = [reference.valid, reference.modified, data.valid, data.modified,
               data.value if data.valid else None, bool(book.key_set.valid and key.value in book.key_set.value),
               held.valid, held.modified, held.value if held.valid else None]
        events.append(row)
        return json.dumps(row)

    class CaptureState(hg.CompoundScalar):
        saved: bool = False

    @hg.compute_node
    def first(reference: hg.REF[hg.TS[int]], data: hg.TS[int],
              _state: hg.STATE[CaptureState] = None) -> hg.REF[hg.TS[int]]:
        if not _state.saved:
            _state.saved = True
            return reference.value

    @hg.compute_node
    def mutable_map(step: hg.TS[int], _output: hg.OUT = None) -> hg.TSD[str, hg.TS[int]]:
        action = case['actions'][step.value]
        if action == 'create_invalid':
            _output.get_or_create('bid')
        elif action == 'invalidate_child':
            _output['bid'].invalidate()
        elif action == 'remove':
            _output.value = {'bid': hg.REMOVE}
        else:
            _output['bid'].value = 7 if action == 'publish_7' else 8

    @hg.graph
    def regular(values: hg.TSD[str, hg.TS[int]], key: hg.TS[str], step: hg.TS[int]) -> hg.TS[str]:
        selected = values[key]
        if case['kind'] == 'held_selection':
            return observe_held(selected, selected, first(selected, selected), values, key, step)
        return observe(selected, selected, values, key, step)

    @hg.graph
    def invalid_child(key: hg.TS[str], step: hg.TS[int]) -> hg.TS[str]:
        values = mutable_map(step)
        selected = values[key]
        return observe(selected, selected, values, key, step)

    try:
        if case['kind'] == 'invalid_child':
            raw = eval_node(invalid_child, case['key'], case['steps'])
        else:
            values = [None if row is None else
                      {key: hg.REMOVE if value == {'remove': True} else value
                       for key, value in row.items()} for row in case['map']]
            raw = eval_node(regular, values, case['key'], list(range(len(values))))
        return {'raw_eval_node': raw, 'events': events}
    except Exception as error:
        return {**error_detail(error), 'events': events}


def scalar_dictionary(corpus):
    import hgraph as hg
    from hgraph.test import eval_node
    observations = {}
    for mode in ('safe', 'fallback', 'strict_present', 'strict_missing'):
        events, failures = [], []
        def read(book, key):
            mapping, selected = book.value, key.value
            if mode == 'safe':
                value = {'present': selected in mapping, 'value': mapping.get(selected)}
            elif mode == 'fallback':
                value = mapping.get(selected, corpus['fallback'])
            else:
                try:
                    value = mapping[selected]
                except KeyError:
                    failures.append({'key': selected, 'error_type': 'KeyError', 'inside_node': True})
                    raise
            events.append(value)
            return json.dumps(value)
        read.__annotations__ = {'book': hg.TS[dict[str, int]], 'key': hg.TS[str], 'return': hg.TS[str]}
        samples = corpus['inputs']
        if mode == 'strict_present':
            samples = [samples[0], samples[2]]
        elif mode == 'strict_missing':
            samples = [samples[1]]
        try:
            node = hg.compute_node(read)
            raw = eval_node(node, samples, corpus['key'])
            observations[mode] = {'raw_eval_node': raw, 'events': events, 'failures': failures}
        except Exception as error:
            observations[mode] = {**error_detail(error), 'events': events, 'failures': failures}
    return observations


def probe():
    before = support.identity()
    corpus = json.loads((HERE / 'reasoned.json').read_text())
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        cases = {name: selection(case) for name, case in corpus['cases'].items()}
        scalar = scalar_dictionary(corpus['scalar_dictionary'])
    assert before == support.identity(), 'Installed engine changed during observation'
    return {'identity': before, 'cases': cases, 'scalar_dictionary': scalar}


def assess(run, corpus):
    result = {name: 'match' if actual.get('events') == corpus['cases'][name]['expected']
              and 'error_type' not in actual else 'divergence'
              for name, actual in run['cases'].items()}
    for mode, actual in run['scalar_dictionary'].items():
        if mode == 'strict_missing':
            matched = ('error_type' in actual and not actual['events']
                       and actual['failures'] == [{'key': 'bid', 'error_type': 'KeyError', 'inside_node': True}])
        else:
            matched = actual.get('events') == corpus['scalar_dictionary'][mode + '_expected'] and 'error_type' not in actual
        result['scalar_dictionary.' + mode] = 'match' if matched else 'divergence'
    return result


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
        assessment = assess(runs[0], corpus)
        result['engines'][name] = {**runs[0], 'runs_sha256': [digest(run) for run in runs], 'assessment': assessment}
        print(name, assessment)
    assert sources == {name: support.sha(HERE / name) for name in sources}
    assert dependencies == {name: support.sha(HERE.parent / name) for name in dependencies}
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + '\n')


if __name__ == '__main__':
    main()
