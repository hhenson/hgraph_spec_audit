"""Check recorded required-read evidence, including deliberate facade variations."""
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "atomic_snapshots"))
from provenance import validate_identity, digest, manifest
from native_observe import command_configuration

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def check():
    cases = json.loads((HERE/'reasoned.json').read_text())['cases']
    public = json.loads((HERE/'observed.json').read_text())
    native = json.loads((HERE/'native_observed.json').read_text())
    validate(cases, public, native)
    ninja = json.loads((HERE/'native_ninja_observed.json').read_text())
    validate(cases, public, ninja)
    assert native['cmake_generator'] == 'Unix Makefiles'
    assert ninja['cmake_generator'] == 'Ninja'
    debug = json.loads((HERE/'native_reconfigured_observed.json').read_text())
    validate(cases, public, debug)
    assert debug['cmake_generator'] == 'Ninja' and debug['target_configuration'] == 'Debug'
    assert debug['observations'] == native['observations']
    assert debug['loaded_libraries_sha256'] == native['loaded_libraries_sha256']
    assert debug['sdk_headers_sha256'] == native['sdk_headers_sha256']
    for configuration in ('Debug', 'Release'):
        multi = json.loads((HERE/f'native_multiconfig_{configuration.lower()}_observed.json').read_text())
        validate(cases, public, multi)
        assert multi['cmake_generator'] == 'Ninja Multi-Config'
        assert multi['target_configuration'] == configuration
        assert multi['observations'] == native['observations']
        assert multi['sdk_headers_sha256'] == native['sdk_headers_sha256']
    archive = HERE/'archive'
    old = json.loads((archive/'native_observed.json').read_text())
    assert old['recorder_sha256'] == sha(archive/'native_observe.py')
    assert old['cmake_sha256'] == sha(archive/'CMakeLists.txt')
    assert old['source_sha256'] == sha(HERE/'native.cpp')
    assert old['observations'] == native['observations'] == ninja['observations']
    assert old['loaded_libraries_sha256'] == native['loaded_libraries_sha256'] == ninja['loaded_libraries_sha256']
    assert old['sdk_headers_sha256'] == native['sdk_headers_sha256'] == ninja['sdk_headers_sha256']
    for snapshot in ('compile_commands', 'target_identity', 'active_configuration'):
        previous = archive/snapshot
        names = ['native_observed.json', 'native_ninja_observed.json']
        if snapshot == 'active_configuration': names.append('native_reconfigured_observed.json')
        for name in names:
            prior = json.loads((previous/name).read_text())
            assert prior['recorder_sha256'] == sha(previous/'native_observe.py')
            assert prior['cmake_sha256'] == sha(previous/'CMakeLists.txt')
            assert prior['source_sha256'] == native['source_sha256']
            assert prior['observations'] == native['observations']
            assert prior['loaded_libraries_sha256'] == native['loaded_libraries_sha256']
            assert prior['sdk_headers_sha256'] == native['sdk_headers_sha256']
    print('Nine cases, two facade surfaces and native typed reads: recorded identities, controls and variations preserved')

def validate_observation_values(case, engine, rows):
    """Check absence and payloads before considering their derived results."""
    payload, payload_type = None, 'NoneType'
    if case['present']:
        payload = {'scalar': 4, 'boolean': case.get('value', True),
                   'fixed_list': [4, 5], 'map': {'7': 4}}[case['shape']]
        payload_type = {'scalar': 'int', 'boolean': 'bool', 'fixed_list': 'tuple',
                        'map': 'frozendict' if engine == 'python' else 'dict'}[case['shape']]
    elif engine == 'python' and case['shape'] in ('fixed_list', 'map'):
        payload, payload_type = ([None, None], 'tuple') if case['shape'] == 'fixed_list' else ({}, 'frozendict')
    for row in rows:
        bundle = row['surface'] == 'bundle_projection'
        missing_field = bundle and engine == 'python' and not case['present']
        retained = ({'sibling': 1} if missing_field else {'sibling': 1, 'child': payload}) if bundle else payload
        expected = {'retained': retained, 'retained_type': 'dict' if bundle else payload_type,
                    'phase': 'projection' if missing_field else 'operation'}
        if not missing_field: expected.update(payload=payload, payload_type=payload_type)
        actual = {key: row[key] for key in ('retained', 'retained_type', 'phase', 'payload', 'payload_type') if key in row}
        # JSON spelling preserves distinctions such as false versus zero.
        assert json.dumps(actual, sort_keys=True) == json.dumps(expected, sort_keys=True), (engine, case['id'], row['surface'])


def validate(cases, public, native):
    assert public['repeats'] == native['repeats'] == 3
    assert public['reasoned_sha256'] == native['reasoned_sha256'] == sha(HERE/'reasoned.json')
    assert public['harness_sha256'] == sha(HERE/'observe.py')
    assert public['support_sha256'] == sha(HERE.parent/'delta_eval/observe.py')
    assert native['source_sha256'] == sha(HERE/'native.cpp')
    assert native['recorder_sha256'] == sha(HERE/'native_observe.py')
    assert native['cmake_sha256'] == sha(HERE/'CMakeLists.txt')
    assert native['support_sha256'] == sha(HERE.parent/'fixed/native_loaded_libraries.h')
    manifest(native['loaded_libraries_sha256'])
    manifest(native['sdk_headers_sha256'])
    for field in ('binary_sha256', 'compiler_sha256', 'compile_commands_sha256', 'target_manifest_sha256'): digest(native[field])
    assert native['target_name'] == 'unset_required_reads_native'
    assert isinstance(native['target_configuration'], str)
    artifact = Path(native['target_artifact'])
    assert not artifact.is_absolute() and '..' not in artifact.parts
    assert artifact.name in ('unset_required_reads_native', 'unset_required_reads_native.exe')
    command = native['compile_command']
    assert isinstance(command, list) and command and all(isinstance(arg, str) and arg for arg in command)
    assert '<source>/native.cpp' in command and '-c' in command
    assert any(arg.startswith('-std=') for arg in command)
    configuration = command_configuration({}, command)
    if native['cmake_generator'] == 'Ninja Multi-Config':
        assert configuration == native['target_configuration']
        assert artifact.parent.name == native['target_configuration']
    else: assert configuration is None or configuration == native['target_configuration']
    ids = {case['id'] for case in cases}
    assert set(native['observations']) == ids
    assert set(public['engines']) == {'python', 'cpp'}
    for engine, group in public['engines'].items():
        validate_identity(group['identity'], engine)
        if engine == 'cpp':
            for library in ('libhgraph_runtime.so', 'libhgraph_wiring.so', 'libhgraph_stdlib.so'):
                assert native['loaded_libraries_sha256'][library] == group['identity']['loaded_hgraph_libraries'][library]
        assert set(group['observations']) == ids
        for case in cases:
            observation = group['observations'][case['id']]
            assert observation['status'] == 'observed' and observation['eval_result'] == [1]
            rows = observation['reads']
            assert [r['surface'] for r in rows] == ['bundle_projection','child_observation']
            assert all(r['child_valid'] == case['present'] for r in rows)
            validate_observation_values(case, engine, rows)
            if case['present']:
                assert all(r['outcome'] == 'value' and r['result'] == case['expected'] for r in rows)
            elif engine == 'python':
                assert rows[0]['outcome'] == 'failure' and rows[0]['phase'] == 'projection' and rows[0]['error_type'] == 'KeyError'
                direct = rows[1]
                if case['shape'] == 'scalar': assert direct['outcome'] == 'failure' and direct['error_type'] == 'TypeError'
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
