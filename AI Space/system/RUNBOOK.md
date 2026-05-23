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

Cosa fa: enumera `AI Space/pending/`, classifica ogni file (`markdown`/`text`/`pdf`/`image`/`unknown`), lo sposta in `AI Space/raw/<categoria>/`, scrive il normalized markdown in `AI Space/normalized/<categoria>/` con frontmatter di provenance, aggiorna `AI Space/normalized/registry.json`, promuove note in `FDE Brain/` via Claude CLI, scrive il run log JSON in `AI Space/logs/runs/`, e committa `chore(ai-pipeline): ingest pending batch YYYY-MM-DD`.

Routing speciale:

- estensione non riconosciuta → `AI Space/review/needs-human/`
- PDF senza testo estraibile → `AI Space/review/low-confidence-normalization/`
- OCR fallito → `AI Space/failed/technical-failures/`

Exit code: `0` se tutti i file sono stati elaborati (anche se ruotati a review), `1` se almeno un file ha avuto un errore tecnico.

### Long-PDF behavior (V3)

I PDF lunghi (≥3 voci outline o >50 pagine) attivano la pipeline multi-nota V3:

1. **Normalize layout-aware**: per ogni pagina del PDF, oltre a `pypdf.extract_text()` viene ispezionata la presenza di immagini/figure/form embedded (`/XObject` di subtype `/Image` o `/Form`). Se la pagina è visual-rich, viene renderizzata a PNG via `pypdfium2` e passata a GLM-OCR; il testo OCR viene combinato con quello pypdf (più lungo vince, oppure concatenati con un marker se entrambi sostanziosi). Tempo: ~5-8s extra per pagina visual-rich.

2. **Distill multi-chunk Claude-driven**: il normalized viene splittato per macro-capitolo L1. Per ogni chunk, una chiamata `claude -p` chiede a Claude di estrarre 0..N note atomiche (`concept`/`framework`/`operation`/`method`/`pattern`/`glossary`) con citazioni puntuali ai heading anchors. Le note possono fondere sotto-sezioni. Una passata finale di overview wikilinka le note prodotte.

3. **Wikilink validation**: tutti i `[[link]]` che puntano a titoli non prodotti vengono rimossi (testo conservato), per evitare allucinazioni nel grafo.

4. **Audit log**: scritto in `AI Space/logs/decisions/{ts}-{run_id}-distill.json` con statistiche per chunk e elenco dei wikilink rimossi.

Per fonti brevi (markdown, text, immagini, PDF <50 pagine senza outline) rimane attivo il flusso V1 single-note (`distill_via_claude`).

## Pending Folder Contract

`AI Space/pending/` is a temporary drop zone. It can contain arbitrary files and notes. It should be empty after a successful scheduled ingestion run, but only after files are safely archived, reviewed, or failed.
