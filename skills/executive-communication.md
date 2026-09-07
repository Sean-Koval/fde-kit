# Executive communication and expectation management

## Relevance

Use this capability to get a correct decision from people who will not read the evidence pack. It is useful when a sponsor must choose to invest, expand, hold, or stop; when a demo has raised expectations faster than the evidence; when scope must be narrowed or refused; and when results have to travel upward without losing their baseline, denominator, or limits. The same fact base feeds every audience; only the framing changes.

## Timing

Set expectations in [Frame](../stages/02-frame/README.md) when the outcome, targets, and decision rules are agreed. Report against those targets in [Deploy](../stages/05-deploy/README.md) and [Enable](../stages/06-enable/README.md). In [Expand](../stages/07-expand/README.md), deliver the readout that separates the expand, hold, and stop decisions.

## Technique

Every number and duration below is a starting heuristic, not an industry standard.

### 1. Choose the altitude, keep the facts

| Audience | Needs to hear | Does not need | Same fact base, framed as |
| --- | --- | --- | --- |
| Sponsor | Outcome, risk, cost, and the decision they own | Mechanism, prompt details | "Median handling fell from 8.0 to 4.6 minutes; the gate passed; decide expand, hold, or stop." |
| Operators | What changes in their day, what does not, where to get help | Business-case arithmetic | "You still approve every draft; the queue is the same; here is the support channel." |
| Engineers and platform owners | Mechanism, integration, controls, failure behavior | Sponsor narrative | "Structured extraction with source spans, deterministic enterprise resource planning (ERP) checks, idempotent write after approval." |

One fact base, different framings, never different facts. If a sponsor's version and an engineer's version would disagree on a number, the readout is wrong.

### 2. Lead with the decision

Order every readout, spoken or written, the same way: decision needed, recommendation, evidence, limits and risks, ask. A reader who stops after the first two lines should still know what you want and why. Detail follows; it never leads.

### 3. State limits before being asked

Say what the evidence does not prove: cohort, period, document types, seasonality, and anything the system did not do. The [worked example](../examples/invoice-intake-ai/README.md) closes with a limitations section for this reason. A limit you state is credibility; a limit someone else discovers is a surprise, and surprises stall rollouts.

### 4. Manage expectations about model capability

| Expectation you will hear | What to say | Why |
| --- | --- | --- |
| "The demo worked, so it is done." | A demo shows what is possible on chosen inputs; production is measured on a representative case set with a rollback path. | Demo inputs are selected; production inputs are not. |
| "Will it be right?" | Behavior is probabilistic, so evaluation replaces certainty: we state a rate, a sample, and an interval, and we re-run it on every change. | Certainty is not available; measured rates are. |
| "95 percent is great." | At 7,500 invoices a month, 95 percent correct means about 375 cases a month need a human; here is who handles them and how long it takes. | A rate only means something in the customer's volume. |
| "Why can't it just act?" | Autonomy advances through gates (assist, shadow, approve, bounded autonomy) because each gate proves a control the next one relies on. | Reversibility and consequence, not confidence, set the pace. |

### 5. Say no, or narrow, and offer the alternative

Refuse scope that has no baseline, no accountable owner, or no recovery design. Pair every no with a bounded yes: "not bank-detail changes in this rollout; a separate discovery on vendor-master work with a control owner named first." The alternative must be real enough to schedule.

### 6. Handle the two hardest conversations

**"The demo worked, why is it not in production?"** Answer with the gate list and where the system stands: which evidence exists, which is pending, who owns the next decision, and the date. Never answer with "it is complicated."

**"Can it also do X?"** Answer with the method, not a yes or no: X changes the actors, consequence, and evidence needed, so it re-enters Discover with an owner and a scorecard row. Show the current scorecard so the request lands somewhere visible rather than being dismissed.

### 7. Deliver bad news early, with a plan

When a threshold is missed or a date will slip, report it within one business day, in the decision-first order: what happened, what it means for the decision, what you propose, what you need. Bad news with a plan preserves trust; bad news discovered by the sponsor destroys it.

### 8. Pre-wire before the group meeting

Walk each decision-maker through the readout individually before the group session, especially the risk and control owner and anyone likely to object. The group meeting confirms a decision people have already understood; it is the wrong place to hear an objection for the first time.

### 9. Numbers carry their baseline, source, and uncertainty

Never state a result alone. "6.9 percent correction" becomes "99 of 1,431 assisted invoices (6.9 percent) needed correction against a target of at most 8.0 percent; source: review-interface events, 30 days, one business unit." Percentages travel with denominators; means travel with intervals; projections are labeled as projections.

### 10. Write the one-page readout

Put the whole thing on one page using the [executive readout](../toolkit/executive-readout.md): decisions needed, recommendation, results against predeclared targets, limits, risks, asks, and the next review date. Predeclared targets come from the [pilot charter](../toolkit/pilot-charter.md); the arithmetic comes from the [business case](../toolkit/business-case.md). The page is the record; the meeting is the discussion.

## Examples

### Good pattern

In the fictional LumenPeak Manufacturing engagement ([worked example](../examples/invoice-intake-ai/README.md)), Elena Torres received a one-page readout that opened with three separate decisions: expand the human-approved workflow, hold bounded autonomy, stop bank-detail-change scope. Each result sat beside the target declared in Frame: median handling 4.6 minutes against at most 5.0; correction 99/1,431 (6.9 percent) against at most 8.0; a matched-sample mean reduction of 3.64 minutes with a 95 percent interval of 3.22 to 4.06; zero policy breaches. The limits section stated what 30 days in one business unit with four analysts do not prove: other document types, quarter-end seasonality, reliability at wider load, or any cash savings. Rina Shah had seen the control results two days earlier, so the meeting confirmed the hold on autonomy rather than debating it. Elena recorded three decisions with dates.

### Weak pattern

A slide reads "92 percent accuracy, ready to scale." There is no baseline, no denominator, no cohort, no statement of what "accuracy" measured, and no limits. The sponsor approves a company-wide rollout in the meeting. Six weeks later the rollout stalls in security review over tool permissions and prompt logging that the readout never mentioned, the operators in the second business unit find that their document mix was never tested, and the sponsor, who was told the system was ready, now doubts every number that follows.

## Practice

Take any result you have produced or can borrow from the worked example. Write a one-page readout in decision-first order for a sponsor, then rewrite the same facts for operators and for engineers without changing a single number. Add a limits section with three things the evidence does not prove. Then script two answers: one to "the demo worked, why is it not in production," and one to "can it also do X," each ending with an owner and a date.

## Self-assessment

- Could a sponsor stop reading after the first two lines and still know the decision and your recommendation?
- Does every number carry its baseline, denominator or sample, source, and uncertainty?
- Did you state the limits before anyone asked, including what the system did not do?
- Have you framed the same fact base for sponsor, operators, and engineers without any number changing?
- Was every decision-maker pre-wired, and did each no come with a bounded alternative that has an owner?

## Links

**Lifecycle stages:** [Frame](../stages/02-frame/README.md), [Deploy](../stages/05-deploy/README.md), [Enable](../stages/06-enable/README.md), [Expand](../stages/07-expand/README.md).

**Toolkit assets:** [Executive readout](../toolkit/executive-readout.md), [Pilot charter](../toolkit/pilot-charter.md), [Business case](../toolkit/business-case.md), [Field report](../toolkit/field-report.md).

**Related skills:** [Evaluation and staged rollout](evaluation-and-rollout.md), [Adoption, operations, and product feedback](adoption-and-feedback.md), [Discovery interviewing and workshop facilitation](discovery-interviewing.md).
