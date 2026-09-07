# Preparing for AI FDE interviews

This page describes interview shapes inferred from public role descriptions for forward deployed and applied AI engineering roles, and from how the work is actually done. It does not describe any company's private process, and processes vary: some roles run all five shapes below, others two, under different names. Nothing here claims what a named company asks.

The public descriptions cited on the closing slide of the [field playbook](presentations/fde-overview.html) converge on the same signals. The table maps each to the kit pages that build it; the [curriculum](curriculum/README.md) sequences those pages, and the [glossary](glossary.md) defines the terms used here.

## What role descriptions consistently ask for

| Signal in public role descriptions | What an interviewer is checking | Kit pages that build it |
| --- | --- | --- |
| Customer empathy and discovery | You learn the real workflow before proposing a solution | [Workflow discovery](../skills/workflow-discovery.md), [Discovery interviewing](../skills/discovery-interviewing.md), [Workflow trace](../toolkit/workflow-trace.md) |
| Deep build skill on frontier models | You build the whole system, not the prompt | [Context engineering](../skills/context-engineering.md), [Designing tool-using agents](../skills/agent-and-tool-design.md), [Retrieval and grounding](../skills/retrieval-and-grounding.md), [System patterns](system-patterns.md) |
| Evaluation rigor | You look at the data and can say what a number proves | [Grader design and error analysis](../skills/eval-engineering.md), [Evaluation and staged rollout](../skills/evaluation-and-rollout.md), [Evaluation pack](../toolkit/evaluation-pack.md) |
| Operating in ambiguity | You name the decision, the evidence gap, and the smallest test | [Opportunity scorecard](../toolkit/opportunity-scorecard.md), [Pilot charter](../toolkit/pilot-charter.md), [Operating principles](operating-principles.md) |
| Production and security judgment | The boundary, permissions, rollback, and Day 2 owners are explicit | [AI system design](../skills/ai-system-design.md), [Production readiness](../skills/production-readiness.md), [AI security review](../toolkit/ai-security-review.md), [Rollout plan](../toolkit/rollout-plan.md) |
| Clear communication across altitudes | Operator, engineer, and sponsor each get the same facts at the right level | [Executive communication](../skills/executive-communication.md), [Executive readout](../toolkit/executive-readout.md) |
| Returning product signal | A field failure becomes a reproducible case someone upstream can act on | [Adoption, operations, and product feedback](../skills/adoption-and-feedback.md), [Field report](../toolkit/field-report.md) |

## Interview shapes

Every duration, count, and week plan on this page is a starting heuristic, not an industry standard. Score each rubric row 0 (absent), 1 (present but weak), or 2 (would satisfy a skeptical reviewer); the right-hand column describes a 2.

### Technical build or take-home

**Format.** Build a small large language model (LLM) system against a given or self-chosen task, within a few days or a timed session, then walk through it. Evaluators typically look for a working system, a case set, honest limits, and clean code.

**Strong looks like.** A repository someone else can run. A case set stratified by the exceptions that matter, with expected outcomes and valid abstentions. Deterministic graders wherever they apply, a model-graded judge only where they do not, and the judge's agreement with your own hand labels reported. Failures read one by one, counted by cause, and the largest cause fixed. Deterministic validation between the model and any effect. A limits section that says what the evidence does not prove.

**Failure modes.** A demo on three inputs and no case set. One accuracy number with no strata or interval. Policy enforced in the prompt instead of in code. A judge never compared with a person. Evaluation cases copied from the few-shot examples. Time spent on the interface instead of on evidence.

**Drill.** Reuse the [module 04](curriculum/04-evaluation-engineering.md) exercise: label 20 real cases by hand, choose the cheapest valid grader per property, and run one error-analysis pass. Then wrap it in a runnable system with pre- and post-validation, as the [module 07](curriculum/07-capstone.md) capstone requires. Budget one evening for the system and one for the evidence; if the split inverts, you are building a demo.

Score the take-home with these rows before submitting it.

