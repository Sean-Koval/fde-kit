#!/usr/bin/env python3
"""Check every relative Markdown link and heading anchor in the repository.

Usage: python3 scripts/check_links.py [ROOT]

Exit 0 when every relative link resolves to an existing file (and, when a
fragment is present, to a heading in that file). External links are not fetched.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

SKIP_DIRS = {".git", ".venv", "node_modules", "target", ".worktrees", ".superpowers"}
LINK = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
IMAGE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")


def markdown_files(root: Path) -> list[Path]:
    files = []
    for path in root.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        files.append(path)
    return sorted(files)


def slug(text: str) -> str:
    """Approximate GitHub's heading anchor algorithm."""
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def anchors(path: Path) -> set[str]:
    seen: dict[str, int] = {}
    result: set[str] = set()
    in_fence = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = HEADING.match(line)
        if not match:
            continue
        base = slug(match.group(2))
        count = seen.get(base, 0)
        seen[base] = count + 1
        result.add(base if count == 0 else f"{base}-{count}")
    for match in re.finditer(r'id="([^"]+)"', path.read_text(encoding="utf-8")):
        result.add(match.group(1))
    return result


def check(root: Path) -> list[str]:
    problems: list[str] = []
    anchor_cache: dict[Path, set[str]] = {}
    for path in markdown_files(root):
        text = path.read_text(encoding="utf-8")
        in_fence = False
        for number, line in enumerate(text.splitlines(), start=1):
            if FENCE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            targets = [m.group(1) for m in LINK.finditer(line)]
            targets += [m.group(1) for m in IMAGE.finditer(line)]
            for raw in targets:
                target = raw.strip("<>")
                if re.match(r"^[a-z][a-z0-9+.-]*:", target):
                    continue
                if target.startswith("#"):
                    file_part, fragment = "", target[1:]
                else:
                    file_part, _, fragment = target.partition("#")
                resolved = path if not file_part else (path.parent / unquote(file_part)).resolve()
                rel = path.relative_to(root)
                if not resolved.exists():
                    problems.append(f"{rel}:{number}: missing target {raw}")
                    continue
                if fragment and resolved.suffix in {".md", ".html"}:
                    if resolved not in anchor_cache:
                        anchor_cache[resolved] = anchors(resolved)
                    if unquote(fragment) not in anchor_cache[resolved]:
                        problems.append(f"{rel}:{number}: missing anchor #{fragment} in {file_part or rel}")
    return problems


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    problems = check(root)
    for problem in problems:
        print(problem)
    count = len(markdown_files(root))
    if problems:
        print(f"links: {len(problems)} problem(s) in {count} Markdown files")
        return 1
    print(f"links: ok ({count} Markdown files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
