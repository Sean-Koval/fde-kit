# FDE Learning Center Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Organize the repository into a practical learning center and lifecycle-based toolkit for Forward Deployed Engineers.

**Architecture:** Foundational concepts live in learning, engagement guidance in stages, cross-stage instruction in skills, and directly usable artifacts in toolkit. A small examples index establishes the future home for coherent worked engagements without adding speculative placeholder content.

**Tech Stack:** Markdown, Reveal.js HTML, Git, POSIX shell validation commands

**Spec:** docs/superpowers/specs/2026-08-24-fde-learning-center-design.md

## Global Constraints

- The lifecycle is exactly Discover → Frame → Design → Build → Deploy → Enable → Expand.
- Create useful navigation and stage guidance without adding empty category directories or placeholder files.
- Do not create a top-level resources directory or generic public-facing docs bucket.
- Do not duplicate reusable artifacts inside stage directories; stages link to skills and toolkit content.
- Preserve fde_reveal_deck_v3.html byte-for-byte when moving it to learning/presentations/fde-overview.html.
- Keep the initial release lean: one strong README per stage and indexes for future skills, toolkit assets, and examples.

---

## File Map

- README.md: Repository purpose, audience, navigation, lifecycle, and learner/practitioner entry paths.
- learning/README.md: Learning-center index and boundary definition.
- learning/what-is-an-fde.md: FDE role, responsibilities, distinctions, and success measures.
- learning/operating-principles.md: Opinionated principles for effective FDE engagement work.
- learning/engagement-lifecycle.md: Seven-stage lifecycle overview and transition logic.
- learning/presentations/fde-overview.html: Existing Reveal.js overview deck, renamed without content changes.
- stages/README.md: Lifecycle navigation and common stage-page conventions.
- stages/01-discover/README.md through stages/07-expand/README.md: Operational guidance for each lifecycle stage.
- skills/README.md: Quality bar, candidate capability map, and contribution format for skill guides.
- toolkit/README.md: Quality bar, candidate asset map, and contribution format for reusable artifacts.
- examples/README.md: Planned coherent sample-engagement shape.

### Task 1: Establish the repository gateway and learning foundation

**Files:**
- Create: README.md
- Create: learning/README.md
- Create: learning/what-is-an-fde.md
- Create: learning/operating-principles.md
- Create: learning/engagement-lifecycle.md
- Move: fde_reveal_deck_v3.html to learning/presentations/fde-overview.html

**Interfaces:**
- Consumes: The content boundaries and lifecycle defined in the design spec.
- Produces: Canonical descriptions and relative links used by every section index and stage page.

- [x] **Step 1: Record the source presentation checksum**

Run:

~~~bash
shasum -a 256 fde_reveal_deck_v3.html
~~~

Expected: one SHA-256 digest followed by the source filename; retain the digest for Step 4.

- [x] **Step 2: Create the learning directories and move the presentation**

Run:

~~~bash
mkdir -p learning/presentations
mv fde_reveal_deck_v3.html learning/presentations/fde-overview.html
~~~

Expected: the renamed presentation exists and the old root-level filename does not.

- [x] **Step 3: Write the repository and learning documents**

Use apply_patch to create the five Markdown files. The root README must include purpose, audience, lifecycle, a content-area table, learner path, active-engagement path, presentation link, and contribution quality bar. The learning pages must define the role, operating principles, and stage transitions without duplicating detailed stage instructions.

- [x] **Step 4: Verify the presentation and learning links**

Run:

~~~bash
shasum -a 256 learning/presentations/fde-overview.html
rg -n '\]\([^)]*\)' README.md learning/*.md
~~~

Expected: the presentation digest exactly matches Step 1, and every listed relative Markdown target exists.

- [x] **Step 5: Commit the gateway and learning foundation**

Run:

~~~bash
git add README.md learning fde_reveal_deck_v3.html
git commit -m "docs: add FDE learning center foundation"
~~~

Expected: a commit containing the learning documents and the presentation rename.

### Task 2: Build the lifecycle stage playbook

**Files:**
- Create: stages/README.md
- Create: stages/01-discover/README.md
- Create: stages/02-frame/README.md
- Create: stages/03-design/README.md
- Create: stages/04-build/README.md
- Create: stages/05-deploy/README.md
- Create: stages/06-enable/README.md
- Create: stages/07-expand/README.md

**Interfaces:**
- Consumes: Canonical lifecycle language from learning/engagement-lifecycle.md.
- Produces: Stable stage paths referenced by the root README and future skills, tools, and examples.

- [x] **Step 1: Create the seven stage directories**

Run:

~~~bash
mkdir -p stages/01-discover stages/02-frame stages/03-design stages/04-build stages/05-deploy stages/06-enable stages/07-expand
~~~

Expected: seven numbered directories exist in lifecycle order.

- [x] **Step 2: Write the lifecycle index**

Use apply_patch to create stages/README.md with a linked seven-stage sequence, an explanation that engagements may loop backward, and the shared stage-page schema.

- [x] **Step 3: Write Discover, Frame, and Design guidance**

Use apply_patch to create the first three stage READMEs. Each must include objective, entry conditions, questions, activities, deliverables, exit criteria, failure modes, related capabilities, and a practice prompt. The progression must turn customer evidence into an agreed problem frame and then a validated solution approach.

- [x] **Step 4: Write Build, Deploy, Enable, and Expand guidance**

Use apply_patch to create the final four stage READMEs with the same schema. The progression must turn the validated approach into working value, production operation, customer independence, and evidence-based expansion.

- [x] **Step 5: Verify stage consistency**

Run:

~~~bash
for file in stages/[0-9][0-9]-*/README.md; do
  for heading in "## Objective" "## Entry conditions" "## Questions to answer" "## Recommended activities" "## Expected deliverables" "## Exit criteria" "## Common failure modes" "## Related capabilities" "## Practice"; do
    rg -q "^$heading$" "$file" || printf "%s missing %s\n" "$file" "$heading"
  done
