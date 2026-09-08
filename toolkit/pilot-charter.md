# Pilot charter

## Purpose

Agree, before pilot work starts, what the pilot must prove, for whom, against which baseline, using which analysis, and what each result leads to. Success, hold, and stop are then decided by criteria written in advance, not argued after the fact.

## Timing

Draft during [Frame](../stages/02-frame/README.md) once the [business case](business-case.md) states the value logic; complete during [Design](../stages/03-design/README.md) when the boundary and prerequisites are known; sign before the first [Deploy](../stages/05-deploy/README.md) gate opens.

## Instructions

1. Write the outcome hypothesis as one sentence naming the users, the workflow slice, the measure, and the expected direction. Take baselines and value logic from the [business case](business-case.md); do not restate them differently here.
2. Define the first wedge and its exclusions from the [opportunity scorecard](opportunity-scorecard.md) and [workflow trace](workflow-trace.md). An exclusion that is not written is not excluded.
3. Choose the cohort and state the selection rationale. A cohort chosen for enthusiasm proves adoption by enthusiasts; say so.
4. Predeclare success and stop criteria and the analysis method, and obtain agreement from the business, technical, and risk owners before the pilot starts. The method (sample, comparison, statistic, uncertainty treatment) must be written down before results exist; a method chosen after seeing results is not evidence.
5. List data access, security, and environment prerequisites with owners and dates. A pilot with an unmet prerequisite has not started.
6. Align the timeline with the [rollout plan](rollout-plan.md) gates and state what each end state (expand, hold, stop) requires and who decides.
7. Write what the pilot does not prove before it runs, so the result cannot be stretched beyond its cohort, document types, regions, seasonality, or load. A 30-day pilot with one cohort is a starting heuristic, not an industry standard; it does not cover a quarter-end peak.

## Expected output

A signed, dated record of hypothesis, scope, cohort, baselines and targets, predeclared criteria and analysis, prerequisites, owners, gated timeline, end states, and limits.

## Supported stages

- [Frame](../stages/02-frame/README.md)
- [Design](../stages/03-design/README.md)
- [Deploy](../stages/05-deploy/README.md)

## Template

```markdown
# Pilot charter — [workflow] — [system and version]

## Outcome hypothesis

[Users] performing [workflow slice] with [system] will [change measure from baseline to target] within [period] without [control or policy breach].

## First wedge and exclusions

- **Included:** [document types, languages, regions, steps, actions the system may propose]
- **Explicitly excluded:** [types, regions, actions, decisions, and data that stay on the current path]
- **Safe state on failure:** [existing queue or manual path; owner]

## Users and cohort

- **Cohort:** [roles, count, location, business unit]
- **Selection rationale:** [representative of volume, exception mix, or skill; or another stated reason and its consequence for inference]

## Baseline and targets

Value logic and counterfactual live in the business case; this table records what the pilot measures.

| Measure | Baseline value and period | Source | Target or threshold | Measurement method during pilot | Owner |
| --- | --- | --- | --- | --- | --- |
| [handling time, quality, on-time rate, adoption, review burden, cost, reliability] | [value; period] | [query, time study, or report ID] | [target] | [trace, audit event, sample review] | [name] |
| Policy or control breach | [count and period] | [control log] | 0 | [control log review] | [name] |

## Predeclared success and stop criteria

| Criterion | Success threshold | Stop threshold | Analysis method | Sample and period | Decision owner |
| --- | --- | --- | --- | --- | --- |
| [measure] | [value] | [value that halts the pilot] | [matched pairs, stratified sample, interval method, or before/after with stated limits] | [count, strata, window] | [name] |
| [control] | [zero breaches] | [any breach] | [control log audit] | [all cases] | [name] |

- **Method agreed on:** [YYYY-MM-DD; by whom]; results existed on that date: [no]
- **Amendment rule:** [any later change to criteria or method requires a signed amendment below stating what was known when it was made]

## Prerequisites

| Prerequisite | Type | Owner | Needed by | Status and evidence |
| --- | --- | --- | --- | --- |
| [data extract, record access, service account] | Data access | [name] | [YYYY-MM-DD] | [approved / pending; ticket or approval ID] |
| [security review, data classification, logging] | Security | [name] | [YYYY-MM-DD] | [status; ID] |
| [environment, integration endpoint, kill switch] | Environment | [name] | [YYYY-MM-DD] | [status; ID] |

## Owners

- **Business outcome owner:** [name and role; accepts the measure and cohort]
- **Technical owner:** [name and role; owns system, rollback, reliability]
- **Risk and control owner:** [name and role; owns policy criteria and the stop decision on any breach]

## Timeline and gates

Gate definitions, promotion criteria, and rollback triggers are in the rollout plan; this table fixes dates and decision points.

| Gate | Start | End | Evidence reviewed | Decision owner |
| --- | --- | --- | --- | --- |
| Observe | [date] | [date] | [baseline credibility] | [name] |
| Assist | [date] | [date] | [offline evaluation and training] | [name] |
| Shadow | [date] | [date] | [field versus evaluation agreement] | [name] |
| Approve | [date] | [date] | [pilot outcome against the criteria above] | [name] |

## End states

| End state | Requires | Then | Decision owner |
| --- | --- | --- | --- |
| Expand | [all success thresholds met; zero breaches; Day 2 owners accept load; business case refreshed] | [next cohort and scope; new evidence period] | [name] |
| Hold | [no stop threshold reached; a named gap in evidence, control, or ownership] | [what must be shown, by whom, by when] | [name] |
| Stop | [any stop threshold reached, or the hypothesis disconfirmed] | [return to Frame or Design; what to preserve; how users are told] | [name] |

## What the pilot does not prove

- **Document or case types:** [types outside the wedge]
- **Regions, languages, and units:** [not in the cohort]
- **Seasonality:** [peaks outside the window]
- **Load:** [volume or concurrency not reached]
- **Autonomy:** [actions the system did not take]

## Sign-off

| Role | Name | Agreed to criteria and method before pilot start | Date | Conditions |
| --- | --- | --- | --- | --- |
| Business outcome owner | [name] | [yes] | [YYYY-MM-DD] | [conditions] |
| Technical owner | [name] | [yes] | [YYYY-MM-DD] | [conditions] |
| Risk and control owner | [name] | [yes] | [YYYY-MM-DD] | [conditions] |
| Amendment | [name] | [what changed and why] | [YYYY-MM-DD] | [what was known] |
```

## Completion checks

- [ ] The hypothesis is one sentence naming users, slice, measure, direction, and period, and the wedge has written exclusions.
- [ ] Success and stop criteria and the analysis method were signed by all three owners before the pilot started and before any result existed.
- [ ] Every baseline cites a source and every target has a measurement method and owner consistent with the business case.
- [ ] Data access, security, and environment prerequisites have owners, dates, and completion evidence.
- [ ] Gates match the rollout plan; expand, hold, and stop each state what they require and who decides; the charter states what the pilot does not prove.
