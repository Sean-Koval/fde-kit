# Discovery interview guide

## Purpose

Plan and run discovery interviews that produce evidence about how work actually happens, not opinions about how it should. Use it to decide which claims to trust, which to test, and what to observe next.

## Timing

Use during [Discover](../stages/01-discover/README.md) before any workflow is selected; reuse during [Frame](../stages/02-frame/README.md) to close specific evidence gaps in the [opportunity scorecard](opportunity-scorecard.md); reuse during [Expand](../stages/07-expand/README.md) when a new cohort, region, or workflow is proposed and its reality has not been observed.

## Instructions

1. Write the interview plan with one disconfirming hypothesis per interviewee: the claim that, if wrong, would change the engagement. Interview operators before supervisors and supervisors before sponsors, so sponsor claims are tested against observed work rather than the reverse.
2. Book a working session, not a meeting. Observe at least one real case per operator from trigger to outcome; this is a starting heuristic, not an industry standard. Ask for the screen, the queue, and the record.
3. Run each question in the ladder: "walk me through the last one" (open), then "show me" (specific), then "how many, how long, and what happens when it fails" (evidence). Ask for the most recent case, never a typical one.
4. Capture what was said and what was shown in separate columns with a source or record identifier, confidence, and a follow-up owner. A statement with no record behind it is a claim, not a fact.
5. Within one day, synthesize: list contradictions between interviewees and between statements and records, name the assumptions to test, draft a candidate problem statement, and record consent for follow-up. Feed cases into the [workflow trace](workflow-trace.md) and people into the [stakeholder map](stakeholder-map.md).

Technique is taught in [Discovery interviewing and workshop facilitation](../skills/discovery-interviewing.md).

## Expected output

An interview record that separates statements from observations, cites records, rates confidence, and yields testable assumptions and a candidate problem statement with named next steps.

## Supported stages

- [Discover](../stages/01-discover/README.md)
- [Frame](../stages/02-frame/README.md)
- [Expand](../stages/07-expand/README.md)

## Template

```markdown
# Discovery interview guide — [workflow or team] — [engagement]

## Interview plan

Operators first, then supervisors, then sponsors. One row per person.

| Interviewee | Role | What this person knows first-hand | Hypothesis to disconfirm | Owner | Date |
| --- | --- | --- | --- | --- | --- |
| [name] | [operator] | [cases handled, screens used, queue owned] | [claim that would change the plan if false] | [interviewer] | [YYYY-MM-DD] |
| [name] | [supervisor] | [queue volumes, exception routing] | [claim] | [interviewer] | [YYYY-MM-DD] |
| [name] | [sponsor] | [outcome, budget, counterfactual] | [claim] | [interviewer] | [YYYY-MM-DD] |
| [name] | [IT and security] | [systems, permissions, review process] | [claim] | [interviewer] | [YYYY-MM-DD] |
| [name] | [data owner] | [record definitions, quality, access rules] | [claim] | [interviewer] | [YYYY-MM-DD] |

## Question bank by role

Each question follows the ladder: open, then specific, then evidence.

### Operator

- **Open:** Walk me through the last [case] you completed, from arrival to done.
- **Specific:** Show me that case on your screen. Which fields did you type, where did each value come from, and what did you check before moving on?
- **Evidence:** How many of these do you do in a day? How long did that one take? What happened the last time one failed, and where is that case now? [record identifier]

### Supervisor

- **Open:** Walk me through the last time the queue got away from you.
- **Specific:** Show me the queue and its age distribution now. Which cases have been waiting longest, and why?
- **Evidence:** How many cases were reworked or escalated last month? What is the median wait, and which report says so? What happens when an exception has no owner? [report identifier]

### Sponsor

- **Open:** Walk me through the last decision you made about this workflow.
- **Specific:** Show me the number you are held to and its report.
- **Evidence:** How many people, hours, and dollars does this workflow consume? What happens if nothing changes for a year? Which result would make you stop? [source]

### IT and security

- **Open:** Walk me through the last new system that touched this data.
- **Specific:** Show me the data classification, the review checklist, and the last approved integration pattern.
- **Evidence:** How many reviews run per quarter and how long does each take? What blocked the last one? What happens when a service in this path is down? [ticket or policy identifier]

### Data owner

- **Open:** Walk me through how a record in this system is created, changed, and retired.
- **Specific:** Show me a record with a known quality problem and a field definition people disagree about.
- **Evidence:** How many records exist, how many change per month, and what share fails validation? What happens when two systems disagree? [query or extract identifier]

## Observation checklist

- **Artifacts requested:** [documents, exports, screenshots, policies; supplier and date]
- **Screens seen:** [system, screen, what the operator did there]
- **Queues and their ages:** [queue name, count, oldest item, source of the count]
- **Exceptions witnessed:** [what happened, how it was routed, who decided]
- **Workarounds:** [spreadsheets, side channels, memorized rules, re-keying; the operator's stated reason]

## Evidence capture

| What was said | What was shown | Source or record identifier | Confidence | Follow-up |
| --- | --- | --- | --- | --- |
| [statement, attributed to a role] | [screen, record, artifact, or nothing] | [record ID, report name, export date] | [high/medium/low] | [owner, action, date] |

## Synthesis

- **Contradictions between interviewees:** [who said what; which record could settle it]
- **Contradictions between statements and records:** [claim, record, gap, and who owns the explanation]
- **Assumptions to test:** [assumption; why it matters; test; owner; date]
- **Candidate problem statement:** [who, doing what, is blocked by what, with what measured consequence and source]
- **Next step:** [observe, trace, query, or interview; owner; date]
- **Consent for follow-up:** [who agreed to be re-contacted, for what, recorded on which date]
```

## Completion checks

- [ ] Every interview has a named hypothesis to disconfirm, and operators were interviewed before sponsors.
- [ ] At least one real case per operator was observed on screen, with the record identifier captured.
- [ ] Every row in the evidence capture table separates what was said from what was shown and cites a source.
- [ ] Contradictions and assumptions are listed with an owner and a test, not resolved by preference.
- [ ] The candidate problem statement names the people, the measured consequence, and its source.
