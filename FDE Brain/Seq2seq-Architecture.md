---
type: concept
status: evergreen
aliases:
  - Seq2seq Architecture
  - Sequence-to-Sequence Model
  - Encoder-Decoder Model
tags:
  - ai-engineering
  - llm
  - architecture
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/042-modeling.md
    locator: pages 82-82
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - At a high level, seq2seq contains an encoder that processes inputs and a decoder that generates outputs.
      - Seq2seq uses RNNs (recurrent neural networks) as its encoder and decoder.
      - The decoder then generates output tokens sequentially, conditioned on both the final hidden state of the input and the previously generated token.
created: 2026-05-26T21:55:45.525791+00:00
updated: 2026-05-26T21:55:45.525791+00:00
ingestion_run: 8d527d59
---

# Seq2seq Architecture

## Summary

A foundational neural network architecture used for tasks involving input and output sequences (e.g., machine translation, summarization). It consists of an Encoder that processes the input and a Decoder that generates the output.

## Core Idea

Seq2seq models process inputs and outputs as sequences of tokens. The Encoder uses RNNs to process the input and condense it into a final hidden state. The Decoder then generates output tokens sequentially, conditioned on both the input's final hidden state and the tokens it has already generated.

## Practical Use

While largely superseded by the Transformer, understanding the Seq2seq pattern (Encoder -> Context Vector -> Decoder) is crucial for understanding the evolution of NLP models and for implementing simpler, specialized sequence tasks where the full complexity of a Transformer is overkill.

## Related

- [[Transformer-Architecture|Transformer Architecture]]
- RNNs
