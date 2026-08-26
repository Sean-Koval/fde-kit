# Worked example: AI-assisted invoice intake

> **Fictional example.** LumenPeak Manufacturing, its people, records, dates, and results are invented for teaching. The figures are internally consistent but are not customer results or industry benchmarks.

This example follows one accounts-payable engagement through [Discover](../../stages/01-discover/README.md), [Frame](../../stages/02-frame/README.md), [Design](../../stages/03-design/README.md), [Build](../../stages/04-build/README.md), [Deploy](../../stages/05-deploy/README.md), [Enable](../../stages/06-enable/README.md), and [Expand](../../stages/07-expand/README.md). It shows completed excerpts from all seven toolkit artifacts. Use the linked artifacts—not these excerpts—for copy-ready instructions and completion checks.

## Engagement at a glance

| Item | Engagement record |
| --- | --- |
| Customer | LumenPeak Manufacturing (fictional), US shared-services accounts payable |
| Problem | AP analysts manually read emailed invoices, find purchase orders, check controls, and enter ERP drafts; intake delay obscures exceptions and threatens on-time processing. |
| First wedge | English-language, USD, PDF invoices with an existing purchase order; one business unit and four of twelve AP analysts |
| Explicit exclusions | Non-PO invoices, credit memos, foreign currency, handwritten documents, vendor onboarding or bank-detail changes, payment approval, and payment release |
| Baseline | 7,500 eligible invoices/month; 8.0 minutes median active handling; 68.0% entered within one business day; 17.6% required rework |
| Pilot target | At most 5.0 minutes median handling, at most 8.0% AI-draft correction, at least 90.0% within one business day, at least 85.0% adoption, and zero policy breaches |
| Measured pilot | 1,486 eligible invoices over 30 days; 4.6 minutes median handling; 3.64 minutes mean reduction in a defined 300-pair matched sample (95% paired-bootstrap CI 3.22–4.06); 6.9% correction; 91.4% within one business day; 96.3% adoption; 1,431/1,431 assisted cases completed successfully with no one-hour reliability breach; zero policy breaches |
| Decision | Expand the human-approved workflow to the remaining US PO-invoice cohort; hold bounded autonomy; stop bank-detail-change scope in this engagement |

All thresholds in this example are engagement-specific starting rules approved by the fictional owners, not industry standards.

## 1. Discover: observe the work before proposing AI

The team applied [Workflow discovery and opportunity framing](../../skills/workflow-discovery.md), observed twelve invoice cases, and checked the observations against a 1,200-record ERP/mailbox sample from 2025-11-03 through 2025-12-12. Elena Torres, Director of Accounts Payable, owned the business outcome.

### Completed [workflow trace](../../toolkit/workflow-trace.md) excerpt

**Case:** `IV-10482`, observed 2026-01-14 with AP analyst Jordan Kim; validated by Jordan and ERP audit record `AP-77291`.

| Step and system | Actor | Evidence and action | Active time / wait | Exception or control |
| --- | --- | --- | --- | --- |
| Triage AP mailbox | AP analyst | Open PDF and identify entity | 1.2 min / 13.4 h median mailbox wait | Unsupported attachments move to the manual queue |
| Read invoice | AP analyst | Transcribe vendor, invoice number, date, PO, and total | 2.4 min | Poor scans require a second reader |
| Find vendor and PO in ERP | AP analyst | Search authoritative vendor and purchase-order records | 1.8 min | Missing or closed PO requires buyer review |
| Check duplicate and tolerance | AP analyst | Compare invoice number, amount, and receipt state | 1.0 min | ERP rules must remain authoritative |
| Enter ERP draft | AP analyst | Re-key fields and attach the source PDF | 1.6 min | Payment approval remains a separate role |

The five active steps total the 8.0-minute baseline. In the 1,200-record sample, 211 invoices required rework (17.6%) and 816 were entered within one business day (68.0%). The improvement boundary was intake and draft preparation; financial approval and payment were not changed.

