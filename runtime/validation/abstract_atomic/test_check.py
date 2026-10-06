import copy
import importlib.util
import json
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('abstract_atomic_check', HERE / 'check.py')
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)

class RecordedFamilyCases(unittest.TestCase):
    def setUp(self):
        self.evidence = json.loads((HERE / 'observed.json').read_text())

    def rejects(self, mutate):
        bad = copy.deepcopy(self.evidence)
        mutate(bad)
        with self.assertRaises(AssertionError): check.validate(bad)

    def test_recorded_evidence(self):
        check.validate(self.evidence)

    def test_rejects_erased_concrete_identity(self):
        self.rejects(lambda e: e['engines']['cpp']['observations']['snapshots']['raw'][3].update(type='First'))

    def test_rejects_lost_repeat(self):
        self.rejects(lambda e: e['engines']['cpp']['observations']['snapshots']['raw'].__setitem__(1, None))

    def test_rejects_aliased_source(self):
        self.rejects(lambda e: e['engines']['cpp']['observations']['retention']['first_after_source_mutation'][0]['values'].append(2))

    def test_preserves_construction_divergence(self):
        self.rejects(lambda e: e['engines']['cpp']['observations']['abstract_construction'].update(accepted=False))

    def test_preserves_historical_absence(self):
        self.rejects(lambda e: e['engines']['python'].update(observations={'declaration': {'accepted': True}}))
