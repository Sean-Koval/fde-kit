# Evaluation pack

## Purpose

Turn representative workflow cases and production failures into release evidence. Evaluate the complete system outcome: correctness, evidence use, policy adherence, tool behavior, review burden, and business result.

## Timing

Start in [Design](../stages/03-design/README.md), execute during [Build](../stages/04-build/README.md), and use as a promotion gate during [Deploy](../stages/05-deploy/README.md) and [Enable](../stages/06-enable/README.md).

## Instructions

1. Assemble representative cases covering common work, costly exceptions, policy-sensitive cases, and known failure modes.
2. Define an expected workflow outcome and evidence requirements for each case; include valid abstention or escalation where appropriate.
3. Specify reproducible graders, thresholds, sample scope, and the owner who decides whether evidence is sufficient.
4. Classify every meaningful failure by likely cause and route it to a system, policy, data, or workflow change.
5. Add validated production failures to the regression set and rerun the pack before any relevant release.

## Expected output

A versioned evaluation record with release criteria, results, failure analysis, an accountable release decision, and a path to roll back or hold a change.

## Supported stages

- [Design](../stages/03-design/README.md)
- [Build](../stages/04-build/README.md)
- [Deploy](../stages/05-deploy/README.md)
- [Enable](../stages/06-enable/README.md)

## Template

```markdown
# Evaluation pack — [workflow] — [system version]

## Release decision

- **Decision:** [promote / hold / roll back]
- **Decision owner:** [name and role]
- **Evaluation date:** [YYYY-MM-DD]
- **System under test:** [model, prompt, retrieval, policy, integration, and application versions]
- **Scope:** [traffic, users, workflow state, and exclusions]
- **Rollback target and owner:** [last known safe version; name]

## Outcome criteria

| Criterion | Definition | Grader and evidence | Threshold | Failure handling | Owner |
| --- | --- | --- | --- | --- | --- |
| Correct workflow result | [what counts as correct] | [human rubric, deterministic check, or both] | [required result] | [hold, fix, or route review] | [name] |
| Evidence grounding | [required source/citation behavior] | [source-span or record check] | [required result] | [abstain or reject] | [name] |
| Policy and safety | [policy that must hold] | [policy test or control check] | [required result] | [block and escalate] | [name] |
| Review burden | [human time or queue load] | [time study or production trace] | [required result] | [hold promotion] | [name] |
| Operational behavior | [latency, tool error, cost, or availability] | [telemetry] | [required result] | [fallback or rollback] | [name] |

## Representative case set

| Case ID | Scenario and risk | Inputs and permitted data | Expected workflow outcome | Required evidence / rationale | Expected human involvement | Source and owner |
| --- | --- | --- | --- | --- | --- | --- |
| [ID] | [common, exception, costly, or adversarial] | [reference or fixture] | [result, abstention, or escalation] | [spans, records, policy] | [none/review/approval] | [source, owner] |

## Results and failure analysis

| Case ID | Result | Pass / fail | Failure taxonomy | Evidence | Corrective action | Regression added | Owner and due date |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [ID] | [observed outcome] | [pass/fail] | [model/data/tool/policy/integration/UX/process] | [trace, screenshot, log] | [specific change] | [yes/no] | [name, date] |

## Online monitoring and re-evaluation

| Signal | Baseline | Alert or review trigger | Response owner | Immediate safe action | Review cadence |
| --- | --- | --- | --- | --- | --- |
| [quality, abstention, review load, drift, latency, cost, tool errors] | [value and period] | [threshold or change] | [name] | [hold, fallback, disable, or queue review] | [cadence] |
```

## Completion checks

- [ ] Cases cover normal work, consequential exceptions, policy-sensitive cases, and known failures.
- [ ] Every case specifies a system outcome, required evidence, and valid human-review or abstention behavior.
- [ ] Thresholds, graders, system version, release decision, and rollback target have named owners.
- [ ] Failures are classified, assigned, and added to regression coverage when meaningful.
