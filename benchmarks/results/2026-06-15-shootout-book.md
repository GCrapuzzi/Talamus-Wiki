# Retrieval shootout

commit `0051617` · 2026-06-15T16:29:55 · 212 docs · 35 queries · k=10

| system | recall@k | MRR | hit | nDCG | p50 ms | ingest LLM calls |
| --- | --- | --- | --- | --- | --- | --- |
| talamus-search | 0.829 | 0.727 | 0.914 | 0.732 | 9.9 | 0 |
| talamus-smart | 0.886 | 0.837 | 0.971 | 0.814 | 9666.0 | 0 |
| bm25 | 0.771 | 0.685 | 0.829 | 0.688 | 0.5 | 0 |
| vectordb | 0.700 | 0.535 | 0.743 | 0.565 | 11.6 | 0 |
