"""Verify preserved reference results without promoting disagreements to passes."""
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from evidence_identity import validate_identity
spec = importlib.util.spec_from_file_location('empty_delta_probe', HERE / 'observe.py')
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)
spec = importlib.util.spec_from_file_location('boundary_checks', HERE.parent / 'publication_boundaries' / 'check.py')
boundary = importlib.util.module_from_spec(spec)
spec.loader.exec_module(boundary)


def validate(evidence):
    paths = {'reasoned_sha256': HERE / 'reasoned.json',
             'harness_sha256': HERE / 'observe.py', 'boundary_support_sha256': probe.BASE,
             'identity_support_sha256': HERE.parent / 'delta_eval' / 'observe.py'}
    for key, path in paths.items():
        assert evidence[key] == probe.support.sha(path)
    cases = json.loads((HERE / 'reasoned.json').read_text())['cases']
    ids = {c['id'] for c in cases}
    assert len(ids) == len(cases) == 18
    assert evidence['repeats'] == 3 and set(evidence['engines']) == {'python', 'cpp'}
    for name, result in evidence['engines'].items():
        validate_identity(result['identity'], name)
        assert set(result['observations']) == set(result['assessment']) == ids
        for case in cases:
            o = result['observations'][case['id']]
            assert boundary.equal(result['assessment'][case['id']], probe.support.assess(case, o))
            assert o['capability'] in ('supported', 'unsupported', 'error')
            if o['capability'] == 'unsupported':
                assert case['shape'] == 'tuple' and o['surface'] == 'hgraph.TST'
                assert 'raw_eval_node' not in o
                continue
            for item in o['producer']:
                boundary.check_state(item['state'])
            for row in o['cycles']:
                boundary.check_state(row['source'])
                boundary.check_state(row['forward'])
            for side in ('source', 'forward'):
                notifications = o[side + '_notifications']
                for item in notifications:
                    boundary.check_state(item['state'])
                events = [item['step'] for item in notifications if item['state']['publication']['present']]
                assert o[side + '_events'] == events
            if o['capability'] == 'error':
                assert o['error_type'] and o['error'] and o['phase']
                assert 'raw_eval_node' not in o
                continue
            n = len(case['actions'])
            assert [row['step'] for row in o['cycles']] == list(range(1, n + 1))
            assert [row['step'] for row in o['producer']] == list(range(1, n + 1))
            for side in ('source', 'forward'):
                assert o[side + '_events'] == [row['step'] for row in o['cycles']
                                             if row[side]['publication']['present']]
                cycles = {row['step']: row[side] for row in o['cycles']}
                for item in o[side + '_notifications']:
                    assert item['step'] in cycles
                    assert boundary.equal(item['state'], cycles[item['step']])
            raw = o['raw_eval_node']
            assert raw is None or isinstance(raw, list)
            dense = [] if raw is None else list(raw)
            padding = max(0, n - len(dense))
            assert o['input_horizon'] == n and o['padding_added'] == padding
            assert boundary.equal(o['dense_from_input_horizon'], dense + [None] * padding)
            assert boundary.equal(o['dense_from_input_horizon'],
                [row['forward']['publication'].get('payload') for row in o['cycles']])


if __name__ == '__main__':
    validate(json.loads((HERE / 'observed.json').read_text()))
    print('18 cases, two reference engines, three fresh processes each: evidence integrity verified; differences retained.')
