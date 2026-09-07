---
name: fde-workflow-trace
description: Use when observing or reconstructing a real workflow case to capture steps, actors, evidence, waits, exceptions, and controls before proposing AI.
---

# Workflow trace

Fills the [workflow trace](../../../toolkit/workflow-trace.md) template. Judgment comes from [Workflow discovery and opportunity framing](../../../skills/workflow-discovery.md) and [Discovery interviewing and workshop facilitation](../../../skills/discovery-interviewing.md).

## Use when

- Discover needs a current-state record of one real case, trigger to outcome, before anyone proposes where AI belongs.
- Frame or Design has surfaced an exception, system, or control the existing trace does not show.
- Not when the user has only a process diagram or a described "typical" case. Ask for a real case; an idealized trace is the guide's weak pattern.

## Obtain first

- [ ] Case identifier, observed date, observer, operator role, and capture method (observation, recording, system export, or reconstruction, labeled as such).
- [ ] The trigger and the outcome of the case.
- [ ] The step sequence with the system touched at each step.
- [ ] Evidence sources by identifier: records, screens, documents, logs, interview notes.
- [ ] Timing per step, active time separate from waiting.
- [ ] Exceptions seen or reported, and how each is handled today.
- [ ] Name and role of the outcome owner.
- [ ] Which operator reviewed the account and which second source corroborated it.

## Procedure

1. Confirm the inputs. Ask for what is missing; do not fill it from domain knowledge.
2. Complete "Case context" from the inputs only.
3. Build the current-state trace, one row per step from trigger through outcome. Give waits, rework, and handoffs their own rows so they are not averaged into active work. Name the system holding state at each step.
4. Complete "Exceptions and controls". Decide which control must remain (human approval, deterministic rule, permission, audit) per guide technique step 3; record a decision owner only when the user names one.
5. Complete "Observations and design implications". Separate what was said from what was shown (interviewing guide, technique 5). Rate confidence high for a system record or observation, medium for a corroborated account, low for an uncorroborated one. Record contradictions and unknowns; do not resolve them by assumption.
6. Complete "Candidate improvement boundary" per guide technique steps 5 and 6. A baseline needs value, period, and source; otherwise write a gap.
7. Record validation. If no operator reviewed the trace or no second source exists, mark the gap and name the source type that would close it.
8. Run the completion checks and print the summary line.

## Output

Fill the Template section of [workflow-trace.md](../../../toolkit/workflow-trace.md). Save to `docs/engagement/<workflow>/workflow-trace-<case-id>.md` in the user's repository.

Print: `Workflow trace <case ID>: <n> steps, <n> exceptions, <n> gaps; validation <complete or open>; candidate boundary: <phrase>.`

## Rules

- No invented facts: every step, time, exception, and owner traces to an input or cited source.
- Missing inputs become `[gap: what is missing and who can supply it]`, never plausible values.
- Any rule-of-thumb number is labeled a starting heuristic, not an industry standard.
- Reference records by identifier; no customer record contents, personal data, or credentials in the trace.
- The improvement boundary is a candidate for the outcome owner to accept, not a decision.

## Completion checks

- [ ] At least one real case is traced from trigger through outcome with evidence sources.
- [ ] Handoffs, waits, exceptions, rework, systems of record, and consequential decisions are visible.
- [ ] An operator validated the trace and a second source corroborated or challenged it.
- [ ] The proposed improvement boundary preserves required controls and names an outcome owner.
