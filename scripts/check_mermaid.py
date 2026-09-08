#!/usr/bin/env python3
"""Render every Mermaid block in the repository's Markdown to prove it parses.

Usage: python3 scripts/check_mermaid.py [ROOT]

Optional check: requires the Mermaid CLI (`mmdc`) on PATH or MMDC set to its
path, plus a Chromium that Puppeteer can launch (PUPPETEER_EXECUTABLE_PATH).
It is not part of the required manifest because CI has no browser; run it
locally before committing a diagram.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

SKIP_DIRS = {".git", ".venv", "node_modules", "target", ".worktrees", ".superpowers"}
BLOCK = re.compile(r"```mermaid\n(.*?)\n```", re.S)


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    mmdc = os.environ.get("MMDC", "mmdc")
    problems: list[str] = []
    count = 0
    with tempfile.TemporaryDirectory() as tmp:
        config = Path(tmp) / "puppeteer.json"
        executable = os.environ.get("PUPPETEER_EXECUTABLE_PATH")
        config.write_text(
            '{"args":["--no-sandbox"]'
            + (f', "executablePath":"{executable}"' if executable else "")
            + "}\n"
        )
        for path in sorted(root.rglob("*.md")):
            if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
                continue
            text = path.read_text(encoding="utf-8")
            for index, match in enumerate(BLOCK.finditer(text), start=1):
                count += 1
                source = Path(tmp) / f"diagram-{count}.mmd"
                source.write_text(match.group(1) + "\n")
                output = Path(tmp) / f"diagram-{count}.svg"
                result = subprocess.run(
                    [mmdc, "-q", "-p", str(config), "-i", str(source), "-o", str(output)],
                    capture_output=True,
                    text=True,
                )
                if result.returncode != 0 or not output.exists():
                    tail = (result.stderr or result.stdout).strip().splitlines()[-3:]
                    problems.append(f"{path.relative_to(root)}: diagram {index} failed: {' | '.join(tail)}")
    for problem in problems:
        print(problem)
    if problems:
        print(f"mermaid: {len(problems)} problem(s) in {count} diagrams")
        return 1
    print(f"mermaid: ok ({count} diagrams)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
