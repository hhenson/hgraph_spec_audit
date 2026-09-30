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
            verify_files(output.parent, {'interface.rs': manifest['hgl_files'][contract['rust_file']]})


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
    if args.hgl:
        verify_files(args.hgl, manifest['hgl_files'])
    if args.compiler:
        check_compiler(manifest, args.upstream.resolve(), args.compiler)
    if args.compiler:
        print('Native interface audit passed')
    elif args.hgl:
        print('HGL interface fingerprints verified')
    else:
        print('Recorded shared inputs verified')


if __name__ == '__main__':
    main()
