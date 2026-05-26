---
type: glossary
tags: [language-model, tokenization, autoregressive, masked-language-model, fundamentals]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#chapter-1-introduction-to-building-ai-applications-with-foundation-models
  - AI Space/normalized/pdf/ai-engineering.md#from-language-models-to-large-language-models
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Language Model

A model that encodes statistical information about one or more languages, predicting how likely a token is to appear in a given context.

The basic unit is a **token** — a character, word, or subword (e.g. `-tion`). Tokenization balances vocabulary size efficiency with semantic granularity: tokens carry more meaning than characters but produce a smaller vocabulary than whole words, and handle unknown words by splitting them into known subword units.

Two main architectures:

- **Masked language model** (e.g. BERT): predicts missing tokens using bidirectional context (fill-in-the-blank). Used for classification, sentiment analysis, code debugging.
- **Autoregressive language model** (a.k.a. causal LM): predicts the next token using only preceding tokens. Powers text generation; dominates current foundation model landscape.

Autoregressive LMs are **completion machines** — given a prompt, they complete it. This simple mechanism is surprisingly general: translation, summarization, classification, and coding can all be framed as completion tasks. Outputs are probabilistic predictions, not guaranteed-correct answers.

Historical roots trace to Claude Shannon's 1951 "Prediction and Entropy of Printed English." Key concepts like entropy remain central to language modeling today.
