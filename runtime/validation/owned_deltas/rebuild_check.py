"""Verify an ordinary source-change build refreshes the native probe's digest."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cmake-arg', action='append', default=[],
                        help='Configure argument, e.g. --cmake-arg=-Dhgraph_DIR=/sdk/cmake/hgraph')
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix='owned-deltas-rebuild-') as temporary:
        root = Path(temporary)
        source = root / 'owned_deltas'
        source.mkdir()
        for name in ('CMakeLists.txt', 'native.cpp'):
            shutil.copy2(HERE / name, source / name)
        (root / 'fixed').mkdir()
        shutil.copy2(HERE.parent / 'fixed/native_loaded_libraries.h', root / 'fixed')
        build = root / 'build'
        subprocess.run(['cmake', '-S', str(source), '-B', str(build), '-G', 'Ninja', *args.cmake_arg], check=True)

        def measure():
            subprocess.run(['cmake', '--build', str(build), '--parallel', '2'], check=True)
            executable = build / 'owned_deltas_native'
            result = json.loads(subprocess.check_output([str(executable)], text=True))
            expected = hashlib.sha256((source / 'native.cpp').read_bytes()).hexdigest()
            assert result['source_sha256'] == expected, 'source digest stale after ordinary build'
            return result, hashlib.sha256(executable.read_bytes()).hexdigest()

        before, before_binary = measure()
        with (source / 'native.cpp').open('a') as stream:
            stream.write('\n// Source-change rebuild regression probe.\n')
        after, after_binary = measure()  # Deliberately no explicit configure call.
        assert before['source_sha256'] != after['source_sha256']
        assert before_binary != after_binary
        assert before['observed'] == after['observed']
        expected = json.loads((HERE / 'reasoned.json').read_text())['native_expected']
        assert after['observed'] == expected
        print('Source-change rebuild refreshed source and binary digests; all six native cases still match.')


if __name__ == '__main__':
    main()
