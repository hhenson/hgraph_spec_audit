"""Ordinary Python defaults, measured in an isolated public-reference interpreter."""
import importlib.util
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('support', HERE.parent / 'delta_eval/observe.py')
support = importlib.util.module_from_spec(spec)
spec.loader.exec_module(support)

CASES = {
    'enclosing_name': '''seed = 7
def choose(first, second=seed): return second
seed = 9
result = [choose(99), choose(99, 5)]
''',
    'earlier_parameter': '''def choose(first, second=first): return second
result = choose(99)
''',
    'shadow_parameter': '''first = 11
def choose(first, second=first): return second
result = choose(99)
''',
    'field_reference': '''from dataclasses import dataclass
@dataclass
class Pair:
    first: int = 7
    second: int = first
pair = Pair(99)
result = [pair.first, pair.second]
''',
    'evaluation_phase': '''count = 0
def bump():
    global count
    count += 1
    return count
def choose(value=bump()): return value
result = [choose(), choose(), count]
''',
}

def identity():
    # Hash the binary behind a venv symlink, retaining no private executable path.
    executable = Path(sys.executable).resolve()
    return {**support.identity(),
            'executable_sha256': hashlib.sha256(executable.read_bytes()).hexdigest()}

def main():
    before = identity()
    results = {}
    for name, source in CASES.items():
        namespace = {}
        try:
            exec(source, namespace)
            results[name] = namespace['result']
        except Exception as exc:
            results[name] = {'error_type': type(exc).__name__, 'message': str(exc)}
    assert before == identity()
    print(json.dumps({'identity': before, 'results': results}, sort_keys=True))

if __name__ == '__main__':
    main()
