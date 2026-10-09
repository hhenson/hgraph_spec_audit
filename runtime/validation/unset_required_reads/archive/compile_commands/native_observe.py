"""Record installed-SDK required reads without a Python scalar conversion."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import shlex

HERE = Path(__file__).resolve().parent

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def compile_command(build_dir, source, sdk_include):
    """Read the native translation unit's command for Make or Ninja builds."""
    entries = json.loads((build_dir / 'compile_commands.json').read_text())
    matches = [entry for entry in entries
               if (Path(entry['directory']) / entry['file']).resolve() == source.resolve()]
    if len(matches) != 1: raise ValueError('Expected one native.cpp compile command')
    entry = matches[0]
    command = entry.get('arguments')
    if command is None: command = shlex.split(entry['command'])
    if not isinstance(command, list) or not command or not all(isinstance(arg, str) for arg in command):
        raise ValueError('Invalid compile command')
    paths = ((str(source.parent.resolve()), '<source>'),
             (str(build_dir.resolve()), '<build>'),
             (str(sdk_include.parent.resolve()), '<sdk>'),
             (str(Path.home()), '<home>'))
    def redact(argument):
        for path, label in paths: argument = argument.replace(path, label)
        return argument
    return [redact(argument) for argument in command]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--executable', type=Path, required=True)
    parser.add_argument('--sdk-include', type=Path, required=True)
    parser.add_argument('--build-dir', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists(): parser.error('new output destination required')
    def headers(): return {str(p.relative_to(args.sdk_include)): sha(p) for p in sorted(args.sdk_include.rglob('*')) if p.is_file()}
    command = compile_command(args.build_dir, HERE/'native.cpp', args.sdk_include)
    command_hash = sha(args.build_dir/'compile_commands.json')
    before = headers()
    binary = sha(args.executable)
    runs = []
    for _ in range(3):
        result = json.loads(subprocess.check_output([str(args.executable.absolute())], text=True, timeout=120))
        result['loaded_libraries_sha256'] = {Path(p).name: sha(p) for p in result.pop('libraries')}
        runs.append(result)
    if any(run != runs[0] for run in runs): raise RuntimeError('Unstable native observations')
    if before != headers() or binary != sha(args.executable): raise RuntimeError('SDK changed')
    result = runs[0]
    cache = (args.build_dir / 'CMakeCache.txt').read_text().splitlines()
    compiler = next(line.split('=',1)[1] for line in cache if line.startswith('CMAKE_CXX_COMPILER:FILEPATH='))
    result.update(measured_at=datetime.now(timezone.utc).isoformat(), repeats=3,
        source_sha256=sha(HERE/'native.cpp'), cmake_sha256=sha(HERE/'CMakeLists.txt'),
        recorder_sha256=sha(__file__), support_sha256=sha(HERE.parent/'fixed/native_loaded_libraries.h'),
        reasoned_sha256=sha(HERE/'reasoned.json'), binary_sha256=binary, sdk_headers_sha256=before,
        compiler_sha256=sha(compiler), compiler_version=subprocess.check_output([compiler,'--version'],text=True).splitlines()[0],
        compile_command=command, compile_commands_sha256=command_hash,
        cmake_generator=next(line.split('=',1)[1] for line in cache if line.startswith('CMAKE_GENERATOR:INTERNAL=')))
    if command_hash != sha(args.build_dir/'compile_commands.json'): raise RuntimeError('Compile commands changed')
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps(result['observations'], sort_keys=True))

if __name__ == '__main__': main()
