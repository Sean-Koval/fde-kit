# AI security and governance review

## Purpose

Enter an enterprise security review of a large language model (LLM) system prepared: the controls exist, the evidence that they work is attached, and every control has a named owner. The review covers data handling, model-provider terms, identity and access, LLM-specific threats, adversarial evaluation, logging, incident response, and inherited compliance controls. It records what has been tested and configured, not what the team intends.

## Timing

Draft during [Design](../stages/03-design/README.md) as soon as data flows, tools, and the model access path are known, so security and privacy owners shape the boundary instead of vetoing it later. Complete the evidence during [Build](../stages/04-build/README.md). Obtain sign-off before the first gate in [Deploy](../stages/05-deploy/README.md) that exposes real data or real actions, and reopen the review whenever a tool, data class, provider, model, or autonomy limit changes.

## Instructions

1. Name the customer's security, privacy or legal, business, and technical reviewers in the first week of Design and ask for the questionnaire or control framework they apply. Map this template onto it rather than running a parallel process.
2. Describe the system as data flows: each data class, where it originates, which components read it, where it rests, and which environment carries it. Reuse the tools, permissions, and approval points recorded in the [responsibility matrix](responsibility-matrix.md) so both documents use the same identifiers.
3. Fill the data-handling table for every class, including traces, logs, and embeddings. A class with no stated retention or reader list is a finding, not a blank.
4. Obtain the model-provider terms in writing and name the document. A claim that cannot be traced to a contract, order form, or published terms is recorded as unverified.
5. Complete the threat table. The review is evidence-based: evidence means a test result, a configuration export, a contract clause, or a trace, never an assertion. Prompt-level mitigations (instructions telling the model to ignore injected text or refuse a request) may be listed as defense in depth but never count as a control on their own, because the model cannot be relied on to enforce them.
6. Add adversarial cases to the [evaluation pack](evaluation-pack.md) and record results here. Starting heuristic, not an industry standard: at least 10 cases per applicable threat row, rerun on every prompt, model, tool, or retrieval change.
7. Record open findings with severity, owner, and due date, and state which gate in the [rollout plan](rollout-plan.md) each blocks. A gate does not open with an unaccepted blocking finding.
8. Collect sign-off from all four roles and file the review with the [operating plan](operating-plan.md) so change control reopens it. The [production readiness](../skills/production-readiness.md) and [designing tool-using agents](../skills/agent-and-tool-design.md) guides explain the mechanisms behind the controls.

## Expected output

A signed review record listing every data class, provider term, identity control, and LLM-specific threat with its control, evidence, owner, and status; adversarial evaluation results; and the open findings that gate rollout.

## Supported stages

- [Design](../stages/03-design/README.md)
- [Build](../stages/04-build/README.md)
- [Deploy](../stages/05-deploy/README.md)

## Template

