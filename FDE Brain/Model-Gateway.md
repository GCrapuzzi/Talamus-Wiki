---
type: pattern
tags: [gateway, infrastructure, api-management, architecture]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#step-3-add-model-router-and-gateway
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Model Gateway

An intermediate layer providing a unified interface to heterogeneous model backends (self-hosted + commercial APIs). Core functions:

- **Unified API** — single interface regardless of provider; if a model API changes, only the gateway is updated.
- **Access control** — centralised token management instead of distributing org API keys; fine-grained per-user/per-app model permissions.
- **Cost management** — monitor and limit API call usage.
- **Fallback & resilience** — route to alternative models on rate limits or API failures; retry with backoff.
- **Bonus capabilities** — load balancing, logging, analytics, caching, guardrails.

Off-the-shelf options: Portkey AI Gateway, MLflow AI Gateway, Wealthsimple LLM Gateway, TrueFoundry, Kong, Cloudflare.
