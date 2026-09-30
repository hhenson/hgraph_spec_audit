"""Evidence cannot pass after losing engines/cases or silently rewriting padding."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'runtime/validation/delta_eval'
sys.path.insert(0,str(SOURCE))
_spec=importlib.util.spec_from_file_location('delta_evidence_check',SOURCE/'check.py')
check=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check)

class DeltaEvidenceTest(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)/'evidence'
        shutil.copytree(SOURCE,self.root,ignore=shutil.ignore_patterns('__pycache__'))
        self.original=check.HERE; check.HERE=self.root
    def tearDown(self):
        check.HERE=self.original; self.temp.cleanup()
    def mutate(self,name,fn):
        path=self.root/name; value=json.loads(path.read_text()); fn(value)
        path.write_text(json.dumps(value))
    def verify(self):
        with contextlib.redirect_stdout(io.StringIO()): check.main()
    def test_preserved_evidence(self): self.verify()
    def test_missing_engine_rejected(self):
        self.mutate('observed.json',lambda x:x['engines'].pop('python'))
        with self.assertRaises(AssertionError): self.verify()
    def test_missing_case_rejected(self):
        self.mutate('observed.json',lambda x:x['engines']['cpp']['observations'].pop('i64_empty'))
        with self.assertRaises(AssertionError): self.verify()
    def test_padding_drift_rejected(self):
        self.mutate('observed.json',lambda x:x['engines']['python']['observations']['bool_all_silent'].update(padding_added=0))
        with self.assertRaises(AssertionError): self.verify()
    def test_hash_drift_rejected(self):
        with (self.root/'observe.py').open('a') as f:f.write('\n# changed\n')
        with self.assertRaises(AssertionError): self.verify()
    def test_missing_native_case_rejected(self):
        self.mutate('native_observed.json',lambda x:x['observed'].pop('i64_empty'))
        with self.assertRaises(AssertionError): self.verify()
    def test_native_provenance_loss_rejected(self):
        self.mutate('native_observed.json',lambda x:x.update(loaded_libraries_sha256={}))
        with self.assertRaises(AssertionError): self.verify()
    def test_lifecycle_divergence_cannot_be_relabelled(self):
        self.mutate('lifecycle_observed.json',lambda x:x['engines']['cpp']['assessment']['empty'].update(record_present_after_eval='match'))
        with self.assertRaises(AssertionError): self.verify()
    def test_lifecycle_missing_callback_rejected(self):
        self.mutate('lifecycle_observed.json',lambda x:x['engines']['python']['observed']['empty']['events'].pop(0))
        with self.assertRaises(AssertionError): self.verify()
    def test_positive_control_cannot_lose_observability(self):
        self.mutate('lifecycle_control_observed.json',lambda x:x['engines']['cpp']['observed'].update(positive_capture={'present':False,'entries':None}))
        with self.assertRaises(AssertionError): self.verify()
    def test_operator_corpus_cannot_lose_a_case(self):
        self.mutate('operator_observed.json',lambda x:x['engines']['cpp']['observations'].pop('false_trigger'))
        with self.assertRaises(AssertionError): self.verify()
    def test_outputless_cannot_be_reported_as_empty_recording(self):
        self.mutate('operator_observed.json',lambda x:x['engines']['python']['observations']['sink_empty'].update(dense=[]))
        with self.assertRaises(AssertionError): self.verify()
    def test_multi_input_padding_cannot_trim_longest_horizon(self):
        self.mutate('operator_observed.json',lambda x:x['engines']['cpp']['observations']['empty_lhs'].update(input_horizon=0))
        with self.assertRaises(AssertionError): self.verify()
if __name__=='__main__':unittest.main()
