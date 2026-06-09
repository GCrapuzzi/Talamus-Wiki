# Talamus

![license](https://img.shields.io/badge/license-Apache--2.0-blue) ![python](https://img.shields.io/badge/python-3.11%2B-blue)

**Local-first memory with time, meaning, and verifiability — for your second brain and your AI agents.**

Talamus compiles your sources (documents, notes, and agent work sessions) into
**source-grounded, cross-linked concept notes**, builds a typed **graph as an
index**, and answers questions **with citations** — all on your machine, on the
LLM engine you already use.

<!-- demo GIF goes here: talamus demo → search → read -->

> Markdown notes you can edit in Obsidian · a graph that routes retrieval ·
> provenance on every claim · usable from the CLI, the SDK, and MCP.

## Why Talamus

Most "AI memory" is either a pile of vector chunks (no structure, no provenance)
or a cloud service (your knowledge leaves your machine). Talamus is built on three
properties that, **together**, nothing else gives you:

- **TIME** — a bitemporal graph: contradictions *invalidate* old facts instead of
  deleting them, so you never lose what was true **and** you know what's true now. *(shipping — MVP: versioned history & `--as-of`)*
- **MEANING** — a typed, self-emerging **ontology** (uses / is-a / part-of /
  contrasts-with / depends-on) the LLM reasons over, not just "related pages". *(shipping — Level 1 today)*
- **VERIFIABILITY** — every note keeps its **sources**, and the original is
  preserved so you can **verify and correct against it** (`talamus verify`). *(shipping)*

Plus a wedge the others don't optimize for: **memory for agents** that need
current, cited, reasoned truth.

## Talamus vs the alternatives

|                                   | Plain RAG | llm_wiki            | Zep / mem0 | **Talamus**       |
| --------------------------------- | --------- | ------------------- | ---------- | ----------------- |
| Local-first                       | varies    | ✅                  | ❌ cloud   | ✅                |
| Human-editable notes (Obsidian)   | ❌        | ✅                  | ❌         | ✅                |
| Typed ontology for reasoning      | ❌        | ❌ statistical graph | partial    | ✅                |
| Keeps history / "truth at time T" | ❌        | ❌ overwrites        | partial    | ✅ *(MVP)*        |
| Provenance + correct-from-source  | ❌        | tracking only       | partial    | ✅                |
| Agent memory (read + write, MCP)  | ❌        | partial             | ✅         | ✅                |

## Quickstart

```bash
pipx install talamus            # or: pip install talamus

talamus demo                    # try a small example brain instantly (no LLM)
talamus search "embedding"

talamus init                    # your own brain (auto-detects your LLM engine)
talamus ingest report.pdf       # PDF / DOCX / HTML / Markdown / URL -> linked concept-notes
talamus ask "how does X work?"  # cited answer
talamus ui                      # optional native desktop app (pip install talamus[ui])
```

Run `talamus` with no arguments for a status panel, or follow the
**[10-minute quickstart](docs/quickstart.md)**.

## Choose your engine

Talamus runs on what you already have — set it in `talamus.json` or `TALAMUS_LLM_PROVIDER`:

- `claude-cli` — your Claude subscription (default if `claude` is on PATH)
- `ollama` — a local model, fully offline (`TALAMUS_LLM_MODEL=llama3`)
- `anthropic-api` — the Anthropic API (`ANTHROPIC_API_KEY`)

## For agents (MCP)

```bash
talamus mcp install             # writes .mcp.json for Claude Code / Cursor / Desktop
talamus hook                    # prints a SessionEnd hook to auto-capture your work
```

Agents `search` / `read_note` / `recall` to read the brain, and `remember` to grow
it. The graph is an **index, not the answer** — agents read the real notes and cite
them.

## Browse it like a wiki

Open `notes/` as an Obsidian vault: notes cross-link with `[[wikilinks]]`, so you
navigate the knowledge by hovering and clicking. Prefer a dedicated app?
**`talamus ui`** — a native Flet desktop/web app (`pip install talamus[ui]`) — gives you
chat, search, clickable wikilinks, and domain browsing over the same SDK (no API).

## How it works

Sources (Markdown, text, **PDF, DOCX, HTML, URLs**) are normalized and preserved; an
LLM extracts atomic **concept notes** (with sources, typed relations, and wikilinks);
Talamus builds rebuildable indexes (graph + BM25 + ontology) and a hierarchical
**domain overview**. Retrieval routes through the overview, then **reranks** a union of
graph + BM25 candidates, and fits the context to a **token budget** so answer cost stays
flat as the brain grows. Answers cite the notes they used, and `talamus eval` measures
retrieval quality (recall@k / MRR) so changes are judged by numbers, not vibes.

Storage is **hybrid**: `notes/*.md` is the human-editable view (Obsidian-compatible),
`.talamus/cache/` holds the machine truth (provenance) and the derived indexes;
`talamus reindex` folds your hand-edits back in. The core is **Python stdlib-only**;
extras (MCP, engines) are optional. See **[architecture](docs/architecture.md)**.

## Use cases

- **Second brain** — compile your reading and notes into a connected, cited wiki.
- **Agent memory** — give your agents a local, structured, verifiable memory they
  can both read and grow.

## Status & roadmap

Working **today**: the text → notes → cited-answers loop, the typed ontology (Level 1),
the **domain overview** + overview-routed retrieval, **reranking** + the `eval` harness
+ context budgets, **concept consolidation**, **source-correction** (`verify`), a
**bitemporal MVP** (`history --as-of`), **multi-format ingestion** (PDF/DOCX/HTML/URL),
a native **desktop UI** (`talamus ui`), the CLI, the engine adapters, and the MCP server.
On the **[roadmap](docs/superpowers/specs/2026-06-08-talamus-roadmap.md)**: full
valid-time bitemporal, hover-preview & graph view in the UI, OCR & more formats, and
packaged installers.

## Development

```bash
pip install -e ".[dev,mcp]"
python dev.py                    # lint + types + tests
```

## License

Apache-2.0.
