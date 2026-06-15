# Retrieval shootout

commit `23f4aef` · 2026-06-15T16:04:26 · 5183 docs · 300 queries · k=10

| system | recall@k | MRR | hit | nDCG | p50 ms | ingest LLM calls |
| --- | --- | --- | --- | --- | --- | --- |
| talamus-search | 0.776 | 0.562 | 0.793 | 0.607 | 68.1 | 0 |
| bm25 | 0.776 | 0.618 | 0.797 | 0.652 | 33.2 | 0 |
| vectordb | 0.783 | 0.605 | 0.793 | 0.645 | 12.3 | 0 |
