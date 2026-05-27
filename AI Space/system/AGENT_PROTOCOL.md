# Agent Protocol

This workspace is no longer treated as a personal `FDE Brain` knowledge vault.
It is now the development workspace for an open-source, local-first knowledge
compiler.

## Current Direction

- Product target: generic `brain` CLI and Python package.
- Default project layout: `knowledge/raw`, `knowledge/normalized`,
  `knowledge/notes`, `knowledge/graph`, `knowledge/index`, `knowledge/logs`,
  `knowledge/review`, and `knowledge/failed`.
- Obsidian is the first storage adapter, not the permanent product boundary.
- Graphify is not part of the core architecture.
- The deterministic graph is an index and routing layer, not source truth.
- Answers must be grounded in real Markdown notes or normalized source files,
  with citations.

## Active Plan

Use this plan as the implementation source of truth:

```text
docs/superpowers/plans/2026-05-27-core-graph-first-foundation.md
```

That plan intentionally builds the core graph-first foundation only:

- Apache-2.0 package foundation
- generic `src/brain/` package
- beginner CLI commands
- canonical note/source models
- Obsidian renderer
- same-batch wikilink resolution
- deterministic graph builder
- built-in BM25 fallback
- graph-first `ask context`
- agent skill and tool-calling docs

Do not add Docling/OCR conversion, LLM extraction, ingestion scheduling, or UI
inside this foundation pass.

## Legacy Workspace Areas

- `FDE Brain/` is a legacy Obsidian vault scaffold. Existing generated Markdown
  notes in that folder are not important and should not be preserved.
- `FDE Brain/.obsidian/` is local UI state. Do not commit its `workspace.json`
  or `graph.json`.
- `AI Space/` contains legacy operating data from the earlier personal wiki
  prototype. It may be useful as reference, but it is not the new product
  layout.
- `tools/fde_brain/` is legacy implementation. Leave it intact unless a plan
  explicitly migrates or removes it.

## Retrieval Rule

For the new product, retrieval is graph-first:

1. Use the deterministic graph to route a question to candidate notes or source
   sections.
2. Read the real Markdown note or normalized source files.
3. Use BM25 only when graph routing is insufficient or empty.
4. Follow validated wikilinks when they add necessary context.
5. Cite the real files, not graph metadata.

## Git Safety

- Keep commits focused.
- Do not stage `.claude/`.
- Do not stage `FDE Brain/.obsidian/workspace.json`.
- Do not stage `FDE Brain/.obsidian/graph.json`.
- Do not include unrelated legacy graph output such as
  `AI Space/graph/brain/graphify-out/` unless a plan explicitly says so.
- Raw source originals should not be permanently deleted unless the user
  explicitly asks for that exact deletion.
