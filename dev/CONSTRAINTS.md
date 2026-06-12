# Constraints — the binding rules and WHY they exist

Every rule here is binding for any agent or contributor. Each one states its
reason and what enforces it. Changing anything in this file requires the
maintainer's (Giovanni's) explicit approval — see the governance section in
[AGENTS.md](../AGENTS.md).

## 1. No embeddings

The revolutionary thesis: **anyone — including non-technical users — gets
personal + agentic memory with only a ~€20/month coding-agent subscription, or
zero subscriptions via a local model.** No GPU, no embedding infra, no
pay-per-call API requirement, no external services. Semantic power is bought
differently: at INGEST time, written into the notes by the user's own LLM
(canonical aliases, bilingual retrieval text, symptom phrasings), and at ASK
time by LLM query expansion. Embeddings may one day exist as a strictly
OPTIONAL extra — only after the by-construction route has given everything.
*Enforced by:* code review; no vector/embedding dependency may enter `core`.

## 2. OS-agnostic and LLM-agnostic, development to product

Contributors may run Linux, macOS or Windows; users may bring ANY engine
(Claude, Codex, Gemini CLIs, ollama local models, an API key). Nothing in the
product or the dev workflow may require a specific OS or a specific model.
Cheap/weak models are first-class citizens: every spot that consumes LLM output
must degrade gracefully on truncated/malformed/empty/prose-wrapped answers.
*Enforced by:* multi-OS CI; `tests/test_talamus_hostile_models.py`; the engine
adapter layer (`adapters/llm.py`).

## 3. Python stdlib core; extras optional

The core runs on the standard library. Optional features live behind extras
(`ui`, `mcp`, `pdf`, `bench`). A user who pip-installs the bare package gets a
fully working brain.
*Enforced by:* import discipline; release checklist (clean-venv install).

## 4. Markdown notes are the human truth; everything else is derived

`notes/*.md` is what the user owns and edits (Obsidian-compatible).
`.talamus/cache/notes/*.json` is the machine truth (provenance, relations,
retrieval text, confidence). Graph, search indexes, overview, federated index
are **derived indexes — never source truth** — and must always be rebuildable
with `talamus reindex`.
*Enforced by:* `reindex` round-trip tests; CACHE_VERSION migrations.

## 5. Answers always read real notes, with citations

`ask` answers only from real note content placed in context, cites `[n]` with
a sources legend, answers in the question's language, and says honestly when
the context is not enough — never invents.
*Enforced by:* the answer prompt contract + e2e tests.

## 6. No costly LLM run without estimate + consent

Any multi-call operation (big-document ingest, enrich, scan) first prints a
dry-run estimate (calls, tokens) and runs only with explicit `--yes`.
*Enforced by:* CLI consent gates + tests asserting zero calls without consent.

## 7. Provenance, history, sources — always preserved

Every note carries source refs (file, locator, content hash). Corrections are
PROPOSED to the review queue, never silently applied. The temporal model
invalidates, never deletes (bitemporal: transaction time + valid time).
*Enforced by:* review-queue tests; history/claims append-only stores.

## 8. The emergent ontology is THE differentiator

Relation types are induced from evidence, named by the LLM in English,
versioned in a schema, and promoted only by measured rules (support ≥ 8 across
≥ 3 distinct notes). Promotion changes runtime behavior (edge re-typing,
typed-first context expansion). Its measured retrieval value is in STRUCTURE
(domain clustering → hierarchical routing → navigation), NOT in scoring —
three experiments confirmed this (propagation, 1-hop expansion swap,
triangulation). Do not re-add ontology boosts to ranking without new data.
*Enforced by:* promotion-rule tests; the rejected-experiments record in
[STATE.md](STATE.md).

## 9. Three-layer language architecture

(1) All prompts are ENGLISH (cheap models follow English best) with an output
language directive. (2) Note prose is in the USER'S language (config
`language`, locale fallback). (3) The machine layer is English-canonical:
every note carries an English canonical alias, bilingual retrieval text, and
ENGLISH relation verbs — cross-language search and a consistent ontology by
construction.
*Enforced by:* `tests/test_talamus_language.py`.

## 10. Science before features: the two-corpora law

No retrieval/quality change ships unless it WINS measured ablations on BOTH
real corpora (the docs corpus, 120 cases, in CI; plus a real local corpus —
currently a 500-page book brain). Error analysis → hypothesis → ablation →
only winners ship → regression floor in CI. Negative results are documented so
nobody re-runs dead experiments. The test corpus is a bench, not the product:
never optimize for one brain.
*Enforced by:* `retrieval_lab.py` + `tests/test_talamus_recall_floor.py` +
the research logs in [research/](research/).

## 11. Every change passes the gate

`python dev.py` = ruff check + ruff format + mypy + full unittest. ALL GREEN
or it does not ship. Public-behavior changes update docs/CLI/SDK/MCP in the
same change.
*Enforced by:* CI on every push, multi-OS.

## 12. Workflow

One commit per milestone/block with measured numbers in the message; the final
merge decision is the maintainer's. Never commit `.claude/`, generated caches,
or any content derived from copyrighted sources (e.g. book eval-sets stay
local).
*Enforced by:* `.gitignore` + review.
