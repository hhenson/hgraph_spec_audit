"""Measure the wiring contract against independently installed reference engines."""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reference', required=True, type=Path)
    parser.add_argument('--candidate', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--repeats', type=int, default=3)
    args = parser.parse_args()
    if args.repeats < 2:
        parser.error('at least two fresh-process repeats are required')
    identity_probe = (
        "import json, sys, importlib.metadata; import hgraph; "
        "print(json.dumps({'hgraph': importlib.metadata.version('hgraph'), "
        "'native': hasattr(hgraph, '_hgraph') or 'hgraph._hgraph' in sys.modules or '_hgraph' in sys.modules}))"
    )
    identities = {}
    for name, executable, family, native in (
        ('python', args.reference, '0.5.', False), ('cpp', args.candidate, '0.8.', True)
    ):
        identity = json.loads(subprocess.check_output([str(executable.absolute()), '-c', identity_probe], text=True).strip().splitlines()[-1])
        if not identity['hgraph'].startswith(family) or identity['native'] != native:
            parser.error(f'{name}: expected hgraph {family}x, native={native}; got {identity}')
        identities[name] = identity
    output = args.output.resolve()
    if output.exists():
        parser.error('output already exists; choose a new directory to preserve prior evidence')
    wiring = output / 'runtime/validation/wiring'
    shutil.copytree(ROOT / 'runtime/validation/wiring', wiring, ignore=shutil.ignore_patterns('__pycache__'))
    for chapter in ('wiring.md', 'time_series.md'):
        shutil.copy2(ROOT / 'runtime' / chapter, output / 'runtime' / chapter)
    # Front-end evidence remains explicitly historical. This run measures runtimes only.
    subprocess.run([str(args.reference.absolute()), str(wiring / 'observe.py'), '--reference', str(args.reference.absolute()),
                    '--candidate', str(args.candidate.absolute()), '--candidate-revision',
                    'release:' + identities['cpp']['hgraph'], '--repeats', str(args.repeats)], check=True)
    subprocess.run([sys.executable, str(wiring / 'check.py')], check=True)
    provenance = {'measured_at': datetime.now(timezone.utc).isoformat(), 'runtimes': identities,
                  'repeats': args.repeats, 'scope': 'wiring runtime observations; HGL front-end evidence is historical',
                  'reasoned_sha256': hashlib.sha256((wiring / 'reasoned.json').read_bytes()).hexdigest()}
    (output / 'provenance.json').write_text(json.dumps(provenance, indent=2) + '\n')
    print(f'Evidence written to {output}')


if __name__ == '__main__':
    main()
