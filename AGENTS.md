<!-- ai-dlc:begin bb71619f3258f6be8585981dd41c0aec6182966702d03088a0b8cd2bbc5a9983 -->
# Shared project guidance

Read ai-dlc.toml and the active .ai-dlc/work record before work.
Use specification artifacts for implementation tasks and the tracker for priority/status.
Finalize required specifications before review. Complete work through ai-dlc work finish.
Store architecture, design, decisions and runbooks in docs/. Keep personal notes in knowledge.

## Verification

- generated: `ai-dlc agents render --check`
- links: `python3 scripts/check_links.py`
- schemas: `python3 scripts/check_schemas.py`
- whitespace: `python3 scripts/check_whitespace.py`

Run `ai-dlc project check --required` in the prepared project environment.

## Selected providers and tools

Read the linked instructions for each configured provider before using its tools.
Modules name installation requirements; their presence does not establish account
access or platform qualification. Run `ai-dlc project readiness --root .` for
offline requirements and use doctor for explicit provider health inspection.

- scm: github; unsupported: no component for provider: github
<!-- ai-dlc:end -->
