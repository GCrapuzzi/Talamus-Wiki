---
type: pattern
tags: [inference, serving, prefill, decode, disaggregation]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#inference-service-optimization
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Prefill-Decode Disaggregation

Separating LLM prefill and decode onto different hardware instances because they have incompatible computational profiles:
- **Prefill**: compute-bound → benefits from high FLOP/s
- **Decode**: memory bandwidth-bound → benefits from high bandwidth

Running both on the same GPU causes resource contention: a new prefill job drains compute from existing decode jobs, degrading TPOT for in-flight requests.

DistServe (Zhong et al., 2024) and "Inference Without Interference" (Hu et al., 2024) show significant goodput improvements. Communication overhead for transferring intermediate states between prefill and decode instances is manageable on modern GPU clusters with NVLink.

**Prefill:decode instance ratio** depends on workload:
- Long inputs + prioritize TTFT → 2:1 to 4:1
- Short inputs + prioritize TPOT → 1:2 to 1:1
