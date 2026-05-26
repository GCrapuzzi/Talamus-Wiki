---
type: glossary
tags: [information-theory, language-modeling, metrics]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#entropy
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Entropy

Measures how much information, on average, a single token carries in a language. Higher entropy = more information per token = more bits needed to represent each token = harder to predict.

Originated from Claude Shannon's 1951 paper "Prediction and Entropy of Printed English."

**Intuition**: A 2-token language (upper/lower) needs 1 bit per token → entropy = 1. A 4-token language (upper-left, upper-right, lower-left, lower-right) needs 2 bits → entropy = 2. More tokens = more expressive but harder to predict.

Entropy is the lower bound for [[Cross Entropy]]: a perfect language model achieves cross entropy equal to the data's entropy. Related to [[Perplexity]] via $PPL = 2^H$.