### Completed [opportunity scorecard](../../toolkit/opportunity-scorecard.md) excerpt

| Rank | Candidate workflow | Impact | Measurability | AI and delivery fit | Readiness | Risk manageability | Decision |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | PO-backed invoice intake | 5 | 5 | 4 | 4 | 4 | Advance a bounded wedge |
| 2 | Payment-inquiry triage | 3 | 4 | 4 | 3 | 4 | Investigate after intake |
| 3 | Vendor onboarding | 4 | 3 | 3 | 2 | 2 | Defer; identity and bank-change controls are unresolved |

- **Selection owner/date:** Elena Torres, 2026-01-23
- **Evidence gate:** demonstrate at most 5.0 minutes median active handling and at least 90.0% one-business-day intake without a policy breach during a 30-day pilot
- **If the gate failed:** return to Frame to narrow the document or exception scope rather than add autonomy

## 2. Frame: agree on the outcome and investment rule

The team framed the outcome as: “Create an accurate, evidence-backed ERP draft for eligible invoices within one business day while preserving AP approval and all existing financial controls.” The initial [business case](../../toolkit/business-case.md) treated released analyst time as capacity value, not cash savings.

| Measure | Baseline and source | Pilot target | Owner |
| --- | --- | --- | --- |
| Eligible volume | 7,500 invoices/month; ERP query `AP-BASE-2025Q4` | Hold scope constant | Elena Torres |
| Median active handling | 8.0 min; time study plus 1,200-record sample | ≤5.0 min | Marcus Lee, AP Manager |
| Entered within one business day | 816/1,200 (68.0%) | ≥90.0% | Elena Torres |
| AI-draft correction | New measure | ≤8.0% of assisted invoices | Marcus Lee |
| Adoption | New measure | ≥85.0% of eligible invoices | Marcus Lee |
| Policy breach | 0 accepted tolerance, duplicate, or permission bypasses | 0 | Rina Shah, Finance Controls Manager |

Scope, measures, and the decision rule were approved on 2026-01-26. The counterfactual was continued queue growth and temporary staffing; no headcount reduction was assumed. The predeclared value analysis required 300 pilot invoices, stratified by vendor tier, page count, amount band, and exception status, to be matched one-to-one with baseline invoices from the same business unit and strata. The investment gate required payback within 12 months at the lower 95% confidence bound of the matched-pair mean time reduction, after annual operating cost.

## 3. Design: put AI inside a controlled architecture

Using [Human, software, and AI system design](../../skills/ai-system-design.md), the team made the ERP authoritative and separated interpretation from validation, approval, and action.

```text
AP mailbox → file/security checks → secure document store
                                      ↓
                              AI extraction + source spans
                                      ↓
ERP vendor/PO state → deterministic duplicate, tolerance, and permission checks
                                      ↓
                         AP review queue → analyst approval
                                      ↓
                         ERP draft invoice + immutable audit event

Any missing evidence, failed check, or unavailable service → existing manual queue
```

### Completed [responsibility matrix](../../toolkit/responsibility-matrix.md) excerpt

| Responsibility | AI | Deterministic software | Human | Failure behavior / owner |
| --- | --- | --- | --- | --- |
| Interpret invoice | Extract five fields and cite PDF spans | Enforce schema and allowed file types | Resolve missing or conflicting values | Abstain to review; Marcus Lee |
| Validate vendor, PO, duplicate, tolerance, and permission | No authoritative decision | Query ERP state; execute PO/duplicate rules, `FIN-AP-07` tolerance, and `IAM-AP-03` role/entity permission controls | Finance Controls approves policy exceptions | Block draft; Rina Shah |
| Decide route | Recommend “ready” or “review” with evidence | Route from rule results; no confidence-only approval | AP analyst approves every proposed draft | Send to manual queue; Elena Torres |
| Create ERP draft | No direct write | Idempotent connector writes only after analyst approval | Analyst confirms source and route | Stop write, retain prior state; Priya Nair |
| Approve or release payment | None | Existing ERP segregation-of-duties rules | Existing authorized approvers | Unchanged process; Rina Shah |

