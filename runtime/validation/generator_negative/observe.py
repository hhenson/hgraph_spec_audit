"""Measure relative-negative admission separately from operands and absolute past times."""
import argparse
import contextlib
from datetime import datetime, timedelta, timezone
import io
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import encode, identity, sha


def probe(case):
    import hgraph as hg
    from hgraph.test import eval_node
    before = identity()
    trace, received = [], []

    def mark_time(label, value):
        trace.append(label)
        if label == 'time':
            if case.get('time_failure'):
                raise RuntimeError('negative-time-operand-sentinel')
            if case['time_kind'] == 'expression_underflow':
                return datetime.min - hg.MIN_TD
        return value

    def mark_payload(label, value):
        trace.append(label)
        if label == 'value' and case.get('payload_failure'):
            raise RuntimeError('negative-payload-operand-sentinel')
        return value

    def body():
        if case['later']:
            yield mark_time('prelude_time', 2 * hg.MIN_TD), mark_payload('prelude_value', 10)
            trace.append('after_prelude')
        time = {'negative': -hg.MIN_TD, 'large_negative': timedelta(days=-1000000),
                'expression_underflow': None, 'zero': timedelta(),
                'past_absolute': hg.MIN_ST + (hg.MIN_TD if case['later'] else -hg.MIN_TD)}[case['time_kind']]
        yield mark_time('time', time), mark_payload('value', 1)
        trace.append('after')
        yield mark_time('time2', hg.MIN_TD), mark_payload('value2', 2)
        trace.append('after2')
    body.__annotations__ = {'return': hg.TS[int]}
    source = hg.generator(body)

    def capture(ts):
        received.append(encode(ts.delta_value))
        return ts.delta_value
    capture.__annotations__ = {'ts': hg.TS[int], 'return': hg.TS[int]}
    compute = hg.compute_node(capture)

    def composition():
        return compute(source())
    composition.__annotations__ = {'return': hg.TS[int]}
    result = {'trace': trace, 'downstream_payloads': received}
    try:
        result.update(raw=encode(eval_node(hg.graph(composition))), fails=False)
    except Exception as exc:
        result.update(fails=True, error_type=type(exc).__name__,
                      error_message=str(exc).replace(str(HERE.parents[2]), '<audit-root>')
                          .replace(sys.prefix, '<environment>').replace(str(Path.home()), '<private-home>'))
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
            result = probe(cases[args.probe])
        print(json.dumps(result, sort_keys=True))
        return
    if not args.python or not args.cpp or not args.output or args.output.exists():
        parser.error('independent interpreters and new output required')
    evidence = {'measured_at': datetime.now(timezone.utc).isoformat(), 'repeats': 3,
                'reasoned_sha256': corpus_hash, 'harness_sha256': sha(__file__),
                'identity_helper_sha256': sha(HERE.parent / 'delta_eval/observe.py'), 'engines': {}}
    for engine, executable in [('python', args.python), ('cpp', args.cpp)]:
        observations, engine_identity = {}, None
        for name in cases:
            runs = [json.loads(subprocess.check_output([str(executable), __file__, '--probe', name],
                                                     text=True, timeout=30)) for _ in range(3)]
            assert all(run == runs[0] for run in runs), (engine, name, 'unstable')
            current = runs[0]
            assert current['identity']['native'] == (engine == 'cpp')
            assert engine_identity is None or engine_identity == current['identity']
            engine_identity = current['identity']
            observations[name] = current['observation']
            print(engine, name, current['observation'], flush=True)
        evidence['engines'][engine] = {'identity': engine_identity, 'observations': observations}
    assert sha(corpus) == corpus_hash, 'prewritten expectations changed'
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')


if __name__ == '__main__':
    main()
