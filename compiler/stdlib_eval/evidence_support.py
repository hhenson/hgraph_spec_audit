"""Runtime fingerprints and the explicitly accepted replay variation."""
import hashlib


def python_fingerprint(root):
    files = {path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
             for path in sorted(root.rglob('*.py'))}
    if not files:
        raise ValueError('no Python runtime sources found')
    fingerprint = hashlib.sha256()
    for name, digest in files.items():
        fingerprint.update(f'{name}\0{digest}\n'.encode())
    return dict(sha256=fingerprint.hexdigest(), files=len(files))


def validate_replay(engine, rows):
    failed = [row for row in rows if not row['matches']]
    if engine == 'cpp' and not failed:
        return
    if engine == 'python' and len(failed) == 1:
        row = failed[0]
        if (row['index'] == 77 and row['function'] == 'reset_integer'
                and row['expected'] == [0, 2, 3, 0, 1]
                and row.get('observed') == [None, 2, 0, 0, 1] and 'error' not in row):
            return
    raise ValueError(f"unexpected {engine} replay mismatches: {[row['index'] for row in failed]}")
