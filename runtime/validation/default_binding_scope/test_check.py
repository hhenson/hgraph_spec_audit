import json
import hashlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import check
import python_probe

HERE = Path(__file__).resolve().parent

class Evidence(unittest.TestCase):
    def setUp(self):
        self.record = json.loads((HERE / 'observed.json').read_text())
    def reseal(self):
        # Reseal process digests to exercise semantic comparisons independently.
        p = self.record['python']
        p['runs_sha256'] = [check.digest({'identity': p['identity'], 'results': p['results']})] * 3
        c = self.record['cpp']
        for r in [c['syntax_control'], *c['rejections'].values()]:
            r['runs_sha256'] = [check.digest({'invocation': r['invocation'], 'capture': r['capture']})] * 3
        c['runs_sha256'] = [check.digest({k: v for k, v in c.items() if k != 'runs_sha256'})] * 3
    def rejected(self):
        self.reseal()
        with self.assertRaises(AssertionError): check.check(self.record)
    def test_compiler_diagnostics_are_not_a_semantic_contract(self):
        for rejection in self.record['cpp']['rejections'].values():
            rejection['capture']['stderr'] = "error: default argument references parameter 'first'"
            rejection['capture']['stdout'] = "diagnostic de compilation"
        self.reseal()
        self.assertTrue(check.check(self.record))
    def test_abnormal_process_termination_cannot_be_source_rejection(self):
        for code in (-9, -11, 3221225477):
            with self.subTest(code=code):
                self.record = json.loads((HERE / 'observed.json').read_text())
                capture = self.record['cpp']['rejections']['earlier_parameter']['capture']
                capture.update(exit_code=code, stdout='', stderr='')
                self.rejected()
    def test_normal_status_without_any_diagnostic_cannot_certify_rejection(self):
        capture = self.record['cpp']['rejections']['earlier_parameter']['capture']
        capture.update(exit_code=1, stdout='', stderr='')
        self.rejected()
    def test_boolean_is_not_a_compiler_exit_status(self):
        self.record['cpp']['rejections']['earlier_parameter']['capture']['exit_code'] = True
        self.rejected()
    def test_recorded(self): self.assertTrue(check.check(self.record))
    def test_unsupported_syntax_option_cannot_certify_source_rejection(self):
        for probe in [self.record['cpp']['syntax_control'], *self.record['cpp']['rejections'].values()]:
            probe['capture'].update(exit_code=1, stdout='', stderr='driver diagnostic')
        self.rejected()
    def test_successful_syntax_control_is_required(self):
        del self.record['cpp']['syntax_control']
        c=self.record['cpp']
        c['runs_sha256']=[check.digest({k:v for k,v in c.items() if k!='runs_sha256'})]*3
        with self.assertRaises(KeyError): check.check(self.record)
    def test_control_status_must_be_normal_zero_even_when_resealed(self):
        for code in (1, -9, 3221225477, False, None):
            with self.subTest(code=code):
                self.record=json.loads((HERE/'observed.json').read_text())
                self.record['cpp']['syntax_control']['capture']['exit_code']=code
                self.rejected()
    def test_control_and_each_rejection_share_exact_driver_options_and_sources(self):
        for name in ('syntax_control','earlier_parameter','shadow_parameter'):
            for field,value in [('compiler_sha256','0'*64),('flags',['-std=c++20']),
                                ('source','another.cpp'),('source_sha256','0'*64)]:
                with self.subTest(name=name,field=field):
                    self.record=json.loads((HERE/'observed.json').read_text())
                    cpp=self.record['cpp']
                    probe=cpp[name] if name=='syntax_control' else cpp['rejections'][name]
                    probe['invocation'][field]=value
                    self.rejected()
    def test_control_repeat_digests_cannot_be_dropped_or_changed(self):
        for values in ([], ['0'*64]*3, ['0'*64]*2):
            with self.subTest(values=values):
                self.record=json.loads((HERE/'observed.json').read_text())
                self.record['cpp']['syntax_control']['runs_sha256']=values
                c=self.record['cpp']
                c['runs_sha256']=[check.digest({k:v for k,v in c.items() if k!='runs_sha256'})]*3
                with self.assertRaises(AssertionError): check.check(self.record)
    def test_python_default_cannot_be_current_argument(self):
        self.record['python']['results']['shadow_parameter'] = 99
        self.rejected()
    def test_cpp_shadowing_rejection_cannot_be_reported_as_accepted(self):
        self.record['cpp']['rejections']['shadow_parameter']['capture']['exit_code'] = 0
        self.rejected()
    def test_cpp_template_binding_is_distinct_from_ordinary_parameter(self):
        self.record['cpp']['results']['template_parameter'] = [7, 7]
        self.rejected()
    def test_cpp_unevaluated_parameter_control_must_survive(self):
        self.record['cpp']['results']['unevaluated_parameter'] = False
        self.rejected()
    def test_field_default_cannot_hide_instance_read_difference(self):
        self.record['cpp']['results']['field_reference'] = [99, 7]
        self.rejected()
    def test_default_phase_difference_cannot_be_erased(self):
        self.record['python']['results']['evaluation_phase'] = [1, 2, 2]
        self.rejected()
    def test_source_fingerprint_required(self):
        self.record['sources_sha256']['positive.cpp'] = '0' * 64
        self.rejected()
    def test_python_executable_bound_to_process_digest(self):
        self.record['python']['identity']['executable_sha256'] = '0' * 64
        with self.assertRaises(AssertionError): check.check(self.record)
    def test_python_executable_hash_must_be_hex_even_when_resealed(self):
        self.record['python']['identity']['executable_sha256'] = 'z' * 64
        self.rejected()
    def test_python_executable_hash_required(self):
        del self.record['python']['identity']['executable_sha256']
        with self.assertRaises(KeyError): check.check(self.record)
    def test_cpp_provenance_bound_to_process_digest(self):
        for field, replacement in (('compiler_sha256', '0' * 64),
                                   ('binary_sha256', '0' * 64),
                                   ('compiler_version', 'different compiler'),
                                   ('flags', ['-std=c++20']),
                                   ('build', {'exit_code': 0, 'stdout': 'changed', 'stderr': ''})):
            with self.subTest(field=field):
                record = json.loads((HERE / 'observed.json').read_text())
                record['cpp'][field] = replacement
                with self.assertRaises(AssertionError): check.check(record)
    def test_cpp_hashes_must_be_hex_even_when_resealed(self):
        for field in ('compiler_sha256', 'binary_sha256'):
            with self.subTest(field=field):
                self.record = json.loads((HERE / 'observed.json').read_text())
                self.record['cpp'][field] = 'z' * 64
                self.rejected()
    def test_cpp_compiler_version_required_even_when_resealed(self):
        self.record['cpp']['compiler_version'] = ''
        self.rejected()

