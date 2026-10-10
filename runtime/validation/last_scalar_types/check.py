"""Check byte traces and preserve the measured object-bridge boundary."""
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from evidence_identity import validate_identity
spec = importlib.util.spec_from_file_location('last_scalar_probe', HERE/'observe.py')
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)


def validate(data):
    corpus = json.loads((HERE/'reasoned.json').read_text())
    assert data['reasoned_sha256'] == probe.support.sha(HERE/'reasoned.json')
    assert data['observer_sha256'] == probe.support.sha(HERE/'observe.py')
    assert data['identity_support_sha256'] == probe.support.sha(HERE.parent/'delta_eval/observe.py')
    assert data['repeats'] == 3 and set(data['engines']) == {'python','cpp'}
    required = {'bytes_'+name for name in corpus['patterns']} | {'byte_constructor','bad_-1','bad_256','object_bridge_mixed','object_bridge_mutable_retention'}
    for name, engine in data['engines'].items():
        validate_identity(engine['identity'], name)
        assert engine['identity']['native'] == (name=='cpp')
        cases = engine['cases']
        assert set(cases) == required
        for pattern, tokens in corpus['patterns'].items():
            observed = cases['bytes_'+pattern]
            expected = [None if t is None else {'bytes':corpus['bytes'][t]} for t in tokens]
            assert observed['horizon'] == len(tokens)
            assert observed['dense'] == expected
            assert observed['raw'] == (expected if any(t is not None for t in tokens) else None)
            assert observed['received'] == [{'value':v,'delta':v} for v in expected if v is not None]
        constructor = cases['byte_constructor']
        assert constructor == {'empty':{'bytes':[]},'valid':{'bytes':[0,127,128,255]},'equal':True,'equal_hash':True,'unsigned_order':True}
        for bad in (-1,256):
            assert cases['bad_'+str(bad)]['error_type'] == 'ValueError'
            assert cases['bad_'+str(bad)]['message']
        mixed = [{'type':'int','value':0},{'type':'bool','value':False},{'type':'str','value':''},{'bytes':[]},{'list':[{'type':'int','value':1}]},None,{'type':'str','value':'next'}]
        assert cases['object_bridge_mixed']['dense'] == cases['object_bridge_mixed']['raw'] == mixed
        assert cases['object_bridge_mixed']['received'] == [{'value':v,'delta':v} for v in mixed if v is not None]
        retained = cases['object_bridge_mutable_retention']
        before = [{'list':[{'type':'int','value':1}]},None,{'list':[{'type':'int','value':2}]}]
        assert retained['dense'] == retained['raw'] == before
        after = json.loads(json.dumps(before))
        if name == 'python':
            after[0]['list'].append({'type':'int','value':9})
        assert retained['captures_after_source_mutation'] == after


def validate_native(data):
    for name,digest in data['sources_sha256'].items():
        assert digest==probe.support.sha(HERE/name)
    assert set(data['sources_sha256'])=={'native.cpp','native_reasoned.json','native_observe.py','CMakeLists.txt'}
    assert data['source_sha256']==data['sources_sha256']['native.cpp']
    assert data['repeats']==3 and data['compiler_version'] and data['flags']
    for digest in [data['binary_sha256'],data['compiler_sha256'],*data['sdk_files_sha256'].values(),*data['loaded_libraries_sha256'].values()]:
        assert len(digest)==64 and set(digest)<=set('0123456789abcdef')
    assert 'include/hgraph/types/static_node.h' in data['sdk_files_sha256']
    assert 'lib/libhgraph_runtime.a' in data['sdk_files_sha256']
    expected=json.loads((HERE/'native_reasoned.json').read_text())
    assert set(data['observed'])==set(expected['expected'])|set(expected['capability_expectations'])
    assert set(data['graphs'])==set(expected['graph_expected'])
    for name,value in expected['expected'].items():
        assert data['observed'][name]==(False if name=='any_flattens' else value)
        assert data['assessment'][name]==('divergence' if name=='any_flattens' else 'match')
    assert data['observed']['any_missing_equality']=='false'
    assert data['observed']['any_missing_order']=='unordered'
    assert data['observed']['any_missing_hash']=={'error':'ValueOps::hash is not available for this value type'}
    for name in expected['capability_expectations']:
        assert data['assessment'][name]==('match' if name=='any_missing_hash' else 'divergence')
    for name,values in expected['graph_expected'].items():
        assert data['graphs'][name]==values and data['assessment'][name+'_graph']=='match'
    assert set(data['assessment'])==set(data['observed'])|{name+'_graph' for name in data['graphs']}


if __name__ == '__main__':
    validate(json.loads((HERE/'observed.json').read_text()))
    validate_native(json.loads((HERE/'native_observed.json').read_text()))
    print('Byte, native boxed and registered atomic traces verified; disagreements retained.')
