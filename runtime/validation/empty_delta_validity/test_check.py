"""Evidence corruption must not hide a difference or invent a publication."""
import copy
import json
from pathlib import Path
import unittest
from check import validate, probe


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

    def test_supported_surface_cannot_be_relabeled_error(self):
        o = self.data['engines']['python']['observations']['initial_set']
        o.update(capability='error', phase='eval_node', error_type='InventedError', error='invented')
        del o['raw_eval_node']
        with self.assertRaises(AssertionError):
            validate(self.data)

    def test_consistent_nonempty_initial_publication_is_rejected(self):
        o = self.data['engines']['cpp']['observations']['initial_set']
        payload = {'added': [7], 'removed': []}
        for item in o['producer']:
            item['state']['value'] = [7]
            if item['step'] == 1:
                item['state']['publication']['payload'] = copy.deepcopy(payload)
        for row in o['cycles']:
            for side in ('source', 'forward'):
                row[side]['value'] = [7]
                if row['step'] == 1:
                    row[side]['publication']['payload'] = copy.deepcopy(payload)
        for side in ('source', 'forward'):
            o[side + '_notifications'][0]['state'] = copy.deepcopy(o['cycles'][0][side])
        o['raw_eval_node'][0] = copy.deepcopy(payload)
        o['dense_from_input_horizon'][0] = copy.deepcopy(payload)
        with self.assertRaises(AssertionError):
            validate(self.data)

    def test_full_horizon_expectations_reject_retention_changes(self):
        cases = {c['id']: c for c in json.loads((Path(__file__).parent / 'reasoned.json').read_text())['cases']}
        for case_id, path, mutate in (
            ('initial_set', 'cycles.1.source.valid', lambda o: o['cycles'][1]['source'].update(valid=False)),
            ('held_fixed', 'cycles.2.source.value', lambda o: o['cycles'][2]['source'].update(value=[99, 20])),
            ('revalidate_fixed', 'cycles.3.source.children.0.valid', lambda o: o['cycles'][3]['source']['children']['0'].update(valid=True)),
        ):
            with self.subTest(case=case_id):
                o = self.data['engines']['cpp']['observations'][case_id]
                mutate(o)
                findings = {f['path']: f['status'] for f in probe.support.assess(cases[case_id], o)}
                self.assertEqual(findings[path], 'divergence')
                with self.assertRaises(AssertionError):
                    validate(self.data)

    def test_suppressed_producer_tick(self):
        for name in ('python', 'cpp'):
            with self.subTest(engine=name):
                state = self.data['engines'][name]['observations']['cancel_set']['producer'][1]['state']
                state['modified'] = False
                state['publication'] = {'present': False}
                with self.assertRaises(AssertionError):
                    validate(self.data)

    def test_child_validity_changes_assessment(self):
        for name in ('python', 'cpp'):
            with self.subTest(engine=name):
                o = self.data['engines'][name]['observations']['initial_fixed']
                o['cycles'][0]['source']['children']['0']['valid'] = True
                with self.assertRaises(AssertionError):
                    validate(self.data)

    def test_missing_invalidation_notification(self):
        for name in ('python', 'cpp'):
            with self.subTest(engine=name):
                o = self.data['engines'][name]['observations']['revalidate_set']
                original = o['source_notifications']
                o['source_notifications'] = [n for n in original if n['step'] != 3]
                with self.assertRaises(AssertionError):
                    validate(self.data)
                o['source_notifications'] = original

    def test_null_raw_replaced_by_empty_list(self):
        for name in ('python', 'cpp'):
            with self.subTest(engine=name):
                o = self.data['engines'][name]['observations']['initial_fixed']
                self.assertIsNone(o['raw_eval_node'])
                o['raw_eval_node'] = []
                with self.assertRaises(AssertionError):
                    validate(self.data)
                o['raw_eval_node'] = None

    def test_changed_notification_payload(self):
        self.data['engines']['python']['observations']['initial_set']['source_notifications'][0]['state']['publication']['payload'] = {'added': [7], 'removed': []}
        with self.assertRaises(AssertionError):
            validate(self.data)


if __name__ == '__main__':
    unittest.main()
