---
name: fde-security-review
description: Use when preparing an LLM system for an enterprise security and governance review with data handling, threats, controls, evidence, and owners.
---

# AI security and governance review

Fills the [AI security and governance review](../../../toolkit/ai-security-review.md) template. Judgment comes from [Production readiness for LLM systems](../../../skills/production-readiness.md), [Designing tool-using agents](../../../skills/agent-and-tool-design.md), and [Retrieval and grounding](../../../skills/retrieval-and-grounding.md).

## Use when

- The team wants to arrive at the customer's security review with evidence, not assurances.
- A reviewer's questionnaire must be answered from the system as built, or Deploy is gated on the review.
- Never as a substitute for the customer's review; the reviewer decides.

## Obtain first

- [ ] System version, responsibility matrix, and every hop from input to output to log.
- [ ] Classification, residency, and retention per hop, with policy identifiers.
- [ ] Provider terms as the customer holds them: data use, retention, region, subprocessors.
- [ ] Tools with permission tier, credential scope, and rate limits; retrieval sources and query-time entitlement enforcement.
- [ ] Prompt and output logging: what, where, readers, retention.
- [ ] Safety evaluation evidence: adversarial and injection cases run, with evaluation pack identifier and results.
- [ ] Incident response: kill switch, on-call owners, escalation path, last rehearsal.
- [ ] Prior findings, the reviewer's questionnaire, and named control owners.

## Procedure

1. Confirm the inputs. A missing classification or contract reference blocks its section; mark the gap and continue.
2. Map the data flow hop by hop; flag any hop where data crosses a region or leaves the customer's control.
3. Enumerate threats against the system as built, at minimum: prompt injection through retrieved and tool-returned content (agent guide, technique step 8), permission escalation through tools, exfiltration through outputs or logs, over-retention, provider-terms conflicts, and unsafe outputs reaching a person or system of record.
4. For each threat, record control, evidence (test result, configuration reference, policy identifier), owner, and status. Without evidence a control is `claimed`, not `in place`.
5. Record safety evaluation results by pack identifier and name uncovered threat classes.
6. Complete incident response; an unrehearsed kill switch is a gap.
7. List residual risks with the accepting owner, and open items with owner and date.
8. Run the completion checks and print the summary line.

## Output

Fill the Template section of [ai-security-review.md](../../../toolkit/ai-security-review.md). Save to `docs/engagement/<workflow>/ai-security-review-<version>.md` in the user's repository.

Print: `Security review <workflow> <version>: <n> threats; controls <n in place, n claimed, n missing>; <n> residual risks; incident response <rehearsed date or open>; <n> gaps.`

## Rules

- No invented facts: controls, terms, classifications, and results come from inputs or cited records.
- Missing inputs become `[gap: what is missing and who can supply it]`.
- Rule-of-thumb numbers are labeled starting heuristics, not industry standards; requirements are cited by policy identifier.
- Reference configurations, contracts, and logs by identifier; no credentials, record contents, personal data, or working injection payloads.
- Residual-risk acceptance belongs to the risk/control owner and the reviewer. The skill prepares; it does not approve.

## Completion checks

- [ ] Every data class, including traces, logs, and embeddings, has classification, residency, retention, reader list, control, and evidence.
- [ ] Model-provider terms cite a named contract, order form, or published document for training use, retention, region, and sub-processors.
- [ ] Every threat row has a control enforced outside the prompt, with test, configuration, contract, or trace evidence and a named owner.
- [ ] Adversarial cases are in the evaluation pack with recorded results and a rerun trigger.
- [ ] Open findings have severity, owner, due date, and the gate they block; sign-off from all four roles is recorded or explicitly open.