| Rubric row | A score of 2 |
| --- | --- |
| Runs from a clean checkout with one documented command | A reviewer ran it unaided |
| Case set is stratified and versioned, with abstain cases | Strata named; expected outcome and evidence per case |
| Graders are reproducible and judges are calibrated | Deterministic first; judge agreement reported |
| Error analysis names the largest cause and the fix | Failures read, counted, fixed in the right layer, added to regression |
| Limits are stated | What the evidence does not prove, in the README |

### LLM system design

**Format.** Given a customer scenario ("Harbor Mutual, a fictional insurer, wants to triage claims correspondence"), design the system in roughly 45 minutes on a whiteboard or shared document while the interviewer pushes on trade-offs.

**Strong looks like.** The first minutes go to the workflow, not the architecture: who does the work, the system of record, the consequential decisions, the baseline. Then a [responsibility matrix](../toolkit/responsibility-matrix.md) across AI, deterministic software, and humans; a [system pattern](system-patterns.md) justified as the least autonomous shape that reaches the outcome; and the evaluation plan, security controls, and rollout gates. You name what you excluded and why.

Suggested structure for 45 minutes: 8 minutes on workflow, actors, baseline, and consequence; 12 on the responsibility matrix; 10 on the pattern, tool contracts, permission tiers, and context layers; 8 on evaluation and rollout gates; 7 on security, failure behavior, and the first thing you would test.

**Failure modes.** Starting with a model choice. Boxes without owners. The model's stated confidence used as a control. No abstention path. No answer to "what happens when retrieval is down" or "what stops the agent". Bounded autonomy on day one.

**Drill.** Reuse the [module 03](curriculum/03-system-design.md) exercise against a timer: a responsibility matrix and a justified pattern choice in 45 minutes, then a peer asks three "what if" questions (conflicting evidence, missing permission, tool failure). Repeat weekly with a different pattern.

| Rubric row | A score of 2 |
| --- | --- |
| Workflow, actors, baseline, and consequence established before architecture | All four named in the first ten minutes |
| Every consequential responsibility has a least fragile owner | Rules in code; humans on irreversible decisions; matrix complete |
| Pattern justified against path variability and consequence | Decision rule stated; the simpler shape ruled out with a reason |
| Evaluation, security, and rollout stated, not implied | Case-set strata, permission tiers, first gate, rollback owner |
| Exclusions and first test named | First wedge and riskiest assumption identified |

### Customer scenario or role-play

**Format.** The interviewer plays a sponsor, an operator, or a security reviewer. Typical scenes: a scoping call that opens with "we want AI for accounts payable"; pushback on scope or timeline; "can it do X" where X is unsafe or unproven; a request that requires saying no.

**Strong looks like.** You climb the question ladder from open to specific to evidence and stay on one real case, separating what was said from what can be shown. To "can it do X" you answer with the mechanism, the evidence you would need, and the boundary. When you say no, you offer the bounded alternative and the evidence gate that would reopen the question, as the [LumenPeak](../examples/invoice-intake-ai/README.md) team did when it stopped bank-detail changes and routed them back to Discover as vendor-master work.

**Failure modes.** Describing the product before understanding the case. Agreeing to autonomy to keep the room happy. Answering "can it do X" with a capability claim. Saying no without an alternative. Never asking who owns the outcome.

**Drill.** Reuse the two hard conversations from the [module 06](curriculum/06-customer-craft.md) exercise, but run them live: a 20-minute scoping call with a peer playing a sponsor who has a solution in mind, then a 10-minute scene where the sponsor asks for an action you should decline. Record it and count the solution statements you made before the first observed case.

| Rubric row | A score of 2 |
| --- | --- |
| Reached a real case and its evidence before any solution talk | One case retold step by step; an artifact requested |
| Named the outcome owner and the decision to be made | Owner, decision, and deadline captured |
| "Can it do X" answered with mechanism, evidence, and boundary | Stated what would have to be true and how it would be shown |
| Said no with a bounded alternative and a reopen condition | Alternative wedge plus the evidence gate |

### Evidence discussion or past-project deep dive

**Format.** Walk through one project you delivered. The interviewer asks for the baseline, the measurement, the numbers behind the claim, what the evidence did not prove, and what you would do differently.

