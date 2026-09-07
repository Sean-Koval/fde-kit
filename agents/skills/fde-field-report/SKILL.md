---
name: fde-field-report
description: Use when sending a reproducible model, product, or platform issue from a customer engagement upstream to your own product or research team.
---

# Field report

Fills the [field report](../../../toolkit/field-report.md) template. Judgment comes from [Grader design and error analysis](../../../skills/eval-engineering.md) for reproduction, classification, and counting, and from [Adoption, operations, and product feedback](../../../skills/adoption-and-feedback.md) for separating defects from requests for new scope.

## Use when

- Build, Enable, or Expand has surfaced a failure that the field team cannot fix in its own layer: model behavior, a product surface, or the platform.
- A pattern recurs across cases and an upstream team could act on it if it were reproducible.
- Not for a one-off failure that a prompt, data, rule, or integration fix resolves locally; route that through the evaluation pack's failure analysis instead.

## Obtain first

- [ ] The observed issue in one sentence, and which layer the field team believes it lives in: model, product, or platform.
- [ ] A reproducible case: input, expected outcome, observed outcome, and the full system version (model, prompt, retrieval, tools, application).
- [ ] Frequency as a count over a stated number of cases from traces or the evaluation pack, not an impression.
- [ ] Business consequence and the workaround in place, with its cost to users or reviewers.
- [ ] Whether the inputs can leave the engagement: customer permission, or a sanitized or synthetic input that still reproduces the issue.
- [ ] The upstream recipient, the requested action, and the identifier of the regression case added locally.

## Procedure

1. Confirm the inputs. Without a reproducible case, stop and help the user build one; a report that cannot be reproduced upstream costs the recipient more than it returns.
2. Reproduce the case if the harness can run the system; record the run identifier and whether the observed outcome recurred. If it cannot be reproduced on rerun, report the recurrence rate instead of asserting a defect.
3. Classify the issue by cause using the failure taxonomy from the grader guide's error-analysis loop (technique 6). Confirm that the largest cause is not in a layer the field team owns; if it is, say so and route locally.
4. Sanitize. Replace customer inputs with redacted or synthetic equivalents and rerun; the report ships only if the sanitized case still reproduces. Record the customer permission or the sanitization method.
5. Quantify with the count, the denominator, and, where the case set allows, an interval (technique 5). Label any severity rule of thumb as a starting heuristic.
6. Separate the defect from any request for new capability (adoption guide, technique step 4). A request for new scope is reported as a request, with the workflow evidence behind it, not as a bug.
7. State the workaround, the local regression case, and the specific action requested upstream with a named recipient.
8. Run the completion checks and print the summary line.

## Output

Fill the Template section of [field-report.md](../../../toolkit/field-report.md). Save to `docs/engagement/<workflow>/field-report-<date>-<short-title>.md` in the user's repository; send the same content upstream through the recipient's intake route.

Print: `Field report <short title>: <model/product/platform>; reproduced <yes/no/intermittent, n of n>; frequency <count/denominator>; sanitized <method or permission>; requested <action> from <recipient>; <n> gaps.`

## Rules

- No invented facts: counts, versions, and outcomes come from traces, runs, or the evaluation pack.
- Missing inputs are written as `[gap: what is missing and who can supply it]`.
- Rules of thumb are labeled starting heuristics, not industry standards.
- No customer confidential data: no record contents, personal data, credentials, or identifiable customer references leave the engagement. Sanitize first; if sanitization breaks reproduction, report that and stop.
- Whether to send the report belongs to the engagement lead and the customer's permission holder. The skill prepares the report; it does not send it.

## Completion checks

- [ ] Every reported issue has a reproducible case with input, expected outcome, observed outcome, and system version.
- [ ] The issue is classified as model, product, or platform with the evidence for that classification.
- [ ] Frequency and consequence are stated as counts over a denominator from traces or the evaluation pack.
- [ ] Inputs are sanitized or synthetic, the reproduction was confirmed after sanitization, and permission to share is recorded.
- [ ] The workaround, the local regression case, the requested action, and the named recipient are recorded.
