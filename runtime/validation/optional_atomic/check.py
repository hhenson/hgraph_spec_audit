"""Check optional-field presence and retain the observed Python alias difference."""
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'atomic_snapshots'))
from provenance import validate_identity
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import sha


def validate(evidence):
    assert type(evidence['repeats']) is int and evidence['repeats'] == 3
    assert evidence['reasoned_sha256'] == sha(HERE / 'reasoned.json')
    assert evidence['harness_sha256'] == sha(HERE / 'observe.py')
    assert evidence['identity_helper_sha256'] == sha(HERE.parent / 'delta_eval/observe.py')
    assert set(evidence['engines']) == {'python', 'cpp'}
    for engine, result in evidence['engines'].items():
        validate_identity(result['identity'], engine)
        cases = result['observations']
        assert set(cases) == {'OptionalRecord', 'DefaultNoneRecord', 'OptionalList'}
        for name in ('OptionalRecord', 'DefaultNoneRecord'):
            def value(label, field):
                return {'type': name, 'name': label, 'value': field}
            trace = [value('a', None), value('a', 0), None, value('b', 7), value('a', None)]
            assert cases[name] == {'input': trace, 'raw': trace,
                                   'received': [v for v in trace if v is not None],
                                   'empty': None, 'silent': None}, (engine, name)
        def value(field):
            return {'type': 'OptionalList', 'values': field}
        trace = [value(None), value([1]), None, value([]), value(None)]
        after = [value(None), value([1, 2]), None, value([]), value(None)] if engine == 'python' else trace
        assert cases['OptionalList'] == {'input': trace, 'raw': trace,
                                         'received': [v for v in trace if v is not None],
                                         'empty': None, 'silent': None, 'after_source': after}


if __name__ == '__main__':
    validate(json.loads((HERE / 'observed.json').read_text()))
    print('Optional field presence checked; Python nested aliasing retained explicitly.')
