"""Check complete publications while retaining Python alias and native-view limits."""
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'atomic_snapshots'))
from provenance import validate_identity
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import sha


def received(values):
    return [{'value': v, 'delta': v} for v in values if v is not None]


def captures(value):
    return [value, None, value]


def validate(evidence):
    assert evidence['repeats'] == 3 and type(evidence['repeats']) is int
    assert evidence['reasoned_sha256'] == sha(HERE / 'reasoned.json')
    assert evidence['harness_sha256'] == sha(HERE / 'observe.py')
    assert evidence['identity_helper_sha256'] == sha(HERE.parent / 'delta_eval/observe.py')
    assert set(evidence['engines']) == {'python', 'cpp'}
    for engine, result in evidence['engines'].items():
        validate_identity(result['identity'], engine)
        cases = result['observations']
        assert set(cases) == {'set_snapshots', 'map_snapshots', 'set_retention', 'map_list_retention'}
        for case, values in {
            'set_snapshots': [{'set': [1, 2]}, {'set': []}, None, {'set': []}, {'set': [3]}],
            'map_snapshots': [{'map': [['a', 1], ['b', 2]]}, {'map': []}, None, {'map': []}, {'map': [['a', 3]]}]
        }.items():
            assert cases[case] == {'input': values, 'raw': values, 'received': received(values),
                                   'second_raw': values, 'second_received': received(values),
                                   'first_after_second': values}
        for case in ('set_retention', 'map_list_retention'):
            if case == 'set_retention':
                old, new, mutated = {'set': [1]}, {'set': [1, 2]}, {'set': [1, 2, 4]}
                native_capture = old
            else:
                old = {'map': [['a', [1]]]}
                new = {'map': [['a', [1, 2]], ['b', [3]]]}
                mutated = {'map': [['a', [1, 2, 4]], ['b', [3]]]}
                native_capture = {'map': [['a', [1, 4]]]}
            expected = {'input': captures(old), 'raw': captures(old), 'received': received(captures(old)),
                        'second_raw': captures(new), 'second_received': received(captures(new))}
            if engine == 'python':
                expected.update(first_after_source_mutation=captures(new), first_after_second=captures(new),
                                first_after_capture_mutation=captures(mutated),
                                second_after_capture_mutation=captures(mutated), source_after_capture_mutation=mutated)
            else:
                expected.update(first_after_source_mutation=captures(old), first_after_second=captures(old),
                                first_after_capture_mutation=[native_capture, None, old],
                                second_after_capture_mutation=captures(new), source_after_capture_mutation=new)
                if case == 'set_retention':
                    expected['capture_mutation_error'] = {'error_type': 'AttributeError',
                                                          'error': "'frozenset' object has no attribute 'add'"}
            assert cases[case] == expected, (engine, case)


if __name__ == '__main__':
    validate(json.loads((HERE / 'observed.json').read_text()))
    print('Complete set/map publications checked; Python aliasing and native immutable set boundary retained.')
