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
    def test_default_records(self): self.assertTrue(check.check())
    def test_empty_public_record_is_not_replaced(self):
        with self.assertRaises(KeyError): check.check({},self.native)
    def test_empty_native_record_is_not_replaced(self):
        with self.assertRaises(KeyError): check.check(self.public,{})
    def test_missing_engine_rejected(self):
        for engine in ('python','cpp'):
            with self.subTest(engine=engine):
                public=copy.deepcopy(self.public)
                del public['engines'][engine]
                with self.assertRaises(AssertionError): check.check(public,self.native)
    def test_empty_engines_rejected(self):
        self.public['engines']={}
        with self.assertRaises(AssertionError): check.check(self.public,self.native)
    def test_extra_engine_rejected(self):
        self.public['engines']['unsupported']=copy.deepcopy(self.public['engines']['python'])
        with self.assertRaises(AssertionError): check.check(self.public,self.native)
    def test_public_owned_flags_cannot_change(self):
        for engine,record in self.public['engines'].items():
            for index,event in enumerate(record['cases']['owned']['events']):
                for field in ('reference_valid','data_valid','reference_modified','data_modified'):
                    with self.subTest(engine=engine,index=index,field=field):
                        public=copy.deepcopy(self.public)
                        public['engines'][engine]['cases']['owned']['events'][index][field]=not event[field]
                        with self.assertRaises(AssertionError): check.check(public,self.native)
    def test_native_owned_flags_cannot_change(self):
        for index,event in enumerate(self.native['owned']):
            for field in ('reference_valid','data_valid','reference_modified','data_modified'):
                with self.subTest(index=index,field=field):
                    native=copy.deepcopy(self.native)
                    native['owned'][index][field]=not event[field]
                    with self.assertRaises(AssertionError): check.check(self.public,native)
    def test_matching_cpp_and_native_owned_flag_corruption_rejected(self):
        for index,event in enumerate(self.native['owned']):
            for field in ('reference_valid','data_valid','reference_modified','data_modified'):
                with self.subTest(index=index,field=field):
                    public=copy.deepcopy(self.public)
                    native=copy.deepcopy(self.native)
                    public['engines']['cpp']['cases']['owned']['events'][index][field]=not event[field]
                    native['owned'][index][field]=not event[field]
                    with self.assertRaises(AssertionError): check.check(public,native)
    def test_owned_flags_must_be_booleans(self):
        for field in ('reference_valid','data_valid','reference_modified','data_modified'):
            with self.subTest(field=field):
                public=copy.deepcopy(self.public)
                native=copy.deepcopy(self.native)
                public['engines']['cpp']['cases']['owned']['events'][0][field]=1
                native['owned'][0][field]=1
                with self.assertRaises(AssertionError): check.check(public,native)
    def test_outer_owner_control_flags_cannot_change(self):
        for engine,record in self.public['engines'].items():
            for index,event in enumerate(record['cases']['outer_owner_control']['events']):
                for field in ('reference_valid','data_valid','reference_modified','data_modified'):
                    with self.subTest(engine=engine,index=index,field=field):
                        public=copy.deepcopy(self.public)
                        native=copy.deepcopy(self.native)
                        public['engines'][engine]['cases']['outer_owner_control']['events'][index][field]=not event[field]
                        if engine=='cpp':
                            native['outer_owner_control'][index][field]=not event[field]
                        with self.assertRaises(AssertionError): check.check(public,native)
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
