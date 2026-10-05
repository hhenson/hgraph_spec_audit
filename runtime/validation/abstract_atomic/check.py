"""Check actual family publication while retaining authoring and construction gaps."""
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'atomic_snapshots'))
from provenance import validate_identity
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import sha


def member(values, name='First'):
    return {'type': name, 'values': values}


def paired(value):
    return [value, None, value]


def validate(evidence):
    assert evidence['repeats'] == 3 and type(evidence['repeats']) is int
    assert evidence['reasoned_sha256'] == sha(HERE / 'reasoned.json')
    assert evidence['harness_sha256'] == sha(HERE / 'observe.py')
    assert evidence['identity_helper_sha256'] == sha(HERE.parent / 'delta_eval/observe.py')
    assert set(evidence['engines']) == {'python', 'cpp'}
    for engine, result in evidence['engines'].items():
        validate_identity(result['identity'], engine)
    historical = evidence['engines']['python']['observations']
    assert historical == {'declaration': {'error_type': 'TypeError',
        'error': 'probe.<locals>.Family.__init_subclass__() takes no keyword arguments'}}
    cases = evidence['engines']['cpp']['observations']
    assert set(cases) == {'declaration', 'abstract_construction', 'snapshots', 'retention'}
    assert cases['declaration'] == {'accepted': True}
    # The native Python authoring surface admits an abstract dataclass construction.
    # This is recorded as a divergence from the source-language rule, not hidden.
    assert cases['abstract_construction'] == {'accepted': True}
    original, changed = member([1]), member([1, 2])
    values = [original, original, None, member([1], 'Second'), member([])]
    received = [value for value in values if value is not None]
    assert cases['snapshots'] == {'input': values, 'raw': values, 'received': received,
        'second_raw': values, 'second_received': received, 'first_after_second': values,
        'empty': None, 'silent': None}
    assert cases['retention'] == {'input': paired(original), 'raw': paired(original),
        'received': [original, original], 'first_after_source_mutation': paired(original),
        'first_after_second': paired(original), 'second_raw': paired(changed),
        'second_received': [changed, changed], 'first_after_capture_mutation': [member([1, 3]), None, original],
        'second_after_capture_mutation': paired(changed), 'source_after_capture_mutation': changed,
        'empty': None, 'silent': None}


if __name__ == '__main__':
    validate(json.loads((HERE / 'observed.json').read_text()))
    print('Abstract family publication checked; historical and native construction gaps retained.')
