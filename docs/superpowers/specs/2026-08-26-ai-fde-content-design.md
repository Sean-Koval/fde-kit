# AI FDE Content Design

## Purpose

Turn the repository's high-level AI implementation presentation into the canonical overview of how an AI-focused Forward Deployed Engineer operates, then make its core artifacts usable through skills, toolkit templates, and one coherent example.

The release must help an aspiring FDE understand the operating model and help a practicing FDE begin an engagement without inventing the basic artifacts from scratch.

## Content Model

The presentation remains a concise, persuasive field playbook rather than a training course. It covers the complete AI implementation engagement while keeping workflow discovery, human/software/AI boundaries, evaluation, and staged autonomy as its center of gravity.

The deck's operating model is:

**Find leverage → Map reality → Design the boundary → Prove quality → Land production → Transfer ownership → Compound learning**

This model complements the repository lifecycle:

**Discover → Frame → Design → Build → Deploy → Enable → Expand**

The presentation introduces the ideas. Skills teach repeatable techniques. Toolkit files are copy-ready working artifacts. The example shows the artifacts used together.

## Presentation Requirements

- Keep the presentation between 16 and 18 horizontal slides.
- Preserve the dark, restrained field-operations aesthetic and mint accent.
- Use point units for presentation typography except Reveal's required base size.
- Give every slide a stable, unique `id` and put visible copy in semantic text elements.
- Replace dense text with diagrams where relationships or sequence matter.
- Cover technical scoping, enterprise integration, security/governance, production operations, adoption, product feedback, and evidence-based expansion.
- Keep numeric rules explicitly labeled as starting heuristics.
- Include concise primary-source attribution to current OpenAI, Palantir, Stripe, and Scale AI role descriptions.
- Do not turn the deck into a generic description of all FDE roles; it is specifically an AI implementation field playbook.

## Toolkit Requirements

Create seven directly reusable Markdown artifacts:

1. Opportunity scorecard
2. Workflow trace
3. Responsibility matrix
4. Evaluation pack
5. Rollout plan
6. Operating plan
7. Business case

Each artifact must state purpose, use timing, instructions, expected output, supported stages, a copy-ready template, and completion checks. Templates must elicit evidence and decisions rather than generic commentary.

## Skills Requirements

Create four cross-stage guides:

1. Workflow discovery and opportunity framing
2. Human/software/AI system design
3. Evaluation and staged rollout
4. Adoption, operations, and product feedback

Each guide must explain relevance, timing, technique, good and weak patterns, a practice exercise, self-assessment, and links to applicable stages and toolkit files.

## Worked Example

Create one fictional but realistic accounts-payable invoice-intake engagement. It must show the progression from operational pain through architecture, evaluation, rollout, adoption, operating ownership, measured impact, and a justified expansion decision. Include completed excerpts of all seven toolkit artifacts without duplicating their full instructions.

## Explicit Exclusions

- No new top-level content category.
- No downloadable office-document formats in this release.
- No vendor-specific implementation tutorial or sample application code.
- No uncurated link collection.
- No unsupported claim that a heuristic is an industry standard.

## Verification

- Render and inspect every presentation slide.
- Check presentation overflow and HTML structure.
- Check every relative Markdown link.
- Confirm all seven toolkit artifacts and four skills meet their required schemas.
- Confirm stage pages link to real skills and toolkit assets.
- Confirm the example references all seven artifacts and all seven lifecycle stages.
- Run `git diff --check` and confirm a clean feature worktree after commits.
