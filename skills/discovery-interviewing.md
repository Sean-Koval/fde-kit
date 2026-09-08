# Discovery interviewing and workshop facilitation

## Relevance

Use this capability to learn how work actually happens before proposing where AI belongs in it. It is useful when an engagement opens with a sponsor's summary rather than observed cases, when the team must choose among candidate workflows, when a kickoff must produce a shared outcome and decision rules, and when an expansion request arrives as an opinion rather than evidence. Interviews and workshops fill the [workflow trace](../toolkit/workflow-trace.md) and [opportunity scorecard](../toolkit/opportunity-scorecard.md) with facts instead of assertions.

## Timing

Run role-based interviews and observation in [Discover](../stages/01-discover/README.md). Use the kickoff and scoping workshops to move the evidence into an agreed frame in [Frame](../stages/02-frame/README.md). Return to it in [Expand](../stages/07-expand/README.md) whenever a new workflow, cohort, or document type is proposed; an expansion inherits the method, not the earlier evidence.

## Technique

Every duration, count, and sample size below is a starting heuristic, not an industry standard.

### 1. Prepare by role and write hypotheses to be disconfirmed

Interview at least one person in each role; each knows something the others cannot tell you.

| Role | What they actually know | What they tend to omit | Ask for |
| --- | --- | --- | --- |
| Operator | Real steps, workarounds, queue behavior, what "done" means in practice | That the official procedure is not followed | A live case, the last hard case, their personal cheat sheet |
| Supervisor | Volume, staffing, rework, escalation paths, which exceptions cost the most | How much rework their own decisions create | Queue reports, backlog age, escalation counts |
| Sponsor | Outcome that matters, budget, constraints, what success must look like upward | Ground-level mechanics; has often never watched a case | The decision they must make and its deadline |
| Information technology (IT) and security | Systems of record, integration options, identity, data classification, review gates | Timelines for access and review | Architecture notes, access process, prior review findings |
| Data owner | Where authoritative records live, their quality, retention, and permissions | Known data defects | Sample records with known-good labels, field definitions |

Before each session, write two or three hypotheses phrased so that an observation could prove them wrong ("extraction is the slowest step; false if approver wait exceeds active time"). Arrive with hypotheses, not a solution.

### 2. Climb the question ladder from open to specific to evidence

| Rung | Purpose | Example prompts |
| --- | --- | --- |
| Open | Let the interviewee define the work in their words | "What does a normal week look like?" "Where does the work come from?" |
| Specific | Anchor on one real case | "Walk me through the last one you did." "What did you do first, then next?" |
| Evidence | Convert memory into things you can check | "Show me." "How many per week?" "What happens when it fails?" "Who finds out, and how long after?" |

Stay on one case until you can retell it step by step; only then generalize. "Would it help if…" is a solution disguised as a question. Park it.

### 3. Observe work rather than ask about it

Sit beside the operator for real cases. Request artifacts: screens, queue views, tickets, spreadsheets, the checklist taped to the monitor. Time active work separately from waiting and note which system each step touches. Record what the person did, not what they described.

### 4. Listen for the highest-signal moments

Workarounds ("I keep my own spreadsheet because…"), exceptions ("unless it's from that vendor"), and blame-shifts ("that's really procurement's problem") reveal where the official process and the real one diverge. Each is a candidate boundary, control, or risk. Write them down verbatim and follow up with "show me one."

### 5. Quantify with the interviewee, and separate said from shown

Build numbers together: "You said about fifty a day; the queue shows 212 for the week, does that match?" Prefer counts to averages: ask for the last ten cases, not the typical case. Keep two columns in your notes, what was said and what was shown. Only the second enters the workflow trace as evidence; the first becomes an assumption to test.

### 6. Avoid leading and solutioning

Do not describe the product, the model, or a demo during discovery. Do not ask "is this step painful?"; ask "how long did this step take on that case?" If you catch yourself designing, note the idea and return to the case.

### 7. Synthesize the same day

Within the day, write an evidence log (source, case identifier, observation, number, date), the contradictions between roles or between said and shown, assumptions to test with a named owner, the next step, and the follow-up permission you obtained (a second observation, a data pull, a named contact). Unresolved contradictions are findings, not failures.

### 8. Design the workshops

**Kickoff, 90 minutes.**

