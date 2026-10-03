"""Check saved operand traces and preserve reference divergences."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    reasoned = json.loads((HERE / 'reasoned.json').read_text())
    evidence = json.loads((HERE / 'observed.json').read_text())
    assert reasoned['written_before_measurement']
    assert evidence['repeats'] == 3
    assert evidence['reasoned_sha256'] == digest(HERE / 'reasoned.json')
    assert evidence['harness_sha256'] == digest(HERE / 'observe.py')
    assert evidence['identity_helper_sha256'] == digest(HERE.parent / 'delta_eval/observe.py')
    cases = reasoned['cases']
    assert set(evidence['engines']) == {'python', 'cpp'}
    for engine, result in evidence['engines'].items():
        assert result['identity']['native'] == (engine == 'cpp')
        assert set(result['observations']) == set(cases) == set(result['assessment'])
        assessment = {case: 'match' if all(result['observations'][case].get(k) == v for k, v in expected.items()) else 'divergence' for case, expected in cases.items()}
        assert result['assessment'] == assessment
        print(engine, assessment)
    print('Saved generator evidence checked; no engines were executed.')

if __name__ == '__main__':
    main()
