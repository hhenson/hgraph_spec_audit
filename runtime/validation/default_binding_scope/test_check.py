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
    def rejected(self):
        # Reseal process digests to exercise semantic comparisons independently.
        p = self.record['python']
        p['runs_sha256'] = [check.digest({'identity': p['identity'], 'results': p['results']})] * 3
        c = self.record['cpp']
        for r in c['rejections'].values():
            r['runs_sha256'] = [check.digest(r['capture'])] * 3
        c['runs_sha256'] = [check.digest({k: v for k, v in c.items() if k != 'runs_sha256'})] * 3
        with self.assertRaises(AssertionError): check.check(self.record)
    def test_recorded(self): self.assertTrue(check.check(self.record))
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
