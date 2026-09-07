---
name: fde-workflow-trace
description: Use when observing or reconstructing a real workflow case to capture steps, actors, evidence, waits, exceptions, and controls before proposing AI.
---

# Workflow trace

Fills the [workflow trace](../../../toolkit/workflow-trace.md) template. Judgment comes from [Workflow discovery and opportunity framing](../../../skills/workflow-discovery.md) and [Discovery interviewing and workshop facilitation](../../../skills/discovery-interviewing.md); read both before the first trace in an engagement.

## Use when

- Discover needs a current-state record of one real case, from trigger to outcome, before anyone proposes where AI belongs.
- Frame or Design needs a constraint check: a new exception, system, or control has surfaced and the existing trace does not show it.
- Not when the user has only a process diagram or a described "typical" case. Ask for a real case first; a trace of an idealized process is the weak pattern the guide warns against.

## Obtain first

- [ ] Case identifier, observed date, observer, operator role, and how the case was captured: live observation, screen recording, system export, or reconstruction from records. A reconstruction is labeled as one.
- [ ] The trigger that started the case and the outcome it reached.
- [ ] The step sequence with the system touched at each step.
- [ ] Evidence sources by identifier: record IDs, screens, documents, logs, interview notes.
- [ ] Timing per step, with active time and waiting time kept separate.
- [ ] Exceptions seen in this case or reported for this workflow, and how each is handled today.
- [ ] Name and role of the outcome owner.
- [ ] Validation status: which operator reviewed the account and which second source corroborated it.

## Procedure

1. Confirm the inputs above. Ask for what is missing; do not fill it from general knowledge of the domain.
2. Complete "Case context" from the inputs only.
3. Build the current-state trace, one row per step from trigger through outcome. Give waits, rework, and handoffs their own rows so they are not averaged into active work (guide self-assessment, second question). Name the system that holds state at each step.
4. Complete "Exceptions and controls" from observed or reported exceptions. Decide which control must remain (human approval, deterministic rule, permission, audit) using guide technique step 3; record a decision owner only when the user names one.
5. Complete "Observations and design implications". Separate what was said from what was shown (interviewing guide, technique 5). Rate confidence by evidence strength: high for a system record or observation, medium for a corroborated account, low for an uncorroborated account. Record contradictions and unknowns as observations, not resolutions.
6. Complete "Candidate improvement boundary" using guide technique steps 5 and 6. The baseline measure needs a value, period, and source; otherwise write a gap.
7. Record validation. If no operator reviewed the trace or no second source exists, mark the gap and name the kind of source that would close it (queue history, audit record, policy document).
8. Run the completion checks and print the summary line.

## Output

Fill the Template section of [workflow-trace.md](../../../toolkit/workflow-trace.md). Save to `docs/engagement/<workflow>/workflow-trace-<case-id>.md` in the user's repository.

Print: `Workflow trace <case ID>: <n> steps, <n> exceptions, <n> gaps; validation <complete or open>; candidate boundary: <one phrase>.`

## Rules

- No invented facts: every step, time, exception, and owner traces to an input or a cited source.
- Missing inputs are written as `[gap: what is missing and who can supply it]`, never as plausible values.
- Any number offered as a rule of thumb is labeled a starting heuristic, not an industry standard.
- Reference records and documents by identifier; never copy customer record contents, personal data, or credentials into the trace.
- The improvement boundary is a candidate for the outcome owner to accept; do not present it as decided.

## Completion checks

- [ ] At least one real case is traced from trigger through outcome with evidence sources.
- [ ] Handoffs, waits, exceptions, rework, systems of record, and consequential decisions are visible.
- [ ] An operator validated the trace and a second source corroborated or challenged it.
- [ ] The proposed improvement boundary preserves required controls and names an outcome owner.
