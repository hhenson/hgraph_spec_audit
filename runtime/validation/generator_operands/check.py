"""Check saved operand traces and preserve reference divergences."""
import hashlib
import json
from pathlib import Path
import sys
from assessment import assess

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from evidence_identity import validate_identity

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def validate(reasoned, evidence):
    assert reasoned['written_before_measurement']
    assert evidence['repeats'] == 3
    assert evidence['reasoned_sha256'] == digest(HERE / 'reasoned.json')
    assert evidence['harness_sha256'] == digest(HERE / 'observe.py')
    assert evidence['identity_helper_sha256'] == digest(HERE.parent / 'delta_eval/observe.py')
    assert evidence['error_contract_sha256'] == digest(HERE / 'error_contract.json')
    assert evidence['assessment_sha256'] == digest(HERE / 'assessment.py')
    contract = json.loads((HERE / 'error_contract.json').read_text())
    cases = reasoned['cases']
    assert set(evidence['engines']) == {'python', 'cpp'}
    for engine, result in evidence['engines'].items():
        validate_identity(result['identity'], engine)
        assert set(result['observations']) == set(cases) == set(result['assessment'])
        for observed in result['observations'].values():
            assert type(observed['fails']) is bool
            if observed['fails']:
                assert isinstance(observed['error_type'], str) and observed['error_type']
                assert isinstance(observed['error_message'], str) and observed['error_message']
                assert type(observed['sentinel']) is bool
                assert observed['sentinel'] == ('operand-audit-sentinel' in observed['error_message'])
        assessment = assess(result['observations'], cases, engine, contract)
        assert result['assessment'] == assessment
        divergences = {'negative_duration'} if engine == 'python' else {'negative_duration', 'past_absolute'}
        assert assessment == {name: 'divergence' if name in divergences else 'match' for name in cases}
        print(engine, assessment)
    print('Saved generator evidence checked; no engines were executed.')

def main():
    validate(json.loads((HERE / 'reasoned.json').read_text()),
             json.loads((HERE / 'observed.json').read_text()))


if __name__ == '__main__':
    main()
