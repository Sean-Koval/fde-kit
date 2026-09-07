# Module 05: Production, rollout, and Day 2

## Outcome

You can land a system that has release evidence: a rollout that advances autonomy only through gates with objective criteria, monitoring that measures workflow outcomes rather than uptime, an operating plan with named Day 2 owners and first responses, and a rollback rehearsed with evidence before any consequential action is exposed. The module produces three artifacts a customer's operations and risk owners could execute without you.

## Prerequisites

- The evaluation pack and release decision from [module 04](04-evaluation-engineering.md).
- The responsibility matrix and security review from module 03; the rollback path must return the system to the safe state those documents defined.
- A tracing or logging setup, if you have model access, so the rehearsal can produce real evidence.

## Study

Read in this order.

1. [Production readiness for LLM systems](../../skills/production-readiness.md): tracing, versioning, guardrails, resilience, cost and latency budgets, drift, change control, and incident response; the checklist of what breaks after the demo.
2. [Adoption, operations, and product feedback](../../skills/adoption-and-feedback.md): Day 2 ownership across business, technical, and risk roles; monitoring that watches workflow reality; and the rule that expansion requests re-enter Discover.
3. [Rollout plan](../../toolkit/rollout-plan.md): the gate table (observe, assist, shadow, approve, bounded autonomy) with entry evidence, promotion criteria, hold triggers, and a rollback rehearsal section.
4. [Operating plan](../../toolkit/operating-plan.md): owners with backups, triggers with first responses, support routes, cadence, and change control.
5. [AI security and governance review](../../toolkit/ai-security-review.md): reread the logging, retention, and incident-response items; your operating plan must satisfy them.
6. [Deploy](../../stages/05-deploy/README.md) and [Enable](../../stages/06-enable/README.md) stage pages: exit criteria and the failure modes of launching without support routes and of declaring adoption from a launch message.
7. Sections 5 and 6 of the [invoice-intake example](../../examples/invoice-intake-ai/README.md): gates with dates and decisions, a kill switch rehearsed in seven minutes with no lost case, Day 2 owners with backups, and a hold on bounded autonomy despite passing metrics.

Where to practice with real tooling: add tracing to your module 03 system so each run records inputs, evidence, output, version, and any tool result. Then rehearse the rollback for real: flip the disable path, route the next case to the fallback, and pull the trace that proves it.

## Exercise

Produce three artifacts for the module 04 system.

1. **Rollout plan.** Choose the safest useful starting state and justify it from the consequence and reversibility of the action. For each gate, state the cohort, the system behavior, entry evidence, promotion criteria drawn from your evaluation thresholds, hold or rollback triggers, the immediate action, and the decision owner. Define at least four signals (quality, review burden, health or tool errors, business outcome) with a baseline, a threshold, a check cadence, and a response owner. As a starting heuristic, not an industry standard, a gate without a named decision owner and a dated review is a wish, not a gate.
2. **Operating plan.** Name the primary and backup owner for business outcome and adoption, technical service and rollback, risk and controls, quality and review burden, and cost. For each, state the trigger and the first response. Add the support route with hours, the review cadence, the change-control rule for model, prompt, retrieval, policy, integration, and autonomy changes, and the learning loop that turns production failures into regression cases.
3. **Rollback rehearsal script.** Step by step: the trigger being simulated, who executes each step, the disable mechanism, where in-flight and new work goes, how prior state is restored, who is notified with what message, and how evidence is preserved. Then write the evidence the rehearsal would produce: trace entries, queue state before and after, timestamps, elapsed time. With a running system, execute the script and attach the real evidence; without one, mark the evidence as expected and state what would make it real.

Write for the people who will hold the pager, not for the sponsor. If a step says "the team investigates", name the person and the first thing they look at.

## Assessment

| Criterion | Developing | Solid | Strong |
| --- | --- | --- | --- |
| Gate design | Gates are calendar milestones or a single launch | Each gate has entry evidence, promotion criteria, hold triggers, and a decision owner | Starting state is justified from consequence and reversibility; promotion criteria trace to specific evaluation thresholds |
| Signal quality | Uptime and error rate only | Quality, review burden, health, and business outcome each have a baseline and threshold | Every signal has a response owner, a first action, and a cadence; the plan says which signal fires first when things degrade |
| Day 2 ownership | "The customer will own it" | Primary and backup owners across business, technical, risk, quality, and cost | Owners have accepted in writing, and each trigger names a concrete first response rather than "review" |
| Rollback readiness | Rollback is described as possible | A written script with steps, owners, and safe state | Rehearsed with evidence (trace, queue state, elapsed time) or the exact evidence specified and marked expected |
| Change control | Changes ship when ready | Model, prompt, retrieval, policy, and integration changes require a rerun and an approval | Each change class names the evaluation cases it must rerun and the rollback target it keeps |

Solid on rollback readiness and Day 2 ownership is the minimum for module 06; the readout must be able to say who runs the system and how it stops.

## Next

[Module 06: Customer craft and communication](06-customer-craft.md) turns the evidence from modules 04 and 05 into an executive readout, an operator briefing, a field report, and responses to the two conversations every FDE eventually has.
