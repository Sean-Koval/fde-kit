# Business case

## Purpose

Make an investment, continuation, or expansion decision with transparent assumptions about measurable workflow impact, delivery and operating cost, risk, ownership, and the evidence still required.

## Timing

Use in [Frame](../stages/02-frame/README.md) to agree on a value hypothesis; refresh in [Deploy](../stages/05-deploy/README.md), [Enable](../stages/06-enable/README.md), and [Expand](../stages/07-expand/README.md) with measured evidence.

## Instructions

1. State the decision, scope, counterfactual, accountable sponsor, and affected workflow clearly.
2. Use source-backed baselines; separate measured values from assumptions and attach an owner and validation date to each assumption.
3. Quantify benefits and costs as ranges where uncertainty is material. Include review work, operations, controls, adoption, and change-management costs.
4. Record safety, policy, delivery, and adoption risks with mitigations, residual risk, and the owner accepting it.
5. Define a time-bound evidence gate that supports invest, continue, improve, pause, or return-to-Discover decisions.

## Expected output

A decision-ready record that connects a bounded investment to measurable impact, total cost, risk acceptance, and an evidence-based next action.

## Supported stages

- [Frame](../stages/02-frame/README.md)
- [Deploy](../stages/05-deploy/README.md)
- [Enable](../stages/06-enable/README.md)
- [Expand](../stages/07-expand/README.md)

## Template

```markdown
# Business case — [workflow or expansion]

## Decision summary

- **Decision requested:** [invest / continue / improve / pause / begin new discovery]
- **Executive decision owner:** [name and role]
- **Workflow and user scope:** [roles, volume, geography, inclusions, exclusions]
- **Counterfactual:** [what happens if the team does not invest]
- **Decision date and review date:** [YYYY-MM-DD; YYYY-MM-DD]
- **Recommended first investment:** [bounded scope, duration, and evidence goal]

## Baseline and value hypothesis

| Measure | Baseline value and period | Source and confidence | Target or expected range | Mechanism of change | Measurement owner |
| --- | --- | --- | --- | --- | --- |
| [cycle time, error rate, cost, revenue, risk, capacity, satisfaction] | [value] | [source; high/medium/low] | [range] | [why the workflow change affects it] | [name] |

## Benefits and costs

| Category | Calculation or assumption | Low / expected / high | Evidence or validation plan | Owner |
| --- | --- | --- | --- | --- |
| Benefit: capacity, cost, revenue, or risk reduction | [volume × effect × value] | [range] | [source or experiment] | [name] |
| Delivery cost | [people, integration, security, data, tooling] | [range] | [estimate source] | [name] |
| Operating cost | [model, infrastructure, support, review, monitoring] | [range] | [forecast and review cadence] | [name] |
| Adoption and change cost | [training, workflow change, communications, temporary coverage] | [range] | [plan] | [name] |
| Control and risk mitigation cost | [assessment, audit, approval, fallback] | [range] | [control owner input] | [name] |

## Assumptions, risks, and ownership

| Item | Type | Impact if wrong | Evidence or mitigation | Residual risk / decision | Accountable owner | Validate by |
| --- | --- | --- | --- | --- | --- | --- |
| [item] | [assumption/safety/policy/delivery/adoption] | [impact] | [test, control, or plan] | [accept, reduce, defer, or stop] | [name] | [date] |

## Evidence gate and decision rule

| Gate | Evidence required | Threshold or comparison | Decision owner | If met | If not met |
| --- | --- | --- | --- | --- | --- |
| [pilot, rollout, or outcome review] | [measured outcome, adoption, quality, safety, operating cost] | [target or baseline comparison] | [name] | [invest, continue, or expand] | [improve, pause, or return to Discover] |

## Approval record

| Approver | Decision | Evidence reviewed | Date | Conditions or follow-ups |
| --- | --- | --- | --- | --- |
| [business, technical, finance, risk/control owner] | [approve/decline/conditional] | [links or IDs] | [YYYY-MM-DD] | [conditions] |
```

## Completion checks

- [ ] The decision, counterfactual, scope, decision owner, and first investment are explicit.
- [ ] Baselines, benefits, and costs cite evidence or identify assumptions, confidence, owners, and validation dates.
- [ ] Safety, policy, delivery, adoption, and operating risks have mitigations and accountable risk owners.
- [ ] A measurable evidence gate defines what will cause investment, continuation, improvement, pause, or re-entry to Discover.
