# Glossary

Terms the kit uses in its own sense, in alphabetical order. Each entry gives the working definition and links the page that owns the idea; read that page for the method. Where a term is defined in ordinary engineering usage, the entry states only what the kit adds. Numeric rules mentioned here are starting heuristics, not industry standards, and are labeled as such on their owning pages.

**Abstention.** The system's explicit output that it cannot decide: a schema value with a reason code, produced when evidence is missing, conflicting, low-confidence, or out of policy, and routed to a review path. An abstention the schema does not allow becomes an invented value. Owner: [Human, software, and AI system design](../skills/ai-system-design.md); the output contract is in [Context engineering](../skills/context-engineering.md).

**Accountable owner.** The named person who answers for a responsibility's outcome and its failure behavior. Every consequential row in a responsibility matrix has one; "the AI" or "the system" is never an accountable owner. Owner: [Responsibility matrix](../toolkit/responsibility-matrix.md).

**Adoption.** Operators choosing the workflow for real work, trusting its review path, and able to say when not to use it; measured by use on eligible cases, not by logins or training completion. Owner: [Adoption, operations, and product feedback](../skills/adoption-and-feedback.md).

**Agent loop.** The orchestration shape in which the model selects the next tool until a stop condition, as opposed to a fixed workflow or a workflow with model-chosen branches. Used only when the path cannot be enumerated and every consequential action is gated. Owner: [Designing tool-using agents](../skills/agent-and-tool-design.md).

**Approval point.** A pause in a workflow or agent loop where a person sees the proposed action, the evidence behind it, and its reversibility, then decides; state is persisted so the loop resumes without rerunning. Owner: [Designing tool-using agents](../skills/agent-and-tool-design.md).

**Autonomy gates (Observe, Assist, Shadow, Approve, Bounded autonomy).** The ordered release states of a rollout plan. Observe measures the baseline with no AI effect; Assist drafts while the operator decides; Shadow processes live cases without changing outcomes; Approve lets AI propose bounded actions that a person approves; Bounded autonomy lets AI act within monitored limits. Each gate has entry evidence, promotion criteria, a hold or rollback trigger, and a decision owner. Owner: [Rollout plan](../toolkit/rollout-plan.md).

**Baseline.** The measured current-state value of an outcome, with its source, period, and selection method, captured before any AI effect. A sponsor's estimate is a claim, not a baseline. Owner: [Workflow trace](../toolkit/workflow-trace.md); reused by the [business case](../toolkit/business-case.md).

**Boundary.** The agreed division of a workflow into what AI may interpret or recommend, what deterministic software enforces, and what accountable humans decide, together with the failure and recovery behavior at each edge. Owner: [Human, software, and AI system design](../skills/ai-system-design.md).

**Business case.** The decision record that connects a bounded investment to a source-backed baseline, benefit and cost ranges, risk acceptance, and a time-bound evidence gate. It values released capacity as capacity, not as cash savings, unless a cash change is measured. Owner: [Business case](../toolkit/business-case.md).

**Case set.** A versioned collection of real or realistic inputs with expected outcomes, required evidence, and permitted human involvement, stratified by workflow segment and exception type, with adversarial and valid-abstain cases and a held-out slice. Owner: [Grader design and error analysis](../skills/eval-engineering.md); recorded in the [evaluation pack](../toolkit/evaluation-pack.md).

**Citation and grounding.** Grounding is the requirement that every produced value or answer be tied to evidence the system was given; a citation is the pointer (source span, record identifier, passage) that makes the tie checkable in code. Owner: [Retrieval and grounding](../skills/retrieval-and-grounding.md).

**Context window and context engineering.** The context window is everything a model call receives; context engineering is assembling it deliberately from named layers (stable instructions, task, labeled evidence, examples, history, output contract) with a token budget and provenance per layer. Owner: [Context engineering](../skills/context-engineering.md).

**Correction rate.** The share of AI-produced outputs an operator changed before accepting, computed over assisted cases. It is the online mirror of offline correctness graders and a promotion or hold signal. Owner: [Grader design and error analysis](../skills/eval-engineering.md), section on online signals; used in the [worked example](../examples/invoice-intake-ai/README.md).

**Day 2.** Operation after launch: named business, technical, and risk/control owners, monitoring of workflow outcomes rather than uptime, incident response, change control, and a learning loop. Day 2 ownership is designed before Day 1. Owner: [Operating plan](../toolkit/operating-plan.md).

**Deterministic control.** A rule, permission check, schema validation, duplicate check, or state transition implemented in code so that it holds every time. Policy that must always hold is a deterministic control, never a prompt instruction. Owner: [Responsibility matrix](../toolkit/responsibility-matrix.md).

**Drift.** A change over time in input distribution, model behavior, corpus content, or operator behavior that moves quality away from what the evaluation established, detected by monitored signals with thresholds and owners. Owner: [Production readiness](../skills/production-readiness.md).

