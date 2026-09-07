# FDE Kit roadmap

Updated: 2026-09-07. This document owns delivery sequence. The [PRD](design/fde-kit-prd.md) owns intended outcomes; the [discovery review](reviews/2026-09-07-fde-kit-review.md) owns the evidence behind them. No tracker is configured; status lives in the work records under `.ai-dlc/work/` and in this table.

## Where the kit is

| Release | Date | Delivered |
| --- | --- | --- |
| R1 Learning center foundation | 2026-08-24 | Information architecture, lifecycle, seven stage pages, section contracts |
| R2 AI FDE content | 2026-08-26 | Field playbook deck, four method guides, seven artifacts, invoice-intake worked example |
| R3 Field craft and technical foundations | in progress | See below |

## R3: Field craft and technical foundations

Goal: make building the AI part, evaluating it, and running the customer relationship as concrete as the kit already makes choosing the workflow and landing production.

| Work ID | Outcome | Depends on | Status |
| --- | --- | --- | --- |
| `repository-workflow` | AI-DLC adopted; link, schema, whitespace, and generated-file checks run locally and in CI; contribution guide | none | done |
| `technical-skill-guides` | Five technical skill guides: context engineering, tool-using agents, retrieval and grounding, grader design and error analysis, production readiness | `repository-workflow` | planned |
| `customer-craft-skill-guides` | Two skill guides: discovery interviewing and facilitation; executive communication | `repository-workflow` | planned |
| `field-craft-toolkit` | Six artifacts: interview guide, stakeholder map, pilot charter, AI security review, executive readout, field report | `repository-workflow` | planned |
| `system-patterns-and-diagrams` | Reference system patterns page with Mermaid diagrams; lifecycle and operating-model diagrams in learning pages | `repository-workflow` | planned |
| `learning-path` | Seven-module curriculum with capstone, interview preparation, glossary | all guides and artifacts above | planned |
| `agent-skills` | Six agent skills in the AI-DLC convention with an installation guide | `field-craft-toolkit` | planned |

Exit: every PRD acceptance row O1 to O9 is satisfied, `ai-dlc project check --required` passes, and a full read of the learner path finds no dead end.

## R4: Second shape, deeper practice

| Work ID | Outcome | Depends on |
| --- | --- | --- |
| `support-agent-example` | Worked example of a retrieval-grounded, tool-using support agent showing permissions-aware retrieval, tool approval tiers, prompt-injection handling, and evaluation of retrieval and generation separately | R3 technical guides |
| `scenario-drills` | Timed practice scenarios (scoping call, security review, "the demo worked but production does not", executive pushback) with model answers and rubrics | `learning-path` |
| `deck-technical-supplement` | A second short deck or an added slide set covering system patterns and evaluation, keeping the field playbook at 16 to 18 slides | `system-patterns-and-diagrams` |

## R5: Distribution and measurement

| Work ID | Outcome | Depends on |
| --- | --- | --- |
| `workflow-bundle` | Package the kit's agent skills and templates as an AI-DLC workflow bundle once that capability ships upstream | AI-DLC portable workflow bundles |
| `usage-evidence` | Collect evidence that the curriculum changes what learners can do: before and after capstone scores, and feedback from practitioners who used an artifact in a real engagement | `learning-path` |
| `tracker-role` | Select a tracker so work records gain published status and evidence-gated finish | maintainer decision |

## Explicitly deferred

- Vendor SDK tutorials and sample application code. The kit teaches mechanisms and decision rules; vendor documentation teaches APIs.
- Company-specific interview claims. The kit describes interview shapes from public role descriptions only.
- Office-document exports of templates.
- A glossary of general machine-learning terms. The glossary covers terms the kit uses in its own sense.
