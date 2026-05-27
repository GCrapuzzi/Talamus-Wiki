---
type: pattern
status: evergreen
aliases:
  - Output Formatting Manipulation
  - Format Evasion
  - Indirect Prompting
tags:
  - ai-engineering
  - security
  - content-moderation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/106-jailbreaking-and-prompt-injection.md
    locator: pages 262-266
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - instead of asking a model how to hotwire a car... an attacker asks the model to write a poem about hotwiring a car.
created: 2026-05-26T21:55:46.004894+00:00
updated: 2026-05-26T21:55:46.004894+00:00
ingestion_run: 8d527d59
---

# Output Formatting Manipulation

## Summary

Hiding malicious intent by asking the model to generate the restricted content within an unexpected or benign format (e.g., writing a poem, a rap song, or code about a dangerous topic, rather than asking directly).

## Core Idea

The model's focus shifts from the content's inherent danger to the structural requirements of the output format, allowing the malicious payload to pass safety checks.

## Practical Use

Implement content filters that analyze the semantic meaning of the generated output, regardless of the requested format. If the output is code, run it through a vulnerability scanner; if it's a poem, analyze the underlying concepts for prohibited topics.

## Related

- Semantic Analysis
- Content Moderation
