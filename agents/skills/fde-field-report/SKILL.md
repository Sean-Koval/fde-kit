---
name: fde-field-report
description: Use when sending a reproducible model, product, or platform issue from a customer engagement upstream to your own product or research team.
---

# Field report

Fills the [field report](../../../toolkit/field-report.md) template. Judgment comes from [Grader design and error analysis](../../../skills/eval-engineering.md) and [Adoption, operations, and product feedback](../../../skills/adoption-and-feedback.md).

## Use when

- A failure the field team cannot fix in its own layer: model behavior, a product surface, or the platform.
- A pattern recurs and an upstream team could act on it if reproducible.
- Not for a failure fixable locally by prompt, data, rule, or integration; use the evaluation pack.

## Obtain first

- [ ] The issue in one sentence and its believed layer: model, product, or platform.
- [ ] A reproducible case: input, expected outcome, observed outcome, and full system version.
- [ ] Frequency as a count over a stated number of cases, from traces or the evaluation pack.
- [ ] Business consequence and the workaround in place, with its cost.
- [ ] Customer permission to share, or a sanitized or synthetic input that still reproduces.
- [ ] The upstream recipient, the requested action, and the local regression case identifier.

## Procedure

1. Confirm the inputs. Without a reproducible case, stop and help the user build one.
2. Reproduce if the harness can run the system; record the run identifier and whether the outcome recurred. If not, report the recurrence rate rather than asserting a defect.
3. Classify the cause with the grader guide's error-analysis taxonomy (technique 6). If the largest cause sits in a layer the field team owns, route locally.
4. Sanitize: replace customer inputs with redacted or synthetic equivalents and rerun; ship only if it still reproduces. Record the permission or method.
5. Quantify with count, denominator, and an interval where the case set allows (technique 5). Label any severity rule of thumb a starting heuristic.
6. Separate defect from request for new capability (adoption guide, technique step 4); report new scope as a request with its evidence.
7. State the workaround, the local regression case, and the action requested from a named recipient.
8. Run the completion checks and print the summary line.

## Output

Fill the Template section of [field-report.md](../../../toolkit/field-report.md). Save to `docs/engagement/<workflow>/field-report-<date>-<short-title>.md` in the user's repository; send the same content through the recipient's intake route.

Print: `Field report <title>: <model/product/platform>; reproduced <n of n>; frequency <count/denominator>; sanitized <method or permission>; requested <action> from <recipient>; <n> gaps.`

## Rules

- No invented facts: counts, versions, and outcomes come from traces, runs, or the evaluation pack.
- Missing inputs become `[gap: what is missing and who can supply it]`.
- Rule-of-thumb numbers are labeled starting heuristics, not industry standards.
- No customer confidential data leaves the engagement: no record contents, personal data, credentials, or identifiable references. If sanitization breaks reproduction, report that and stop.
- Sending belongs to the engagement lead and the customer's permission holder. The skill prepares; it does not send.

## Completion checks

- [ ] The report covers one issue, with one classification and one receiving team.
- [ ] At least one reproducible case records input, expected and observed result, model, prompt, tool or retrieval versions, and a trace reference.
- [ ] Inputs are synthetic or redacted; no customer confidential data appears, and the check is signed.
- [ ] Frequency, conditions, business impact, workaround cost, and gate impact are stated with denominators and sources.
- [ ] Priority is justified by customers affected, revenue or risk, and evidence quality, and the report names its owner.
