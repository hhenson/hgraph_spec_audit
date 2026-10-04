"""Preserve the distinction between zone syntax and exact provider membership."""
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'atomic_snapshots'))
from provenance import validate_identity

ACCEPTED = {'UTC': 0, 'Etc/UTC': 0, 'America/New_York': -14400, 'US/Eastern': -14400}
REJECTED = ['utc', 'america/new_york', 'Etc/Unknown', 'Missing/Zone']


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def same(actual, expected):
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True), (actual, expected)


def validate(reasoned, evidence):
    assert reasoned['written_before_measurement'] is True
    cases = {name: {'provider_accepts': True, 'offset_seconds': offset} for name, offset in ACCEPTED.items()}
    cases.update({name: {'provider_accepts': False} for name in REJECTED})
    same(reasoned['cases'], cases)
    assert evidence['reasoned_sha256'] == sha(HERE / 'reasoned.json')
    assert evidence['harness_sha256'] == sha(HERE / 'observe.py')
    assert evidence['identity_helper_sha256'] == sha(HERE.parent / 'delta_eval/observe.py')
    assert type(evidence['repeats']) is int and evidence['repeats'] == 3
    assert set(evidence['engines']) == {'python', 'cpp'}
    for engine, result in evidence['engines'].items():
        validate_identity(result['identity'], engine)
        same(result['observations']['@availability'],
             {'exports': {'ZoneId': engine == 'cpp', 'ZonedDateTime': engine == 'cpp'}})
    assert set(evidence['engines']['python']['observations']) == {'@availability'}
    observations = evidence['engines']['cpp']['observations']
    assert set(observations) == set(cases) | {'@availability'}
    for name in cases:
        expected = {phase: {'status': 'success', 'value': name} for phase in
                    ('constructor_without_provider', 'constructor_with_provider',
                     'json_without_provider', 'json_with_provider')}
        expected['equal_to_new_york'] = name == 'America/New_York'
        expected['at_zone_with_provider'] = (
            {'status': 'success', 'value': {'instant': '2026-09-03T09:30:00', 'zone': name,
                                          'offset_seconds': ACCEPTED[name]}} if name in ACCEPTED else
            {'status': 'error', 'error_type': 'ValueError', 'error_message': 'unknown time-zone identifier'})
        same(observations[name], expected)
    print('Eight exact-name probes checked: syntax/ad-hoc JSON accept all; provider rejects four; no Python parity claim.')


def main():
    validate(json.loads((HERE / 'reasoned.json').read_text()), json.loads((HERE / 'observed.json').read_text()))


if __name__ == '__main__':
    main()
