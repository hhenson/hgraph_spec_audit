"""Validate recorded package/source identities and loaded native provenance."""
import hashlib
import json
from pathlib import PurePosixPath


def digest(value):
    assert isinstance(value, str) and len(value) == 64
    assert all(c in '0123456789abcdef' for c in value)


def manifest(value):
    assert isinstance(value, dict) and value
    for name, value in value.items():
        assert isinstance(name, str) and name and not name.startswith('/')
        digest(value)


def validate_identity(identity, engine):
    assert type(identity['native']) is bool and identity['native'] == (engine == 'cpp')
    for field in ('python', 'hgraph', 'eval_node_module'):
        assert isinstance(identity[field], str) and identity[field]
    digest(identity['eval_node_source_sha256'])
    package = identity['package']
    assert package['version'] == identity['hgraph']
    manifest(package['sources_sha256'])
    manifest(package['artifacts_sha256'])
    content = {k: v for k, v in package.items() if k != 'identity_sha256'}
    digest(package['identity_sha256'])
    assert hashlib.sha256(json.dumps(content, sort_keys=True).encode()).hexdigest() == package['identity_sha256']
    module_path = identity['eval_node_module'].removeprefix('hgraph.').replace('.', '/') + '.py'
    assert package['sources_sha256'][module_path] == identity['eval_node_source_sha256']
    for name, value in package['sources_sha256'].items():
        artifact = name if name in package['artifacts_sha256'] else 'hgraph/' + name
        assert package['artifacts_sha256'][artifact] == value
    if engine == 'cpp':
        manifest(identity['native_artifacts'])
        manifest(identity['loaded_hgraph_libraries'])
        native = identity['native_artifacts']
        loaded = identity['loaded_hgraph_libraries']
        assert {'libhgraph_runtime.so', 'libhgraph_wiring.so', 'libhgraph_stdlib.so'} <= set(loaded)
        assert any(name.startswith('_hgraph.') for name in loaded)
        assert {PurePosixPath(name).name: value for name, value in native.items()} == loaded
        for name, value in native.items():
            artifact = name if name in package['artifacts_sha256'] else 'hgraph/' + name
            assert package['artifacts_sha256'][artifact] == value
    else:
        assert identity['native_artifacts'] == identity['loaded_hgraph_libraries'] == {}
