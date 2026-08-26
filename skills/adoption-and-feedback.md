# Adoption, operations, and product feedback

## Relevance

Use this capability to make an AI workflow durable after release: people can use it, owners can operate it, the team can learn from production, and further investment is justified by measured value. It is useful when a release is ready for broader use, when operating ownership is moving to the customer team, or when feedback and outcomes must decide whether to improve, pause, or expand.

## Timing

Prepare ownership and support in [Deploy](../stages/05-deploy/README.md), establish durable operating practice in [Enable](../stages/06-enable/README.md), and use measured evidence to choose the next investment in [Expand](../stages/07-expand/README.md).

## Technique

1. Define the adoption behavior that creates the intended workflow outcome. Segment users by role, decision, access, and support need; training is not complete when a launch message is sent.
2. Transfer business outcome, technical service, and risk/control ownership with backups, support routes, escalation paths, and a known manual fallback.
3. Observe both service health and workflow reality: quality, abstention, review load, drift, latency, cost, tool errors, safety, and the business outcome. Link each signal to an owner and first response.
4. Turn user feedback and production traces into a regularly reviewed, evidence-backed improvement queue. Separate defects, policy issues, usability barriers, data gaps, and requests for new workflow scope.
5. Use controlled change: evaluate and approve changes to models, prompts, policy, integrations, data, or autonomy limits; retain a rollback target and communicate effects to affected users.
6. Refresh the business case with measured value, total operating cost, residual risk, and support capacity. Decide to continue, improve, pause, or begin a new Discover cycle before calling something an expansion.

## Examples

### Good pattern

After invoice assist launches, AP supervisors own the workflow outcome, platform operations owns service response, and compliance owns exceptions to financial policy. A weekly review examines correction rate, review queue age, manual fallback use, and on-time processing by cohort. Operators can submit annotated feedback from the review queue; recurring missing-PO cases become a design item, while a request to handle vendor onboarding starts a separate discovery scorecard. The sponsor sees a monthly business-case update before approving a wider rollout.

### Weak pattern

"Training is complete and the dashboard is green, so scale it to every finance workflow." No owner is responsible for user adoption or control outcomes, the dashboard measures only uptime, feedback is not triaged, costs are unknown, and the proposed expansion has not been discovered or framed.

## Practice

Choose a released workflow. Define a 30-day operating review with one user behavior, one quality or control signal, one service signal, one business-outcome signal, and the accountable owner for each. Add one feedback item that should be fixed within the existing scope and one request that must re-enter Discover. State the decision rule for continuing, improving, pausing, or expanding.

## Self-assessment

- Are business, technical, and risk/control owners named with backups and a usable escalation route?
- Can users obtain role-specific help and safely use a manual fallback when the workflow is unavailable or uncertain?
- Do monitoring and reviews include workflow quality, review burden, safety, cost, and business impact—not merely uptime?
- Is feedback classified and routed to the correct lifecycle decision rather than treated as a generic backlog?
- Does any expansion decision use measured value, residual risk, operating capacity, and a refreshed opportunity decision?

## Links

**Lifecycle stages:** [Deploy](../stages/05-deploy/README.md), [Enable](../stages/06-enable/README.md), [Expand](../stages/07-expand/README.md).

**Toolkit assets:** [Evaluation pack](../toolkit/evaluation-pack.md), [Rollout plan](../toolkit/rollout-plan.md), [Operating plan](../toolkit/operating-plan.md), [Business case](../toolkit/business-case.md), [Opportunity scorecard](../toolkit/opportunity-scorecard.md).
