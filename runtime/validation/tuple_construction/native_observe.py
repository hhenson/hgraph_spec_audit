"""Record direct C++ std::tuple argument expressions, not hgraph structural tuples."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cxx', default='g++')
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        parser.error('output must be a new destination')
    compiler = Path(shutil.which(args.cxx) or args.cxx).resolve(strict=True)
    source = HERE / 'native_call.cpp'
    expected_path = HERE / 'reasoned.json'
    expected_hash = sha(expected_path)
    expected = json.loads(expected_path.read_text())['native_call_target']
    flags = ['-std=c++23', '-O2', '-Wall', '-Wextra', '-Werror']
    with tempfile.TemporaryDirectory() as directory:
        binary = Path(directory) / 'tuple-call'
        subprocess.run([str(compiler), *flags, str(source), '-o', str(binary)], check=True, timeout=60)
        runs = [json.loads(subprocess.check_output([str(binary)], text=True, timeout=10)) for _ in range(3)]
        if any(run != runs[0] for run in runs):
            raise RuntimeError('unstable native observations')
        observed = runs[0]
        evidence = {
            'measured_at': datetime.now(timezone.utc).isoformat(), 'repeats': 3,
            'scope': 'C++ standard-library tuple constructor argument expressions; no hgraph runtime or TST',
            'compiler': compiler.name, 'compiler_sha256': sha(compiler),
            'compiler_version': subprocess.check_output([str(compiler), '--version'], text=True).splitlines()[0],
            'flags': flags, 'binary_sha256': sha(binary), 'source_sha256': sha(source),
            'recorder_sha256': sha(__file__), 'reasoned_sha256': expected_hash,
            'observed': observed,
            'assessment': {key: 'match' if observed[key] == value else 'variation'
                           for key, value in expected.items()}}
    if sha(expected_path) != expected_hash:
        raise RuntimeError('expectations changed during measurement')
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')
    print(evidence['observed'], evidence['assessment'])


if __name__ == '__main__':
    main()
