"""Verify NaN evidence while retaining domain errors and false-valued ticks."""
import importlib.util
import json
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from evidence_identity import validate_identity
spec = importlib.util.spec_from_file_location('nan_probe', HERE / 'observe.py')
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)


def same(a, b): return json.dumps(a, sort_keys=True, allow_nan=False) == json.dumps(b, sort_keys=True, allow_nan=False)


def validate(evidence):
    assert evidence['reasoned_sha256'] == probe.sha(HERE / 'reasoned.json')
    assert evidence['harness_sha256'] == probe.sha(HERE / 'observe.py')
    assert evidence['identity_helper_sha256'] == probe.sha(HERE.parent / 'delta_eval/observe.py')
    assert evidence['repeats'] == 3 and set(evidence['engines']) == {'python', 'cpp'}
    corpus = json.loads((HERE / 'reasoned.json').read_text())
    cases = corpus['cases']; ids = {c['id'] for c in cases}
    assert len(ids) == len(cases) == 28
    for name, engine in evidence['engines'].items():
        validate_identity(engine['identity'], name)
        assert set(engine['observations']) == set(engine['assessment']) == ids
        assert set(engine['primitives']) == set(corpus['primitive_candidates']) == {'is_nan', 'isnan'}
        for primitive in engine['primitives'].values():
            assert primitive == {'public_exported': False, 'native_registered': False if name == 'cpp' else None}
        for case in cases:
            obs = engine['observations'][case['id']]
            assert obs['status'] in ('observed', 'error')
            assert engine['assessment'][case['id']] == probe.assessment(case, obs)
            assert set(obs['events']) == {'lhs', 'rhs', 'result'}
            for events in obs['events'].values():
                for e in events:
                    assert e['valid'] is True and e['modified'] is True
                    assert same(e['value'], e['delta'])
            if obs['status'] == 'error':
                assert name == 'python' and case['id'] in ('ln_negative', 'ln_negative_self_eq', 'ln_negative_self_ne')
                assert obs['error_type'] == 'NodeException' and 'ValueError: expected a positive input, got -1.0' in obs['error']
                assert 'raw_eval_node' not in obs and not obs['events']['result']
                continue
            assert engine['assessment'][case['id']] == 'match'
            assert same(obs['raw_eval_node'], case['expected'])
            assert same(obs['dense'], case['expected'])
            assert obs['input_horizon'] == 2 and obs['padding_added'] == 0
            assert len(obs['events']['result']) == 1
            assert same(obs['events']['result'][0]['value'], case['expected'][0])
            if case['kind'] == 'comparison':
                for label, operand in zip(('lhs', 'rhs'), case['operands']):
                    assert len(obs['events'][label]) == 1
                    want = {'float_class': 'nan'} if operand == 'nan' else operand
                    assert same(obs['events'][label][0]['value'], want)
            elif case['kind'] == 'ln_compare':
                for label in ('lhs', 'rhs'):
                    assert len(obs['events'][label]) == 1
                    assert obs['events'][label][0]['value'] == {'float_class': 'nan'}
    # A removed error cannot be relabelled as an observed success, even if it
    # fabricates a result matching the candidate cross-runtime expectation.
    for id in ('ln_negative', 'ln_negative_self_eq', 'ln_negative_self_ne'):
        assert evidence['engines']['python']['observations'][id]['status'] == 'error'


def main():
    validate(json.loads((HERE / 'observed.json').read_text()))
    print('NaN evidence verified: 28 cases, native 28 matches; historical 25 matches + 3 retained domain errors; no engines executed.')


if __name__ == '__main__': main()
