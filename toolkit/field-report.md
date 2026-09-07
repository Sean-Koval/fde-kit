# Field report

## Purpose

Send reproducible product, model, and platform signal from an engagement upstream to the forward deployed engineer's (FDE's) own product, research, or platform teams so it can be acted on and prioritized. The report turns a field failure or gap into cases that another team can rerun, with the business impact stated so the receiving team can rank it against other work. It is a signal to the FDE's own organization, not a customer deliverable.

## Timing

Write during [Build](../stages/04-build/README.md) when error analysis reveals a failure the engagement cannot fix locally, during [Enable](../stages/06-enable/README.md) when production traces show a recurring pattern, and during [Expand](../stages/07-expand/README.md) when a gap blocks a scope the customer wants next. Send it while the reproduction still works; a report about a pattern that can no longer be reproduced is anecdote.

## Instructions

1. Report one issue per field report. A report that mixes a model behavior with a documentation gap cannot be routed to one owner.
2. Classify the issue as model behavior, product gap, documentation gap, integration or platform issue, or feature request. If two classes fit, choose the one whose fix would remove the workaround.
3. Include at least one reproducible case per reported issue. A case records the input, the expected result, the observed result, and the exact model, prompt, tool, and retrieval versions, with a trace reference the receiving team can open. Without a case the report is not sent.
4. Never include customer confidential data. Use a synthetic equivalent or a redacted input that reproduces the behavior; state which, and confirm that the receiving team's access to the trace store is covered by the customer's terms. If the behavior cannot be reproduced without confidential data, build a synthetic case first.
5. Describe the pattern, not only the case: how often it occurs, under which conditions, what it costs the customer, and whether it blocks a gate in the [rollout plan](rollout-plan.md) or a criterion in the [evaluation pack](evaluation-pack.md).
6. State the workaround in place and its cost in review time, latency, tokens, or lost scope, so the receiving team can see what the fix would release.
7. Justify the priority with numbers: customers or workflows affected, revenue or risk at stake, and the quality of the evidence (production traces, evaluation run, or single observation). Starting heuristic, not an industry standard: three or more engagements with the same pattern justifies a roadmap conversation; one engagement justifies a tracked issue.
8. Name the owner who will answer questions and the customer-impact statement the receiving team can quote internally. Do not commit the customer to a timeline you do not control, and do not share the report with the customer; if they need a status, use the [executive readout](executive-readout.md).

The fictional LumenPeak example shows the shape: the one low-quality scan that the extraction step failed to escalate in run `EVAL-2026-03-06` became a regression case; a field report would carry a synthetic degraded scan, the expected abstention, the observed confident extraction, and the versions under test upstream to the team that owns extraction behavior.

## Expected output

A routed, reproducible report that a product, research, or platform team can rerun, prioritize against other work, and close with a change that removes the workaround.

## Supported stages

- [Build](../stages/04-build/README.md)
- [Enable](../stages/06-enable/README.md)
- [Expand](../stages/07-expand/README.md)

## Template

```markdown
# Field report — [short issue title] — [YYYY-MM-DD]

- **Report ID and status:** [identifier; new / acknowledged / in progress / resolved / declined]
- **Routed to:** [product, research, or platform team and owner]
- **Confidentiality check:** [synthetic or redacted inputs only; checked by name; date]

## Engagement context

- **Industry and workflow shape:** [industry; extraction, retrieval-grounded assistant, tool-using agent, classification; anonymized]
- **Deployment pattern:** [batch or interactive; human approval level; integration type; scale]
- **Stage and gate:** [lifecycle stage; gate the engagement is at]

## Classification

[model behavior / product gap / documentation gap / integration or platform issue / feature request — one]

## Pattern observed

- **What happens:** [behavior, in one or two sentences]
- **How often:** [count / denominator; period; source: production traces, evaluation run, or observation]
- **Conditions:** [input type, length, language, tool state, retrieval state, or load under which it occurs]
- **Business impact:** [review time, incorrect outcomes, lost scope, or cost; value and denominator]
- **Blocks a gate:** [yes/no; which gate or criterion]

## Reproducible cases

| Case ID | Input (redacted or synthetic) | Expected result | Observed result | Model version | Prompt version | Tool or retrieval version | Trace reference |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [ID] | [synthetic input or redacted fixture; where stored] | [result] | [result] | [version] | [version] | [version] | [trace ID the receiving team can open] |

## Workaround in place

- **Workaround:** [prompt change, deterministic check, routing to review, scope exclusion]
- **Cost:** [review minutes, latency, tokens, or excluded volume; value and denominator]

## Requested change and priority

- **Requested change:** [specific behavior, capability, document, or fix]
- **Customers or workflows affected:** [count; list of anonymized engagements]
- **Revenue or risk at stake:** [value or range; basis]
- **Evidence quality:** [production traces / evaluation run / single observation]
- **Why now:** [gate, renewal, or expansion this blocks; date]

## Customer impact statement

[Two sentences the receiving team can quote internally: who is affected, what they cannot do, and what changes when it is fixed. No customer name or confidential detail.]

## Owner and contact

- **Reporting FDE:** [name; channel; time zone]
- **Engagement owner:** [name]
- **Follow-up expectation:** [acknowledgement by; decision by]

## Attachments and evidence links

- [evaluation run ID and case set version]
- [trace references]
- [synthetic fixtures location]
- [related reports from other engagements]
```

## Completion checks

- [ ] The report covers one issue, with one classification and one receiving team.
- [ ] At least one reproducible case records input, expected and observed result, model, prompt, tool or retrieval versions, and a trace reference.
- [ ] Inputs are synthetic or redacted; no customer confidential data appears, and the check is signed.
- [ ] Frequency, conditions, business impact, workaround cost, and gate impact are stated with denominators and sources.
- [ ] Priority is justified by customers affected, revenue or risk, and evidence quality, and the report names its owner.
