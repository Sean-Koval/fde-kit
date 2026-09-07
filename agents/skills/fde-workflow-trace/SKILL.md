---
name: fde-workflow-trace
description: Use when observing or reconstructing a real workflow case to capture steps, actors, evidence, waits, exceptions, and controls before proposing AI.
---

# Workflow trace

Fills the [workflow trace](../../../toolkit/workflow-trace.md) template. Judgment comes from [Workflow discovery and opportunity framing](../../../skills/workflow-discovery.md) and [Discovery interviewing and workshop facilitation](../../../skills/discovery-interviewing.md).

## Use when

- Discover needs a current-state record of one real case, trigger to outcome, before anyone proposes where AI belongs.
- Frame or Design has surfaced an exception, system, or control the existing trace does not show.
- Not when the user has only a process diagram or a "typical" case. Ask for a real one; an idealized trace is the guide's weak pattern.

## Obtain first

- [ ] Case identifier, date, observer, operator role, and capture method (observation, recording, export, or reconstruction, labeled as such).
- [ ] Trigger and outcome of the case.
- [ ] Step sequence with the system touched at each step.
- [ ] Evidence sources by identifier: records, screens, documents, logs, notes.
- [ ] Timing per step, active time separate from waiting.
- [ ] Exceptions seen or reported, and their current handling.
- [ ] Outcome owner, name and role.
- [ ] The operator who reviewed the account and the second source that corroborated it.

## Procedure

1. Confirm the inputs; ask for what is missing rather than filling it from domain knowledge.
2. Complete "Case context" from the inputs only.
3. Build the trace, one row per step from trigger through outcome. Give waits, rework, and handoffs their own rows; name the system holding state at each step.
4. Complete "Exceptions and controls". Choose the control that must remain per guide technique step 3; name a decision owner only when the user does.
5. Complete "Observations and design implications". Separate said from shown (interviewing guide, technique 5). Rate confidence high for a record or observation, medium for a corroborated account, low otherwise. Leave contradictions and unknowns unresolved.
6. Complete "Candidate improvement boundary" per guide technique steps 5 and 6. A baseline without value, period, and source is a gap.
7. Record validation, or mark the gap and name the second source type that would close it.
8. Run the completion checks and print the summary line.

## Output

Fill the Template section of [workflow-trace.md](../../../toolkit/workflow-trace.md). Save to `docs/engagement/<workflow>/workflow-trace-<case-id>.md` in the user's repository.

Print: `Workflow trace <case ID>: <n> steps, <n> exceptions, <n> gaps; validation <complete or open>; candidate boundary: <phrase>.`

## Rules

- No invented facts: every step, time, exception, and owner traces to an input or cited source.
- Missing inputs become `[gap: what is missing and who can supply it]`.
- Rule-of-thumb numbers are labeled starting heuristics, not industry standards.
- Reference records by identifier; no customer record contents, personal data, or credentials in the trace.
- The improvement boundary is a candidate for the outcome owner to accept, not a decision.

## Completion checks

- [ ] At least one real case is traced from trigger through outcome with evidence sources.
- [ ] Handoffs, waits, exceptions, rework, systems of record, and consequential decisions are visible.
- [ ] An operator validated the trace and a second source corroborated or challenged it.
- [ ] The proposed improvement boundary preserves required controls and names an outcome owner.
