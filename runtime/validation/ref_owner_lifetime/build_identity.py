"""Bind the probe to its configured target, SDK and selected compile command."""
import json
import hashlib
from pathlib import Path
import re
import shlex
import subprocess

def cache_values(build_dir):
    cache = {}
    for line in (build_dir/'CMakeCache.txt').read_text().splitlines():
        if line and not line.startswith(('#', '//')) and '=' in line:
            key, value = line.split('=', 1)
            cache[key.split(':', 1)[0]] = value
    return cache

def include_paths(command):
    paths = []
    separate=('-I','-isystem','-iquote','-idirafter','--include-directory','--include-directory-after','/I','/external:I')
    joined=('--include-directory-after=','--include-directory=','-isystem','-iquote','-idirafter','/external:I','-I','/I')
    for index, argument in enumerate(command):
        if argument in separate and index+1 < len(command):
            paths.append(command[index+1])
        else:
            for prefix in joined:
                if argument.startswith(prefix) and argument!=prefix:
                    paths.append(argument[len(prefix):])
                    break
    return paths

def command_configuration(entry, command):
    """Require configuration clues from CMake's output and arguments to agree."""
    clues = {arg.split('=', 1)[1].strip('\\"') for arg in command if arg.startswith('-DCMAKE_INTDIR=')}
    outputs = [entry['output']] if 'output' in entry else []
    outputs += [command[index+1] for index, arg in enumerate(command[:-1]) if arg == '-o']
    if not outputs: raise ValueError('Missing declared target compile output')
    for output in outputs:
        parts = Path(output).parts
        target = 'ref_owner_lifetime_native.dir'
        if target not in parts: raise ValueError('Compile output belongs to another target')
        tail = parts[parts.index(target)+1:]
        if len(tail) > 1: clues.add(tail[0])
    if len(clues) > 1: raise ValueError('Conflicting compile-command configurations')
    return next(iter(clues), None)


def compile_command(build_dir, source, sdk_include, configuration=None, redact_paths=True):
    """Read exactly one command for the source and selected configuration."""
    entries = json.loads((build_dir / 'compile_commands.json').read_text())
    cache = cache_values(build_dir) if (build_dir/'CMakeCache.txt').is_file() else {}
    multi = bool(cache.get('CMAKE_CONFIGURATION_TYPES'))
    if multi and configuration is None: raise ValueError('Multi-config command requires selected configuration')
    matches = []
    for entry in entries:
        if (Path(entry['directory']) / entry['file']).resolve() != source.resolve(): continue
        command = entry.get('arguments')
        if command is None: command = shlex.split(entry['command'])
        if not isinstance(command, list) or not command or not all(isinstance(arg, str) for arg in command):
            raise ValueError('Invalid compile command')
        selected = command_configuration(entry, command)
        if multi and selected is None: continue
        if configuration is None or selected is None or selected == configuration:
            matches.append((command, entry['directory']))
    if len(matches) != 1: raise ValueError('Expected one native.cpp compile command for the selected configuration')
    command, directory = matches[0]
    paths = ((str(source.parent.resolve()), '<source>'),
             (str(build_dir.resolve()), '<build>'),
             (str(sdk_include.parent.resolve()), '<sdk>'),
             (str(Path.home()), '<home>'))
    def redact(argument):
        for path, label in paths: argument = argument.replace(path, label)
        return argument
    if not any((Path(directory) / include).resolve()==sdk_include.resolve() for include in include_paths(command)):
        raise ValueError('Probe compile command does not use supplied SDK headers')
    if not redact_paths:
        return command,Path(directory)
    return [redact(argument) for argument in command]

