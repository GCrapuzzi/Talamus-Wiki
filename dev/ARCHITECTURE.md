# Architecture — how every part of Talamus works

The engineering map: what each module does, how data flows, and where to look.
File references are relative to `src/talamus/`. Update this document in the
same change that alters public behavior (see governance in
[AGENTS.md](../AGENTS.md)).

## Anatomy of a brain on disk

```
<brain root>/
  talamus.json            ← config: llm_provider, llm_model, language, providers
  notes/*.md              ← HUMAN TRUTH: Obsidian-compatible notes, frontmatter
                            (id, title, aliases, tags, confidence, sources)
  .talamus/
    raw/                  ← preserved source copies (files, URL dumps, chunks)
    normalized/           ← sectioned normalized view (provenance anchors)
    cache/
      notes/*.json        ← MACHINE TRUTH: full CanonicalNote (relations,
                            retrieval_text, proposed_links, sources, history ptr)
      index.sqlite        ← persistent search index (FTS5) — derived
      postings.json       ← fallback search index — derived
      graph.json          ← note/source graph — derived
      ontology.json       ← typed edges + concepts — derived
      overview.json       ← domains (id, name, description, members) — derived
      overview-tree.json  ← macro-areas over domains — derived
      schema.json         ← ontology schema (versioned, candidate/active)
      claims.jsonl        ← valid-time facts, append-only
      history/            ← note versions, append-only
      jobs/               ← resumable job records + logs
      ingested.json       ← content hashes for incremental ingest
    logs/capture.log      ← agent-capture audit trail
```

Hybrid truth model: Markdown = human-editable truth for prose fields;
cache JSON = machine truth for provenance/relations/retrieval. `reindex`
re-reads Markdown, merges human edits into machine records, rebuilds every
derived index. CACHE_VERSION (in `paths.py`) bumps force a reindex migration.

## Data model (`models.py`)

`CanonicalNote`: note_id, title, aliases, folder, tags, summary,
retrieval_text, body_sections (fixed structural keys: definizione,
funzionamento, quando, esempio, relazioni — identifiers, not display text),
proposed_links (anchor→target), relations (source, relation, target,
confidence), sources (`SourceRef`: raw_path, normalized_path#section, locator,
source_hash over extracted TEXT, supported_claims), confidence, timestamps.

## Ingest pipeline (`ingest.py`, `sources.py`, `normalize.py`, `extract.py`)

1. `extract_text` dispatches on suffix: pdf (pypdf, optional extra), docx
   (stdlib zip+xml), html (stdlib strip), md/txt. URLs via `read_url`.
2. Incremental: content hash in `ingested.json` skips unchanged files.
3. **Chunking** (`split_chunks`, CHUNK_CHARS=20k): deterministic paragraph
   split. >1 chunk → `ingest_large`: a resumable JOB, one extraction call per
   chunk, progress persisted after each, engine failures PAUSE (resumable),
   single bad chunks retried once then recorded without aborting. Chunk files
   are always `.md` (extracted text). One reindex at job end (crash-safe).
   CLI consent gate: estimate printed, runs only with `--yes`.
4. `normalize_text` → sections with stable ids (provenance anchors);
   `source_hash` = sha256 of the extracted text (NOT file bytes — Windows
   newlines and binary formats would break comparison).
5. `extract_notes` (`extract.py`): ONE English prompt with output-language
   directive. The model returns a JSON array of notes; parser takes first
   `[`..last `]`, `json.loads(strict=False)` (tolerates literal control chars
   from cheap models). Notes must carry: English canonical alias, bilingual
   retrieval_text + SYMPTOM phrasings come later via enrich, English relation
   verbs.
6. `_compile_package`: phase 1 writes all note JSONs (merge on same id —
   `merge_notes` unions aliases/tags/relations/sources/retrieval_text, keeps
   higher-confidence prose); phase 2 renders Markdown with a whole-batch
   registry so same-batch wikilinks resolve (self-links dropped); then
   `rebuild_indexes`.

