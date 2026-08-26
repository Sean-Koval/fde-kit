# Workflow trace

## Purpose

Make the current workflow observable enough to design a credible change. Capture real cases, hidden work, exceptions, systems, decisions, evidence, and handoffs—not an idealized process diagram.

## Timing

Use during [Discover](../stages/01-discover/README.md); refine it through [Frame](../stages/02-frame/README.md) and [Design](../stages/03-design/README.md) as new cases expose constraints.

## Instructions

1. Observe operators completing representative work; collect artifacts and system records alongside interviews.
2. Trace one case per row from trigger through outcome, including waits, rework, decisions, and exceptions.
3. Mark the evidence that justified each decision, the system that holds state, and the person accountable for the result.
4. Validate the trace with an operator and a second evidence source; flag contradictions and unknowns.
5. Use the trace to select a bounded improvement target and to define what must remain under human or deterministic control.

## Expected output

A validated current-state record that explains the happy path, consequential exceptions, evidence flow, and design constraints for a specific workflow.

## Supported stages

- [Discover](../stages/01-discover/README.md)
- [Frame](../stages/02-frame/README.md)
- [Design](../stages/03-design/README.md)

## Template

```markdown
# Workflow trace — [workflow name] — [case ID]

## Case context

- **Observed date and duration:** [YYYY-MM-DD, start/end]
- **Observer:** [name]
- **Operator and role:** [name or role]
- **Outcome owner:** [name and role]
- **Case trigger:** [event that started the work]
- **Case outcome:** [completed, escalated, rejected, delayed, or other]
- **Evidence sources:** [screens, record IDs, documents, logs, interview notes]
- **Validation:** [operator who reviewed the trace and second source used]

## Current-state trace

| # | Step and system | Actor | Input and evidence | Decision or action | Time / wait | Exception or rework | State and audit record |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | [step; system] | [role] | [source, fields, and confidence] | [decision/action] | [active/wait] | [what can go wrong] | [system of record, ID, log] |
| 2 | [step; system] | [role] | [source, fields, and confidence] | [decision/action] | [active/wait] | [what can go wrong] | [system of record, ID, log] |
| 3 | [step; system] | [role] | [source, fields, and confidence] | [decision/action] | [active/wait] | [what can go wrong] | [system of record, ID, log] |

## Exceptions and controls

| Condition | Frequency or consequence | Current response | Evidence required | Decision owner | Control that must remain |
| --- | --- | --- | --- | --- | --- |
| [exception] | [rate, cost, risk] | [workaround or escalation] | [document, system record, policy] | [name] | [human approval, deterministic rule, permission, or audit] |

## Observations and design implications

| Observation | Evidence | Confidence | Implication | Owner / next validation |
| --- | --- | --- | --- | --- |
| [fact, contradiction, or unknown] | [source] | [high/medium/low] | [constraint, opportunity, or question] | [name and date] |

## Candidate improvement boundary

- **Work to improve:** [specific step or decision]
- **Work that must not change yet:** [safety, policy, or operational boundary]
- **Baseline measure:** [measure, value, period, source]
- **Open question before design:** [question and validation method]
```

## Completion checks

- [ ] At least one real case is traced from trigger through outcome with evidence sources.
- [ ] Handoffs, waits, exceptions, rework, systems of record, and consequential decisions are visible.
- [ ] An operator validated the trace and a second source corroborated or challenged it.
- [ ] The proposed improvement boundary preserves required controls and names an outcome owner.
