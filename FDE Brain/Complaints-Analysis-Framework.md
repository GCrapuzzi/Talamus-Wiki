---
type: framework
status: evergreen
aliases:
  - Complaints Analysis Framework
  - Failure Mode Taxonomy
  - User Dissatisfaction Categorization
tags:
  - ai-engineering
  - product-management
  - data-analysis
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/175-extracting-conversational-feedback.md
    locator: pages 499-503
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Complaints can also be general expressions of negative sentiments... without explaining the reason why...
      - If you know that the user doesn’t like verbose answers, you can change the bot’s prompt to make it more concise.
created: 2026-05-26T21:55:46.572221+00:00
updated: 2026-05-26T21:55:46.572221+00:00
ingestion_run: 8d527d59
---

# Complaints Analysis Framework

## Summary

A structured approach to classifying user complaints into specific failure categories (e.g., irrelevance, factual inaccuracy, lack of detail, tone) rather than treating them as general negative sentiment.

## Core Idea

Moving beyond 'bad answer' requires taxonomy. By classifying complaints (e.g., 'Answer is factually incorrect' vs. 'Answer is too verbose'), engineering teams can target specific prompt or data gaps, leading to precise model improvements.

## Practical Use

Implement a classification layer on all complaint feedback. Use the resulting categories (e.g., 'Lacking Detail', 'Irrelevant', 'Factually Incorrect') to create a prioritized backlog of model improvements, directly linking user pain points to engineering tasks.

## Related

- [[Natural-Language-Feedback-Signals|Natural Language Feedback Signals]]
