"""Record direct native eval_node output without synthesizing missing cycles."""
import argparse
from datetime import date,datetime,time,timezone
import hashlib
import json
from pathlib import Path
import subprocess
HERE=Path(__file__).resolve().parent

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def encode_expected(value):
    if not isinstance(value,dict): return value
    if 'date' in value: return (date.fromisoformat(value['date'])-date(1970,1,1)).days
    if 'time' in value:
        t=time.fromisoformat(value['time']); return ((t.hour*60+t.minute)*60+t.second)*1000000+t.microsecond
    if 'datetime' in value:
        d=datetime.fromisoformat(value['datetime'])-datetime(1970,1,1)
        return (d.days*86400+d.seconds)*1000000+d.microseconds
    if 'duration_us' in value: return value['duration_us']
    raise ValueError(value)
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--executable',type=Path,required=True)
    parser.add_argument('--sdk-include',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists(): parser.error('output already exists')
    binary_hash=sha(args.executable)
    header_manifest={p.relative_to(args.sdk_include).as_posix():sha(p) for p in sorted(args.sdk_include.rglob('*')) if p.is_file()}
    runs=[]
    for _ in range(3):
        run=json.loads(subprocess.check_output([str(args.executable.absolute())],text=True))
        if run['source_sha256']!=sha(HERE/'native_scalar.cpp'): raise RuntimeError('source identity mismatch')
        # Actual loaded libraries are reported by the native process. Keep paths private.
        run['loaded_libraries_sha256']={Path(p).name:sha(p) for p in run.pop('libraries')}
        runs.append(run)
    if any(r!=runs[0] for r in runs): raise RuntimeError('unstable native observation')
    if binary_hash!=sha(args.executable): raise RuntimeError('binary changed during observation')
    after={p.relative_to(args.sdk_include).as_posix():sha(p) for p in sorted(args.sdk_include.rglob('*')) if p.is_file()}
    if after!=header_manifest: raise RuntimeError('headers changed during observation')
    expected={c['id']:[encode_expected(v) for v in c['expected']] for c in json.loads((HERE/'reasoned.json').read_text())['cases'] if c['type'] in ('bool','i64','f64','str','date','time','datetime','duration')}
    result=runs[0]
    if set(result['observed'])!=set(expected): raise RuntimeError('native case coverage mismatch')
    result.update(repeats=3,measured_at=datetime.now(timezone.utc).isoformat(),binary_sha256=binary_hash,
                  recorder_sha256=sha(__file__),reasoned_sha256=sha(HERE/'reasoned.json'),sdk_headers_sha256=header_manifest,
                  assessment={k:'match' if v==result['observed'][k] else 'divergence' for k,v in expected.items()},
                  output_encoding='Raw C++ eval_node vector. Date=epoch days, time=midnight microseconds, datetime=epoch microseconds, duration=microseconds. No adapter padding.')
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    from collections import Counter
    print(dict(Counter(result['assessment'].values())))
if __name__=='__main__': main()
