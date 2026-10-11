"""Fingerprint a frozen installed-SDK native scalar probe in three fresh processes."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
from build_identity import cache_values, loaded_sdk_libraries, prepare_executable, sdk_binding

HERE = Path(__file__).resolve().parent

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def sdk_hashes(root):
    return {p.relative_to(root).as_posix(): sha(p) for directory in ('include','lib','bin')
            for p in sorted((root/directory).rglob('*')) if p.is_file()}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--executable',type=Path,required=True)
    parser.add_argument('--sdk',type=Path,required=True)
    parser.add_argument('--build-dir',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists(): parser.error('New evidence destination required')
    sources={name:sha(HERE/name) for name in ('native.cpp','native_reasoned.json','native_observe.py','CMakeLists.txt','build_identity.py')}
    artifact, config, manifest, command, libraries = sdk_binding(args.build_dir, args.executable, args.sdk)
    sdk=sdk_hashes(args.sdk)
    prepare_executable(args.build_dir, args.executable)
    if sdk_binding(args.build_dir, args.executable, args.sdk) != (artifact, config, manifest, command, libraries):
        raise RuntimeError('Configured target changed during build')
    manifest_hash=sha(manifest)
    command_hash=sha(args.build_dir/'compile_commands.json')
    cache_hash=sha(args.build_dir/'CMakeCache.txt')
    compiler=Path(cache_values(args.build_dir)['CMAKE_CXX_COMPILER']).resolve()
    compiler_hash=sha(compiler)
    compiler_version=subprocess.check_output([str(compiler),'--version'],text=True).splitlines()[0]
    binary=sha(artifact)
    runs=[]
    for _ in range(3):
        result=json.loads(subprocess.check_output([str(artifact)],text=True,timeout=60))
        assert result['source_sha256']==sources['native.cpp']
        loaded=loaded_sdk_libraries(result.pop('libraries'), args.sdk, sdk, libraries)
        result['loaded_sdk_libraries_sha256']=loaded
        result['loaded_libraries_sha256']={Path(p).name:fingerprint for p,fingerprint in loaded.items()}
        runs.append(result)
    assert all(run==runs[0] for run in runs)
    assert sources=={name:sha(HERE/name) for name in sources}
    assert sdk==sdk_hashes(args.sdk) and binary==sha(args.executable)
    reasoned=json.loads((HERE/'native_reasoned.json').read_text())
    assessment={name:'match' if runs[0]['observed'][name]==value else 'divergence'
                for name,value in reasoned['expected'].items()}
    for name in reasoned['capability_expectations']:
        assessment[name]='match' if isinstance(runs[0]['observed'][name],dict) and 'error' in runs[0]['observed'][name] else 'divergence'
    assessment.update({name+'_graph':'match' if runs[0]['graphs'][name]==value else 'divergence'
                       for name,value in reasoned['graph_expected'].items()})
    assert manifest_hash==sha(manifest) and command_hash==sha(args.build_dir/'compile_commands.json')
    assert cache_hash==sha(args.build_dir/'CMakeCache.txt') and compiler_hash==sha(compiler)
    assert sdk_binding(args.build_dir, args.executable, args.sdk) == (artifact, config, manifest, command, libraries)
    data={'measured_at':datetime.now(timezone.utc).isoformat(),'repeats':3,'sources_sha256':sources,
          'sdk_files_sha256':sdk,'binary_sha256':binary,'compiler_sha256':compiler_hash,
          'compiler_version':compiler_version,
          'compile_command':command,'compile_commands_sha256':command_hash,
          'target_name':'last_scalar_types_native','target_configuration':config,
          'target_artifact':artifact.relative_to(args.build_dir.resolve()).as_posix(),
          'target_manifest_sha256':manifest_hash,'cmake_cache_sha256':cache_hash,
          'cmake_generator':cache_values(args.build_dir)['CMAKE_GENERATOR'],
          'sdk_target_libraries':libraries,
          **runs[0],'assessment':assessment}
    data['measurement_sha256']=hashlib.sha256(json.dumps(data,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    args.output.write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
    print(assessment)

if __name__=='__main__': main()
