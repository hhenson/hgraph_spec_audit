"""Bind the probe to its configured target, SDK and selected compile command."""
import hashlib
import json
from pathlib import Path, PureWindowsPath
import shlex
import subprocess

def split_windows_command(value):
    """Split CMake's MSVC command using Windows backslash/quote rules."""
    arguments = []
    index = 0
    while index < len(value):
        while index < len(value) and value[index].isspace(): index += 1
        if index == len(value): break
        token = []
        quoted = False
        while index < len(value) and (quoted or not value[index].isspace()):
            slashes = 0
            while index < len(value) and value[index] == '\\':
                slashes += 1
                index += 1
            if index < len(value) and value[index] == '"':
                token.extend('\\' * (slashes // 2))
                if slashes % 2: token.append('"')
                elif quoted and index+1 < len(value) and value[index+1] == '"':
                    token.append('"')
                    index += 1
                else: quoted = not quoted
                index += 1
            else:
                token.extend('\\' * slashes)
                if index < len(value) and (quoted or not value[index].isspace()):
                    token.append(value[index])
                    index += 1
        if quoted: raise ValueError('Unterminated Windows command quote')
        arguments.append(''.join(token))
    return arguments


def unquote(value):
    return value[1:-1] if len(value) >= 2 and value[0] == value[-1] == '"' else value


def include_paths(command):
    """Extract actual include operands for GCC/Clang and MSVC."""
    prefixes = ('-isystem', '-external:I', '-I', '/external:I', '/I')
    paths = []
    index = 0
    while index < len(command):
        argument = unquote(command[index])
        for prefix in prefixes:
            if argument == prefix:
                index += 1
                if index == len(command): raise ValueError('Missing include path operand')
                paths.append(unquote(command[index]))
                break
            if argument.startswith(prefix):
                paths.append(unquote(argument[len(prefix):]))
                break
        index += 1
    return paths

def shared_library(path):
    name = Path(path).name.lower()
    return name.endswith(('.dll', '.dylib', '.so')) or '.so.' in name


def loaded_sdk_libraries(paths, sdk, sdk_hashes, target_libraries):
    """Bind actual loader paths and bytes to the supplied SDK, not basenames."""
    sdk = sdk.resolve()
    loaded = {}
    names = set()
    for value in paths:
        path = Path(value).resolve(strict=True)
        if not shared_library(path):
            raise ValueError('Loaded hgraph library is not a shared artifact')
        if not path.is_relative_to(sdk):
            raise ValueError('Loaded hgraph library does not belong to supplied SDK')
        relative = path.relative_to(sdk).as_posix()
        fingerprint = hashlib.sha256(path.read_bytes()).hexdigest()
        if relative not in sdk_hashes or sdk_hashes[relative] != fingerprint:
            raise ValueError('Loaded hgraph library does not match supplied SDK manifest')
        if path.name in names:
            raise ValueError('Duplicate loaded hgraph library basename')
        names.add(path.name)
        loaded[relative] = fingerprint
    required = {path for path in target_libraries if shared_library(path)}
    if not required <= set(loaded):
        raise ValueError('Configured hgraph shared target library was not loaded')
    return loaded

def cache_values(build_dir):
    cache = {}
    for line in (build_dir/'CMakeCache.txt').read_text().splitlines():
        if line and not line.startswith(('#', '//')) and '=' in line:
            key, value = line.split('=', 1)
            cache[key.split(':', 1)[0]] = value
    return cache


def command_configuration(entry, command):
    """Require configuration clues from CMake's output and arguments to agree."""
    clues = {arg.split('=', 1)[1].strip('\\"') for arg in command if arg.startswith(('-DCMAKE_INTDIR=', '/DCMAKE_INTDIR='))}
    outputs = [entry['output']] if 'output' in entry else []
    outputs += [command[index+1] for index, arg in enumerate(command[:-1]) if arg == '-o']
    for index, argument in enumerate(command):
        if argument == '/Fo' and index+1 < len(command): outputs.append(unquote(command[index+1]))
        elif argument.startswith('/Fo') and argument != '/Fo': outputs.append(unquote(argument[3:]))
    if not outputs: raise ValueError('Missing declared target compile output')
    for output in outputs:
        parts = PureWindowsPath(output).parts if '\\' in output else Path(output).parts
        target = 'last_scalar_types_native.dir'
        if target not in parts: raise ValueError('Compile output belongs to another target')
        tail = parts[parts.index(target)+1:]
        if len(tail) > 1: clues.add(tail[0])
    if len(clues) > 1: raise ValueError('Conflicting compile-command configurations')
    return next(iter(clues), None)


def compile_command(build_dir, source, sdk_include, configuration=None):
    """Read exactly one command for the source and selected configuration."""
    entries = json.loads((build_dir / 'compile_commands.json').read_text())
    cache = cache_values(build_dir) if (build_dir/'CMakeCache.txt').is_file() else {}
    multi = bool(cache.get('CMAKE_CONFIGURATION_TYPES'))
    if multi and configuration is None: raise ValueError('Multi-config command requires selected configuration')
    matches = []
    for entry in entries:
        if (Path(entry['directory']) / entry['file']).resolve() != source.resolve(): continue
        command = entry.get('arguments')
        if command is None:
            raw = entry['command']
            # CMake exposes arguments directly on some generators. Its MSVC
            # command strings need Windows parsing even during evidence checks
            # on another platform; POSIX shlex consumes Windows backslashes.
            leading = raw.lstrip()
            first = leading.split('"',2)[1] if leading.startswith('"') else leading.split()[0]
            msvc_names = ('cl', 'cl.exe', 'clang-cl', 'clang-cl.exe')
            windows = any(PureWindowsPath(value).name.lower() in msvc_names
                          for value in (first, cache.get('CMAKE_CXX_COMPILER','')))
            command = split_windows_command(raw) if windows else shlex.split(raw)
        if not isinstance(command, list) or not command or not all(isinstance(arg, str) for arg in command):
            raise ValueError('Invalid compile command')
        selected = command_configuration(entry, command)
        if multi and selected is None: continue
        if configuration is None or selected is None or selected == configuration:
            matches.append((command, Path(entry['directory'])))
    if len(matches) != 1: raise ValueError('Expected one native.cpp compile command for the selected configuration')
    command, directory = matches[0]
    paths = ((str(source.parent.resolve()), '<source>'),
             (str(build_dir.resolve()), '<build>'),
             (str(sdk_include.parent.resolve()), '<sdk>'),
             (str(Path.home()), '<home>'))
    def redact(argument):
        for path, label in sorted(paths, key=lambda item:len(item[0]), reverse=True):
            argument = argument.replace(path, label).replace(path.replace('\\','/'), label)
        return argument
    includes = include_paths(command)
    if not any((directory / include).resolve()==sdk_include.resolve() for include in includes):
        raise ValueError('Probe compile command does not use supplied SDK headers')
    return [redact(argument) for argument in command]


def target_artifact(build_dir, executable):
    """Resolve only artifacts declared by the configured CMake target."""
    cache = cache_values(build_dir)
    configurations = [value for value in cache.get('CMAKE_CONFIGURATION_TYPES', '').split(';') if value]
    if not configurations:
        if 'CMAKE_BUILD_TYPE' not in cache: raise ValueError('Missing active CMake build configuration')
        configurations = [cache['CMAKE_BUILD_TYPE']]
    matches = []
    for config in configurations:
        manifest = build_dir/f'last_scalar_types_target-{config}.txt'
        if not manifest.is_file(): continue
        declared = Path(manifest.read_text().splitlines()[0])
        if declared.is_absolute() and declared.resolve() == executable.resolve():
            matches.append((declared.resolve(), config, manifest))
    if len(matches) != 1: raise ValueError('Executable is not one configured last_scalar_types_native target artifact')
    return matches[0]


def prepare_executable(build_dir, executable):
    artifact, config, manifest = target_artifact(build_dir, executable)
    # A newer foreign executable or object can make an incremental build lie
    # about provenance. Rebuild the configured target from clean outputs.
    command = ['cmake', '--build', str(build_dir.absolute()), '--clean-first', '--target', 'last_scalar_types_native']
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
    if len(set(libraries)) != 3 or any(not path.is_file() or not any(path.is_relative_to(sdk/directory) for directory in ('lib','bin')) for path in libraries):
        raise ValueError('Configured hgraph targets do not belong to the supplied SDK')
    cache = cache_values(build_dir)
    if Path(cache['CMAKE_HOME_DIRECTORY']).resolve() != Path(__file__).resolve().parent:
        raise ValueError('Build directory belongs to another probe source')
    command = compile_command(build_dir, Path(__file__).with_name('native.cpp'), sdk/'include', config)
    return artifact, config, manifest, command, [path.relative_to(sdk).as_posix() for path in libraries]
