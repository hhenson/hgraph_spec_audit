"""Read dense scalar assertions from the pinned HGL sources; execute no HGL code."""
import ast
from datetime import date, datetime, time, timedelta
import hashlib
from pathlib import Path
import re

TYPES = {'i64': int, 'f64': float, 'bool': bool, 'str': str,
         'date': date, 'datetime': datetime, 'time': time, 'duration': timedelta}


def split_nested(text):
    parts, start, depth, quoted, escaped = [], 0, 0, False, False
    for index, char in enumerate(text):
        if quoted:
            if escaped: escaped = False
            elif char == '\\': escaped = True
            elif char == '"': quoted = False
        elif char == '"': quoted = True
        elif char in '[(': depth += 1
        elif char in '])': depth -= 1
        elif char == ',' and depth == 0:
            parts.append(text[start:index].strip()); start = index + 1
    parts.append(text[start:].strip())
    return parts


def literal(text):
    text = text.strip()
    if text.startswith('['):
        return [literal(item) for item in split_nested(text[1:-1])] if text[1:-1].strip() else []
    if text == '_': return None
    if text in ('true', 'false'): return text == 'true'
    if text.startswith('@'):
        value = text[1:]
        return datetime.fromisoformat(value.removesuffix('Z')) if 'T' in value else time.fromisoformat(value) if ':' in value else date.fromisoformat(value)
    if re.fullmatch(r'\d+[a-z]+(?:\d+[a-z]+)*(?:\s*[+-]\s*\d+[a-z]+(?:\d+[a-z]+)*)*', text):
        factors = {'us': 1, 'ms': 1000, 's': 1000000, 'm': 60000000, 'h': 3600000000, 'd': 86400000000}
        total, sign = 0, 1
        for item in re.findall(r'[+-]|\d+[a-z]+', text):
            if item in ('+', '-'): sign = 1 if item == '+' else -1
            else:
                number, unit = re.fullmatch(r'(\d+)([a-z]+)', item).groups()
                total += sign * int(number) * factors[unit]
        return timedelta(microseconds=total)
    return ast.literal_eval(text)


def read(root):
    cases, hashes = [], {}
    for path in sorted(Path(root).rglob('*.hgl')):
        text = path.read_text()
        if 'assert eval(' not in text: continue
        relative = str(path.relative_to(root))
        hashes[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
        module = re.search(r'^module (\S+)', text, re.M)[1]
        signatures = {}
        for match in re.finditer(r'(?<!\w)fn (\w+)\(([^)]*)\)\s*->\s*(\w+)', text):
            params = []
            for part in split_nested(match[2]):
                name, ty = part.split(':', 1)
                ty, _, default = ty.partition('=')
                params.append((name.removeprefix('const ').strip(), ty.strip(), name.startswith('const '), literal(default) if default else None))
            signatures[match[1]] = (params, match[3])
        pattern = r'assert\s+eval\((.*?)\)\s*==\s*(\[(?:[^"\]]|"(?:[^"\\]|\\.)*")*\])'
        for match in re.finditer(pattern, text, re.S):
            pieces = split_nested(match[1]); function = pieces.pop(0)
            params, output = signatures[function]
            args = {}
            for index, item in enumerate(pieces):
                named = re.match(r'^(\w+)\s*:\s*(.*)$', item, re.S)
                name, value = (named[1], named[2]) if named else (params[index][0], item)
                args[name] = literal(value)
            for name, _, fixed, default in params:
                if fixed and name not in args: args[name] = default
            case = re.findall(r'\btest (\w+)\s*\{', text[:match.start()])[-1]
            cases.append(dict(module=module, function=function, name=case, parameters=params, output=output,
                              arguments=args, expected=literal(match[2]), source=relative))
    return cases, hashes


def encode(value):
    if isinstance(value, timedelta): return {'duration_us': (value.days*86400+value.seconds)*1000000+value.microseconds}
    if isinstance(value, (date, time, datetime)): return {type(value).__name__: value.isoformat()}
    raise TypeError(type(value).__name__)
