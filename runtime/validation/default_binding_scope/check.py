"""Check conventional default-binding captures without loading measured runtimes."""
import hashlib
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
NAMES = ('reasoned.json', 'python_probe.py', 'positive.cpp', 'earlier_parameter.cpp', 'shadow_parameter.cpp', 'observe.py')
SUPPORT = ('delta_eval/observe.py', 'fixed/reference_identity.py', 'fixed/native_identity.py')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()

def valid_sha(value):
    assert isinstance(value, str) and re.fullmatch(r'[0-9a-f]{64}', value)

def check(record=None):
    record = record if record is not None else json.loads((HERE / 'observed.json').read_text())
    expected = json.loads((HERE / 'reasoned.json').read_text())
    assert expected['written_before_measurement'] is True
    assert record['repeats'] == 3
    assert record['sources_sha256'] == {name: sha(HERE / name) for name in NAMES}
    assert record['support_sha256'] == {name: sha(HERE.parent / name) for name in SUPPORT}
    python = record['python']
    identity = python['identity']
    valid_sha(identity['executable_sha256'])
    assert identity['native'] is False and not identity['native_artifacts']
    package = identity['package']
    assert package['sources_sha256'] and package['artifacts_sha256']
    for hashes in (package['sources_sha256'], package['artifacts_sha256']):
        for value in hashes.values(): valid_sha(value)
    assert package['identity_sha256'] == digest({k: v for k, v in package.items() if k != 'identity_sha256'})
    assert python['runs_sha256'] == [digest({'identity': identity, 'results': python['results']})] * 3
    normalized = {name: result['error_type'] if isinstance(result, dict) and 'error_type' in result else result for name, result in python['results'].items()}
    assert normalized == expected['python']
    assert python['results']['earlier_parameter']['message'] == "name 'first' is not defined"
    cpp = record['cpp']
    assert cpp['runs_sha256'] == [digest({k: v for k, v in cpp.items() if k != 'runs_sha256'})] * 3
    valid_sha(cpp['compiler_sha256'])
    valid_sha(cpp['binary_sha256'])
    assert isinstance(cpp['compiler_version'], str) and cpp['compiler_version'].strip()
    assert cpp['flags'] == ['-std=c++20', '-O0', '-Wall', '-Wextra']
    assert cpp['build']['exit_code'] == 0
    assert set(cpp['rejections']) == {'earlier_parameter', 'shadow_parameter'}
    results = dict(cpp['results'])
    for name, rejection in cpp['rejections'].items():
        capture = rejection['capture']
        assert rejection['runs_sha256'] == [digest(capture)] * 3
        assert type(capture['exit_code']) is int and 0 < capture['exit_code'] <= 255
        assert isinstance(capture['stdout'], str) and isinstance(capture['stderr'], str)
        assert capture['stdout'].strip() or capture['stderr'].strip()
        results[name] = 'compile_reject'
    assert results == expected['cpp']
    return True

if __name__ == '__main__':
    check()
    print('Conventional default lookup, phase and template/member distinctions verified')