```markdown
# AI security and governance review — [system and version]

## Review record

- **Review owner:** [name and role]
- **Customer reviewers:** [security; privacy or legal; business; technical — names]
- **Framework or questionnaire applied:** [customer document and version]
- **Dates:** [drafted; evidence complete; sign-off — YYYY-MM-DD]
- **Reopen triggers:** [new tool, data class, provider, model, autonomy change, or incident]

## System description

- **Workflow and actors:** [outcome; end users, reviewers, operators, service accounts]
- **Model access path:** [application → gateway → provider endpoint; region; authentication]
- **Environments:** [development, evaluation, staging, production; which hold real data]

| Data flow | Source | Read by | Rests in | Environment | Crosses trust boundary |
| --- | --- | --- | --- | --- | --- |
| [prompt, document, tool result] | [origin] | [components] | [store] | [environment] | [yes/no; which] |

| Tool | Permission granted | Scope or allowlist | Reversible | Approval required |
| --- | --- | --- | --- | --- |
| [name] | [read/write/execute on what] | [records, endpoints, actions] | [yes/no] | [none / deterministic check / human] |

## Data handling

| Data class | Classification | Residency | Retention | Who can read it | Control | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Prompts | [class] | [region] | [duration; deletion method] | [roles] | [encryption, access policy] | [configuration export] |
| Retrieved evidence | [class] | [region] | [duration] | [roles] | [control] | [evidence] |
| Tool inputs and outputs | [class] | [region] | [duration] | [roles] | [control] | [evidence] |
| Model outputs | [class] | [region] | [duration] | [roles] | [control] | [evidence] |
| Traces and logs | [class] | [region] | [duration] | [roles] | [redaction; access control] | [evidence] |
| Embeddings | [class of source text] | [region] | [deleted with source] | [roles] | [control] | [evidence] |

## Model-provider terms

| Term | Value | Evidence document | Contractual control | Owner |
| --- | --- | --- | --- | --- |
| Inputs used for training | [yes / no / opt-out status] | [contract, order form, or published terms; section] | [clause] | [name] |
| Retention window | [duration; zero retention if contracted] | [document; section] | [clause] | [name] |
| Processing region | [region; failover region] | [document; section] | [clause] | [name] |
| Sub-processors | [list or link] | [document; section] | [notification clause] | [name] |

## Identity and access

| Concern | Design | Evidence | Owner | Status |
| --- | --- | --- | --- | --- |
| User identity propagation to retrieval and tools | [carried end to end / shared service account and why] | [test: user A cannot reach user B's records] | [name] | [verified/open] |
| Entitlement filtering at query time | [applied inside retrieval, not after generation] | [test with a restricted document] | [name] | [status] |
| Agent credentials | [least privilege; per-tool allowlist] | [permission audit export] | [name] | [status] |
| Secrets handling | [vault; rotation; never in prompts, outputs, or logs] | [scan result] | [name] | [status] |

## Threat table

| Threat | Control | Evidence | Owner | Status |
| --- | --- | --- | --- | --- |
| Direct prompt injection | [output validation; deterministic tool gating] | [cases passed/total; run ID] | [name] | [status] |
| Indirect injection through retrieved documents and tool results | [retrieved content treated as data; tool calls authorized outside the model] | [cases passed/total; run ID] | [name] | [status] |
| Data exfiltration through tool calls or generated links | [egress allowlist; no fetch or render of model-generated links] | [cases passed/total; network policy export] | [name] | [status] |
| Over-permissioned tools | [scoped credentials; allowlist review on change] | [permission audit; date] | [name] | [status] |
| Unsafe or irreversible actions | [human approval; idempotency; compensating action] | [responsibility matrix row; rehearsal record] | [name] | [status] |
| Personal-data leakage in logs | [redaction before storage; trace access control] | [redaction test; stored-trace sample audit] | [name] | [status] |
| Cost or denial abuse | [rate limits; step and token budgets; per-user quotas] | [load test; configuration] | [name] | [status] |
| Corpus poisoning | [source allowlist; ingestion review; provenance] | [test with a planted document] | [name] | [status] |
| Model output used as authority | [system of record enforces state; deterministic checks; citations required] | [control recall from evaluation pack] | [name] | [status] |

## Safety and adversarial evaluation

- **Case set, version, and run:** [identifier; run ID; date; system version]

| Threat row | Cases | Passed | Failed | Failure handling | Regression added |
| --- | --- | --- | --- | --- | --- |
| [threat] | [count] | [count] | [count] | [fix, hold, or accepted by name] | [yes/no] |

## Logging, audit, and monitoring

- **Logged:** [prompts, retrieved evidence, tool calls and results, outputs, approvals, trace IDs]
- **Redaction:** [what is masked before storage; method; test]
- **Reviewer and cadence:** [name; sample size; what they look for]
- **Alerting:** [signal, threshold, first responder for policy, exfiltration, cost, and tool errors]

## Incident response

- **Kill switch:** [what it disables; who can invoke it; rehearsal date and duration]
- **Manual fallback:** [workflow users follow when the system is off]
- **Evidence preservation:** [traces, inputs, outputs, tool calls; where; by whom]
- **Notification obligations:** [internal owners, provider, regulator, affected users; deadline; owner]

## Inherited compliance controls (as applicable)

| Control area | Existing customer control | Applies | Gap | Owner |
| --- | --- | --- | --- | --- |
| [access, encryption, logging, vendor management, retention] | [control ID or framework reference the customer holds] | [yes/partly/no] | [gap] | [name] |

## Open findings

| ID | Finding | Severity | Blocks gate | Owner | Due date | Status |
| --- | --- | --- | --- | --- | --- | --- |
| [ID] | [finding] | [critical/high/medium/low] | [gate or none] | [name] | [YYYY-MM-DD] | [open/accepted/closed] |

## Sign-off

| Role | Name | Decision | Conditions | Date |
| --- | --- | --- | --- | --- |
| Security | [name] | [approve/conditional/reject] | [conditions] | [YYYY-MM-DD] |
| Privacy or legal | [name] | [decision] | [conditions] | [YYYY-MM-DD] |
| Business | [name] | [decision] | [conditions] | [YYYY-MM-DD] |
| Technical | [name] | [decision] | [conditions] | [YYYY-MM-DD] |
```

## Completion checks

- [ ] Every data class, including traces, logs, and embeddings, has classification, residency, retention, reader list, control, and evidence.
- [ ] Model-provider terms cite a named contract, order form, or published document for training use, retention, region, and sub-processors.
- [ ] Every threat row has a control enforced outside the prompt, with test, configuration, contract, or trace evidence and a named owner.
- [ ] Adversarial cases are in the evaluation pack with recorded results and a rerun trigger.
- [ ] Open findings have severity, owner, due date, and the gate they block; sign-off from all four roles is recorded or explicitly open.
