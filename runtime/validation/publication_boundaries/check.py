"""Check source identity and preserved distinctions without running either engine."""
import importlib.util
import json
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from evidence_identity import validate_identity
spec = importlib.util.spec_from_file_location('publication_boundary_probe', HERE / 'observe.py')
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)


def equal(a, b): return json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)


def check_state(state):
    for flag in ('valid', 'modified'): assert type(state[flag]) is bool
    pub = state['publication']
    assert type(pub['present']) is bool
    assert pub['present'] == (state['valid'] and state['modified'])
    assert set(pub) == ({'present', 'payload'} if pub['present'] else {'present'})
    assert 'value' in state
    if 'members' in state:
        assert state['members'] == sorted(state['children'])
        for child in state['children'].values():
            assert type(child['valid']) is bool and type(child['modified']) is bool
            assert 'value' in child


def validate(evidence, corpus, harness, supplemental=False):
    assert evidence['reasoned_sha256'] == probe.sha(HERE / corpus)
    assert evidence['harness_sha256'] == probe.sha(HERE / harness)
    assert evidence['support_sha256'] == probe.sha(HERE.parent / 'delta_eval/observe.py')
    if supplemental: assert evidence['baseline_harness_sha256'] == probe.sha(HERE / 'observe.py')
    assert evidence['repeats'] == 3 and set(evidence['engines']) == {'python', 'cpp'}
    cases = json.loads((HERE / corpus).read_text())['cases']
    ids = {c['id'] for c in cases}
    assert len(ids) == len(cases) == (6 if supplemental else 18)
    for name, result in evidence['engines'].items():
        validate_identity(result['identity'], name)
        assert set(result['observations']) == set(result['assessment']) == ids
        for case in cases:
            o = result['observations'][case['id']]
            assert o['capability'] in ('supported', 'unsupported', 'error')
            assert equal(result['assessment'][case['id']], probe.assess(case, o))
            if o['capability'] == 'unsupported':
                assert case['shape'] == 'tuple' and o['surface'] == 'hgraph.TST'
                assert 'raw_eval_node' not in o
                continue
            for p in o['producer']: check_state(p['state'])
            for c in o['cycles']:
                check_state(c['source']); check_state(c['forward'])
            for side in ('source', 'forward'):
                for item in o[side + '_notifications']: check_state(item['state'])
                events = [n['step'] for n in o[side + '_notifications'] if n['state']['publication']['present']]
                assert equal(o[side + '_events'], events)
            if o['capability'] == 'error':
                assert o['error_type'] and o['error'] and o['phase']
                assert 'raw_eval_node' not in o and 'dense_from_input_horizon' not in o
                continue
            n = len(case['actions'])
            assert [c['step'] for c in o['cycles']] == list(range(1, n + 1))
            assert [p['step'] for p in o['producer']] == list(range(1, n + 1))
            for side in ('source', 'forward'):
                assert o[side + '_events'] == [c['step'] for c in o['cycles'] if c[side]['publication']['present']]
            raw = o['raw_eval_node']
            assert raw is None or isinstance(raw, list)
            # This observed API returned raw None for every no-publication run;
            # preserve it rather than replacing it with an invented empty capture.
            if not o['forward_events']: assert raw is None
            else: assert isinstance(raw, list)
            dense = [] if raw is None else list(raw)
            padding = max(0, n - len(dense))
            assert o['input_horizon'] == n and o['padding_added'] == padding
            assert equal(o['dense_from_input_horizon'], dense + [None] * padding)
            captures = [c['forward']['publication'].get('payload') for c in o['cycles']]
            assert equal(o['dense_from_input_horizon'], captures)


def main():
    baseline = json.loads((HERE / 'observed.json').read_text())
    growing = json.loads((HERE / 'growing_observed.json').read_text())
    validate(baseline, 'reasoned.json', 'observe.py')
    validate(growing, 'growing_reasoned.json', 'growing_observe.py', True)
    for name in ('python', 'cpp'):
        assert baseline['engines'][name]['identity'] == growing['engines'][name]['identity']
    print('Publication-boundary evidence verified: 18 baseline + 6 growing cases, two engines, 3 fresh processes each; disagreements/errors preserved.')


if __name__ == '__main__': main()
