# Talamus — Internal Architecture

A map of the modules and the data flow, so a new contributor (or agent) can find
their way without reading everything. Core is **Python stdlib-only**; optional
features (MCP, OCR) live behind extras and adapters.

## Storage model (hybrid)

- `notes/*.md` — the **human-editable view** (Obsidian-compatible), each carries a stable `id` in frontmatter.
- `.talamus/cache/notes/<id>.json` — the **machine truth** (provenance, relations, confidence).
- `.talamus/{raw,normalized}/` — the preserved **sources** (raw copy + normalized view).
- `.talamus/cache/{graph,bm25,ontology}.json` + `manifest.json` — **derived indexes**, always rebuildable.
- `talamus reindex` re-reads the Markdown for human fields and merges, preserving machine fields.

## Modules (`src/talamus/`)

| Module | Responsibility |
|---|---|
| `paths.py` | `TalamusPaths`: every filesystem location. |
| `config.py` | `TalamusConfig`: provider selection; load/save/validate/env-override. |
| `errors.py` | Exception hierarchy (`TalamusError` + actionable subclasses). |
| `log.py` | Quiet-by-default logging (`--verbose` / `TALAMUS_LOG`). |
| `adapters/llm.py` | `LLMProvider` protocol + `ClaudeCliProvider`. The pluggable engine. |
| `normalize.py` | Raw text → `NormalizedPackage` (sections). |
| `session.py` | Agent transcript+diff → `NormalizedPackage` (capture); compaction + worth-remembering gate. |
| `extract.py` | `NormalizedPackage` + LLM → `CanonicalNote[]` (the "librarian" prompt). |
| `models.py` | `CanonicalNote`, `SourceRef` (provenance), `Relation`, `ProposedLink`. |
| `linking.py` | `NoteRegistry` — resolve wikilinks within a batch. |
| `naming.py` | `note_slug` / `note_filename` — cross-OS-safe names. |
| `storage/obsidian.py` | Render a note to Markdown with `[[wikilinks]]`. |
| `noteparse.py` | Parse Markdown back to human fields (for `reindex`). |
| `store.py` | Cache write + `merge_notes`, `load_notes`, `rebuild_indexes`, `reindex`, cache versioning. |
| `graph.py` | `build_graph` + `query_graph` (term overlap) — the retrieval index. |
| `ontology.py` | Typed relations (`normalize_relation`), `build_ontology`, `neighbors`. |
| `search.py` | `BM25Index` — lexical fallback. |
| `ask.py` | `build_context_bundle` (graph-first → ontology expand → BM25 fallback) + `answer_question` (cited). |
| `recall.py` | Read SDK: `search_notes`, `read_note_text`, `recall_context`, `concept_neighbors`. |
| `ingest.py` | Write SDK: `_compile_package` (shared), `ingest_file`, `remember_session`, `ingest_text`. |
| `cli.py` | The `talamus` CLI (thin shell over the SDK). |
| `mcp_server.py` | Optional MCP server (read tools + `remember`). |

## Data flow

**Write (ingest):**

```
source ─▶ normalize_text / normalize_session ─▶ NormalizedPackage
        ─▶ write .talamus/normalized/<name>.md
        ─▶ extract_notes (LLM) ─▶ CanonicalNote[]
        ─▶ write_note_json (cache truth, merge same-id)
        ─▶ render_note_markdown (notes/*.md, wikilinks resolved batch-wide)
        ─▶ rebuild_indexes (graph + ontology + bm25 + manifest)
```

**Read (recall / ask):**

```
question ─▶ build_context_bundle
              ├─ query_graph (term overlap on the graph)
              ├─ ontology expand (1 hop via typed relations)
              └─ BM25 fallback
         ─▶ answer_question (LLM composes a cited answer)
```

Surfaces (CLI, MCP, future UI) are **thin shells** over the SDK. The engine
(`LLMProvider`) is injected, so the same flow runs on any backend.

## Principles

Local-first · the LLM reasons and chooses · the graph is an **index**, not the
truth · stdlib core + optional adapters · see `docs/superpowers/specs/` for the
vision and the execution roadmap.
