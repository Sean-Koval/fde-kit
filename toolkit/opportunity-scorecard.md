# Opportunity scorecard

## Purpose

Choose a first workflow investment using comparable evidence about impact, AI and delivery fit, risk, and accountable ownership. Use it to make a prioritization decision, not to justify a preselected demo.

## Timing

Use during [Discover](../stages/01-discover/README.md) and [Frame](../stages/02-frame/README.md), before committing delivery capacity or promising a production outcome.

## Instructions

1. Score each candidate workflow from evidence gathered from operators, system records, and the accountable owner.
2. Record the source, date, and confidence for every nontrivial score; distinguish observed facts from assumptions.
3. Identify safety, privacy, policy, integration, and adoption constraints before recommending a workflow.
4. Compare candidates and record a named decision owner’s choice: advance, investigate, defer, or enable locally.
5. Revisit the score when new discovery evidence invalidates an assumption.

## Expected output

A ranked, evidence-backed opportunity decision with a bounded first wedge, known risks, and an owner who accepts the next step.

## Supported stages

- [Discover](../stages/01-discover/README.md)
- [Frame](../stages/02-frame/README.md)
- [Expand](../stages/07-expand/README.md)

## Template

```markdown
# Opportunity scorecard — [workflow name]

## Decision

- **Decision:** [advance / investigate / defer / enable locally]
- **Decision owner:** [name and role]
- **Decision date:** [YYYY-MM-DD]
- **Recommended first wedge:** [smallest workflow slice that can create and measure value]
- **Why now:** [evidence-backed reason]

## Workflow and evidence

| Field | Entry |
| --- | --- |
| Users and outcome owner | [who performs the work; who owns the business result] |
| Current workflow | [trigger, key steps, handoffs, and systems] |
| Pain signal | [delay, cost, risk, error, lost revenue, or capacity constraint] |
| Baseline | [measure, value, period, and source] |
| Evidence reviewed | [links or identifiers for interviews, logs, cases, and reports] |
| Assumptions to test | [assumption, why it matters, and test] |

## Scoring

Score each criterion 1–5. These are starting heuristics for comparison, not industry standards.

| Criterion | Score | Evidence and rationale | Confidence | Owner |
| --- | ---: | --- | --- | --- |
| Workflow impact | [1–5] | [volume, consequence, and affected users] | [high/medium/low] | [name] |
| Measurability | [1–5] | [baseline and outcome signal available] | [high/medium/low] | [name] |
| AI and delivery fit | [1–5] | [messy interpretation, data access, integration feasibility] | [high/medium/low] | [name] |
| Operational readiness | [1–5] | [named owner, user access, support capacity] | [high/medium/low] | [name] |
| Risk manageability | [1–5] | [reversibility, controls, review path] | [high/medium/low] | [name] |

## Constraints and safeguards

| Area | Constraint or risk | Required control or evidence | Accountable owner | Open decision |
| --- | --- | --- | --- | --- |
| Data and privacy | [classification, residency, retention] | [approved data path or review] | [name] | [decision] |
| Safety and policy | [harm, policy, or financial consequence] | [human review, limits, or policy check] | [name] | [decision] |
| Integration | [system, permission, dependency, failure mode] | [contract or feasibility proof] | [name] | [decision] |
| Adoption | [role, workflow change, training, incentive] | [pilot commitment or observation plan] | [name] | [decision] |

## Next evidence gate

- **Hypothesis:** [what the first wedge must prove]
- **Measure and threshold:** [measure, target or comparison, time window]
- **Evidence owner:** [name]
- **Review date:** [YYYY-MM-DD]
- **If the gate fails:** [investigate, reframe, defer, or return to Discover]
```

## Completion checks

- [ ] The workflow, affected users, business outcome owner, and first wedge are named.
- [ ] Every score cites evidence or is explicitly marked as an assumption with a test.
- [ ] Safety, data, integration, and adoption constraints have accountable owners.
- [ ] The decision, decision owner, next evidence gate, and failure path are recorded.
