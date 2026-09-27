"""The selected SDK must be the one CMake uses, even with caller overrides."""
import importlib.util
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('run_stdlib', ROOT / 'tools/run_stdlib.py')
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class SdkSelection(unittest.TestCase):
    @unittest.skipUnless(shutil.which('cmake'), 'CMake is required for SDK selection')
    def test_cmake_uses_the_recorded_sdk_despite_typed_overrides(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'native'
            source.mkdir()
            (source / 'CMakeLists.txt').write_text(
                'cmake_minimum_required(VERSION 3.26)\nproject(sdk_selection NONE)\n')
            sdk, build = root / 'sdk', root / 'build'
            overrides = ['-DCMAKE_PREFIX_PATH:PATH=/other/sdk',
                         '-Dhgraph_DIR:PATH=/other/sdk/lib/cmake/hgraph',
                         '-DHGL_EXECUTABLE:FILEPATH=/other/hgl']
            with patch.object(runner, 'CORPUS', root):
                subprocess.run(runner.configure_command(sdk, build, overrides),
                               check=True, capture_output=True, text=True)
            cache = {}
            for line in (build / 'CMakeCache.txt').read_text().splitlines():
                if '=' in line and not line.startswith(('#', '//')):
                    key, value = line.split('=', 1)
                    cache[key.split(':')[0]] = value
            self.assertEqual(cache['CMAKE_PREFIX_PATH'], str(sdk))
            self.assertEqual(cache['hgraph_DIR'], str(sdk / 'lib/cmake/hgraph'))
            self.assertTrue(Path(cache['HGL_EXECUTABLE']).is_relative_to(sdk / 'bin'))
