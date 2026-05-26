---
type: concept
tags: [model-collapse, synthetic-data, training-risk]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#ai-powered-data-synthesis
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Model Collapse

Recursive training on AI-generated data causes irreversible model degradation (Shumailov et al., 2023). Over iterations, probable events become over-represented while rare events vanish from the model's output distribution.

Observed in VAEs, Gaussian mixture models, and LLMs during both pre-training and post-training.

**Mitigation:** Model collapse is inevitable if training data is 100% synthetic, but can be avoided by mixing synthetic with real data (Gerstgrasser et al., 2024; Bertrand et al., 2023). No definitive optimal ratio exists yet.

**Counterpoint:** Some teams have scaled synthetic data to ~1M samples without saturation (Li et al., 2024 on math) and NVIDIA's Nemotron-4 used 98% synthetic data successfully—but these were single-iteration experiments.

**Related risk:** AI-generated data can amplify existing biases through feedback loops (Taori and Hashimoto, 2023). More faithful model outputs → more stable feedback loops → less bias amplification.
