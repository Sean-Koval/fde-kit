#!/usr/bin/env python3
"""Verify AI-DLC managed files without requiring the AI-DLC CLI.

Usage: python3 scripts/check_generated.py [ROOT]

This is the CI-side stand-in for `ai-dlc agents render --check`. It confirms that
every file recorded in .ai-dlc/agent-ownership.json still matches its recorded
digest, and that the verification index in AGENTS.md lists every check command in
ai-dlc.toml. The authoritative render check still runs locally through the CLI.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
import tomllib
from pathlib import Path


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    problems: list[str] = []

    manifest_path = root / ".ai-dlc" / "agent-ownership.json"
    if not manifest_path.exists():
        problems.append(".ai-dlc/agent-ownership.json: missing; run ai-dlc agents render --apply")
    else:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for name, digest in sorted(manifest.get("files", {}).items()):
            path = root / name
            if not path.exists():
                problems.append(f"{name}: managed file missing")
                continue
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
            if actual != digest:
                problems.append(f"{name}: managed file edited; run ai-dlc agents render --apply")

    config = tomllib.loads((root / "ai-dlc.toml").read_text(encoding="utf-8"))
    commands = config.get("checks", {}).get("commands", {})
    agents = (root / "AGENTS.md").read_text(encoding="utf-8") if (root / "AGENTS.md").exists() else ""
    block = re.search(r"<!-- ai-dlc:begin [0-9a-f]{64} -->(.*?)<!-- ai-dlc:end -->", agents, re.S)
    if not block:
        problems.append("AGENTS.md: managed block missing; run ai-dlc agents render --apply")
    else:
        body = block.group(1)
        for check_id, command in commands.items():
            if f"- {check_id}: `{command}`" not in body:
                problems.append(f"AGENTS.md: verification index is stale for check '{check_id}'")
    claude = (root / "CLAUDE.md").read_text(encoding="utf-8") if (root / "CLAUDE.md").exists() else ""
    if "@AGENTS.md" not in claude:
        problems.append("CLAUDE.md: must import AGENTS.md")

    for problem in problems:
        print(problem)
    if problems:
        print(f"generated: {len(problems)} problem(s)")
        return 1
    print("generated: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
