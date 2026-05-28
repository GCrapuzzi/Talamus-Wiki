# Claude Code Workspace Instructions

This repository is Kortex: an open-source, local-first knowledge compiler with
graph-first retrieval.

Use the same development protocol as Codex:

```text
AGENTS.md
```

Operational expectations:

- Work against `src/kortex/` and `tests/test_kortex_*.py`.
- Use `kortex` as the CLI name.
- Treat the graph as an index, not source truth.
- Do not reintroduce legacy personal-workspace folders.
- Do not commit `.claude/` or generated caches.
