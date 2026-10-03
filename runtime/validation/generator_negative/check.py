"""Validate precise negative-duration observations; do not infer admission from generic errors."""
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
    assert evidence['repeats'] == 3
    assert evidence['reasoned_sha256'] == sha(HERE / 'reasoned.json')
    assert evidence['harness_sha256'] == sha(HERE / 'observe.py')
    assert evidence['identity_helper_sha256'] == sha(HERE.parent / 'delta_eval/observe.py')
    assert set(evidence['engines']) == {'python', 'cpp'}
    cases = corpus['cases']
    assert len(cases) == 10
    for engine, result in evidence['engines'].items():
        validate_identity(result['identity'], engine)
        assert set(result['observations']) == set(cases)
        for name, case in cases.items():
            observed = result['observations'][name]
            # These are measured reference outcomes, including departures from
            # the pre-measurement HGL effect expectations. Never repair evidence.
            expected = dict(case['expected'])
            if engine == 'python' and name in {'negative_later', 'zero_later'}:
                expected = {'fails': False, 'raw': [None, None, 1, 2],
                            'trace': cases['past_absolute_later']['expected']['trace']}
            if engine == 'cpp' and name in {'negative_start', 'negative_target_underflow', 'past_absolute_start'}:
                expected = {'fails': False, 'raw': None, 'trace': ['time', 'value']}
            if engine == 'cpp' and name == 'past_absolute_later':
                expected = dict(cases['negative_later']['expected'])
            for field, value in expected.items():
                assert json.dumps(observed[field]) == json.dumps(value), (engine, name, field)
            assert type(observed['fails']) is bool
            downstream = [] if observed['fails'] or observed['raw'] is None else [v for v in observed['raw'] if v is not None]
            assert observed['downstream_payloads'] == downstream
            assert set(observed) == ({'trace', 'downstream_payloads', 'fails', 'error_type', 'error_message'}
                                     if observed['fails'] else {'trace', 'downstream_payloads', 'fails', 'raw'})
            if observed['fails']:
                assert observed['error_type'] == ('NodeException' if engine == 'python' else 'RuntimeError')
                assert isinstance(observed['error_message'], str)
                assert '\nActivation Back Trace:' in observed['error_message']
                lines = observed['error_message'].splitlines()
                assert len(lines) >= 2
                terminal = observed['error_message'].split('\nActivation Back Trace:', 1)[0].rstrip().splitlines()[-1]
                if name == 'negative_start':
                    assert engine == 'python'
                    assert lines[1] == 'NodeError: Duplicate time produced by generator: [1970-01-01 00:00:00] - 1'
                elif name in {'negative_later', 'zero_later', 'past_absolute_later'}:
                    assert engine == 'cpp'
                    assert lines[0] == "node[0 'composition.body'] evaluate failed: Python generator output times must be strictly increasing"
                elif name in {'negative_target_underflow', 'time_expression_underflow'}:
                    assert terminal == 'OverflowError: date value out of range'
                    if engine == 'python':
                        assert lines[1] == 'NodeError: date value out of range'
                else:
                    sentinel = ('negative-time-operand-sentinel' if case.get('time_failure')
                                else 'negative-payload-operand-sentinel')
                    assert terminal == 'RuntimeError: ' + sentinel
                    if engine == 'python':
                        assert lines[1] == 'NodeError: ' + sentinel
            comparison = {field: 'match' if json.dumps(observed.get(field)) == json.dumps(value) else 'divergence'
                          for field, value in case['expected'].items()}
            print(engine, name, 'Pre-ordering HGL effect comparison:', comparison)
    supersession = json.loads((HERE.parent / 'generator_operands/supersession.json').read_text())
    assert supersession['superseded_reasoned_sha256'] == sha(HERE.parent / 'generator_operands/reasoned.json')
    assert supersession['superseded_by'] == '../generator_negative/README.md'
    print('Negative-duration reference facts checked; matching effects do not establish matching error causes.')


def main():
    validate(json.loads((HERE / 'reasoned.json').read_text()),
             json.loads((HERE / 'observed.json').read_text()))


if __name__ == '__main__':
    main()
