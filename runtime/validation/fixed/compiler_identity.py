"""Cold compiler identity profiles shared by installed-SDK audit recorders."""
import hashlib
from pathlib import Path
import subprocess


def capture_compiler_identity(executable):
    executable = Path(executable).resolve(strict=True)
    before = hashlib.sha256(executable.read_bytes()).hexdigest()
    msvc = executable.name.lower() in ('cl', 'cl.exe')
    arguments = [] if msvc else ['--version']
    result = subprocess.run([str(executable), *arguments], capture_output=True, timeout=60)
    if hashlib.sha256(executable.read_bytes()).hexdigest() != before:
        raise RuntimeError('Compiler executable changed during identity capture')
    stdout = result.stdout.decode('utf-8', errors='replace').splitlines()
    stderr = result.stderr.decode('utf-8', errors='replace').splitlines()
    stdout = [line.strip() for line in stdout if line.strip()]
    stderr = [line.strip() for line in stderr if line.strip()]
    if result.returncode != 0:
        raise ValueError('Unexpected compiler identity exit status')
    if msvc:
        # Bare cl returns success and prints its banner to stderr. Preserve
        # both complete streams by digest; do not classify localized usage or
        # diagnostics by English substrings. The configured build separately
        # proves that this selected compiler produces the probe.
        if not stderr: raise ValueError('Missing MSVC compiler banner')
        version = stderr[0]
    else:
        if not stdout: raise ValueError('Missing compiler version output')
        version = stdout[0]
    return {'compiler_sha256': before, 'compiler_version': version,
            'compiler_identity': {'profile': 'msvc-no-input' if msvc else 'version',
                                  'arguments': arguments, 'exit_code': result.returncode,
                                  'stdout_sha256': hashlib.sha256(result.stdout).hexdigest(),
                                  'stderr_sha256': hashlib.sha256(result.stderr).hexdigest()}}


def validate_compiler_identity(record):
    identity = record['compiler_identity']
    assert identity['profile'] in ('version', 'msvc-no-input')
    assert type(identity['exit_code']) is int and identity['exit_code'] == 0
    assert identity['arguments'] == ([] if identity['profile'] == 'msvc-no-input' else ['--version'])
    for name in ('stdout_sha256', 'stderr_sha256'):
        value = identity[name]
        assert isinstance(value, str) and len(value) == 64 and set(value) <= set('0123456789abcdef')
    assert isinstance(record['compiler_version'], str) and record['compiler_version'].strip()
