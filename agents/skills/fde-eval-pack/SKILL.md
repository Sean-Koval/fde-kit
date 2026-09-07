---
name: fde-eval-pack
description: Use when turning representative cases and production failures into a versioned evaluation record with graders, thresholds, results, and a release decision.
---

# Evaluation pack

Fills the [evaluation pack](../../../toolkit/evaluation-pack.md) template. Judgment comes from [Grader design and error analysis](../../../skills/eval-engineering.md) and [Evaluation and staged rollout](../../../skills/evaluation-and-rollout.md).

## Use when

- Design needs the evidence approach defined before the first increment: cases, graders, thresholds, decision owner.
- Build has a run to record or a failure to classify and route.
- Deploy or Enable needs a promote, hold, or rollback record, or a production failure must join the regression set.
- Not when the only evidence is a demo or a public benchmark; see the grader guide's anti-patterns.

## Obtain first

- [ ] System under test: model, prompt, retrieval, policy, integration, and application versions.
- [ ] The case set or its sources, selection method, count per stratum, and version identifier.
- [ ] Expected outcome, required evidence, and permitted human involvement per case.
- [ ] Graders available; for a model-graded judge, its measured agreement with human labels.
- [ ] Thresholds, who set them, and when.
- [ ] Run results, if any: run identifier, date, executor, environment, settings, per-case outcomes.
- [ ] Release decision owner, rollback target, and rollback owner.
- [ ] Production failures awaiting classification, with trace identifiers.

## Procedure

1. Confirm the inputs. Without a versioned case set and a named decision owner, produce only "Outcome criteria" and "Representative case set" and mark the rest as gaps.
2. Choose the unit of evaluation per criterion: response, trajectory, or workflow outcome (grader guide, technique 1).
3. Complete "Representative case set". Check coverage of common work, costly exceptions, policy-sensitive cases, and known failures; add adversarial and valid-abstain cases (technique 2). State the selection method verbatim; cite the guide's sizing heuristics as heuristics.
4. Complete "Outcome criteria" with the cheapest valid grader per criterion (technique 3). Record a judge metric only beside its agreement statistic (technique 4).
5. Complete "Reproducibility metadata"; any missing field is a gap.
6. Complete "Results and failure analysis" with per-stratum rates and uncertainty where inputs allow (technique 5). Read failures before classifying; assign a cause class, route it to the layer where the cause lives, and mark whether it joins regression (technique 6).
7. Complete "Online monitoring and re-evaluation" with the signals that mirror the offline graders (technique 7).
8. Complete "Release decision" with what the owner recorded; otherwise mark it open and summarize which thresholds passed, using the rollout states in the rollout guide's technique step 5.
9. Run the completion checks and print the summary line.

## Output

Fill the Template section of [evaluation-pack.md](../../../toolkit/evaluation-pack.md). Save to `docs/engagement/<workflow>/evaluation-pack-<system-version>.md` in the user's repository, one file per version.

Print: `Evaluation pack <workflow> <version>: <n> cases, <n> strata; <n> of <n> criteria met; <n> failures classified, <n> added to regression; decision <promote/hold/roll back/open>; <n> gaps.`

## Rules

- No invented facts: results, agreement statistics, thresholds, and versions come from inputs or run records.
- Missing inputs become `[gap: what is missing and who can supply it]`.
- Sizing and threshold rules of thumb are labeled starting heuristics, not industry standards.
- Reference cases and traces by identifier; no customer record contents, personal data, or credentials in the pack.
- Promote, hold, and roll back belong to the release owner; thresholds belong to whoever set them. The skill reports; it does not decide.

## Completion checks

- [ ] Cases cover normal work, consequential exceptions, policy-sensitive cases, and known failures.
- [ ] Every case specifies a system outcome, required evidence, and valid human-review or abstention behavior.
- [ ] Case-set/version ID, sample-selection method and count, grader/rubric version, and evaluation-run metadata make the result reproducible.
- [ ] Thresholds, graders, system version, release decision, and rollback target have named owners.
- [ ] Failures are classified, assigned, and added to regression coverage when meaningful.
