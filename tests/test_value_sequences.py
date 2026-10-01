"""Guard coverage, engine identity and ownership assessment in sequence evidence."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'runtime/validation/value_sequences'
spec=importlib.util.spec_from_file_location('value_sequence_evidence_check',SOURCE/'check.py')
check=importlib.util.module_from_spec(spec);spec.loader.exec_module(check)

class ValueSequenceEvidenceTest(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();base=Path(self.temp.name)
        self.root=base/'value_sequences';shutil.copytree(SOURCE,self.root,ignore=shutil.ignore_patterns('__pycache__'))
        (base/'delta_eval').mkdir();shutil.copy2(SOURCE.parent/'delta_eval/observe.py',base/'delta_eval/observe.py')
        self.original=check.HERE;check.HERE=self.root
    def tearDown(self):check.HERE=self.original;self.temp.cleanup()
    def verify(self):
        with contextlib.redirect_stdout(io.StringIO()):check.main()
    def mutate(self,name,fn):
        path=self.root/name;value=json.loads(path.read_text());fn(value);path.write_text(json.dumps(value))
    def test_saved_evidence(self):self.verify()
    def test_missing_engine_rejected(self):
        self.mutate('observed.json',lambda x:x['engines'].pop('python'))
        with self.assertRaises(AssertionError):self.verify()
    def test_missing_alias_group_rejected(self):
        self.mutate('observed.json',lambda x:x['engines']['cpp']['observed'].pop('global_state_aliasing'))
        with self.assertRaises(AssertionError):self.verify()
    def test_source_drift_rejected(self):
        with (self.root/'native.cpp').open('a') as f:f.write('\n// drift\n')
        with self.assertRaises(AssertionError):self.verify()
    def test_lost_native_case_rejected(self):
        self.mutate('native_observed.json',lambda x:x['observed'].pop('native_value_clone'))
        with self.assertRaises(AssertionError):self.verify()
    def test_copy_divergence_cannot_be_relabelled(self):
        self.mutate('native_observed.json',lambda x:x['observed'].update(native_value_clone=[99,2,3]))
        with self.assertRaises(AssertionError):self.verify()
    def test_fake_engine_identity_rejected(self):
        self.mutate('observed.json',lambda x:x['engines']['python']['identity'].update(native=True))
        with self.assertRaises(AssertionError):self.verify()
if __name__=='__main__':unittest.main()
