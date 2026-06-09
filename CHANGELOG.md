# Changelog

All notable changes to Talamus are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/), and the project aims to follow
semantic versioning once it reaches a public release.

## [Unreleased]

Pre-release. The project was renamed **Kortex → Talamus**.

### Added

- **CLI**: no-arg status panel, `quickstart`, smart `init` (engine auto-detect,
  `--engine`), enhanced `doctor` (engine/cache/notes), `--json` on read commands,
  global+project brain **scoping** (`--root` / `--brain` / `--global`, `TALAMUS_HOME`),
  `brains`, `where`, `export`/`import`, shell `completion`, and `demo`
  (an instant, LLM-free example brain).
- **Engines**: pluggable LLM adapters via a `build_provider` factory — `claude-cli`,
  local **Ollama**, and the **Anthropic API**; selected from config (`llm_provider`,
  `llm_model`). The CLI and MCP server build the engine from config.
- **Onboarding**: `talamus mcp install` (writes `.mcp.json`) and `talamus hook` /
  `hook-run` (a robust Claude Code capture hook). 10-minute quickstart.
- **Quality**: `ruff` + `mypy` + a `dev.py` runner, multi-OS CI, an exception
  hierarchy with actionable messages, logging, config validation, **normalized
  source files written to disk**, cache schema versioning, and a benchmark harness.
- **Docs**: a 10k-star README, internal architecture doc, a security policy, and
  this docs site.
- **Retrieval & meaning**: a hierarchical **domain overview** (`talamus overview`,
  hybrid graph-clusters + LLM naming) with overview-routed `ask`; deterministic
  **reranking** (`rank.py`: graph + BM25 union with an exact-name boost — no more
  funnel); a **context token budget** (`budget.py`) for flat answer cost; an
  **evaluation harness** (`talamus eval`, recall@k / precision@k / MRR); a light
  Italian stemmer and last-resort query expansion; **concept consolidation**
  (`talamus consolidate`).
- **Time & verifiability**: a **bitemporal MVP** — `talamus history [--as-of]`,
  invalidate-not-delete versioning; **source-correction** (`talamus verify [--apply]`)
  against the preserved original; typed-relation listing/pruning (`talamus relations`).
- **Ingestion**: multi-format `talamus ingest` for files, folders (recursive,
  incremental), and URLs — Markdown/text, **PDF** (`pdf` extra), **DOCX** and **HTML**
  (stdlib), with content-hash skip of unchanged sources.
- **Interfaces**: a native **Flet desktop/web UI** (`talamus ui`, `ui` extra) — chat,
  search, note view with clickable wikilinks, and domain browsing, calling the SDK
  directly (no API); the MCP server gains an **`overview`** tool (cached domain map,
  no LLM cost).
- **Polish**: `talamus --version`; `--limit` on `search`/`recall`; **PEP 561**
  `py.typed` so SDK consumers get type hints; folder ingest now **reports failed files**
  instead of dropping them silently; clear messages when the engine returns empty output;
  the UI surfaces engine errors instead of hanging, and renders wikilinks with spaces.

### Changed

- Package `kortex` → `talamus`; CLI `kortex` → `talamus`; config `kortex.json` →
  `talamus.json`; cache `.kortex/` → `.talamus/`; env `KORTEX_*` → `TALAMUS_*`.
