# Benchmarks (dev-only)

Reproducible measurements that back Talamus's efficiency claims. Not part of the
package; they need the `bench` extra and a real brain to run against.

```bash
pip install -e ".[bench]"
python benchmarks/token_efficiency.py PATH_TO_BRAIN
```

- **`token_efficiency.py`** — token cost of targeted *recall* vs *loading the whole
  brain*, plus the cost of *search* (titles+summaries). Uses tiktoken (cl100k_base)
  as a tokenizer proxy. Build a brain first with `talamus ingest`.
