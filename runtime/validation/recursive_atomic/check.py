"""Check finite recursive publications while preserving historical deep aliases."""
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'atomic_snapshots'))
from provenance import validate_identity
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import sha


def chain(values, child=None):
    return {'type': 'Chain', 'values': values, 'next': child}


def deep(tail):
    return chain([1], chain([2], chain(tail)))


def paired(root):
    return [root, None, root]


def validate(evidence):
    assert evidence['repeats'] == 3 and type(evidence['repeats']) is int
    assert evidence['reasoned_sha256'] == sha(HERE / 'reasoned.json')
    assert evidence['harness_sha256'] == sha(HERE / 'observe.py')
    assert evidence['identity_helper_sha256'] == sha(HERE.parent / 'delta_eval/observe.py')
    assert set(evidence['engines']) == {'python', 'cpp'}
    original, changed, native_capture, aliased = deep([3]), deep([3, 4]), deep([3, 5]), deep([3, 4, 5])
    values = [original, original, None, chain([9])]
    received = [v for v in values if v is not None]
    mutual = [{'type': 'MutualA', 'value': 1, 'other': {'type': 'MutualB', 'value': 2,
               'other': {'type': 'MutualA', 'value': 3, 'other': None}}}, None,
              {'type': 'MutualA', 'value': 9, 'other': None}]
    for engine, result in evidence['engines'].items():
        validate_identity(result['identity'], engine)
        cases = result['observations']
        assert set(cases) == {'self_snapshots', 'self_retention', 'mutual_snapshots'}
        assert cases['self_snapshots'] == {'input': values, 'raw': values, 'received': received,
                'second_raw': values, 'second_received': received, 'first_after_second': values,
                'empty': None, 'silent': None}
        assert cases['mutual_snapshots'] == {'input': mutual, 'raw': mutual,
                                            'received': [v for v in mutual if v is not None]}
        expected = {'input': paired(original), 'raw': paired(original), 'received': [original, original],
                    'second_raw': paired(changed), 'second_received': [changed, changed],
                    'empty': None, 'silent': None}
        if engine == 'cpp':
            expected.update(first_after_source_mutation=paired(original), first_after_second=paired(original),
                            first_after_capture_mutation=[native_capture, None, original],
                            second_after_capture_mutation=paired(changed), source_after_capture_mutation=changed)
        else:
            expected.update(first_after_source_mutation=paired(changed), first_after_second=paired(changed),
                            first_after_capture_mutation=paired(aliased),
                            second_after_capture_mutation=paired(aliased), source_after_capture_mutation=aliased)
        assert cases['self_retention'] == expected, engine


if __name__ == '__main__':
    validate(json.loads((HERE / 'observed.json').read_text()))
    print('Recursive self/mutual publications checked; Python deep aliases retained.')
