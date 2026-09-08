# Decision: adopt AI-DLC for the repository workflow

Status: accepted
Owner: repository maintainer
Date: 2026-09-07

## Context

FDE Kit was built through design specs and implementation plans under `docs/superpowers/`, with verification listed as manual shell steps. There was no CI, no validation script, and no place to record work scope and acceptance before implementation. The maintainer also maintains [AI-DLC](https://github.com/Sean-Koval/ai-dlc), which provides a project workflow (discovery → requirements → design → specification decision → reviewed work record → implement → checks → finish), a checks manifest, managed agent guidance files, and a packaging convention for agent skills.

## Options considered

1. Keep the ad hoc spec-and-plan process and add a CI workflow by hand.
2. Adopt AI-DLC with the generic preset, configure repository-specific checks, and use its work records and documentation templates.
3. Adopt AI-DLC fully, including tracker (Linear) and specification (OpenSpec) roles.

## Decision

Option 2. Adopt AI-DLC with the `scm` and `agent-client` capabilities only.

- `ai-dlc.toml` declares four required checks: `generated`, `links`, `schemas`, `whitespace`. The last three are plain Python scripts under `scripts/` with no dependencies beyond Python 3.11 and Git.
- `.ai-dlc/work/<id>.toml` records reviewed scope and acceptance for each delivery slice. Work is tracked manually until a tracker role is selected; `ai-dlc work publish/finish` are not used.
- Durable records follow the AI-DLC templates: `docs/design/` for PRDs and designs, `docs/decisions/` for ADRs, `docs/reviews/` for discovery reviews, `docs/roadmap.md` for sequencing. The earlier `docs/superpowers/` records remain as history.
- CI (`.github/workflows/verify.yml`) runs the check scripts directly rather than through `scripts/bootstrap.sh`, because no AI-DLC release bootstrap is published yet. The `generated` check in CI uses `scripts/check_generated.py`, which verifies managed-file digests and the AGENTS.md check index without the CLI. Locally and in agent sessions, `ai-dlc project check --required` runs the authoritative manifest, including `ai-dlc agents render --check`.
- `.mise.toml` pins no runtime. The repository is Markdown plus small scripts.

## Consequences

- Every content contract that was previously checked by hand is now enforced automatically, locally and in CI.
- Agent sessions receive shared guidance through `AGENTS.md` and `CLAUDE.md` and the eight AI-DLC skills under `.claude/skills/` and `.agents/skills/`. Those files are managed; edit `ai-dlc.toml` and re-render instead of editing them.
- Template-managed files (`AI-DLC.md`, `bootstrap/`, `scripts/bootstrap.sh`, `docs/workflows/`, `docs/templates/`, `docs/development-workflow.md`) can be updated later with `ai-dlc project sync`. `verify.yml` was modified and will merge three-way on sync.
- When an AI-DLC release bootstrap is published, CI can switch to the template's bootstrap path and receipts without changing the check manifest.
- Selecting a tracker or specification role later requires no change to the check manifest; it adds finish gates.

## Links

- [Development workflow](../development-workflow.md)
- [Release design](../design/2026-09-07-field-craft-and-technical-foundations.md)
- [AI-DLC brownfield workflow](../workflows/brownfield.md)
