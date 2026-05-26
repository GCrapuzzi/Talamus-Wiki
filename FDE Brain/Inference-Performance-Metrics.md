---
type: framework
tags: [inference, latency, throughput, goodput, SLO, metrics]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#inference-performance-metrics
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Inference Performance Metrics

Key metrics for evaluating inference systems, organized by stakeholder concern.

### Latency metrics
- **TTFT (Time to First Token)**: duration of the prefill step; depends on input length. For agentic/CoT queries, distinguish model TTFT from user-visible "time to publish."
- **TPOT (Time Per Output Token)**: decode speed after first token. ~120 ms/token (6–8 tokens/s) matches fast human reading speed.
- **TBT / ITL**: time between tokens / inter-token latency — variations of TPOT.
- **Total latency** = TTFT + TPOT × (number of output tokens)

Report latency as percentiles (p50, p90, p95, p99), not averages — outliers skew means.

### Throughput metrics
- **Tokens/s (TPS)**: output tokens generated per second across all users. Directly linked to cost.
- **RPM**: completed requests per minute.
- Separate input and output throughput — they have different computational profiles.

### Quality-adjusted metric
- **Goodput**: requests/s that satisfy the SLO (e.g., TTFT ≤ 200 ms and TPOT ≤ 100 ms). Prevents optimizing raw throughput at the expense of user experience.

Latency and throughput trade off: 2–3× throughput gains are common if you sacrifice TTFT/TPOT (LinkedIn, 2024).
