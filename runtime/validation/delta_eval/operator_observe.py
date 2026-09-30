"""Measure prewritten multi-input, isolated-run and outputless eval cases."""
import argparse
import contextlib
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import subprocess
import sys
from observe import identity, encode, sha

HERE = Path(__file__).resolve().parent
CORPUS = HERE / 'operator_reasoned.json'

def probe():
    from hgraph import TS, compute_node, sink_node
    from hgraph.test import eval_node
    @compute_node
    def add(lhs: TS[int], rhs: TS[int]) -> TS[int]:
        return lhs.value + rhs.value
    @compute_node
    def sample(value: TS[str], trigger: TS[bool]) -> TS[str]:
        if trigger.modified:
            return value.value
    @compute_node
    def text(ts: TS[str]) -> TS[str]:
        return ts.delta_value
    @sink_node
    def sink(ts: TS[int]):
        pass
    nodes = {'sum': add, 'sample': sample, 'text': text, 'sink': sink}
    before = identity()
    observations = {}
    for case in json.loads(CORPUS.read_text())['cases']:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            raw = encode(eval_node(nodes[case['node']], *case['inputs']))
        horizon = max(map(len, case['inputs']), default=0)
        if case['node'] == 'sink':
            dense = None
        else:
            dense = [] if raw is None else list(raw)
            dense += [None] * max(0, horizon - len(dense))
        observations[case['id']] = {'raw': raw, 'input_horizon': horizon, 'dense': dense,
                                    'outputless': case['node'] == 'sink'}
    if before != identity():
        raise RuntimeError('engine identity changed during observation')
    return {'identity_sha256': before['package']['identity_sha256'],
            'native': before['native'], 'observations': observations}

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
        if any(run != runs[0] for run in runs) or runs[0]['native'] != native:
            raise RuntimeError(name + ': unstable observations or incorrect engine')
        result = runs[0]
        result['assessment'] = {case['id']: 'match' if
            result['observations'][case['id']]['dense'] == case['expected'] else 'divergence'
            for case in cases}
        evidence['engines'][name] = result
    if sha(CORPUS) != corpus_hash:
        raise RuntimeError('expectations changed during observation')
    args.output.write_text(json.dumps(evidence, sort_keys=True, indent=2) + '\n')
    for name, result in evidence['engines'].items():
        print(name, result['assessment'])

if __name__ == '__main__':
    main()
