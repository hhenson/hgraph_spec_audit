"""Ordinary Python defaults, measured in an isolated public-reference interpreter."""
import importlib.util
import json
from pathlib import Path

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

def main():
    identity = support.identity()
    results = {}
    for name, source in CASES.items():
        namespace = {}
        try:
            exec(source, namespace)
            results[name] = namespace['result']
        except Exception as exc:
            results[name] = {'error_type': type(exc).__name__, 'message': str(exc)}
    assert identity == support.identity()
    print(json.dumps({'identity': identity, 'results': results}, sort_keys=True))

if __name__ == '__main__':
    main()
