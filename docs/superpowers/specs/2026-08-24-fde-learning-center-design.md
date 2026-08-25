# FDE Learning Center and Toolkit Design

## Purpose

This repository will help Forward Deployed Engineers learn the role, understand the lifecycle of a customer engagement, practice reusable capabilities, and apply practical artifacts during real work.

The information architecture must make four questions easy to answer:

1. What should an FDE understand?
2. What should an FDE do at this point in an engagement?
3. How does an FDE perform an important capability well?
4. What artifact can an FDE use immediately?

## Repository Structure

```text
fde-kit/
├── README.md
├── learning/
│   ├── README.md
│   ├── what-is-an-fde.md
│   ├── operating-principles.md
│   ├── engagement-lifecycle.md
│   └── presentations/
│       └── fde-overview.html
├── stages/
│   ├── README.md
│   ├── 01-discover/
│   ├── 02-frame/
│   ├── 03-design/
│   ├── 04-build/
│   ├── 05-deploy/
│   ├── 06-enable/
│   └── 07-expand/
├── skills/
│   └── README.md
├── toolkit/
│   └── README.md
└── examples/
    └── README.md
```

The initial implementation will stay deliberately lean. It will create useful navigation and stage guidance without adding empty category directories or placeholder files.

## Content Boundaries

### Learning

`learning/` explains concepts and mental models. It contains the FDE role overview, operating principles, lifecycle overview, and high-level presentation.

Learning content answers **what** and **why**. It does not contain reusable templates or duplicate stage instructions.

### Stages

`stages/` is the operational spine of the repository. Its lifecycle is:

```text
Discover → Frame → Design → Build → Deploy → Enable → Expand
```

Each stage begins with one useful `README.md` containing:

- Objective
- Entry conditions
- Questions to answer
- Recommended activities
- Expected deliverables
- Exit criteria
- Common failure modes
- Relevant skills and toolkit assets
- A short practice prompt

Stage content answers **what should happen now**. As the repository grows, a stage may be split into focused files only when its README becomes difficult to navigate.

### Skills

`skills/` teaches reusable capabilities that span multiple lifecycle stages. Examples include discovery interviewing, problem framing, rapid prototyping, technical communication, stakeholder management, and production readiness.

A mature skill guide should contain:

- Definition and relevance
- Situations in which it matters
- A repeatable technique
- Good and bad examples
- Practice exercise
- Self-assessment rubric
- Links to applicable stages and toolkit assets

Skills answer **how to perform a capability well**. They are instructional rather than downloadable artifacts.

### Toolkit

`toolkit/` contains artifacts intended for direct use. Future assets may include interview guides, worksheets, architecture review checklists, prototype scopes, deployment checklists, workshop guides, prompts, and small scripts.

Each artifact must state its purpose, when to use it, instructions, expected output, and supported lifecycle stages.

Toolkit content answers **what can I use right now**. A skill may teach discovery interviewing; a toolkit asset may provide the interview guide.

### Examples

`examples/` demonstrates what good FDE work looks like. The preferred future example is one coherent fictional engagement that connects customer context, discovery evidence, problem framing, solution design, prototype planning, deployment, and executive communication.

Examples should show completed outputs rather than repeat instructional material.

## Explicit Exclusions

The initial structure will not include:

- A generic top-level `docs/` content bucket beyond internal design and plan records
- A top-level `resources/` directory
- Empty directories for speculative future categories
- A glossary before specialized terminology warrants one
- Generic software-engineering tutorials without a clear FDE context
- Duplicated checklists in both stages and the toolkit
- Uncurated lists of external links

Further reading belongs next to the relevant learning topic or skill.

## Root README

The root README will serve as the repository gateway. It will:

- Define the intended audience and purpose
- Explain the difference among learning, stages, skills, toolkit, and examples
- Show the seven-stage engagement lifecycle
- Provide separate starting paths for learners and active practitioners
- Link to the FDE overview presentation
- Explain that the repository is intentionally practical and will grow through useful, tested content

## Initial Release Scope

The first commit will include:

- A complete root README
- The high-level presentation moved into `learning/presentations/fde-overview.html`
- Foundational learning pages
- A lifecycle index
- Seven useful stage READMEs
- Initial indexes for skills, toolkit, and examples
- Internal design and implementation-plan records

It will not manufacture large volumes of thin content. New skills, templates, and examples should be added only when they provide a concrete learning or field-use benefit.

## Verification

Before completion:

- Every internal Markdown link will be checked.
- Every expected file will be present.
- No empty public-facing directories will remain.
- The presentation will remain byte-identical after it is moved.
- The repository status and commit contents will be reviewed before pushing.
