# Talamus UI — Design (Flet)

**Data:** 2026-06-08 · **Stato:** design del primo cut. · La UI è il **primo componente non-MVP**: deve essere solida, nativa, installabile su tutti i dispositivi, bella e completa.

## Stack & principi

- **Flet** (Python → Flutter): un solo codice Python → **desktop (Win/mac/Linux) + web + mobile**; `flet build <target>` produce gli installabili nativi.
- **Nessuna API**: la UI chiama l'**SDK Talamus direttamente** (in-process). Flet gestisce il ponte col frontend Flutter.
- **UI sottile**: tutta la logica sta nell'SDK già testato (`recall`, `ask`, `domains`, `store`, `timeline`, `correct`…). La UI orchestra e rende, non duplica logica.
- **Local-first**: opera su un brain risolto come per la CLI (`--root`/scoping).

## Avvio & packaging

- Comando **`talamus ui [--root ...]`** → lancia `flet` con `app(target=main)`.
- Extra opzionale **`ui = ["flet>=0.24"]`** (il core resta stdlib).
- Distribuzione: `flet build windows|macos|linux|web|apk|ipa`.

## Schermate (primo cut)

Layout: una **NavigationRail** a sinistra (Chat · Cerca · Domini) + area contenuto a destra (Material/Flutter).

1. **Chat sulla memoria** — casella domanda → `answer_question` → **risposta citata**; le citazioni `[n]` rimandano alle note usate. (Multi-turno: iterazione.)
2. **Cerca** — query → `search_notes` → lista risultati (titolo + riassunto) → click apre la nota.
3. **Vista nota** — rende il Markdown della scheda; i **wikilink `[[X]]`** sono cliccabili e **navigano** alla nota X.
4. **Domini** — `load_overview` → elenco domini (nome + descrizione) → click → note di quel dominio.

## Iterazioni successive

- **Effetto-Wikipedia**: anteprima all'**hover** dei wikilink (popover col corpo della nota linkata).
- **Viz del grafo** (WebView interna + sigma.js, o Canvas).
- **Ingestione da UI** (file picker → `ingest_path`), inclusi cartelle/URL.
- **Code di revisione** (consolidamento / correzione-da-fonte / proposte d'ontologia) con UI di approvazione.
- **Storia bitemporale** della nota (timeline `history`/`--as-of`) e **editing** delle note (poi `reindex`).
- Selettore **motore/brain**, stato/`doctor` in UI.

## Verifica

La GUI si verifica eseguendo **`talamus ui`** (non è testabile headless in CI). La UI resta sottile apposta: i percorsi logici (recupero, risposta, domini) sono coperti dai test dell'SDK; la UI aggiunge solo rendering e navigazione.
