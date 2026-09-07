# Product requirements: FDE Kit

Owner: repository maintainer
Status: reviewed 2026-09-07
Supersedes: the purpose sections of the 2026-08-24 and 2026-08-26 design specs under `docs/superpowers/specs/`, which remain the record of those releases.

## Problem and audience

AI forward deployed engineers turn a customer's operational problem into an adopted, governed production system built on frontier models. People who want to do this work, and people already doing it, lack one place that teaches the method, the technical craft, and the customer craft together, with artifacts they can use the same day.

Two audiences, in priority order:

1. **Learner.** An engineer who wants to become an AI FDE at a company such as OpenAI, Anthropic, Palantir, or Scale, or on an enterprise AI team. Needs a sequenced path, exercises, a way to self-assess, and preparation for how such roles are evaluated.
2. **Practitioner.** An engineer starting or running an engagement. Needs stage guidance, method guides, copy-ready artifacts, and agent tooling that fits the harness they already work in.

Secondary readers: delivery leaders and adjacent partners (account, product, research) who need a shared model of the work.

## Outcomes and acceptance

| ID | Outcome | Acceptance |
| --- | --- | --- |
| O1 | A learner can follow a sequenced curriculum from role understanding to a capstone engagement | `learning/curriculum/` has ordered modules with outcome, prerequisites, study, exercise, assessment, and next; a capstone module with a rubric exists |
| O2 | A learner can prepare for how AI FDE roles are evaluated | `learning/interview-preparation.md` describes interview shapes with practice drills and cites only public role descriptions |
| O3 | A practitioner can build the AI part of a workflow well, not only place it | Skill guides exist for context and prompt design, tool-using agents, retrieval and grounding, grader design and error analysis, and production readiness; each follows the skill schema |
| O4 | A practitioner can run the customer-facing parts of an engagement | Skill guides for discovery interviewing and facilitation, and executive communication; toolkit artifacts for interview guide, stakeholder map, pilot charter, executive readout, and field report |
| O5 | A practitioner can enter an enterprise security review prepared | `toolkit/ai-security-review.md` covers data handling, prompt injection, tool permissions, logging and retention, provider terms, and incident response |
| O6 | Key ideas are visible as diagrams on GitHub | Mermaid diagrams for the lifecycle, operating model, system patterns, responsibility boundary, autonomy ladder, and evaluation loop |
| O7 | An FDE can use the kit's methods inside an agent harness | `agents/skills/<name>/SKILL.md` files in the AI-DLC convention wrap the workflow trace, opportunity scorecard, responsibility matrix, evaluation pack, security review, and field report |
| O8 | Every published file meets its schema and every link resolves, automatically | `ai-dlc project check --required` and CI run link, schema, whitespace, and generated-file checks |
| O9 | Existing navigation reflects the published content | No index says that skills or toolkit content is not yet available |

## Scope and exclusions

In scope: Markdown guides, templates, curriculum, diagrams, agent skill wrappers, validation scripts, CI, and repository workflow records.

Out of scope for this PRD:

- Vendor SDK tutorials, sample application code, or notebooks. Technical guides name mechanisms (structured output, tool calling, retrieval, model-graded evaluation) neutrally.
- A second worked example. Scheduled in the [roadmap](../roadmap.md) after the technical guides exist.
- Changes to the seven-stage lifecycle, the seven original artifacts, or the deck's slide count.
- Any claim about a specific company's private interview process.
- Office-document exports.

## Constraints and risks

- Every numeric rule remains a starting heuristic, labeled as such.
- New content must link into existing stages and the existing artifacts rather than duplicating them.
- Growth must not blur the section boundaries: learning explains, stages sequence, skills teach, toolkit equips, examples show, agents wrap.
- Risk: technical guides age quickly. Mitigation: teach durable mechanisms and decision rules, not vendor feature lists; date the guides.
- Risk: volume without quality. Mitigation: schema checks, one reviewer pass per file, and the quality bar in `CONTRIBUTING.md`.
- Risk: agent skills drift from the human guides. Mitigation: skills are thin wrappers that reference the guide and template paths; the schema check enforces frontmatter.

## Open questions

- Whether to package the agent skills as an AI-DLC workflow bundle once that capability ships upstream. Not blocking.
- Whether the deck should gain a technical slide set in a later release. Deferred.

## Links

- [Discovery review](../reviews/2026-09-07-fde-kit-review.md)
- [Release design](2026-09-07-field-craft-and-technical-foundations.md)
- [Roadmap](../roadmap.md)
- Work records under `.ai-dlc/work/`
