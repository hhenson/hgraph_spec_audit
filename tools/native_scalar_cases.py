"""Measure scalar operator traces against one independently installed engine."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / 'spec/compiler/native_scalar/cases.json'


def probe():
    import importlib.metadata
    import hgraph
    from hgraph.test import eval_node
    cases = json.loads(CORPUS.read_text())
    observations = {case['name']: eval_node(getattr(hgraph, case['operator']), case['lhs'], case['rhs']) for case in cases}
    binaries = [getattr(module, '__file__', '') for name, module in sys.modules.items() if name in ('_hgraph', 'hgraph._hgraph')]
    binary = next((Path(name) for name in binaries if name), None)
    return {'hgraph': importlib.metadata.version('hgraph'),
            'native_binary_sha256': hashlib.sha256(binary.read_bytes()).hexdigest() if binary else None,
            'observed': observations}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--probe', action='store_true')
    parser.add_argument('--engine', choices=('python', 'cpp'))
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.probe:
        print(json.dumps(probe()))
        return
    if not args.engine or not args.output or args.output.exists():
        parser.error('supply an engine and a new output path')
    runs = [json.loads(subprocess.check_output([sys.executable, __file__, '--probe'], text=True).splitlines()[-1])
            for _ in range(3)]
    report = runs[0]
    if any(run != report for run in runs):
        raise SystemExit('unstable repeated observations')
    prefix = '0.5.' if args.engine == 'python' else '0.8.'
    if not report['hgraph'].startswith(prefix) or bool(report['native_binary_sha256']) != (args.engine == 'cpp'):
        raise SystemExit('wrong reference engine')
    expected = {case['name']: case['expected'] for case in json.loads(CORPUS.read_text())}
    if report['observed'] != expected:
        raise SystemExit('observations differ from reasoned ticks: ' + json.dumps(report))
    report.update(engine=args.engine, repeats=3, measured_at=datetime.now(timezone.utc).isoformat(),
                  corpus_sha256=hashlib.sha256(CORPUS.read_bytes()).hexdigest(),
                  harness_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(f'{args.engine}: {len(expected)} cases match reasoning in three fresh processes')


if __name__ == '__main__':
    main()
