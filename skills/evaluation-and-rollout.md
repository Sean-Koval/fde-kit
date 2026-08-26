# Evaluation and staged rollout

## Relevance

Use this capability to turn claims that an AI workflow is ready into repeatable evidence and a controlled production decision. It is useful when a prototype appears promising, when a model, prompt, policy, retrieval source, or integration changes, and when a team is deciding whether to hold, promote, reduce, or expand autonomy.

## Timing

Define the evidence approach in [Design](../stages/03-design/README.md), run and improve it in [Build](../stages/04-build/README.md), use it as a promotion gate in [Deploy](../stages/05-deploy/README.md), and keep it current through [Enable](../stages/06-enable/README.md).

## Technique

1. Build a representative case set that includes common work, costly exceptions, policy-sensitive cases, and known production failures. State how the sample was selected and version it.
2. Define the expected end-to-end workflow result for each case, including acceptable abstention or escalation. Evaluate evidence use, policy adherence, tool behavior, review burden, and business outcome—not only model output.
3. Choose reproducible graders and thresholds. Name the release decision owner, the rollback target, and the response when a threshold is missed.
4. Classify meaningful failures by likely cause: data, retrieval, model behavior, prompt, deterministic rule, integration, policy, or workflow design. Fix the cause and add validated production failures to the regression set.
5. Release through the safest useful state: observe, assist, shadow, approve, then bounded autonomy. Advance only when quality, controls, review load, adoption, and business signals support it.
6. Rehearse rollback and communicate the cohort, support route, and decision criteria before a gate opens. Return to Frame or Design when evidence invalidates the underlying assumptions.

## Examples

### Good pattern

An invoice-assist release uses a versioned set of invoices that includes clean, duplicate, missing-PO, and policy-exception cases. The evaluation checks correct extracted fields with source evidence, ERP rule outcomes, and whether the system queues uncertain cases. The first cohort sees drafts only; promotion requires correction rate and review time to meet agreed thresholds with no policy breach. A duplicate-detection regression becomes a permanent case after a live near miss.

### Weak pattern

"The model scored 92% on a sample, so enable auto-posting." The sample method, case version, workflow criterion, reviewer burden, permission checks, threshold owner, and rollback action are unknown. The score cannot justify a production autonomy decision.

## Practice

For a proposed AI-assisted workflow, define four cases: a common case, a costly exception, a policy-sensitive case, and an uncertainty case. For each, state the expected end-to-end result and the evidence that proves it. Choose an initial rollout state, one promotion criterion, one hold or rollback trigger, and the owner who makes that decision.

## Self-assessment

- Can another team rerun the evaluation and obtain a comparable result from the recorded cases, graders, and system version?
- Do the cases test the complete workflow, including valid abstention, deterministic controls, and tool effects?
- Are promotion, hold, and rollback criteria objective enough for the named decision owner to use?
- Does the initial rollout match the consequence and reversibility of the action?
- Are live failures routed into a versioned learning loop instead of being handled as one-off incidents?

## Links

**Lifecycle stages:** [Design](../stages/03-design/README.md), [Build](../stages/04-build/README.md), [Deploy](../stages/05-deploy/README.md), [Enable](../stages/06-enable/README.md).

**Toolkit assets:** [Responsibility matrix](../toolkit/responsibility-matrix.md), [Evaluation pack](../toolkit/evaluation-pack.md), [Rollout plan](../toolkit/rollout-plan.md), [Operating plan](../toolkit/operating-plan.md).
