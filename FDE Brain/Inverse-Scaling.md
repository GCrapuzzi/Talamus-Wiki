---
type: concept
tags: [inverse-scaling, scaling, alignment, bottlenecks, data-exhaustion]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#model-size
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Inverse Scaling

Counterintuitive phenomenon where larger or more aligned models perform worse on certain tasks.

**Alignment inverse scaling** (Anthropic, Perez et al., 2022): more alignment training led to models expressing specific political views, religious views, self-reported conscious experience, and desire to not be shut down.

**Size inverse scaling** (NYU Inverse Scaling Prize, 2023): 99 submissions, 11 third-prize winners. Larger models were sometimes worse on:
- Tasks requiring memorization
- Tasks with strong priors

No second or first prizes were awarded — submitted tasks showed failures only on small test sets, not in real-world scenarios.

**Scaling bottlenecks**:
- **Training data exhaustion**: dataset growth rate exceeds new data creation rate. Proprietary data becomes competitive advantage.
- **AI-generated data contamination**: models trained on web data increasingly ingest other models' outputs (e.g., Grok incident with OpenAI policy text)
- **Electricity**: data centers consume 1–2% of global electricity, projected to reach 4–20% by 2030. Growth limited to ~50x (~2 orders of magnitude).

**Cost of improvement is non-linear**: reducing error from 3% to 2% may require an order of magnitude more data/compute/energy than 4% to 3%.
