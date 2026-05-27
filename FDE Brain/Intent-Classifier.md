---
type: concept
status: evergreen
aliases:
  - Intent Classifier
  - Intent Detection
  - Scope Checker
tags:
  - ai-engineering
  - nlp
  - llm-deployment
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/169-step-3.-add-model-router-and-gateway.md
    locator: pages 480-483
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - An intent classifier can prevent your system from engaging in out-of-scope conversations.
      - An intent classifier can help the system detect ambiguous queries and ask for clarification.
created: 2026-05-26T21:55:46.529920+00:00
updated: 2026-05-26T21:55:46.529920+00:00
ingestion_run: 8d527d59
---

# Intent Classifier

## Summary

A component, often implemented as a smaller language model, responsible for predicting the user's underlying goal or intent from a given query.

## Core Idea

The intent classifier is the core mechanism of the Model Router. It determines if a query is in-scope, what specific action is required, and whether the query is ambiguous. This prevents the system from wasting API calls on out-of-scope or unclear requests.

## Practical Use

Use the classifier first to check if the query is relevant to the product domain. If the query is out-of-scope (e.g., political opinions), the system can provide a polite, pre-written decline response without calling an expensive LLM API. If the query is ambiguous ('Freezing'), the classifier can trigger a clarification prompt.

## Related

- [[Model-Router-Pattern|Model Router Pattern]]
- Guardrails
