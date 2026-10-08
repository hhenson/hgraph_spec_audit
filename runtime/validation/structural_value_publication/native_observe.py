"""Record a genuine native owned-value copy through an installed SDK graph."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--executable', type=Path, required=True)
    parser.add_argument('--sdk-include', type=Path, required=True)
    parser.add_argument('--build-dir', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists(): parser.error('new output destination required')
    headers = {str(p.relative_to(args.sdk_include)): sha(p) for p in sorted(args.sdk_include.rglob('*')) if p.is_file()}
    binary_hash = sha(args.executable)
    reasoned = HERE / 'native_reasoned.json'
    reasoned_hash = sha(reasoned)
    expected = json.loads(reasoned.read_text())['expected']
    runs = []
    for _ in range(3):
        raw = subprocess.run([str(args.executable.absolute())], capture_output=True, text=True, timeout=120)
        if raw.returncode:
            runs.append({'status': 'error', 'returncode': raw.returncode,
                         'stderr': raw.stderr.replace(str(Path.home()), '<private-home>')})
            continue
        result = json.loads(raw.stdout)
        assert result['source_sha256'] == sha(HERE / 'native.cpp')
        result['loaded_libraries_sha256'] = {Path(p).name: sha(p) for p in result.pop('libraries')}
        runs.append({'status': 'observed', **result})
    if any(run != runs[0] for run in runs): raise RuntimeError('unstable native observations')
    if sha(args.executable) != binary_hash or sha(reasoned) != reasoned_hash:
        raise RuntimeError('measurement input changed')
    if headers != {str(p.relative_to(args.sdk_include)): sha(p) for p in sorted(args.sdk_include.rglob('*')) if p.is_file()}:
        raise RuntimeError('SDK changed')
    evidence = runs[0]
    if evidence['status'] == 'observed':
        evidence['assessment'] = {}
        for name, wanted in expected.items():
            # Preserve raw recorded strings; parse only to assess their observed child state.
            rows = [json.loads(row) if row is not None else {} for row in evidence['observed'][name]['raw_eval_node']]
            got = [row.get('output', {}).get('children') for row in rows]
            source = [row.get('source', {}).get('children') for row in rows]
            evidence['assessment'][name] = {'state': 'match' if json.dumps(got, sort_keys=True) == json.dumps(wanted, sort_keys=True) else 'divergence',
                                             'source': 'match' if json.dumps(source, sort_keys=True) == json.dumps(wanted, sort_keys=True) else 'divergence'}
    cache = (args.build_dir / 'CMakeCache.txt').read_text().splitlines()
    compiler = next(line.split('=', 1)[1] for line in cache if line.startswith('CMAKE_CXX_COMPILER:FILEPATH='))
    flags = (args.build_dir / 'CMakeFiles/structural_value_publication_native.dir/flags.make').read_text().splitlines()
    evidence.update(measured_at=datetime.now(timezone.utc).isoformat(), repeats=3,
                    reasoned_sha256=reasoned_hash, recorder_sha256=sha(__file__),
                    binary_sha256=binary_hash, sdk_headers_sha256=headers,
                    compiler_version=subprocess.check_output([compiler, '--version'], text=True).splitlines()[0],
                    compiler_sha256=sha(compiler),
                    flags=next(line.split('=', 1)[1].strip() for line in flags if line.startswith('CXX_FLAGS =')))
    args.output.write_text(json.dumps(evidence, sort_keys=True, indent=2) + '\n')
    print(evidence.get('assessment', evidence.get('stderr')))


if __name__ == '__main__': main()
