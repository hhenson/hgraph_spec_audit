"""Evidence corruption must not hide a difference or invent a publication."""
import json
from pathlib import Path
import unittest
from check import validate


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((Path(__file__).parent / 'observed.json').read_text())

    def test_recorded_evidence(self):
        validate(self.data)

    def test_masked_difference(self):
        self.data['engines']['python']['assessment']['initial_fixed'][0]['status'] = 'match'
        with self.assertRaises(AssertionError):
            validate(self.data)

    def test_manufactured_empty_tick(self):
        self.data['engines']['cpp']['observations']['initial_set']['cycles'][1]['forward']['publication'] = {
            'present': True, 'payload': {'added': [], 'removed': []}}
        with self.assertRaises(AssertionError):
            validate(self.data)

    def test_empty_replaced_by_silence(self):
        self.data['engines']['python']['observations']['initial_set']['dense_from_input_horizon'][0] = None
        with self.assertRaises(AssertionError):
            validate(self.data)

    def test_missing_unsupported_case(self):
        del self.data['engines']['cpp']['observations']['initial_tuple']
        with self.assertRaises(AssertionError):
            validate(self.data)

    def test_changed_reasoning_hash(self):
        self.data['reasoned_sha256'] = '0' * 64
        with self.assertRaises(AssertionError):
            validate(self.data)

    def test_missing_producer_rows(self):
        self.data['engines']['python']['observations']['initial_set']['producer'] = []
        with self.assertRaises(AssertionError):
            validate(self.data)

    def test_missing_notifications(self):
        for side in ('source', 'forward'):
            with self.subTest(side=side):
                original = self.data['engines']['cpp']['observations']['initial_set'][side + '_notifications']
                self.data['engines']['cpp']['observations']['initial_set'][side + '_notifications'] = []
                with self.assertRaises(AssertionError):
                    validate(self.data)
                self.data['engines']['cpp']['observations']['initial_set'][side + '_notifications'] = original

    def test_changed_notification_payload(self):
        self.data['engines']['python']['observations']['initial_set']['source_notifications'][0]['state']['publication']['payload'] = {'added': [7], 'removed': []}
        with self.assertRaises(AssertionError):
            validate(self.data)


if __name__ == '__main__':
    unittest.main()
