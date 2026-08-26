# AI FDE Content Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver a visually stronger AI FDE overview deck backed by practical skills, toolkit artifacts, and one worked engagement.

**Architecture:** The deck defines the operating model and names the field artifacts. Four skills teach reusable methods, seven toolkit files provide copy-ready templates, and one worked example demonstrates the complete lifecycle. Existing stage pages provide navigation rather than duplicating the detailed content.

**Tech Stack:** Markdown, Reveal.js 5 HTML/CSS, Node-based slide validation, Git

**Spec:** docs/superpowers/specs/2026-08-26-ai-fde-content-design.md

## Global Constraints

- Keep the presentation specifically about AI implementation FDE work and between 16 and 18 horizontal slides.
- Preserve the dark field-operations visual language and mint accent.
- Use point units for slide typography except Reveal's required base size.
- Numeric rules are starting heuristics, not asserted industry standards.
- Skills teach techniques; toolkit files contain reusable artifacts; stages link instead of duplicating them.
- Add no new top-level content category, vendor tutorial, office-document binary, or generic resources bucket.

---

### Task 1: Revise the AI FDE field-playbook deck

**Files:**
- Modify: `learning/presentations/fde-overview.html`
- Modify: `learning/README.md`
- Modify: `learning/what-is-an-fde.md`

**Interfaces:**
- Consumes: The operating model and presentation requirements in the spec.
- Produces: Canonical deck terminology and seven named field artifacts used by later tasks.

- [ ] Replace dense slides with an opportunity heatmap, observation loop, representative workflow swimlane, layered enterprise architecture, evaluation flywheel, deployment gates, and lifecycle artifact map.
- [ ] Add complete AI FDE ownership, technical delivery, enterprise integration, security/governance, Day 2 operations, adoption, product feedback, and expansion coverage without exceeding 18 slides.
- [ ] Add unique slide IDs, semantic visible copy, point-based typography, speaker notes, and primary-source links.
- [ ] Update learning copy so the role description explicitly frames this repository around AI implementation.
- [ ] Run structural checks, overflow checks, and render screenshots of every slide; inspect and correct visual defects.
- [ ] Commit with `docs: refine AI FDE field playbook`.

### Task 2: Create the field toolkit

**Files:**
- Create: `toolkit/opportunity-scorecard.md`
- Create: `toolkit/workflow-trace.md`
- Create: `toolkit/responsibility-matrix.md`
- Create: `toolkit/evaluation-pack.md`
- Create: `toolkit/rollout-plan.md`
- Create: `toolkit/operating-plan.md`
- Create: `toolkit/business-case.md`
- Modify: `toolkit/README.md`

**Interfaces:**
- Consumes: Artifact names and lifecycle language from Task 1.
- Produces: Stable artifact paths linked by skills, stages, and the example.

- [ ] Write seven copy-ready artifacts with purpose, timing, instructions, output, supported stages, template, and completion checks.
- [ ] Make safety, ownership, evidence, rollback, and measurable impact explicit where relevant.
- [ ] Replace the candidate-only toolkit catalog with links to the real artifacts while preserving the contribution contract.
- [ ] Validate every artifact against the required schema and commit with `docs: add AI FDE field toolkit`.

### Task 3: Add cross-stage AI FDE skills

**Files:**
- Create: `skills/workflow-discovery.md`
- Create: `skills/ai-system-design.md`
- Create: `skills/evaluation-and-rollout.md`
- Create: `skills/adoption-and-feedback.md`
- Modify: `skills/README.md`
- Modify: `stages/01-discover/README.md` through `stages/07-expand/README.md`

**Interfaces:**
- Consumes: Toolkit paths from Task 2.
- Produces: Four instructional guides and stage-to-content navigation.

- [ ] Write four guides containing relevance, timing, repeatable technique, good/weak patterns, practice, self-assessment, and stage/toolkit links.
- [ ] Replace the candidate-only skills catalog with links to the real guides and retain only genuinely useful future candidates.
- [ ] Update every stage's Related capabilities section to link to applicable real skills and toolkit assets.
- [ ] Check all relative links and commit with `docs: add AI FDE capability guides`.

### Task 4: Demonstrate the complete lifecycle

**Files:**
- Create: `examples/invoice-intake-ai/README.md`
- Modify: `examples/README.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: All seven toolkit artifacts, four skills, and seven lifecycle stages.
- Produces: A canonical worked example and updated repository entry paths.

- [ ] Write a fictional accounts-payable engagement showing Discover through Expand and completed excerpts of all seven artifacts.
- [ ] Include baseline, target, architecture, evaluation thresholds, staged rollout, Day 2 ownership, measured outcome, limitations, and evidence-based expansion decision.
- [ ] Update example and root navigation to point to substantive content rather than future catalogs.
- [ ] Verify the example references every artifact and lifecycle stage, then commit with `docs: add worked AI FDE engagement`.

### Task 5: Verify the integrated release

**Files:**
- Modify: `docs/superpowers/plans/2026-08-26-ai-fde-content.md`

**Interfaces:**
- Consumes: Tasks 1–4.
- Produces: A verified feature branch ready for integration.

- [ ] Check required files, artifact/skill schemas, stage schemas, deck slide count and IDs, source links, and example coverage.
- [ ] Check all relative Markdown links, empty public directories, forbidden top-level resources, and whitespace errors.
- [ ] Re-render and inspect every slide after the integrated changes.
- [ ] Mark completed plan steps and commit with `docs: record AI FDE content implementation`.
