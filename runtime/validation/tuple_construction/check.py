"""Verify saved tuple construction evidence; do not execute either engine."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def digest(value):
    assert isinstance(value, str) and len(value) == 64
    assert all(c in '0123456789abcdef' for c in value)


def main():
    reasoned = json.loads((HERE / 'reasoned.json').read_text())
    evidence = json.loads((HERE / 'observed.json').read_text())
    assert evidence['reasoned_sha256'] == sha(HERE / 'reasoned.json')
    assert evidence['harness_sha256'] == sha(HERE / 'observe.py')
    assert evidence['identity_helper_sha256'] == sha(HERE.parent / 'delta_eval/observe.py')
    assert evidence['repeats'] == 3 and set(evidence['engines']) == {'python', 'cpp'}
    for name, result in evidence['engines'].items():
        identity = result['identity']
        assert identity['native'] == (name == 'cpp')
        package = identity['package']
        for field in ('sources_sha256', 'artifacts_sha256'):
            assert package[field]
            for source, value in package[field].items():
                assert source and not source.startswith('/')
                digest(value)
        content = {key: value for key, value in package.items() if key != 'identity_sha256'}
        assert sha_json(content) == package['identity_sha256']
        assert set(result['assessment']) == set(reasoned['expected'])
        assert set(result['observed']) == set(reasoned['expected']) | {'ordinary_python_alias'}
        for key, expected in reasoned['expected'].items():
            assert result['assessment'][key] == ('match' if result['observed'][key] == expected else 'divergence')
        assert result['observed']['ordinary_python_alias'] == reasoned['descriptive_python_alias']
    native = json.loads((HERE / 'native_observed.json').read_text())
    for key, source in [('source_sha256', 'native_call.cpp'), ('recorder_sha256', 'native_observe.py'),
                        ('reasoned_sha256', 'reasoned.json')]:
        assert native[key] == sha(HERE / source)
    for key in ('binary_sha256', 'compiler_sha256'):
        digest(native[key])
    assert native['repeats'] == 3
    assert native['observed']['value'] == [2, 1] and native['observed']['constructed'] is False
    for key, expected in reasoned['native_call_target'].items():
        assert native['assessment'][key] == ('match' if native['observed'][key] == expected else 'variation')
    print('Saved tuple evidence verified; native call-order variations retained, no TST parity claim.')


def sha_json(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


if __name__ == '__main__':
    main()
