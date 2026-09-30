"""Validate frozen empty-event and recursive-delta cases with genuine engines."""
import argparse
import contextlib
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import subprocess
from observe import encode, identity, sha

HERE = Path(__file__).resolve().parent
CORPUS = HERE / 'collection_reasoned.json'


def observe(case):
    from hgraph import TS, TSS, TSD, OUT, compute_node, graph, set_delta
    from hgraph.test import eval_node
    producer = []
    received = []
    kind = case['id']
    schema = TSD[int, TSD[int, TS[int]]] if kind == 'N0' else TSS[int]

    def forward(ts):
        received.append({'valid': ts.valid, 'modified': ts.modified,
                         'delta': encode(ts.delta_value), 'value': encode(ts.value)})
        return ts.delta_value
    forward.__annotations__ = {'ts': schema, 'return': schema}
    pass_through = compute_node(forward)
    if kind == 'E1':
        @compute_node
        def cancel(step: TS[int], _output: OUT = None) -> TSS[int]:
            _output.add(1)
            _output.remove(1)
            producer.append({'step': step.value, 'valid': _output.valid,
                             'modified': _output.modified, 'delta': encode(_output.delta_value)})
        @graph
        def target(step: TS[int]) -> TSS[int]:
            return pass_through(cancel(step))
        samples = case['inputs']
    elif kind == 'E0':
        target = pass_through
        samples = [None if v is None else set_delta(set(v['added']), set(v['removed']))
                   for v in case['inputs']]
    else:
        target = pass_through
        samples = [None if v is None else {int(k): {int(c): value for c, value in child.items()}
                                          for k, child in v.items()} for v in case['inputs']]
    try:
        raw = encode(eval_node(target, samples))
        dense = [] if raw is None else list(raw)
        dense += [None] * max(0, len(samples) - len(dense))
        return {'raw': raw, 'input_horizon': len(samples), 'dense': dense,
                'producer': producer, 'received': received}
    except Exception as exc:
        # Keep partial endpoint observations if wiring/execution fails.
        message = str(exc).replace(str(Path.home()), '<private-path>')
        return {'error_type': type(exc).__name__, 'error': message,
                'producer': producer, 'received': received}


def probe():
    before = identity()
    observations = {}
    for case in json.loads(CORPUS.read_text())['cases']:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            observations[case['id']] = observe(case)
    if before != identity():
        raise RuntimeError('engine identity changed during observation')
    return {'identity': before, 'observations': observations}


def assessment(case, observed):
    result = {'output': 'error' if 'error_type' in observed else
              'match' if observed['dense'] == case['expected'] else 'divergence'}
    if 'expected_producer' in case:
        result['producer'] = 'match' if observed['producer'] == case['expected_producer'] else 'divergence'
    if 'expected_values' in case:
        result['held_values'] = 'match' if [x['value'] for x in observed['received']] == case['expected_values'] else 'divergence'
    return result


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
        parser.error('independent interpreters and a new output are required')
    corpus_hash = sha(CORPUS)
    cases = json.loads(CORPUS.read_text())['cases']
    evidence = {'measured_at': datetime.now(timezone.utc).isoformat(),
                'reasoned_sha256': corpus_hash, 'harness_sha256': sha(__file__),
                'repeats': 3, 'engines': {}}
    for name, executable, native in [('python', args.python, False), ('cpp', args.cpp, True)]:
        runs = [json.loads(subprocess.check_output([str(executable.absolute()), __file__, '--probe'],
                        text=True).strip().splitlines()[-1]) for _ in range(3)]
        if any(run != runs[0] for run in runs) or runs[0]['identity']['native'] != native:
            raise RuntimeError(name + ': unstable observations or incorrect engine')
        result = runs[0]
        result['assessment'] = {case['id']: assessment(case, result['observations'][case['id']])
                                for case in cases}
        evidence['engines'][name] = result
    if sha(CORPUS) != corpus_hash:
        raise RuntimeError('expectations changed during observation')
    args.output.write_text(json.dumps(evidence, sort_keys=True, indent=2) + '\n')
    for name, result in evidence['engines'].items():
        print(name, result['assessment'])


if __name__ == '__main__':
    main()
