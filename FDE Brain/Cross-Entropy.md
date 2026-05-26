---
type: glossary
tags: [evaluation, language-modeling, metrics, information-theory]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#cross-entropy
  - AI Space/normalized/pdf/ai-engineering.md#bits-per-character-and-bits-per-byte
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Cross Entropy

Cross entropy $H(P, Q)$ measures how difficult it is for a language model (learned distribution $Q$) to predict the next token in a dataset (true distribution $P$).

$$H(P, Q) = H(P) + D_{KL}(P \| Q)$$

where $H(P)$ is the dataset's entropy (intrinsic unpredictability) and $D_{KL}(P \| Q)$ is the KL divergence between the true and learned distributions.

Key properties:
- Cross entropy is **not symmetric**: $H(P,Q) \neq H(Q,P)$
- A perfectly trained model achieves $H(P,Q) = H(P)$ (KL divergence goes to zero)
- Cross entropy is the primary training objective for autoregressive language models

Related metrics that are interconvertible given necessary information:
- **Bits-per-character (BPC)**: cross entropy normalized by average characters per token
- **Bits-per-byte (BPB)**: cross entropy normalized by bytes—more standardized across character encodings
- **[[Perplexity]]**: $2^{H(P,Q)}$ (exponential of cross entropy)

Cross entropy also quantifies compression efficiency: a BPB of 3.43 means the model can compress text to less than half its original size.
