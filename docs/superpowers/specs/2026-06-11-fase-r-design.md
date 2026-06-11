# Fase R — Rivoluzione: UI da 10k stelle + memoria per chiunque

**Data:** 2026-06-11 · **Stato:** design approvato dalla direttiva di Giovanni.
**Direttiva:** la UI attuale è impalcatura, non prodotto ("solo spazi vuoti");
ispirarsi a llm_wiki; grafo vero con fisica stile Obsidian (click sul nodo →
nota); impostazioni complete (chiavi API, motore, MCP, ...). E oltre la UI:
portare il progetto a livello avanzato e rivoluzionario. **Vincoli invariati**,
in particolare: niente embeddings; Python; core stdlib; il target rivoluzionario
è che *chiunque* — anche l'utente meno tecnico — configuri memorie personali e
agentiche avendo SOLO l'abbonamento da ~20€/mese di un coding agent qualsiasi.

## Studio: cosa rende buona la UI di llm_wiki (analisi 2026-06-11)

- Layout a **tre colonne ridimensionabili**: albero/fonti a sinistra, lavoro al
  centro, anteprima/inspector a destra; **sidebar a icone** per cambiare vista.
- **Grafo**: sigma.js + ForceAtlas2; nodi colorati per tipo/community (Louvain,
  palette a 12 colori), dimensione = numero di link, hover evidenzia i vicini.
- Settings con provider LLM, chiavi API e preferenze, tutto in-app.
- Stack: React+Tailwind+shadcn su Tauri — **non replicabile in Python**, ma i
  *principi* sì: densità calma, gerarchia tipografica, pannelli, grafo fisico.

**Decisione di stack (confermata):** restiamo su **Flet** (vincolo "tutto
Python, nessuna API" già deciso). Il gap non era lo stack ma il design: Flet
regge un workbench denso con tema scuro, card e pannelli; il grafo fisico si
implementa in **puro Python** su `flet.canvas` (force-directed, zero dipendenze).

## I cantieri della fase

### R1 — Design system + layout (ui/theme.py, refactor viste)
Tema scuro di default (palette tipo "carbone + accenti per tipo di relazione"),
scala di spaziatura, card, gerarchia tipografica; layout a tre zone: rail a
icone · pannello principale · **inspector destro** (fonti, relazioni, storia
della nota aperta). Stati vuoti curati ("empty state" con azione, non vuoto).

### R2 — Grafo vero con fisica (ui/graph.py)
Force-directed in puro Python (repulsione O(N²) con cap dei nodi visibili,
molle sugli archi, gravità al centro, damping; integrazione verlet) disegnato su
`flet.canvas`, animato con un loop a timer. **Click sul nodo → apre la nota**;
colore = dominio (overview), dimensione = grado; archi tipizzati distinti da
`related`. Vista globale (cap ~150 nodi più connessi) + vista locale (vicinato
della nota aperta). Fisica testabile headless (il layout è una funzione pura).

### R3 — Impostazioni complete (ui/settings + config)
In-app: scelta del **motore** tra quelli rilevati sul PATH (claude/codex/gemini/
ollama) o API; modello; **chiave API** salvata in `TALAMUS_HOME/credentials.json`
(mai nel repo: la nostra stessa redaction la flaggerebbe — env var vince sempre);
budget di contesto; bottoni **Installa MCP** e **Installa hook**; gestione del
registry dei brain (flag federated/sensitive); default dello scan.

### R4 — "Qualsiasi coding agent da 20€" (adapters + talamus setup)
Adapter CLI per **codex** e **gemini** (oggi mancano: solo claude-cli/ollama/
api). Comando **`talamus setup`**: rileva gli agent installati, sceglie/conferma
il motore, installa MCP + hook per quell'agent, crea il brain, propone lo scan
— l'onboarding intero in un comando (e nella UI come primo avvio). Questa è la
tesi rivoluzionaria resa prodotto: l'abbonamento che hai già È la memoria.

### R5 — Ricerca: routing multi-livello senza embeddings
Il baseline M0 ha provato che l'overview single-level ha costo token **lineare**
e il recall sulle domande vaghe è il gap (0.39 vs 0.85). R5 costruisce
l'**overview gerarchico** (domini → sotto-domini, indotti dagli stessi cluster
strutturali) con routing a 2 passi a costo ~log(N), e misura su eval-set reale.
Niente embeddings: la scommessa scientifica è che ontologia emergente + routing
gerarchico + lessico stemmato bastino — e l'harness lo dimostrerà o smentirà.

## Ordine di esecuzione (rischio prima)
R2 grafo (il pezzo più difficile e più visibile) → R1 tema/layout → R3
impostazioni → R4 setup universale → R5 routing gerarchico. Gate verde e commit
per cantiere; la resa visiva si verifica a runtime (`talamus ui`).

## Criteri di accettazione
- Il grafo si muove con fisica fluida a ≥100 nodi, click apre la nota, colori
  per dominio: confrontabile concettualmente con Obsidian/llm_wiki.
- Una persona non tecnica con solo `claude` (o `codex`/`gemini`) installato fa
  `talamus setup` e ha memoria personale + agentica funzionante in <5 minuti.
- Routing gerarchico: curva token sub-lineare misurata; recall sulle vaghe in
  miglioramento misurato vs baseline M4.
- Tutte le impostazioni d'uso quotidiano modificabili dalla UI.
