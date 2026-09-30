"""Run the unchanged HGL suites through a built C++ compiler and engine."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
from shared_cases import read


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--build', type=Path, required=True)
    parser.add_argument('--stdlib', type=Path, required=True)
    parser.add_argument('--revision', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    driver = args.build / 'language/tests/hgl_stdlib_test_driver'
    generated = args.build / 'language/generated/hgl_core_native'
    native = args.source / 'language/stdlib/hgl/hgraph'
    native_cpp = args.source / 'language/stdlib/cpp'
    env = dict(os.environ)
    env['CPLUS_INCLUDE_PATH'] = os.pathsep.join([str(generated / 'include'), str(native_cpp), env.get('CPLUS_INCLUDE_PATH','')])
    rows = []
    groups = {
        'standard': ['standard.hgl','control.hgl','stream.hgl','temporal.hgl'] + [f'{folder}/{name}.hgl' for folder in ('impl','tests') for name in ('standard','control','stream','temporal')],
        'operators': ['operators.hgl','impl/operators.hgl','tests/operators.hgl'],
        'native': ['native/scalar_values.hgl','native/scalar_values_i64.hgl','native/scalar_operators.hgl','native/temporal_values.hgl','tests/native_scalar_operators.hgl'],
    }
    for name, files in groups.items():
        files = [args.stdlib / file for file in files]
        extra = []
        if name == 'native':
            files.insert(0,native / 'native.hgl')
            files += [native / f'native/impl/cpp_{part}.hgl' for part in ('scalar_values','scalar_values_i64','scalar_operators','temporal_values')]
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
    _, hashes = read(args.stdlib)
    report = dict(reference_revision=args.revision, compiler_sha256=hashlib.sha256(driver.read_bytes()).hexdigest(),
                  sources=hashes, groups=rows, tests=sum(len(row['tests']) for row in rows))
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(f"C++ HGL: {report['tests']} tests passed")


if __name__ == '__main__': main()
