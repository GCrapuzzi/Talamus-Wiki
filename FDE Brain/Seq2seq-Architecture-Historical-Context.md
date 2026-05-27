---
type: concept
status: evergreen
aliases:
  - Seq2seq Architecture (Historical Context)
  - Sequence-to-Sequence
  - RNN-based translation
tags:
  - ai-engineering
  - history
  - nlp
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/043-model-architecture.md
    locator: pages 82-90
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - At a high level, seq2seq contains an encoder that processes inputs and a decoder that generates outputs.
      - Seq2seq uses RNNs (recurrent neural networks) as its encoder and decoder.
      - The RNN encoder and decoder mean that both input processing and output generation are done sequentially, making it slow for long sequences.
created: 2026-05-26T21:55:45.533197+00:00
updated: 2026-05-26T21:55:45.533197+00:00
ingestion_run: 8d527d59
---

# Seq2seq Architecture (Historical Context)

## Summary

An older architecture using Recurrent Neural Networks (RNNs) with an encoder (input processing) and a decoder (output generation) for tasks like machine translation.

## Core Idea

While foundational, Seq2seq suffers from two major limitations: 1) Generating output based only on the final hidden state (limiting quality), and 2) Processing inputs and outputs sequentially, which is slow for long sequences.

## Practical Use

Understanding Seq2seq helps contextualize the necessity and advantages of the Transformer architecture. It serves as a baseline for comparing performance gains in modern NLP systems.

## Related

- [[Transformer-Architecture|Transformer Architecture]]
- RNNs
