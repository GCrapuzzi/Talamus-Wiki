# Agent Workspace Instructions

This repository is Talamus: an open-source, local-first knowledge compiler with
graph-first retrieval, for humans and AI agents.

The source of truth for product direction is the PRD:

```text
docs/superpowers/specs/2026-06-10-talamus-final-product-prd.md
```

Background architecture (read before changing retrieval, storage or protocols):

```text
docs/superpowers/specs/2026-05-27-local-first-knowledge-pipeline-v1-design.md
docs/superpowers/specs/2026-06-08-talamus-roadmap.md
docs/research/2026-06-ontology-learning-review.md
```

Rules:

- Product code lives under `src/talamus/`; tests are `tests/test_talamus_*.py`.
- The CLI command is `talamus`; the config file is `talamus.json`.
- The quality gate is `python dev.py` (ruff + mypy + unittest); it must be green
  before any commit.
- The graph, the persistent indexes and the federated index are **indexes and
  routing layers, never source truth**: answers must read real Markdown notes or
  normalized source files.
- Notes never move: temporality (valid-time claims), invalidations and the
  emergent ontology schema live in overlays under `.talamus/cache/`.
- The core stays Python stdlib-only; UI/MCP/PDF/bench/docs are optional extras.
- No expensive scans or bulk LLM calls without a dry-run, an estimate and
  explicit consent (`talamus scan` is the model).
- Provenance is mandatory: every important claim points to a source + locator.
- Tests must stay hermetic: `tests/__init__.py` redirects `TALAMUS_HOME` to a
  throwaway directory — never weaken that.
- Do not commit `.claude/`, generated caches, or anything under `.talamus/`.
