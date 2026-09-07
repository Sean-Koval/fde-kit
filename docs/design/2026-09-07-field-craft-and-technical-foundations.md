# Design: Field craft and technical foundations release

## Identity and links

- Owner: repository maintainer
- Status: reviewed 2026-09-07
- Work IDs: `repository-workflow`, `technical-skill-guides`, `customer-craft-skill-guides`, `field-craft-toolkit`, `learning-path`, `system-patterns-and-diagrams`, `agent-skills`
- Requirements: [PRD](fde-kit-prd.md) outcomes O1 to O9
- Tracker: not configured; see [ADR 0001](../decisions/0001-adopt-ai-dlc.md)

## Outcome and scope

- Audience and problem: see the [PRD](fde-kit-prd.md). This release closes findings F1 to F6, F8, and F9 of the [discovery review](../reviews/2026-09-07-fde-kit-review.md).
- Measurable outcome: every PRD acceptance row for O1 to O9 is satisfied and `ai-dlc project check --required` passes.
- In scope: the files listed under Delivery below.
- Non-goals: a second worked example (F7), deck changes, vendor tutorials.
- Constraints: existing schemas, section boundaries, and heuristic labeling.

## Content architecture after this release

```text
fde-kit/
├── learning/
│   ├── what-is-an-fde.md, operating-principles.md, engagement-lifecycle.md   (existing; gain Mermaid diagrams)
│   ├── system-patterns.md                (new: reference patterns with diagrams)
│   ├── glossary.md                       (new)
│   ├── interview-preparation.md          (new)
│   ├── curriculum/                       (new: README + 07 modules)
│   └── presentations/fde-overview.html   (unchanged)
├── stages/                               (existing; Related capabilities gain new links)
├── skills/                               (4 existing + 7 new)
├── toolkit/                              (7 existing + 6 new)
├── examples/                             (unchanged)
├── agents/                               (new: README + skills/<name>/SKILL.md)
├── scripts/check_*.py                    (new)
├── docs/                                 (AI-DLC workflow records)
└── .ai-dlc/work/*.toml                   (reviewed work records)
```

### Skills added

| File | Title | Teaches | Stages |
| --- | --- | --- | --- |
| `skills/context-engineering.md` | Context engineering and prompt design | What belongs in context, instruction versus evidence, structured output, decomposition, prompts as versioned code, failure modes | Design, Build, Enable |
| `skills/agent-and-tool-design.md` | Designing tool-using agents | Workflow versus agent loop, tool contracts, permission tiers, approval points, state, stopping rules, budgets, traces | Design, Build, Deploy |
| `skills/retrieval-and-grounding.md` | Retrieval and grounding | Choosing retrieval, long context, or tuning; indexing and chunking; hybrid search; citations; permissions-aware retrieval; evaluating retrieval separately | Design, Build, Enable |
| `skills/eval-engineering.md` | Grader design and error analysis | Case sets, grader types, calibrating model-graded judges against human labels, uncertainty, the error-analysis loop, online signals | Design, Build, Deploy, Enable |
| `skills/production-readiness.md` | Production readiness for LLM systems | Tracing, versioning, guardrails, resilience, cost and latency budgets, drift, change control, incident response | Build, Deploy, Enable |
| `skills/discovery-interviewing.md` | Discovery interviewing and workshop facilitation | Interview technique, observation, synthesis, kickoff and scoping workshops | Discover, Frame, Expand |
| `skills/executive-communication.md` | Executive communication and expectation management | Altitude, decision-first structure, evidence and limits, capability expectations, saying no, written readouts | Frame, Deploy, Enable, Expand |

### Toolkit artifacts added

| File | Title | Purpose | Stages |
| --- | --- | --- | --- |
| `toolkit/discovery-interview-guide.md` | Discovery interview guide | Plan and run interviews by role; capture evidence, not opinions | Discover, Frame, Expand |
| `toolkit/stakeholder-map.md` | Stakeholder map | Decision rights, incentives, risk posture, engagement plan | Discover, Frame, Deploy, Enable |
| `toolkit/pilot-charter.md` | Pilot charter | Hypothesis, wedge, exclusions, success and stop criteria, data access, owners, timeline, exit | Frame, Design, Deploy |
| `toolkit/ai-security-review.md` | AI security and governance review | Prepare for enterprise security review of an LLM system | Design, Build, Deploy |
| `toolkit/executive-readout.md` | Executive readout | Decision-first status and outcome communication to sponsors | Frame, Deploy, Enable, Expand |
| `toolkit/field-report.md` | Field report | Send reproducible product and model signal upstream | Build, Enable, Expand |

