# AI FDE curriculum

A sequenced path from understanding the AI forward deployed engineer (FDE) role to running a fictional engagement end to end. Each module reads the kit's practitioner material in order, then makes you produce the artifact a real engagement would need at that point. By the capstone you will have written every artifact from Discover to Expand for a scenario you did not choose and scored it against the [invoice-intake example](../../examples/invoice-intake-ai/README.md).

## Who it is for

- An engineer who wants to become an AI FDE and needs more than a reading list: a sequence, exercises with outputs, and a way to tell whether the output is any good.
- A practitioner filling specific gaps. Jump to the gap, but do the exercise, not only the reading; the artifacts are where the method becomes visible.

It assumes you can write code against a model provider's application programming interface (API), read a JSON schema, and talk with an operations manager without a script.

## How to use it

1. Do the modules in order. Each builds on the previous artifact: module 03 designs the wedge module 02 chartered, and module 06 writes the readout from module 04 and 05 results.
2. Produce the artifact. Every module ends with a concrete output using a [toolkit](../../toolkit/README.md) template. Reading without producing does not complete a module.
3. Score it. Assessments are self-scored rubrics with three levels: developing, solid, strong. For each criterion, name the evidence in your artifact that supports the level.
4. Get it reviewed. A reviewer, such as a peer working through the curriculum, a mentor, or a practitioner who has shipped an AI system to production, makes the rubrics far more useful. Ask them to challenge your evidence, not your formatting. Without a reviewer, swap artifacts with another learner; scoring someone else's work teaches almost as much as writing your own.
5. Keep one folder per engagement. The capstone reuses the structure.

## Expected effort

As a starting heuristic, not an industry standard: six to eight weeks at five to seven hours per week, with the capstone taking about a third of the total. Modules 03 and 04 take longest because they include building against real tooling; recalibrate after module 02.

## Modules

| Number | Title | What you produce |
| --- | --- | --- |
| 01 | [The role and the operating model](01-role-and-operating-model.md) | A one-page explanation of the seven-move operating model applied to a workflow you know |
| 02 | [Discovery and framing](02-discovery-and-framing.md) | Two workflow traces, two interview records, a stakeholder map, a scored opportunity scorecard, a pilot charter |
| 03 | [System design: boundaries, context, tools, retrieval](03-system-design.md) | A responsibility matrix, a justified pattern choice, an output contract with an abstain value, tool contracts and permission tiers, a first-pass security review |
| 04 | [Evaluation engineering](04-evaluation-engineering.md) | A stratified case set, graders, a calibrated judge or its calibration plan, an error-analysis pass, an evaluation pack with a release decision |
| 05 | [Production, rollout, and Day 2](05-production-and-day-two.md) | A rollout plan with gates and signals, an operating plan with Day 2 owners, a rollback rehearsal script |
| 06 | [Customer craft and communication](06-customer-craft.md) | An executive readout, the operator version of the same facts, a field report, written responses to two hard conversations |
| 07 | [Capstone: run a fictional engagement end to end](07-capstone.md) | Every artifact from Discover to Expand for a scenario seed, a limitations section, a weighted self-score |

## What the curriculum does not do

It does not replace building a real system. Written artifacts can be internally consistent and still wrong about how a model, a retrieval index, or an enterprise connector behaves. Every module therefore says where to practice with real tooling: a model API with structured output, a small retrieval index over documents you can inspect, a tracing store you can query, and a case set you run more than once. If you cannot run a model, modules 03 to 05 say what to write instead; your self-score should say so.

It does not certify anyone; a strong capstone score is evidence to show a reviewer or interviewer, not a credential. And it does not teach one vendor's software development kit (SDK): the kit names mechanisms, vendor documentation teaches the API calls.

## Relation to interview preparation

[Interview preparation](../interview-preparation.md) describes the shapes AI FDE interviews take (technical build, large language model (LLM) system design, customer scenario, evidence discussion, behavioral) and reuses the curriculum exercises as drills. Do the curriculum first: the drills assume you have a responsibility matrix, an evaluation pack, and a readout of your own to talk from, because evidence discussions expose rehearsed answers quickly. Module 07 ends with what a strong capstone lets you say in each interview shape.