done
~~~

Expected: no output.

- [x] **Step 6: Commit the lifecycle playbook**

Run:

~~~bash
git add stages
git commit -m "docs: add FDE engagement lifecycle playbook"
~~~

Expected: a commit containing the lifecycle index and all seven stage READMEs.

### Task 3: Define skills, toolkit, and examples boundaries

**Files:**
- Create: skills/README.md
- Create: toolkit/README.md
- Create: examples/README.md
- Modify: README.md

**Interfaces:**
- Consumes: Stage paths from Task 2 and content-boundary language from the design spec.
- Produces: Contribution contracts that prevent skill guides, reusable assets, and worked examples from overlapping.

- [x] **Step 1: Write the skills index**

Use apply_patch to explain that skills are reusable instructional capabilities, list high-value candidate guides mapped to stages, and define the required guide structure: relevance, technique, examples, exercise, rubric, and links.

- [x] **Step 2: Write the toolkit index**

Use apply_patch to explain that toolkit items are directly reusable artifacts, list high-value candidate assets mapped to stages, and define the required artifact metadata: purpose, timing, instructions, expected output, and supported stages.

- [x] **Step 3: Write the examples index**

Use apply_patch to define a coherent fictional engagement as the preferred example format and list its future artifact sequence from customer context through executive update.

- [x] **Step 4: Complete cross-navigation from the root README**

Use apply_patch to ensure the root README links to all five public content areas, all seven lifecycle stages, and the overview presentation using relative paths.

- [x] **Step 5: Commit the content contracts**

Run:

~~~bash
git add README.md skills toolkit examples
git commit -m "docs: define FDE skills toolkit and examples"
~~~

Expected: a commit containing the three indexes and any root navigation refinements.

### Task 4: Verify and publish the initial repository

**Files:**
- Modify: docs/superpowers/plans/2026-08-24-fde-learning-center.md to mark completed steps

**Interfaces:**
- Consumes: All deliverables from Tasks 1–3.
- Produces: A verified main branch published to origin/main.

- [x] **Step 1: Validate required files and forbidden public buckets**

Run:

~~~bash
test -f README.md
test -f learning/presentations/fde-overview.html
test -f learning/what-is-an-fde.md
test -f learning/operating-principles.md
test -f learning/engagement-lifecycle.md
test -f stages/01-discover/README.md
test -f stages/02-frame/README.md
test -f stages/03-design/README.md
test -f stages/04-build/README.md
test -f stages/05-deploy/README.md
test -f stages/06-enable/README.md
test -f stages/07-expand/README.md
test -f skills/README.md
test -f toolkit/README.md
test -f examples/README.md
test ! -d resources
~~~

Expected: exit status 0 with no output.

- [x] **Step 2: Check every relative Markdown link**

Run:

~~~bash
missing=0
while IFS=: read -r file target; do
  case "$target" in
    http:*|https:*|mailto:*|\#*) continue ;;
  esac
  target="${target%%#*}"
  [ -z "$target" ] && continue
  resolved="$(cd "$(dirname "$file")" && pwd)/$target"
  if [ ! -e "$resolved" ]; then
    printf '%s -> %s\n' "$file" "$target"
    missing=1
  fi
done < <(rg -o --no-heading --with-filename '\]\(([^)#]+)(#[^)]*)?\)' -r '$1' --glob '*.md')
exit "$missing"
~~~

Expected: exit status 0 with no missing targets.

- [x] **Step 3: Check repository hygiene**

Run:

~~~bash
git diff --check
find learning stages skills toolkit examples -type d -empty -print
git status --short
~~~

Expected: no whitespace errors, no empty public-facing directories, and only the implementation-plan completion update remains uncommitted.

- [x] **Step 4: Commit the completed implementation plan**

Run:

~~~bash
git add docs/superpowers/plans/2026-08-24-fde-learning-center.md
git commit -m "docs: record FDE learning center implementation"
~~~

Expected: a commit recording completed checklist items.

- [ ] **Step 5: Review commits and push**

Run:

~~~bash
git log --oneline --decorate --max-count=5
git status --short --branch
git push -u origin HEAD:main
~~~

Expected: the worktree is clean and main tracks origin/main after a successful push.
