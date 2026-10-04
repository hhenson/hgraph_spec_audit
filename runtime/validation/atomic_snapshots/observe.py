"""Observe complete atomic snapshots and retention without repairing reference aliases."""
import argparse
import contextlib
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta, timezone
import io
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import encode, identity, sha


def probe(name):
    import hgraph as hg
    from hgraph.test import eval_node

    @dataclass(frozen=True)
    class Quote(hg.CompoundScalar):
        bid: int
        ask: int = 7

    @dataclass(frozen=True)
    class Record(hg.CompoundScalar):
        count: int
        values: list[int]

    def snapshot(value):
        if isinstance(value, Quote):
            return {'bid': value.bid, 'ask': value.ask}
        if isinstance(value, Record):
            return {'count': value.count, 'values': snapshot(value.values)}
        if isinstance(value, (tuple, list)):
            return [snapshot(v) for v in value]
        return encode(value)

    values = (False, 0, 0.0, '', date(2026, 1, 2), time(3, 4, 5),
              datetime(2026, 1, 2, 3, 4, 5), timedelta(microseconds=-3))
    shared = [1, 2]
    cases = {
        'tuple_eight_scalars': (tuple[bool, int, float, str, date, time, datetime, timedelta], [values, None, values]),
        'tuple_nested_list': (tuple[list[int], int], [([1, 2], 4), None, ([3], 5)]),
        'list_i64': (list[int], [[1, 2], None, [3], [], []]),
        'list_nested': (list[list[int]], [[[1], [2]], None, [[3]], [], []]),
        'list_shared_captures': (list[int], [shared, None, shared]),
        'required_nominal': (Record, [Record(1, [10, 11]), None, Record(2, [20])]),
        'defaulted_nominal': (Quote, [Quote(1), None, Quote(2, 9), Quote(2, 9)]),
        'list_nominal': (list[Quote], [[Quote(1), Quote(2)], None, [Quote(3, 8)], []]),
    }
    scalar, inputs = cases[name]

    def mutate(value, marker):
        if name == 'tuple_nested_list':
            value[0].append(marker)
        elif name == 'list_nested':
            value[0].append(marker)
        elif name == 'required_nominal':
            value.values.append(marker)
        elif name == 'list_nominal':
            value.append(Quote(marker))
        elif name in {'list_i64', 'list_shared_captures'}:
            value.append(marker)
        else:
            return False
        return True

    before = identity()
    received = []
    original = snapshot(inputs)

    def forward(value):
        received.append({'value': snapshot(value.value), 'delta': snapshot(value.delta_value)})
        return value.delta_value
    forward.__annotations__ = {'value': hg.TS[scalar], 'return': hg.TS[scalar]}
    node = hg.compute_node(forward)
    result = {'inputs_before': original}
    try:
        raw = eval_node(node, inputs)
        result.update(raw_after_eval=snapshot(raw), received=received.copy())
        result['source_mutated'] = mutate(inputs[0], 999)
        result['inputs_after_mutation'] = snapshot(inputs)
        result['raw_after_source_mutation'] = snapshot(raw)
        second = eval_node(node, inputs)
        result['second_raw'] = snapshot(second)
        result['raw_after_second_eval'] = snapshot(raw)
        result['capture_mutated'] = mutate(raw[0], 888)
        result['raw_after_capture_mutation'] = snapshot(raw)
        result['second_raw_after_capture_mutation'] = snapshot(second)
    except Exception as exc:
        result['error_type'] = type(exc).__name__
        result['error_message'] = str(exc).replace(str(HERE.parents[2]), '<audit-root>')\
            .replace(sys.prefix, '<environment>').replace(str(Path.home()), '<private-home>')
    assert before == identity(), 'engine identity changed'
    return {'identity': before, 'observation': result}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--probe')
    parser.add_argument('--python', type=Path)
    parser.add_argument('--cpp', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    corpus = HERE / 'reasoned.json'
    corpus_hash = sha(corpus)
    cases = json.loads(corpus.read_text())['cases']
    if args.probe:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            result = probe(args.probe)
        print(json.dumps(result, sort_keys=True))
        return
    if not args.python or not args.cpp or not args.output or args.output.exists():
        parser.error('independent interpreters and a new output path required')
    evidence = {'measured_at': datetime.now(timezone.utc).isoformat(), 'repeats': 3,
                'reasoned_sha256': corpus_hash, 'harness_sha256': sha(__file__),
                'identity_helper_sha256': sha(HERE.parent / 'delta_eval/observe.py'), 'engines': {}}
    for engine, executable in [('python', args.python), ('cpp', args.cpp)]:
        observations, engine_identity = {}, None
        for name in cases:
            runs = [json.loads(subprocess.check_output([str(executable), __file__, '--probe', name], text=True, timeout=30))
                    for _ in range(3)]
            assert all(run == runs[0] for run in runs), (engine, name, 'unstable')
            current = runs[0]
            assert current['identity']['native'] == (engine == 'cpp')
            assert engine_identity is None or engine_identity == current['identity']
            engine_identity = current['identity']
            observations[name] = current['observation']
            print(engine, name, current['observation'], flush=True)
        evidence['engines'][engine] = {'identity': engine_identity, 'observations': observations}
    assert sha(corpus) == corpus_hash
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')


if __name__ == '__main__':
    main()
