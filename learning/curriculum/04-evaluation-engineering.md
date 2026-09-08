# Module 04: Evaluation engineering

## Outcome

You can turn a design into release evidence: a stratified case set with a stated selection method, graders that can be rerun, a model-graded judge whose agreement with human labels is measured rather than assumed, an error-analysis pass that classifies failures by cause, and an evaluation pack that ends in a release decision with an owner and a rollback target. This is the habit that separates field engineers from demo builders, and it is the module reviewers weigh most heavily in the capstone.

## Prerequisites

- The design package from [module 03](03-system-design.md), especially the output contract with its abstain value and provenance fields.
- The two traces from module 02 as the seed for cases.
- Model access, if available, to run the system and to build a model-graded judge. Without it, the exercise substitutes hand-simulated outputs and a written calibration plan.

## Study

Read in this order.

1. [Evaluation and staged rollout](../../skills/evaluation-and-rollout.md): the evidence standard (cases, expected end-to-end results, reproducible graders, thresholds with owners) and the rule that live failures enter a versioned regression set.
2. [Grader design and error analysis](../../skills/eval-engineering.md): grader types (deterministic checks, rubric-based human grading, model-graded judges), calibrating a judge against human labels, reporting uncertainty, and the error-analysis loop.
3. [Evaluation pack](../../toolkit/evaluation-pack.md): the template, including reproducibility metadata that lets another team rerun the evaluation.
4. [Build](../../stages/04-build/README.md) stage page: what an increment must prove before Deploy, and the failure mode of treating a prototype as proof.
5. Section 4 of the [invoice-intake example](../../examples/invoice-intake-ai/README.md): a 240-case stratified sample, criteria that grade controls and escalation rather than extraction alone, and a release decision of "promote to staged production", not "auto-post".

Where to practice with real tooling: run your system from module 03 over the case set at least twice, store the outputs with the system version, and diff the runs. A grader you have only described is a plan; a grader you have rerun and whose disagreements you have read is evidence.

## Exercise

Produce an evaluation pack for the module 03 design.

1. **Case set.** Build 30 cases as a starting heuristic, not an industry standard, stratified across common work, costly exceptions, policy-sensitive cases, adversarial or malformed inputs, and cases where the correct answer is to abstain. Record the selection method and the strata counts. Each case states the expected end-to-end workflow result, the required evidence, and the expected human involvement. Version the set.
2. **Graders.** For each criterion in your pack (correct result, evidence grounding, policy and safety, review burden, operational behavior), define the grader: deterministic check, human rubric, or model-graded judge. Write the rubric text for any human or model grader, with pass and fail examples.
3. **Labels and calibration.** Label 20 cases by hand against the rubric. If you have model access, build a model-graded judge for at least one criterion, run it on the same 20, and report agreement with your labels (raw agreement and the cases where it disagreed, with your reading of why). If you do not, write the calibration plan: sample size, agreement measure, the threshold at which you would trust the judge unsupervised, and what you do below it.
4. **Error analysis.** Run the system (or hand-simulate outputs for every case, marking them simulated). Read every failure one by one and classify it by likely cause: data, retrieval, model behavior, prompt, deterministic rule, integration, policy, or workflow design. Record the corrective action and whether the case joins the regression set.
5. **Release decision.** Complete the pack's decision section: promote, hold, or roll back; owner; system version; rollback target; and the threshold that was closest to failing.

Grade the whole workflow, not the model. A case where the model is wrong but the deterministic check catches it and routes to review is a pass for the system and a data point for the model.

## Assessment

| Criterion | Developing | Solid | Strong |
| --- | --- | --- | --- |
| Case set construction | Cases are the happy path or chosen after seeing outputs | Stratified with stated method and counts; expected results include abstention | Strata are tied to trace evidence of what is common and what is costly, and the set is versioned with a change log |
| Grader reproducibility | "Looks right" or a single score | Each criterion has a named grader type and a written rubric | Another person could rerun every grader from the pack alone and get a comparable result |
| Judge calibration | Model-graded score used without human labels | Agreement with 20 human labels reported, or a specific calibration plan | Disagreements are read and explained; the pack states where the judge is and is not trusted |
| Error analysis | Failures counted, not read | Every failure classified by cause with a corrective action | Causes are ranked by frequency and cost; fixes are separated from workflow-design changes; regression additions are named |
| Release decision | Missing or "ready" | Decision, owner, version, and rollback target stated | The nearest-to-failing threshold and its uncertainty are stated, and the decision matches the evidence rather than the schedule |

Solid on grader reproducibility and release decision is the minimum for module 05; a rollout gate that cannot be rerun is not a gate.

## Next

[Module 05: Production, rollout, and Day 2](05-production-and-day-two.md) turns the release decision into gates, signals, owners, and a rehearsed rollback. Your evaluation thresholds become the promotion criteria.
