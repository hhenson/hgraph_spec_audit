"""Check recorded fixture identities and outcomes; do not execute either compiler."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from observe import expectations, matches, sha


def validate(cases_dir: Path, report_path: Path) -> int:
    manifest_path = cases_dir / 'cases.json'
    manifest = json.loads(manifest_path.read_text())
    report = json.loads(report_path.read_text())
    if manifest['schema_version'] != 2 or manifest['path_base'] != 'manifest_directory':
        raise ValueError('unsupported fixture manifest')
    if report['manifest_sha256'] != sha(manifest_path):
        raise ValueError('fixture manifest differs from measured input')
    if report['observer_sha256'] != sha(Path(__file__).with_name('observe.py')):
        raise ValueError('observer differs from recorded identity')
    expected = manifest['cases']
    observed = report['cases']
    if len(expected) != len(observed) or not expected:
        raise ValueError('missing or additional observations')
    failures = []
    for case, row in zip(expected, observed):
        for key in ('id', 'file', 'mode', 'expected_exit'):
            if row[key] != case[key]:
                raise ValueError(f'{case["id"]}: changed {key}')
        if row['source_sha256'] != sha(cases_dir / case['file']):
            raise ValueError(f'{case["id"]}: changed source')
        required = expectations(case, report['cases_directory'])
        if row['expected'] != required:
            raise ValueError(f'{case["id"]}: changed outcome expectations')
        parts = [dict(file=name, sha256=sha(cases_dir / name))
                 for name in case.get('parts', [])]
        if row['part_sources'] != parts:
            raise ValueError(f'{case["id"]}: changed module parts')
        matched = matches(required, row)
        if matched != row['matches']:
            raise ValueError(f'{case["id"]}: inconsistent match flag')
        if not matched:
            failures.append(case['id'])
    if failures:
        raise ValueError(f'recorded mismatches: {failures}')
    print(f'{report["backend"]}: {len(expected)} recorded expectations checked; no fresh execution')
    return len(expected)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cases-dir', type=Path, default=Path(__file__).resolve().parents[2] / 'spec/compiler/negative_testing')
    parser.add_argument('reports', type=Path, nargs='*', default=[Path(__file__).with_name('cpp.json'), Path(__file__).with_name('rust.json')])
    args = parser.parse_args()
    for report in args.reports:
        validate(args.cases_dir, report)


if __name__ == '__main__':
    main()
