# Contributing to FDE Kit

FDE Kit is practical by design. Add content when it gives a concrete learning or field-use benefit, has a clear home, is accurate enough to use, and links to the relevant lifecycle context. This page states the quality bar, the content conventions, and the workflow.

## Where content belongs

| Section | Answers | Contains | Never contains |
| --- | --- | --- | --- |
| `learning/` | What should I understand and why? | Concepts, mental models, patterns, curriculum, glossary | Templates, stage checklists |
| `stages/` | What should happen now? | One README per lifecycle stage with the shared schema | Reusable artifacts, method detail |
| `skills/` | How do I perform a capability well? | Method guides with technique, examples, practice, rubric | Copy-ready templates |
| `toolkit/` | What can I use right now? | Artifacts with purpose, timing, instructions, template, checks | Teaching text beyond instructions |
| `examples/` | What does good work look like? | Completed fictional engagements | Instructions, placeholders |
| `agents/` | How does my harness run the method? | Thin agent skills that wrap a guide and a template | Judgment that belongs in the guide |

If a contribution does not fit one row, it probably needs to be split or does not belong.

## Content conventions

These conventions keep the kit usable in real engagements. Reviewers check them.

1. **Write for a practitioner under time pressure.** Lead with the decision or action. Short paragraphs. Tables for comparisons. No preamble about how important the topic is.
2. **Evidence over opinion.** Ask for sources, owners, dates, thresholds, and failure paths. A claim about a customer, a model, or a result needs a stated basis.
3. **Heuristics are labeled.** Any number used as a rule (a threshold, a sample size, a slide count) is "a starting heuristic, not an industry standard", stated on the page.
4. **Concrete good and weak patterns.** Every skill guide contrasts a specific good pattern with a specific weak one. Use the invoice-intake engagement or another realistic setting; never a vague "a company".
5. **Vendor-neutral, mechanism-specific.** Name mechanisms (structured output, tool calling, retrieval, model-graded evaluation, tracing). Do not teach one vendor's SDK or claim a vendor's private behavior.
6. **Fictional is stated.** Examples and scenarios say they are fictional in the first lines.
7. **Link into the lifecycle.** New guides and artifacts link the stages they serve and the artifacts they use, and the stage pages and section indexes link back.
8. **Diagrams are Mermaid** beside the text they explain. See [ADR 0003](docs/decisions/0003-mermaid-for-diagrams.md).
9. **No placeholders.** No "TODO", "TBD", or empty sections. Unfinished content stays on a branch.
10. **Plain language.** No hype, no anthropomorphizing the model beyond what the mechanism does, no unexplained acronyms on first use.

## Required schemas

`scripts/check_schemas.py` enforces these. Section headings are `##` and appear in this order.

- **Toolkit artifact:** Purpose, Timing, Instructions, Expected output, Supported stages, Template (with a ```` ```markdown ```` block), Completion checks (with `- [ ]` items).
- **Skill guide:** Relevance, Timing, Technique, Examples, Practice, Self-assessment, Links.
- **Stage page:** Objective, Entry conditions, Questions to answer, Recommended activities, Expected deliverables, Exit criteria, Common failure modes, Related capabilities, Practice.
- **Curriculum module:** Outcome, Prerequisites, Study, Exercise, Assessment, Next.
- **Agent skill:** `agents/skills/<name>/SKILL.md` with frontmatter `name: <name>` and `description:`.
- **Worked example:** states it is fictional, references all seven stages, and ends with an "Artifact and skill index" that lists only artifacts the narrative used.

## Workflow

This repository uses [AI-DLC](https://github.com/Sean-Koval/ai-dlc); see [AI-DLC.md](AI-DLC.md) and the [development workflow](docs/development-workflow.md).

1. For anything larger than a fix, record scope and acceptance in `.ai-dlc/work/<id>.toml` (copy `.ai-dlc/examples/work.toml.example`) and, when the change alters what the kit teaches, a design note in `docs/design/`. Consequential choices get an ADR in `docs/decisions/`.
2. Write the content and update every index and stage page that should link it.
3. Run the required checks:

   ```sh
   ai-dlc project check --required
   ```

   Without the AI-DLC CLI, run the same scripts directly:

   ```sh
   python3 scripts/check_generated.py
   python3 scripts/check_links.py
   python3 scripts/check_schemas.py
   python3 scripts/check_whitespace.py
   ```

4. Commit with a conventional prefix (`docs:`, `feat:`, `fix:`, `chore:`) and a message that names the outcome, not the file list.
5. Open a pull request. CI runs the same checks.

Do not edit `AGENTS.md`, `CLAUDE.md`, `.claude/skills/`, `.agents/skills/`, `.mcp.json`, or `.codex/config.toml` by hand; they are rendered from `ai-dlc.toml` with `ai-dlc agents render --apply`.