**Entitlement-filtered retrieval.** Retrieval that applies the requesting user's permissions at query time so the model never receives a passage the user may not see. A prompt instruction not to reveal restricted content is not an access control. Owner: [Retrieval and grounding](../skills/retrieval-and-grounding.md).

**Error analysis.** The loop of running the case set, reading failures one by one, building a taxonomy of causes from what was read, counting by cause, fixing the largest cause in the layer where it lives, and adding the motivating cases to the regression set. Owner: [Grader design and error analysis](../skills/eval-engineering.md).

**Evaluation pack.** The versioned release record: system under test, case-set version, graders and their versions, thresholds with owners, per-stratum results, failure analysis, and the promote, hold, or roll back decision. Owner: [Evaluation pack](../toolkit/evaluation-pack.md).

**Evidence gate.** A predeclared measure, threshold, owner, and review date that decides whether work advances, holds, narrows, or returns to an earlier stage. Any gate must be able to say stop. Owner: [Opportunity scorecard](../toolkit/opportunity-scorecard.md); also in the [business case](../toolkit/business-case.md) and [pilot charter](../toolkit/pilot-charter.md).

**Executive readout.** A one-page, decision-first communication to a sponsor: the decision needed, the evidence with baseline and uncertainty, the limits, and the ask. Owner: [Executive readout](../toolkit/executive-readout.md); technique in [Executive communication](../skills/executive-communication.md).

**Field report.** A reproducible package sent upstream to product, research, or platform owners: a repeated failure or missing capability with frequency, impact, traces, evaluation cases, and the current workaround. Owner: [Field report](../toolkit/field-report.md).

**First wedge.** The smallest workflow slice that can create and measure value under an accountable owner, with written exclusions. The LumenPeak wedge was English-language, USD, PDF invoices with an existing purchase order, in one business unit. Owner: [Workflow discovery](../skills/workflow-discovery.md); recorded in the [pilot charter](../toolkit/pilot-charter.md).

**Grader.** A reproducible procedure that scores a case: deterministic (exact match, schema validity, rule outcome, citation existence), programmatic assertion on a trace, human rubric label, or model-graded judge. The cheapest valid grader is chosen first. Owner: [Grader design and error analysis](../skills/eval-engineering.md).

**Judge (model-graded).** A grader in which a model scores an output against a rubric or reference. Valid only when its agreement with human labels has been measured and is reported beside every metric it produces, with position, length, and self-preference biases corrected. Owner: [Grader design and error analysis](../skills/eval-engineering.md).

**Kill switch.** A rehearsed, single action that disables the AI path, routes new work to the existing manual process, preserves the trace, and restores the last safe state; timed during rehearsal and owned by name. Owner: [Operating plan](../toolkit/operating-plan.md); rehearsed under the [rollout plan](../toolkit/rollout-plan.md).

**Least fragile owner.** The rule for assigning a responsibility: AI for bounded interpretation or recommendation, deterministic software for rules, permissions, and state changes, accountable humans for ambiguity, exceptions, and costly or irreversible decisions. Owner: [Human, software, and AI system design](../skills/ai-system-design.md).

**Lifecycle stages (Discover, Frame, Design, Build, Deploy, Enable, Expand).** The seven-stage engagement spine. Discover observes the work and its pain; Frame agrees the problem, measures, scope, and decision rule; Design chooses a testable approach and boundary; Build proves the increment against the case set; Deploy lands it through autonomy gates; Enable transfers Day 2 ownership and measures adoption; Expand decides the next investment from measured value. Evidence can send work back to an earlier stage. Owner: [Engagement lifecycle](engagement-lifecycle.md); operational detail in the [stage playbook](../stages/README.md).

**Matched sample.** A predeclared set of pilot cases paired one-to-one with baseline cases from the same strata, so that a mean difference and its confidence interval, rather than a difference of medians, become the annualization basis. Owner: [Worked example](../examples/invoice-intake-ai/README.md); predeclared in the [pilot charter](../toolkit/pilot-charter.md).

**Operating plan.** The owner-approved contract for Day 2: ownership with backups, operating signals with thresholds and first responses, an incident runbook, change control, and review cadence. Owner: [Operating plan](../toolkit/operating-plan.md).

**Opportunity scorecard.** A comparison of candidate workflows on impact, measurability, AI and delivery fit, operational readiness, and risk manageability, each score citing evidence, ending in a named owner's decision to advance, investigate, defer, or enable locally. Owner: [Opportunity scorecard](../toolkit/opportunity-scorecard.md).

**Output contract.** The schema a model call must satisfy: enumerated decisions, required fields, a citation per extracted value, and an explicit abstain value, validated in code after every call. Owner: [Context engineering](../skills/context-engineering.md).

**Permission tier.** The classification of a tool as read-only, reversible write, or irreversible and high consequence, which fixes how it executes (automatic, with approval, or never) and which credentials it carries. A tool result can never raise a tier. Owner: [Designing tool-using agents](../skills/agent-and-tool-design.md).

