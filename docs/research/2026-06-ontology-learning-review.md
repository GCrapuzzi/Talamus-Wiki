# Ontologia auto-emergente: revisione e decisioni (F5.6)

**Data:** 2026-06-10 · **Stato:** v1, accompagna l'Ontology Lab (M5).
**Domanda di ricerca (PRD 12.1):** può Talamus indurre dal corpus locale
un'ontologia stabile, utile e comprensibile, senza prescrivere l'intero sistema
di tipi, restando economico, verificabile ed evolvibile nel tempo?

## 1. Il problema specifico di Talamus

L'estrazione LLM emette superfici di relazione **libere** ("alimenta",
"sostituisce", "deriva da"). Il normalizzatore a tipi fissi ne riconosce 5
(uses / is-a / part-of / contrasts-with / depends-on) e appiattisce tutto il
resto a `related`: **perdita d'informazione sistematica**, misurabile come quota
di archi non tipizzati (metrica *coverage*). L'obiettivo non è "costruire
un'ontologia" in astratto: è **recuperare significato già presente nel corpus**
e usarlo per il recupero, con revisione umana e storia.

## 2. Posizionamento rispetto alla letteratura

**Ontology learning classico** (Text2Onto, OntoLearn; survey Buitelaar et al.):
pipeline termini→concetti→tassonomia→relazioni, tipicamente supervisionata da
risorse esterne (WordNet) e pensata per corpora di dominio statici. *Differenza:*
Talamus parte da note già concettualizzate dall'estrattore (i "concetti" esistono
già: sono le schede), quindi il problema si riduce all'**induzione del sistema di
tipi di relazione** — più trattabile e locale.

**Taxonomy induction** (Hearst patterns; TaxoGen): induce gerarchie is-a.
*Differenza:* is-a è già un tipo fisso; il valore per Talamus sta nei tipi NON
tassonomici specifici del corpus (chi alimenta cosa, chi sostituisce cosa).

**OpenIE** (ReVerb, OLLIE, OpenIE5, Stanford): estrae triple a superficie aperta
senza schema. È l'analogo più vicino al nostro *evidence layer*, con la stessa
debolezza nota: proliferazione di superfici sinonime senza canonicalizzazione.
*Scelta:* teniamo il passo OpenIE-like (le triple grezze dell'estrattore) ma
aggiungiamo il livello che a OpenIE manca: clustering delle superfici +
promozione governata a tipi canonici.

**KG construction con LLM** (GraphRAG di Microsoft, AutoKG, KG-GPT): gli LLM
costruiscono grafi entity-relation su larga scala; le relazioni o sono open
(rumorose) o prescritte (perdita). GraphRAG aggiunge community detection +
summary gerarchici — strutturalmente simile al nostro overview di domini, ma
**il grafo è trattato come verità** e non c'è revisione umana né storia dello
schema. *Differenza chiave di Talamus:* il grafo resta **indice**, le risposte
leggono le note reali, e lo schema è un artefatto versionato e rivedibile.

**Temporal knowledge graphs / Zep, Graphiti:** bitemporalità sugli *edge*
(fatti che si invalidano). Talamus la estende di un livello: oltre ai fatti,
**lo schema stesso è temporale** (tipi con valid_from/valid_to, candidate →
active → deprecated, mai cancellati). Nei TKG accademici lo schema è assunto
fisso; questa è la nostra scommessa differenziante.

**Agent memory** (mem0, Zep, Letta/MemGPT): memorie episodiche/semantiche con
estrazione di fatti, poca o nessuna ontologia esplicita, nessuna revisione umana
del *tipo* di conoscenza. *Differenza:* Talamus tratta i tipi di relazione come
conoscenza di prima classe che l'utente può promuovere, rifiutare, deprecare.

## 3. Cosa abbiamo implementato (v1) e perché

1. **Evidence layer deterministico** — ogni superficie grezza diventa un record
   con soggetto/oggetto/contesto/fonte. Costo: zero LLM. (Eco di OpenIE, ma con
   provenienza obbligatoria.)
2. **Clustering deterministico delle superfici inspiegate** — chiave = token
   stemmati della superficie. Il *cosa* diventa candidato lo decide il supporto
   (soglie), non l'LLM: riproducibilità e stabilità by-design (Jaccard = 1.0 su
   corpus invariato, misurato).