Also: `ingest_dir` (recursive, failures recorded), `ingest_url`,
`ingest_text` (agent insights, scan digests), `remember_session` (transcript+
diff behind a worth-remembering gate, audited in capture.log).

## Retrieval (`indexes.py`, `textutil.py`)

Three blended channels, **no embeddings** (RS1 research):

```
score = lexical_bm25 + 0.7 · trigram(title+aliases) + 0.3 · trigram(summary)
```

- Lexical: bilingual light stemmer (`textutil.tokens` — IT pass, EN suffix
  pass, IT pass), field-weighted haystack (title ×3, aliases ×2, tags,
  retrieval_text, summary). BM25.
- Trigram channels: character 3-grams — the **cognate bridge**
  (architettur*ali*/architectur*e*) that buys cross-language recall without
  embeddings.
- Backends: sqlite FTS5 (4 columns, per-column bm25 weights) preferred;
  deterministic JSON postings fallback; legacy in-memory path. Channels
  normalized per query then weighted-summed (`_blend`).
- `search_index(paths, query, limit)` → [{note_id, title, summary, aliases,
  score}].

Cross-language search works BY CONSTRUCTION: English canonical aliases and
bilingual retrieval_text are written at ingest, symptom phrasings via enrich.

## Ask path (`ask.py`) — the user-facing pipeline

```
question
  → routing (LLM): macro-areas (if tree exists) → domains, by stable id,
    validated against the map; name-substring fallback for legacy overviews
  → LLM query EXPANSION (the user's LLM acts as the embedding model:
    translates phrasing into corpus vocabulary; +1 call)
  → selection (_select_bundle_titles, deterministic): chosen domains'
    members ranked against question+expansion via the persistent index,
    plus GLOBAL_ESCAPE_SEEDS=2 top global hits outside the chosen domains
    (escape hatch for routing mistakes)
  → budget (fit_to_budget, TALAMUS_CONTEXT_BUDGET)
  → answer (LLM): only from context, cites [n], answers in the question's
    language, refuses honestly when context is insufficient; Fonti legend
```

No overview → index path: persistent-index seeds + 1-hop typed-first ontology
expansion (active only when seeds < limit); still nothing → LLM query
expansion retry. `--as-of` reads historical versions; `--trace` returns the
full route (areas, domains, expansion, items_read, tokens). Federated extras
(`[central]` items) are appended by the CLI layer per scope policy.

Measured (book corpus): hit@8 0.972. History: list-order selection was 0.361
— ranking + expansion are what fixed it; details in STATE.md.

## Ontology (`ontology.py`, `ontology_lab.py`, `relations.py`)

- `build_ontology`: edges from note relations (normalized surfaces) +
  proposed_links (type "related"); rebuilt at every reindex with
  `active_surface_map` so **promotions re-type edges globally**.
- Ontology Lab: evidence layer → deterministic clustering of unexplained
  surfaces → ONE LLM naming call (English definitions) → versioned schema
  (candidate/active/deprecated, full history) → promotion only by rule:
  support ≥ 8 across ≥ 3 distinct notes (`--force` to override, logged).
- Runtime effect: typed edges first in context expansion and in the UI graph;
  domain clustering runs on the ontology edges.
- Measured role: STRUCTURE (clustering, routing, navigation) — scoring boosts
  rejected three times with data (see STATE.md).

## Domains & hierarchical overview (`domains.py`)

- `_structural_clusters`: union-find over ontology edges.
- ≤60 notes: single full-partition naming call. >60 notes: **batched
  induction** (single-prompt collapses at scale — found on the 243-note book):
  giant clusters (≥25) get a dedicated split call; mid clusters named in one
  call echoing only a numeric index (first title as deterministic fallback);
  strays assigned in batches of 40 against the named domains. A malformed
  answer hurts only its slice.
