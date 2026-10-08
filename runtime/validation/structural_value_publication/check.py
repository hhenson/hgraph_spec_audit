"""Check frozen structural-value measurements without running an engine."""
import hashlib
import json
from pathlib import Path
import runpy

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def same(a, b):
    return json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)


def verify(evidence, native):
    corpus = json.loads((HERE / 'reasoned.json').read_text())
    assess = runpy.run_path(str(HERE / 'observe.py'))['assess']
    assert evidence['repeats'] == 3
    assert evidence['reasoned_sha256'] == sha(HERE / 'reasoned.json')
    assert evidence['harness_sha256'] == sha(HERE / 'observe.py')
    assert evidence['support_sha256'] == sha(HERE.parent / 'delta_eval/observe.py')
    assert set(evidence['engines']) == {'python', 'cpp'}
    cases = {c['id']: c for c in corpus['cases']}
    for name, engine in evidence['engines'].items():
        assert engine['identity']['native'] is (name == 'cpp')
        package = engine['identity']['package']
        content = {k: v for k, v in package.items() if k != 'identity_sha256'}
        assert hashlib.sha256(json.dumps(content, sort_keys=True).encode()).hexdigest() == package['identity_sha256']
        assert set(engine['observations']) == set(engine['assessment']) == set(cases)
        assert engine['structural_tuple']['measured'] is False
        assert engine['structural_tuple']['atomic_substitute_used'] is False
        for key, case in cases.items():
            observed = engine['observations'][key]
            assert same(engine['assessment'][key], assess(case, observed))
            if observed['status'] == 'error':
                assert observed['error_type'] and observed['error']
                continue
            assert [row['step'] for row in observed['cycles']] == [1, 2, 3]
            assert len(observed['transfers']) == 3
            assert 'raw_eval_node' in observed and 'events' in observed
            for cycle in observed['cycles']:
                for endpoint in ('source', 'output'):
                    state = cycle[endpoint]
                    assert state['members'] == sorted(state['children'])
                    for child in state['children'].values():
                        assert type(child['valid']) is bool and type(child['modified']) is bool
                        if not child['valid']: assert child['value'] is None
            for row in observed['transfers']:
                assert row['operation'] == case['mode']
                if case['mode'] in ('return_value', 'assign_value'): assert 'retained_value' in row
    assert native['repeats'] == 3
    for key, file in [('source_sha256', 'native.cpp'), ('recorder_sha256', 'native_observe.py'),
                      ('reasoned_sha256', 'native_reasoned.json')]:
        assert native[key] == sha(HERE / file)
    assert native['sdk_headers_sha256'] and native['loaded_libraries_sha256']
    assert native['status'] == 'observed'
    expected = json.loads((HERE / 'native_reasoned.json').read_text())['expected']
    assert set(native['observed']) == set(native['assessment']) == set(expected)
    for key, wanted in expected.items():
        measurement = native['observed'][key]
        rows = [json.loads(row) for row in measurement['raw_eval_node']]
        assert [row['step'] for row in rows] == [1, 2, 3]
        got = [row['output']['children'] for row in rows]
        source = [row['source']['children'] for row in rows]
        assert native['assessment'][key] == {
            'state': 'match' if same(got, wanted) else 'divergence',
            'source': 'match' if same(source, wanted) else 'divergence'}
        captures = [json.loads(row) for row in measurement['retentions']]
        assert [row['step'] for row in captures] == [1, 2, 3]
        for capture in captures:
            assert 'source_value' in capture and 'retained_value' in capture


def main():
    verify(json.loads((HERE / 'observed.json').read_text()),
           json.loads((HERE / 'native_observed.json').read_text()))
    print('Structural-value evidence verified; return, assignment, endpoint copy and native value copy remain distinct.')


if __name__ == '__main__': main()
