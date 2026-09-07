# Stakeholder map

## Purpose

Record who decides, who can stop the work, what each person wants and fears, and what evidence would move them. Use it to plan engagement deliberately rather than discovering a veto at go-live.

## Timing

Draft during [Discover](../stages/01-discover/README.md) as interviews reveal owners; confirm decision rights during [Frame](../stages/02-frame/README.md); update before every gate in [Deploy](../stages/05-deploy/README.md) and when ownership transfers in [Enable](../stages/06-enable/README.md). Update at every stage transition.

## Instructions

1. List every person who owns a system, a budget, a control, a user group, or an approval in the workflow's path. Take names from the [discovery interview guide](discovery-interview-guide.md) plan and from the [workflow trace](workflow-trace.md), not from an organization chart alone.
2. Record what each person owns or decides, what they want, and what they fear, in their own words where possible. Do not record opinions about people as facts. "Rina is difficult" is an opinion; "Rina declined the data extract on 2026-01-15 until the retention policy was cited" is evidence.
3. Tie every stance to something the person said or did, with a date. A stance with no dated evidence is unknown, and the map must say so.
4. Fill the decision-rights table for scope, data access, security approval, go-live, autonomy promotion, and budget. Each decision has exactly one decider; disagreement about who decides is itself a finding to escalate.
5. List who can stop the work and the condition under which they would. Design the engagement so that each stopper sees the evidence that addresses their condition before the gate that needs their approval.
6. Assign an engagement owner and cadence per stakeholder. Rate influence on a 1–5 scale; this is a starting heuristic for comparison, not an industry standard.

## Expected output

A dated record of decision rights, incentives, risk posture, and engagement plan that names who approves, who can stop, what evidence each needs, and how disagreements escalate.

## Supported stages

- [Discover](../stages/01-discover/README.md)
- [Frame](../stages/02-frame/README.md)
- [Deploy](../stages/05-deploy/README.md)
- [Enable](../stages/06-enable/README.md)

## Template

```markdown
# Stakeholder map — [workflow] — [engagement]

- **Map owner:** [name and role]
- **Last updated and stage:** [YYYY-MM-DD; Discover / Frame / Design / Build / Deploy / Enable / Expand]
- **Sources:** [interview records, meeting notes, tickets, approvals]

## Stakeholders

Every entry in the stance and fear columns cites something the person said or did, with a date. Write "unknown" rather than infer.

| Name | Role | Owns or decides | Wants | Fears or risk posture | Influence | Current stance and dated evidence | Evidence that would move them | Engagement owner and cadence |
| --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| [name] | [business outcome owner] | [budget, outcome measure, cohort] | [stated goal] | [stated concern; accepts or avoids reversible risk] | [1–5] | [support / neutral / oppose / unknown; "said or did X on YYYY-MM-DD"] | [measure, threshold, or demonstration] | [name; weekly / per gate] |
| [name] | [operator or supervisor] | [queue, daily work, exception routing] | [stated goal] | [stated concern] | [1–5] | [stance; dated evidence] | [evidence] | [name; cadence] |
| [name] | [technical or platform owner] | [systems, integration, environments] | [stated goal] | [stated concern] | [1–5] | [stance; dated evidence] | [evidence] | [name; cadence] |
| [name] | [security, risk, or controls] | [policy, approval, audit] | [stated goal] | [stated concern] | [1–5] | [stance; dated evidence] | [evidence] | [name; cadence] |
| [name] | [data owner] | [records, access, retention] | [stated goal] | [stated concern] | [1–5] | [stance; dated evidence] | [evidence] | [name; cadence] |

## Decision rights

One decider per decision. If two people claim the same decision, record both and escalate before the decision is needed.

| Decision | Decides | Consulted | Informed | Revisit trigger |
| --- | --- | --- | --- | --- |
| Scope and exclusions | [name] | [names] | [names] | [new evidence about volume, exceptions, or users] |
| Data access | [name] | [names] | [names] | [new data class, region, or retention rule] |
| Security approval | [name] | [names] | [names] | [new integration, permission, or model change] |
| Go-live | [name] | [names] | [names] | [gate evidence changes; see rollout plan] |
| Autonomy promotion | [name] | [names] | [names] | [threshold breach, incident, or control change] |
| Budget | [name] | [names] | [names] | [cost variance beyond an agreed band] |

## Who can stop this

| Person | Can stop by | Condition under which they would | Evidence they need before the next gate | Owner and date |
| --- | --- | --- | --- | --- |
| [name and role] | [withholding approval, revoking access, reallocating people, withdrawing budget] | [stated or demonstrated condition, with date] | [what to show and when] | [name; YYYY-MM-DD] |

## Escalation path

| Disagreement | First forum | Escalates to | Time limit before escalation | Record kept in |
| --- | --- | --- | --- | --- |
| [scope, access, approval, priority, or ownership] | [working session or owner] | [name and role] | [days] | [decision log or ticket] |

## Maintenance

- Update this map at every stage transition and after any change in ownership, budget, or approval path; record the date and stage above.
- Re-verify each stance against something said or done since the last update; a stance older than the previous stage transition is stale and reverts to unknown.
- Retire a row only when the person no longer owns or decides anything in the path; note who inherited it.
```

## Completion checks

- [ ] Every stakeholder who owns a system, budget, control, user group, or approval in the workflow's path is listed.
- [ ] Every stance and fear cites something the person said or did, with a date, or is marked unknown.
- [ ] Scope, data access, security approval, go-live, autonomy promotion, and budget each have exactly one decider.
- [ ] Everyone who can stop the work is named with the condition and the evidence that addresses it.
- [ ] An escalation path and an engagement owner with cadence exist for each stakeholder, and the map records its last stage update.
