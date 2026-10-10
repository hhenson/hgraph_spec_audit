"""Verify captured REF-route evidence and separate it from frozen requirements."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE_NAMES = ('reasoned.json', 'observe.py')
SUPPORT_NAMES = ('delta_eval/observe.py', 'fixed/reference_identity.py', 'fixed/native_identity.py')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def check(record=None):
    record = record if record is not None else json.loads((HERE / 'observed.json').read_text())
    corpus = json.loads((HERE / 'reasoned.json').read_text())
    baseline = json.loads((HERE.parent / 'ref_owner_lifetime/observed.json').read_text())
    assert corpus['written_before_measurement'] is True
    assert record['repeats'] == 3
    assert record['sources_sha256'] == {name: sha(HERE / name) for name in SOURCE_NAMES}
    assert record['support_sha256'] == {name: sha(HERE.parent / name) for name in SUPPORT_NAMES}
    assert set(record['engines']) == {'python', 'cpp'}
    for engine, measured in record['engines'].items():
        identity = measured['identity']
        assert identity == baseline['engines'][engine]['identity']
        assert identity['native'] is (engine == 'cpp')
        package = identity['package']
        assert package['sources_sha256'] and package['artifacts_sha256']
        assert package['identity_sha256'] == digest({k: v for k, v in package.items() if k != 'identity_sha256'})
        assert len(identity['eval_node_source_sha256']) == 64
        if engine == 'cpp':
            assert identity['native_artifacts'] and identity['loaded_hgraph_libraries']
        else:
            assert not identity['native_artifacts'] and not identity['loaded_hgraph_libraries']
        cases = measured['cases']
        assert set(cases) == set(corpus['case_order'])
        assert measured['runs_sha256'] == [digest({'identity': identity, 'cases': cases})] * 3
        for name, captured in cases.items():
            required = corpus['cases'][name]
            assert captured['input_horizon'] == required['input_horizon']
            if 'error_type' in captured:
                assert set(captured) == {'input_horizon', 'events', 'error_type', 'message'}
                assessment = 'error'
            else:
                raw = captured['raw_eval_node']
                assert raw is None or isinstance(raw, list)
                assert raw is None or all(row is None or isinstance(row, str) for row in raw)
                decoded = [] if raw is None else [None if row is None else json.loads(row) for row in raw]
                padding = max(0, required['input_horizon'] - len(decoded))
                assert captured['decoded_eval_node'] == decoded
                assert captured['padding_added'] == padding
                assert captured['dense_from_input_horizon'] == decoded + [None] * padding
                assert len(captured['dense_from_input_horizon']) == required['input_horizon']
                assert captured['events'] == [row for row in decoded if row is not None]
                # Recorded observation boundary, never a replacement requirement.
                observed_dense = list(required['expected_dense'])
                if engine == 'cpp' and required['kind'] == 'tree':
                    observed_dense[3] = None
                assert captured['dense_from_input_horizon'] == observed_dense
                assessment = 'match' if captured['dense_from_input_horizon'] == required['expected_dense'] else 'divergence'
            assert measured['assessment'][name] == assessment
        assert cases['nested_scalar_first'] == cases['nested_scalar_fresh']
        assert cases['exported_tree_first'] == cases['exported_tree_fresh']
    return True

if __name__ == '__main__':
    check()
    print('Recorded REF export traces, requirements and fingerprints verified')
