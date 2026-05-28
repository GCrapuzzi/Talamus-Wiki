# Codex Workspace Instructions

This repository is Kortex: an open-source, local-first knowledge compiler with
graph-first retrieval.

Before modifying product architecture, retrieval behavior, generated knowledge
storage, or agent-facing protocol, read:

```text
docs/superpowers/specs/2026-05-27-local-first-knowledge-pipeline-v1-design.md
docs/superpowers/specs/2026-05-28-kortex-repository-cleanup-design.md
```

Current implementation focus:

```text
docs/superpowers/plans/2026-05-28-kortex-repository-cleanup.md
```

Rules:

- Product code lives under `src/kortex/`.
- Tests for active product code are named `tests/test_kortex_*.py`.
- The CLI command is `kortex`.
- The default config file is `kortex.json`.
- The graph is an index and routing layer, not source truth.
- Answers must be grounded in real Markdown notes or normalized source files.
- Do not commit `.claude/` or generated caches.
