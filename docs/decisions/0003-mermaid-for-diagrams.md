# Decision: Mermaid in Markdown is the diagram source

Status: accepted
Owner: repository maintainer
Date: 2026-09-07

## Context

The only visuals in the kit were inside a Reveal.js deck, which GitHub shows as source. Readers on GitHub never see the lifecycle loop, the layered architecture, the responsibility boundary, the autonomy ladder, or the evaluation flywheel. The kit's contribution rules exclude binary office documents and favor text that diffs.

## Options considered

1. Export PNG or SVG diagrams from a drawing tool and commit them.
2. Write Mermaid blocks inside the Markdown pages that explain each idea.
3. Generate diagrams in a design tool and link to them externally.

## Decision

Option 2. Diagrams are Mermaid code blocks placed beside the text they explain, so a change to the idea and a change to the picture land in the same diff. GitHub renders Mermaid natively; most Markdown viewers and agent harnesses can read the source when they cannot render it.

Rules:

- Keep each diagram small enough to read on a laptop screen; split rather than crowd.
- Label edges with the decision or evidence that moves work along them, not only arrows.
- Use `flowchart` for sequence and boundaries, `stateDiagram-v2` for autonomy or gate states, and `sequenceDiagram` only when actor interaction is the point.
- Do not duplicate a diagram across pages; link to the page that owns it.
- The deck keeps its own hand-built SVG visuals; the `assets/` banner stays SVG.

## Consequences

- Visuals appear wherever the kit is read, including inside agent sessions.
- No binary assets, no export step, and diagrams are reviewable in pull requests.
- Complex illustrations that Mermaid cannot express well stay in the deck.

## Links

- [Release design](../design/2026-09-07-field-craft-and-technical-foundations.md)
- [System patterns](../../learning/system-patterns.md)