3. **LLM solo per nominare/definire** — 1 chiamata per induzione, indipendente
   dalla dimensione del corpus. (Ipotesi H2: i segnali simbolici bastano per
   candidati stabili; gli embedding restano un extra opzionale futuro.)
4. **Schema versionato candidate/active/deprecated** con history append-only e
   regole di promozione (supporto ≥ 8 su ≥ 3 note, nomi non in conflitto,
   esempi con fonti reali — PRD 12.6). I candidati NON toccano il runtime
   (F5.10). (Ipotesi H3/H4.)
5. **Aggancio al runtime misurabile** — le superfici dei tipi ATTIVI vengono
   ri-tipizzate in `build_ontology`, e l'espansione 1-hop del recupero dà
   priorità agli archi tipizzati su `related`: una promozione **cambia il
   contesto recuperato** quando il limite taglia. Provato con l'harness eval
   (lift recall: baseline miss → emergente hit sul caso di prova; `talamus
   ontology eval` lo misura su casi reali). (Ipotesi H1.)
6. **Review burden controllato** — i candidati finiscono anche nella coda di
   review; le soglie di induzione (supporto ≥ 3, ≥ 2 note) tengono basso il
   rumore. (Ipotesi H5.)

## 4. Limiti onesti della v1

- Il clustering è **per superficie esatta stemmata**: sinonimi diversi
  ("alimenta" vs "fornisce dati a") restano cluster separati finché un segnale
  di similarità (embedding opzionale o LLM-merge in review) non li unisce.
- L'evidence v1 usa solo `note.relations`; i predicati nel corpo della prosa
  (sezione "relazioni") non sono ancora estratti come superfici autonome.
- La *retrieval utility* su eval-set reale va ancora misurata a corpus grande
  (E3 su 120 casi); il lift è dimostrato sul meccanismo, non ancora sul corpus
  dei doc reali (dove i tipi emergenti compariranno solo dopo ingest reali).
- Domain/range hints, inversi materializzati nel grafo e tassonomie di tipi
  (tipi di tipi) sono progettati nello schema ma non ancora usati dal runtime.

## 5. Decisioni implementative (richieste da F5.6)

1. **D1 — Mantenere i 5 tipi fissi come baseline permanente.** Lo schema
   emergente li estende, non li sostituisce: fallback garantito (R1).
2. **D2 — Separare per sempre evidence (fatti) da schema (tipi).** L'evidence è
   ricostruibile dal corpus; lo schema è curato e versionato. Mai fonderli.
3. **D3 — LLM mai nel percorso di decisione, solo di proposta.** Clustering e
   soglie decidono cosa esiste; l'LLM nomina; l'umano promuove. Una chiamata per
   induzione, costo indipendente da N.
4. **D4 — Lo schema è temporale come i fatti.** candidate/active/deprecated con
   valid_from/valid_to e history append-only; la deprecazione preserva la
   mappatura (mai delete). Si integra con M6 (valid-time sugli archi).
5. **D5 — Ogni promozione deve essere misurabile.** `ontology eval` (lift su
   recall/MRR vs baseline fissa) e `coverage` sono il giudice; se una promozione
   regredisce il recupero, si deprecata (mai si cancella).
6. **D6 — Embedding solo come extra opzionale** per il merge di superfici
   sinonime, mai richiesti dal core (vincolo stdlib).
7. **D7 — Prossimi passi in ordine:** (a) superfici dalla prosa della sezione
   "relazioni"; (b) merge di cluster sinonimi in review; (c) uso di inversi e
   range-hints nell'espansione; (d) E7 (secondo corpus di dominio diverso) prima
   di dichiarare generalità.

## 6. Metriche correnti (riproducibili)

| metrica | comando | stato v1 |
| --- | --- | --- |
| coverage (quota archi tipizzati) | `talamus ontology status` | misurata per brain |
| stabilità cluster (Jaccard) | `talamus ontology stability` | 1.0 su corpus invariato |
| lift sul recupero | `talamus ontology eval --cases F` | meccanismo provato (test) |
| review burden | `talamus review list` | soglie: supporto ≥3, note ≥2 |
| storia dello schema | `talamus ontology history` | append-only, versionata |
