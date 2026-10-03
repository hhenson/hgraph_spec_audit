"""Observe prewritten generator operand traces without changing failing outcomes."""
import argparse
import contextlib
from datetime import timedelta, datetime, timezone
import io
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'delta_eval'))
from observe import encode, identity, sha
from assessment import assess


def observe(name):
    import hgraph as hg
    from hgraph.test import eval_node
    trace = []

    def marked_time(label, value):
        trace.append(label)
        if name == 'time_failure':
            raise RuntimeError('operand-audit-sentinel')
        return value

    def marked_value(label, value):
        trace.append(label)
        if name == 'past_payload_failure':
            raise RuntimeError('operand-audit-sentinel')
        return value

    def body():
        first = (hg.MIN_ST - hg.MIN_TD if name in {'past_absolute', 'past_payload_failure', 'time_failure'} else
                 -hg.MIN_TD if name == 'negative_duration' else
                 2 * hg.MIN_TD if name == 'future_resume' else timedelta())
        yield marked_time('time1', first), marked_value('value1', 1)
        trace.append('after1')
        second = hg.MIN_ST + 2 * hg.MIN_TD if name == 'past_absolute' else hg.MIN_TD if name == 'future_resume' else timedelta()
        yield marked_time('time2', second), marked_value('value2', 2)
        trace.append('after2')
    body.__annotations__ = {'return': hg.TS[int]}
    try:
        raw = encode(eval_node(hg.generator(body)))
        return {'trace': trace, 'raw': raw, 'fails': False}
    except Exception as exc:
        return {'trace': trace, 'fails': True, 'error_type': type(exc).__name__,
                'sentinel': 'operand-audit-sentinel' in str(exc),
                # Preserve exception text; only replace private filesystem prefixes.
                'error_message': str(exc).replace(str(HERE.parents[2]), '<audit-root>')
                    .replace(sys.prefix, '<environment>').replace(str(Path.home()), '<private-home>')}


def probe():
    before = identity()
    results = {}
    for name in json.loads((HERE / 'reasoned.json').read_text())['cases']:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            results[name] = observe(name)
    if before != identity():
        raise RuntimeError('engine changed during observation')
    return {'identity': before, 'observations': results}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--probe', action='store_true')
    p.add_argument('--python', type=Path)
    p.add_argument('--cpp', type=Path)
    p.add_argument('--output', type=Path)
    args = p.parse_args()
    if args.probe:
        print(json.dumps(probe(), sort_keys=True))
        return
    if not args.python or not args.cpp or not args.output or args.output.exists():
        p.error('independent interpreters and new output required')
    corpus = HERE / 'reasoned.json'
    corpus_hash = sha(corpus)
    cases = json.loads(corpus.read_text())['cases']
    contract_path = HERE / 'error_contract.json'
    contract_hash = sha(contract_path)
    contract = json.loads(contract_path.read_text())
    evidence = {'measured_at': datetime.now(timezone.utc).isoformat(),
                'reasoned_sha256': corpus_hash, 'harness_sha256': sha(__file__),
                'identity_helper_sha256': sha(HERE.parent / 'delta_eval/observe.py'),
                'error_contract_sha256': contract_hash, 'assessment_sha256': sha(HERE / 'assessment.py'),
                'repeats': 3, 'engines': {}}
    for name, executable, native in [('python', args.python, False), ('cpp', args.cpp, True)]:
        runs = [json.loads(subprocess.check_output([str(executable), __file__, '--probe'], text=True)) for _ in range(3)]
        if any(run != runs[0] for run in runs) or runs[0]['identity']['native'] != native:
            raise RuntimeError('unstable or incorrect engine: ' + name)
        result = runs[0]
        result['assessment'] = assess(result['observations'], cases, name, contract)
        evidence['engines'][name] = result
        print(name, result['assessment'])
    if sha(corpus) != corpus_hash or sha(contract_path) != contract_hash:
        raise RuntimeError('expectations changed')
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + '\n')

if __name__ == '__main__':
    main()
