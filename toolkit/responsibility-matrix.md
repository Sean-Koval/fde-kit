# Responsibility matrix

## Purpose

Assign each workflow responsibility to AI, deterministic software, and accountable humans according to ambiguity, consequence, reversibility, and required evidence. This is a governance decision, not a model capability inventory.

## Timing

Use during [Design](../stages/03-design/README.md); maintain it through [Build](../stages/04-build/README.md) and [Deploy](../stages/05-deploy/README.md) when controls or integrations change.

## Instructions

1. Decompose the workflow into interpretation, validation, decision, action, and recovery responsibilities.
2. Assign the least fragile owner for each responsibility; do not assign an accountable or irreversible decision to AI without explicit limits and approval.
3. Specify required evidence, permissions, deterministic checks, human review triggers, and the system of record.
4. Define a safe failure behavior and recovery path for every automated or AI-assisted action.
5. Obtain approval from the business, technical, and risk/control owners before production use.

## Expected output

A reviewable boundary contract that makes ownership, controls, evidence, escalation, and rollback behavior explicit for the production workflow.

## Supported stages

- [Design](../stages/03-design/README.md)
- [Build](../stages/04-build/README.md)
- [Deploy](../stages/05-deploy/README.md)
- [Enable](../stages/06-enable/README.md)

## Template

```markdown
# Responsibility matrix — [workflow or increment]

## Boundary decision

- **Workflow outcome:** [business result]
- **Business outcome owner:** [name and role]
- **Technical service owner:** [name and role]
- **Risk/control owner:** [name and role]
- **Approved scope and version:** [scope, version, date]
- **Default safety rule:** AI proposes; deterministic software constrains; accountable humans approve costly, novel, or irreversible decisions.

## Responsibility matrix

| Responsibility | AI role | Software role | System of record / authoritative state | Human role | Required evidence | Control and permission | Escalation trigger | Failure behavior / rollback | Accountable owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Interpret [input] | [extract/classify/recommend or none] | [schema parsing or none] | [source system and record ID] | [resolve ambiguity] | [source spans, record IDs] | [allowed sources] | [missing/conflicting evidence] | [abstain and queue review] | [name] |
| Validate [condition] | [semantic check or none] | [rule, range, duplicate, permission check] | [policy or transaction record] | [policy override] | [rule result and rationale] | [policy version] | [rule conflict or high consequence] | [block action; retain prior state] | [name] |
| Decide [route] | [recommendation and confidence] | [threshold routing] | [decision and approval record] | [accountable approval] | [inputs, rationale, approval] | [decision limits] | [low confidence or threshold breach] | [send to review queue] | [name] |
| Act [system change] | [bounded tool-call proposal or none] | [authorized API call and idempotency] | [authoritative application or ledger state] | [approve/perform sensitive action] | [request, response, audit ID] | [least privilege and allowlist] | [permission, policy, or rollback uncertainty] | [stop action; compensate or restore] | [name] |
| Recover [failure] | [summarize trace] | [retry, fallback, restore state] | [incident and restored-state record] | [incident command or exception decision] | [trace, incident record] | [kill switch] | [repeated failure or harm signal] | [disable automation; use manual path] | [name] |

## Approval and open decisions

| Decision | Evidence reviewed | Approver | Date | Status | Revisit trigger |
| --- | --- | --- | --- | --- | --- |
| [boundary, permission, or control] | [test, policy, trace, or review] | [name] | [YYYY-MM-DD] | [approved/open/rejected] | [change that requires review] |
```

## Completion checks

- [ ] Every consequential responsibility has an accountable human owner, not only an AI or system label.
- [ ] Each AI or automated action has evidence requirements, permission limits, escalation criteria, and a safe failure behavior.
- [ ] Deterministic validation and the system of record or authoritative state are named where state or policy must be enforced.
- [ ] Business, technical, and risk/control approvals are recorded or explicitly open before deployment.
