---
name: fde-security-review
description: Use when preparing an LLM system for an enterprise security and governance review with data handling, threats, controls, evidence, and owners.
---

# AI security and governance review

Fills the [AI security and governance review](../../../toolkit/ai-security-review.md) template. Judgment comes from [Production readiness for LLM systems](../../../skills/production-readiness.md), [Designing tool-using agents](../../../skills/agent-and-tool-design.md), and [Retrieval and grounding](../../../skills/retrieval-and-grounding.md).

## Use when

- Design or Build is ahead of the customer's security review and the team wants to arrive with evidence, not assurances.
- Deploy is gated on a review, or a reviewer's questionnaire must be answered from the system as built.
- Never as a substitute for the customer's review; the reviewer decides.

## Obtain first

- [ ] System version, the responsibility matrix, and every hop from input to output to log.
- [ ] Data classification, residency, and retention per hop, with policy identifiers.
- [ ] The model provider's contractual terms as the customer holds them: data use, retention, region, subprocessors.
- [ ] Tool inventory with permission tier, credential scope, and rate limits; retrieval sources and how entitlements are enforced at query time.
- [ ] Prompt and output logging: what, where, who can read it, retention.
- [ ] Safety evaluation evidence: adversarial and prompt-injection cases run, with evaluation pack identifier and results.
- [ ] Incident response: kill switch, on-call owners, escalation path, last rehearsal date.
- [ ] Prior findings, the reviewer's questionnaire if any, and named control owners.

## Procedure

1. Confirm the inputs. A missing classification or contract reference blocks its section; mark the gap and continue.
2. Map the data flow hop by hop with classification, residency, and retention; flag any hop where data crosses a region or leaves the customer's control.
3. Enumerate threats against the system as built, at minimum: prompt injection through retrieved and tool-returned content (agent guide, technique step 8), permission escalation through tools, exfiltration through outputs or logs, over-retention, provider-terms conflicts, and unsafe outputs reaching a person or a system of record.
4. For each threat, record the control, its evidence (test result, configuration reference, policy identifier), owner, and status. A control without evidence is `claimed`, not `in place`.
5. Record safety evaluation results by evaluation pack identifier and name the threat classes with no coverage.
6. Complete incident response with kill switch, owners, escalation path, and rehearsal evidence; an unrehearsed kill switch is a gap.
7. List residual risks with the owner who must accept each, and open items with owner and date.
8. Run the completion checks and print the summary line.

## Output

Fill the Template section of [ai-security-review.md](../../../toolkit/ai-security-review.md). Save to `docs/engagement/<workflow>/ai-security-review-<version>.md` in the user's repository.

Print: `Security review <workflow> <version>: <n> threats; controls <n in place, n claimed, n missing>; <n> residual risks awaiting acceptance; incident response <rehearsed date or open>; <n> gaps.`

## Rules

- No invented facts: controls, terms, classifications, and results come from inputs or cited records.
- Missing inputs become `[gap: what is missing and who can supply it]`.
- Rule-of-thumb numbers are labeled starting heuristics, not industry standards; policy requirements are cited by identifier.
- Reference configurations, contracts, and logs by identifier; no credentials, record contents, personal data, or working injection payloads in the review.
- Accepting residual risk belongs to the risk/control owner and the reviewer. The skill prepares; it does not approve.

## Completion checks

- [ ] Data classification, residency, and retention are recorded for every hop from input through output and logs.
- [ ] Prompt injection through retrieved and tool-returned content, tool permission scoping, prompt and output logging, model-provider terms, safety evaluation, and incident response are each covered.
- [ ] Every control has evidence, an owner, and a status; claimed controls are distinguished from controls in place.
- [ ] Residual risks and open items have a named owner and a date.
- [ ] The kill switch and incident owners are named, and the last rehearsal is recorded or marked open.
