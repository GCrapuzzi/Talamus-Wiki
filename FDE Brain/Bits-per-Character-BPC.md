---
type: metric
status: evergreen
aliases:
  - Bits-per-Character (BPC)
  - Character Efficiency Metric
tags:
  - llm-metrics
  - compression
  - data-efficiency
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/060-bits-per-character-and-bits-per-byte.md
    locator: pages 145-145
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If the number of bits per token is 6 and on average, each token consists of 2 characters, the BPC is 6/2 = 3.
created: 2026-05-26T21:55:45.660600+00:00
updated: 2026-05-26T21:55:45.660600+00:00
ingestion_run: 8d527d59
---

# Bits-per-Character (BPC)

## Summary

A metric estimating model efficiency by calculating the bits required per token divided by the average number of characters per token. It is a proxy for compression but is sensitive to tokenization and character encoding.

## Core Idea

BPC is a quick, intuitive metric for model efficiency, but its calculation is highly dependent on the specific tokenization scheme and the character encoding used (e.g., ASCII vs. UTF-8).

## Practical Use

Used for preliminary, comparative analysis of model efficiency when BPB calculation is overly complex. Engineers must account for the underlying character encoding when interpreting BPC results.

## Related

- [[Bits-per-Byte-BPB|Bits-per-Byte (BPB)]]
