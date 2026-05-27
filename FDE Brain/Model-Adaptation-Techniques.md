---
type: decision_framework
status: evergreen
aliases:
  - Model Adaptation Techniques
  - Prompting vs Finetuning
  - Model Customization Strategy
tags:
  - ai-engineering
  - llm-ops
  - optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/035-ai-engineering-versus-ml-engineering.md
    locator: pages 63-69
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Prompt-based techniques... adapt a model without updating the model weights.
      - Finetuning... requires updating model weights.
      - Prompt engineering is easier to get started and requires less data.
      - Finetuning techniques... can improve your model’s quality, latency, and cost significantly.
created: 2026-05-26T21:55:45.477346+00:00
updated: 2026-05-26T21:55:45.477346+00:00
ingestion_run: 8d527d59
---

# Model Adaptation Techniques

## Summary

A decision framework for customizing foundation models based on complexity, data availability, and performance requirements. Techniques range from non-weight-updating prompting to full weight-updating finetuning.

## Core Idea

The choice of adaptation technique dictates the required resources (data, compute) and the achievable performance ceiling. Prompting is easiest but limited; Finetuning is complex but powerful.

## Practical Use

1. Start with Prompt Engineering (low data, fast iteration) for initial prototypes. 2. If performance requirements are strict or the task is complex, escalate to Finetuning (high data, high compute) to improve quality and latency.

## Related

- [[Prompt-Engineering|Prompt Engineering]]
- [[Finetuning|Finetuning]]
- Dataset Engineering
