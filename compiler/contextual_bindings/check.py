"""Verify the bounded recorded observations; do not rerun a compiler."""
import argparse
import json
from pathlib import Path

from observe import HERE, sha


VARIATIONS = {
    'conditional_initial_port_change', 'conditional_initial_scalar_change',
    'node_atomic_composite', 'port_to_scalar', 'scalar_to_port',
    'unused_category_change', 'conditional_unused_scalar_write',
    'uninitialized_scalar_to_port',
}


def validate(cases_dir):
    manifest = json.loads((cases_dir / 'cases.json').read_text())
    report = json.loads((HERE / 'cpp.json').read_text())
    assert report['harness_sha256'] == sha(HERE / 'observe.py')
    assert report['manifest_sha256'] == sha(cases_dir / 'cases.json')
    assert report['engine'] == 'cpp-hgl'
    assert report['build'] == dict(rebuilt=False, source_revision_verified=False)
    assert len(manifest) == len(report['cases']) == 20
    assert report['version']['returncode'] == 0
    failures, tests = set(), 0
    for expected, row in zip(manifest, report['cases']):
        assert row['id'] == expected['id']
        assert row['file'] == expected['file']
        assert row['source_sha256'] == sha(cases_dir / expected['file'])
        assert row['expected_check'] == expected['check']
        check = row['check']
        assert check['command'] == ['check']
        assert check['returncode'] in (0, 1)
        matches = check['returncode'] == (0 if expected['check'] == 'accept' else 1)
        if diagnostic := expected.get('diagnostic_contains'):
            assert row['expected_diagnostic_contains'] == diagnostic
            matches &= diagnostic in check['stderr']
        if expected.get('test'):
            tests += 1
            assert row['test']['command'] == ['test']
            assert row['test']['returncode'] == 0
            assert f"{row['id']} ... ok\n1 test, 0 failed\n" == row['test']['stdout']
            assert row['test']['stderr'] == ''
        assert row['matches'] == matches
        if not matches:
            failures.add(row['id'])
        if row['id'] in {'unused_category_change', 'conditional_unused_scalar_write'}:
            assert "backend: 'local' is declared but never read" in check['stderr']
        elif row['id'] in VARIATIONS:
            assert check['returncode'] == 0
        if expected.get('dump_ir'):
            assert row['ir']['returncode'] == 0
            assert 'phase=runtime kind=runtime-value' in row['ir']['stdout']
    assert tests == 6
    assert failures == VARIATIONS
    print('20 recorded C++ cases checked: six runtime tests passed; eight documented variations; no fresh measurement.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cases-dir', type=Path,
                        default=HERE.parents[1] / 'spec/compiler/contextual_bindings')
    validate(parser.parse_args().cases_dir)
