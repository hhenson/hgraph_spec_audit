"""Measure frozen REF export requirements using public interpreters, never HGL."""
import argparse
import contextlib
from datetime import datetime, timezone
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('support', HERE.parent / 'delta_eval/observe.py')
support = importlib.util.module_from_spec(spec)
spec.loader.exec_module(support)
CORPUS = HERE / 'reasoned.json'


def measure(case):
    import hgraph as hg
    from hgraph.test import eval_node

    events = []
    @hg.compute_node
    def producer(value: hg.TS[int]) -> hg.TS[int]:
        return value.delta_value
    @hg.compute_node
    def relay(value: hg.REF[hg.TS[int]]) -> hg.REF[hg.TS[int]]:
        return value.value

    if case['kind'] == 'scalar':
        @hg.graph
        def inner_first(first: hg.TS[int], second: hg.TS[int]) -> hg.REF[hg.TS[int]]:
            return relay(producer(first))
        @hg.graph
        def inner_second(first: hg.TS[int], second: hg.TS[int]) -> hg.REF[hg.TS[int]]:
            return relay(producer(second))
        @hg.graph
        def inner_route(inner: hg.TS[bool], first: hg.TS[int], second: hg.TS[int]) -> hg.REF[hg.TS[int]]:
            return hg.switch_(inner, {True: inner_first, False: inner_second}, first=first, second=second)
        @hg.graph
        def outer_first(inner: hg.TS[bool], first: hg.TS[int], second: hg.TS[int], third: hg.TS[int], fourth: hg.TS[int]) -> hg.REF[hg.TS[int]]:
            return inner_route(inner, first, second)
        @hg.graph
        def outer_second(inner: hg.TS[bool], first: hg.TS[int], second: hg.TS[int], third: hg.TS[int], fourth: hg.TS[int]) -> hg.REF[hg.TS[int]]:
            return inner_route(inner, third, fourth)
        @hg.compute_node
        def followed(value: hg.TS[int]) -> hg.TS[int]:
            return value.delta_value
        @hg.compute_node
        def observe(value: hg.TS[int]) -> hg.TS[str]:
            row = value.delta_value
            events.append(row)
            return json.dumps(row, sort_keys=True)
        @hg.graph
        def graph(outer: hg.TS[bool], inner: hg.TS[bool], first: hg.TS[int], second: hg.TS[int], third: hg.TS[int], fourth: hg.TS[int]) -> hg.TS[str]:
            selected = hg.switch_(outer, {True: outer_first, False: outer_second}, inner=inner, first=first, second=second, third=third, fourth=fourth)
            return observe(followed(selected))
    else:
        class Pair(hg.TimeSeriesSchema):
            left: hg.TS[int]
            right: hg.TS[int]
        @hg.compute_node
        def tree_relay(value: hg.REF[hg.TSB[Pair]]) -> hg.REF[hg.TSB[Pair]]:
            return value.value
        @hg.graph
        def natural(left: hg.TS[int], right: hg.TS[int]) -> hg.REF[hg.TSB[Pair]]:
            return tree_relay(hg.TSB[Pair].from_ts(left=left, right=right))
        @hg.graph
        def duplicate(left: hg.TS[int], right: hg.TS[int]) -> hg.REF[hg.TSB[Pair]]:
            return tree_relay(hg.TSB[Pair].from_ts(left=left, right=left))
        @hg.graph
        def pair_route(duplicate_left: hg.TS[bool], left: hg.TS[int], right: hg.TS[int]) -> hg.REF[hg.TSB[Pair]]:
            return hg.switch_(duplicate_left, {False: natural, True: duplicate}, left=left, right=right)
        @hg.graph
        def pair_first(duplicate_left: hg.TS[bool], first_left: hg.TS[int], first_right: hg.TS[int], second_left: hg.TS[int], second_right: hg.TS[int]) -> hg.REF[hg.TSB[Pair]]:
            return pair_route(duplicate_left, producer(first_left), producer(first_right))
        @hg.graph
        def pair_second(duplicate_left: hg.TS[bool], first_left: hg.TS[int], first_right: hg.TS[int], second_left: hg.TS[int], second_right: hg.TS[int]) -> hg.REF[hg.TSB[Pair]]:
            return pair_route(duplicate_left, producer(second_left), producer(second_right))
        @hg.compute_node
        def followed(value: hg.TSB[Pair]) -> hg.TSB[Pair]:
            return dict(value.delta_value)
        @hg.compute_node
        def observe(value: hg.TSB[Pair]) -> hg.TS[str]:
            row = support.encode(value.delta_value)
            events.append(row)
            return json.dumps(row, sort_keys=True)
        @hg.graph
        def graph(enabled: hg.TS[bool], duplicate_left: hg.TS[bool], first_left: hg.TS[int], first_right: hg.TS[int], second_left: hg.TS[int], second_right: hg.TS[int]) -> hg.TS[str]:
            selected = hg.switch_(enabled, {True: pair_first, False: pair_second}, duplicate_left=duplicate_left, first_left=first_left, first_right=first_right, second_left=second_left, second_right=second_right)
            return observe(followed(selected))

    result = {'input_horizon': case['input_horizon']}
    try:
        # Keep the public result untouched; decoded/padded views are separately named.
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            raw = eval_node(graph, **case['inputs'])
        result['raw_eval_node'] = raw
        decoded = [] if raw is None else [None if row is None else json.loads(row) for row in raw]
        result['decoded_eval_node'] = decoded
        result['padding_added'] = max(0, case['input_horizon'] - len(decoded))
        result['dense_from_input_horizon'] = decoded + [None] * result['padding_added']
    except Exception as exc:
        message = str(exc)
        for prefix in (str(HERE.parents[3]), str(Path.home()), sys.prefix):
            message = message.replace(prefix, '<private-path>')
        result.update(error_type=type(exc).__name__, message=message)
    result['events'] = events
    return result