The approved version, `AP-INTAKE-1.0`, allowed draft creation only after human approval. The kill switch disabled the connector and returned every case to the existing mailbox queue.

## 4. Build: prove the whole workflow

The first increment extracted five fields with source spans, ran ERP controls, and prepared a reviewable draft. The team used [Evaluation and staged rollout](../../skills/evaluation-and-rollout.md) rather than treating extraction accuracy alone as release evidence.

### Completed [evaluation pack](../../toolkit/evaluation-pack.md) excerpt

- **System:** `AP-INTAKE-1.0`; case set `AP-INTAKE-v1.2`; rubric `AP-RUBRIC-1.1`
- **Run:** `EVAL-2026-03-06`; fixed 240-case stratified sample: 150 common, 30 duplicate, 30 missing/invalid PO, 15 policy exceptions, and 15 low-quality or conflicting documents
- **Policy-exception mapping:** nine cases exceeded the `FIN-AP-07` PO/receipt tolerance; six cases presented a role/entity permission violation under `IAM-AP-03`. Every case was expected to block the draft and route to an authorized reviewer with zero ERP write.
- **Release owner / rollback:** Priya Nair; rollback to manual intake with the connector disabled

| Criterion | Promotion threshold | Result | Decision |
| --- | --- | --- | --- |
| Required-field exact match | ≥97.0% | 1,177/1,200 fields (98.1%) | Pass |
| Correct source span | ≥98.0% | 1,192/1,200 fields (99.3%) | Pass |
| Duplicate and PO control recall | 100% on known control cases | 60/60 (100%) | Pass |
| Named tolerance and permission controls | 15/15 policy exceptions blocked and routed; zero ERP writes | `FIN-AP-07`: 9/9; `IAM-AP-03`: 6/6; zero ERP writes | Pass |
| Valid escalation on uncertain cases | ≥95.0% | 15/15 policy cases plus 14/15 low-quality/conflicting cases = 29/30 (96.7%) | Pass; add the missed low-quality scan to regression |
| Median review time | ≤5.0 min | 4.7 min | Pass |
| Unauthorized ERP writes | 0 | 0 | Pass |

The release decision was **promote to staged production**, not “auto-post.” Known limitations—handwriting, credit memos, foreign currency, and non-PO cases—remained routed to the manual path.

## 5. Deploy: advance only through evidence gates

The [rollout plan](../../toolkit/rollout-plan.md) named four analysts in one business unit as the first cohort, `#ap-intake-support` as the support route, Priya Nair as release/rollback owner, and the manual queue as the safe state.

### Completed rollout-plan excerpt

| Gate and dates | System behavior | Promotion criteria | Hold or rollback trigger | Decision |
| --- | --- | --- | --- | --- |
| Observe, Jan 12–23 | Measure current work; no AI | Credible baseline and control map | Missing source or owner | Complete |
| Assist, Feb 23–Mar 6 | Draft fields; analyst decides and enters | Offline thresholds pass; users complete scenario training | Added review time or unsupported document | Promote |
| Shadow, Mar 9–13 | Process live copies; no ERP effect | ≥97% field accuracy, 100% control recall, traceable evidence | Any control miss or material offline/field mismatch | Promote after 312 cases |
| Approve, Mar 16–Apr 14 | Analyst approves every ERP draft | 30-day outcome targets and zero policy breaches | Any unauthorized write; correction >8%; tool success <99% in any rolling one-hour window | Continue and widen cohort |
| Bounded autonomy | Reversible ERP draft without case-by-case approval | 60 more days across the widened cohort plus risk approval | Any uncertain control ownership or rollback gap | **Hold** |

The team rehearsed the kill switch on 2026-03-12: disable the connector, preserve the trace, route new work to the mailbox, restore the last approved draft state, and notify the cohort. The rehearsal completed in seven minutes with no lost case.

## 6. Enable: transfer Day 2 ownership and measure use

