"""Check real growing-list forwarding and the unavailable historical growth path."""
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'atomic_snapshots'))
from provenance import validate_identity
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import sha


def validate(evidence):
    assert evidence['repeats'] == 3 and type(evidence['repeats']) is int
    assert evidence['reasoned_sha256'] == sha(HERE / 'reasoned.json')
    assert evidence['harness_sha256'] == sha(HERE / 'observe.py')
    assert evidence['identity_helper_sha256'] == sha(HERE.parent / 'delta_eval/observe.py')
    assert set(evidence['engines']) == {'python', 'cpp'}
    removed = {'remove': True}
    deltas = {'growth_update_shrink': [{'0': 1, '1': 2}, {'1': 3, '2': 4}, None, {'0': 5, '1': removed, '2': removed}],
              'shrink_empty_regrow': [{'0': 1, '1': 2}, {'0': removed, '1': removed}, {'0': 3}],
              'repeat_child': [{'0': 1}, {'0': 1}]}
    values = {'growth_update_shrink': [[1, 2], [1, 3, 4], None, [5]],
              'shrink_empty_regrow': [[1, 2], [], [3]], 'repeat_child': [[1], [1]]}
    for engine, result in evidence['engines'].items():
        validate_identity(result['identity'], engine)
        observations = result['observations']
        assert set(observations) == set(deltas) | {'all_silent', 'empty'}
        for case in ('all_silent', 'empty'):
            assert observations[case] == {'raw': None, 'received': []}
        for case, raw in deltas.items():
            actual = observations[case]
            if engine == 'cpp':
                expected = {'raw': raw, 'received': [
                    {'value': v, 'delta': d, 'valid': True, 'all_valid': True}
                    for v, d in zip(values[case], raw) if d is not None]}
                assert actual == expected, case
            else:
                assert set(actual) == {'error_type', 'error', 'received'}
                assert actual['error_type'] == 'NodeException' and actual['received'] == []
                count = 1 if case == 'repeat_child' else 2
                message = actual['error']
                assert message.startswith('replay_from_memory(key: str, tp: type[hgraph._types._tsl_type.TimeSeriesListInput[')
                assert f'NodeError: Expected 0 elements, got {count}\n' in message
                assert f'ValueError: Expected 0 elements, got {count}\n' in message
                assert message.endswith('eval_node_graph.replay_from_memory<0>: replay_from_memory(key, tp, is_operator, recordable_id)\n')


if __name__ == '__main__':
    validate(json.loads((HERE / 'observed.json').read_text()))
    print('Native growing-list deltas checked; historical growth failures retained.')
