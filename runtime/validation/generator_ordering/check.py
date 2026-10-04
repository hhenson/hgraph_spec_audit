"""Preserve measured ordering behavior separately from HGL's all-target rule."""
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from evidence_identity import validate_identity


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(corpus, evidence):
    assert corpus['written_before_measurement'] is True
    assert evidence['reasoned_sha256'] == sha(HERE / 'reasoned.json')
    assert evidence['harness_sha256'] == sha(HERE / 'observe.py')
    assert evidence['identity_helper_sha256'] == sha(HERE.parent / 'delta_eval/observe.py')
    assert evidence['repeats'] == 3
    assert set(evidence['engines']) == {'python', 'cpp'}
    cases = corpus['cases']
    assert len(cases) == 8
    full_trace = [label for i in (1, 2, 3) for label in (f'time{i}', f'value{i}', f'after{i}')]
    for engine, result in evidence['engines'].items():
        validate_identity(result['identity'], engine)
        assert set(result['observations']) == set(cases)
        for name, case in cases.items():
            offsets = case['absolute_offsets_us']
            assert len(offsets) == 3 and all(type(value) is int for value in offsets)
            assert case['expected']['fails'] == any(b <= a for a, b in zip(offsets, offsets[1:]))
            observed = result['observations'][name]
            if engine == 'cpp' and 'past' in name:
                expected = {'fails': False, 'raw': None, 'trace': ['time1', 'value1']}
            elif engine == 'cpp' and name in {'repeat_future', 'decrease_future'}:
                expected = {'fails': True, 'trace': ['time1', 'value1', 'after1', 'time2', 'value2']}
            else:
                raw = ([None, None, 3] if 'past' in name else
                       [None, None, 2, 3] if name == 'repeat_future' else
                       [None, None, 1, 3] if name == 'decrease_future' else [None, 1, 2, 3])
                expected = {'fails': False, 'raw': raw, 'trace': full_trace}
            for field, value in expected.items():
                assert json.dumps(observed[field]) == json.dumps(value), (engine, name, field)
            assert type(observed['fails']) is bool
            downstream = [] if observed['fails'] or observed['raw'] is None else [v for v in observed['raw'] if v is not None]
            assert json.dumps(observed['downstream_payloads']) == json.dumps(downstream)
            fields = {'trace', 'downstream_payloads', 'fails'}
            if observed['fails']:
                assert set(observed) == fields | {'error_type', 'error_message'}
                assert observed['error_type'] == 'RuntimeError'
                assert observed['error_message'] == ("node[0 'composition.body'] evaluate failed: "
                        'Python generator output times must be strictly increasing\n'
                        'Activation Back Trace:\ncomposition.body[0]\n')
            else:
                assert set(observed) == fields | {'raw'}
            comparison = {field: 'match' if json.dumps(observed.get(field)) == json.dumps(value) else 'divergence'
                          for field, value in case['expected'].items()}
            print(engine, name, 'HGL effect comparison:', comparison)
    supersession = json.loads((HERE.parent / 'generator_negative/supersession.json').read_text())
    assert supersession['superseded_reasoned_sha256'] == sha(HERE.parent / 'generator_negative/reasoned.json')
    assert supersession['superseded_by'] == '../generator_ordering/README.md'
    assert supersession['changed_expected_cases'] == ['past_absolute_later']
    print('Strict-order reference evidence checked; halted first yields do not demonstrate pair validation.')


def main():
    validate(json.loads((HERE / 'reasoned.json').read_text()),
             json.loads((HERE / 'observed.json').read_text()))


if __name__ == '__main__':
    main()
