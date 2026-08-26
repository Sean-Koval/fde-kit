# Deploy

Deploy puts the working solution into the customer’s operating environment responsibly.

## Objective

Put the solution into the customer’s operating environment with the required reliability, security, observability, and support arrangements.

## Entry conditions

- The solution satisfies its intended use for the agreed scope.
- Production requirements, limitations, and accountable owners are known.
- The customer environment, release path, and relevant operational controls are available.

## Questions to answer

- What reliability, security, privacy, compliance, and access requirements apply in production?
- How will the team release, observe, support, and recover the solution?
- Who owns operations, incident response, maintenance, and customer communication?
- What rollout approach limits risk while producing evidence of production readiness?

## Recommended activities

- Validate production configuration, access, integrations, data handling, and operational dependencies.
- Instrument the solution so owners can observe health, usage, and outcome signals.
- Define rollout, rollback, incident response, support, and communication procedures.
- Release in an appropriate sequence, monitor the result, and resolve production issues with the accountable owners.

## Expected deliverables

- A deployed solution in the customer’s operating environment.
- Production runbooks covering release, monitoring, support, rollback, and incident response.
- Observability signals and ownership for service health, usage, and outcomes.
- A rollout record with readiness evidence, known limitations, and follow-up actions.

## Exit criteria

- The outcome is available for the intended people to use.
- Reliability, security, observability, and support arrangements are operating with clear ownership.
- The release has evidence that it can be operated safely within the agreed scope.

## Common failure modes

- Treating a successful demo or technical release as a production deployment.
- Releasing without usable monitoring, rollback, or support ownership.
- Ignoring customer environment constraints that were not exercised during build.
- Calling deployment complete before the intended people can access and use the outcome.

## Related capabilities

- [Human, software, and AI system design](../../skills/ai-system-design.md)
- [Evaluation and staged rollout](../../skills/evaluation-and-rollout.md)
- [Adoption, operations, and product feedback](../../skills/adoption-and-feedback.md)
- [Responsibility matrix](../../toolkit/responsibility-matrix.md)
- [Evaluation pack](../../toolkit/evaluation-pack.md)
- [Rollout plan](../../toolkit/rollout-plan.md)
- [Operating plan](../../toolkit/operating-plan.md)
- [Business case](../../toolkit/business-case.md)

Related catalogs: [Skills](../../skills/README.md) teach reusable capabilities; [Toolkit](../../toolkit/README.md) contains reusable artifacts.

## Practice

For a working increment, write a lightweight rollout plan that names the first users, one health signal, one outcome signal, a rollback trigger, and the owner responsible for responding to it.
