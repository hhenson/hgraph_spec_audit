"""Check recorded required-read evidence, including deliberate facade variations."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def check():
    cases = json.loads((HERE/'reasoned.json').read_text())['cases']
    public = json.loads((HERE/'observed.json').read_text())
    native = json.loads((HERE/'native_observed.json').read_text())
    validate(cases, public, native)
    print('Nine cases, two facade surfaces and native typed reads: recorded identities, controls and variations preserved')

def validate(cases, public, native):
    assert public['repeats'] == native['repeats'] == 3
    assert public['reasoned_sha256'] == native['reasoned_sha256'] == sha(HERE/'reasoned.json')
    assert public['harness_sha256'] == sha(HERE/'observe.py')
    assert public['support_sha256'] == sha(HERE.parent/'delta_eval/observe.py')
    assert native['source_sha256'] == sha(HERE/'native.cpp')
    assert native['recorder_sha256'] == sha(HERE/'native_observe.py')
    assert native['cmake_sha256'] == sha(HERE/'CMakeLists.txt')
    assert native['support_sha256'] == sha(HERE.parent/'fixed/native_loaded_libraries.h')
    assert native['loaded_libraries_sha256'] and native['sdk_headers_sha256']
    ids = {case['id'] for case in cases}
    assert set(native['observations']) == ids
    for engine, group in public['engines'].items():
        assert group['identity']['native'] == (engine == 'cpp')
        assert set(group['observations']) == ids
        for case in cases:
            observation = group['observations'][case['id']]
            assert observation['status'] == 'observed' and observation['eval_result'] == [1]
            rows = observation['reads']
            assert [r['surface'] for r in rows] == ['bundle_projection','child_observation']
            assert all(r['child_valid'] == case['present'] for r in rows)
            if case['present']:
                assert all(r['outcome'] == 'value' and r['result'] == case['expected'] for r in rows)
            elif engine == 'python':
                assert rows[0]['phase'] == 'projection' and rows[0]['error_type'] == 'KeyError'
                direct = rows[1]
                if case['shape'] == 'scalar': assert direct['error_type'] == 'TypeError'
                else:
                    assert direct['outcome'] == 'value'
                    assert direct['result'] == {'boolean':0,'fixed_list':2,'map':[]}[case['shape']]
            else:
                assert all(r['payload'] is None for r in rows)
                if case['shape'] == 'boolean': assert all(r['result'] == 0 for r in rows)
                else: assert all(r['outcome'] == 'failure' and r['phase'] == 'operation' for r in rows)
    for case in cases:
        row = native['observations'][case['id']]
        assert row['source_child_valid'] == row['retained_child_valid'] == case['present']
        if case['present']: assert row['outcome'] == 'value' and row['result'] == case['expected']
        else: assert row['outcome'] == 'failure' and row['error']

if __name__ == '__main__': check()
