---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 048
section-title: Sampling
source-location: pages 112-112
previous-section: AI Space/normalized/pdf/ai-engineering/sections/047-preference-finetuning.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/049-sampling-fundamentals.md
classification: reusable-knowledge-candidate
---
# Sampling

Empirically, RLHF and DPO both improve performance compared to SFT alone.
However, as of this writing, there are debates on why they work. As the field evolves,
I suspect that preference finetuning will change significantly in the future. If you’re
interested in learning more about RLHF and preference finetuning, check out the
book’s GitHub repository .
Both SFT and preference finetuning are steps taken to address the problem created
by the low quality of data used for pre-training. If one day we have better pre-training
data or better ways to train foundation models, we might not need SFT and prefer‐
ence at all.
Some companies find it okay to skip reinforcement learning altogether. For example,
Stitch Fix and Grab find that having the reward model alone is good enough for their
applications. They get their models to generate multiple outputs and pick the ones
given high scores by their reward models. This approach, often referred to as the best
of N  strategy, leverages how a model samples outputs to improve its performance.
The next section will shed light on how best of N works.
Sampling
A model constructs its outputs through a process known as sampling. This section
discusses different sampling strategies and sampling variables, including temperature,
top-k, and top-p. It’ll then explore how to sample multiple outputs to improve a
model’s performance. We’ll also see how the sampling process can be modified to get
models to generate responses that follow certain formats and constraints.
Sampling makes AI’s outputs probabilistic. Understanding this probabilistic nature is
important for handling AI’s behaviors, such as inconsistency and hallucination. This
section ends with a deep dive into what this probabilistic nature means and how to
work with it.
Sampling Fundamentals
Given an input, a neural network produces an output by first computing the proba‐
bilities of possible outcomes. For a classification model, possible outcomes are the
available classes. As an example, if a model is trained to classify whether an email is
spam or not, there are only two possible outcomes: spam and not spam. The model
computes the probability of each of these two outcomes—e.g., the probability of the
email being spam is 90%, and not spam is 10%. You can then make decisions based
on these output probabilities. For example, if you decide that any email with a spam
probability higher than 50% should be marked as spam, an email with a 90% spam
probability will be marked as spam.
88 | Chapter 2: Understanding Foundation Models
