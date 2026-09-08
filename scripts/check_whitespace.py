#!/usr/bin/env python3
"""Reject trailing whitespace, missing final newlines, and CRLF in tracked text files.

Usage: python3 scripts/check_whitespace.py [ROOT]
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

TEXT_SUFFIXES = {".md", ".toml", ".yml", ".yaml", ".py", ".sh", ".json", ".html", ".css", ".txt"}


def tracked(root: Path) -> list[Path]:
    output = subprocess.run(
        ["git", "ls-files", "-z"], cwd=root, check=True, capture_output=True, text=True
    ).stdout
    return [root / name for name in output.split("\0") if name]


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    problems: list[str] = []
    for path in tracked(root):
        if path.suffix not in TEXT_SUFFIXES or not path.exists():
            continue
        data = path.read_bytes()
        if not data:
            continue
        rel = path.relative_to(root)
        if b"\r\n" in data:
            problems.append(f"{rel}: CRLF line endings")
        if not data.endswith(b"\n"):
            problems.append(f"{rel}: missing final newline")
        for number, line in enumerate(data.split(b"\n"), start=1):
            if line.rstrip(b"\r") != line.rstrip(b"\r").rstrip(b" \t"):
                problems.append(f"{rel}:{number}: trailing whitespace")
    for problem in problems:
        print(problem)
    if problems:
        print(f"whitespace: {len(problems)} problem(s)")
        return 1
    print("whitespace: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
