"""Check recorded evidence in a scratch copy; never rewrite archived results."""
from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CHECKS = ('runtime/validation/check.py', 'runtime/validation/fixed/check.py',
          'runtime/validation/descriptions/check.py', 'runtime/validation/wiring/check.py')


def main():
    with tempfile.TemporaryDirectory() as temporary:
        work = Path(temporary)
        shutil.copytree(ROOT / 'runtime', work / 'runtime', ignore=shutil.ignore_patterns('__pycache__'))
        for check in CHECKS:
            completed = subprocess.run([sys.executable, str(work / check)], capture_output=True, text=True)
            expected_exit = 1 if '/fixed/' in check else 0
            if completed.returncode != expected_exit:
                raise RuntimeError(f'{check}: unexpected exit {completed.returncode}\n{completed.stdout}\n{completed.stderr}')
            original = ROOT / Path(check).parent / 'assessment.json'
            generated = work / Path(check).parent / 'assessment.json'
            if json.loads(original.read_text()) != json.loads(generated.read_text()):
                raise RuntimeError(f'{check}: recorded assessment changed')
            print(check + ': recorded assessment reproduced')
        for folder in ('runtime/validation/descriptions',):
            subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', str(work / folder)], check=True)
    print('Recorded evidence checked; no fresh runtime measurements were made.')


if __name__ == '__main__':
    main()