### Learning additions

- `learning/curriculum/README.md` and modules `01-role-and-operating-model.md`, `02-discovery-and-framing.md`, `03-system-design.md`, `04-evaluation-engineering.md`, `05-production-and-day-two.md`, `06-customer-craft.md`, `07-capstone.md`. Module schema: Outcome, Prerequisites, Study, Exercise, Assessment, Next.
- `learning/interview-preparation.md`: interview shapes (technical build, LLM system design, customer scenario, evidence discussion, behavioral), drills that reuse curriculum exercises, and a self-scoring rubric.
- `learning/glossary.md`: terms used across the kit with one-sentence definitions and links.
- `learning/system-patterns.md`: assist, extract-validate-act, retrieval-grounded assistant, tool-using agent, batch classification and routing. Each with a Mermaid diagram, when to use, boundary and evaluation notes, and links to skills.
- Mermaid diagrams added inline to `learning/engagement-lifecycle.md` (lifecycle loop) and `learning/what-is-an-fde.md` (operating model and artifacts).

### Agent skills

`agents/README.md` explains installation (copy a skill directory into `.claude/skills/` or `.agents/skills/`, or manage it through AI-DLC) and the design rule: a skill supplies judgment and points to the human guide and template; it never replaces them. Skills: `fde-workflow-trace`, `fde-opportunity-scorecard`, `fde-responsibility-matrix`, `fde-eval-pack`, `fde-security-review`, `fde-field-report`. Each SKILL.md has `name` and `description` frontmatter, a short procedure, the evidence it must ask for, the template path, and completion checks.

### Repository workflow

AI-DLC adopted with the generic preset and `scm` plus `agent-client` capabilities. Checks: `generated`, `links`, `schemas`, `whitespace`. CI runs the check scripts directly. `CONTRIBUTING.md` carries the quality bar and content conventions.

## User journey and states

Learner: `README.md` → `learning/curriculum/README.md` → modules in order → capstone → `interview-preparation.md`. Every module links the guides and artifacts it uses, so the learner reads the practitioner material in a sequence.

Practitioner: `README.md` → stage page → skill guide → toolkit artifact → agent skill when working in a harness → example for comparison.

## System boundaries and interfaces

- Section boundaries are unchanged. Agent skills are a tooling layer under `agents/`, not a content category.
- Interfaces between files are relative links; the link check enforces them.
- Schemas are enforced by `scripts/check_schemas.py`; a new content type must add its schema there in the same change.

## Decisions and rationale

- [ADR 0001](../decisions/0001-adopt-ai-dlc.md): adopt AI-DLC for the workflow; CI runs the checks manifest directly.
- [ADR 0002](../decisions/0002-agent-skills-wrap-human-guides.md): agent skills follow the AI-DLC packaging convention and wrap human guides.
- [ADR 0003](../decisions/0003-mermaid-for-diagrams.md): Mermaid in Markdown is the diagram source.

## Behavioral contract

Acceptance criteria live in each work record under `.ai-dlc/work/`. No formal specification provider is configured; each record states `requires_spec = false` with its reason.

## Verification strategy

- `ai-dlc project check --required` locally; CI runs the same scripts.
- One reviewer pass per new file against the quality bar in `CONTRIBUTING.md`: specific, evidence-oriented, heuristics labeled, good and weak patterns concrete, links into stages and artifacts.
- Manual read of the learner path end to end after all modules exist.

## Delivery and recovery

Delivery slices map one to one to work records and can land in any order after `repository-workflow`. Each slice is additive; rollback is reverting the slice's commit. Index updates (`README.md`, section READMEs, stage Related capabilities) land with the slice that adds the linked files so no index ever points at a missing file.

## Traceability

- Work records: `.ai-dlc/work/*.toml`
- Branch: `claude/fde-kit-review-buildout-yh03mj`
- Discovery: `docs/reviews/2026-09-07-fde-kit-review.md`
- Roadmap: `docs/roadmap.md`
