# Agent skills

Agent skills are the kit's methods packaged so that an agent harness such as Claude Code or Codex can run them. Each skill is a thin procedure: it supplies the judgment calls an agent must make while working (what to ask for first, what to refuse to invent, when to stop) and the order of operations. The human skill guide under [skills/](../skills/README.md) supplies the reasoning; the toolkit artifact under [toolkit/](../toolkit/README.md) supplies the structure. A person reads the guide, an agent runs the skill, and both fill the same template. The rule is recorded in [ADR 0002](../docs/decisions/0002-agent-skills-wrap-human-guides.md).

## Installation

Copy one skill directory into the place your harness reads skills from:

| Location | Scope |
| --- | --- |
| `<your project>/.claude/skills/<name>/` | One project, Claude Code |
| `<your project>/.agents/skills/<name>/` | One project, harnesses that follow the AI-DLC layout |
| Your personal skills location (for example `~/.claude/skills/<name>/`) | Every project on your machine |

```sh
cp -r agents/skills/fde-workflow-trace <your project>/.claude/skills/
```

Copy the whole directory so the `SKILL.md` keeps its name. The relative links inside a skill point back into this repository; keep a checkout of the kit beside your project, or read the linked guide and template from GitHub when the skill cites them.

This repository's own `.claude/skills/` and `.agents/skills/` are rendered from `ai-dlc.toml` and reserved for AI-DLC-managed files, so kit skills are not installed there. Distribution as an AI-DLC workflow bundle is a later path; see the [roadmap](../docs/roadmap.md).

## Skills

| Skill | Use when | Fills | Defers to |
| --- | --- | --- | --- |
| [fde-workflow-trace](skills/fde-workflow-trace/SKILL.md) | Observing or reconstructing a real workflow case before proposing AI | [Workflow trace](../toolkit/workflow-trace.md) | [Workflow discovery](../skills/workflow-discovery.md), [Discovery interviewing](../skills/discovery-interviewing.md) |
| [fde-opportunity-scorecard](skills/fde-opportunity-scorecard/SKILL.md) | Comparing candidate workflows and recording an advance, investigate, defer, or enable-locally decision | [Opportunity scorecard](../toolkit/opportunity-scorecard.md) | [Workflow discovery](../skills/workflow-discovery.md) |
| [fde-responsibility-matrix](skills/fde-responsibility-matrix/SKILL.md) | Assigning responsibilities to AI, deterministic software, and accountable humans | [Responsibility matrix](../toolkit/responsibility-matrix.md) | [AI system design](../skills/ai-system-design.md), [Agent and tool design](../skills/agent-and-tool-design.md), [System patterns](../learning/system-patterns.md) |
| [fde-eval-pack](skills/fde-eval-pack/SKILL.md) | Turning cases and production failures into a versioned evaluation record and release decision | [Evaluation pack](../toolkit/evaluation-pack.md) | [Grader design and error analysis](../skills/eval-engineering.md), [Evaluation and staged rollout](../skills/evaluation-and-rollout.md) |
| [fde-security-review](skills/fde-security-review/SKILL.md) | Preparing an LLM system for an enterprise security and governance review | [AI security and governance review](../toolkit/ai-security-review.md) | [Production readiness](../skills/production-readiness.md), [Agent and tool design](../skills/agent-and-tool-design.md), [Retrieval and grounding](../skills/retrieval-and-grounding.md) |
| [fde-field-report](skills/fde-field-report/SKILL.md) | Sending a reproducible model, product, or platform issue upstream | [Field report](../toolkit/field-report.md) | [Grader design and error analysis](../skills/eval-engineering.md), [Adoption and feedback](../skills/adoption-and-feedback.md) |

## How a skill behaves

- **Asks for evidence before producing.** Every skill opens with an "Obtain first" checklist. The agent collects those inputs from the user, the repository, or linked records before it writes a line of the artifact.
- **Never invents.** Owners, thresholds, evidence, dates, approvals, and results come from the user or a cited source. When one is missing, the skill writes `[gap: what is missing and who can supply it]` in that position and continues.
- **Labels heuristics.** A number the skill supplies as a rule of thumb is labeled a starting heuristic, not an industry standard, the same way the guides do.
- **Keeps customer data out of reports.** Artifacts reference records, documents, and configurations by identifier; they do not carry record contents, credentials, or personal data.
- **Leaves decisions with their owners.** A skill records a decision that a named owner has made, or lists the decision as open with the evidence assembled for it. It does not advance the decision itself.
- **Ends with the artifact's completion checks.** The agent reports each check as met or not met, with the gaps that block it.

## Contributing a skill

1. Create `agents/skills/<name>/SKILL.md`, with a name prefixed `fde-` so it cannot collide with AI-DLC's own skills.
2. Start with frontmatter: `name:` equal to the directory name and a one-sentence `description:` that begins "Use when".
3. Write the body with exactly these `##` sections: Use when, Obtain first, Procedure, Output, Rules, Completion checks. Keep the body between 300 and 550 words (a starting heuristic for this repository, not an industry standard). Reference the guide for judgment and the template for structure; do not restate either.
4. Link with relative paths from the skill directory (`../../../toolkit/...`, `../../../skills/...`).
5. Add a row to the table above and run `python3 scripts/check_schemas.py`.
