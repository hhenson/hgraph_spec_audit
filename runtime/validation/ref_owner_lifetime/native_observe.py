"""Fingerprint a frozen installed-SDK native scalar probe in three fresh processes."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def sdk_hashes(root):
    return {str(p.relative_to(root)): sha(p) for directory in ('include','lib')
            for p in sorted((root/directory).rglob('*')) if p.is_file()}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--executable',type=Path,required=True)
    parser.add_argument('--sdk',type=Path,required=True)
    parser.add_argument('--build-dir',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists(): parser.error('New evidence destination required')
    sources={name:sha(HERE/name) for name in ('native.cpp','native_reasoned.json','native_observe.py','CMakeLists.txt')}
    sdk=sdk_hashes(args.sdk)
    binary=sha(args.executable)
    runs=[]
    for _ in range(3):
        result=json.loads(subprocess.check_output([str(args.executable.absolute())],text=True,timeout=60))
        assert result['source_sha256']==sources['native.cpp']
        result['loaded_libraries_sha256']={Path(p).name:sha(p) for p in result.pop('libraries')}
        runs.append(result)
    assert all(run==runs[0] for run in runs)
    assert sources=={name:sha(HERE/name) for name in sources}
    assert sdk==sdk_hashes(args.sdk) and binary==sha(args.executable)
    reasoned=json.loads((HERE/'native_reasoned.json').read_text())
    assessment={case:'match' if [row['value'] for row in runs[0][case]]==reasoned[case+'_followed'] else 'divergence' for case in ('owned','outer_owner_control')}
    assessment['reference_identity']='match' if runs[0]['identity']==[reasoned['reference_identity']] else 'divergence'
    assessment['bool_operations']='match' if runs[0]['bool_operations']==reasoned['bool_operations'] else 'divergence'
    cache=(args.build_dir/'CMakeCache.txt').read_text().splitlines()
    compiler=next(line.split('=',1)[1] for line in cache if line.startswith('CMAKE_CXX_COMPILER:FILEPATH='))
    flags=subprocess.check_output(['ninja','-C',str(args.build_dir),' -t'.strip(), 'commands','ref_owner_lifetime_native'],text=True).splitlines()
    data={'measured_at':datetime.now(timezone.utc).isoformat(),'repeats':3,'sources_sha256':sources,
          'sdk_files_sha256':sdk,'binary_sha256':binary,'compiler_sha256':sha(compiler),
          'compiler_version':subprocess.check_output([compiler,'--version'],text=True).splitlines()[0],
          'flags':[option for option in next(line for line in flags if ' -c ' in line).split() if option.startswith(('-O','-std=','-W'))],
          **runs[0],'assessment':assessment}
    args.output.write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
    print(assessment)

if __name__=='__main__': main()
