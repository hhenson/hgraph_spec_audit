"""Observe tuple expressions on independent Python and native hgraph packages."""
import argparse
import contextlib
import copy
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import identity, encode, sha


def probe():
    import hgraph as hg
    from hgraph.test import eval_node
    before = identity()
    trace = []

    def mark(value):
        trace.append(value)
        return value

    def fail(value):
        trace.append(value)
        raise ValueError('tuple element failed')

    value = (mark(2), mark(1))
    observed = {'written_order': {'trace': list(trace), 'value': encode(value)}}
    trace.clear()
    try:
        value = (fail(2), mark(1))
        observed['first_failure'] = {'trace': list(trace), 'constructed': True}
    except ValueError as exc:
        observed['first_failure'] = {'trace': list(trace), 'constructed': False,
                                     'error_type': type(exc).__name__}
    trace.clear()
    value = ((mark(2), mark(1)), mark(3))
    observed['nested_order'] = {'trace': list(trace), 'value': encode(value)}
    source = [7]
    alias = (source, source)
    owned = (copy.deepcopy(source), copy.deepcopy(source))
    source.append(9)
    observed['ordinary_python_alias'] = encode(alias)
    observed['explicit_owned_copy'] = encode(owned)

    try:
        @hg.compute_node
        def runtime_pair(value: hg.TS[int]) -> hg.TS[tuple[int, bool]]:
            return (value.value, value.value > 0)
        observed['runtime_pair'] = {'status': 'observed', 'value': encode(
            eval_node(runtime_pair, [7, None, -1, 0]))}
    except Exception as exc:
        observed['runtime_pair'] = {'status': 'error', 'error_type': type(exc).__name__,
                                   'message': str(exc).replace(str(Path.home()), '<private-home>')}
    if before != identity():
        raise RuntimeError('engine artifacts changed during observation')
    return {'identity': before, 'observed': observed}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--probe', action='store_true')
    parser.add_argument('--python', type=Path)
    parser.add_argument('--cpp', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.probe:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            result = probe()
        print(json.dumps(result, sort_keys=True))
        return
    if not args.python or not args.cpp or not args.output or args.output.exists():
        parser.error('supply independent interpreters and a new output destination')
    corpus = HERE / 'reasoned.json'
    corpus_hash = sha(corpus)
    expected = json.loads(corpus.read_text())['expected']
    evidence = {'measured_at': datetime.now(timezone.utc).isoformat(), 'repeats': 3,
                'reasoned_sha256': corpus_hash, 'harness_sha256': sha(__file__),
                'identity_helper_sha256': sha(HERE.parent / 'delta_eval/observe.py'), 'engines': {}}
    for name, exe in [('python', args.python), ('cpp', args.cpp)]:
        runs = [json.loads(subprocess.check_output(
            [str(exe.absolute()), __file__, '--probe'], text=True, timeout=120).strip().splitlines()[-1])
                for _ in range(3)]
        if any(run != runs[0] for run in runs):
            raise RuntimeError(name + ' fresh-process observations are unstable')
        result = runs[0]
        if result['identity']['native'] != (name == 'cpp'):
            raise RuntimeError(name + ' has wrong engine identity')
        result['assessment'] = {key: 'match' if result['observed'][key] == value else 'divergence'
                                for key, value in expected.items()}
        evidence['engines'][name] = result
    if sha(corpus) != corpus_hash:
        raise RuntimeError('expectations changed during measurement')
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')
    for name, result in evidence['engines'].items():
        print(name, result['assessment'])


if __name__ == '__main__':
    main()
