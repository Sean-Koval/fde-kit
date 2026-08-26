# Workflow discovery and opportunity framing

## Relevance

Use this capability to find a workflow where an AI-enabled change can create measurable value without hiding risk, ownership, or the work people actually do. It is useful when an engagement starts with a broad symptom, a queue of possible opportunities, or a request for an AI demonstration that has not yet been tied to a credible workflow outcome.

## Timing

Start in [Discover](../stages/01-discover/README.md). Carry the evidence into [Frame](../stages/02-frame/README.md), and return to it in [Expand](../stages/07-expand/README.md) when a new workflow or an earlier assumption needs fresh discovery.

## Technique

1. Name the candidate workflow, the outcome owner, and the decision that discovery must inform; do not begin with a model or feature.
2. Observe representative operators completing real cases from trigger to outcome. Capture source records, waits, rework, exceptions, and the evidence behind consequential decisions.
3. Validate the trace with the operator and an independent source such as a system record, policy, or queue history. Mark contradictions and unknowns instead of resolving them by assumption.
4. Compare candidate workflows on impact, measurability, delivery fit, operational readiness, risk manageability, and evidence gaps. A score supports a decision; it does not replace the evidence.
5. Frame the smallest useful wedge: affected users, present pain, desired outcome, success signal, explicit exclusions, and the owner who will decide whether to proceed.
6. Record the next decision as advance, investigate, defer, enable locally, or begin new discovery. State what evidence would change that decision.

## Examples

### Good pattern

An accounts-payable lead observes three invoice-intake cases, including a duplicate invoice and a missing purchase order. The team measures active handling time and wait time separately, identifies the ERP as the authoritative state, and learns that approvers—not data extraction—create the largest delay. It selects a bounded first wedge: extract invoice fields with source citations and route exceptions to the existing review queue. The finance owner agrees to judge success from correction rate, review time, and on-time processing.

### Weak pattern

"Invoices are manual, so we should automate AP with AI." The claim has no observed cases, no baseline, no exception evidence, no system-of-record decision, and no accountable owner. A polished demo may answer a different problem from the one that constrains production work.

## Practice

Choose one recurring workflow. Observe or reconstruct two contrasting cases: one common case and one costly exception. Write a one-sentence candidate problem statement, name one measurable outcome and one exclusion, then decide whether the evidence supports advance, investigate, or defer. Explain which missing fact could reverse the decision.

## Self-assessment

- Can another person follow the evidence from a real case to the chosen first wedge?
- Did the work distinguish active effort, waiting, rework, and exception handling instead of averaging them into one pain claim?
- Are the outcome owner, system of record, major controls, and evidence gaps named?
- Does the recommendation state what is excluded and what decision will be made next?
- Could the same method compare a newly proposed expansion opportunity fairly with the current workflow?

## Links

**Lifecycle stages:** [Discover](../stages/01-discover/README.md), [Frame](../stages/02-frame/README.md), [Expand](../stages/07-expand/README.md).

**Toolkit assets:** [Workflow trace](../toolkit/workflow-trace.md), [Opportunity scorecard](../toolkit/opportunity-scorecard.md), [Business case](../toolkit/business-case.md).
