---
name: fde-field-report
description: Use when sending a reproducible model, product, or platform issue from a customer engagement upstream to your own product or research team.
---

# Field report

Fills the [field report](../../../toolkit/field-report.md) template. Judgment comes from [Grader design and error analysis](../../../skills/eval-engineering.md) for reproduction, classification, and counting, and from [Adoption, operations, and product feedback](../../../skills/adoption-and-feedback.md) for separating defects from requests for new scope.

## Use when

- Build, Enable, or Expand has surfaced a failure the field team cannot fix in its own layer: model behavior, a product surface, or the platform.
- A pattern recurs across cases and an upstream team could act on it if it were reproducible.
- Not for a failure that a prompt, data, rule, or integration fix resolves locally; route that through the evaluation pack's failure analysis.

## Obtain first

- [ ] The issue in one sentence and the layer the team believes it lives in: model, product, or platform.
- [ ] A reproducible case: input, expected outcome, observed outcome, and full system version (model, prompt, retrieval, tools, application).
- [ ] Frequency as a count over a stated number of cases from traces or the evaluation pack, not an impression.
- [ ] Business consequence and the workaround in place, with its cost to users or reviewers.
- [ ] Whether inputs can leave the engagement: customer permission, or a sanitized or synthetic input that still reproduces.
- [ ] The upstream recipient, the requested action, and the identifier of the local regression case.

## Procedure

1. Confirm the inputs. Without a reproducible case, stop and help the user build one; an unreproducible report costs the recipient more than it returns.
2. Reproduce the case if the harness can run the system; record the run identifier and whether the outcome recurred. If it does not recur, report the recurrence rate instead of asserting a defect.
3. Classify the cause with the taxonomy from the grader guide's error-analysis loop (technique 6). If the largest cause is in a layer the field team owns, say so and route locally.
4. Sanitize. Replace customer inputs with redacted or synthetic equivalents and rerun; ship only if the sanitized case still reproduces. Record the permission or the sanitization method.
5. Quantify with count, denominator, and, where the case set allows, an interval (technique 5). Label any severity rule of thumb a starting heuristic.
6. Separate the defect from any request for new capability (adoption guide, technique step 4). Report new scope as a request with its workflow evidence, not as a bug.
7. State the workaround, the local regression case, and the specific action requested from a named recipient.
8. Run the completion checks and print the summary line.

## Output

Fill the Template section of [field-report.md](../../../toolkit/field-report.md). Save to `docs/engagement/<workflow>/field-report-<date>-<short-title>.md` in the user's repository; send the same content through the recipient's intake route.

Print: `Field report <short title>: <model/product/platform>; reproduced <yes/no/intermittent, n of n>; frequency <count/denominator>; sanitized <method or permission>; requested <action> from <recipient>; <n> gaps.`

## Rules

- No invented facts: counts, versions, and outcomes come from traces, runs, or the evaluation pack.
- Missing inputs become `[gap: what is missing and who can supply it]`.
- Rules of thumb are labeled starting heuristics, not industry standards.
- No customer confidential data: no record contents, personal data, credentials, or identifiable customer references leave the engagement. If sanitization breaks reproduction, report that and stop.
- Sending belongs to the engagement lead and the customer's permission holder. The skill prepares the report; it does not send it.

## Completion checks

- [ ] Every reported issue has a reproducible case with input, expected outcome, observed outcome, and system version.
- [ ] The issue is classified as model, product, or platform with the evidence for that classification.
- [ ] Frequency and consequence are stated as counts over a denominator from traces or the evaluation pack.
- [ ] Inputs are sanitized or synthetic, reproduction was confirmed after sanitization, and permission to share is recorded.
- [ ] The workaround, the local regression case, the requested action, and the named recipient are recorded.
