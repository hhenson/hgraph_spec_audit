"""Record installed-SDK required reads without a Python scalar conversion."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--executable', type=Path, required=True)
    parser.add_argument('--sdk-include', type=Path, required=True)
    parser.add_argument('--build-dir', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists(): parser.error('new output destination required')
    def headers(): return {str(p.relative_to(args.sdk_include)): sha(p) for p in sorted(args.sdk_include.rglob('*')) if p.is_file()}
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
    flags = (args.build_dir / 'CMakeFiles/unset_required_reads_native.dir/flags.make').read_text().splitlines()
    result.update(measured_at=datetime.now(timezone.utc).isoformat(), repeats=3,
        source_sha256=sha(HERE/'native.cpp'), cmake_sha256=sha(HERE/'CMakeLists.txt'),
        recorder_sha256=sha(__file__), support_sha256=sha(HERE.parent/'fixed/native_loaded_libraries.h'),
        reasoned_sha256=sha(HERE/'reasoned.json'), binary_sha256=binary, sdk_headers_sha256=before,
        compiler_sha256=sha(compiler), compiler_version=subprocess.check_output([compiler,'--version'],text=True).splitlines()[0],
        flags=next(line.split('=',1)[1].strip() for line in flags if line.startswith('CXX_FLAGS =')))
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps(result['observations'], sort_keys=True))

if __name__ == '__main__': main()
