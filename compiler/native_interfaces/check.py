"""Audit C++ to Rust native interfaces without depending on the private runtime."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def verify_files(root, files):
    for name, expected in files.items():
        path = root / name
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError(f'Native interface audit: missing or changed {name}')


# Exact substitutions for the two archived sources, not an arbitrary rewrite API.
ACCESS_SPELLINGS = {
    'language/examples/const-debug.hgl': [
        ('scheduler.schedule(0s)', 'schedule(scheduler, 0s)')],
    'language/tests/codegen/native-provider.hgl': [
        ('logger.info("HGL helper")', 'info(logger, "HGL helper")'),
        ('clock.evaluation_time()', 'clock.evaluation_time')],
}


def verify_source_migrations(root, manifest):
    archive = json.loads((root / manifest['historical_sources']).read_text())
    if archive['hgraph_revision'] != manifest['hgraph_revision'] or set(archive['sources']) != set(ACCESS_SPELLINGS):
        raise ValueError('Native interface audit: incomplete or relabelled historical sources')
    migrations = manifest['source_migrations']
    if len(migrations) != len(ACCESS_SPELLINGS) or {m['upstream'] for m in migrations} != set(ACCESS_SPELLINGS):
        raise ValueError('Native interface audit: incomplete source migration coverage')
    for migration in migrations:
        if migration['spelling'] != 'capability-functions-clock-properties-v2':
            raise ValueError('Native interface audit: unknown source migration')
        transformed = archive['sources'][migration['upstream']].encode('utf-8')
        if hashlib.sha256(transformed).hexdigest() != manifest['upstream_files'][migration['upstream']]:
            raise ValueError('Native interface audit: changed historical source')
        for old, new in ACCESS_SPELLINGS[migration['upstream']]:
            if transformed.count(old.encode()) != 1:
                raise ValueError('Native interface audit: unexpected original capability call')
            transformed = transformed.replace(old.encode(), new.encode())
        current = root / migration['shared']
        if current.read_bytes() != transformed:
            raise ValueError('Native interface audit: source changed beyond capability access spelling')
        digest = hashlib.sha256(transformed).hexdigest()
        if manifest['shared_files'][migration['shared']] != digest or manifest['hgl_files'][migration['hgl']] != digest:
            raise ValueError('Native interface audit: migrated source fingerprints disagree')
    # The historical compiler output is immutable and remains the ABI byte baseline.
    rust_files = {contract['rust_file'] for contract in manifest['contracts']}
    if set(manifest['historical_interface_files']) != rust_files:
        raise ValueError('Native interface audit: incomplete historical ABI coverage')
    for name in rust_files:
        if manifest['hgl_files'][name] != manifest['historical_interface_files'][name]:
            raise ValueError('Native interface audit: current ABI differs from historical interface')


def check_compiler(manifest, upstream, compiler):
    revision = subprocess.check_output(
        ['git', '-C', str(upstream), 'rev-parse', 'HEAD'], text=True).strip()
    if revision != manifest['hgraph_revision']:
        raise ValueError('Native interface audit: unexpected upstream revision')
    verify_files(upstream, manifest['upstream_files'])
    for contract in manifest['contracts']:
        with tempfile.TemporaryDirectory(prefix='native-interface-audit-') as directory:
            output = Path(directory) / 'interface.rs'
            subprocess.run([str(compiler.resolve()), 'emit-native-rust',
                            str(upstream / contract['interface']), '--part',
                            str(upstream / contract['implementation']), '--out', str(output)], check=True)
            subprocess.run(['rustfmt', '+' + manifest['rust_toolchain'],
                            '--edition', '2024', str(output)], check=True)
            verify_files(output.parent, {'interface.rs': manifest['historical_interface_files'][contract['rust_file']]})


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--hgl', type=Path, help='Verify an HGL checkout against the audited fingerprints')
    parser.add_argument('--upstream', type=Path, help='Pinned public hgraph checkout')
    parser.add_argument('--compiler', type=Path, help='Compiler built from that checkout')
    args = parser.parse_args(argv)
    if bool(args.upstream) != bool(args.compiler) or (args.hgl and args.compiler):
        parser.error('supply --hgl, or both --upstream and --compiler')
    manifest = json.loads((HERE / 'contracts.json').read_text())
    verify_files(ROOT, manifest['shared_files'])
    verify_source_migrations(ROOT, manifest)
    if args.hgl:
        verify_files(args.hgl, manifest['hgl_files'])
    if args.compiler:
        check_compiler(manifest, args.upstream.resolve(), args.compiler)
    if args.compiler:
        print('Historical compiler ABI verified; current sources checked only for scoped syntax migration')
    elif args.hgl:
        print('Current HGL fingerprints and scoped source migration verified; no current-source compilation performed')
    else:
        print('Current shared inputs and archived source migration verified; historical ABI baseline retained')


if __name__ == '__main__':
    main()
