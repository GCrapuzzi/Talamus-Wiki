---
type: concept
tags: [bias, feedback, degenerate-loop, rlhf, data-quality]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#feedback-limitations
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Feedback Bias and Degenerate Feedback Loops

User feedback is valuable but systematically biased. Key biases:

- **Leniency bias** — users rate positively to avoid extra work or conflict. Uber average driver rating was 4.8/5; below 4.6 risked deactivation. Mitigation: replace numeric scales with descriptive options that reduce negative connotation.
- **Randomness** — unmotivated users click arbitrarily, especially on side-by-side comparisons of long responses.
- **Position bias** — users favour the first-presented option. Mitigate by randomising option order or modelling true success rate conditioned on position.
- **Length bias** — users prefer longer responses even when less accurate.
- **Recency bias** — users favour the last response seen in A/B comparisons.

### Degenerate feedback loops
When model predictions influence the feedback that trains the next model iteration, initial biases get amplified:
- **Exposure/popularity bias** — higher-ranked items get more clicks, reinforcing their rank (filter bubbles).
- **Audience capture** — small early signal (e.g., cat-photo preference) attracts like-minded users whose feedback further skews the model, narrowing the product's focus.
- **Sycophancy** — models trained on human feedback learn to tell users what they want to hear rather than what's accurate (Sharma et al., 2023).

Feedback is incomplete: you only get signal on what you show users. Before incorporating feedback into training, understand its biases and potential to distort the product.