The team used [Adoption, operations, and product feedback](../../skills/adoption-and-feedback.md) to train with real exception scenarios, observe work at the review queue, and transfer ownership before the pilot outcome review.

### Completed [operating plan](../../toolkit/operating-plan.md) excerpt

| Day 2 responsibility | Primary / backup | Trigger and first response |
| --- | --- | --- |
| Business outcome and adoption | Elena Torres / Marcus Lee | One-day intake <90% or adoption <85% weekly → inspect queue and workflow friction |
| Technical service and rollback | Priya Nair / Devon Brooks | Tool success <99% in any rolling one-hour window → disable connector and use manual queue |
| Risk and financial controls | Rina Shah / Omar Bennett | Any control bypass or unauthorized write → kill switch, preserve evidence, Sev-1 review |
| Quality and review burden | Marcus Lee / Jordan Kim | Correction >8% or median review >5.0 min weekly → hold rollout and classify failures |
| Cost and capacity | Elena Torres / Priya Nair | Operating cost >$1.05/invoice monthly → investigate usage and service design |

- **Support:** `#ap-intake-support`, 08:00–18:00 CT; Priya owns service incidents and Elena owns user communication.
- **Cadence:** daily pilot health review, weekly operations review, and monthly outcome/control review.
- **Change control:** model, prompt, integration, policy, data, or autonomy changes require a rerun of the relevant evaluation cases, owner approval, and a rollback target.
- **Learning loop:** the one live duplicate near miss was blocked by the deterministic ERP check, added to `AP-INTAKE-v1.3`, and reviewed before cohort expansion.

### Thirty-day measured outcome

For additive capacity evidence, timestamped review-UI and ERP audit events measured foreground active time; waiting and idle gaps longer than 60 seconds were excluded. The predeclared matched sample contained 300 stratified pilot invoices and 300 one-to-one baseline matches. Baseline active time totaled 2,544 minutes (8.48 mean); pilot active time totaled 1,452 minutes (4.84 mean). The paired mean reduction was 3.64 minutes per invoice, with a 95% paired-bootstrap confidence interval of 3.22–4.06 minutes from 10,000 resamples. This matched-pair mean—not the difference between the two medians—is the annualization basis.

The tool-success denominator was the 1,431 cases on which an analyst used the assist workflow. A success required extraction, authoritative ERP control queries, and any approved draft write to complete within the service objective; a case sent to manual fallback after a tool failure would count as unsuccessful. All 1,431 assisted cases completed successfully (100%). No rolling one-hour window fell below 99%, so the rollout and operating trigger never fired. The 55 eligible cases processed manually by operator choice counted against adoption, not tool success.

| Signal | Result | Target | Interpretation |
| --- | --- | --- | --- |
| Adoption | 1,431/1,486 eligible invoices (96.3%) | ≥85.0% | Met |
| Median active handling | 4.6 min, down from 8.0 min | ≤5.0 min | Met; 42.5% reduction |
| Matched-sample mean active time | 1,452/300 = 4.84 min, down from 2,544/300 = 8.48 min | Predeclared 300 matched pairs | 3.64 min mean reduction; 95% CI 3.22–4.06 |
| AI drafts needing correction | 99/1,431 assisted invoices (6.9%) | ≤8.0% | Met |
| Entered within one business day | 1,358/1,486 (91.4%) | ≥90.0% | Met |
| Tool success | 1,431/1,431 assisted cases (100%) | ≥99% in every rolling one-hour window | Met; no below-99% one-hour breach |
| Policy breaches / unauthorized writes | 0 / 0 | 0 / 0 | Met |
| Operating cost | $0.88 per eligible invoice | ≤$1.05 | Met for this cohort |

## 7. Expand: separate expand, hold, and stop decisions

The refreshed [business case](../../toolkit/business-case.md) used measured pilot values and a new [opportunity scorecard](../../toolkit/opportunity-scorecard.md) review. It did not treat user enthusiasm as expansion evidence.

### Completed business-case excerpt

