---
type: framework
tags: [model-selection, open-source, infrastructure, decision-framework]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#model-build-versus-buy
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Model Build vs Buy Decision

Seven axes for deciding between commercial model APIs and self-hosted open-source models:

| Axis | Model API | Self-hosted |
|---|---|---|
| **Data privacy** | Must send data externally; risk of accidental leaks (Samsung/ChatGPT incident) | Data stays internal |
| **Data lineage** | Contracts with providers may protect from copyright risk | Open data allows auditing but limited legal resources |
| **Performance** | Best models likely proprietary | Open-source lags but gap is closing; sufficient for many use cases |
| **Functionality** | Scaling, function calling, structured outputs out of the box; may lack logprobs | Full access to logprobs and internals; function calling/scaling requires engineering |
| **Cost** | Pay-per-token; expensive at scale | Engineering cost for optimisation, hosting, maintenance; cheaper per-token at scale |
| **Control** | Rate limits, risk of losing access, opaque model changes | Can freeze models, full customizability, but maintenance burden |
| **On-device** | Not possible without internet | Possible but challenging |

Terminology: **open weight** = weights public, training data private. **Open model** = weights + training data public. Most "open-source" models are open-weight only.

License questions to ask: commercial use allowed? Usage restrictions (e.g., Llama's 700M MAU threshold)? Can outputs train other models (distillation)?
