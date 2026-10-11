"""Reject unrelated binaries/SDKs and select the actual build configuration."""
import json
import hashlib
import os
import shutil
import subprocess
import time
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from build_identity import prepare_executable, sdk_binding, selected_sdk_headers, include_paths

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

    def headers(self,root):
        for name in ('lib/testing/eval_node.h','lib/std/std_operators.h','lib/std/std_nodes.h','types/static_node.h'):
            path=root/'hgraph'/name
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text('#pragma once\n// '+name+'\n')

    @unittest.skipUnless(shutil.which('c++'),'C++ preprocessor required')
    def test_real_preprocessor_rejects_foreign_sdk_I_before_intended_isystem(self):
        self.configure()
        self.headers(self.sdk/'include')
        foreign=self.root/'foreign sdk/include'
        self.headers(foreign)
        path=self.build/'compile_commands.json'
        original=json.loads(path.read_text())
        response=self.build/'includes.rsp'
        response.write_text('-I"'+str(foreign)+'"\n')
        for added in (['-I'+str(foreign)],['-I',str(foreign)],['--include-directory='+str(foreign)],['@'+str(response)]):
            commands=json.loads(json.dumps(original))
            commands[0]['arguments'][1:2]=['-isystem',str(self.sdk/'include'),*added]
            path.write_text(json.dumps(commands))
            # The intended SDK appears first in argv, but -I still wins.
            with self.subTest(added=added),self.assertRaisesRegex(ValueError,'shadow'):
                selected_sdk_headers(self.build,HERE/'native.cpp',self.sdk/'include','Release')

    @unittest.skipUnless(shutil.which('c++'),'C++ preprocessor required')
    def test_real_preprocessor_detects_environment_shadowing(self):
        self.configure()
        self.headers(self.sdk/'include')
        foreign=self.root/'foreign/include'
        self.headers(foreign)
        path=self.build/'compile_commands.json'
        commands=json.loads(path.read_text())
        commands[0]['arguments'][1:2]=['-isystem',str(self.sdk/'include')]
        path.write_text(json.dumps(commands))
        with patch.dict(os.environ,{'CPATH':str(foreign)}),self.assertRaisesRegex(ValueError,'shadow'):
            selected_sdk_headers(self.build,HERE/'native.cpp',self.sdk/'include','Release')
        # The compiler puts this system environment path after explicit system
        # directories; its unused foreign headers must not cause a false alarm.
        with patch.dict(os.environ,{'CPATH':'','CPLUS_INCLUDE_PATH':str(foreign)}):
            self.assertEqual(len(selected_sdk_headers(self.build,HERE/'native.cpp',self.sdk/'include','Release')),4)

    @unittest.skipUnless(shutil.which('c++'),'C++ preprocessor required')
    def test_legitimate_dependency_includes_do_not_hide_selected_sdk(self):
        self.configure()
        self.headers(self.sdk/'include')
        dependencies=self.root/'dependencies'
        dependencies.mkdir()
        (dependencies/'dependency.h').write_text('#pragma once\n')
        path=self.build/'compile_commands.json'
        commands=json.loads(path.read_text())
        commands[0]['arguments'][1:1]=['-I'+str(dependencies),'-include','dependency.h']
        path.write_text(json.dumps(commands))
        self.assertEqual(len(selected_sdk_headers(self.build,HERE/'native.cpp',self.sdk/'include','Release')),4)

    def test_msvc_line_directives_and_portable_include_forms(self):
        self.configure()
        self.headers(self.sdk/'include')
        path=self.build/'compile_commands.json'
        commands=json.loads(path.read_text())
        commands[0]['arguments'][0]='cl.exe'
        commands[0]['arguments'][1:2]=['/external:I'+str(self.sdk/'include')]
        path.write_text(json.dumps(commands))
        lines='\n'.join('#line 1 '+json.dumps(str(p)) for p in (self.sdk/'include/hgraph').rglob('*.h'))
        with patch('build_identity.subprocess.run',return_value=subprocess.CompletedProcess([],0,lines,'')) as invoked:
            self.assertEqual(len(selected_sdk_headers(self.build,HERE/'native.cpp',self.sdk/'include','Release')),4)
            self.assertEqual(invoked.call_args.args[0][-1],'/E')
        for option in ('-I','-isystem','-iquote','-idirafter','--include-directory=','/I','/external:I'):
            self.assertEqual(include_paths([option+'<sdk>/include']),['<sdk>/include'])
        with patch('build_identity.subprocess.run',return_value=subprocess.CompletedProcess([],0,'','')):
            with self.assertRaisesRegex(ValueError,'every direct'):
                selected_sdk_headers(self.build,HERE/'native.cpp',self.sdk/'include','Release')


    @unittest.skipUnless(all(shutil.which(tool) for tool in ('cmake', 'c++', 'make', 'ninja')),
                         'CMake, C++ compiler, Make and Ninja are required for the replacement control')
    def test_clean_rebuild_replaces_newer_foreign_same_source_executable(self):
        source = self.root / 'source'
        source.mkdir()
        target = 'ref_owner_lifetime_native'
        (source / 'native.cpp').write_text('#include <iostream>\nint main() { std::cout << PROBE_MESSAGE; }\n')
        (source / 'CMakeLists.txt').write_text(
            'cmake_minimum_required(VERSION 3.26)\nproject(replacement LANGUAGES CXX)\n'
            'add_executable(' + target + ' native.cpp)\n'
            'target_compile_definitions(' + target + ' PRIVATE PROBE_MESSAGE="${PROBE_MESSAGE}")\n'
            'file(GENERATE OUTPUT "${CMAKE_CURRENT_BINARY_DIR}/ref_owner_lifetime_target-$<CONFIG>.txt" '
            'CONTENT "$<TARGET_FILE:' + target + '>\\n")\n')
        for generator, multi in [('Unix Makefiles', False), ('Ninja', False), ('Ninja Multi-Config', True)]:
            with self.subTest(generator=generator):
                tag = generator.replace(' ', '-')
                builds = [self.root / (tag + '-declared'), self.root / (tag + '-foreign')]
                artifacts = []
                for build, message in zip(builds, ('declared', 'foreign')):
                    subprocess.run(['cmake', '-S', str(source), '-B', str(build), '-G', generator,
                                    '-DCMAKE_BUILD_TYPE=Release', '-DPROBE_MESSAGE=' + message],
                                   check=True, capture_output=True, text=True)
                    subprocess.run(['cmake', '--build', str(build), '--target', target, '--config', 'Release'],
                                   check=True, capture_output=True, text=True)
                    artifacts.append(build / 'Release' / target if multi else build / target)
                declared, foreign = artifacts
                foreign_hash = hashlib.sha256(foreign.read_bytes()).hexdigest()
                shutil.copy2(foreign, declared)
                future = time.time() + 86400
                os.utime(declared, (future, future))
                self.assertEqual(subprocess.check_output([str(declared)], text=True), 'foreign')
                # Make leaves this newer foreign output untouched. Ninja may
                # detect its build-log mismatch, so demonstrate the incremental
                # failure on Make and require clean replacement on all three.
                if generator == 'Unix Makefiles':
                    subprocess.run(['cmake', '--build', str(builds[0]), '--target', target, '--config', 'Release'],
                                   check=True, capture_output=True, text=True)
                    self.assertEqual(subprocess.check_output([str(declared)], text=True), 'foreign')
                prepare_executable(builds[0], declared)
                self.assertEqual(subprocess.check_output([str(declared)], text=True), 'declared')
                self.assertNotEqual(hashlib.sha256(declared.read_bytes()).hexdigest(), foreign_hash)


if __name__ == '__main__':
    unittest.main()
