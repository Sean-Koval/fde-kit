# Module 02: Discovery and framing

## Outcome

You can turn a workflow you know into evidence: observed cases with active time, waits, exceptions, and controls; interview records that separate what people said from what records show; a stakeholder map with decision rights; a scored comparison of candidate wedges; and a pilot charter an owner has agreed to. These artifacts feed every later module.

## Prerequisites

- The one-page explanation from [module 01](01-role-and-operating-model.md), scored at least solid on boundary clarity and honest limits.
- Access to the workflow: observe it, or reconstruct two cases from records (tickets, emails, audit logs) with one operator who will check the reconstruction.
- Two people willing to be interviewed for thirty minutes each, ideally one operator and one outcome owner or approver.

## Study

Read in this order.

1. [Workflow discovery and opportunity framing](../../skills/workflow-discovery.md): the method from symptom to bounded wedge, and the separation of active effort, waiting, rework, and exceptions that the trace depends on.
2. [Discovery interviewing and workshop facilitation](../../skills/discovery-interviewing.md): how to get evidence instead of opinions, and how to synthesize across people who disagree.
3. [Workflow trace](../../toolkit/workflow-trace.md): the per-case template; note the validation step against a second evidence source.
4. [Discovery interview guide](../../toolkit/discovery-interview-guide.md): role-based question sets and the capture format that keeps claims and evidence apart.
5. [Stakeholder map](../../toolkit/stakeholder-map.md): decision rights, incentives, and risk posture; where you learn who can say yes and who can quietly say no.
6. [Opportunity scorecard](../../toolkit/opportunity-scorecard.md): the comparison table and the rule that a score supports a decision rather than replacing the evidence.
7. [Business case](../../toolkit/business-case.md): baseline, counterfactual, and predeclared evidence gate; read it now so the charter's success criteria are ones a business case can later use.
8. [Pilot charter](../../toolkit/pilot-charter.md): hypothesis, wedge, exclusions, success and stop criteria, data access, owners, timeline, and exit; the artifact that ends this module.
9. [Discover](../../stages/01-discover/README.md) and [Frame](../../stages/02-frame/README.md) stage pages: the exit criteria your artifacts must satisfy and the failure modes reviewers check.
10. Sections 1 and 2 of the [invoice-intake example](../../examples/invoice-intake-ai/README.md): a trace validated against a 1,200-record sample, a scorecard that defers vendor onboarding for a stated reason, and measures that each have a baseline, a source, and an owner.

Where to practice with real tooling: export the records behind your workflow (queue timestamps, ticket histories, audit events) and compute the baseline yourself, as the example's 68.0% one-business-day figure was.

## Exercise

Work on the workflow from module 01. Produce five artifacts in this order.

1. **Two workflow traces.** One common case and one costly exception, observed live or reconstructed from records. Per row: actor, system, evidence used, active time, wait time, and the control or exception path. Validate each trace with the operator and a second source; mark contradictions rather than resolving them by assumption. As a starting heuristic, not an industry standard, a trace with no confirming system record is a draft, not evidence.
2. **Two interview records.** Use the interview guide with one operator and one outcome owner. Tag each claim observed, stated, or inferred, and name the record that would confirm it. Write a half-page synthesis naming the two largest disagreements between what people said and what the traces show.
3. **A stakeholder map.** Outcome owner, technical owner, risk or control owner, and anyone who can block deployment, each with decision rights, what they are measured on, and their risk posture toward AI acting in this workflow.
4. **A scored opportunity scorecard** for three candidate wedges in or adjacent to the workflow. Score impact, measurability, delivery fit, readiness, and risk manageability; state the evidence gap for each; choose one with a decision of advance, investigate, or defer and a reason.
5. **A pilot charter** for the chosen wedge: hypothesis, included and excluded cases, success criteria with baselines and sources, stop criteria, data needed and who grants access, owners, timeline, and exit condition. Ask the outcome owner (or your reviewer standing in) to agree or object in writing.

If you cannot observe or interview anyone, reconstruct from records and say so in every artifact; the assessment scores honesty about method above completeness.

## Assessment

| Criterion | Developing | Solid | Strong |
| --- | --- | --- | --- |
| Trace fidelity | Steps are the idealized process; no waits or exceptions | Active time, waits, rework, and exceptions are separated; each step names its system | Both traces are validated against a second source; contradictions are listed, not smoothed over |
| Interview evidence | Records are opinions transcribed as facts | Each claim is tagged observed, stated, or inferred, with a confirming record named | Synthesis names disagreements between interviews and traces and what would resolve each |
| Stakeholder clarity | A list of names and titles | Decision rights, measures, and risk posture per stakeholder | The map names who can block, why, and what evidence would change their posture |
| Wedge selection | One candidate, scored to justify a prior choice | Three candidates scored with evidence gaps; a reasoned decision | Rejected candidates have conditions for reconsideration; the score is visibly subordinate to the evidence |
| Charter discipline | Success is "works well"; no stop criteria | Success and stop criteria have baselines, thresholds, and owners | The charter predeclares how success will be measured and what evidence would send the team back to Discover |

Solid on trace fidelity and charter discipline is the minimum before module 03; design cannot bound what discovery did not observe.

## Next

[Module 03: System design](03-system-design.md) designs the boundary around the chartered wedge: responsibility matrix, pattern, output contract, tools, and a first-pass security review. Bring the exception trace; it decides most of the boundary.
