---
name: fde-responsibility-matrix
description: Use when assigning workflow responsibilities to AI, deterministic software, and accountable humans with evidence, controls, escalation, and rollback.
---

# Responsibility matrix

Fills the [responsibility matrix](../../../toolkit/responsibility-matrix.md) template. Judgment comes from [Human, software, and AI system design](../../../skills/ai-system-design.md), [Designing tool-using agents](../../../skills/agent-and-tool-design.md), and [System patterns](../../../learning/system-patterns.md).

## Use when

- Design must state what the system may interpret, validate, recommend, or act on before the first increment is built.
- Build or Deploy changed a control, integration, tool, or autonomy limit and the boundary needs re-approval.
- Not without a validated workflow trace; run [fde-workflow-trace](../fde-workflow-trace/SKILL.md) first.

## Obtain first

- [ ] The validated workflow trace, or an equivalent record with exceptions and controls.
- [ ] Workflow outcome, increment scope, and version identifier.
- [ ] Names and roles of the business outcome, technical service, and risk/control owners.
- [ ] Systems of record and the authoritative state per responsibility.
- [ ] Policy checks that must hold, by identifier, and the permissions the integration can actually be granted.
- [ ] The existing review queue and manual fallback.
- [ ] Tools the system will call, their reversibility, and available credentials.
- [ ] Approvals already given, with approver and date.

## Procedure

1. Confirm the inputs. Owners and policy identifiers are most often missing; ask before drafting.
2. Decompose the outcome into interpretation, validation, decision, action, and recovery (design guide, technique step 1), one row each; split any row that mixes interpretation with action.
3. Choose the least autonomous shape that reaches the outcome (agent guide, technique step 1; System patterns).
4. Assign the least fragile owner per row (design guide, technique step 3): AI interprets or recommends; deterministic software enforces rules, permissions, and state changes; an accountable human owns ambiguity, policy exceptions, and costly or irreversible decisions.
5. Give every action row a permission tier and, for approval-tier actions, state what the approver will see (agent guide, technique steps 3 and 4). Mark tool results and retrieved content as untrusted in the control column (step 8).
6. Fill required evidence, escalation trigger, and failure behavior for every AI or automated row (design guide, technique steps 4 and 5). A failure behavior returns the case to the queue or restores prior state; "retry" alone does not qualify.
7. Complete "Approval and open decisions". Record approvals only with approver and date from the inputs; everything else is `open` with the evidence the approver needs.
8. Run the completion checks and print the summary line.

## Output

Fill the Template section of [responsibility-matrix.md](../../../toolkit/responsibility-matrix.md). Save to `docs/engagement/<workflow>/responsibility-matrix-<version>.md` in the user's repository.

Print: `Responsibility matrix <workflow> <version>: <n> responsibilities; <n> AI rows, <n> approval-tier actions; approvals <n recorded, n open>; <n> gaps.`

## Rules

- No invented facts: owners, policies, permissions, and approvals come from inputs or cited records.
- Missing inputs become `[gap: what is missing and who can supply it]`; an owner column never holds a role guess.
- Rule-of-thumb numbers are labeled starting heuristics, not industry standards.
- Reference policies and records by identifier; no credentials, record contents, or personal data in the matrix.
- Approval belongs to the named owners. The skill prepares the decision; it does not approve.

## Completion checks

- [ ] Every consequential responsibility has an accountable human owner, not only an AI or system label.
- [ ] Each AI or automated action has evidence requirements, permission limits, escalation criteria, and a safe failure behavior.
- [ ] Deterministic validation and the system of record or authoritative state are named where state or policy must be enforced.
- [ ] Business, technical, and risk/control approvals are recorded or explicitly open before deployment.
