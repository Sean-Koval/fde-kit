# Module 06: Customer craft and communication

## Outcome

You can state the same facts at three altitudes without changing them: a decision-first readout a sponsor reads in two minutes, an operator briefing that says what changes at the desk on Monday, and a field report that gives a product or research team one reproducible case. You can also hold the two conversations that decide whether an engagement survives its expectations: why the demo is not in production yet, and why the system will not also do X.

## Prerequisites

- The evaluation pack from [module 04](04-evaluation-engineering.md) and the rollout and operating plans from [module 05](05-production-and-day-two.md); this module writes from their numbers and invents none.
- One failure from your error analysis that you can reproduce or describe precisely.
- A reviewer willing to play the sponsor for twenty minutes.

## Study

Read in this order.

1. [Executive communication and expectation management](../../skills/executive-communication.md): altitude, decision-first structure, evidence and limits together, capability expectations, and saying no with a reason and an alternative.
2. The workshop sections of [Discovery interviewing and workshop facilitation](../../skills/discovery-interviewing.md): how to run a room toward a decision rather than a discussion; a readout is a workshop compressed into a page.
3. [Executive readout](../../toolkit/executive-readout.md): the template; it opens with the decision requested and puts limits beside results, not in an appendix.
4. [Field report](../../toolkit/field-report.md): the format for sending signal upstream with a reproducible case, system version, and observed versus expected behavior.
5. [Expand](../../stages/07-expand/README.md) stage page: the failure mode of treating enthusiasm as expansion evidence, which is what "can it also do X" is about.
6. Section 7 and the "Limitations" section of the [invoice-intake example](../../examples/invoice-intake-ai/README.md): three separate decisions (expand, hold, stop) from one body of evidence, each with a reason, and a limitations list that says what the numbers do not prove.

Where to practice with real tooling: pull the field report's case (trace identifier, input, system version, output) from your module 05 tracing rather than retyping it.

## Exercise

Produce four pieces from the module 04 and 05 results. Every number must trace to those artifacts; if you lack one, write "not measured" and say how it would be.

1. **Executive readout, one page.** Open with the decision you are asking the sponsor to make. Follow with results against the charter's targets (met, missed, not yet measurable), the evidence basis and its uncertainty, the limits (what the result does not prove), remaining risks and their owners, and the next gate with date and owner. As a starting heuristic, not an industry standard, the reader should reach the decision, the strongest number, and the biggest limit within the first 100 words.
2. **Operator version.** The same facts for daily users: what changes in their queue, what the system will and will not do, what to do when it abstains, how to report a bad output, who to call, and what is measured about their work and why. No new claims, no softened limits.
3. **Field report.** Take one failure from your error analysis: system version, exact input (redacted as the security review requires), expected behavior, observed behavior, frequency in your case set, business consequence, your cause classification, and what you have already tried. A reader with no context should be able to reproduce it.
4. **Two hard conversations, written.** For each, write the question as the sponsor would ask it, then your response in the words you would say, at most half a page.
   - "The demo worked. Why is it not in production?" Name the gate the system is at, the evidence that gate requires, what has been measured so far, and the date of the next decision. Do not apologize for the gate.
   - "Can it also do X?" Pick an X adjacent to your wedge (in the invoice example, bank-detail changes). Separate the request from the current rollout, name what would have to be discovered and measured first, and offer the path: a scorecard entry with an owner and a date.

Rehearse both aloud with your reviewer as the sponsor. Ask them to push once on each; note where your answer went vague and fix that sentence.

## Assessment

| Criterion | Developing | Solid | Strong |
| --- | --- | --- | --- |
| Decision-first structure | Narrates the project; the ask is at the end or absent | Opens with the decision requested; results against targets follow | Decision, strongest number, and biggest limit within the first 100 words; every later section supports the ask |
| Evidence and limits together | Results without basis; limits omitted or buried | Each result names its basis and uncertainty; a limits section exists | Limits sit beside the results they qualify; the readout says what would change the decision |
| Altitude consistency | Operator version adds claims or softens limits | Same facts at both altitudes | The operator version answers what operators actually ask (abstain, report, escalate) and a sponsor would not read it as a different story |
| Field report reproducibility | A complaint with no case | Version, input, expected, observed, and frequency | Reproducible from the report alone, with cause classified and prior attempts listed |
| Hard conversations | Defensive, or agrees to scope to keep the peace | Names the gate and evidence; separates the request from the rollout | Gives the sponsor a decision and a date in both, and says no to unsafe scope with an alternative path |

Solid on every row is the bar for the capstone, whose rubric scores communication and honesty together; a readout that hides a limit fails both.

## Next

[Module 07: Capstone](07-capstone.md) runs a fictional engagement end to end on a scenario you did not choose; everything from modules 02 to 06 is produced again, faster, and scored with a weighted rubric.
