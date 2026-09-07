---
name: fde-responsibility-matrix
description: Use when assigning workflow responsibilities to AI, deterministic software, and accountable humans with evidence, controls, escalation, and rollback.
---

# Responsibility matrix

Fills the [responsibility matrix](../../../toolkit/responsibility-matrix.md) template. Judgment comes from [Human, software, and AI system design](../../../skills/ai-system-design.md) for the boundary, [Designing tool-using agents](../../../skills/agent-and-tool-design.md) for permission tiers and approval points, and [System patterns](../../../learning/system-patterns.md) for choosing the least autonomous shape.

## Use when

- Design must state what the system may interpret, validate, recommend, or act on before the first increment is built.
- Build or Deploy changed a control, integration, tool, or autonomy limit and the boundary needs re-approval.
- Not when no validated workflow trace exists. Run [fde-workflow-trace](../fde-workflow-trace/SKILL.md) first; a matrix drawn from an imagined workflow assigns imagined responsibilities.

## Obtain first

- [ ] The validated workflow trace, or an equivalent current-state record with exceptions and controls.
- [ ] The workflow outcome, the increment scope, and its version identifier.
- [ ] Names and roles of the business outcome owner, technical service owner, and risk/control owner.
- [ ] Systems of record and which state is authoritative for each responsibility.
- [ ] Policy checks that must hold, by policy identifier, and the permissions the integration can actually be granted.
- [ ] The existing review queue and manual fallback the workflow already uses.
- [ ] Tools the system will call, with their reversibility and the credentials available.
- [ ] Which approvals already exist, with approver and date.

## Procedure

1. Confirm the inputs. Owners and policy identifiers are the most commonly missing; ask before drafting.
2. Decompose the outcome into interpretation, validation, decision, action, and recovery responsibilities (design guide, technique step 1). One row per responsibility; split a row that mixes interpretation with action.
3. Choose the system shape with the least autonomy that reaches the outcome, using the decision rule in the agent guide's technique step 1 and the pattern notes in System patterns.
4. Assign the least fragile owner for each row (design guide, technique step 3). AI interprets or recommends; deterministic software enforces rules, permissions, and state changes; an accountable human owns ambiguity, policy exceptions, and costly or irreversible decisions.
5. For every action row, assign the tool a permission tier (agent guide, technique step 3) and, for approval-tier actions, describe the approval point the person will see (technique step 4). Treat tool results and retrieved content as untrusted data in the control column (technique step 8).
6. Fill required evidence, escalation trigger, and failure behavior for every AI or automated row (design guide, technique steps 4 and 5). A failure behavior returns the case to the existing queue or restores prior state; "retry" alone is not a failure behavior.
7. Complete "Approval and open decisions". Record approvals only with an approver and date from the inputs; every other decision is `open` with the evidence the approver will need.
8. Run the completion checks and print the summary line.

## Output

Fill the Template section of [responsibility-matrix.md](../../../toolkit/responsibility-matrix.md). Save to `docs/engagement/<workflow>/responsibility-matrix-<version>.md` in the user's repository.

Print: `Responsibility matrix <workflow> <version>: <n> responsibilities; <n> AI rows, <n> approval-tier actions; approvals <n recorded, n open>; <n> gaps.`

## Rules

- No invented facts: owners, policies, permissions, and approvals come from inputs or cited records.
- Missing inputs are written as `[gap: what is missing and who can supply it]`; an owner column is never filled with a role guess.
- Rules of thumb (for example a step budget) are labeled starting heuristics, not industry standards.
- Reference policies and records by identifier; no credentials, record contents, or personal data in the matrix.
- Business, technical, and risk/control approval belong to their named owners. The skill prepares the decision; it does not approve.

## Completion checks

- [ ] Every consequential responsibility has an accountable human owner, not only an AI or system label.
- [ ] Each AI or automated action has evidence requirements, permission limits, escalation criteria, and a safe failure behavior.
- [ ] Deterministic validation and the system of record or authoritative state are named where state or policy must be enforced.
- [ ] Business, technical, and risk/control approvals are recorded or explicitly open before deployment.
