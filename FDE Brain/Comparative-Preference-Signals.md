---
type: method
status: evergreen
aliases:
  - Comparative Preference Signals
  - A/B testing feedback
  - Side-by-side comparison
tags:
  - ai-engineering
  - ml-ops
  - data-collection
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/176-feedback-design.md
    locator: pages 504-513
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - When a model is uncertain, outputting two summaries side-by-side allows the user to choose their preference.
      - Comparative signals can be used for preference finetuning.
      - Showing partial responses side-by-side can reduce cognitive load and improve vote quality.
created: 2026-05-26T21:55:46.580369+00:00
updated: 2026-05-26T21:55:46.580369+00:00
ingestion_run: 8d527d59
---

# Comparative Preference Signals

## Summary

A technique used when a model is uncertain about the optimal output, presenting the user with two or more options to elicit a clear preference signal for fine-tuning.

## Core Idea

Instead of asking for subjective ratings ('Which is better?'), presenting concrete choices (A vs. B) forces the user to provide a high-signal, comparative vote, which is ideal for preference fine-tuning (RLHF).

## Practical Use

When summarizing a paper, if the model is uncertain between a 'short, high-level summary' and a 'detailed section-by-section summary,' present both side-by-side. The user's click/selection provides a direct preference signal. If full responses are too much, show partial responses (e.g., Google Gemini) and require a click to expand, making the vote low-effort.

## Related

- [[AI-Feedback-Signal-Taxonomy|AI Feedback Signal Taxonomy]]
- [[Feedback-Collection-Timing-Framework|Feedback Collection Timing Framework]]
