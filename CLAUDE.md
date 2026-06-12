# Claude Code Workspace Instructions

This repository is Talamus: an open-source, local-first knowledge compiler
with time, meaning and verifiability — for humans and AI agents.

The single entry point for every agent is:

```text
AGENTS.md
```

Read it first: it gives the reading order for the developer canon in `dev/`
(CONSTRAINTS → ARCHITECTURE → STATE → PRODUCT), the binding rules, the known
traps, and the documentation governance.

Operational expectations:

- Work against `src/talamus/` and `tests/test_talamus_*.py`.
- The quality gate is `python dev.py` — ALL GREEN before any commit.
- Use `talamus` as the CLI name.
- Treat the graph and every index as derived, never source truth.
- Do not commit `.claude/` or generated caches.
