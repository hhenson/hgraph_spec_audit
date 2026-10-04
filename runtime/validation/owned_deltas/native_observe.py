"""Measure native independently retained ordinary timed structural delta values."""
import argparse
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import subprocess
HERE=Path(__file__).resolve().parent

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--executable',type=Path,required=True);p.add_argument('--sdk-include',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.exists():p.error('new output required')
    header_hashes={str(x.relative_to(a.sdk_include)):sha(x) for x in sorted(a.sdk_include.rglob('*')) if x.is_file()}
    executable_hash=sha(a.executable);reasoned_hash=sha(HERE/'reasoned.json');runs=[]
    for _ in range(3):
        raw=subprocess.run([str(a.executable.absolute())],capture_output=True,text=True)
        if raw.returncode:
            # Keep a failed measurement as such, without constructing expected observations.
            runs.append({'status':'error','returncode':raw.returncode,'stderr':raw.stderr.replace(str(Path.home()),'<private-home>')});continue
        result=json.loads(raw.stdout)
        if result['source_sha256']!=sha(HERE/'native.cpp'):raise RuntimeError('compiled source mismatch')
        result['loaded_libraries_sha256']={Path(x).name:sha(x) for x in result.pop('libraries')}
        runs.append({'status':'observed',**result})
    if any(x!=runs[0] for x in runs):raise RuntimeError('unstable native observations')
    if sha(a.executable)!=executable_hash or sha(HERE/'reasoned.json')!=reasoned_hash:raise RuntimeError('input changed')
    if header_hashes!={str(x.relative_to(a.sdk_include)):sha(x) for x in sorted(a.sdk_include.rglob('*')) if x.is_file()}:raise RuntimeError('SDK changed')
    result=runs[0];expected=json.loads((HERE/'reasoned.json').read_text())['native_expected']
    if result['status']=='observed':
        selected=expected
        result['assessment']={k:'match' if result['observed'].get(k)==v else 'divergence' for k,v in selected.items()}
    result.update(reasoned_sha256=reasoned_hash,recorder_sha256=sha(__file__),binary_sha256=executable_hash,sdk_headers_sha256=header_hashes,repeats=3,measured_at=datetime.now(timezone.utc).isoformat())
    a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(result.get('assessment',result.get('stderr')))
if __name__=='__main__':main()
