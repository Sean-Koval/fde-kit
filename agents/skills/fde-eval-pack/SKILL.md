---
name: fde-eval-pack
description: Use when turning representative cases and production failures into a versioned evaluation record with graders, thresholds, results, and a release decision.
---

# Evaluation pack

Fills the [evaluation pack](../../../toolkit/evaluation-pack.md) template. Judgment comes from [Grader design and error analysis](../../../skills/eval-engineering.md) for case sets, graders, calibration, and the error-analysis loop, and from [Evaluation and staged rollout](../../../skills/evaluation-and-rollout.md) for release states and gates.

## Use when

- Design needs the evidence approach defined before the first increment: cases, graders, thresholds, and the owner who decides.
- Build has a run to record, or a failure to classify and route.
- Deploy or Enable needs a promotion, hold, or rollback decision, or a production failure must join the regression set.
- Not when the only evidence is a demo or a public benchmark score; the grader guide's anti-pattern table explains why neither is release evidence.

## Obtain first

- [ ] System under test: model, prompt, retrieval, policy, integration, and application versions.
- [ ] The case set or its sources (production traces, review queues, the workflow trace), the selection method, the count per stratum, and the case-set version identifier.
- [ ] Expected outcome, required evidence, and permitted human involvement for each case.
- [ ] Graders available: deterministic checks, trace assertions, human rubric, model-graded judge. For a judge, its measured agreement with human labels.
- [ ] Thresholds, who set them, and when; thresholds set after a run are recorded as such.
- [ ] Run results if a run exists: run identifier, date, executor, environment, seed or settings, per-case outcomes.
- [ ] Release decision owner, rollback target, and rollback owner.
- [ ] Production failures awaiting classification, with trace identifiers.

## Procedure

1. Confirm the inputs. Without a versioned case set and a named decision owner, produce only the "Outcome criteria" and "Representative case set" sections and mark the rest as gaps.
2. Choose the unit of evaluation per criterion: response, trajectory, or end-to-end workflow outcome (grader guide, technique 1). Most workflows need one criterion at the response level and one at the workflow level.
3. Complete "Representative case set". Check coverage against the four required kinds: common work, costly exceptions, policy-sensitive cases, known failures; add adversarial and valid-abstain cases (technique 2). State the selection method verbatim from the inputs. Size the set by the guide's sizing heuristics, and label them as such if you cite them.
4. Complete "Outcome criteria" with the cheapest valid grader per criterion (technique 3). Record a judge-produced metric only beside its agreement statistic (technique 4); if agreement was never measured, write a gap.
5. Complete "Reproducibility metadata" from the run inputs. Any missing field is a gap, because the check for reproducibility fails without it.
6. Complete "Results and failure analysis". Report per-stratum rates with uncertainty where the inputs allow (technique 5). Read failures before classifying them, assign each to the model, data, tool, policy, integration, UX, or process class, route it to the layer where the cause lives, and mark whether it joins the regression set (technique 6).
7. Complete "Online monitoring and re-evaluation" with the signals that mirror the offline graders (technique 7).
8. Complete "Release decision" with the decision the owner has recorded. If the owner has not decided, write the decision as open and summarize which thresholds passed and which did not, using the rollout states in the rollout guide's technique step 5 as the vocabulary.
9. Run the completion checks and print the summary line.

## Output

Fill the Template section of [evaluation-pack.md](../../../toolkit/evaluation-pack.md). Save to `docs/engagement/<workflow>/evaluation-pack-<system-version>.md` in the user's repository; keep one file per system version so runs are comparable.

Print: `Evaluation pack <workflow> <system version>: <n> cases in <n> strata; <n> of <n> criteria met; <n> failures classified, <n> added to regression; decision <promote/hold/roll back/open>; <n> gaps.`

## Rules

- No invented facts: results, agreement statistics, thresholds, and versions come from inputs or run records.
- Missing inputs are written as `[gap: what is missing and who can supply it]`.
- Sizing and threshold rules of thumb are labeled starting heuristics, not industry standards.
- Reference cases and traces by identifier; the pack carries no customer record contents, personal data, or credentials.
- Promote, hold, and roll back belong to the release decision owner; thresholds belong to whoever set them. The skill reports against them; it does not move them or decide.

## Completion checks

- [ ] Cases cover normal work, consequential exceptions, policy-sensitive cases, and known failures.
- [ ] Every case specifies a system outcome, required evidence, and valid human-review or abstention behavior.
- [ ] Case-set/version ID, sample-selection method and count, grader/rubric version, and evaluation-run metadata make the result reproducible.
- [ ] Thresholds, graders, system version, release decision, and rollback target have named owners.
- [ ] Failures are classified, assigned, and added to regression coverage when meaningful.
