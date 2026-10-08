import json
import copy
import tempfile
from pathlib import Path
import unittest
from check import validate
from native_observe import compile_command

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

if __name__ == '__main__': unittest.main()
