"""Verify frozen expectations, provenance and separately labelled dense normalization."""
import hashlib
import json
from pathlib import Path
import sys

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
    cases = {case['id']: case for case in reasoned['cases']}
    assert len(cases) == 24
    assert set(evidence['engines']) == {'python', 'cpp'}
    for engine, result in evidence['engines'].items():
        validate_identity(result['identity'], engine)
        assert set(result['observations']) == set(cases) == set(result['assessment'])
        for name, case in cases.items():
            outcome = result['observations'][name]
            if 'error' in outcome:
                assessment = 'error'
            else:
                raw = outcome['raw_eval_result']
                assert raw is None or isinstance(raw, list)
                dense = [] if raw is None else list(raw)
                padding = max(0, case['horizon'] - len(dense))
                assert all(type(outcome[field]) is int for field in
                           ('source_entry_count', 'external_dense_horizon', 'padding_added'))
                assert outcome['source_entry_count'] == len(case['timed_entries'])
                assert outcome['external_dense_horizon'] == case['horizon']
                assert outcome['padding_added'] == padding
                assert json.dumps(outcome['dense_from_external_horizon'], sort_keys=True) == json.dumps(dense + [None] * padding, sort_keys=True)
                assessment = 'match' if json.dumps(outcome['dense_from_external_horizon'], sort_keys=True) == json.dumps(case['expected_dense'], sort_keys=True) else 'divergence'
            assert result['assessment'][name] == assessment == 'match', (engine, name, outcome)
        print(engine, result['assessment'])
    print('Timed-value evidence verified; no engines were executed.')


def main():
    validate(json.loads((HERE / 'reasoned.json').read_text()),
             json.loads((HERE / 'observed.json').read_text()))


if __name__ == '__main__':
    main()
