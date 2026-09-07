# FDE Kit review and discovery

Owner: repository maintainer
Status: reviewed discovery; feeds the [PRD](../design/fde-kit-prd.md) and [next-release design](../design/2026-09-07-field-craft-and-technical-foundations.md)
Date: 2026-09-07
Method: AI-DLC `discovery` skill applied to the repository at commit `4d32cb6`, plus an expert reading of the content against what AI forward deployed engineers do at frontier-model companies.

## Bounded problem statement

FDE Kit teaches an evidence-driven delivery method for AI implementation work and provides seven copy-ready artifacts, four method guides, and one strong worked example. It does not yet teach the technical craft of building LLM systems, the customer-facing craft of running an engagement, or provide a structured path for a person to become an AI FDE. It also has no agent-usable tooling, no diagrams that render on GitHub, and, before this review, no automated checks.

The next release should close the gaps that block the two named audiences: a **learner** who wants to become a great AI FDE, and a **practitioner** who wants to start an engagement tomorrow without inventing the basics.

## What the repository does well

These strengths should be protected, not diluted, by growth.

1. **The information architecture is disciplined.** Learning explains *what and why*, stages say *what now*, skills teach *how*, the toolkit gives *what to use*, examples show *what good looks like*. Each index states its contribution contract. Most practitioner repositories never get this far.
2. **The operating model is correct.** "Find leverage → Map reality → Design the boundary → Prove quality → Land production → Transfer ownership → Compound learning" mirrors how strong FDE teams actually work. The "least fragile owner" rule for assigning responsibilities to AI, deterministic software, and accountable humans is the single most useful idea in the kit; it is how mature AI teams think about production boundaries.
3. **The worked example models intellectual honesty.** Predeclared analysis, matched samples, confidence intervals, a limitations section, and three separate expand/hold/stop decisions are exactly the evidence discipline that research-led organizations want from field engineers. This is a differentiator; most "case studies" in this space assert results.
4. **The templates elicit decisions and evidence.** Every artifact asks for owners, dates, thresholds, failure paths, and revisit triggers rather than commentary. That keeps them usable in a real engagement.
5. **The build process is traceable.** Design specs and implementation plans under `docs/superpowers/` show how each release was produced and verified.

## Evidence reviewed

| Source | What it shows |
| --- | --- |
| `README.md`, five section indexes | Audience, boundaries, learner and practitioner paths |
| `learning/*.md`, `learning/presentations/fde-overview.html` | Role framing, principles, lifecycle, 16-slide field playbook |
| `stages/0[1-7]-*/README.md` | Consistent nine-section stage schema; every stage links real skills and artifacts |
| `skills/*.md` (4), `toolkit/*.md` (7) | Method guides and templates; schemas consistent |
| `examples/invoice-intake-ai/README.md` | Complete Discover→Expand narrative with completed excerpts of all seven artifacts |
| `docs/superpowers/specs`, `docs/superpowers/plans` | Two shipped releases (2026-08-24 structure, 2026-08-26 AI FDE content); verification was manual |
| Git history (17 commits) | Steady, reviewed increments; no CI, no validation scripts, no CONTRIBUTING |
| Public role descriptions for forward deployed and applied AI engineers at OpenAI, Anthropic, Palantir, Scale, and Stripe (cited in the deck) | Expectations: embed with customers, build production systems on frontier models, own evaluation, integrate with enterprise systems, handle security review, enable customer teams, return product signal |

## Findings

Findings are ordered by how much they block the two audiences.

### F1. The technical layer is missing

The kit teaches *where* AI belongs in a workflow but not *how to build the AI part well*. An AI FDE at a frontier-model company spends most build time on context and prompt design, tool-using agents, retrieval and grounding, structured output, model and cost selection, grader construction, error analysis, guardrails, and observability. None of these have a skill guide. The evaluation skill correctly covers evidence gates and staged autonomy, but not how to construct a grader, calibrate a model-graded judge, or run an error-analysis loop.

Consequence: a learner can explain the operating model in an interview but cannot pass the technical rounds; a practitioner can scope an engagement but reaches Build with no guidance.

### F2. Customer craft is described but not equipped

Discover lists a "stakeholder map" as a deliverable and "interview users in the context of their work" as an activity, but the toolkit has no interview guide, stakeholder map, kickoff or workshop plan, pilot charter, or executive readout. The skills index already names workshop facilitation as a future candidate. Field engineers are judged heavily on discovery interviews, expectation management, and executive communication; the kit gives no practice material for any of them.

### F3. Security and governance have a slide but no artifact

Enterprise AI engagements are gated by security review: prompt injection through retrieved or tool-returned content, tool permission scoping, data classification and residency, logging of prompts and outputs, and model-provider terms. The deck names these; nothing in the toolkit lets an FDE walk into the review prepared.

