"""Compile the shared HGL stdlib cases against an installed C++ SDK and record ticks."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / 'compiler/stdlib'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def configure_command(sdk, build, extra):
    compiler = sdk / 'bin' / ('hgl.exe' if sys.platform == 'win32' else 'hgl')
    # Fresh configuration prevents cached SDK/compiler selections surviving a run.
    # Trusted definitions follow caller options, including typed -D overrides.
    return ['cmake', *extra, '--fresh', '-S', str(CORPUS / 'native'), '-B', str(build),
            '-DCMAKE_BUILD_TYPE=Release', '-DCMAKE_PREFIX_PATH=' + str(sdk),
            '-Dhgraph_DIR=' + str(sdk / 'lib/cmake/hgraph'),
            '-DHGL_EXECUTABLE=' + str(compiler), '-DPython_EXECUTABLE=' + sys.executable]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sdk', type=Path, required=True)
    parser.add_argument('--build-dir', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--parallel', type=int, default=2)
    parser.add_argument('--cmake-arg', action='append', default=[])
    args = parser.parse_args()
    sdk, build = args.sdk.resolve(), args.build_dir.resolve()
    if args.parallel < 1:
        parser.error('--parallel must be positive')
    if args.output.exists():
        parser.error('output exists; use a new path and review before replacing recorded evidence')
    if build == ROOT or build.is_relative_to(CORPUS):
        parser.error('build directory must be outside the corpus')
    # A matching library name is insufficient: the installed HGL must match our pin.
    sources = {}
    for source in sorted((ROOT / 'stdlib/hgl/hgraph').rglob('*.hgl')):
        relative = source.relative_to(ROOT / 'stdlib/hgl')
        installed = sdk / 'share/hgl/stdlib' / relative
        if sha(source) != sha(installed):
            raise SystemExit(f'SDK standard-library source differs from pin: {relative}')
        sources[str(relative)] = sha(source)
    if not sources:
        parser.error('stdlib dependency is missing; initialize submodules first')
    subprocess.run(configure_command(sdk, build, args.cmake_arg), check=True)
    subprocess.run(['cmake', '--build', str(build), '--config', 'Release',
                    '--parallel', str(args.parallel)], check=True)
    executable = build / ('stdlib_conformance.exe' if sys.platform == 'win32' else 'stdlib_conformance')
    if not executable.exists():
        executable = build / 'Release' / executable.name
    runs = []
    expected = {c['name']: c['expected'] for c in json.loads((CORPUS / 'cases.json').read_text())}
    for _ in range(3):
        result = subprocess.run([str(executable)], capture_output=True, text=True)
        rows = [json.loads(line) for line in result.stdout.splitlines() if line.startswith('{')]
        observations = {row['name']: {'ticks': row['ticks'], 'matches': row['ticks'] == expected[row['name']]} for row in rows}
        if result.returncode or set(observations) != set(expected) or len(rows) != len(expected):
            raise SystemExit('HGL execution failed: ' + result.stdout + result.stderr)
        runs.append(observations)
    if not all(run == runs[0] for run in runs) or not all(row['matches'] for row in runs[0].values()):
        raise SystemExit('Unstable or mismatching HGL ticks; review observations before recording')
    compiler = sdk / 'bin' / ('hgl.exe' if sys.platform == 'win32' else 'hgl')
    report = {
        'measured_at': datetime.now(timezone.utc).isoformat(),
        'runtime_test_status': 'passed', 'runtime_test_exit_code': 0,
        'execution': 'shared HGL imports compiled to C++, linked to the installed HGL standard library',
        'repeats': len(runs), 'observed': runs[0],
        'checked_source_sha256': {name: sha(CORPUS / name) for name in ('nodes.hgl', 'cases.hgl', 'cases.json')},
        'harness_sha256': {name: sha(ROOT / name) for name in ('tools/run_stdlib.py', 'tools/stdlib_cases.py', 'compiler/stdlib/native/main.cpp', 'compiler/stdlib/native/CMakeLists.txt')},
        'stdlib_source_sha256': sources, 'compiler_sha256': sha(compiler),
        'compiler_version': subprocess.check_output([str(compiler), '--version'], text=True).strip(),
        'executable_sha256': sha(executable),
        'sdk_libraries_sha256': {str(p.relative_to(sdk)): sha(p) for p in sorted((sdk / 'lib').glob('*hgl*')) if p.is_file()},
        'replay_digests': [hashlib.sha256(json.dumps(run, sort_keys=True).encode()).hexdigest() for run in runs],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(f'{len(expected)} scenarios, {sum(map(len, expected.values()))} tick cells, three identical runs')


if __name__ == '__main__':
    main()
