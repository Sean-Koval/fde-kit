# Operating plan

## Purpose

Transfer a production AI workflow into durable Day 2 operation. Define service and business ownership, observability, support, incident response, change control, learning, and routine outcome review.

## Timing

Create before production deployment in [Deploy](../stages/05-deploy/README.md). Confirm and practice it in [Enable](../stages/06-enable/README.md); use it to inform [Expand](../stages/07-expand/README.md).

## Instructions

1. Name the business outcome, technical service, and risk/control owners, including backups and escalation routes.
2. Instrument workflow quality, abstention, review load, drift, latency, cost, tool errors, and business impact—not only model uptime.
3. Set operating objectives, alert thresholds, response expectations, fallback modes, and incident communication.
4. Require evaluation, approval, and rollback evidence for changes to models, prompts, policy, integrations, data, or autonomy limits.
5. Establish a recurring review that turns production traces and user feedback into prioritized improvements or a decision to revisit an earlier stage.

## Expected output

An owner-approved operating contract that supports safe operation, recovery, controlled change, and measurable learning after launch.

## Supported stages

- [Deploy](../stages/05-deploy/README.md)
- [Enable](../stages/06-enable/README.md)
- [Expand](../stages/07-expand/README.md)

## Template

```markdown
# Operating plan — [workflow/service]

## Service and ownership

- **Service purpose and workflow outcome:** [what the service enables and the measurable result]
- **Business outcome owner / backup:** [name and contact]
- **Technical service owner / backup:** [name and contact]
- **Risk/control owner / backup:** [name and contact]
- **Support route and user audience:** [channel, hours, response expectation]
- **Escalation path:** [severity levels, incident lead, customer communication owner]
- **Safe fallback mode:** [manual workflow, disabled automation, or prior version]

## Operating signals

| Signal | Definition and source | Baseline / objective | Alert or review trigger | Cadence | Primary owner | First response |
| --- | --- | --- | --- | --- | --- | --- |
| Workflow quality | [correct outcomes with evidence] | [baseline/objective] | [trigger] | [cadence] | [name] | [review queue, hold, or incident] |
| Review burden and abstention | [time, queue, or rate] | [baseline/objective] | [trigger] | [cadence] | [name] | [adjust scope or staffing] |
| Safety and policy | [control outcome] | [objective] | [trigger] | [cadence] | [name] | [disable action and escalate] |
| Reliability | [latency, errors, availability, tool health] | [objective] | [trigger] | [cadence] | [name] | [fallback and incident response] |
| Cost and capacity | [cost per case, usage, queue] | [objective] | [trigger] | [cadence] | [name] | [throttle, investigate, or revise] |
| Business outcome | [measure and source] | [baseline/objective] | [review trigger] | [cadence] | [name] | [outcome review] |

## Incident and recovery runbook

| Severity / trigger | Triage owner | Immediate safe action | Evidence to preserve | Escalation and communication | Recovery / rollback condition |
| --- | --- | --- | --- | --- | --- |
| [policy or safety breach] | [name] | [disable automation, queue work] | [trace, inputs, outputs, tool calls] | [risk owner and users] | [approved remediation and test] |
| [quality or drift breach] | [name] | [hold promotion or narrow scope] | [evaluation and traces] | [business owner] | [threshold restored and decision recorded] |
| [service failure] | [name] | [fallback to manual/prior version] | [logs and incident timeline] | [technical owner and users] | [health restored and rehearsal complete] |

## Change control and learning

| Change | Required evaluation and approvals | Release / rollback plan | Owner | Review date | Production learning to capture |
| --- | --- | --- | --- | --- | --- |
| [model, prompt, policy, data, integration, autonomy limit] | [evaluation pack, owners] | [gate and safe state] | [name] | [date] | [failure, feedback, or opportunity] |

## Review cadence

- **Weekly operational review:** [attendees, signals, decisions]
- **Monthly outcome review:** [attendees, business measure, adoption evidence, improvement decision]
- **Regression intake:** [how meaningful failures become evaluation cases]
```

## Completion checks

- [ ] Business, technical, and risk/control owners plus backups and escalation routes are named.
- [ ] Outcome, quality, safety, reliability, review burden, and cost signals have objectives and response paths.
- [ ] Incidents preserve evidence, invoke a safe fallback, and have recovery and communication responsibilities.
- [ ] Changes require evaluation, approval, release evidence, and a rollback plan.
