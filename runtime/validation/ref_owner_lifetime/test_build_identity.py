"""Reject unrelated binaries/SDKs and select the actual build configuration."""
import json
from pathlib import Path
import tempfile
import unittest

from build_identity import sdk_binding

HERE = Path(__file__).resolve().parent


class BuildIdentityTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.build = self.root / 'build'
        self.sdk = self.root / 'sdk'
        self.build.mkdir()
        (self.sdk / 'lib/cmake/hgraph').mkdir(parents=True)
        (self.sdk / 'include').mkdir()
        self.libraries = [self.sdk / 'lib' / ('libhgraph_' + name + '.a')
                          for name in ('stdlib', 'wiring', 'runtime')]
        for library in self.libraries:
            library.write_bytes(b'fixture archive')

    def configure(self, generator='Ninja', multi=False):
        configs = ['Debug', 'Release'] if multi else ['Release']
        cache = ['CMAKE_HOME_DIRECTORY:INTERNAL=' + str(HERE),
                 'CMAKE_GENERATOR:INTERNAL=' + generator]
        cache += ['CMAKE_CONFIGURATION_TYPES:STRING=Debug;Release'] if multi else ['CMAKE_BUILD_TYPE:STRING=Release']
        (self.build / 'CMakeCache.txt').write_text('\n'.join(cache) + '\n')
        commands = []
        for config in configs:
            artifact = self.build / config / 'ref_owner_lifetime_native' if multi else self.build / 'ref_owner_lifetime_native'
            artifact.parent.mkdir(exist_ok=True)
            artifact.write_bytes(b'identical fixture executable')
            manifest = self.build / ('ref_owner_lifetime_target-' + config + '.txt')
            manifest.write_text('\n'.join(map(str, [artifact, self.sdk / 'lib/cmake/hgraph', *self.libraries])) + '\n')
            command = ['c++', '-I' + str(self.sdk / 'include'), '-std=c++23']
            if multi:
                command.append('-DCMAKE_INTDIR="' + config + '"')
            command += ['-o', 'CMakeFiles/ref_owner_lifetime_native.dir/' + (config + '/' if multi else '') + 'native.cpp.o',
                        '-c', str(HERE / 'native.cpp')]
            commands.append({'directory': str(self.build), 'file': str(HERE / 'native.cpp'), 'arguments': command})
        (self.build / 'compile_commands.json').write_text(json.dumps(commands))
        return artifact

    def test_make_ninja_and_multiconfiguration(self):
        for generator, multi in [('Unix Makefiles', False), ('Ninja', False), ('Ninja Multi-Config', True)]:
            with self.subTest(generator=generator):
                artifact = self.configure(generator, multi)
                result = sdk_binding(self.build, artifact, self.sdk)
                self.assertEqual(result[1], 'Release')
                self.assertIn('<sdk>/include', ' '.join(result[3]))
                self.assertEqual(len(result[4]), 3)

    def test_identical_executable_outside_declared_target_is_rejected(self):
        artifact = self.configure()
        unrelated = self.root / 'identical-probe'
        unrelated.write_bytes(artifact.read_bytes())
        with self.assertRaisesRegex(ValueError, 'configured'):
            sdk_binding(self.build, unrelated, self.sdk)

    def test_supplied_sdk_must_match_configured_package(self):
        artifact = self.configure()
        with self.assertRaisesRegex(ValueError, 'package'):
            sdk_binding(self.build, artifact, self.root / 'other-sdk')

    def test_configured_library_outside_sdk_is_rejected(self):
        artifact = self.configure()
        other = self.root / 'other-library.a'
        other.write_bytes(self.libraries[0].read_bytes())
        manifest = self.build / 'ref_owner_lifetime_target-Release.txt'
        manifest.write_text(manifest.read_text().replace(str(self.libraries[0]), str(other)))
        with self.assertRaisesRegex(ValueError, 'targets'):
            sdk_binding(self.build, artifact, self.sdk)

    def test_missing_sdk_header_command_is_rejected(self):
        artifact = self.configure()
        path = self.build / 'compile_commands.json'
        commands = json.loads(path.read_text())
        commands[0]['arguments'][1] = '-I/another/include'
        path.write_text(json.dumps(commands))
        with self.assertRaisesRegex(ValueError, 'headers'):
            sdk_binding(self.build, artifact, self.sdk)

    def test_unrelated_target_compile_output_is_rejected(self):
        artifact = self.configure()
        path = self.build / 'compile_commands.json'
        path.write_text(path.read_text().replace('ref_owner_lifetime_native.dir', 'unrelated.dir'))
        with self.assertRaisesRegex(ValueError, 'another target'):
            sdk_binding(self.build, artifact, self.sdk)

    def test_similar_header_path_or_definition_is_rejected(self):
        artifact = self.configure()
        path = self.build / 'compile_commands.json'
        original = json.loads(path.read_text())
        for argument in ['-I' + str(self.sdk / 'include-other'), '-DFAKE=' + str(self.sdk / 'include')]:
            commands = json.loads(json.dumps(original))
            commands[0]['arguments'][1] = argument
            path.write_text(json.dumps(commands))
            with self.subTest(argument=argument), self.assertRaisesRegex(ValueError, 'headers'):
                sdk_binding(self.build, artifact, self.sdk)

    def test_ambiguous_configuration_is_rejected(self):
        artifact = self.configure('Ninja Multi-Config', True)
        path = self.build / 'compile_commands.json'
        commands = json.loads(path.read_text())
        commands.append(commands[-1])
        path.write_text(json.dumps(commands))
        with self.assertRaisesRegex(ValueError, 'one native.cpp'):
            sdk_binding(self.build, artifact, self.sdk)

    def test_relative_include_uses_selected_entry_directory(self):
        artifact = self.configure()
        path = self.build / 'compile_commands.json'
        commands = json.loads(path.read_text())
        commands[0]['arguments'][1] = '-I../sdk/include'
        commands.append({'directory': str(self.root / 'unrelated'), 'file': 'other.cpp',
                         'arguments': ['c++', '-c', 'other.cpp']})
        path.write_text(json.dumps(commands))
        self.assertEqual(sdk_binding(self.build, artifact, self.sdk)[0], artifact)


if __name__ == '__main__':
    unittest.main()