class ExecutableIdentity(unittest.TestCase):
    def test_resolved_binary_fingerprinted_without_publishing_path(self):
        with tempfile.TemporaryDirectory() as temporary:
            executable = Path(temporary) / 'executable'
            executable.write_bytes(b'first executable')
            launcher = Path(temporary) / 'python'
            launcher.symlink_to(executable)
            with patch.object(python_probe.sys, 'executable', str(launcher)), \
                 patch.object(python_probe.support, 'identity', return_value={'python': 'same version'}):
                before = python_probe.identity()
                self.assertEqual(before['executable_sha256'], hashlib.sha256(executable.read_bytes()).hexdigest())
                self.assertNotIn(temporary, json.dumps(before))
                executable.write_bytes(b'second executable')
                self.assertNotEqual(before, python_probe.identity())
    def test_probe_rejects_binary_change_during_measurement(self):
        with tempfile.TemporaryDirectory() as temporary:
            executable = Path(temporary) / 'python'
            executable.write_bytes(b'first executable')
            calls = 0
            def package_identity():
                nonlocal calls
                calls += 1
                if calls == 2: executable.write_bytes(b'second executable')
                return {'python': 'same version'}
            with patch.object(python_probe.sys, 'executable', str(executable)), \
                 patch.object(python_probe.support, 'identity', side_effect=package_identity), \
                 patch('sys.stdout', new_callable=io.StringIO):
                with self.assertRaises(AssertionError): python_probe.main()

if __name__ == '__main__': unittest.main()