### F4. The learner path is four links, not a path

The stated goal for this repository includes helping a person become a great AI FDE. There is no curriculum with modules, exercises, and self-assessment; no capstone; no interview preparation; no glossary. The existing skills have practice prompts, which is a good seed, but nothing sequences them.

### F5. Visuals exist only in a deck GitHub cannot render

The Reveal.js playbook is good, but a reader on GitHub sees HTML source. GitHub renders Mermaid natively, and the ideas that most benefit from diagrams (lifecycle loop, layered architecture, autonomy ladder, evaluation flywheel, responsibility boundary) have no Markdown diagram.

### F6. The kit is for AI FDEs but offers no agent tooling

Skills are human-readable guides only. Field engineers now work inside agent harnesses (Claude Code, Codex, and similar). Packaging the kit's methods as agent skills would let an FDE run a workflow trace, evaluation pack, or field report from inside their harness. AI-DLC already defines the packaging convention (`agents/skills/<name>/SKILL.md` with `name` and `description` frontmatter), so the kit can adopt it without inventing one.

### F7. One example, one shape

The invoice example is document extraction plus deterministic controls. The most common enterprise asks today are different shapes: a retrieval-grounded assistant over internal knowledge, and a tool-using agent that acts in business systems. Each raises different evaluation, security, and boundary questions that the current example cannot show.

### F8. Repository infrastructure was manual

Both implementation plans list link, schema, slide-count, and whitespace checks as manual shell steps. No script existed, and there was no CI. This review adopted AI-DLC and added the checks; see the [decision record](../decisions/0001-adopt-ai-dlc.md).

### F9. Stale index copy

`learning/README.md`, `learning/engagement-lifecycle.md`, and `stages/README.md` still say that skills and toolkit "currently define curated catalogs" or "do not yet supply stage-ready guides". That was true on 2026-08-24 and false since 2026-08-26.

## Assumptions

- A1. The primary reader is an individual engineer, not a delivery organization. The kit should optimize for one person learning and one person starting an engagement, not for a firm's methodology governance.
- A2. Vendor-neutral technical guidance is in scope; vendor tutorials and sample application code remain out of scope, as the August spec decided. Technical guides can name concrete mechanisms (structured outputs, tool calling, retrieval, model-graded evaluation) without teaching one vendor's SDK.
- A3. The seven-stage lifecycle and the seven artifacts are stable. New content links into them; it does not restructure them.
- A4. Mermaid is an acceptable diagram source because GitHub renders it and it diffs as text.
- A5. Agent skills packaged in the AI-DLC convention are a tooling layer, not a fifth content category; they are thin wrappers that reference the human guides and templates.

## Open questions

- Q1. Should the kit ship a second worked example in this release or the next? It is the most expensive item and its value depends on the technical guides existing first. Recommendation: next release.
- Q2. Should interview preparation name specific companies? Recommendation: describe the interview shapes (technical build, LLM system design, customer scenario, evidence discussion) and cite public role descriptions, without claiming knowledge of any company's private process.
- Q3. Should the deck grow technical slides? Recommendation: not now; keep it at 16 to 18 slides and let Markdown diagrams carry the technical layer.

## Smallest useful next investigation

None is required before building. The gaps are visible from the repository itself and from public role descriptions. The next step is a reviewed PRD and design for one release that closes F1 through F6, F8, and F9, and schedules F7.

## What "great" looks like for the person using this kit

This is the expert view that the roadmap should optimize toward. A strong AI FDE at a frontier-model company reliably does six things:

1. **Finds the workflow, not the demo.** Observes real work, measures a baseline, and picks a bounded wedge with an accountable owner. The kit already teaches this well.
2. **Builds the whole system, not the prompt.** Puts the model behind deterministic controls, designs tools with least privilege, grounds outputs in evidence, and returns to a safe state on failure. The kit teaches the boundary; it must now teach the build.
3. **Looks at the data.** Builds a representative case set, writes graders that can be re-run, reads failures one by one, classifies causes, and feeds fixes back into a regression set. This is the habit that separates strong field engineers from demo builders.
4. **Lands it in production and hands it over.** Staged autonomy, monitoring that measures workflow outcomes rather than uptime, named Day 2 owners, a rehearsed rollback. The kit covers this.
5. **Communicates precisely across altitudes.** Runs a discovery interview, facilitates a scoping workshop, writes an executive readout that states evidence and limits, and says no to unsafe scope. The kit needs artifacts here.
6. **Sends signal upstream.** Turns field failures into reproducible cases and product feedback that research and product teams can act on. The kit names this; a field report template makes it real.

The next release should make items 2, 3, and 5 as concrete as items 1, 4, and 6 already are.
