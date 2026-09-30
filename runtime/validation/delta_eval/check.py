"""Check preserved delta-eval evidence against pre-observation expectations."""
import hashlib
import json
from pathlib import Path
from native_observe import encode_expected
HERE=Path(__file__).resolve().parent
SCALARS={'bool','i64','f64','str','date','time','datetime','duration'}

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def digest(value):
    assert isinstance(value,str) and len(value)==64 and all(c in '0123456789abcdef' for c in value)
def manifest(value):
    assert isinstance(value,dict) and value
    for name,value in value.items():
        assert isinstance(name,str) and name and not name.startswith('/')
        digest(value)
def main():
    cases=json.loads((HERE/'reasoned.json').read_text())['cases']
    ids={c['id'] for c in cases}
    assert len(ids)==len(cases)==37
    evidence=json.loads((HERE/'observed.json').read_text())
    assert evidence['reasoned_sha256']==sha(HERE/'reasoned.json')
    assert evidence['harness_sha256']==sha(HERE/'observe.py')
    assert evidence['repeats']==3
    assert set(evidence['engines'])=={'python','cpp'}
    for name,engine in evidence['engines'].items():
        identity=engine['identity']
        assert identity['native']==(name=='cpp')
        assert identity['python'] and identity['hgraph'] and identity['eval_node_module']
        digest(identity['eval_node_source_sha256'])
        package=identity['package']
        manifest(package['sources_sha256']); manifest(package['artifacts_sha256'])
        content={k:v for k,v in package.items() if k!='identity_sha256'}
        assert hashlib.sha256(json.dumps(content,sort_keys=True).encode()).hexdigest()==package['identity_sha256']
        if name=='cpp':
            manifest(identity['native_artifacts']); manifest(identity['loaded_hgraph_libraries'])
            assert {'libhgraph_runtime.so','libhgraph_wiring.so','libhgraph_stdlib.so'}<=set(identity['loaded_hgraph_libraries'])
        else:
            assert not identity['native_artifacts'] and not identity['loaded_hgraph_libraries']
        assert set(engine['observations'])==ids
        assert set(engine['assessment'])==ids
        for case in cases:
            observation=engine['observations'][case['id']]
            assert 'error_type' not in observation,(name,case['id'],observation)
            raw=observation['raw_eval_node']
            assert raw is None or isinstance(raw,list)
            dense=[] if raw is None else list(raw)
            n=max(0,len(case['inputs'])-len(dense))
            dense += [None]*n
            assert observation['input_horizon']==len(case['inputs'])
            assert observation['padding_added']==n
            assert observation['dense_from_input_horizon']==dense
            status='match' if dense==case['expected'] else 'divergence'
            assert engine['assessment'][case['id']]==status
            assert status=='match',(name,case['id'],dense,case['expected'])
    native_path=HERE/'native_observed.json'
    if native_path.exists():
        native=json.loads(native_path.read_text())
        native_ids={c['id'] for c in cases if c['type'] in SCALARS}
        assert len(native_ids)==32
        assert set(native['observed'])==set(native['assessment'])==native_ids
        assert native['source_sha256']==sha(HERE/'native_scalar.cpp')
        assert native['recorder_sha256']==sha(HERE/'native_observe.py')
        assert native['reasoned_sha256']==sha(HERE/'reasoned.json')
        assert native['repeats']==3
        digest(native['binary_sha256']); manifest(native['sdk_headers_sha256']); manifest(native['loaded_libraries_sha256'])
        for library in ('libhgraph_runtime.so','libhgraph_wiring.so','libhgraph_stdlib.so'):
            assert native['loaded_libraries_sha256'][library]==evidence['engines']['cpp']['identity']['loaded_hgraph_libraries'][library]
        for case in cases:
            if case['id'] in native_ids:
                assert native['observed'][case['id']]==[encode_expected(v) for v in case['expected']],case['id']
                assert native['assessment'][case['id']]=='match'
    lifecycle=json.loads((HERE/'lifecycle_observed.json').read_text())
    lifecycle_expected=json.loads((HERE/'lifecycle_reasoned.json').read_text())['expectations']
    assert lifecycle['reasoned_sha256']==sha(HERE/'lifecycle_reasoned.json')
    assert lifecycle['harness_sha256']==sha(HERE/'lifecycle.py')
    assert lifecycle['repeats']==3 and set(lifecycle['engines'])=={'python','cpp'}
    for name,engine in lifecycle['engines'].items():
        assert engine['native']==(name=='cpp')
        assert engine['identity_sha256']==evidence['engines'][name]['identity']['package']['identity_sha256']
        assert set(engine['observed'])==set(engine['assessment'])==set(lifecycle_expected)
        for case,fields in lifecycle_expected.items():
            assert set(engine['assessment'][case])==set(fields)
            for field,value in fields.items():
                status='match' if engine['observed'][case][field]==value else 'divergence'
                assert engine['assessment'][case][field]==status
        for case in ('empty','all_silent'):
            result=engine['observed'][case];events=result['events']
            assert result['recorder_start_callbacks']==sum(x['event']=='recorder_started' for x in events)==1
            assert result['recorder_stop_callbacks']==sum(x['event']=='recorder_stopped' for x in events)==1
            names=[x['event'] for x in events]
            assert names.index('recorder_started')<names.index('recorder_stopped')<names.index('graph_stopped')<names.index('eval_returned')
            post=events[-1]['external_capture']
            assert post['present']==result['record_present_after_eval']
            assert post['entries']==result['record_entries_after_eval']
    control=json.loads((HERE/'lifecycle_control_observed.json').read_text())
    control_expected=json.loads((HERE/'lifecycle_control_reasoned.json').read_text())['expected']
    assert control['reasoned_sha256']==sha(HERE/'lifecycle_control_reasoned.json')
    assert control['harness_sha256']==sha(HERE/'lifecycle_control.py')
    assert control['repeats']==3 and set(control['engines'])=={'python','cpp'}
    for name,engine in control['engines'].items():
        assert engine['native']==(name=='cpp')
        assert engine['identity_sha256']==evidence['engines'][name]['identity']['package']['identity_sha256']
        assert set(engine['assessment'])==set(control_expected)
        for field,value in control_expected.items():
            status='match' if engine['observed'][field]==value else 'divergence'
            assert engine['assessment'][field]==status
        assert engine['observed']['positive_capture']=={'present':True,'entries':2}
        assert engine['capture_key'] in engine['observed']['positive_global_keys']
    operators=json.loads((HERE/'operator_observed.json').read_text())
    operator_cases=json.loads((HERE/'operator_reasoned.json').read_text())['cases']
    operator_ids={case['id'] for case in operator_cases}
    assert len(operator_ids)==len(operator_cases)==12
    assert operators['reasoned_sha256']==sha(HERE/'operator_reasoned.json')
    assert operators['harness_sha256']==sha(HERE/'operator_observe.py')
    assert operators['repeats']==3 and set(operators['engines'])=={'python','cpp'}
    for name,engine in operators['engines'].items():
        assert engine['native']==(name=='cpp')
        assert engine['identity_sha256']==evidence['engines'][name]['identity']['package']['identity_sha256']
        assert set(engine['observations'])==set(engine['assessment'])==operator_ids
        for case in operator_cases:
            result=engine['observations'][case['id']]
            horizon=max(map(len,case['inputs']),default=0)
            assert result['input_horizon']==horizon
            assert result['outputless']==(case['node']=='sink')
            if result['outputless']:
                assert result['raw'] is None
                dense=None
            else:
                assert result['raw'] is None or isinstance(result['raw'],list)
                dense=[] if result['raw'] is None else list(result['raw'])
                dense += [None]*max(0,horizon-len(dense))
            assert result['dense']==dense==case['expected']
            assert engine['assessment'][case['id']]=='match'
    print('49 cases × 2 engines and 32 direct native scalar cases match frozen traces; lifecycle evidence retains its divergences.')
if __name__=='__main__': main()
