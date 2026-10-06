"""Check recorded evidence in a scratch copy; never rewrite archived results."""
from pathlib import Path
import json
import hashlib
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CHECKS = ('runtime/validation/check.py', 'runtime/validation/fixed/check.py',
          'runtime/validation/fixed/native_nested.py', 'runtime/validation/parity/check.py', 'runtime/validation/descriptions/check.py', 'runtime/validation/wiring/check.py')


def main():
    with tempfile.TemporaryDirectory() as temporary:
        work = Path(temporary)
        shutil.copytree(ROOT / 'runtime', work / 'runtime', ignore=shutil.ignore_patterns('__pycache__'))
        for check in CHECKS:
            completed = subprocess.run([sys.executable, str(work / check)], capture_output=True, text=True)
            expected_exit = 1 if check == 'runtime/validation/fixed/check.py' else 0
            if completed.returncode != expected_exit:
                raise RuntimeError(f'{check}: unexpected exit {completed.returncode}\n{completed.stdout}\n{completed.stderr}')
            report = 'native_nested_assessment.json' if check.endswith('native_nested.py') else 'assessment.json'
            original = ROOT / Path(check).parent / report
            generated = work / Path(check).parent / report
            if json.loads(original.read_text()) != json.loads(generated.read_text()):
                raise RuntimeError(f'{check}: recorded assessment changed')
            print(check + ': recorded assessment reproduced')
        released = ROOT / 'results/releases-0.5.42-0.8.30'
        wiring = work / 'runtime/validation/wiring'
        provenance = json.loads((released / 'provenance.json').read_text())
        if hashlib.sha256((released / 'reasoned.json').read_bytes()).hexdigest() != provenance['reasoned_sha256']:
            raise RuntimeError('released wiring expectations changed')
        shutil.copy2(released / 'reasoned.json', wiring / 'reasoned.json')
        shutil.copy2(released / 'observed.json', wiring / 'observed.json')
        subprocess.run([sys.executable, str(wiring / 'check.py')], check=True, capture_output=True)
        if json.loads((wiring / 'assessment.json').read_text()) != json.loads((released / 'assessment.json').read_text()):
            raise RuntimeError('released wiring assessment changed')
        print('released wiring assessment reproduced')
        for folder in ('runtime/validation/descriptions', 'runtime/validation/fixed'):
            subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', str(work / folder)], check=True)
    for folder in ('compiler/stdlib', 'compiler/stdlib_eval', 'compiler/negative_testing',
                   'runtime/validation/eval_timed_values', 'runtime/validation/generator_operands',
                   'runtime/validation/owned_deltas', 'runtime/validation/publication_boundaries', 'runtime/validation/recorder_keys',
                   'runtime/validation/generator_negative', 'runtime/validation/generator_ordering',
                   'runtime/validation/atomic_snapshots', 'runtime/validation/temporal_scalars', 'runtime/validation/strict_zone_names', 'runtime/validation/zoned_time', 'runtime/validation/enum_publications', 'runtime/validation/scalar_collection_keys', 'runtime/validation/atomic_set_map', 'runtime/validation/growing_list', 'runtime/validation/rolling_publications', 'runtime/validation/optional_atomic', 'runtime/validation/recursive_atomic', 'runtime/validation/abstract_atomic', 'runtime/validation/composite_keys'):
        subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', str(ROOT / folder)], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/delta_eval/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'compiler/native_interfaces/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'compiler/contextual_bindings/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/value_sequences/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/constructor_order/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/eval_timed_values/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/generator_operands/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/owned_deltas/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/publication_boundaries/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/recorder_keys/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/generator_negative/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/generator_ordering/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/atomic_snapshots/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/temporal_scalars/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/strict_zone_names/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/zoned_time/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/enum_publications/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/scalar_collection_keys/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/atomic_set_map/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/growing_list/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/rolling_publications/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/optional_atomic/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/recursive_atomic/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/abstract_atomic/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'runtime/validation/composite_keys/check.py')], check=True)
    subprocess.run([sys.executable, str(ROOT / 'compiler/negative_testing/check.py')], check=True)
    print('Recorded evidence checked; no fresh runtime measurements were made.')


if __name__ == '__main__':
    main()
