"""Verify recorded map-key evidence without rerunning either engine."""
import copy
import hashlib
import json
from pathlib import Path
import observe

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(record=None):
    record = record if record is not None else json.loads((HERE / 'observed.json').read_text())
    corpus = json.loads((HERE / 'reasoned.json').read_text())
    provenance = json.loads((HERE / 'provenance.json').read_text())
    assert record['repeats'] == 3
    assert record['sources_sha256'] == {name: sha(HERE / name) for name in ('reasoned.json', 'observe.py')}
    assert record['support_sha256'] == {name: sha(HERE.parent / name) for name in observe.SUPPORT}
    assert provenance['history_sha256'] == {name: sha(HERE / name) for name in provenance['history_sha256']}
    assert set(record['engines']) == {'python', 'cpp'}
    for engine, measured in record['engines'].items():
        identity = measured['identity']
        assert identity['native'] is (engine == 'cpp')
        assert identity['python'] == '3.14.4'
        assert identity['hgraph'] == ('0.0.0' if engine == 'cpp' else '0.5.41')
        package = identity['package']
        assert package['sources_sha256'] and package['artifacts_sha256']
        assert package['identity_sha256'] == observe.digest({k: v for k, v in package.items() if k != 'identity_sha256'})
        assert len(identity['eval_node_source_sha256']) == 64
        assert bool(identity['native_artifacts']) is (engine == 'cpp')
        assert bool(identity['loaded_hgraph_libraries']) is (engine == 'cpp')
        assert set(measured['cases']) == set(corpus['cases'])
        assert set(measured['scalar_dictionary']) == {'safe', 'fallback', 'strict_present', 'strict_missing'}
        payload = {key: measured[key] for key in ('identity', 'cases', 'scalar_dictionary')}
        assert measured['runs_sha256'] == [observe.digest(payload)] * 3
        assert measured['assessment'] == observe.assess(payload, corpus)
        for name, actual in measured['cases'].items():
            expected = copy.deepcopy(corpus['cases'][name]['expected'])
            if engine == 'python' and name == 'key_changes':
                expected[3][1] = True  # Preserve the measured repeated-empty tick.
            if engine == 'cpp' and name == 'invalid_child_membership':
                expected[2][3] = True  # Preserve the measured invalid-input modified flag.
            if engine == 'python' and name == 'held_removal_readd':
                assert actual['events'] == expected[:5]
                assert actual['error_type'] == 'AttributeError'
                assert actual['error'] == "'NoneType' object has no attribute 'graph'"
                assert 'raw_eval_node' not in actual
            else:
                assert 'error_type' not in actual
                assert actual['events'] == expected
                assert actual['events'] == [json.loads(row) for row in actual['raw_eval_node'] if row is not None]
        for mode, actual in measured['scalar_dictionary'].items():
            if mode == 'strict_missing':
                assert measured['assessment']['scalar_dictionary.' + mode] == 'match'
                assert actual['error_type'] == ('RuntimeError' if engine == 'cpp' else 'NodeException')
                assert 'KeyError' in actual['error']
            else:
                assert 'error_type' not in actual
                assert actual['events'] == corpus['scalar_dictionary'][mode + '_expected']
                assert actual['events'] == [json.loads(row) for row in actual['raw_eval_node'] if row is not None]
        failures = {name for name, result in measured['assessment'].items() if result == 'divergence'}
        assert failures == ({'invalid_child_membership'} if engine == 'cpp' else {'key_changes', 'held_removal_readd'})
    return True


if __name__ == '__main__':
    check()
    print('Map-key requirements, observed variations, raw rows and identities verified')
