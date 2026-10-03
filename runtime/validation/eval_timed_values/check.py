"""Verify frozen expectations, provenance and separately labelled dense normalization."""
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
    cases = {case['id']: case for case in reasoned['cases']}
    assert len(cases) == 24
    assert set(evidence['engines']) == {'python', 'cpp'}
    for engine, result in evidence['engines'].items():
        assert result['identity']['native'] == (engine == 'cpp')
        assert set(result['observations']) == set(cases) == set(result['assessment'])
        for name, case in cases.items():
            outcome = result['observations'][name]
            if 'error' in outcome:
                assessment = 'error'
            else:
                raw = outcome['raw_eval_result']
                dense = [] if raw is None else list(raw)
                padding = max(0, case['horizon'] - len(dense))
                assert outcome['source_entry_count'] == len(case['timed_entries'])
                assert outcome['external_dense_horizon'] == case['horizon']
                assert outcome['padding_added'] == padding
                assert outcome['dense_from_external_horizon'] == dense + [None] * padding
                assessment = 'match' if outcome['dense_from_external_horizon'] == case['expected_dense'] else 'divergence'
            assert result['assessment'][name] == assessment
        print(engine, result['assessment'])
    print('Timed-value evidence verified; no engines were executed.')


if __name__ == '__main__':
    main()
