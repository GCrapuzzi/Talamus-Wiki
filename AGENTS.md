# Codex Workspace Instructions

This workspace is being converted into an open-source, local-first knowledge
compiler with graph-first retrieval.

Before modifying product architecture, retrieval behavior, generated knowledge
storage, or agent-facing protocol, read:

```text
AI Space/system/AGENT_PROTOCOL.md
```

Current implementation plan:

```text
docs/superpowers/plans/2026-05-27-core-graph-first-foundation.md
```

Current product design:

```text
docs/superpowers/specs/2026-05-27-local-first-knowledge-pipeline-v1-design.md
```

Important workspace state:

- `FDE Brain/` is a legacy Obsidian vault kept only as local workspace scaffolding.
- Existing generated Markdown knowledge in `FDE Brain/` is disposable and has been removed from the active project.
- New product work must target the generic `brain` package and default `knowledge/*` project layout.
- `AI Space/` contains legacy sources, logs, experiments, and protocol files; do not treat it as the future product layout.
- Do not commit `.claude/`, `FDE Brain/.obsidian/workspace.json`, or `FDE Brain/.obsidian/graph.json`.
