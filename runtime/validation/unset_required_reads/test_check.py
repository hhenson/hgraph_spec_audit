import json
import copy
import tempfile
from pathlib import Path
import unittest
from unittest.mock import patch
from check import validate
from native_observe import compile_command, prepare_executable, target_artifact

HERE = Path(__file__).resolve().parent

class EvidenceIntegrity(unittest.TestCase):
    def setUp(self):
        self.cases = json.loads((HERE/'reasoned.json').read_text())['cases']
        self.public = json.loads((HERE/'observed.json').read_text())
        self.native = json.loads((HERE/'native_observed.json').read_text())

    def test_recorded_evidence(self):
        validate(self.cases, self.public, self.native)

    def test_false_cannot_be_mistaken_for_absence(self):
        self.native['observations']['bool_false']['retained_child_valid'] = False
        with self.assertRaises(AssertionError): validate(self.cases, self.public, self.native)

    def test_collection_coercion_variation_is_not_repaired(self):
        self.public['engines']['python']['observations']['list_unset']['reads'][1]['result'] = 0
        with self.assertRaises(AssertionError): validate(self.cases, self.public, self.native)

    def test_native_absence_cannot_be_defaulted(self):
        self.native['observations']['scalar_unset'].update(outcome='value',result=0)
        with self.assertRaises(AssertionError): validate(self.cases, self.public, self.native)

    def test_missing_case_fails(self):
        del self.native['observations']['map_unset']
        with self.assertRaises(AssertionError): validate(self.cases, self.public, self.native)

    def test_missing_empty_or_extra_engine_fails(self):
        for keys in ([], ['python'], ['cpp'], ['python', 'cpp', 'other']):
            with self.subTest(keys=keys):
                evidence = copy.deepcopy(self.public)
                evidence['engines'] = {key: copy.deepcopy(self.public['engines'].get(key, self.public['engines']['python'])) for key in keys}
                with self.assertRaises(AssertionError): validate(self.cases, evidence, self.native)

    def test_stripped_engine_identity_fails(self):
        for engine in ('python', 'cpp'):
            with self.subTest(engine=engine):
                evidence = copy.deepcopy(self.public)
                evidence['engines'][engine]['identity'] = {'native': engine == 'cpp'}
                with self.assertRaises((AssertionError, KeyError)): validate(self.cases, evidence, self.native)

    def test_corrupt_artifact_or_runner_identity_fails(self):
        for engine in ('python', 'cpp'):
            for field in ('package', 'eval_node_source_sha256', 'loaded_hgraph_libraries'):
                with self.subTest(engine=engine, field=field):
                    evidence = copy.deepcopy(self.public)
                    identity = evidence['engines'][engine]['identity']
                    if field == 'package': identity[field]['identity_sha256'] = '0' * 64
                    elif field == 'eval_node_source_sha256': identity[field] = '0' * 64
                    else: identity[field] = {'invented.so': '0' * 64}
                    with self.assertRaises(AssertionError): validate(self.cases, evidence, self.native)

    def test_defaulted_absence_with_unchanged_result_fails(self):
        mutations = [('python', 'bool_unset', False, 'bool'),
                     ('cpp', 'bool_unset', False, 'bool'),
                     ('python', 'list_unset', [4, 5], 'tuple'),
                     ('python', 'map_unset', None, 'NoneType')]
        for engine, case, value, type_name in mutations:
            for field in ('retained', 'payload'):
                with self.subTest(engine=engine, case=case, field=field):
                    evidence = copy.deepcopy(self.public)
                    row = evidence['engines'][engine]['observations'][case]['reads'][1]
                    row[field], row[field+'_type'] = value, type_name
                    with self.assertRaises(AssertionError): validate(self.cases, evidence, self.native)

    def test_absent_bundle_field_cannot_be_synthesized(self):
        row = self.public['engines']['python']['observations']['bool_unset']['reads'][0]
        row['retained']['child'] = None
        with self.assertRaises(AssertionError): validate(self.cases, self.public, self.native)

    def test_value_and_type_corruption_with_equal_python_values_fails(self):
        for engine in ('python', 'cpp'):
            for field, value in (('retained', 1), ('payload', 1), ('retained_type', 'int'), ('payload_type', 'int')):
                with self.subTest(engine=engine, field=field):
                    evidence = copy.deepcopy(self.public)
                    evidence['engines'][engine]['observations']['bool_present']['reads'][1][field] = value
                    with self.assertRaises(AssertionError): validate(self.cases, evidence, self.native)

    def test_native_and_facade_library_mismatch_fails(self):
        for library in ('libhgraph_runtime.so', 'libhgraph_wiring.so', 'libhgraph_stdlib.so'):
            with self.subTest(library=library):
                native = copy.deepcopy(self.native)
                native['loaded_libraries_sha256'][library] = '0' * 64
                with self.assertRaises(AssertionError): validate(self.cases, self.public, native)

    def test_exception_rows_cannot_report_success(self):
        rows = [(case, 0) for case in ('scalar_unset', 'bool_unset', 'list_unset', 'map_unset')]
        rows.append(('scalar_unset', 1))
        for case, index in rows:
            with self.subTest(case=case, index=index):
                evidence = copy.deepcopy(self.public)
                evidence['engines']['python']['observations'][case]['reads'][index]['outcome'] = 'value'
                with self.assertRaises(AssertionError): validate(self.cases, evidence, self.native)

    def test_missing_compile_command_fails(self):
        self.native['compile_command'] = []
        with self.assertRaises(AssertionError): validate(self.cases, self.public, self.native)

