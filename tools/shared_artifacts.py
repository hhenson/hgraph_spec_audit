"""Materialize pinned shared sources at compatibility paths. Standard library only."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def inside(root: Path, name: str) -> Path:
    path = (root / name).resolve()
    if Path(name).is_absolute() or not path.is_relative_to(root.resolve()) or path == root.resolve():
        raise ValueError(f"path escapes repository: {name}")
    return path


def materialize(root: Path, check: bool = False) -> int:
    root = root.resolve()
    manifest = json.loads((root / 'shared-artifacts.json').read_text())
    state_path = root / '.shared-artifacts-state.json'
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    pending, next_state = [], {}
    # Validate the entire operation before modifying any file.
    for target, source in sorted(manifest['files'].items()):
        destination = inside(root, target)
        owner = inside(root, manifest['repositories'][source['repository']])
        origin = inside(owner, source['path'])
        data = origin.read_bytes()
        expected = digest(data)
        actual = digest(destination.read_bytes()) if destination.exists() else None
        if check and actual != expected:
            raise ValueError(f"missing or stale shared file: {target}")
        if actual not in (None, expected, state.get(target)):
            raise ValueError(f"edited shared file: {target}; move edits to {source['repository']}/{source['path']} first")
        if actual != expected:
            pending.append((destination, data))
        next_state[target] = expected
    retired = []
    for target, previous in state.items():
        if target not in next_state:
            destination = inside(root, target)
            if destination.exists():
                if digest(destination.read_bytes()) != previous:
                    raise ValueError(f"edited retired shared file: {target}")
                if check:
                    raise ValueError(f"retired shared file still present: {target}")
                retired.append(destination)
    if not check:
        for destination, data in pending:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
        for destination in retired:
            destination.unlink()
        state_path.write_text(json.dumps(next_state, indent=2, sort_keys=True) + '\n')
    return len(next_state)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--offline', action='store_true', help='use already initialized submodules')
    args = parser.parse_args()
    try:
        if not args.offline and not args.check:
            subprocess.run(['git', 'submodule', 'update', '--init', '--recursive'], cwd=args.root, check=True)
        print(f"{materialize(args.root, args.check)} shared files {'verified' if args.check else 'materialized'}")
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, f'{error}\n')


if __name__ == '__main__':
    main()
