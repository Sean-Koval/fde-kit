# FDE skills

Skills is a curated catalog and contribution contract for reusable instructional capabilities that span multiple lifecycle stages. Published skill guides teach **how to perform a capability well**. A skill guide is not a downloadable artifact: use the [toolkit](../toolkit/README.md) for published reusable artifacts, [examples](../examples/README.md) for published completed work, and [agent skills](../agents/README.md) to run a method inside an agent harness.

## Published guides

### Method: choosing and landing the workflow

| Guide | Useful stages |
| --- | --- |
| [Workflow discovery and opportunity framing](workflow-discovery.md) | [Discover](../stages/01-discover/README.md), [Frame](../stages/02-frame/README.md), [Expand](../stages/07-expand/README.md) |
| [Human, software, and AI system design](ai-system-design.md) | [Design](../stages/03-design/README.md), [Build](../stages/04-build/README.md), [Deploy](../stages/05-deploy/README.md), [Enable](../stages/06-enable/README.md) |
| [Evaluation and staged rollout](evaluation-and-rollout.md) | [Design](../stages/03-design/README.md), [Build](../stages/04-build/README.md), [Deploy](../stages/05-deploy/README.md), [Enable](../stages/06-enable/README.md) |
| [Adoption, operations, and product feedback](adoption-and-feedback.md) | [Deploy](../stages/05-deploy/README.md), [Enable](../stages/06-enable/README.md), [Expand](../stages/07-expand/README.md) |

### Technical: building the AI part well

| Guide | Useful stages |
| --- | --- |
| [Context engineering and prompt design](context-engineering.md) | [Design](../stages/03-design/README.md), [Build](../stages/04-build/README.md), [Enable](../stages/06-enable/README.md) |
| [Designing tool-using agents](agent-and-tool-design.md) | [Design](../stages/03-design/README.md), [Build](../stages/04-build/README.md), [Deploy](../stages/05-deploy/README.md) |
| [Retrieval and grounding](retrieval-and-grounding.md) | [Design](../stages/03-design/README.md), [Build](../stages/04-build/README.md), [Enable](../stages/06-enable/README.md) |
| [Grader design and error analysis](eval-engineering.md) | [Design](../stages/03-design/README.md), [Build](../stages/04-build/README.md), [Deploy](../stages/05-deploy/README.md), [Enable](../stages/06-enable/README.md) |
| [Production readiness for LLM systems](production-readiness.md) | [Build](../stages/04-build/README.md), [Deploy](../stages/05-deploy/README.md), [Enable](../stages/06-enable/README.md) |

### Customer craft: running the engagement

| Guide | Useful stages |
| --- | --- |
| [Discovery interviewing and workshop facilitation](discovery-interviewing.md) | [Discover](../stages/01-discover/README.md), [Frame](../stages/02-frame/README.md), [Expand](../stages/07-expand/README.md) |
| [Executive communication and expectation management](executive-communication.md) | [Frame](../stages/02-frame/README.md), [Deploy](../stages/05-deploy/README.md), [Enable](../stages/06-enable/README.md), [Expand](../stages/07-expand/README.md) |

Read the guides in the order the [curriculum](../learning/curriculum/README.md) sequences them if you are learning the role; jump to the guide a [stage page](../stages/README.md) names if you are in an engagement.

## Future candidates

- Technical decision recording across [Build](../stages/04-build/README.md) and [Deploy](../stages/05-deploy/README.md).
- Migrating a workflow between model versions across [Build](../stages/04-build/README.md) and [Enable](../stages/06-enable/README.md), once the production-readiness guide's model-lifecycle section proves insufficient on its own.

## Required guide structure

Every skill guide must include:

- **Relevance:** the capability, why it matters, and the situations in which it is useful.
- **Timing:** when in the lifecycle to apply it.
- **Technique:** a repeatable method for applying the capability.
- **Examples:** good and weak patterns that make the technique concrete.
- **Practice:** an exercise that applies the technique.
- **Self-assessment:** a rubric for evaluating the result.
- **Links:** the applicable [lifecycle stages](../stages/README.md) and relevant [toolkit assets](../toolkit/README.md).

Add a skill only when it teaches a capability that can be reused across engagements. Keep stage-specific sequencing in the [stage playbook](../stages/README.md), and put directly reusable materials in the [toolkit](../toolkit/README.md). See [CONTRIBUTING.md](../CONTRIBUTING.md) for the quality bar; `scripts/check_schemas.py` enforces the structure.
