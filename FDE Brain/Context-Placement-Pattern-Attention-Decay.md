---
type: pattern
status: evergreen
aliases:
  - Context Placement Pattern (Attention Decay)
  - Start-End Prompting
  - Attention Gradient
tags:
  - prompt-engineering
  - llm-optimization
  - prompt-design
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/095-context-length-and-context-efficiency.md
    locator: pages 242-243
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Research has shown that a model is much better at understanding instructions given at the beginning and the end of a prompt than in the middle.
      - All the models tested seemed much better at finding the information when it’s closer to the beginning and the end of the prompt than the middle.
created: 2026-05-26T21:55:45.922750+00:00
updated: 2026-05-26T21:55:45.922750+00:00
ingestion_run: 8d527d59
---

# Context Placement Pattern (Attention Decay)

## Summary

LLMs tend to perform optimally when critical instructions or information are placed at the beginning and the end of a prompt, showing reduced performance when the same information is buried in the middle of a long context.

## Core Idea

Model attention mechanisms are not uniformly distributed across the input context. Placing key information at the boundaries (start/end) maximizes the model's ability to retrieve and utilize that data, mitigating 'attention decay' over long inputs.

## Practical Use

Structure complex prompts by placing the primary instruction/goal at the beginning (System Prompt) and the required output format or final constraint at the end. Use the middle section for the bulk of the source material or context data.

## Related

- [[Needle-in-a-Haystack-NIAH|Needle in a Haystack (NIAH)]]
- System Prompt Engineering