def probe():
    identity = support.identity()
    corpus = json.loads(CORPUS.read_text())
    cases = {name: measure(corpus['cases'][name]) for name in corpus['case_order']}
    assert identity == support.identity(), 'Loaded artifacts changed during measurement'
    return {'identity': identity, 'cases': cases}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--probe', action='store_true')
    parser.add_argument('--python', type=Path)
    parser.add_argument('--cpp', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.probe:
        print(json.dumps(probe(), sort_keys=True))
        return
    if not args.python or not args.cpp or not args.output or args.output.exists():
        parser.error('Independent interpreters and a new evidence destination required')
    sources = {name: support.sha(HERE / name) for name in ('reasoned.json', 'observe.py')}
    dependencies = {name: support.sha(HERE.parent / name) for name in ('delta_eval/observe.py', 'fixed/reference_identity.py', 'fixed/native_identity.py')}
    corpus = json.loads(CORPUS.read_text())
    record = {'measured_at': datetime.now(timezone.utc).isoformat(), 'repeats': 3,
              'sources_sha256': sources, 'support_sha256': dependencies, 'engines': {}}
    for engine, executable, native in [('python', args.python, False), ('cpp', args.cpp, True)]:
        runs = [json.loads(subprocess.check_output([str(executable.absolute()), __file__, '--probe'], text=True, timeout=120).strip().splitlines()[-1]) for _ in range(3)]
        assert all(run == runs[0] for run in runs), 'Fresh processes disagree'
        assert runs[0]['identity']['native'] == native, 'Wrong interpreter artifact'
        assessments = {name: 'error' if 'error_type' in case else 'match' if case['dense_from_input_horizon'] == corpus['cases'][name]['expected_dense'] else 'divergence' for name, case in runs[0]['cases'].items()}
        record['engines'][engine] = {**runs[0], 'assessment': assessments}
        print(engine, assessments)
    assert sources == {name: support.sha(HERE / name) for name in sources}
    assert dependencies == {name: support.sha(HERE.parent / name) for name in dependencies}
    args.output.write_text(json.dumps(record, sort_keys=True, indent=2) + '\n')

if __name__ == '__main__':
    main()
