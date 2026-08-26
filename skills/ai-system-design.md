# Human, software, and AI system design

## Relevance

Use this capability to design an AI workflow as a controlled system of people, deterministic software, and AI—not as a model placed at the center of every decision. It is useful when the team must decide what the system may interpret, validate, recommend, or act on; what must remain deterministic or human-owned; and how the workflow recovers when evidence, permissions, or confidence are insufficient.

## Timing

Begin in [Design](../stages/03-design/README.md), turn the boundary into working integration and controls in [Build](../stages/04-build/README.md), and confirm it before production use in [Deploy](../stages/05-deploy/README.md). Revisit it in [Enable](../stages/06-enable/README.md) when operating evidence changes the safe boundary.

## Technique

1. Start with a validated workflow outcome and decompose it into interpretation, validation, decision, action, and recovery responsibilities.
2. Identify authoritative state, required evidence, permissions, and non-negotiable policy checks for each responsibility.
3. Assign the least fragile owner: AI for bounded interpretation or recommendation; deterministic software for rules, permissions, state changes, and repeatable checks; accountable humans for ambiguity, policy exceptions, and costly or irreversible decisions.
4. Define an explicit abstention or escalation trigger for missing, conflicting, low-confidence, or out-of-policy evidence. Design the review queue and manual fallback before increasing autonomy.
5. Make actions observable and recoverable: record inputs, evidence, decision, approval, tool result, and the safe rollback or compensating action.
6. Review the boundary with business, technical, and risk/control owners. Update it when integrations, policy, or autonomy limits change.

## Examples

### Good pattern

For invoice intake, AI extracts a vendor name, total, and purchase-order candidate with cited source spans. Deterministic software checks supplier identity, duplicate status, purchase-order existence, amount limits, and caller permission in the ERP. An AP analyst resolves conflicting values; an authorized approver accepts an exception; the integration records the result and can leave the invoice in the existing review queue. The team can explain why an action occurred and safely stop it.

### Weak pattern

"The agent reads the invoice and posts it to the ERP." This collapses interpretation, policy validation, authorization, and action into one opaque step. It provides no authoritative state, evidence requirement, exception path, permission boundary, or recovery behavior.

## Practice

Pick a workflow step that changes a record or commits a decision. Split it into interpretation, validation, decision, action, and recovery. For each part, assign an owner and state the required evidence, escalation trigger, and failure behavior. Then ask what would happen if the source document conflicts with the system of record.

## Self-assessment

- Does every consequential action have an accountable human owner, an authorized system path, and an auditable state change?
- Are deterministic checks and permissions explicit rather than described as AI judgment?
- Is there a usable abstention and review path for uncertainty, conflict, or policy breach?
- Can the team state how to return to a safe state after a failed or harmful action?
- Have business, technical, and risk/control owners agreed to the boundary and its limits?

## Links

**Lifecycle stages:** [Design](../stages/03-design/README.md), [Build](../stages/04-build/README.md), [Deploy](../stages/05-deploy/README.md), [Enable](../stages/06-enable/README.md).

**Toolkit assets:** [Workflow trace](../toolkit/workflow-trace.md), [Responsibility matrix](../toolkit/responsibility-matrix.md), [Evaluation pack](../toolkit/evaluation-pack.md), [Rollout plan](../toolkit/rollout-plan.md).