- Domains get stable ids (`dom-*`); ≥12 domains → `build_overview_tree`
  groups them into macro-areas (`area-*`): routing cost ~log(N).

## Temporal (`temporal.py`, `timeline.py`)

- Transaction time: note versions in append-only history; `note_as_of`.
- Valid time: claims.jsonl, append-only; `record_claim` / `invalidate_claim`
  (corrections close the old claim and open the new — never delete);
  `claims_as_of`, `note_timeline`. `parse_when`: partial dates mean END of
  period; naive datetimes warn and use local tz.

## Verification (`correct.py`)

- `provenance_status` (no LLM): resolves the RAW source first (hash was
  computed on extracted text; re-extracts to compare — never file bytes),
  normalized view proves existence only; flags source_missing /
  source_changed / low_confidence.
- `verify_batch`: stale → review items without LLM; checked notes → LLM
  compares against source; mismatches become PROPOSED corrections in the
  review queue. `review apply` writes them with history preserved.

## Curation

- **`enrich.py`**: symptom-vocabulary enrichment — batches of 20, English
  prompt echoing note ids, idempotent (marker in retrieval_text), guard-rails
  for weak models (400-char cap, structural filter), estimate + `--yes`,
  one reindex at end. Uses `overwrite_note_json` (write_note_json MERGES and
  would keep the old text).
- **`consolidate.py`**: duplicate detection (one call, balanced-object salvage
  parser for truncated answers) → groups PROPOSED; `apply_consolidation`
  accepts REVIEWED groups (the model lumps related-but-distinct concepts);
  merge unions retrieval_text and accumulates provenance.

## Jobs (`jobs.py`)

Persistent records under cache/jobs, created BEFORE the first expensive call.
States: queued→running→completed/failed/cancelled (+paused). `run_items`:
done-set persisted per item, cooperative cancel between items, failures leave
a resumable record, stale 'running' records (hard kill) are adopted on resume.
Runners registered in `cli.JOB_RUNNERS` (scan, ingest).

## Multi-brain (`registry.py`, `scope.py`, `federation.py`)

Registry at TALAMUS_HOME/registry.json. Scope policies: project-only /
central-only / project+central (default) / all. Federation = pointer index
(derived); central reads federate into search/ask (`[central]` markers),
writes stay local unless `--all-brains`; `brains promote` moves a note to
central. `talamus brains list/use/info/rename/delete/register/index`.

## Engines (`adapters/llm.py`)

`LLMProvider` protocol = `complete(prompt) -> str`. Adapters: claude-cli
(`claude -p`), codex-cli (`codex exec` — an AGENT, pinned read-only sandbox,
prompt on stdin), gemini-cli (headless `-p ""` + stdin — also an agent:
`--approval-mode plan` read-only + `--skip-trust`), ollama (`ollama run`),
anthropic-api (key from env or TALAMUS_HOME/credentials.json; env wins).
Optional model passthrough via config `llm_model` → `-m`. Executables resolved
with `shutil.which` (Windows shims). All model JSON is parsed defensively
(strict=False, balanced-object salvage, batch isolation) — enforced by the
hostile-model CI battery.

`services/engines.py` is the shared UI/CLI/SDK setup slice over this adapter
metadata: it lists canonical engine ids and readiness statuses, chooses the
default installed CLI engine with the `claude-cli` fallback, loads/updates only
`llm_provider`, `llm_model` and `language` in `talamus.json`, and saves the
Anthropic API key through the existing machine credential store without
returning the secret. Mutating service calls return `ServiceResult` from
`services/result.py` (`success`, `message`, optional `code`, optional `data`).

## Interfaces

The front ends (CLI, MCP, UI, SDK) route through `services/`: typed
`ServiceResult` contracts are the one seam between the core and every interface,
so behaviour stays identical across them. CLI and MCP are fully on the seam; the
UI is mid-migration onto it.

