---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 063
section-title: Exact Evaluation
source-location: pages 149-149
previous-section: AI Space/normalized/pdf/ai-engineering/sections/062-perplexity-interpretation-and-use-cases.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/064-functional-correctness.md
classification: reusable-knowledge-candidate
---
# Exact Evaluation

How to Use a Language Model to Compute a Text’s Perplexity
A model’s perplexity with respect to a text measures how difficult it is for the model
to predict that text. Given a language model X, and a sequence of tokens
x1, x2, ..., xn , X’s perplexity for this sequence is:
P(x1, x2, ..., xn)
-
n = (
P (x1, x2, â¦, xn) )
n = (∏ i=1
n 1
P (xi | x1, ..., xi -1) )
n
where P(xi | x1, ..., xi-1) denotes the probability that X assigns to the token xi given
the previous tokens x1, ..., xi-1.
To compute perplexity, you need access to the probabilities (or logprobs) the lan‐
guage model assigns to each next token. Unfortunately, not all commercial models
expose their models’ logprobs, as discussed in Chapter 2.
Exact Evaluation
When evaluating models’ performance, it’s important to differentiate between exact
and subjective evaluation. Exact evaluation produces judgment without ambiguity.
For example, if the answer to a multiple-choice question is A and you pick B, your
answer is wrong. There’s no ambiguity around that. On the other hand, essay grading
is subjective. An essay’s score depends on who grades the essay. The same person, if
asked twice some time apart, can give the same essay different scores. Essay grading
can become more exact with clear grading guidelines. As you’ll see in the next sec‐
tion, AI as a judge is subjective. The evaluation result can change based on the judge
model and the prompt.
I’ll cover two evaluation approaches that produce exact scores: functional correctness
and similarity measurements against reference data. Note that this section focuses
on evaluating open-ended responses (arbitrary text generation) as opposed to
close-ended responses (such as classification). This is not because foundation models
aren’t being used for close-ended tasks. In fact, many foundation model systems have
at least a classification component, typically for intent classification or scoring. This
section focuses on open-ended evaluation because close-ended evaluation is already
well understood.
Exact Evaluation | 125
