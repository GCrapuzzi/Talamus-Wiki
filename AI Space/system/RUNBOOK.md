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

## Run Ingestion

```powershell
python -m tools.fde_brain.ingest --root .
```

Flag opzionali:

- `--no-commit` — esegue tutta la pipeline ma non crea il commit finale (working tree dirty al termine).
- `--dry-run` — esegue solo lo snapshot e il print del riepilogo; non scrive log, non sposta file, non committa.

Cosa fa: enumera `AI Space/pending/`, classifica ogni file (`markdown`/`text`/`pdf`/`image`/`unknown`), lo sposta in `AI Space/raw/<categoria>/`, scrive il normalized markdown in `AI Space/normalized/<categoria>/` con frontmatter di provenance, aggiorna `AI Space/normalized/registry.json`, invoca `claude -p` per la promozione selettiva in `FDE Brain/`, scrive il run log JSON in `AI Space/logs/runs/`, e committa `chore(ai-pipeline): ingest pending batch YYYY-MM-DD`.

Routing speciale:

- estensione non riconosciuta → `AI Space/review/needs-human/`
- PDF senza testo estraibile → `AI Space/review/low-confidence-normalization/`
- OCR fallito → `AI Space/failed/technical-failures/`

Exit code: `0` se tutti i file sono stati elaborati (anche se ruotati a review), `1` se almeno un file ha avuto un errore tecnico.

## Pending Folder Contract

`AI Space/pending/` is a temporary drop zone. It can contain arbitrary files and notes. It should be empty after a successful scheduled ingestion run, but only after files are safely archived, reviewed, or failed.
