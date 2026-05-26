---
type: framework
tags: [post-training, SFT, RLHF, DPO, alignment, reward-model]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#post-training
  - AI Space/normalized/pdf/ai-engineering.md#supervised-finetuning
  - AI Space/normalized/pdf/ai-engineering.md#preference-finetuning
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Post-Training Pipeline

Two-step process to make pre-trained models safe, conversational, and aligned with human preferences.

**Step 1: Supervised Finetuning (SFT)**
- Trains on (prompt, response) demonstration data to shift model from completion to conversation
- Requires high-quality labelers (~90% college-educated for InstructGPT)
- Expensive: ~$10 per demonstration pair, ~30 min per complex sample
- Alternative: filter internet data for dialogue-like patterns (DeepMind's approach for Gopher)
- Growing use of AI-generated synthetic data to reduce annotation costs

**Step 2: Preference Finetuning**
- Aligns outputs with human preferences using comparison data (prompt, winning_response, losing_response)
- Comparison is easier/cheaper than absolute scoring (~$3.50 vs $25 per sample)
- Inter-labeler agreement: ~73%
- Techniques: RLHF (GPT-3.5, Llama 2), DPO (Llama 3), RLAIF (Claude)

**RLHF details**: train a reward model on comparison data, then optimize the foundation model via PPO to maximize reward scores.

**Post-training uses only ~2% of total compute** (InstructGPT). It unlocks capabilities already latent in the pre-trained model.

Some teams skip RL entirely, using **best-of-N** with a reward model (Stitch Fix, Grab).

See also: [[Supervised Finetuning]], [[Test Time Compute]].
