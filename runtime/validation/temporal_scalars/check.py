"""Check bounded native measurements and reject invented reference coverage."""
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'atomic_snapshots'))
from provenance import validate_identity

SCOPE = ['civil_datetime', 'timezone', 'zoned_datetime']
PATTERNS = {'equal_distinct': ['a', 'a', 'b', 'a'],
            'silence': [None, 'a', None, 'a', 'b', None],
            'all_silent': [None, None, None], 'empty': []}
EXTRAS = ['zone_alias', 'same_instant_different_zone'] + [k + '_retention' for k in SCOPE]
VALUES = {
    'civil_datetime': ({'civil_datetime': "CivilDateTime('1970-01-01T00:00:00')"},
                       {'civil_datetime': "CivilDateTime('2026-09-03T10:30:00')"}),
    'timezone': ({'timezone': 'UTC'}, {'timezone': 'Europe/London'}),
    'zoned_datetime': ({'instant': '2026-09-03T09:30:00', 'zone': 'UTC', 'offset_seconds': 0},
                       {'instant': '2026-09-03T09:30:00', 'zone': 'Europe/London', 'offset_seconds': 3600}),
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def same(actual, expected):
    assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True), (actual, expected)


def received(values):
    return [{'value': v, 'delta': v} for v in values if v is not None]


def validate(reasoned, evidence):
    assert reasoned['written_before_measurement'] is True
    same(reasoned['scope'], SCOPE)
    same(reasoned['patterns'], PATTERNS)
    same(reasoned['extra_cases'], EXTRAS)
    assert reasoned['spec_baseline'] == '73f03bfa77349bfa284a23eb781e4c79c85eff8a'
    assert evidence['reasoned_sha256'] == sha(HERE / 'reasoned.json')
    assert evidence['harness_sha256'] == sha(HERE / 'observe.py')
    assert evidence['identity_helper_sha256'] == sha(HERE.parent / 'delta_eval/observe.py')
    assert type(evidence['repeats']) is int and evidence['repeats'] == 3
    assert set(evidence['engines']) == {'python', 'cpp'}
    for engine, result in evidence['engines'].items():
        validate_identity(result['identity'], engine)
        exports = {'CivilDateTime': engine == 'cpp', 'ZoneId': engine == 'cpp',
                   'ZonedDateTime': engine == 'cpp', 'ZonedTime': False}
        same(result['observations']['availability'], {'exports': exports})
    assert set(evidence['engines']['python']['observations']) == {'availability'}
    observations = evidence['engines']['cpp']['observations']
    case_ids = [k + '_' + p for k in SCOPE for p in PATTERNS] + EXTRAS
    assert set(observations) == set(case_ids) | {'availability', 'provider'}
    for name in case_ids:
        if name == 'zone_alias':
            a, b = {'timezone': 'US/Eastern'}, {'timezone': 'America/New_York'}
            inputs = [a, b, a]
        elif name == 'same_instant_different_zone':
            a, b = VALUES['zoned_datetime']
            inputs = [a, b, a]
        else:
            kind, pattern = next((k, name[len(k) + 1:]) for k in SCOPE if name.startswith(k + '_'))
            a, b = VALUES[kind]
            inputs = [[a], None, [a]] if pattern == 'retention' else [
                None if token is None else a if token == 'a' else b for token in PATTERNS[pattern]]
        raw = inputs if any(v is not None for v in inputs) else None
        second = [[a, b], None, [a, b]] if name.endswith('_retention') else inputs
        second_raw = second if any(v is not None for v in second) else None
        expected = {'inputs_before': inputs, 'a_equals_b': False, 'raw': raw, 'received': received(inputs),
                    'inputs_second': second, 'second_raw': second_raw, 'second_received': received(second),
                    'first_after_second': raw}
        if name.endswith('_retention'):
            expected.update(raw_after_source_mutation=raw,
                            first_after_capture_mutation=[[a, a], None, [a]],
                            second_after_capture_mutation=second)
        same(observations[name], expected)
    london = VALUES['zoned_datetime'][1]
    same(observations['provider'], {'events': [
        {'phase': 'outside_state:before'},
        {'phase': 'outside_state:failure', 'error_type': 'RuntimeError',
         'error_message': 'no active GlobalState. Declare it as an injectable on the graph or node that needs it -- `def my_graph(..., state: GlobalState = None)` -- which binds the state the runtime is actually using. `with GlobalState():` selects a seed around wiring and is a compatibility surface that is removed in 1.0.'},
        {'phase': 'state_without_provider:before'},
        {'phase': 'state_without_provider:failure', 'error_type': 'RuntimeError',
         'error_message': 'no time-zone provider is installed in GlobalState'},
        {'phase': 'state_with_provider:before'},
        {'phase': 'state_with_provider:success', 'value': london},
        {'phase': 'after_state_before_eval'},
        {'phase': 'eval_without_active_provider:success', 'raw': [london, london],
         'received': received([london, london])}]})
    print('17 native temporal cases, provider phases and both availability boundaries checked; no Python parity claim.')


def main():
    validate(json.loads((HERE / 'reasoned.json').read_text()), json.loads((HERE / 'observed.json').read_text()))


if __name__ == '__main__':
    main()
