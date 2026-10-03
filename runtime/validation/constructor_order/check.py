"""Verify saved constructor order evidence without fresh runtime measurements."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def digest(value):
    assert isinstance(value, str) and len(value) == 64
    assert all(c in '0123456789abcdef' for c in value)


def main():
    evidence = json.loads((HERE / 'observed.json').read_text())
    expected = json.loads((HERE / 'reasoned.json').read_text())['expected']
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
        assert hashlib.sha256(json.dumps(content, sort_keys=True).encode()).hexdigest() == package['identity_sha256']
        digest(result['compound_scalar_source_sha256'])
        assert result['compound_scalar_module'].startswith('hgraph.')
        assert set(result['observed']) == set(expected) == set(result['assessment'])
        for key, value in expected.items():
            assert result['assessment'][key] == ('match' if result['observed'][key] == value else 'divergence')
    print('Saved constructor argument order evidence verified; no native C++ expression-order claim.')


if __name__ == '__main__':
    main()
