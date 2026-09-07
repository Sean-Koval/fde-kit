# Module 01: The role and the operating model

## Outcome

You can explain what an AI forward deployed engineer (FDE) is accountable for, state the seven-move operating model in your own words, and apply it to a workflow you know well enough to name the accountable owner, the system of record, and the first wedge. The module produces a one-page explanation a reviewer can check for evidence rather than assertion.

## Prerequisites

- Read the [curriculum README](README.md) and decide who reviews your artifacts.
- Pick one workflow you know from the inside: something you have done, supported, or observed for weeks. Ticket triage, expense approval, contract review, and incident response all work; a workflow you know only from a product demo does not.
- Clone or download the repository so you can open the deck locally; GitHub renders its HTML as source.

## Study

Read in this order; about two hours as a starting heuristic, not an industry standard.

1. [What is an FDE?](../what-is-an-fde.md): defines the accountability (a valuable outcome in use, sustained by the customer) that every later module measures against.
2. [Operating principles](../operating-principles.md): the habits the rubrics in this curriculum keep testing, especially "make evidence visible" and "start with the work, not the solution".
3. [Engagement lifecycle](../engagement-lifecycle.md): the seven stages, what uncertainty each resolves, and when a team loops back; the curriculum follows this order.
4. [AI system patterns](../system-patterns.md): the five reference shapes an AI system takes, so that "first wedge" means a pattern, not a slogan.
5. The [AI Implementation Field Playbook](../presentations/fde-overview.html), opened locally: the seven moves (find leverage, map reality, design the boundary, prove quality, land production, transfer ownership, compound learning) and the artifact each produces. Read the speaker notes.
6. The "Engagement at a glance" and "Limitations and what the evidence does not prove" sections of the [invoice-intake example](../../examples/invoice-intake-ai/README.md): the first is a completed engagement record in one table; the second is the honesty standard, a result that states what it does not prove.

Where to practice with real tooling: not yet. For a head start, write down where your workflow's state actually lives (a queue, a table, an inbox); module 02 starts there.

## Exercise

Write one page (about 500 words) that applies the seven-move operating model to your chosen workflow, using this structure:

1. **The workflow in one sentence.** Trigger, actor, outcome, and volume; label the volume as measured or estimated.
2. **Accountable owner.** The role whose measure changes if the workflow improves or breaks, not the person who asked for AI. Say how you know.
3. **System of record.** Where authoritative state lives and which system wins if a document and the record disagree.
4. **The seven moves, one short paragraph each:** find leverage (which step carries the pain and what evidence shows it); map reality (the exception the happy path hides); design the boundary (what AI interprets, what software checks, what a human decides); prove quality (the case type most expensive to get wrong); land production (the safest starting state and why); transfer ownership (who runs it on Day 2); compound learning (the measured signal that would justify or refuse expansion).
5. **First wedge.** The smallest slice that could create measurable value, one explicit exclusion, and the [system pattern](../system-patterns.md) it uses.
6. **What you do not know.** Three facts you would need to observe before recommending anything, and how you would get each.

Compare the page to the "Engagement at a glance" table: every row there should have a counterpart, even one that says "unknown; would measure by ...".

## Assessment

Score each criterion and name the evidence in your page that supports the level; a reviewer should be able to disagree using the same evidence.

| Criterion | Developing | Solid | Strong |
| --- | --- | --- | --- |
| Evidence over assertion | Pain and value are asserted ("it is slow", "AI would help") | Each claim names a source: a count, a record, an observed case, or a labeled estimate | Claims are separated into observed, estimated, and assumed, and the page says which assumption would reverse the recommendation |
| Boundary clarity | AI, software, and human responsibilities are blended ("the agent handles it") | Interpretation, validation, decision, and action each have a named owner type | The boundary names the deterministic check and the human decision for the costliest failure, and states what happens when evidence is missing |
| Owner and system of record | Owner is the requester; system of record is not stated | Both are named with a reason | Page states which system wins on conflict and who resolves the exception |
| Wedge discipline | The wedge is the whole workflow or a demo | Bounded, with one exclusion and a pattern | The smallest slice that still produces a measurable signal, and the page names the signal |
| Honest limits | No unknowns listed, or unknowns are generic | Three specific unknowns with a way to resolve each | Unknowns are ranked by how much they could change the decision, mirroring the example's limitations section |

Solid on every row is ready for module 02. Developing on boundary clarity or honest limits means rewrite before moving on; the rest of the curriculum depends on those two habits.

## Next

[Module 02: Discovery and framing](02-discovery-and-framing.md) turns the unknowns you listed into workflow traces, interviews, and a pilot charter for the same workflow. Keep this page; module 07 asks you to compare it with your capstone.