class CompileCommands(unittest.TestCase):
    def test_command_and_arguments_keep_quoted_flags(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root/'source files'/'native.cpp'
            sdk = root/'sdk'/'include'
            arguments = ['/usr/bin/c++', '-DNAME=two words', '-I'+str(sdk), '-c', str(source)]
            import shlex
            for form in ({'arguments': arguments}, {'command': shlex.join(arguments)}):
                with self.subTest(form=list(form)):
                    (root/'compile_commands.json').write_text(json.dumps([{'directory':str(root), 'file':str(source), **form}]))
                    self.assertEqual(compile_command(root, source, sdk),
                        ['/usr/bin/c++', '-DNAME=two words', '-I<build>/sdk/include', '-c', '<source>/native.cpp'])

    def test_missing_or_ambiguous_source_command_fails(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            entry = {'directory':str(root), 'file':'native.cpp', 'arguments':['c++','-c','native.cpp']}
            for entries in ([], [entry, entry]):
                with self.subTest(entries=len(entries)):
                    (root/'compile_commands.json').write_text(json.dumps(entries))
                    with self.assertRaises(ValueError): compile_command(root, root/'native.cpp', root/'include')

class TargetArtifacts(unittest.TestCase):
    def test_other_build_executable_rejected_before_build(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            build, other = root/'build', root/'other-build'
            build.mkdir(); other.mkdir()
            expected = build/'unset_required_reads_native'
            stale = other/'unset_required_reads_native'
            expected.write_text('same binary content'); stale.write_text('same binary content')
            (build/'unset_required_reads_target-Release.txt').write_text(str(expected)+'\n')
            with patch('native_observe.subprocess.run') as run:
                with self.assertRaises(ValueError): prepare_executable(build, stale)
                run.assert_not_called()

    def test_selected_target_is_built_before_use(self):
        with tempfile.TemporaryDirectory() as temporary:
            build = Path(temporary)
            executable = build/'unset_required_reads_native'
            executable.write_text('stale binary')
            manifest = build/'unset_required_reads_target-Release.txt'
            manifest.write_text(str(executable)+'\n')
            with patch('native_observe.subprocess.run', side_effect=lambda *a, **k: executable.write_text('rebuilt binary')) as run:
                self.assertEqual(prepare_executable(build, executable), (executable, 'Release', manifest))
                self.assertEqual(run.call_args.args[0], ['cmake', '--build', str(build), '--target', 'unset_required_reads_native', '--config', 'Release'])
                self.assertTrue(run.call_args.kwargs['check'])
            self.assertEqual(executable.read_text(), 'rebuilt binary')

    def test_missing_or_ambiguous_target_metadata_fails(self):
        with tempfile.TemporaryDirectory() as temporary:
            build = Path(temporary)
            executable = build/'unset_required_reads_native'
            with self.assertRaises(ValueError): target_artifact(build, executable)
            for config in ('Debug', 'Release'):
                (build/f'unset_required_reads_target-{config}.txt').write_text(str(executable)+'\n')
            with self.assertRaises(ValueError): target_artifact(build, executable)

    def test_failed_build_cannot_run_stale_executable(self):
        import subprocess
        with tempfile.TemporaryDirectory() as temporary:
            build = Path(temporary)
            executable = build/'unset_required_reads_native'
            executable.write_text('stale binary')
            (build/'unset_required_reads_target-Release.txt').write_text(str(executable)+'\n')
            with patch('native_observe.subprocess.run', side_effect=subprocess.CalledProcessError(1, 'cmake')):
                with self.assertRaises(subprocess.CalledProcessError): prepare_executable(build, executable)

if __name__ == '__main__': unittest.main()
