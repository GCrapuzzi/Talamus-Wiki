# Multi-brain: project brains + a federated central hub

Talamus uses the **"Federated Hub with Project-Local Ownership"** model: every
project owns its brain; your personal **central** brain can *read across* all the
registered brains, without absorbing them.

## The pieces

- **Project brain** — a folder with `talamus.json` (created by `talamus init`,
  which always targets the current directory). It owns its notes.
- **Central brain** — `talamus init --global` (lives under `TALAMUS_HOME`, default
  `~/talamus/default`). Durable personal knowledge + the federation hub.
- **Registry** — `TALAMUS_HOME/registry.json`: every brain on the machine, with
  type (`project`/`central`/`archive`) and the `federated`/`sensitive` flags.
  `init` registers automatically; `talamus brains register PATH` adds existing ones.
- **Federated index** — `talamus brains index`: a rebuildable **pointer index**
  (brain + note + path + metadata). Never source truth: every answer reads the
  real note from the owning brain.

## Scope policies

`ask` / `search` / `recall` / `overview` accept `--scope`:

| policy | meaning |
| --- | --- |
| `project-only` | only the current brain |
| `central-only` | only your central brain |
| `project+central` | **default inside a project** — local first, hub as fallback |
| `all` (`--all-brains`) | every registered, federated, non-sensitive brain |

Results carry markers — `[project]`, `[central]`, `[project:name]` — so you always
know where knowledge came from. Brains marked `sensitive` are excluded from `all`
unless you opt in. Missing brains degrade to warnings, never failures.

## Moving knowledge

Writes go to the **current project** by default; promotion to the hub is explicit:

```bash
talamus brains promote "Pattern Retry" --from lavoro --to default
```

Promotion preserves the note id, provenance and history, and records the origin.

## Quick reference

```bash
talamus brains                      # list + flags
talamus brains use <name>           # selected global (when no project is found)
talamus brains set <name> --sensitive true
talamus brains index status
talamus where --json                # which brain resolved, and why
```
