# Handoff: field craft and technical foundations release (R3)

Written with the AI-DLC `handoff` skill on 2026-09-07. The next person or agent should need the linked artifacts, not the session that produced them.

## Objective

Close findings F1 to F6, F8, and F9 of the [discovery review](../reviews/2026-09-07-fde-kit-review.md): teach the technical craft of building LLM systems, equip the customer-facing parts of an engagement, give learners a sequenced path, make the key ideas visible as diagrams, package the methods as agent skills, and automate the repository's content checks under AI-DLC.

## Branch and work reference

- Branch: `claude/fde-kit-review-buildout-yh03mj`, based on `main` at `4d32cb6`.
- Work records: `.ai-dlc/work/*.toml`. Seven R3 records are `reviewed = true` and delivered; `support-agent-example` is recorded for R4 with `reviewed = false`.
- Requirements and design: [PRD](../design/fde-kit-prd.md), [release design](../design/2026-09-07-field-craft-and-technical-foundations.md), ADRs [0001](../decisions/0001-adopt-ai-dlc.md), [0002](../decisions/0002-agent-skills-wrap-human-guides.md), [0003](../decisions/0003-mermaid-for-diagrams.md).
- Sequence: [roadmap](../roadmap.md).

## Verified state

Run on the final tree of this branch:

| Check | Command | Result |
| --- | --- | --- |
| generated | `ai-dlc agents render --check` and `scripts/check_generated.py` | passed |
| links | `python3 scripts/check_links.py` | passed, 104 Markdown files |
| schemas | `python3 scripts/check_schemas.py` | passed |
| whitespace | `python3 scripts/check_whitespace.py` | passed |
| mermaid (optional) | `python3 scripts/check_mermaid.py` with the Mermaid CLI and Chromium | passed, 16 diagrams |
| manifest | `ai-dlc project check --root . --required` | all four required checks passed |

CI (`.github/workflows/verify.yml`) runs the same four scripts on every pull request and push to `main`. It has not yet run on this branch because no pull request has been opened.

## What was delivered

| Slice | Files |
| --- | --- |
| Repository workflow | `ai-dlc.toml`, `AGENTS.md`, `CLAUDE.md`, `.ai-dlc/`, `.claude/skills/`, `.agents/skills/`, `scripts/check_*.py`, `.github/workflows/verify.yml`, `CONTRIBUTING.md`, AI-DLC template files (`AI-DLC.md`, `bootstrap/`, `docs/workflows/`, `docs/templates/`, `docs/development-workflow.md`) |
| Technical skill guides | `skills/context-engineering.md`, `skills/agent-and-tool-design.md`, `skills/retrieval-and-grounding.md`, `skills/eval-engineering.md`, `skills/production-readiness.md` |
| Customer-craft skill guides | `skills/discovery-interviewing.md`, `skills/executive-communication.md` |
| Field-craft toolkit | `toolkit/discovery-interview-guide.md`, `toolkit/stakeholder-map.md`, `toolkit/pilot-charter.md`, `toolkit/ai-security-review.md`, `toolkit/executive-readout.md`, `toolkit/field-report.md` |
| System patterns and diagrams | `learning/system-patterns.md`; Mermaid added to `learning/engagement-lifecycle.md` and `learning/what-is-an-fde.md` |
| Learning path | `learning/curriculum/README.md` and modules 01 to 07, `learning/interview-preparation.md`, `learning/glossary.md` |
| Agent skills | `agents/README.md`, `agents/skills/fde-{workflow-trace,opportunity-scorecard,responsibility-matrix,eval-pack,security-review,field-report}/SKILL.md` |
| Navigation | `README.md`, `learning/README.md`, `skills/README.md`, `toolkit/README.md`, `stages/README.md`, `examples/README.md`, and Related capabilities on all seven stage pages |

Totals after this release: 11 skill guides, 13 toolkit artifacts, 7 curriculum modules, 6 agent skills, 1 worked example, 16 slide deck unchanged.

## Remaining risks and open items

1. **No human read of the learner path yet.** Every file was reviewed against the quality bar and schema, but nobody has walked modules 01 to 07 as a learner. First task of R4.
2. **Agent skills are untested in a live harness.** They follow the AI-DLC packaging convention and reference real template sections, but no session has run one end to end. Try `fde-workflow-trace` on a real case and record what the skill asked for that the template did not need, or the reverse.
3. **CI is unverified on this branch.** The workflow was rewritten to run without an AI-DLC release bootstrap; its first run happens when a pull request is opened. If it fails, the scripts run identically locally, so the cause will be environment (Python version on the runner) rather than content.
4. **Fictional figures added inside the LumenPeak story.** The new guides introduce a prompt version `P-AP-1.3`, judge agreement of 94 percent with kappa 0.83, and an 11-of-19 failure cluster that the worked example does not itself record. They are labeled fictional and do not contradict the example. Either add them to the example in R4 or keep them as guide-only illustrations.
5. **Template-managed files were modified.** `verify.yml` differs from the AI-DLC template; `ai-dlc project sync` will merge three-way when the template updates. `.gitignore` was merged by hand.
6. **The sandbox could not run `mise install` for the AI-DLC checkout itself** (proxy blocks mise's version endpoints and the GitHub releases API). This does not affect FDE Kit, whose `.mise.toml` pins nothing. On a normal machine `sh scripts/bootstrap.sh --source` in the ai-dlc checkout completes.

## Next action

Open a pull request from `claude/fde-kit-review-buildout-yh03mj` to `main`, confirm CI is green, and have one person read the learner path end to end, recording dead ends as issues. Then start R4 with `support-agent-example` (record already in `.ai-dlc/work/`), which the technical guides now make possible.

## Authoritative links

- Discovery: `docs/reviews/2026-09-07-fde-kit-review.md`
- Requirements: `docs/design/fde-kit-prd.md`
- Design: `docs/design/2026-09-07-field-craft-and-technical-foundations.md`
- Decisions: `docs/decisions/`
- Sequence: `docs/roadmap.md`
- Workflow: `AI-DLC.md`, `docs/development-workflow.md`, `CONTRIBUTING.md`