**Pilot charter.** The agreement, signed before pilot work starts, of the outcome hypothesis, first wedge and exclusions, cohort, baselines and targets, predeclared success and stop criteria and analysis method, prerequisites, owners, timeline, end states, and what the pilot does not prove. Owner: [Pilot charter](../toolkit/pilot-charter.md).

**Prompt injection (direct and indirect).** Direct injection is instruction text supplied by the user of the system; indirect injection is instruction text carried inside retrieved documents or tool results. Both are mitigated by treating evidence as data, validating outputs, and authorizing tool calls outside the model, never by a prompt alone. Owner: [AI security and governance review](../toolkit/ai-security-review.md); context handling in [Context engineering](../skills/context-engineering.md).

**Regression set.** The subset of the case set built from validated production failures and near misses, rerun before any change to model, prompt, retrieval, policy, or integration ships. Owner: [Grader design and error analysis](../skills/eval-engineering.md); maintained through the [evaluation pack](../toolkit/evaluation-pack.md).

**Responsibility matrix.** The boundary contract: for each responsibility (interpret, validate, decide, act, recover), the AI role, software role, system of record, human role, required evidence, controls, escalation trigger, failure behavior, and accountable owner, approved by the three owners. Owner: [Responsibility matrix](../toolkit/responsibility-matrix.md).

**Retrieval.** Bringing selected passages from a corpus into the context window at query time, chosen over long context or tuning when the corpus changes faster than a model could be retrained and every answer must be traceable and entitlement-filtered. Retrieval quality is graded separately from generation. Owner: [Retrieval and grounding](../skills/retrieval-and-grounding.md).

**Review burden.** The human time and queue load an AI path adds or removes, measured by time study or trace; a promotion criterion at the Assist gate and a hold trigger thereafter. Owner: [Rollout plan](../toolkit/rollout-plan.md).

**Rollback and safe state.** Rollback is the rehearsed return to a known safe state: the prior version, the disabled automation, or the existing manual path, with work preserved and users told. The safe state is named per gate and owned by name. Owner: [Rollout plan](../toolkit/rollout-plan.md).

**Rollout plan.** The staged release record: release authority, cohort, scope and exclusions, the gate plan through the autonomy gates, monitoring signals with baselines and owners, and the rollback rehearsal. Owner: [Rollout plan](../toolkit/rollout-plan.md).

**Said versus shown.** The discovery discipline of recording what an interviewee stated and what was observed on a screen or record in separate columns; only the second enters the workflow trace as evidence. Owner: [Discovery interviewing](../skills/discovery-interviewing.md); captured in the [discovery interview guide](../toolkit/discovery-interview-guide.md).

**Stakeholder map.** The record of who owns a system, budget, control, user group, or approval in the workflow's path, with decision rights, incentives, risk posture, who can stop the work, an escalation path, and an engagement owner per stakeholder. Owner: [Stakeholder map](../toolkit/stakeholder-map.md).

**Stopping rule and budget.** The per-case limits on steps, tokens, time, and cost for an agent loop, plus stuck detection; a breach is a graceful exit that writes the trace and returns the case to the queue with a reason. Owner: [Designing tool-using agents](../skills/agent-and-tool-design.md).

**System of record.** The system that holds authoritative state for a responsibility (the enterprise resource planning system for vendor and purchase-order state, for example). The model receives a view of it and never replaces it; deterministic checks query it. Owner: [Responsibility matrix](../toolkit/responsibility-matrix.md); identified in the [workflow trace](../toolkit/workflow-trace.md).

**System pattern.** A named boundary and control shape for placing a model in a workflow: assist; extract, validate, act; retrieval-grounded assistant; tool-using agent; batch classification and routing. Choose the least autonomous pattern that meets the outcome. Owner: [AI system patterns](system-patterns.md).

**Three owners.** The business outcome owner, technical service owner, and risk/control owner who approve the boundary, the release, and Day 2, each with a backup. Owner: [Operating plan](../toolkit/operating-plan.md); named first in the [responsibility matrix](../toolkit/responsibility-matrix.md).

**Tool contract.** A tool's documentation for the model: purpose, when to use it, typed inputs and outputs, structured error cases, idempotency, and what it must not be used for, tested in isolation before any loop runs. Owner: [Designing tool-using agents](../skills/agent-and-tool-design.md).

**Trace.** The per-step runtime record of a case: context sent, tool selected, arguments, result, latency, cost, permission decision, keyed by case identifier and system version, so that any case can be replayed and its trajectory graded. Owner: [Production readiness](../skills/production-readiness.md); trajectory grading in [Grader design and error analysis](../skills/eval-engineering.md).

**Workflow trace.** A discovery artifact, distinct from a runtime trace: one observed case recorded from trigger to outcome with steps, systems, actors, evidence, active time and waits, exceptions, and audit records, validated by the operator and a second source. Owner: [Workflow trace](../toolkit/workflow-trace.md).
