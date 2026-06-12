# Ricerca sul recall: il ponte trigram cross-lingua (Fase RS)

**Data:** 2026-06-11 · **Metodo:** error analysis → ipotesi → ablazioni misurate →
solo i vincitori in produzione → pavimento di regressione in CI.
**Strumenti:** eval-set reale da 120 casi (`examples/eval-cases-real.json`),
corpus deterministico dai doc del repo (74 note, zero LLM), laboratorio di
varianti in `talamus/retrieval_lab.py`. **Vincolo:** niente embeddings.

## 1. Diagnosi (error analysis su 56 miss reali)

| classe di fallimento | quota | esempio |
| --- | --- | --- |
| **Mismatch di lingua IT↔EN** | ~60% | "come creo il mio brain personale?" → *"3. Your own brain"*: zero overlap di token |
| Inquinamento da hub | ~20% | la nota-roadmap gigante matcha quasi ogni query per massa lessicale |
| Cross-source multi-nota | ~15% | servono 2-3 note, il ranking ne porta una |

L'intuizione chiave: i **cognati IT/EN condividono trigrammi di caratteri**
(architettur*ali*/architectur*e*, princip*i*/princip*les*, comand*i*/command*s*,
variabil*i*/variabl*es*) — un ponte cross-lingua **senza embeddings**.

## 2. Ablazioni (laboratorio, stessi 120 casi, k=5)

| variante | recall@5 | MRR | hit | cross-src |
| --- | --- | --- | --- | --- |
| V0 baseline (BM25 stemmato) | 0.367 | 0.338 | 0.473 | 0.192 |
| V1 stemming bilingue | 0.377 | 0.341 | 0.473 | 0.175 |
| **V2 canale trigram (titolo)** | **0.489** | **0.456** | **0.600** | **0.367** |
| V3 pesi di campo (titolo×3) | 0.394 | 0.366 | 0.509 | 0.217 |
| V4 propagazione sul grafo | 0.345 ↓ | 0.330 | 0.446 | 0.150 |
| **V123 (combo vincente)** | **0.498** | **0.466** | **0.600** | **0.367** |
| V1234 (+propagazione) | 0.438 ↓ | 0.428 | 0.536 | 0.283 |

Raffinamenti misurati: sweep del peso trigram (ottimo 0.8 sul titolo); **due
canali** titolo 0.7 + summary 0.3 → MRR 0.472, hit 0.618 (scelto). **Scartati
con dati**: propagazione sul grafo (−2pt, conferma il test avversariale storico:
lo spreading additivo inquina), RRF rank-fusion (0.467 < 0.498, e peggiora le
vague), trigram-solo-summary (diluisce la precisione del titolo), espansione
con spodestamento dei seed (E1 = E0, nessun guadagno → non adottata).

## 3. Conferma in produzione (indice persistito + rerank, percorso vero)

Ricetta cablata: **stemmer bilingue** (`textutil`: passata EN tra due passate IT,
"note"/"notes" → stesso stem) + **pesi di campo** nel haystack (titolo×3,
alias×2) + **tre canali nell'indice** (lessicale 1.0 + trigram-titolo 0.7 +
trigram-summary 0.3), su entrambi i backend (FTS5 multi-colonna con pesi
`bm25()` per colonna; posting list per campo nel fallback JSON). CACHE_VERSION 3
(migrazione = `talamus reindex`).

| metrica | M4 (prima) | **RS (ora)** | Δ |
| --- | --- | --- | --- |
| recall@5 | 0.394 | **0.492** | **+25%** |
| MRR | 0.333 | **0.449** | **+35%** |
| hit-rate | 0.491 | **0.600** | **+22%** |
| cross-source | 0.217 | **0.383** | **+76%** |
| direct | 0.467 | **0.650** | +39% |
| code | 0.300 | **0.433** | +44% |
| temporal | 0.700 | **0.833** | +19% |
| vague | 0.317 | 0.267 | −16% ⚠ |
| latenza p95 @10k | 34ms | ~55ms | +21ms (20× sotto il target) |

## 4. Il pavimento di regressione (la ricerca protetta per sempre)

`tests/test_talamus_recall_floor.py` riesegue la misura esatta a ogni gate:
recall ≥ 0.45, MRR ≥ 0.40, hit ≥ 0.55. Chi tocca stemming/indici/ranking e
regredisce, **fallisce la CI**. I numeri non sono uno slide: sono un test.

## 5. Posizione competitiva (perché è difendibile)

Il ponte cross-lingua dei sistemi concorrenti è l'embedding (costo: modello,
RAM, GPU o API). Talamus lo ottiene con **trigrammi di caratteri pesati idf in
FTS5/posting list**: stdlib pura, ~20ms extra a 10k note, funziona offline su
qualsiasi macchina. Per il caso d'uso reale (memorie personali multilingue
europee, dove i cognati abbondano) è un rapporto qualità/costo che gli stack a
embedding non possono eguagliare a parità di footprint.

## 6. Fronte aperto e prossimi esperimenti

1. **Vague (-16%)**: il rumore trigram danneggia le parafrasi senza cognati.
   Ipotesi da testare: blend adattivo (peso trigram ridotto quando la copertura
   lessicale è forte); espansione PRF dai top-3 lessicali; e soprattutto il
   **routing LLM** (overview gerarchico) che in produzione fa da ponte semantico
   — l'harness misura il pavimento deterministico, il percorso `ask` completo va
   misurato con engine reale (esperimento da fare con claude-cli su questo corpus).
2. **Hub pollution**: penalità di lunghezza oltre BM25-b, o splitting delle
   note-doc giganti all'ingest.
3. **E7 ontologia**: secondo corpus di dominio diverso per la generalità.
4. Ri-tarare le soglie del rifiuto dei negativi sui nuovi score multi-canale.
