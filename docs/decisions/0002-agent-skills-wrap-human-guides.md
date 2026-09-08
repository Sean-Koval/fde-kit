# Decision: agent skills follow the AI-DLC convention and wrap human guides

Status: accepted
Owner: repository maintainer
Date: 2026-09-07

## Context

The kit's skills are human-readable method guides. Field engineers increasingly work inside agent harnesses such as Claude Code and Codex, and the kit's purpose includes giving AI FDEs tooling. AI-DLC already packages agent skills as `agents/skills/<name>/SKILL.md` with `name` and `description` frontmatter, mirrored into `.claude/skills/` and `.agents/skills/`.

## Options considered

1. Do nothing; keep skills human-only.
2. Rewrite the human guides as agent prompts and drop the human form.
3. Add a separate `agents/skills/` layer in the AI-DLC convention, where each skill is a thin procedure that references the human guide and the toolkit template.
4. Invent a kit-specific packaging format.

## Decision

Option 3.

- `agents/skills/<name>/SKILL.md` is the source. Names are prefixed `fde-` to avoid collisions with AI-DLC's own skills.
- A skill states when to use it, the evidence it must ask the user for before producing anything, the procedure, the template path it fills, and completion checks. It links the human skill guide for judgment and the toolkit artifact for structure. It does not restate either.
- Skills never invent evidence, owners, thresholds, or approvals. Where evidence is missing they leave a marked gap and say what would fill it.
- `scripts/check_schemas.py` enforces frontmatter and index coverage.
- The kit's own `.claude/skills/` and `.agents/skills/` directories stay reserved for AI-DLC-managed files. Users install kit skills by copying a directory into their project or personal skill location, or through AI-DLC when its workflow bundle capability ships.

## Consequences

- One method, two surfaces: a person reads the guide; an agent runs the skill; both fill the same template.
- Agent skills stay small and stable because judgment lives in the guides, which are reviewed as content.
- If the AI-DLC convention changes, only the frontmatter and directory layout change.

## Links

- [agents/README.md](../../agents/README.md)
- [AI-DLC playbook](https://github.com/Sean-Koval/ai-dlc/blob/main/playbook/README.md)
