"""Check enum publication identity and preserve raw no-output behavior."""
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'atomic_snapshots'))
from provenance import validate_identity
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import sha

PATTERNS = {'equal_distinct': ['first', 'first', 'second', 'third'],
            'silence': [None, 'first', None, 'second', None],
            'all_silent': [None, None], 'empty': []}
MEMBERS = {'first': -7, 'second': 11, 'third': 9223372036854775807}
CONTROLS = {'same_member_equal': True, 'different_member_equal': False,
            'other_enum_equal': False, 'integer_equal': False}


def validate(evidence):
    reasoned = json.loads((HERE / 'reasoned.json').read_text())
    assert reasoned['patterns'] == PATTERNS and reasoned['members'] == MEMBERS
    assert reasoned['controls'] == CONTROLS
    assert evidence['repeats'] == 3 and type(evidence['repeats']) is int
    assert evidence['reasoned_sha256'] == sha(HERE / 'reasoned.json')
    assert evidence['harness_sha256'] == sha(HERE / 'observe.py')
    assert evidence['identity_helper_sha256'] == sha(HERE.parent / 'delta_eval/observe.py')
    assert set(evidence['engines']) == {'python', 'cpp'}
    for engine, result in evidence['engines'].items():
        validate_identity(result['identity'], engine)
        observed = result['observations']
        assert observed['controls'] == CONTROLS
        assert set(observed['cases']) == set(PATTERNS)
        for name, tokens in PATTERNS.items():
            values = [None if member is None else {'type': 'Mode', 'name': member,
                      'number': MEMBERS[member]} for member in tokens]
            raw = values if any(v is not None for v in values) else None
            received = [{'value': v, 'delta': v} for v in values if v is not None]
            assert observed['cases'][name] == {'raw': raw, 'received': received,
                                               'second_raw': raw, 'second_received': received,
                                               'first_after_second': raw}


if __name__ == '__main__':
    validate(json.loads((HERE / 'observed.json').read_text()))
    print('Four enum traces per engine match; exact enum identity and raw silence preserved.')
