"""Check rolling arrivals and retain exact baseline harness/operator disagreements."""
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'atomic_snapshots'))
from provenance import validate_identity
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import sha

INPUTS = {'tick': [10, None, 20, 30], 'duration_gap': [10, None, 20, None, None, None, None, None, 30],
          'duration_zero_min': [10, None, 20], 'equal_arrivals': [10, 10, None, 10],
          'empty': [], 'all_silent': [None, None]}


def stamp(t):
    return f'1970-01-01T00:00:00.{t:06}'


def event(value, delta, ready, times, endpoint=None, removed=None):
    out = {'value': value, 'delta': delta, 'valid': True, 'all_valid': ready,
           'value_times': None if times is None else [stamp(t) for t in times]}
    if endpoint:
        out['endpoint'] = endpoint
    else:
        out.update(has_removed=removed is not None, removed=removed)
    return out


def native_events(case):
    if case == 'tick':
        return [event([10], 10, False, [1]), event([10, 20], 20, True, [1, 3]),
                event([20, 30], 30, True, [3, 4], removed=10)]
    if case == 'duration_gap':
        return [event([10], 10, False, [1]), event([10, 20], 20, True, [1, 3]),
                event([30], 30, False, [9], removed=20)]
    if case == 'duration_zero_min':
        return [event([10], 10, True, [1]), event([10, 20], 20, True, [1, 3])]
    if case == 'equal_arrivals':
        return [event([10], 10, True, [1]), event([10, 10], 10, True, [1, 2]),
                event([10, 10], 10, True, [2, 4], removed=10)]
    return []


def validate(evidence, composed=False):
    prefix = 'composed_' if composed else ''
    assert evidence['repeats'] == 3 and type(evidence['repeats']) is int
    assert evidence['reasoned_sha256'] == sha(HERE / (prefix + 'reasoned.json'))
    assert evidence['harness_sha256'] == sha(HERE / (prefix + 'observe.py'))
    assert evidence['identity_helper_sha256'] == sha(HERE.parent / 'delta_eval/observe.py')
    assert set(evidence['engines']) == {'python', 'cpp'}
    for engine, result in evidence['engines'].items():
        validate_identity(result['identity'], engine)
        assert set(result['observations']) == set(INPUTS)
        for case, inputs in INPUTS.items():
            raw = inputs if any(v is not None for v in inputs) else None
            events = native_events(case)
            if engine == 'python' and not composed:
                expected = {'error_type': 'IncorrectTypeBinding',
                            'error': 'value: TSW[int] <- TS[int] is not type compatible', 'received': []}
            elif not composed:
                expected = {'raw': raw, 'received': events}
            else:
                paired = []
                for e in events:
                    for label in ('input', 'output'):
                        current = {k: v for k, v in e.items() if k not in ('has_removed', 'removed')}
                        current['endpoint'] = label
                        if case == 'duration_zero_min' and label == 'input' and engine == 'cpp':
                            current['all_valid'] = False
                        paired.append(current)
                expected = {'raw': raw, 'received': paired}
                if engine == 'python' and case in ('tick', 'equal_arrivals'):
                    expected = {'error_type': 'NodeException',
                                'error': "TSW output application: Expected <class 'int'>, got <class 'numpy.int64'>",
                                'received': [event(None, 10, False, None, 'input') if case == 'tick'
                                             else event([10], 10, True, [1], 'input')]}
                elif engine == 'python' and case == 'duration_gap':
                    expected = {'raw': [None, None, 20, None, None, None, None, None, 30],
                                'received': [event(None, None, True, [1], 'input'),
                                             event([10, 20], 20, True, [1, 3], 'input'),
                                             event([20], 20, True, [3], 'output'),
                                             event([30], 30, True, [9], 'input'),
                                             event([30], 30, True, [9], 'output')]}
            assert result['observations'][case] == expected, (engine, case, composed)


if __name__ == '__main__':
    validate(json.loads((HERE / 'observed.json').read_text()))
    validate(json.loads((HERE / 'composed_observed.json').read_text()), True)
    print('Rolling arrivals checked; direct/composed harness and readiness disagreements retained.')
