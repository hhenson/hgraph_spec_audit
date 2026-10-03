"""Check saved key-collision observations; never rerun or repair engine results."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    corpus = json.loads((HERE / 'reasoned.json').read_text())
    evidence = json.loads((HERE / 'observed.json').read_text())
    assert corpus['written_before_measurement']
    assert evidence['reasoned_sha256'] == sha(HERE / 'reasoned.json')
    assert evidence['harness_sha256'] == sha(HERE / 'observe.py')
    assert evidence['identity_helper_sha256'] == sha(HERE.parent / 'delta_eval/observe.py')
    assert evidence['repeats'] == 3
    assert set(evidence['engines']) == {'python', 'cpp'}
    for engine, result in evidence['engines'].items():
        native = engine == 'cpp'
        assert result['identity']['native'] == native
        assert result['identity']['package']['identity_sha256']
        if native:
            assert result['identity']['native_artifacts']
            assert result['identity']['loaded_hgraph_libraries']
        assert set(result['observations']) == set(corpus['cases'])
        for name, observed in result['observations'].items():
            case = corpus['cases'][name]
            recorder_key = 'eval_node::out' if native else 'nodes.record.out'
            assert observed['recorder_key'] == recorder_key
            assert observed['user_key'] == (recorder_key if case['collide'] else 'audit.user.recording')
            timed = case['layout'] == 'sparse' or not native
            assert observed['logical_entry_type'] == ('list[tuple[datetime,int]]' if timed else 'list[int]')
            assert observed['events'] and observed['events'][0]['phase'] == 'start_before'
            for snapshot in [observed['initial_user_entry'], observed['final_user_entry'], observed['final_recorder_entry']] + [s for e in observed['events'] for s in (e['recorder_entry'], e['user_entry'])]:
                assert type(snapshot['present']) is bool
                if snapshot['present']:
                    assert snapshot['exported_types']['kind'] == 'list'
                    assert len(snapshot['value']) == len(snapshot['exported_types']['items'])
                    for value, shape in zip(snapshot['value'], snapshot['exported_types']['items']):
                        if timed:
                            assert shape == {'kind': 'tuple', 'items': ['datetime', 'int']}
                            assert len(value) == 2 and set(value[0]) == {'datetime'} and type(value[1]) is int
                        else:
                            assert shape == 'int' and type(value) is int
            outcome = observed['result']
            if 'error' in outcome:
                assert outcome['error'] and outcome['error_type'] and 'raw' not in outcome
                output_assessment = 'error'
            else:
                assert set(outcome) == {'raw'}
                output_assessment = 'match' if outcome['raw'] == case['expected_raw'] else 'divergence'
            final = observed['final_user_entry']
            values = None if not final['present'] else ([v[1] for v in final['value']] if timed else final['value'])
            expected = {'output_isolation': output_assessment,
                        'user_entry_preserved': 'match' if values == case['expected_user_payloads'] else 'divergence'}
            assert observed['assessment'] == expected
            print(engine, name, expected)
    source = json.loads((HERE / 'source_inventory.json').read_text())
    assert source['native_header']['installed_sha256'] == source['native_header']['checkout_sha256']
    assert source['native_header']['revision'] == '8e899e600089902f9b755f67d9998292fcc03e84'
    for engine, field, hash_field in [('cpp', 'native_header', 'installed_sha256'),
                                      ('python', 'historical_recorder', 'sha256')]:
        artifacts = evidence['engines'][engine]['identity']['package']['artifacts_sha256']
        assert artifacts[source[field]['path']] == source[field][hash_field]
    print('Recorded key-collision evidence verified; no engines were executed.')


if __name__ == '__main__':
    main()
