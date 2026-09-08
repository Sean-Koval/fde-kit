---
name: fde-eval-pack
description: Use when turning representative cases and production failures into a versioned evaluation record with graders, thresholds, results, and a release decision.
---

# Evaluation pack

Fills the [evaluation pack](../../../toolkit/evaluation-pack.md) template. Judgment comes from [Grader design and error analysis](../../../skills/eval-engineering.md) and [Evaluation and staged rollout](../../../skills/evaluation-and-rollout.md).

## Use when

- Design needs cases, graders, thresholds, and a decision owner defined before the first increment.
- Build has a run to record or a failure to classify and route.
- Deploy or Enable needs a promote, hold, or rollback record, or a production failure must join regression.
- Not for a demo or public benchmark score; see the grader guide's anti-patterns.

## Obtain first

- [ ] System under test: model, prompt, retrieval, policy, integration, and application versions.
- [ ] The case set or its sources, selection method, count per stratum, and version identifier.
- [ ] Expected outcome, required evidence, and permitted human involvement per case.
- [ ] Graders available; for a model-graded judge, its measured agreement with human labels.
- [ ] Thresholds and who set them; release decision owner, rollback target, and rollback owner.
- [ ] Run results, if any: run identifier, date, executor, environment, settings, per-case outcomes.
- [ ] Production failures to classify, with trace identifiers.

## Procedure

1. Confirm the inputs. Without a versioned case set and a named decision owner, fill only the criteria and case-set sections; the rest are gaps.
2. Choose the unit of evaluation per criterion: response, trajectory, or workflow outcome (grader guide, technique 1).
3. Complete "Representative case set": common work, costly exceptions, policy-sensitive cases, known failures, adversarial and valid-abstain cases (technique 2). State the selection method verbatim; size per the guide's labeled heuristics.
4. Complete "Outcome criteria" with the cheapest valid grader per criterion (technique 3). Record a judge metric only beside its agreement statistic (technique 4).
5. Complete "Reproducibility metadata"; any missing field is a gap.
6. Complete "Results and failure analysis" with per-stratum rates and uncertainty (technique 5). Read failures before classifying; assign a cause class, route the fix to that layer, and mark regression additions (technique 6).
7. Complete "Online monitoring and re-evaluation" with signals mirroring the offline graders (technique 7).
8. Complete "Release decision" as the owner recorded it; otherwise mark it open and summarize thresholds passed and missed (rollout guide, technique step 5).
9. Run the completion checks and print the summary line.

## Output

Fill the Template section of [evaluation-pack.md](../../../toolkit/evaluation-pack.md). Save to `docs/engagement/<workflow>/evaluation-pack-<system-version>.md` in the user's repository, one file per version.

Print: `Evaluation pack <workflow> <version>: <n> cases; <n> of <n> criteria met; <n> failures classified, <n> to regression; decision <promote/hold/roll back/open>; <n> gaps.`

## Rules

- No invented facts: results, agreement statistics, thresholds, and versions come from inputs or run records.
- Missing inputs become `[gap: what is missing and who can supply it]`.
- Sizing and threshold rules of thumb are labeled starting heuristics, not industry standards.
- Reference cases and traces by identifier; no customer record contents, personal data, or credentials.
- Decisions belong to the release owner and thresholds to whoever set them; the skill reports, it does not decide.

## Completion checks

- [ ] Cases cover normal work, consequential exceptions, policy-sensitive cases, and known failures.
- [ ] Every case specifies a system outcome, required evidence, and valid human-review or abstention behavior.
- [ ] Case-set/version ID, sample-selection method and count, grader/rubric version, and evaluation-run metadata make the result reproducible.
- [ ] Thresholds, graders, system version, release decision, and rollback target have named owners.
- [ ] Failures are classified, assigned, and added to regression coverage when meaningful.
