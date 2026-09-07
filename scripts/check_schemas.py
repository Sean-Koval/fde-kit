#!/usr/bin/env python3
"""Validate the content contracts that hold this repository together.

Usage: python3 scripts/check_schemas.py [ROOT]

Checks:
- Toolkit artifacts, skill guides, stage pages, curriculum modules, and agent
  skills carry their required sections in order.
- Section indexes link every published file in their directory.
- Every stage page links at least one skill and one toolkit artifact.
- Worked examples reference every lifecycle stage and every toolkit artifact
  they claim in their artifact index.
- The overview deck has 16 to 18 top-level slides with unique IDs.
- No public directory is empty and no placeholder text remains.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

TOOLKIT_SECTIONS = [
    "Purpose",
    "Timing",
    "Instructions",
    "Expected output",
    "Supported stages",
    "Template",
    "Completion checks",
]
SKILL_SECTIONS = [
    "Relevance",
    "Timing",
    "Technique",
    "Examples",
    "Practice",
    "Self-assessment",
    "Links",
]
STAGE_SECTIONS = [
    "Objective",
    "Entry conditions",
    "Questions to answer",
    "Recommended activities",
    "Expected deliverables",
    "Exit criteria",
    "Common failure modes",
    "Related capabilities",
    "Practice",
]
MODULE_SECTIONS = [
    "Outcome",
    "Prerequisites",
    "Study",
    "Exercise",
    "Assessment",
    "Next",
]
STAGES = ["01-discover", "02-frame", "03-design", "04-build", "05-deploy", "06-enable", "07-expand"]
SKIP_DIRS = {".git", ".venv", "node_modules", "target", ".worktrees", ".superpowers", ".ai-dlc"}
PLACEHOLDERS = ("TODO", "TBD", "lorem ipsum", "FIXME")


def h2s(text: str) -> list[str]:
    in_fence = False
    result = []
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence and line.startswith("## "):
            result.append(line[3:].strip())
    return result


def require_sections(path: Path, sections: list[str], problems: list[str], root: Path) -> None:
    text = path.read_text(encoding="utf-8")
    found = h2s(text)
    rel = path.relative_to(root)
    missing = [s for s in sections if s not in found]
    if missing:
        problems.append(f"{rel}: missing sections {missing}")
        return
    order = [found.index(s) for s in sections]
    if order != sorted(order):
        problems.append(f"{rel}: sections out of order; expected {sections}")


def published(directory: Path) -> list[Path]:
    return sorted(p for p in directory.glob("*.md") if p.name != "README.md")


def links_in(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    return {m.group(1).split("#")[0] for m in re.finditer(r"\]\(([^)\s]+)\)", text)}


def check(root: Path) -> list[str]:
    problems: list[str] = []

    toolkit = root / "toolkit"
    for path in published(toolkit):
        require_sections(path, TOOLKIT_SECTIONS, problems, root)
        text = path.read_text(encoding="utf-8")
        if "```markdown" not in text:
            problems.append(f"{path.relative_to(root)}: Template must contain a ```markdown block")
        if "- [ ]" not in text:
            problems.append(f"{path.relative_to(root)}: Completion checks must use '- [ ]' items")

    skills = root / "skills"
    for path in published(skills):
        require_sections(path, SKILL_SECTIONS, problems, root)

    for name in STAGES:
        page = root / "stages" / name / "README.md"
        if not page.exists():
            problems.append(f"stages/{name}/README.md: missing")
            continue
        require_sections(page, STAGE_SECTIONS, problems, root)
        targets = links_in(page)
        if not any(t.startswith("../../skills/") and not t.endswith("README.md") for t in targets):
            problems.append(f"stages/{name}/README.md: links no skill guide")
        if not any(t.startswith("../../toolkit/") and not t.endswith("README.md") for t in targets):
            problems.append(f"stages/{name}/README.md: links no toolkit artifact")

    for directory in (toolkit, skills):
        index = directory / "README.md"
        if not index.exists():
            problems.append(f"{directory.relative_to(root)}/README.md: missing")
            continue
        listed = links_in(index)
        for path in published(directory):
            if path.name not in listed:
                problems.append(f"{directory.name}/README.md: does not link {path.name}")

    curriculum = root / "learning" / "curriculum"
    if curriculum.exists():
        for path in published(curriculum):
            require_sections(path, MODULE_SECTIONS, problems, root)
        index = curriculum / "README.md"
        if index.exists():
            listed = links_in(index)
            for path in published(curriculum):
                if path.name not in listed:
                    problems.append(f"learning/curriculum/README.md: does not link {path.name}")

    examples = root / "examples"
    example_pages = sorted(p for p in examples.glob("*/README.md"))
    if not example_pages:
        problems.append("examples: no worked example present")
    example_index = links_in(examples / "README.md") if (examples / "README.md").exists() else set()
    for page in example_pages:
        rel = page.relative_to(root)
        text = page.read_text(encoding="utf-8")
        if f"{page.parent.name}/README.md" not in example_index:
            problems.append(f"examples/README.md: does not link {page.parent.name}")
        for name in STAGES:
            if f"../../stages/{name}/README.md" not in text:
                problems.append(f"{rel}: does not reference stage {name}")
        if "Fictional" not in text and "fictional" not in text:
            problems.append(f"{rel}: must state that it is fictional")
        if "## Artifact and skill index" not in text:
            problems.append(f"{rel}: missing 'Artifact and skill index' section")
        else:
            index_text = text.split("## Artifact and skill index", 1)[1]
            claimed = re.findall(r"\.\./\.\./toolkit/([a-z0-9-]+\.md)", index_text)
            for artifact in claimed:
                if not (toolkit / artifact).exists():
                    problems.append(f"{rel}: claims unknown artifact {artifact}")
        body = text.split("## Artifact and skill index", 1)[0]
        for artifact in re.findall(r"\.\./\.\./toolkit/([a-z0-9-]+\.md)", text.split("## Artifact and skill index", 1)[1] if "## Artifact and skill index" in text else ""):
            if f"../../toolkit/{artifact}" not in body:
                problems.append(f"{rel}: artifact index lists {artifact} but the narrative never uses it")

    agent_skills = root / "agents" / "skills"
    if agent_skills.exists():
        for skill in sorted(agent_skills.iterdir()):
            if not skill.is_dir():
                continue
            file = skill / "SKILL.md"
            if not file.exists():
                problems.append(f"agents/skills/{skill.name}: missing SKILL.md")
                continue
            text = file.read_text(encoding="utf-8")
            match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
            if not match:
                problems.append(f"agents/skills/{skill.name}/SKILL.md: missing frontmatter")
                continue
            front = match.group(1)
            name = re.search(r"^name:\s*(\S+)", front, re.M)
            if not name or name.group(1) != skill.name:
                problems.append(f"agents/skills/{skill.name}/SKILL.md: frontmatter name must be '{skill.name}'")
            if not re.search(r"^description:\s*\S", front, re.M):
                problems.append(f"agents/skills/{skill.name}/SKILL.md: frontmatter description missing")
            index = agent_skills / "README.md"
            if index.exists() and f"{skill.name}/SKILL.md" not in index.read_text(encoding="utf-8"):
                problems.append(f"agents/skills/README.md: does not link {skill.name}/SKILL.md")

    deck = root / "learning" / "presentations" / "fde-overview.html"
    if deck.exists():
        html = deck.read_text(encoding="utf-8")
        slides_html = html.split('class="slides"', 1)[1] if 'class="slides"' in html else ""
        ids = re.findall(r"<section\s+id=\"([^\"]+)\"", slides_html)
        if not 16 <= len(ids) <= 18:
            problems.append(f"deck: expected 16-18 slides, found {len(ids)}")
        if len(ids) != len(set(ids)):
            problems.append("deck: duplicate slide IDs")
        if "<aside class=\"notes\">" not in html and "<aside class='notes'>" not in html:
            problems.append("deck: no speaker notes found")

    for directory in root.rglob("*"):
        if not directory.is_dir():
            continue
        parts = directory.relative_to(root).parts
        if any(part in SKIP_DIRS or part.startswith(".") for part in parts):
            continue
        if not any(directory.iterdir()):
            problems.append(f"{directory.relative_to(root)}: empty public directory")

    for path in root.rglob("*.md"):
        parts = path.relative_to(root).parts
        if any(part in SKIP_DIRS or part.startswith(".") for part in parts):
            continue
        if path.name == "CONTRIBUTING.md":
            continue  # names the banned markers on purpose
        text = path.read_text(encoding="utf-8")
        for marker in PLACEHOLDERS:
            if re.search(rf"\b{re.escape(marker)}\b", text):
                problems.append(f"{path.relative_to(root)}: contains placeholder '{marker}'")

    return problems


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    problems = check(root)
    for problem in problems:
        print(problem)
    if problems:
        print(f"schemas: {len(problems)} problem(s)")
        return 1
    print("schemas: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
