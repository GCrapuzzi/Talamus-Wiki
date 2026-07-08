# Retrieval shootout

commit `1f0671b` · 2026-07-08T10:59:54 · 5183 docs · 300 queries · k=10

| system | recall@k | MRR | hit | nDCG | p50 ms | ingest LLM calls |
| --- | --- | --- | --- | --- | --- | --- |
| talamus-search | 0.797 | 0.628 | 0.813 | 0.664 | 86.0 | 0 |
| bm25 | 0.776 | 0.618 | 0.797 | 0.652 | 39.9 | 0 |
| vectordb | 0.783 | 0.605 | 0.793 | 0.645 | 28.3 | 0 |
| dense-multilingual | 0.807 | 0.666 | 0.820 | 0.694 | 229.4 | 0 |
