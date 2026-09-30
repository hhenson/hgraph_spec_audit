"""Run the unchanged HGL suites through a built C++ compiler and engine."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess


GROUPS = {
    'standard': ['standard.hgl','control.hgl','stream.hgl','temporal.hgl'] + [f'{folder}/{name}.hgl' for folder in ('impl','tests') for name in ('standard','control','stream','temporal')],
    'operators': ['operators.hgl','impl/operators.hgl','tests/operators.hgl'],
    'native': ['native/scalar_values.hgl','native/scalar_values_i64.hgl','native/scalar_operators.hgl','native/temporal_values.hgl','tests/native_scalar_operators.hgl'],
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stdlib_sources(stdlib):
    return {name: digest(stdlib / name) for name in sorted({file for files in GROUPS.values() for file in files})}


def source_revision(source, expected=None):
    source = source.resolve()
    def git(*args):
        return subprocess.check_output(['git', '-C', str(source), *args], text=True).strip()
    if Path(git('rev-parse', '--show-toplevel')).resolve() != source:
        raise ValueError('--source must be the root of a Git checkout')
    revision = git('rev-parse', 'HEAD')
    if expected is not None and expected != revision:
        raise ValueError(f'expected revision {expected}, source HEAD is {revision}')
    subprocess.run(['git', '-C', str(source), 'diff', '--quiet', 'HEAD', '--'], check=True)
    return revision


def build_source(build):
    cache = (build / 'CMakeCache.txt').read_text()
    match = re.search(r'^CMAKE_HOME_DIRECTORY:INTERNAL=(.+)$', cache, re.M)
    if not match:
        raise ValueError('build has no CMake source directory')
    return Path(match[1]).resolve()


def rebuild(source, build, revision, jobs):
    if build_source(build) != source.resolve():
        raise ValueError('build was configured from a different source checkout')
    subprocess.run(['cmake', '-S', str(source), '-B', str(build)], check=True)
    subprocess.run(['cmake', '--build', str(build), '--clean-first', '--target',
                    'hgl_stdlib_test_driver', '--parallel', str(jobs)], check=True)
    source_revision(source, revision)
    return dict(source_revision=revision, clean_rebuild=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--build', type=Path, required=True)
    parser.add_argument('--stdlib', type=Path, required=True)
    parser.add_argument('--revision', help='Expected source HEAD (optional full commit hash)')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--jobs', type=int, default=8)
    args = parser.parse_args()
    if args.jobs < 1:
        parser.error('--jobs must be positive')
    revision = source_revision(args.source, args.revision)
    build = rebuild(args.source, args.build, revision, args.jobs)
    driver = args.build / 'language/tests/hgl_stdlib_test_driver'
    generated = args.build / 'language/generated/hgl_core_native'
    native = args.source / 'language/stdlib/hgl/hgraph'
    native_cpp = args.source / 'language/stdlib/cpp'
    env = dict(os.environ)
    env['CPLUS_INCLUDE_PATH'] = os.pathsep.join([str(generated / 'include'), str(native_cpp), env.get('CPLUS_INCLUDE_PATH','')])
    rows = []
    sources = stdlib_sources(args.stdlib)
    native_sources = {}
    for name, files in GROUPS.items():
        files = [args.stdlib / file for file in files]
        extra = []
        if name == 'native':
            native_parts = [native / 'native.hgl'] + [native / f'native/impl/cpp_{part}.hgl' for part in ('scalar_values','scalar_values_i64','scalar_operators','temporal_values')]
            files = native_parts[:1] + files + native_parts[1:]
            native_sources = {file.relative_to(args.source).as_posix(): digest(file) for file in native_parts}
            extra = ['--native-provider-header','native_scalar.h','--native-provider','hgl::stdlib::scalar_native']
        else:
            extra = ['--module-descriptor',str(generated / 'src/native.hgl-module.json')]
        command = [str(driver),'test',str(files[0])]
        for file in files[1:]: command += ['--part',str(file)]
        output = subprocess.run(command+extra, env=env, capture_output=True, text=True)
        tests = re.findall(r'^(\w+) \.\.\. (ok|FAILED.*)$',output.stdout,re.M)
        row = dict(group=name, passed=output.returncode == 0, tests=[dict(name=n,result=r) for n,r in tests])
        if output.returncode:
            # Diagnostics may contain private build paths; keep them local.
            raise RuntimeError(output.stdout + output.stderr)
        rows.append(row)
    source_revision(args.source, revision)
    if sources != stdlib_sources(args.stdlib):
        raise RuntimeError('standard-library sources changed during the run')
    report = dict(reference_revision=revision, build=build, compiler_sha256=digest(driver),
                  harness_sha256=digest(Path(__file__)), sources=sources,
                  native_sources=dict(sorted(native_sources.items())),
                  descriptor_sha256=digest(generated / 'src/native.hgl-module.json'),
                  provider_header_sha256=digest(native_cpp / 'native_scalar.h'),
                  groups=rows, tests=sum(len(row['tests']) for row in rows))
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(f"C++ HGL: {report['tests']} tests passed")


if __name__ == '__main__': main()
