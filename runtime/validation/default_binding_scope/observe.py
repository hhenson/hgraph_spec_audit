"""Run frozen ordinary-language probes without a compiler-under-development."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
NAMES = ('reasoned.json', 'python_probe.py', 'positive.cpp', 'earlier_parameter.cpp', 'shadow_parameter.cpp', 'observe.py')
SUPPORT = ('delta_eval/observe.py', 'fixed/reference_identity.py', 'fixed/native_identity.py')
FLAGS = ('-std=c++20', '-O0', '-Wall', '-Wextra')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()

def normalized(text, build):
    return text.replace(str(HERE), '<probe>').replace(str(build), '<build>')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--python', type=Path, required=True)
    parser.add_argument('--compiler', type=Path, required=True)
    parser.add_argument('--build-dir', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists() or args.build_dir.exists():
        parser.error('New evidence and isolated build destinations required')
    args.build_dir.mkdir(parents=True)
    sources = {name: sha(HERE / name) for name in NAMES}
    support = {name: sha(HERE.parent / name) for name in SUPPORT}
    compiler = args.compiler.resolve()
    compiler_sha = sha(compiler)
    python = [json.loads(subprocess.check_output([str(args.python.absolute()), str(HERE / 'python_probe.py')], text=True, timeout=60)) for _ in range(3)]
    assert all(run == python[0] for run in python)
    assert python[0]['identity']['native'] is False
    binary = args.build_dir / 'default_scope'
    build = subprocess.run([str(compiler), *FLAGS, str(HERE / 'positive.cpp'), '-o', str(binary)], capture_output=True, text=True, timeout=60)
    assert build.returncode == 0, normalized(build.stderr, args.build_dir)
    binary_sha = sha(binary)
    cpp = [json.loads(subprocess.check_output([str(binary)], text=True, timeout=60)) for _ in range(3)]
    assert all(run == cpp[0] for run in cpp)
    rejected = {}
    for name in ('earlier_parameter', 'shadow_parameter'):
        runs = [subprocess.run([str(compiler), *FLAGS, '-fsyntax-only', str(HERE / (name + '.cpp'))], capture_output=True, text=True, timeout=60) for _ in range(3)]
        captures = [{'exit_code': run.returncode, 'stdout': normalized(run.stdout, args.build_dir), 'stderr': normalized(run.stderr, args.build_dir)} for run in runs]
        assert all(run == captures[0] for run in captures)
        rejected[name] = {'capture': captures[0], 'runs_sha256': [digest(run) for run in captures]}
    assert sources == {name: sha(HERE / name) for name in NAMES}
    assert support == {name: sha(HERE.parent / name) for name in SUPPORT}
    assert compiler_sha == sha(compiler) and binary_sha == sha(binary)
    record = {'measured_at': datetime.now(timezone.utc).isoformat(), 'repeats': 3,
              'sources_sha256': sources, 'support_sha256': support,
              'python': {**python[0], 'runs_sha256': [digest(run) for run in python]},
              'cpp': {'results': cpp[0], 'runs_sha256': [digest(run) for run in cpp],
                      'rejections': rejected, 'binary_sha256': binary_sha,
                      'compiler_sha256': compiler_sha,
                      'compiler_version': subprocess.check_output([str(compiler), '--version'], text=True).splitlines()[0],
                      'flags': list(FLAGS), 'build': {'exit_code': build.returncode, 'stdout': normalized(build.stdout, args.build_dir), 'stderr': normalized(build.stderr, args.build_dir)}}}
    args.output.write_text(json.dumps(record, sort_keys=True, indent=2) + '\n')
    print('python', python[0]['results'])
    print('cpp', cpp[0], {name: r['capture']['exit_code'] for name, r in rejected.items()})

if __name__ == '__main__':
    main()