| Item | Completed value |
| --- | --- |
| Full eligible scope | 7,500 invoices/month, or 90,000/year |
| Annualization basis | Defined 300-pair matched sample: 3.64 min mean reduction, with 95% paired-bootstrap CI 3.22–4.06 |
| Annual capacity released | 3.64 min × 90,000 ÷ 60 = 5,460 hours; 95% interval 4,830–6,090 hours |
| Gross annual capacity value | 5,460 hours × $58 loaded hourly cost = $316,680; 95% interval $280,140–$353,220; this is capacity value, not cash savings |
| Annual operating cost | $84,000 ($0.93/invoice) for service, monitoring, support, and control review |
| Net recurring capacity value | $316,680 − $84,000 = $232,680/year; 95% interval $196,140–$269,220 |
| One-time delivery and enablement | $165,000 |
| Implied payback | $165,000 ÷ $232,680 × 12 = 8.5 months; uncertainty range 7.4–10.1 months |
| Investment gate | Payback ≤12 months at the lower-benefit bound; 10.1 months, pass |

Elena Torres recorded three distinct decisions on 2026-04-20:

1. **Expand the human-approved workflow** to the remaining eight US AP analysts and the second US business unit. Quality, adoption, on-time processing, control, reliability, cost, and the conservative payback gate all passed: tool success was 1,431/1,431 with no below-99% one-hour breach, and the lower-benefit bound implied 10.1 months against the ≤12-month gate. Day 2 owners accepted the additional load.
2. **Hold bounded autonomy.** The pilot covered one business unit for only 30 days, did not include quarter-end seasonality, and still relied on analyst judgment for conflicting supplier details. Promotion requires 60 additional days across the wider cohort, zero control breaches, correction at or below 8.0%, and explicit Finance Controls approval.
3. **Stop bank-detail-change scope in this engagement.** It changes the workflow, actors, fraud consequence, and evidence requirements; there is no baseline or approved recovery design. Any future proposal must re-enter [Discover](../../stages/01-discover/README.md) as vendor-master work rather than ride the invoice-intake rollout.

## Limitations and what the evidence does not prove

- The 30-day pilot involved four analysts, one business unit, English-language USD PDFs, and no quarter-end peak; results may not transfer to other document types, regions, or periods.
- The financial result values released capacity. It does not claim a headcount reduction, cash savings, or revenue increase.
- Annualized capacity assumes the matched-sample mean reduction persists across 90,000 eligible invoices. The 95% interval reflects sampling uncertainty, not quarter-end seasonality, mix changes, adoption changes, or operating-cost variance; annual value remains a projection rather than a measured annual result.
- The cohort observed 1,431 successful assisted cases and no one-hour reliability breach. That does not establish reliability at wider-cohort load, so the same rolling-window trigger and manual fallback remain in force during expansion.
- Zero observed policy breaches does not prove zero future risk. Deterministic controls, human approval, monitoring, and rollback remain required.
- The system did not approve invoices, change vendor master data, release payment, or reach bounded autonomy.
- Wider rollout is a new evidence period. Any threshold breach can hold rollout, narrow scope, or return the team to Frame or Design.

## Artifact and skill index

| Type | Interfaces demonstrated |
| --- | --- |
| Toolkit | [Opportunity scorecard](../../toolkit/opportunity-scorecard.md), [Workflow trace](../../toolkit/workflow-trace.md), [Responsibility matrix](../../toolkit/responsibility-matrix.md), [Evaluation pack](../../toolkit/evaluation-pack.md), [Rollout plan](../../toolkit/rollout-plan.md), [Operating plan](../../toolkit/operating-plan.md), [Business case](../../toolkit/business-case.md) |
| Skills | [Workflow discovery and opportunity framing](../../skills/workflow-discovery.md), [Human, software, and AI system design](../../skills/ai-system-design.md), [Evaluation and staged rollout](../../skills/evaluation-and-rollout.md), [Adoption, operations, and product feedback](../../skills/adoption-and-feedback.md) |
