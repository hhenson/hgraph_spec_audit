"""Compare the current source/sink contract with an installed hgraph runtime."""
import argparse
import hashlib
import importlib.metadata
import json
from pathlib import Path
import re
import subprocess
import sys

def evaluate(case):
    from datetime import timedelta
    from hgraph import TS, const, debug_print, graph
    from hgraph.test import eval_node

    @graph
    def source(value: int, delay: timedelta, sample: int) -> TS[int]:
        ts = const(value, delay=delay)
        debug_print('answer', ts, sample=sample)
        return ts

    @graph
    def sink(ts: TS[int], sample: int) -> TS[int]:
        debug_print('answer', ts, sample=sample)
        return ts

    if case['kind'] == 'source':
        ticks = eval_node(source, case['value'], timedelta(microseconds=case['delay_us']), case['sample'])
    else:
        ticks = eval_node(sink, case['input'], case['sample'])
    engine = 'cpp' if '_hgraph' in sys.modules else 'python'
    print('RESULT=' + json.dumps({'engine': engine, 'ticks': ticks}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cases', type=Path, required=True)
    parser.add_argument('--case', type=int)
    parser.add_argument('--engine', choices=['python', 'cpp'])
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    cases = json.loads(args.cases.read_text())
    if args.case is not None:
        evaluate(cases[args.case])
        return
    if args.engine is None or args.output is None:
        parser.error('--engine and --output are required')
    observed = {}
    for index, case in enumerate(cases):
        process = subprocess.run([sys.executable, __file__, '--cases', str(args.cases), '--case', str(index)], check=True, capture_output=True, text=True)
        result = re.search(r'^RESULT=(.*)$', process.stdout, re.MULTILINE)
        if result is None:
            raise RuntimeError(process.stdout + process.stderr)
        data = json.loads(result[1])
        if data.pop('engine') != args.engine:
            raise RuntimeError('wrong runtime loaded')
        data['lines'] = re.findall(r'(?:\[2\] )?answer: -?\d+', process.stdout)
        data['matches'] = data['ticks'] == case['ticks'] and data['lines'] == case['lines']
        observed[case['name']] = data
    import hgraph
    native = sys.modules.get('_hgraph')
    report = {
        'engine': args.engine,
        'package_version': importlib.metadata.version('hgraph'),
        'package_init_sha256': hashlib.sha256(Path(hgraph.__file__).read_bytes()).hexdigest(),
        'native_binary_sha256': hashlib.sha256(Path(native.__file__).read_bytes()).hexdigest() if native else None,
        'cases_sha256': hashlib.sha256(args.cases.read_bytes()).hexdigest(),
        'observed': observed,
    }
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    if not all(case['matches'] for case in observed.values()):
        raise SystemExit('reference mismatch')


if __name__ == '__main__':
    main()