def selected_sdk_headers(build_dir,source,sdk_include,configuration=None):
    """Ask the selected compiler which SDK headers its actual lookup chooses.

    Preprocessing retains the command's flags, response files and inherited
    environment. Line directives work for GCC/Clang and MSVC without parsing
    localized diagnostics or guessing the ordering of -I and -isystem.
    """
    command,directory=compile_command(build_dir,source,sdk_include,configuration,redact_paths=False)
    msvc=any(Path(arg).name.lower() in {'cl','cl.exe','clang-cl','clang-cl.exe'} for arg in command[:3]) or '--driver-mode=cl' in command
    options=[]
    index=0
    while index<len(command):
        argument=command[index]
        if argument in ('-o','/Fo'):
            index+=2
            continue
        if argument in ('-c','/c') or argument.startswith('/Fo'):
            index+=1
            continue
        options.append(argument)
        index+=1
    preprocess=[*options,*(['/E'] if msvc else ['-E','-o','-'])]
    result=subprocess.run(preprocess,cwd=directory,capture_output=True,text=True,timeout=120)
    if result.returncode!=0:
        raise ValueError('Selected compile command could not establish header lookup')
    expected={p.relative_to(sdk_include).as_posix():p.resolve() for p in (sdk_include/'hgraph').rglob('*') if p.is_file()}
    selected={}
    for match in re.finditer(r'^\s*#\s*(?:line\s+)?\d+\s+("(?:[^"\\]|\\.)*")',result.stdout,re.MULTILINE):
        name=json.loads(match.group(1))
        if name.startswith('<'): continue
        path=(directory/name).resolve()
        parts=path.parts
        for index,part in enumerate(parts):
            if part!='hgraph': continue
            relative=Path(*parts[index:]).as_posix()
            if relative not in expected: continue
            if path!=expected[relative]:
                raise ValueError('Foreign headers shadow the supplied SDK: '+relative)
            selected['include/'+relative]=hashlib.sha256(path.read_bytes()).hexdigest()
    direct={'include/hgraph/lib/testing/eval_node.h','include/hgraph/lib/std/std_operators.h',
            'include/hgraph/lib/std/std_nodes.h','include/hgraph/types/static_node.h'}
    if not direct<=set(selected):
        raise ValueError('Selected compiler did not report every direct SDK header')
    return selected


def target_artifact(build_dir, executable):
    """Resolve only artifacts declared by the configured CMake target."""
    cache = cache_values(build_dir)
    configurations = [value for value in cache.get('CMAKE_CONFIGURATION_TYPES', '').split(';') if value]
    if not configurations:
        if 'CMAKE_BUILD_TYPE' not in cache: raise ValueError('Missing active CMake build configuration')
        configurations = [cache['CMAKE_BUILD_TYPE']]
    matches = []
    for config in configurations:
        manifest = build_dir/f'ref_owner_lifetime_target-{config}.txt'
        if not manifest.is_file(): continue
        declared = Path(manifest.read_text().splitlines()[0])
        if declared.is_absolute() and declared.resolve() == executable.resolve():
            matches.append((declared.resolve(), config, manifest))
    if len(matches) != 1: raise ValueError('Executable is not one configured ref_owner_lifetime_native target artifact')
    return matches[0]


def prepare_executable(build_dir, executable):
    artifact, config, manifest = target_artifact(build_dir, executable)
    # A newer foreign executable or object can make an incremental build lie
    # about provenance. Rebuild the configured target from clean outputs.
    command = ['cmake', '--build', str(build_dir.absolute()), '--clean-first', '--target', 'ref_owner_lifetime_native']
    if config: command += ['--config', config]
    subprocess.run(command, check=True, capture_output=True, text=True)
    if target_artifact(build_dir, executable) != (artifact, config, manifest):
        raise RuntimeError('Target artifact changed during build')
    if not artifact.is_file(): raise ValueError('Configured target executable is missing after build')
    return artifact, config, manifest


def sdk_binding(build_dir, executable, sdk):
    artifact, config, manifest = target_artifact(build_dir, executable)
    sdk = sdk.resolve()
    rows = manifest.read_text().splitlines()
    if len(rows) != 5:
        raise ValueError('Incomplete configured SDK target manifest')
    package = Path(rows[1]).resolve()
    if package != sdk/'lib/cmake/hgraph':
        raise ValueError('Configured hgraph package does not belong to the supplied SDK')
    libraries = [Path(row).resolve() for row in rows[2:]]
    if len(set(libraries)) != 3 or any(not path.is_file() or not path.is_relative_to(sdk/'lib') for path in libraries):
        raise ValueError('Configured hgraph targets do not belong to the supplied SDK')
    cache = cache_values(build_dir)
    if Path(cache['CMAKE_HOME_DIRECTORY']).resolve() != Path(__file__).resolve().parent:
        raise ValueError('Build directory belongs to another probe source')
    command = compile_command(build_dir, Path(__file__).with_name('native.cpp'), sdk/'include', config)
    return artifact, config, manifest, command, [str(path.relative_to(sdk)) for path in libraries]
