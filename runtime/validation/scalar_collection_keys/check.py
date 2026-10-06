"""Check exact scalar membership observations and preserve NaN disagreements."""
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'atomic_snapshots'))
from provenance import validate_identity
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import sha

SCOPE = ['bool', 'i64', 'f64', 'str', 'date', 'time', 'datetime', 'duration',
         'civil_datetime', 'timezone', 'zoned_datetime', 'zoned_time', 'enum']
SET = [{'add': ['a', 'b'], 'remove': []}, None, {'add': [], 'remove': ['a']}]
MAP = [{'upsert': [['a', 10], ['b', 20]], 'remove': []},
       {'upsert': [['a', 10]], 'remove': []}, None, {'upsert': [], 'remove': ['a']}]


def provenance(evidence, floating=False):
    prefix = 'float_' if floating else ''
    assert evidence['repeats'] == 3 and type(evidence['repeats']) is int
    assert evidence['reasoned_sha256'] == sha(HERE / (prefix + 'reasoned.json'))
    assert evidence['harness_sha256'] == sha(HERE / (prefix + 'observe.py'))
    assert evidence['identity_helper_sha256'] == sha(HERE.parent / 'delta_eval/observe.py')
    assert set(evidence['engines']) == {'python', 'cpp'}
    for engine, result in evidence['engines'].items():
        validate_identity(result['identity'], engine)


def validate(evidence):
    provenance(evidence)
    reasoned = json.loads((HERE / 'reasoned.json').read_text())
    assert reasoned['scope'] == SCOPE
    assert reasoned['set_trace'] == SET and reasoned['map_trace'] == MAP
    for engine, result in evidence['engines'].items():
        assert set(result['observations']) == set(SCOPE)
        missing = {'zoned_time'} if engine == 'cpp' else {'zoned_time', 'timezone', 'zoned_datetime', 'civil_datetime'}
        for kind, observed in result['observations'].items():
            expected = {'availability': 'canonical authoring type unavailable'} if kind in missing else {
                'a_equals_b': False,
                'set': {'raw': SET, 'received': [x for x in SET if x is not None]},
                'map': {'raw': MAP, 'received': [x for x in MAP if x is not None]}}
            assert observed == expected, (engine, kind)


def set_delta(add=(), remove=()):
    return {'add': list(add), 'remove': list(remove)}


def map_delta(upsert=(), remove=()):
    return {'upsert': list(upsert), 'remove': list(remove)}


def result(raw, held):
    return {'raw': raw, 'received': [{'delta': d, 'held': h} for d, h in zip(raw, held) if d is not None]}


def validate_float(evidence):
    provenance(evidence, True)
    zero_set = [set_delta(['+0']), None, set_delta(remove=['+0'])]
    zero_map = [map_delta([['+0', 10]]), map_delta([['+0', 20]]), map_delta(remove=['+0'])]
    inf_set = [set_delta(['+inf', '-inf']), set_delta(remove=['+inf'])]
    inf_map = [map_delta([['+inf', 10], ['-inf', 20]]), map_delta(remove=['+inf'])]
    nan_set = [set_delta(['nan', 'nan']), set_delta(remove=['nan'])]
    nan_map = [map_delta([['nan', 10], ['nan', 20]]), map_delta(remove=['nan'])]
    for engine, value in evidence['engines'].items():
        expected = {
            'signed_zero': {'a_equals_b': True, 'a_equals_self': True, 'equal_hashes': True,
                            'set': result(zero_set, [['+0'], ['+0'], []]),
                            'map': result(zero_map, [[['+0', 10]], [['+0', 20]], []])},
            'infinities': {'a_equals_b': False, 'a_equals_self': True, 'equal_hashes': False,
                           'set': result(inf_set, [['+inf', '-inf'], ['-inf']]),
                           'map': result(inf_map, [[['+inf', 10], ['-inf', 20]], [['-inf', 20]]])},
            'nan': {'a_equals_b': False, 'a_equals_self': False, 'equal_hashes': False,
                    'set': result(nan_set, [['nan', 'nan'], ['nan']]),
                    'map': result(nan_map, [[['nan', 10], ['nan', 20]], [['nan', 20]]])}}
        if engine == 'cpp':
            expected['nan']['set'] = result([nan_set[0], None], [['nan', 'nan'], ['nan', 'nan']])
            expected['nan']['map'] = {'error_type': 'RuntimeError',
                                      'error': 'REMOVE: key not present in TSD (use REMOVE_IF_EXISTS to remove-if-present)',
                                      'received': []}
        assert value['observations'] == expected, engine


if __name__ == '__main__':
    validate(json.loads((HERE / 'observed.json').read_text()))
    validate_float(json.loads((HERE / 'float_observed.json').read_text()))
    print('Scalar collection identity checked; unavailable types and NaN disagreements preserved.')
