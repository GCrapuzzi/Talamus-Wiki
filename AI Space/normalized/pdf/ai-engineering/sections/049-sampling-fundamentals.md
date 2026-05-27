---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 049
section-title: Sampling Fundamentals
source-location: pages 112-113
previous-section: AI Space/normalized/pdf/ai-engineering/sections/048-sampling.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/050-sampling-strategies.md
classification: reusable-knowledge-candidate
---
# Sampling Fundamentals

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

For a language model, to generate the next token, the model first computes the prob‐
ability distribution over all tokens in the vocabulary, which looks like Figure 2-14.
Figure 2-14. To generate the next token, the language model first computes the proba‐
bility distribution over all tokens in the vocabulary.
When working with possible outcomes of different probabilities, a common strategy
is to pick the outcome with the highest probability. Always picking the most likely
outcome = is called greedy sampling . This often works for classification tasks. For
example, if the model thinks that an email is more likely to be spam than not spam, it
makes sense to mark it as spam. However, for a language model, greedy sampling
creates boring outputs. Imagine a model that, for whatever question you ask, always
responds with the most common words.
Instead of always picking the next most likely token, the model can sample the next
token according to the probability distribution over all possible values. Given the
context of “My favorite color is …” as shown in Figure 2-14 , if “red” has a 30%
chance of being the next token and “green” has a 50% chance, “red” will be picked
30% of the time, and “green” 50% of the time.
How does a model compute these probabilities? Given an input, a neural network
outputs a logit vector. Each logit corresponds to one possible value. In the case of a
language model, each logit corresponds to one token in the model’s vocabulary. The
logit vector size is the size of the vocabulary. A visualization of the logits vector is
shown in Figure 2-15.
Sampling | 89

[Visual content extracted via GLM-OCR]

For a language model, to generate the next token, the model first computes the probability distribution over all tokens in the vocabulary, which looks like Figure 2-14.

Figure 2-14. To generate the next token, the language model first computes the probability distribution over all tokens in the vocabulary.

When working with possible outcomes of different probabilities, a common strategy is to pick the outcome with the highest probability. Always picking the most likely outcome = is called greedy sampling. This often works for classification tasks. For example, if the model thinks that an email is more likely to be spam than not spam, it makes sense to mark it as spam. However, for a language model, greedy sampling creates boring outputs. Imagine a model that, for whatever question you ask, always responds with the most common words.

Instead of always picking the next most likely token, the model can sample the next token according to the probability distribution over all possible values. Given the context of “My favorite color is …” as shown in Figure 2-14, if “red” has a 30% chance of being the next token and “green” has a 50% chance, “red” will be picked 30% of the time, and “green” 50% of the time.

How does a model compute these probabilities? Given an input, a neural network outputs a logit vector. Each logit corresponds to one possible value. In the case of a language model, each logit corresponds to one token in the model’s vocabulary. The logit vector size is the size of the vocabulary. A visualization of the logits vector is shown in Figure 2-15.
