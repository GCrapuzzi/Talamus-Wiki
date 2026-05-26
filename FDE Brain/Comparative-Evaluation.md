---
type: framework
tags: [evaluation, model-selection, elo, bradley-terry, chatbot-arena, ranking]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#ranking-models-with-comparative-evaluation
  - AI Space/normalized/pdf/ai-engineering.md#challenges-of-comparative-evaluation
  - AI Space/normalized/pdf/ai-engineering.md#the-future-of-comparative-evaluation
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Comparative Evaluation

Rank models by having evaluators (human or AI) compare outputs pairwise, rather than scoring each model independently ([[AI as a Judge]] pointwise).

**Why comparative > pointwise for subjective tasks:**
- Easier to say "A is better than B" than to assign absolute scores
- As models surpass human ability, humans may still detect *differences* even when they can't score absolutely
- Harder to game than benchmark leaderboards (no reference data to train on)
- Never saturates as long as new models appear

**Process:**
1. For each query, two models generate responses
2. An evaluator picks the winner (ties optionally allowed)
3. A **rating algorithm** (Elo, Bradley–Terry, TrueSkill) computes rankings from match history
4. Ranking quality = predictive accuracy on future matches

LMSYS Chatbot Arena switched from Elo to Bradley–Terry because Elo was sensitive to evaluator/prompt ordering.

**Challenges:**
- **Quadratic scaling**: $n$ models → $\binom{n}{2}$ pairs. 57 models = 1,596 pairs. Mitigated by transitivity assumptions and smart matching algorithms that sample uncertainty-reducing matches.
- **Transitivity may not hold**: Human preference isn't necessarily transitive, and different pairs are evaluated by different people on different prompts.
- **Lack of standardization**: Crowdsourced evaluators may prefer fluent-but-wrong answers, use trivial prompts (0.55% of Arena prompts were just "hello"/"hi"), or lack domain expertise.
- **No absolute performance**: Knowing B beats A 51% of the time doesn't tell you if either model is *good enough*, or how win-rate translates to real-world task completion.
- **New model onboarding**: Each new model must be compared against existing models, potentially shifting all rankings.

**Not the same as A/B testing**: In A/B testing users see one option; in comparative evaluation they see both simultaneously.

Best used as a complement to benchmark evaluation and A/B testing, not a replacement.
