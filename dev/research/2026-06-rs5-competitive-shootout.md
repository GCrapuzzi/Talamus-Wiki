# RS5 — competitive retrieval shootout (2026-06)

First REAL head-to-head against the competition, on a judged IR benchmark, with
every system run on the same corpus/queries/qrels through one harness
(`benchmarks/shootout/`). Phase 1 systems: Talamus (lexical + smart), BM25
(rank-bm25), dense-RAG (sentence-transformers `all-MiniLM-L6-v2` + FAISS exact
inner-product). Corpus: BEIR **SciFact** (5183 docs, official qrels). No
embeddings in the product — the vector DB is a bench-only competitor.

## Headline: full test set (300 queries, deterministic, free systems)

| system | recall@10 | nDCG@10 | MRR | hit@10 | p50 ms | extra RAM |
|---|---|---|---|---|---|---|
| talamus-search | 0.776 | 0.607 | 0.562 | 0.793 | 68 | none |
| bm25 | 0.776 | **0.652** | **0.618** | **0.797** | 33 | none |
| vectordb (MiniLM+FAISS) | **0.783** | 0.645 | 0.605 | 0.793 | 12 | 80 MB model |

**The result the product thesis needed, and it is honest: on a clean semantic
IR benchmark — the vector DB's home turf — lexical retrieval matches dense
embeddings.** recall@10 0.776 vs 0.783 (Δ +0.007); hit-rate IDENTICAL at 0.793;
and BM25 actually leads on ranking quality (nDCG 0.652, MRR 0.618). The dense
advantage that looked like +0.07 on a 50-query subset nearly vanishes at full
scale — with ZERO embedding infrastructure on our side.

Honest caveats (stated, not buried):
- **Talamus-search trails BM25 on nDCG/MRR** (0.607/0.562 vs 0.652/0.618): our
  stemming + trigram channel buys recall parity but ranks the top results
  slightly worse than vanilla BM25 on monolingual English scientific text. A
  real tuning front (the trigram channel adds noise where cross-language isn't
  needed — consider an adaptive blend that down-weights trigrams for
  monolingual corpora).
- **SciFact is the dense model's best case and our worst**: English,
  monolingual, paraphrase-heavy. It does NOT exercise Talamus's cross-language
  bridge, symptom enrichment, or the three moats (time/meaning/verifiability).
  We tie on its turf; our turf is the whole workflow.
- **vectordb's 12ms/query hides its cost**: it loaded an 80 MB embedding model
  into RAM and paid an encode pass at ingest. talamus/bm25 need no model and no
  GPU.

## The LLM tier (talamus-smart, Query2doc), 50-query subset

| run | talamus-search | talamus-smart | bm25 | vectordb |
|---|---|---|---|---|
| recall@10 | 0.703 | 0.763 / 0.703 | 0.723 | 0.790 |

talamus-smart (LLM query expansion) is the ask-path tool, not a search
competitor: ~10 s/query (the LLM call) vs 12–68 ms for the index tiers. On
SciFact it is also NOISY (0.763 then 0.703 across two runs — expansion is
nondeterministic) and helps little, because scientific-claim queries already
share vocabulary with the abstracts (no vocabulary gap to bridge). Smart's win
is on VAGUE cross-language queries (the book corpus: hit 0.86→0.97), which
SciFact does not contain. Reported separately and honestly.

## What this establishes

1. The "parity without embeddings" claim is now MEASURED on a standard judged
   benchmark, not asserted: recall/hit parity with a real vector DB.
2. BM25 and Talamus-search are recall-equivalent here; Talamus's edge over BM25
   shows up on the cross-language/vague corpora, not on SciFact.
3. A real, reproducible harness exists: add a competitor = one adapter; run =
   one command; results are provenance-stamped.

## Method & reproducibility

```
pip install -e ".[bench]"
python benchmarks/run.py --tier shootout --yes --dataset scifact --no-smart   # free, full set
python benchmarks/run.py --tier shootout --yes --dataset scifact --queries 50 # + LLM smart tier
```

Same corpus/queries/qrels for every system; exact FAISS index (best-case dense
recall, not approximate HNSW — we do not sabotage the competitor); same k=10.
Results land provenance-stamped in `benchmarks/results/`.

## Next (later phases)

- mem0 adapter (agent-memory peer); Zep/llm_wiki qualitative capability matrix.
- Layer-2 workflow profiler: ingest cost, €/answer, hallucination rate,
  verifiability — the axes where SciFact-style benchmarks say nothing and our
  moats live.
- Multi-dataset: a cross-language and a vague-query judged set where Talamus's
  bridge + smart tier should pull ahead (SciFact is the adversarial case for us).
- The ~10k real corpus for token/€/footprint curves.
- Adaptive trigram blend to recover the nDCG/MRR gap vs BM25 on monolingual text.