**Strong looks like.** The baseline with its source and period; the sample and how it was selected; the threshold fixed before the run and its owner; the result with its uncertainty. You volunteer the limits (cohort, duration, seasonality, what was not measured), name one failure you read in a trace and the layer where the fix went, and separate capacity value from cash savings. The [LumenPeak](../examples/invoice-intake-ai/README.md) limitations section is the model: a 30-day, four-analyst pilot with a matched sample, a confidence interval, and a list of what the result does not establish.

**Failure modes.** A percentage with no denominator. A baseline that was the sponsor's estimate. A threshold chosen after the results were seen. Crediting the model when a deterministic check or a workflow change did the work. Limits offered only when asked.

**Drill.** Reuse the [module 07](curriculum/07-capstone.md) capstone: write its evaluation pack and limitations section, then have a peer interrogate only "what the evidence does not prove" for 15 minutes. Add every question you could not answer to the pack.

| Rubric row | A score of 2 |
| --- | --- |
| Baseline has a source, period, and owner | Record identifier and selection method stated |
| Threshold and decision owner fixed before the run | Named owner; hold and rollback rules stated |
| Result reported with denominator, strata, and uncertainty | Per-stratum rates and an interval |
| Limits volunteered, not extracted | Cohort, duration, mix, and unmeasured effects listed |
| One concrete change you would make, with the evidence behind it | A specific failure, its cause, and the fix layer |

### Behavioral

**Format.** Structured questions about past behavior: ownership when nobody else took it, work under ambiguity, cross-functional conflict, delivering bad news, learning from a failure.

**Strong looks like.** Stories with a decision in the middle. Ownership: the consequential call you made, who you told, and what you would have done if wrong. Ambiguity: the decision you had to inform, the evidence gap, and the smallest test you ran. Cross-functional work: the boundary disagreement among business, technical, and risk/control owners and how evidence resolved it. Bad news: the decision-first readout with the number, the limit, and the ask.

**Failure modes.** Team stories with no personal decision. Ambiguity resolved by working harder rather than by naming the decision. Bad news delivered as a status update. Conflict stories in which the other party was simply wrong.

**Drill.** Reuse the [module 01](curriculum/01-role-and-operating-model.md) exercise, the seven-move operating model applied to a workflow you know, and add one story from your own history per move in four lines: situation, the decision you made, the evidence you used, what happened. Rehearse the four that fit the prompts above in under two minutes each.

| Rubric row | A score of 2 |
| --- | --- |
| A decision you personally made sits at the center | The call, the alternatives, and your reasoning |
| Evidence and its limits appear in the story | Numbers with sources; what you did not know |
| The other party's constraint is stated fairly | Their incentive and risk posture named |
| Bad news led with the decision needed | Decision, evidence, limit, ask, in that order |

## Four-week preparation plan

A starting heuristic for someone who has completed the [curriculum](curriculum/README.md) or has equivalent field experience. Each week pairs one build task with one rehearsal; the artifacts accumulate into the list below.

| Week | Build | Rehearse |
| --- | --- | --- |
| 1 | Capstone trace, responsibility matrix, pattern choice, first case set | Behavioral stories: seven moves, four lines each |
| 2 | Graders, judge calibration, first error-analysis pass | Two 45-minute design sessions with a peer, different patterns |
| 3 | Rollout plan, operating plan, security review, field report from one failure | Two role-play scenes: scoping call and saying no |
| 4 | Clean the repository; write the limits section and the readout | Evidence deep dive on your own pack; one full timed design session |

If a week slips, drop the second rehearsal rather than the build task; interviewers can probe a real artifact far more deeply than a rehearsed answer.

## What to bring

- A capstone from [module 07](curriculum/07-capstone.md) that runs from a clean checkout, with its responsibility matrix and system pattern documented.
- An [evaluation pack](../toolkit/evaluation-pack.md) for it: versioned case set, graders, judge agreement, per-stratum results, error-analysis counts, regression cases.
- A [field report](../toolkit/field-report.md) that turns one failure into a reproducible case with frequency, impact, and a proposed owner.
- An [executive readout](../toolkit/executive-readout.md) of one page: decision, evidence, limits, ask.
- Working definitions of the terms you will use; see the [glossary](glossary.md).

Bring them as links you can open in the session, not as slides. An interviewer who can see the case set and the failure taxonomy asks better questions, and those are where your evidence pays off.
