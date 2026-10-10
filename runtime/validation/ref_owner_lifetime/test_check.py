import copy
import json
from pathlib import Path
import unittest
import check
HERE=Path(__file__).resolve().parent

class RecordedEvidence(unittest.TestCase):
    def setUp(self):
        self.public=json.loads((HERE/'observed.json').read_text())
        self.native=json.loads((HERE/'native_observed.json').read_text())
    def test_recorded(self): self.assertTrue(check.check(self.public,self.native))
    def test_stale_capture_cannot_be_reported_as_expired(self):
        self.native['owned'][3]['value']=None
        with self.assertRaises(AssertionError): check.check(self.public,self.native)
    def test_live_outer_owner_cannot_be_expired(self):
        self.public['engines']['python']['cases']['outer_owner_control']['events'][3]['value']=None
        with self.assertRaises(AssertionError): check.check(self.public,self.native)
    def test_identity_cannot_be_payload_equality(self):
        self.native['identity'][0]['distinct_equal_endpoints']=True
        with self.assertRaises(AssertionError): check.check(self.public,self.native)
    def test_false_bool_order_cannot_pass(self):
        self.native['bool_operations']['false_before_true']=False
        with self.assertRaises(AssertionError): check.check(self.public,self.native)
    def test_source_fingerprint_required(self):
        self.native['sources_sha256']['native.cpp']='0'*64
        with self.assertRaises(AssertionError): check.check(self.public,self.native)

if __name__=='__main__': unittest.main()
