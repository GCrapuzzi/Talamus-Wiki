# v1 launch — messaging & the 60-second demo

**The word we own:** *"the memory your agent already has."*
Not a wiki with an MCP bolted on; not a vector DB with a chat UI. The single
local brain the human and the agent use natively, together.

## The one-liner (README, PyPI, post titles)

> Talamus — the local-first memory your agent already has. Shared with you,
> in your language, token-cheap, zero extra setup. €0, no cloud, no embeddings.

## The four claims (each one measured, never oversell)

| Claim | Evidence |
|---|---|
| **Shared** — one brain, two consumers | MCP 8 read + 6 write tools; session-capture hook; the human edits the same `notes/*.md` in Obsidian |
| **In your language** — cross-language by construction | book corpus (IT queries over EN sources): ask hit@8 0.972; three-layer language architecture |
| **Cheap** — doesn't burn your subscription | per-task tiering (bulk = cheap model, answers = strong); token recall −97.7% vs load-all; routing ~log(N) |
| **Zero setup** — nothing beyond the agent/PC you have | `pipx install talamus && talamus setup` → cited answer in ~3 min (re-verified live 2026-07-02); no API key, no cloud, no embedding infra |

## The 60-second terminal demo (record as-is)

```bash
pipx install talamus

talamus setup                    # detects your CLI (claude/codex/gemini/ollama), MCP, hook
talamus scan . --yes             # your repo becomes a brain (secrets redacted, cost shown first)
talamus ask "come funziona l'autenticazione qui?"   # cited answer, IN YOUR LANGUAGE

talamus import-vault ~/vault     # coming from Obsidian/Notion? 1:1, zero LLM cost
talamus ui                       # the living graph of everything you know
```

Beats to hit on camera: (1) the cost preview BEFORE any LLM call, (2) the
citations + Sources legend, (3) the Italian question over English sources,
(4) the graph appearing in the workbench.

## Channel copy (short forms)

- **HN (Show HN):** "Show HN: Talamus — local-first memory for you AND your
  coding agent (no embeddings, no cloud, €0)". First comment: the honest
  benchmark table (incl. where we lose: monolingual nDCG vs a strong dense
  model) — honesty is the differentiator in that room.
- **r/LocalLLaMA:** lead with the fully-local path (ollama gemma e2e, measured
  0.800 correctness, €0) and the token-cheapness.
- **X/Twitter:** the 60-second demo video + "your agent remembers now".

## Anti-overclaim rules (binding)

- Never say "beats embeddings" — say: ties dense on SciFact with zero infra;
  wins hit-rate cross-language; loses monolingual nDCG to multilingual-e5 (RS7).
- Never imply Cursor is an engine (it consumes Talamus via MCP).
- Every number in public copy must exist in STATE.md or benchmarks/results/.
