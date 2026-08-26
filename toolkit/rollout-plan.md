# Rollout plan

## Purpose

Release a workflow change through explicit autonomy and readiness gates. Define who receives it, what evidence permits promotion, how the team observes impact, and how it returns to a safe state.

## Timing

Draft during [Build](../stages/04-build/README.md); approve and execute during [Deploy](../stages/05-deploy/README.md); update with adoption evidence during [Enable](../stages/06-enable/README.md).

## Instructions

1. Choose the safest useful starting state: observe, assist, shadow, approve, or bounded autonomy.
2. Specify the user cohort, workflow scope, permissions, control owner, support route, and communication for each gate.
3. Define health, quality, review-burden, and business-outcome signals with baseline, threshold, and response owner.
4. Set objective promotion, hold, and rollback criteria; rehearse the rollback path before exposing consequential actions.
5. Record the decision at each gate and return to an earlier lifecycle stage if evidence invalidates the frame or design.

## Expected output

A staged release record that makes risk limits, evidence gates, ownership, support, communication, and rollback executable.

## Supported stages

- [Build](../stages/04-build/README.md)
- [Deploy](../stages/05-deploy/README.md)
- [Enable](../stages/06-enable/README.md)

## Template

```markdown
# Rollout plan — [workflow] — [release/version]

## Release authority

- **Business outcome owner:** [name and role]
- **Technical release owner:** [name and role]
- **Risk/control approver:** [name and role]
- **First user cohort:** [roles, size, location, and selection rationale]
- **Workflow scope and exclusions:** [included steps, data, permissions, and explicit exclusions]
- **Support and communication route:** [channel, response expectation, user message owner]
- **Rollback owner and safe state:** [name; feature flag, manual path, or prior version]

## Gate plan

| Gate | User and system behavior | Entry evidence | Promotion criteria | Hold or rollback trigger | Immediate action | Decision owner |
| --- | --- | --- | --- | --- | --- | --- |
| Observe | [baseline only; no AI outcome affects work] | [workflow and owner known] | [baseline is credible] | [missing evidence or control] | [extend observation] | [name] |
| Assist | [AI drafts/extracts; operator decides] | [offline quality and training complete] | [utility exceeds added review burden] | [harm, policy issue, or unacceptable review load] | [disable assist; use current workflow] | [name] |
| Shadow | [AI processes live cases without changing outcome] | [assist evidence and traceability] | [field results agree with evaluation] | [material mismatch or unsafe output] | [stop shadow processing] | [name] |
| Approve | [AI proposes bounded action; human approves exceptions or all actions] | [controls and approval path tested] | [quality, controls, and adoption targets met] | [approval escape, policy breach, or incident] | [require manual approval] | [name] |
| Bounded autonomy | [AI acts only within approved limits] | [residual risk accepted] | [sustained monitored evidence] | [threshold breach, drift, or rollback uncertainty] | [disable automation; queue work] | [name] |

## Monitoring and response

| Signal | Baseline | Gate threshold | Check cadence | Response owner | Response and communication |
| --- | --- | --- | --- | --- | --- |
| [quality] | [value] | [threshold] | [cadence] | [name] | [hold/promote/rollback message] |
| [review burden] | [value] | [threshold] | [cadence] | [name] | [hold/promote/rollback message] |
| [health or tool errors] | [value] | [threshold] | [cadence] | [name] | [fallback or incident route] |
| [business outcome] | [value] | [threshold] | [cadence] | [name] | [decision review] |

## Rollback rehearsal

- **Trigger tested:** [condition]
- **Steps tested:** [disable, route work, restore state, notify users, preserve evidence]
- **Result and evidence:** [date, trace, owner]
- **Gaps and remediation owner:** [gap, name, date]
```

## Completion checks

- [ ] The release cohort, scope, permissions, support route, and three accountable owners are explicit.
- [ ] Each autonomy gate has entry evidence, promotion criteria, hold or rollback triggers, and a decision owner.
- [ ] Health, quality, review burden, and business outcome signals have baselines and response owners.
- [ ] A rollback to a known safe state has been rehearsed and evidence is recorded.