- **Shared services** (`services/`): UI/CLI/SDK-neutral contracts and probes.
  `readiness.py` reports brain/engine/cache/job state for dashboards; the
  engine setup slice handles settings parity without duplicating adapter logic;
  `ingestion.py` exposes typed ingest preview/confirmation/run operations over
  `estimate_chunks` and `ingest_path`, preserving the no-LLM-call consent gate
  for large local files; `scan.py` exposes typed repository scan preview,
  confirmation, secret-blocking, background queueing, and execution over the
  existing dry-run/JobStore/execute_plan flow without constructing an LLM
  provider before approval; `enrich.py` exposes typed symptom-vocabulary
  preview/confirmation/run operations over the existing batched enrichment path;
  `consolidation.py` exposes typed duplicate-group proposals and reviewed-group
  apply operations over the existing consolidation merge path; `verification.py`
  exposes typed batch provenance/content verification, single-note verification,
  and explicit correction application over the existing correction path;
  `brains.py` wraps registry list/register/select/rename/delete/flag operations
  in typed `ServiceResult` contracts for CLI/UI parity; `jobs.py` exposes
  read/cancel/log controls over persisted job records while execution resume
  stays with CLI runners; `review.py` exposes review queue list/show/apply/reject
  decisions, including correction application, behind the same service contract;
  `query.py` exposes read-side search/read/recall without introducing new LLM
  calls; `graph.py` exposes typed graph-cache snapshots and ontology neighbors
  for CLI/UI graph navigation while keeping rendering and physics inside the UI;
  `diagnostics.py` exposes doctor-style config/layout/engine/cache/index/overview
  checks as typed warnings/errors for onboarding, settings, and CLI reuse;
  `library.py` exposes read-only note lists and note detail metadata/markdown for
  library, inspector, and provenance-oriented UI surfaces; `integrations.py`
  exposes MCP config status/install and capture-hook snippets for UI settings
  and CLI reuse; `backup.py` exposes export/import archive operations with
  explicit path-traversal rejection for UI/CLI portability flows; `ontology.py`
  exposes typed status/candidate review/apply/reject/deprecate/history/export
  operations while LLM-backed induction and eval remain separate contracts.
- **CLI** (`cli/` package — `app.py` dispatch + `parser.py` + command groups
  `dashboard`/`lifecycle`/`pipeline`/`query`/`groups` over `_common.py`): the
  full surface; bare `talamus` = dashboard; `--json` on read commands;
  `--root`/scope flags; consent gates.
- **MCP** (`mcp_server.py`, optional extra): read tools (search, read_note,
  recall, neighbors, overview, history, sources, ontology_status) + write
  tools (remember, ingest_text with scope, propose_note → review,
  review_list/apply/reject), all routed through `services/`. Local stdio;
  optional localhost HTTP.
- **SDK** (`recall.py`): read-side functions for embedding in agent code.
- **Web workbench** (`webapi/`, optional `ui` extra): FastAPI + React/Vite static
  workbench launched by `talamus ui`; `ui/physics.py` remains as the pure
  server-side force layout used by `webapi/graph_layout.py`.
- **Hook** (`scripts/talamus-session-hook.py`): session capture on agent
  session end.

## Research instrumentation (`retrieval_lab.py`, `eval.py`, `corpus.py`, `bench.py`)

- `eval.py`: recall@k / precision / MRR / hit-rate / negative rejection over a
  pluggable retriever; cases from JSON; category breakdown. CLI `talamus eval`.
- `retrieval_lab.py`: in-memory ablation variants (tokenizers, channels,
  weights, bundle selection, rejection analysis) — hypotheses run here first;
  only two-corpora winners ship.
- `corpus.py`: deterministic corpora (docs corpus = this repo's docs).
- Floors in CI lock past wins (`test_talamus_recall_floor.py`).

## The gate

`python dev.py` = ruff check + ruff format --check + mypy + unittest discover.
Cross-platform (pure Python). CI runs it on Linux/macOS/Windows.
