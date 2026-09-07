---
name: fde-security-review
description: Use when preparing an LLM system for an enterprise security and governance review with data handling, threats, controls, evidence, and owners.
---

# AI security and governance review

Fills the [AI security and governance review](../../../toolkit/ai-security-review.md) template. Judgment comes from [Production readiness for LLM systems](../../../skills/production-readiness.md) for guardrails, logging, change control, and incident response; [Designing tool-using agents](../../../skills/agent-and-tool-design.md) for permission tiers and untrusted tool results; and [Retrieval and grounding](../../../skills/retrieval-and-grounding.md) for permissions-aware retrieval.

## Use when

- Design or Build is ahead of the customer's security review and the team wants to arrive with evidence rather than assurances.
- Deploy is gated on a review, or a reviewer has sent a questionnaire the team must answer from the system as built.
- Not as a substitute for the customer's own review. The artifact prepares for it and records the findings; the reviewer decides.

## Obtain first

- [ ] System description and version: the responsibility matrix, the data-flow diagram or a description of every hop from input to output to log.
- [ ] Data classification for each input, retrieved source, tool result, output, and log, plus residency and retention requirements by policy identifier.
- [ ] The model provider's contractual terms as the customer holds them: data use, retention, region, and subprocessors. Reference the contract; do not summarize from memory.
- [ ] Tool inventory with permission tier, credential scope, and rate limits.
- [ ] Retrieval sources with how entitlements are enforced at query time.
- [ ] Logging: what is captured from prompts and outputs, where it is stored, who can read it, and how long it is kept.
- [ ] Safety evaluation evidence: adversarial and prompt-injection cases run, with the evaluation pack identifier and results.
- [ ] Incident response: kill switch, on-call owners, escalation path, and the last rehearsal date.
- [ ] Prior review findings, the reviewer's questionnaire if one exists, and named control owners.

## Procedure

1. Confirm the inputs. A missing data classification or contract reference blocks the corresponding section; mark the gap and continue with the rest.
2. Map the data flow hop by hop and record classification, residency, and retention at each hop. Flag any hop where data crosses a region or leaves the customer's control.
3. Enumerate threats against the system as built, at minimum: prompt injection through retrieved and tool-returned content (agent guide, technique step 8), permission escalation through tools, data exfiltration through outputs or logs, over-retention of prompts and outputs, provider-terms conflicts, and unsafe outputs reaching a person or a system of record.
4. For each threat, record the control, the evidence that the control exists (a test result, a configuration reference, a policy identifier), the owner, and the status. A control without evidence is recorded as `claimed`, not `in place`.
5. Record the safety evaluation results by evaluation pack identifier and note which threat classes have no test coverage.
6. Complete incident response with the kill switch, owners, escalation path, and rehearsal evidence. An unrehearsed kill switch is a gap.
7. List residual risks with the owner who must accept each, and open items with owner and date.
8. Run the completion checks and print the summary line.

## Output

Fill the Template section of [ai-security-review.md](../../../toolkit/ai-security-review.md). Save to `docs/engagement/<workflow>/ai-security-review-<version>.md` in the user's repository.

Print: `Security review <workflow> <version>: <n> threats; controls <n in place, n claimed, n missing>; <n> residual risks awaiting acceptance; incident response <rehearsed on date or open>; <n> gaps.`

## Rules

- No invented facts: controls, terms, classifications, and test results come from inputs or cited records.
- Missing inputs are written as `[gap: what is missing and who can supply it]`.
- Rules of thumb (for example a retention period) are labeled starting heuristics, not industry standards; policy requirements are cited by identifier instead.
- Reference configurations, contracts, and logs by identifier. The review never contains credentials, keys, record contents, personal data, or confidential document text, and never reproduces a working injection payload.
- Acceptance of residual risk belongs to the named risk/control owner and to the customer's reviewer. The skill prepares; it does not accept or approve.

## Completion checks

- [ ] Data classification, residency, and retention are recorded for every hop from input through output and logs.
- [ ] Prompt injection through retrieved and tool-returned content, tool permission scoping, prompt and output logging, model-provider terms, safety evaluation, and incident response are each covered.
- [ ] Every control has evidence, an owner, and a status; claimed controls are distinguished from controls in place.
- [ ] Residual risks and open items have a named owner and a date.
- [ ] The kill switch and incident owners are named, and the last rehearsal is recorded or marked open.
