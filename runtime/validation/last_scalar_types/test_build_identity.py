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

from build_identity import include_paths, loaded_sdk_libraries, prepare_executable, sdk_binding, split_windows_command

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
            artifact = self.build / config / 'last_scalar_types_native' if multi else self.build / 'last_scalar_types_native'
            artifact.parent.mkdir(exist_ok=True)
            artifact.write_bytes(b'identical fixture executable')
            manifest = self.build / ('last_scalar_types_target-' + config + '.txt')
            manifest.write_text('\n'.join(map(str, [artifact, self.sdk / 'lib/cmake/hgraph', *self.libraries])) + '\n')
            command = ['c++', '-I' + str(self.sdk / 'include'), '-std=c++23']
            if multi:
                command.append('-DCMAKE_INTDIR="' + config + '"')
            command += ['-o', 'CMakeFiles/last_scalar_types_native.dir/' + (config + '/' if multi else '') + 'native.cpp.o',
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
        manifest = self.build / 'last_scalar_types_target-Release.txt'
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
        path.write_text(path.read_text().replace('last_scalar_types_native.dir', 'unrelated.dir'))
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

    def test_portable_include_operands_and_quoted_spaces(self):
        # The real fixture path contains spaces; MSVC-style arguments must
        # still bind to this exact SDK, not a similar directory or definition.
        relocated=self.root/'SDK with spaces'
        self.sdk.rename(relocated)
        self.sdk=relocated
        self.libraries=[self.sdk/'lib'/path.name for path in self.libraries]
        include=str(self.sdk/'include')
        for prefix in ('-I','-isystem','/I','/external:I'):
            for arguments in ([prefix,include],[prefix+include],
                              [prefix,'"'+include+'"'],[prefix+'"'+include+'"']):
                with self.subTest(arguments=arguments):
                    artifact=self.configure()
                    path=self.build/'compile_commands.json'
                    entries=json.loads(path.read_text())
                    entries[0]['arguments'][1:2]=arguments
                    path.write_text(json.dumps(entries))
                    sdk_binding(self.build,artifact,self.sdk)

    def test_msvc_command_string_preserves_backslashes_quotes_and_output(self):
        command=r'"C:\Program Files\MSVC\cl.exe" /I"C:\SDK with spaces\include" /external:I "C:\external files" /Fo"CMakeFiles\last_scalar_types_native.dir\Release\native.cpp.obj" /c native.cpp'
        tokens=split_windows_command(command)
        self.assertEqual(tokens[0],r'C:\Program Files\MSVC\cl.exe')
        self.assertEqual(include_paths(tokens),[r'C:\SDK with spaces\include',r'C:\external files'])
        # Round-trip the platform-independent serializer's escaped quotes and
        # trailing backslashes, which POSIX shlex would consume.
        values=['C:\\SDK files\\', 'a"b', '', r'plain\path']
        self.assertEqual(split_windows_command(subprocess.list2cmdline(values)),values)
        self.assertEqual(split_windows_command('cl.exe "a""b"'),['cl.exe','a"b'])
        with self.assertRaisesRegex(ValueError,'Unterminated'):
            split_windows_command('cl.exe /I"C:\\unfinished')
        artifact=self.configure('Ninja Multi-Config',True)
        path=self.build/'compile_commands.json'
        entries=json.loads(path.read_text())
        for entry,config in zip(entries,('Debug','Release')):
            entry.pop('arguments')
            entry['command']='cl.exe /I"'+str(self.sdk/'include')+'" /DCMAKE_INTDIR=\\"'+config+'\\" /Fo"CMakeFiles\\last_scalar_types_native.dir\\'+config+'\\native.cpp.obj" /c "'+str(HERE/'native.cpp')+'"'
        path.write_text(json.dumps(entries))
        result=sdk_binding(self.build,artifact,self.sdk)
        self.assertEqual(result[1],'Release')
        self.assertIn('<sdk>/include',include_paths(result[3]))

    def test_msvc_separate_output_and_unrelated_include_text(self):
        artifact=self.configure()
        path=self.build/'compile_commands.json'
        entries=json.loads(path.read_text())
        original=entries[0]['arguments']
        entries[0]['arguments']=['cl.exe','/external:I',str(self.sdk/'include'),
                                 '/Fo',r'CMakeFiles\last_scalar_types_native.dir\native.cpp.obj','/c',str(HERE/'native.cpp')]
        path.write_text(json.dumps(entries))
        sdk_binding(self.build,artifact,self.sdk)
        for argument in ('/DFAKE=/I'+str(self.sdk/'include'),
                         '-DFAKE=-I'+str(self.sdk/'include'),
                         '/I'+str(self.sdk/'include-other'),
                         '/external:I'+str(self.sdk/'include-other')):
            entries[0]['arguments']=original.copy()
            entries[0]['arguments'][1]=argument
            path.write_text(json.dumps(entries))
            with self.subTest(argument=argument),self.assertRaisesRegex(ValueError,'headers'):
                sdk_binding(self.build,artifact,self.sdk)
        for command in (['cl.exe','/I'],['cl.exe','/external:I']):
            with self.subTest(command=command),self.assertRaisesRegex(ValueError,'operand'):
                include_paths(command)

    def test_relative_include_uses_selected_command_directory(self):
        artifact=self.configure()
        path=self.build/'compile_commands.json'
        entries=json.loads(path.read_text())
        entries[0]['arguments'][1:2]=['/I','../sdk/include']
        entries.append({'directory':str(self.root/'unrelated/directory'),
                        'file':'unrelated.cpp','arguments':['cl.exe','/I','../sdk/include']})
        path.write_text(json.dumps(entries))
        sdk_binding(self.build,artifact,self.sdk)

    def test_ambiguous_configuration_is_rejected(self):
        artifact = self.configure('Ninja Multi-Config', True)
        path = self.build / 'compile_commands.json'
        commands = json.loads(path.read_text())
        commands.append(commands[-1])
        path.write_text(json.dumps(commands))
        with self.assertRaisesRegex(ValueError, 'one native.cpp'):
            sdk_binding(self.build, artifact, self.sdk)

    def test_loaded_library_must_match_sdk_path_and_bytes(self):
        library=self.sdk/'lib/libhgraph_runtime.so'
        library.write_bytes(b'shared fixture')
        relative=library.relative_to(self.sdk).as_posix()
        fingerprints={relative:hashlib.sha256(library.read_bytes()).hexdigest()}
        self.assertEqual(loaded_sdk_libraries([str(library)],self.sdk,fingerprints,[relative]),fingerprints)
        foreign=self.root/library.name
        foreign.write_bytes(library.read_bytes())
        with self.assertRaisesRegex(ValueError,'belong'):
            loaded_sdk_libraries([str(foreign)],self.sdk,fingerprints,[])
        library.write_bytes(b'changed after SDK fingerprint')
        with self.assertRaisesRegex(ValueError,'manifest'):
            loaded_sdk_libraries([str(library)],self.sdk,fingerprints,[])

    def test_configured_shared_targets_must_be_loaded(self):
        for target in ('lib/libhgraph_runtime.so','lib/libhgraph_runtime.so.1',
                       'lib/libhgraph_runtime.dylib','bin/hgraph_runtime.dll'):
            with self.subTest(target=target),self.assertRaisesRegex(ValueError,'not loaded'):
                loaded_sdk_libraries([],self.sdk,{},[target])
        self.assertEqual(loaded_sdk_libraries([],self.sdk,{},['lib/libhgraph_runtime.a']),{})

    @unittest.skipUnless(os.name=='posix' and Path('/proc/self/maps').exists() and shutil.which('c++'),
                         'Linux compiler and loader are required for the runtime override control')
    def test_ld_library_path_override_is_rejected(self):
        source=self.root/'library.cpp'
        source.write_text('extern "C" int probe_value() { return PROBE_VALUE; }\n')
        directories=[self.sdk/'lib',self.root/'foreign']
        for directory,value in zip(directories,(1,2)):
            directory.mkdir(exist_ok=True)
            subprocess.run(['c++','-shared','-fPIC','-DPROBE_VALUE='+str(value),str(source),
                            '-o',str(directory/'libhgraph_runtime.so')],check=True,capture_output=True)
        probe=self.root/'loader.cpp'
        probe.write_text('#include <dlfcn.h>\n#include <iostream>\n'
                         'extern "C" int probe_value();\nint main() { Dl_info info{}; '
                         'if (!dladdr((void*)&probe_value, &info)) return 1; '
                         'std::cout << probe_value() << "\\n" << info.dli_fname << "\\n"; }\n')
        executable=self.root/'loader'
        subprocess.run(['c++',str(probe),'-L'+str(directories[0]),'-lhgraph_runtime','-ldl',
                        '-Wl,--enable-new-dtags','-Wl,-rpath,'+str(directories[0]),'-o',str(executable)],
                       check=True,capture_output=True)
        sdk_library=directories[0]/'libhgraph_runtime.so'
        relative=sdk_library.relative_to(self.sdk).as_posix()
        fingerprints={relative:hashlib.sha256(sdk_library.read_bytes()).hexdigest()}
        for directory,value in zip(directories,('1','2')):
            environment=dict(os.environ,LD_LIBRARY_PATH=str(directory))
            lines=subprocess.check_output([str(executable)],env=environment,text=True).splitlines()
            self.assertEqual(lines[0],value)
            self.assertEqual(Path(lines[1]).resolve(),directory/'libhgraph_runtime.so')
            if value=='1':
                self.assertEqual(loaded_sdk_libraries(lines[1:],self.sdk,fingerprints,[relative]),fingerprints)
            else:
                with self.assertRaisesRegex(ValueError,'belong'):
                    loaded_sdk_libraries(lines[1:],self.sdk,fingerprints,[relative])


    @unittest.skipUnless(all(shutil.which(tool) for tool in ('cmake', 'c++', 'make', 'ninja')),
                         'CMake, C++ compiler, Make and Ninja are required for the replacement control')
    def test_clean_rebuild_replaces_newer_foreign_same_source_executable(self):
        source = self.root / 'source'
        source.mkdir()
        target = 'last_scalar_types_native'
        (source / 'native.cpp').write_text('#include <iostream>\nint main() { std::cout << PROBE_MESSAGE; }\n')
        (source / 'CMakeLists.txt').write_text(
            'cmake_minimum_required(VERSION 3.26)\nproject(replacement LANGUAGES CXX)\n'
            'add_executable(' + target + ' native.cpp)\n'
            'target_compile_definitions(' + target + ' PRIVATE PROBE_MESSAGE="${PROBE_MESSAGE}")\n'
            'file(GENERATE OUTPUT "${CMAKE_CURRENT_BINARY_DIR}/last_scalar_types_target-$<CONFIG>.txt" '
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
