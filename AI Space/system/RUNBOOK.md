# Development Runbook

This runbook reflects the new open-source product direction. The old
Graphify-centered `tools.fde_brain` commands are legacy prototype commands.

## Current Source Of Truth

Design:

```powershell
Get-Content docs/superpowers/specs/2026-05-27-local-first-knowledge-pipeline-v1-design.md
```

Implementation plan:

```powershell
Get-Content docs/superpowers/plans/2026-05-27-core-graph-first-foundation.md
```

## Foundation Development Flow

Use Superpowers Subagent-Driven execution against the current plan:

```text
docs/superpowers/plans/2026-05-27-core-graph-first-foundation.md
```

Foundation scope:

- package foundation
- generic `src/brain/` package
- `brain init`, `brain status`, `brain doctor`
- canonical note/source models
- Obsidian renderer
- deterministic graph builder
- BM25 fallback
- graph-first `ask context`
- agent skill and tool-calling docs

Do not include conversion adapters, OCR, LLM extraction, scheduling, or UI in
this foundation pass.

## Expected Verification

During implementation, run the commands specified in the plan. Final foundation
verification should include:

```powershell
$env:PYTHONPATH="src"
python -m unittest discover -s tests -v
```

Beginner smoke flow:

```powershell
$tmp = Join-Path $env:TEMP "brain-foundation-smoke"
Remove-Item -LiteralPath $tmp -Recurse -Force -ErrorAction SilentlyContinue
$env:PYTHONPATH="src"
python -m brain.cli init --root $tmp
python -m brain.cli status --root $tmp
python -m brain.cli doctor --root $tmp
```

## Legacy Areas

- `FDE Brain/` is a legacy Obsidian vault scaffold. It should not drive product
  architecture.
- `AI Space/` is legacy operating space from the personal prototype.
- `tools/fde_brain/` remains available as reference until an explicit migration
  plan removes it.
- Graphify output is legacy and not part of the new core.
