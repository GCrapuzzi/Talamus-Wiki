# FDE Brain Runbook

## Validate Workspace

```powershell
python -m tools.fde_brain.validate_workspace --root .
```

Expected when foundation is complete:

```text
workspace validation ok
```

## Check Local Engines

```powershell
python -m tools.fde_brain.preflight
```

Expected required tools:

- Claude Code
- Codex CLI
- Git
- Ollama
- GLM-OCR model in Ollama
- Graphify

## Print Graphify Commands

```powershell
python -m tools.fde_brain.graphify brain --root .
python -m tools.fde_brain.graphify sources --root .
```

## Manual Brain Graph Refresh

Print command:

```powershell
python -m tools.fde_brain.graphify brain --root .
```

Copy and run the printed command after confirming Graphify is installed.

## Manual Source Graph Refresh

Print command:

```powershell
python -m tools.fde_brain.graphify sources --root .
```

Copy and run the printed command after confirming Graphify is installed.

## Pending Folder Contract

`AI Space/pending/` is a temporary drop zone. It can contain arbitrary files and notes. It should be empty after a successful scheduled ingestion run, but only after files are safely archived, reviewed, or failed.
