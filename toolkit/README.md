# FDE toolkit

The toolkit is a curated catalog and contribution contract for directly reusable field artifacts. Published toolkit items answer **what can I use right now**. A toolkit item is not an instructional guide: use [skills](../skills/README.md) to learn the reusable capability behind it, [examples](../examples/README.md) to see published completed engagement outputs, and [agent skills](../agents/README.md) to have an agent harness fill an artifact with you.

## Field artifacts

### Choosing and framing the workflow

| Artifact | Use it to | Useful stages |
| --- | --- | --- |
| [Discovery interview guide](discovery-interview-guide.md) | Plan and run interviews by role and capture evidence, not opinions. | [Discover](../stages/01-discover/README.md), [Frame](../stages/02-frame/README.md), [Expand](../stages/07-expand/README.md) |
| [Workflow trace](workflow-trace.md) | Observe real cases, exceptions, evidence, and controls before designing change. | [Discover](../stages/01-discover/README.md), [Frame](../stages/02-frame/README.md), [Design](../stages/03-design/README.md) |
| [Stakeholder map](stakeholder-map.md) | Record who decides, who can stop the work, what each person needs, and how to engage them. | [Discover](../stages/01-discover/README.md), [Frame](../stages/02-frame/README.md), [Deploy](../stages/05-deploy/README.md), [Enable](../stages/06-enable/README.md) |
| [Opportunity scorecard](opportunity-scorecard.md) | Compare workflow investments using evidence, risk, and ownership. | [Discover](../stages/01-discover/README.md), [Frame](../stages/02-frame/README.md), [Expand](../stages/07-expand/README.md) |
| [Pilot charter](pilot-charter.md) | Agree the wedge, cohort, predeclared criteria, prerequisites, owners, and end states before a pilot starts. | [Frame](../stages/02-frame/README.md), [Design](../stages/03-design/README.md), [Deploy](../stages/05-deploy/README.md) |
| [Business case](business-case.md) | Decide whether to invest, continue, improve, pause, or expand from measured value. | [Frame](../stages/02-frame/README.md), [Deploy](../stages/05-deploy/README.md), [Enable](../stages/06-enable/README.md), [Expand](../stages/07-expand/README.md) |

### Designing, proving, and landing the system

| Artifact | Use it to | Useful stages |
| --- | --- | --- |
| [Responsibility matrix](responsibility-matrix.md) | Set human, software, and AI boundaries with controls and recovery behavior. | [Design](../stages/03-design/README.md), [Build](../stages/04-build/README.md), [Deploy](../stages/05-deploy/README.md), [Enable](../stages/06-enable/README.md) |
| [AI security and governance review](ai-security-review.md) | Enter an enterprise security review prepared with data handling, threats, controls, evidence, and owners. | [Design](../stages/03-design/README.md), [Build](../stages/04-build/README.md), [Deploy](../stages/05-deploy/README.md) |
| [Evaluation pack](evaluation-pack.md) | Build release evidence from representative cases and production failures. | [Design](../stages/03-design/README.md), [Build](../stages/04-build/README.md), [Deploy](../stages/05-deploy/README.md), [Enable](../stages/06-enable/README.md) |
| [Rollout plan](rollout-plan.md) | Advance autonomy through evidence gates with clear rollback. | [Build](../stages/04-build/README.md), [Deploy](../stages/05-deploy/README.md), [Enable](../stages/06-enable/README.md) |
| [Operating plan](operating-plan.md) | Transfer Day 2 ownership, monitoring, change control, and learning. | [Deploy](../stages/05-deploy/README.md), [Enable](../stages/06-enable/README.md), [Expand](../stages/07-expand/README.md) |

### Communicating and sending signal

| Artifact | Use it to | Useful stages |
| --- | --- | --- |
| [Executive readout](executive-readout.md) | Give sponsors a decision-first, one-page view of outcome, evidence, limits, and asks. | [Frame](../stages/02-frame/README.md), [Deploy](../stages/05-deploy/README.md), [Enable](../stages/06-enable/README.md), [Expand](../stages/07-expand/README.md) |
| [Field report](field-report.md) | Send a reproducible model, product, or platform issue upstream to your own organization. | [Build](../stages/04-build/README.md), [Enable](../stages/06-enable/README.md), [Expand](../stages/07-expand/README.md) |

The [invoice-intake example](../examples/invoice-intake-ai/README.md) shows the first seven artifacts completed for one engagement.

## Required artifact metadata

Every toolkit artifact must state:

- **Purpose:** the decision or work the artifact supports.
- **Timing:** when to use it in an engagement.
- **Instructions:** how to complete or apply it.
- **Expected output:** the result a user should produce.
- **Supported stages:** the applicable [lifecycle stages](../stages/README.md).
- **Template:** a copy-ready starting point that elicits decisions and evidence.
- **Completion checks:** the conditions that make the artifact ready to use or review.

Add an artifact only when an FDE can use it directly in field work. Keep reusable methods and judgment in [skills](../skills/README.md), and keep completed engagement artifacts in [examples](../examples/README.md). See [CONTRIBUTING.md](../CONTRIBUTING.md) for the quality bar; `scripts/check_schemas.py` enforces the structure.
