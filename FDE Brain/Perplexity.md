---
type: glossary
tags: [evaluation, language-modeling, metrics, perplexity]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#perplexity
  - AI Space/normalized/pdf/ai-engineering.md#perplexity-interpretation-and-use-cases
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Perplexity

Perplexity (PPL) is the exponential of [[Cross Entropy]]. It measures the amount of uncertainty a language model has when predicting the next token.

$$PPL(P, Q) = 2^{H(P,Q)}$$

(or $e^{H(P,Q)}$ when using nats, as in PyTorch/TensorFlow).

A perplexity of 4 means the model is, on average, choosing among 4 equally likely options per token. Values as low as 3 are common for strong models—remarkable given vocabularies of 10k–100k tokens.

**Interpretation rules of thumb:**
- More structured data (e.g., HTML) → lower expected perplexity
- Bigger vocabulary → higher perplexity
- Longer context window → lower perplexity

**Practical uses beyond training:**
- **Data contamination detection**: Low perplexity on a benchmark suggests it appeared in training data
- **Training data deduplication**: Only add new data if its perplexity is high
- **Anomaly detection**: Gibberish and unusual text produce high perplexity
- **Model capability proxy**: Lower perplexity correlates with better downstream performance (GPT-2 scaling results confirm this)

**Caveats**: Perplexity typically *increases* after post-training (SFT/RLHF)—sometimes called "entropy collapse." [[Quantization]] can also shift perplexity unpredictably. Due to confusion between bit and nat units, many papers report perplexity instead of cross entropy.
