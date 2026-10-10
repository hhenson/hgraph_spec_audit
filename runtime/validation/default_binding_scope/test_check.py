import json
from pathlib import Path
import unittest
import check

HERE = Path(__file__).resolve().parent

class Evidence(unittest.TestCase):
    def setUp(self):
        self.record = json.loads((HERE / 'observed.json').read_text())
    def rejected(self):
        # Reseal process digests to exercise semantic comparisons independently.
        p = self.record['python']
        p['runs_sha256'] = [check.digest({'identity': p['identity'], 'results': p['results']})] * 3
        c = self.record['cpp']
        c['runs_sha256'] = [check.digest(c['results'])] * 3
        for r in c['rejections'].values():
            r['runs_sha256'] = [check.digest(r['capture'])] * 3
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

if __name__ == '__main__': unittest.main()
