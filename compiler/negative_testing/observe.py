"""Run the shared HGL negative-testing fixtures without changing their expectations."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import posixpath
import re
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


def outcomes(output: str) -> list[dict]:
    """Read explicit case outcomes, never diagnostic prose or summary counts."""
    pattern = re.compile(r"^(?P<identity>.+?) \.\.\. (?P<status>ok|FAILED) \[(?P<kind>executed|rejection)\](?::.*)?$")
    rows = []
    for line in output.splitlines():
        match = pattern.fullmatch(line)
        if match:
            row = match.groupdict()
            row['identity'] = row['identity'].replace('\\', '/')
            row['outcome'] = 'passed' if row.pop('status') == 'ok' else 'failed'
            rows.append(row)
    return rows


def named(identity: str, name: str) -> bool:
    return identity == name or identity.endswith('::' + name)


def matches(case: dict, observed: dict) -> bool:
    result = observed['run']
    if result['timed_out'] or result['returncode'] != case['expected_exit']:
        return False
    if case.get('preflight', False):
        checked = observed.get('source_check')
        if not checked or checked['timed_out'] or checked['returncode'] != 0:
            return False
    rows = outcomes(result['stdout'])
    if len(rows) != len(case.get('runtime_results', [])) + len(case.get('rejection_results', [])):
        return False
    for field, kind in (('runtime_results', 'executed'), ('rejection_results', 'rejection')):
        for expected in case.get(field, []):
            candidates = [row for row in rows if row['kind'] == kind and (
                named(row['identity'], expected['name']) if 'name' in expected else
                row['identity'] == expected['identity'] or row['identity'].startswith(expected['identity'] + ' '))]
            if len(candidates) != 1 or candidates[0]['outcome'] != expected['outcome']:
                return False
    for name in case.get('not_executed', []):
        if any(row['kind'] == 'executed' and named(row['identity'], name) for row in rows):
            return False
    return True


def expectations(case: dict, cases_dir: Path | str) -> dict:
    """Keep portable manifest paths while deriving exact source identities."""
    result = dict(case)
    result['rejection_results'] = [
        dict(row, identity=f"{posixpath.normpath(str(cases_dir).replace(chr(92), '/') + '/' + row['file'])}:{row['owner_line']}")
        if 'file' in row else row for row in case.get('rejection_results', [])]
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--compiler', type=Path, required=True)
    parser.add_argument('--backend', choices=['rust', 'cpp'], required=True)
    parser.add_argument('--cases-dir', type=Path, required=True)
    parser.add_argument('--part', type=Path, action='append', default=[])
    parser.add_argument('--library', type=Path, action='append', default=[])
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
    if document['schema_version'] != 2 or document['path_base'] != 'manifest_directory':
        raise ValueError('unsupported fixture manifest')
    manifest = document['cases']
    if len({case['id'] for case in manifest}) != len(manifest):
        raise ValueError('duplicate fixture identity')
    parts = [str(value.resolve()) for value in args.part]
    libraries = [value.resolve() for value in args.library]
    report = dict(measured_at=datetime.now(timezone.utc).isoformat(), backend=args.backend,
                  source_revision=args.source_revision, source_revision_verified_by_runner=False,
                  compiler_sha256=sha(compiler), observer_sha256=sha(Path(__file__)),
                  manifest_sha256=sha(manifest_path), cases_directory=cases_dir.as_posix(), parts=[dict(name=Path(p).name, sha256=sha(Path(p))) for p in parts],
                  libraries=[dict(name=library.name, files=[
                      dict(file=path.relative_to(library).as_posix(), sha256=sha(path))
                      for path in sorted(library.rglob('*.hgl'))]) for library in libraries],
                  cases=[])
    for case in manifest:
        source = (cases_dir / case['file']).resolve()
        if not source.is_relative_to(cases_dir.parent.parent) or case['mode'] != 'test':
            raise ValueError(f'invalid fixture: {case}')
        if case['expected_exit'] not in (0, 1):
            raise ValueError(f'invalid expected exit: {case}')
        case_parts = [(cases_dir / part).resolve() for part in case.get('parts', [])]
        if any(not part.is_relative_to(cases_dir.parent.parent) for part in case_parts):
            raise ValueError('module part outside specification root')
        extra = [value for part in [*parts, *map(str, case_parts)] for value in ('--part', part)]
        extra += [value for library in libraries for value in ('--library', str(library))]
        row = dict(id=case['id'], file=case['file'], mode=case['mode'],
                   expected_exit=case['expected_exit'], source_sha256=sha(source),
                   part_sources=[dict(file=name, sha256=sha(path)) for name, path in zip(case.get('parts', []), case_parts)],
                   expected=expectations(case, cases_dir))
        if case['preflight']:
            with tempfile.TemporaryDirectory(prefix='hgl-negative-check-') as temporary:
                check = ([str(compiler), 'emit-tests', str(source), *extra, '--out', str(Path(temporary) / 'checked.rs')]
                         if args.backend == 'rust' else [str(compiler), 'check', str(source), *extra])
                row['source_check'] = invoke(check, args.timeout)
        command = [str(compiler), 'test', str(source), *case.get('select', []), *extra]
        row['run'] = invoke(command, args.timeout)
        row['matches'] = matches(row['expected'], row)
        report['cases'].append(row)
        print(f"{case['id']}: {'match' if row['matches'] else 'MISMATCH'}", flush=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    raise SystemExit(0 if all(row['matches'] for row in report['cases']) else 1)


if __name__ == '__main__':
    main()