| Block | Minutes | Output |
| --- | --- | --- |
| Outcome: what business result must change, stated by the sponsor | 20 | One-sentence outcome with a measure and an owner |
| Roles: who decides, operates, controls risk, integrates | 20 | Named owners with backups; the start of the [stakeholder map](../toolkit/stakeholder-map.md) |
| Scope: what is in the first look, what is explicitly out | 30 | Inclusion and exclusion list with reasons |
| Decision rules: what evidence advances, holds, or stops the work, and who decides | 20 | Written rule, decision owner, review date |

**Scoping workshop, two to three hours.** Candidates in, a ranked [opportunity scorecard](../toolkit/opportunity-scorecard.md) out.

| Block | Minutes | Output |
| --- | --- | --- |
| Evidence review: traces and numbers so far, contradictions flagged | 30 | Shared fact base; open questions assigned |
| Candidate workflows: one line each, owner, volume, present pain, system of record | 30 | Candidate list, no more than eight |
| Scoring against the criteria, one criterion at a time across all candidates | 60 | Draft scorecard with evidence gaps marked |
| Wedge and exclusions for the top candidate | 30 | First wedge, exclusions, evidence gate, and owner |
| Decisions and next steps | 15 | Decision log with owners and dates |

Facilitation moves for both sessions: timebox every block and say when it ends; park off-topic items on a visible list with an owner; announce before each block whether it is to decide or to discuss; capture each decision with the decider, the date, and the evidence it rests on; close by reading the decisions back.

### 9. Anti-patterns

| Anti-pattern | Why it fails | Replace with |
| --- | --- | --- |
| Interviewing only sponsors | Sponsors know the outcome, not the mechanics | One operator per role, observed on real cases |
| Demo-first meetings | Anchors the room on a solution and suppresses contradicting evidence | Evidence-first agenda; demos after the frame is agreed |
| Sending a survey instead of observing | Surveys collect opinions and averages; workarounds do not appear | Shadowing and artifact requests |
| Accepting averages instead of cases | Averages hide the exceptions that decide the boundary | The last ten cases, timed and sourced |

## Examples

### Good pattern

In the fictional LumenPeak Manufacturing engagement ([worked example](../examples/invoice-intake-ai/README.md)), the team sat with accounts-payable (AP) analyst Jordan Kim rather than interviewing Elena Torres alone. Over twelve invoice cases they timed each active step separately from waiting and recorded which enterprise resource planning (ERP) screen each step used. Active steps summed to about eight minutes, but the mailbox median wait was 13.4 hours, and the longest delays traced to missing purchase orders sitting with approvers, not to reading the invoice. The hypothesis "extraction is the bottleneck" was disproved by the trace. Jordan's remark "I keep my own vendor list because the ERP search is slow" became a data-quality question for the data owner, not a feature request. The evidence log, the contradiction between Elena's estimate and the queue report, and the permission to pull a 1,200-record sample went into the same-day synthesis, and the scoping workshop ranked purchase-order-backed intake first on that evidence.

### Weak pattern

A 45-minute call with a finance sponsor, no operator present, ends with "AI for accounts payable" as the scope. No case was observed, no artifact requested, active time and waiting never separated, and the sponsor's "about ten minutes an invoice" recorded as the baseline. The next meeting opens with a demo, the room debates features, and the exceptions that will decide the production boundary remain unknown.

## Practice

Choose one recurring workflow you can access. Write three hypotheses an observation could disprove. Interview one operator using the ladder, then watch two real cases and collect one artifact. Produce a same-day synthesis with an evidence log, one contradiction, two assumptions with owners, and the follow-up permission you obtained. Then draft a 90-minute kickoff agenda for that workflow with the four outputs above.

## Self-assessment

- Did every role in the preparation table contribute, and can you name what each one told you that the others could not?
- Can you separate, line by line, what was said from what was shown, and does only the second enter the trace?
- Did you record at least one workaround, exception, or blame-shift verbatim and follow it to a case?
- Were the numbers built with the interviewee from counts and cases rather than accepted as averages?
- Did the workshop end with written decisions, owners, dates, and an evidence gate that could still say stop?

## Links

**Lifecycle stages:** [Discover](../stages/01-discover/README.md), [Frame](../stages/02-frame/README.md), [Expand](../stages/07-expand/README.md).

**Toolkit assets:** [Discovery interview guide](../toolkit/discovery-interview-guide.md), [Stakeholder map](../toolkit/stakeholder-map.md), [Workflow trace](../toolkit/workflow-trace.md), [Opportunity scorecard](../toolkit/opportunity-scorecard.md).

**Related skills:** [Workflow discovery and opportunity framing](workflow-discovery.md), [Executive communication and expectation management](executive-communication.md).
