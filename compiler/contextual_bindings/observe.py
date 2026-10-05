"""Run shared contextual-binding cases with an existing C++ HGL executable."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile


HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def invoke(executable, command, source=None):
    args = ([str(executable), command[0], source.name, *command[1:]]
            if source is not None else [str(executable), *command])
    result = subprocess.run(args, cwd=source.parent if source else None,
                            capture_output=True, text=True, timeout=120)
    return dict(command=command, returncode=result.returncode,
                stdout=result.stdout, stderr=result.stderr)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--hgl', type=Path, required=True)
    parser.add_argument('--cases-dir', type=Path,
                        default=HERE.parents[1] / 'spec/compiler/contextual_bindings')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    executable = args.hgl.resolve()
    cases_dir = args.cases_dir.resolve()
    manifest = json.loads((cases_dir / 'cases.json').read_text())
    report = dict(measured_at=datetime.now(timezone.utc).isoformat(),
                  engine='cpp-hgl', scope='existing-binary focused compiler probe',
                  binary_sha256=sha(executable), version=invoke(executable, ['--version']),
                  build=dict(rebuilt=False, source_revision_verified=False),
                  harness_sha256=sha(__file__), manifest_sha256=sha(cases_dir / 'cases.json'),
                  cases=[])
    with tempfile.TemporaryDirectory(prefix='contextual-bindings-') as temporary:
        for case in manifest:
            name = case['file']
            if Path(name).name != name or not name.endswith('.hgl'):
                raise ValueError(f'invalid case filename: {name}')
            source = Path(temporary) / name
            source.write_bytes((cases_dir / name).read_bytes())
            check = invoke(executable, ['check'], source)
            accepted = check['returncode'] == 0
            expected_diagnostic = case.get('diagnostic_contains')
            row = dict(id=case['id'], file=name, source_sha256=sha(source),
                       expected_check=case['check'], check=check,
                       matches=(accepted if case['check'] == 'accept' else check['returncode'] == 1))
            if expected_diagnostic:
                row['expected_diagnostic_contains'] = expected_diagnostic
                row['matches'] &= expected_diagnostic in check['stderr']
            if case.get('test') and accepted:
                row['test'] = invoke(executable, ['test'], source)
                row['matches'] &= row['test']['returncode'] == 0
            if case.get('dump_ir') and accepted:
                row['ir'] = invoke(executable, ['check', '--dump-hgraph-ir'], source)
            report['cases'].append(row)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    failed = [case['id'] for case in report['cases'] if not case['matches']]
    print(f"{len(report['cases'])} cases observed; mismatches: {failed}")
    raise SystemExit(bool(failed))


if __name__ == '__main__':
    main()
