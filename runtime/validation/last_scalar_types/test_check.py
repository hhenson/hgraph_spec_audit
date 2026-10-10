"""Corrupted reference records must fail rather than broaden scalar coverage."""
import copy
import json
from pathlib import Path
import unittest
from check import validate, validate_native


class ScalarEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((Path(__file__).parent/'observed.json').read_text())

    def test_recorded_evidence(self):
        validate(self.data)

    def test_native_record(self):
        validate_native(json.loads((Path(__file__).parent/'native_observed.json').read_text()))

    def test_native_corruption(self):
        original=json.loads((Path(__file__).parent/'native_observed.json').read_text())
        mutations=[
            lambda d:d['observed'].update(any_flattens=True),
            lambda d:d['observed'].update(any_missing_equality={'error':'expected error'}),
            lambda d:d['graphs']['any'].__setitem__(0,None),
            lambda d:d['graphs']['native'].__setitem__(1,None),
            lambda d:d['assessment'].update(any_missing_order='match'),
            lambda d:d['sdk_files_sha256'].pop('lib/libhgraph_runtime.a'),
        ]
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                data=copy.deepcopy(original);mutation(data)
                with self.assertRaises(AssertionError):validate_native(data)

    def test_corruption(self):
        mutations = [
            lambda d: d.update(reasoned_sha256='0'*64),
            lambda d: d['engines']['cpp']['cases']['bytes_equal_distinct']['dense'].__setitem__(0,None),
            lambda d: d['engines']['python']['cases']['bytes_all_silent'].update(raw=[]),
            lambda d: d['engines']['cpp']['cases']['bytes_silence']['received'].pop(),
            lambda d: d['engines']['cpp']['cases']['bad_256'].update(error_type='success'),
            lambda d: d['engines']['python']['cases']['object_bridge_mutable_retention']['captures_after_source_mutation'][0]['list'].pop(),
            lambda d: d['engines']['cpp']['cases'].pop('object_bridge_mixed'),
        ]
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                data = copy.deepcopy(self.data)
                mutation(data)
                with self.assertRaises(AssertionError):
                    validate(data)


if __name__ == '__main__':
    unittest.main()
