"""Run the shared HGL negative-testing fixtures without changing their expectations."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def invoke(command: list[str], timeout: int) -> dict:
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=timeout)
        return dict(returncode=result.returncode, stdout=result.stdout, stderr=result.stderr,
                    timed_out=False)
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            return value.decode(errors='replace') if isinstance(value, bytes) else value or ''
        return dict(returncode=None, stdout=decoded(error.stdout), stderr=decoded(error.stderr),
                    timed_out=True)


def matches(case: dict, observed: dict) -> bool:
    result = observed['run']
    if result['timed_out'] or result['returncode'] != case['expected_exit']:
        return False
    if case['mode'] == 'test':
        checked = observed['source_check']
        if checked['timed_out'] or checked['returncode'] != 0:
            return False
        if case['expected_exit'] == 1 and ' ... FAILED' not in result['stdout'] + result['stderr']:
            return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--compiler', type=Path, required=True)
    parser.add_argument('--backend', choices=['rust', 'cpp'], required=True)
    parser.add_argument('--cases-dir', type=Path, required=True)
    parser.add_argument('--part', type=Path, action='append', default=[])
    parser.add_argument('--source-revision', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--timeout', type=int, default=900)
    args = parser.parse_args()
    if args.output.exists():
        parser.error('output exists; use a new path to preserve earlier observations')
    compiler = args.compiler.resolve()
    cases_dir = args.cases_dir.resolve()
    manifest_path = cases_dir / 'cases.json'
    document = json.loads(manifest_path.read_text())
    if document['schema_version'] != 1 or document['path_base'] != 'manifest_directory':
        raise ValueError('unsupported fixture manifest')
    manifest = document['cases']
    parts = [str(value.resolve()) for value in args.part]
    report = dict(measured_at=datetime.now(timezone.utc).isoformat(), backend=args.backend,
                  source_revision=args.source_revision, source_revision_verified_by_runner=False,
                  compiler_sha256=sha(compiler), observer_sha256=sha(Path(__file__)),
                  manifest_sha256=sha(manifest_path), parts=[dict(name=Path(p).name, sha256=sha(Path(p))) for p in parts],
                  cases=[])
    for case in manifest:
        source = (cases_dir / case['file']).resolve()
        if not source.is_relative_to(cases_dir.parent.parent) or case['mode'] not in ('test', 'reject'):
            raise ValueError(f'invalid fixture: {case}')
        if case['expected_exit'] not in (0, 1):
            raise ValueError(f'invalid expected exit: {case}')
        extra = [value for part in parts for value in ('--part', part)]
        row = dict(id=case['id'], file=case['file'], mode=case['mode'],
                   expected_exit=case['expected_exit'], source_sha256=sha(source))
        if case['mode'] == 'test':
            with tempfile.TemporaryDirectory(prefix='hgl-negative-check-') as temporary:
                check = ([str(compiler), 'emit-tests', str(source), *extra, '--out', str(Path(temporary) / 'checked.rs')]
                         if args.backend == 'rust' else [str(compiler), 'check', str(source), *extra])
                row['source_check'] = invoke(check, args.timeout)
            command = [str(compiler), 'test', str(source), *extra]
        else:
            command = [str(compiler), 'test', '--reject', str(source)]
        row['run'] = invoke(command, args.timeout)
        row['matches'] = matches(case, row)
        report['cases'].append(row)
        print(f"{case['id']}: {'match' if row['matches'] else 'MISMATCH'}", flush=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    raise SystemExit(0 if all(row['matches'] for row in report['cases']) else 1)


if __name__ == '__main__':
    main()
