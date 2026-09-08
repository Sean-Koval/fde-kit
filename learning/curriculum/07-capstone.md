# Module 07: Capstone: run a fictional engagement end to end

## Outcome

You can run an AI engagement from Discover to Expand on a scenario you did not choose, producing every artifact the kit defines, an evidence chain a reviewer can follow from observed case to expansion decision, and a limitations section that states what the evidence does not prove. The capstone is the artifact set you talk from in interviews and the baseline for your first real engagement.

## Prerequisites

- Modules [01](01-role-and-operating-model.md) through [06](06-customer-craft.md) complete, each at least solid on its minimum criteria.
- A reviewer who has agreed to score the result with the rubric below.
- About a third of the total curriculum effort reserved, as a starting heuristic, not an industry standard.

## Study

No new reading. Reread, in this order, with the scenario in mind.

1. The [invoice-intake example](../../examples/invoice-intake-ai/README.md) in full: the standard your capstone is compared against, from the "at a glance" table to the three separate Expand decisions.
2. The [stage playbook](../../stages/README.md): each stage's exit criteria are your checkpoints; do not start the next artifact until the current one meets them.
3. The [toolkit index](../../toolkit/README.md): every artifact you will produce, with its completion checks.
4. [AI security and governance review](../../toolkit/ai-security-review.md): both scenarios carry regulated or customer data.

Where to practice with real tooling: write thirty to fifty synthetic letters or tickets, build the case set from them, run a real model against your output contract, and trace the runs. The rubric scores real evaluation runs above simulated outputs.

## Exercise

Choose one seed. Both are fictional; every name, number, and system is invented for teaching. The facts are where discovery starts, not what it concludes: reconstruct cases, invent consistent records, and interview the personas (played by your reviewer, or written in their voice) to fill the gaps.

### Seed A: Harbor Mutual, claims correspondence triage

| Fact | Starting value |
| --- | --- |
| Organization | Harbor Mutual, a fictional property and casualty insurer with two regional claims centers |
| Workflow | Incoming correspondence (letters, emails, scanned forms) is read, classified, linked to a claim, and routed to an adjuster or specialist queue |
| Volume | About 9,000 items per month: 60% email, 30% scanned mail, 10% portal uploads |
| Pain | Median arrival-to-correct-queue time 1.6 business days; 22% of items re-routed at least once; complaint and legal items sometimes sit in general queues |
| Systems | Claims platform is the system of record; a document management system holds images; routing is a shared mailbox plus a spreadsheet of queue rules |
| Controls | Regulatory complaints must reach the complaints team within one business day; litigation items must never be summarized to adjusters without legal review; personal data must not leave the approved region |
| Constraints | Model calls run only in an approved environment; no customer-facing generated text in the first release; claims director Ana Ferreira owns the outcome; compliance lead Tomas Reilly can block deployment |

### Seed B: Northwind Software, support knowledge assistant

| Fact | Starting value |
| --- | --- |
| Organization | Northwind Software, a fictional vendor of mid-market finance software with a three-tier support organization |
| Workflow | Tier 1 agents answer product questions from a knowledge base, release notes, and internal engineering notes; unresolved cases escalate to tier 2 |
| Volume | About 14,000 tickets per month: 55% how-to or configuration questions; 15% escalated to tier 2 |
| Pain | Median first response 3.1 hours; 31% of tier 2 escalations are answerable from existing articles; 4,200 articles, an unknown share stale |
| Systems | Ticketing system is the system of record; knowledge base and release notes live in two content systems with different permission models; engineering notes contain customer names and unreleased features |
| Controls | Agents must not disclose unreleased features or other customers' data; every customer-facing answer must cite a published article; security tickets go to a separate team |
| Constraints | Retrieval must respect content permissions per agent tier; agent-assist only in the first release; support director Mei Okafor owns the outcome; head of information security Dana Lindqvist must approve any indexing of engineering notes |

### What you produce

1. **Discover:** stakeholder map, two interview records, two validated traces (common and costly exception), discovery evidence log.
2. **Frame:** opportunity scorecard with three candidates, pilot charter, business case with a predeclared evidence gate.
3. **Design:** responsibility matrix, justified pattern choice, output contract with an abstain value, tool contracts if any, completed security review.
4. **Build:** evaluation pack with versioned case set, graders, calibration evidence or plan, error analysis, release decision.
5. **Deploy:** rollout plan with gates and signals, rollback rehearsal record.
6. **Enable:** operating plan with Day 2 owners, and a thirty-day outcome (simulated, labeled as such, with the measurement method stated).
7. **Expand:** refreshed business case, a scorecard entry for the request the sponsor will inevitably make, and separate expand, hold, and stop decisions.
8. **Limitations:** what the evidence does not prove, in the form the invoice example uses.

Then write a two-page comparison against the invoice example: where your evidence chain is as strong, where weaker, and what a real engagement would need to close each gap. Attach your module 01 page and note what you got wrong then.

## Assessment

Score each dimension 1 (developing) to 3 (strong) and multiply by the weight. As a starting heuristic, 24 or more of 30 with no dimension at 1 is strong; 18 to 23 is solid; below 18, repeat the weakest module before rescoring.

| Dimension | Weight | Developing (1) | Solid (2) | Strong (3) |
| --- | ---: | --- | --- | --- |
| Evidence chain | 2 | Wedge and targets asserted from the seed facts | Traces, interviews, and records support wedge, baseline, and targets | Every number traces from an observed case or record to the Expand decision; contradictions are recorded |
| Boundary and controls | 2 | AI makes, or effectively makes, consequential decisions | Interpretation, validation, decision, and action assigned with failure behavior | Every seed control is enforced deterministically or by a named human; the conflict case is resolved; the security review is complete with owners |
| Evaluation quality | 2 | Happy-path cases; a single score | Stratified, versioned set; reproducible graders; failures classified | Judge calibrated or its plan specific; real runs where possible; nearest-to-failing threshold and its uncertainty stated |
| Production and Day 2 readiness | 2 | Launch plan without gates or owners | Gates with criteria and owners; operating plan with backups | Rollback rehearsed with evidence; change control per change class; monitoring that detects the costliest failure first |
| Communication and honesty | 1 | Results without limits; the readout narrates | Decision-first readout; limits section present | Same facts at every altitude; limits beside results; hard conversations answered with a decision and a date |
| Overall coherence | 1 | Artifacts contradict each other (targets, owners, versions) | Names, thresholds, versions, and decisions agree across artifacts | Reads as one engagement; the comparison against the example is specific about gaps |

### Getting it reviewed

Give the reviewer the artifact set and the rubric, nothing else; if they need you to explain something, that is a finding. Ask for the score, the weakest link in the evidence chain, and one question they would ask as the compliance or security persona. Disagreements about the score are the useful part; record them.

### What a strong capstone lets you say

In an [interview](../interview-preparation.md), a strong capstone lets you answer from artifacts rather than memory: which pattern you chose and what evidence would have changed it; where your judge disagreed with your labels and what you did; why bounded autonomy was held despite passing metrics; and what your result did not prove. Those are the answers evidence-discussion interviews are designed to find missing.

## Next

Turn the capstone into practice material with [interview preparation](../interview-preparation.md), then find a real workflow to apply it to. The [roadmap](../../docs/roadmap.md) lists what the kit adds next, including a second worked example and timed scenario drills.
