---
name: fde-opportunity-scorecard
description: Use when comparing candidate workflows for an AI investment and recording an evidence-backed advance, investigate, defer, or enable-locally decision.
---

# Opportunity scorecard

Fills the [opportunity scorecard](../../../toolkit/opportunity-scorecard.md) template. Judgment comes from [Workflow discovery and opportunity framing](../../../skills/workflow-discovery.md), technique steps 4 to 6.

## Use when

- Discover or Frame has more than one candidate workflow and the sponsor needs a comparison before delivery capacity is committed.
- Expand is reprioritizing from measured outcomes and a new candidate must be compared fairly with the current workflow.
- Not when one preselected demo has no evidence for alternatives. Say so; the artifact is a decision aid, not a justification.

## Obtain first

- [ ] The candidate list: workflow, users, outcome owner, and system of record for each.
- [ ] Per candidate: pain signal, baseline (measure, value, period, source), volume, and evidence reviewed, ideally a [workflow trace](../../../toolkit/workflow-trace.md).
- [ ] Constraints per candidate: data classification, policy or safety consequence, integration dependencies, adoption barriers.
- [ ] The named selection decision owner and the date a decision is needed.
- [ ] Any thresholds the owner has already set for the first evidence gate.

## Procedure

1. Confirm the inputs. A candidate with no baseline and no observed case can be scored, but its scores are assumptions with tests, not evidence.
2. Score one criterion at a time across all candidates, not one candidate at a time, so the standard stays even (see the scoping workshop in [Discovery interviewing](../../../skills/discovery-interviewing.md)). Use the template's 1 to 5 scale, which it labels a starting heuristic.
3. For every score, cite evidence and source and rate confidence. Where evidence is absent, write "assumption" and the test that would settle it.
4. Complete "Constraints and safeguards" for the leading candidate; record an accountable owner only when the user names one.
5. Complete "Comparison and selection". Rank from the scores, then state the rationale as a trade-off in words; a higher total is not a rationale (technique step 4).
6. Draft "Candidate recommendation" with what the evidence supports: advance, investigate, defer, or enable locally (technique step 6). State the smallest first wedge and the missing fact that could reverse the recommendation.
7. Complete "Next evidence gate" with hypothesis, measure, and failure path. Thresholds come from the owner; if none exist, write a gap naming the owner.
8. Record the decision only if the owner has made it; otherwise mark it open and list what the owner needs. Run the completion checks and print the summary line.

## Output

Fill the Template section of [opportunity-scorecard.md](../../../toolkit/opportunity-scorecard.md). Save to `docs/engagement/<workflow>/opportunity-scorecard.md` in the user's repository, where `<workflow>` is the leading candidate or the engagement name.

Print: `Opportunity scorecard: <n> candidates; leading <workflow>; recommendation <advance/investigate/defer/enable locally>; decision <recorded or open>; <n> gaps.`

## Rules

- No invented facts: baselines, volumes, and constraints come from inputs or cited sources.
- Missing inputs become `[gap: what is missing and who can supply it]`.
- Scores are labeled heuristics once, near the first score.
- Reference interviews, logs, and records by identifier; no customer record contents or personal data in the scorecard.
- Selection belongs to the named decision owner. The skill recommends; it does not select.

## Completion checks

- [ ] Candidate workflows are compared in the ranking summary, and the selection decision has a named owner.
- [ ] The selected workflow, affected users, business outcome owner, and first wedge are named.
- [ ] Every score cites evidence or is explicitly marked as an assumption with a test.
- [ ] Safety, data, integration, and adoption constraints have accountable owners.
- [ ] The decision, decision owner, next evidence gate, and failure path are recorded.
