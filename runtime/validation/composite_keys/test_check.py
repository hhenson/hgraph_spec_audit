import copy
import importlib.util
import json
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('composite_key_check', HERE / 'check.py')
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)

class RecordedCompositeKeyCases(unittest.TestCase):
    def setUp(self): self.evidence = json.loads((HERE / 'observed.json').read_text())
    def rejects(self, mutate):
        bad = copy.deepcopy(self.evidence)
        mutate(bad)
        with self.assertRaises(AssertionError): check.validate(bad)
    def test_recorded_evidence(self): check.validate(self.evidence)
    def test_rejects_erased_nominal_identity(self):
        self.rejects(lambda e: e['engines']['cpp']['observations']['struct_map']['raw'][0][0]['key'].update(type='Other'))
    def test_rejects_lost_component(self):
        self.rejects(lambda e: e['engines']['python']['observations']['tuple_map']['raw'][0][0]['key']['tuple'].pop())
    def test_rejects_duplicate_member_tick(self):
        self.rejects(lambda e: e['engines']['cpp']['observations']['tuple_set']['raw'][1]['added'].append({'tuple':[1,'a']}))
    def test_rejects_lost_equal_child_update(self):
        self.rejects(lambda e: e['engines']['python']['observations']['struct_map']['raw'][1].pop(0))
    def test_rejects_lost_removal(self):
        self.rejects(lambda e: e['engines']['cpp']['observations']['struct_set']['raw'].__setitem__(3,None))
