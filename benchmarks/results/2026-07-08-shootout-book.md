# Retrieval shootout

commit `1f0671b` · 2026-07-08T09:47:53 · 212 docs · 35 queries · k=10

| system | recall@k | MRR | hit | nDCG | p50 ms | ingest LLM calls |
| --- | --- | --- | --- | --- | --- | --- |
| talamus-search | 0.829 | 0.727 | 0.914 | 0.732 | 11.6 | 0 |
| talamus-smart | 0.929 | 0.865 | 0.971 | 0.847 | 16687.6 | 0 |
| bm25 | 0.771 | 0.685 | 0.829 | 0.688 | 0.8 | 0 |
| vectordb | 0.700 | 0.535 | 0.743 | 0.565 | 161.4 | 0 |
| dense-multilingual | 0.871 | 0.857 | 0.914 | 0.837 | 1781.2 | 0 |
