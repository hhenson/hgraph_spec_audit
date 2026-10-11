"""Verify recorded REF ownership and scalar-capability evidence without runtimes."""
import hashlib
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def check_flags(events, expected):
    fields=('reference_valid','data_valid','reference_modified','data_modified')
    assert len(events)==len(expected)
    for event,flags in zip(events,expected):
        assert all(event[field] is flag for field,flag in zip(fields,flags))

def check(public=None,native=None):
    if public is None:
        public=json.loads((HERE/'observed.json').read_text())
    if native is None:
        native=json.loads((HERE/'native_observed.json').read_text())
    reasoned=json.loads((HERE/'reasoned.json').read_text())
    native_reasoned=json.loads((HERE/'native_reasoned.json').read_text())
    for record,names in [(public,('observe.py','reasoned.json')),(native,('native.cpp','native_reasoned.json','native_observe.py','CMakeLists.txt'))]:
        assert record['repeats']==3
        assert record['sources_sha256']=={name:sha(HERE/name) for name in names}
    assert set(public['engines'])=={'python','cpp'}
    for engine,record in public['engines'].items():
        assert record['identity']['native']==(engine=='cpp')
        cases=record['cases']
        control=cases['outer_owner_control']
        assert [row['value'] for row in control['events']]==reasoned['outer_owner_control']['expected_followed']
        check_flags(control['events'],[(True,True,True,True)]+[(True,True,False,True)]*5)
        scalar=cases['scalar_and_reference_identity']
        assert scalar['reference_identity']==native_reasoned['reference_identity']
        assert scalar['bool_operations']==native_reasoned['bool_operations']
        owned=cases['owned']
        # Preserve measured flags, including the C++ target's late invalidation;
        # these are evidence checks, not the reasoned owner-expiry requirement.
        owned_flags=[(True,True,True,True),(True,True,False,True),(True,True,False,False)]
        if engine=='python':
            assert [row['value'] for row in owned['events']]==[7,8,8]
            assert owned['error_type']=='AttributeError'
            assert owned['message']=="'NoneType' object has no attribute 'graph'"
        else:
            assert [row['value'] for row in owned['events']]==[7,8,8,8,None,None]
            owned_flags += [(True,True,False,False)]+[(True,False,False,False)]*2
        check_flags(owned['events'],owned_flags)
    assert native['source_sha256']==native['sources_sha256']['native.cpp']
    assert native['sdk_files_sha256'] and len(native['binary_sha256'])==64 and len(native['compiler_sha256'])==64
    assert native['owned']==public['engines']['cpp']['cases']['owned']['events']
    assert native['outer_owner_control']==public['engines']['cpp']['cases']['outer_owner_control']['events']
    assert native['identity']==[native_reasoned['reference_identity']]
    assert native['bool_operations']==native_reasoned['bool_operations']
    assert native['assessment']=={'owned':'divergence','outer_owner_control':'match','reference_identity':'match','bool_operations':'match'}
    assert [row['value'] for row in native['owned']]!=native_reasoned['owned_followed']
    return True

if __name__=='__main__':
    check();print('Recorded reference ownership, identity and bool evidence verified')
