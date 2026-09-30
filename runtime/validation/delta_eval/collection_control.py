"""Observe actual downstream empty-set events independently of recording."""
import argparse
import contextlib
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import subprocess
from observe import encode, identity, sha

HERE = Path(__file__).resolve().parent
CORPUS = HERE / 'collection_control_reasoned.json'

def probe():
    from hgraph import TS, TSS, OUT, compute_node, graph, sink_node
    from hgraph.test import eval_node
    downstream = []
    @compute_node
    def cancel(step: TS[int], _output: OUT = None) -> TSS[int]:
        _output.add(1)
        _output.remove(1)
    @compute_node
    def forward(ts: TSS[int]) -> TSS[int]:
        return ts.delta_value
    @sink_node
    def watch(ts: TSS[int]):
        downstream.append({'valid': ts.valid, 'modified': ts.modified,
                           'delta': encode(ts.delta_value)})
    @graph
    def target(step: TS[int]) -> TSS[int]:
        out = forward(cancel(step))
        watch(out)
        return out
    before = identity()
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        raw = encode(eval_node(target, [1, 2, None]))
    if before != identity():
        raise RuntimeError('engine identity changed')
    return {'identity_sha256': before['package']['identity_sha256'],
            'native': before['native'], 'raw': raw, 'downstream': downstream}

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
    expected = json.loads(CORPUS.read_text())['expected_downstream']
    evidence = {'measured_at': datetime.now(timezone.utc).isoformat(),
                'reasoned_sha256': corpus_hash, 'harness_sha256': sha(__file__),
                'repeats': 3, 'engines': {}}
    for name, executable, native in [('python', args.python, False), ('cpp', args.cpp, True)]:
        runs = [json.loads(subprocess.check_output([str(executable.absolute()), __file__, '--probe'],
                        text=True).strip().splitlines()[-1]) for _ in range(3)]
        if any(run != runs[0] for run in runs) or runs[0]['native'] != native:
            raise RuntimeError(name + ': unstable observations or incorrect engine')
        result = runs[0]
        result['assessment'] = 'match' if result['downstream'] == expected else 'divergence'
        evidence['engines'][name] = result
    if sha(CORPUS) != corpus_hash:
        raise RuntimeError('expectations changed during observation')
    args.output.write_text(json.dumps(evidence, sort_keys=True, indent=2) + '\n')
    for name, result in evidence['engines'].items():
        print(name, result['assessment'], result['downstream'])

if __name__ == '__main__':
    main()
