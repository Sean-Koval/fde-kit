# Module 03: System design: boundaries, context, tools, retrieval

## Outcome

You can design the system around the model call for a chartered wedge: which responsibilities go to AI, deterministic software, and accountable humans; which reference pattern fits and why; what the model must return, including when it must abstain; what tools it may call with which permissions; and what an enterprise security reviewer will ask before production. The module produces a design package a reviewer can attack row by row.

## Prerequisites

- The pilot charter and exception trace from [module 02](02-discovery-and-framing.md).
- Model access with structured output (a JSON schema the response must satisfy), if available; otherwise the exercise says what to write instead.

## Study

Read in this order.

1. [Human, software, and AI system design](../../skills/ai-system-design.md): the least-fragile-owner rule and the decomposition into interpretation, validation, decision, action, and recovery; everything else here hangs off it.
2. [AI system patterns](../system-patterns.md): the five reference shapes with diagrams, boundary notes, and evaluation notes; you will choose one and defend it.
3. [Context engineering and prompt design](../../skills/context-engineering.md): what belongs in the context window, instruction versus evidence, the output contract, and prompts as versioned code.
4. [Designing tool-using agents](../../skills/agent-and-tool-design.md): tool contracts, permission tiers, approval points, stopping rules, and budgets; read it even if your wedge has no tools, because it explains why not to add any.
5. [Retrieval and grounding](../../skills/retrieval-and-grounding.md): when retrieval beats long context or tuning, citations, and permissions-aware retrieval; where most quiet assistant failures start.
6. [Responsibility matrix](../../toolkit/responsibility-matrix.md): the template that records the boundary with failure behavior and an owner per row.
7. [AI security and governance review](../../toolkit/ai-security-review.md): prompt injection through retrieved or tool-returned content, data classification, logging and retention, provider terms, incident response; the questions asked before Deploy.
8. [Design](../../stages/03-design/README.md) stage page: exit criteria, and the failure mode of designing a complete future state before validating the riskiest assumption.
9. Section 3 of the [invoice-intake example](../../examples/invoice-intake-ai/README.md): the architecture sketch, a matrix where AI never makes an authoritative decision, and a kill switch that returns every case to the existing queue.

Where to practice with real tooling: implement the output contract as a schema and call a model with structured output on five cases from your traces, including the exception. What the model does with a field it cannot find shapes your abstain value more than any reading.

## Exercise

For the chartered wedge from module 02, produce a design package with five parts.

1. **Responsibility matrix.** Decompose the wedge into interpretation, validation, decision, action, and recovery. Per row: AI, deterministic software, or human; required evidence; escalation trigger; failure behavior; owner. Test each row against the exception trace: what happens when the source document and the system of record disagree?
2. **Pattern choice.** Pick one [system pattern](../system-patterns.md). In half a page, say why it fits, which alternative you rejected, and what trace evidence would change the choice. As a starting heuristic, not an industry standard, a wedge that needs a tool-using agent on day one has not been narrowed enough; start with the pattern that meets the outcome with the least autonomy.
3. **Output contract.** Write the schema the model must return. Every field has a type, an allowed range or enumeration, and a provenance requirement (source span, record identifier, or retrieved chunk). Include an explicit abstain value per field or per response and state what deterministic code does when it appears. If you ran the model, include the five outputs and what they taught you; if not, write three ways you expect the contract to fail and how each would be detected.
4. **Tool contracts and permission tiers.** If the wedge calls tools, define each: inputs, outputs, side effects, idempotency, and permission tier (read-only, reversible write, or irreversible and high consequence). Name the approval point and the budget (steps, time, cost) after which the loop stops. If there are no tools, say so and why.
5. **First-pass security review.** Complete the template as far as you can. For each unanswered item, write the decision rule for finding the answer and who at the customer owns it.

Design against the costliest failure, not the average case: if a model output can reach an irreversible action without a deterministic check, the design is not finished.

## Assessment

| Criterion | Developing | Solid | Strong |
| --- | --- | --- | --- |
| Boundary rigor | AI "handles" steps; controls are implied | Each responsibility has an owner type, evidence requirement, and failure behavior | Every consequential action passes a deterministic check and has a named human approver; the conflict case is resolved explicitly |
| Pattern justification | Named without alternatives | Reasoned against one rejected alternative | Tied to trace evidence with a stated reversal condition; autonomy is the least that meets the outcome |
| Output contract | Free text or a schema with no abstain path | Typed schema with provenance and an abstain value | Abstain behavior is specified per field, handled by code, and tested against real or predicted model outputs |
| Tool and permission design | Tools have broad access or are undefined | Each tool has a contract and a permission tier | Approval points, budgets, and stopping rules are explicit; unnecessary tools are absent with a reason |
| Security readiness | Not attempted | Template completed with gaps marked | Every gap has a decision rule and an owner; injection through retrieved or tool content is addressed specifically |

Solid on boundary rigor and output contract is the minimum for module 04; graders need a contract to grade against.

## Next

[Module 04: Evaluation engineering](04-evaluation-engineering.md) builds the case set and graders that prove this design does what the matrix claims; the abstain value and provenance fields become gradable criteria.
