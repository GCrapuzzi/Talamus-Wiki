---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 059
section-title: Cross Entropy
source-location: pages 144-144
previous-section: AI Space/normalized/pdf/ai-engineering/sections/058-entropy.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/060-bits-per-character-and-bits-per-byte.md
classification: reusable-knowledge-candidate
---
# Cross Entropy

Figure 3-4. Two languages describe positions within a square. Compared to the lan‐
guage on the left (a), the tokens on the right (b) carry more information, but they need
more bits to represent them.
If your language has four tokens, shown as (b) in Figure 3-4, each token can give you
a more specific position: upper-left, upper-right, lower-left, or lower-right. However,
since there are now four tokens, you need two bits to represent them. The entropy of
this language is 2. This language has higher entropy, since each token carries more
information, but each token requires more bits to represent.
Intuitively, entropy measures how difficult it is to predict what comes next in a lan‐
guage. The lower a language’s entropy (the less information a token of a language
carries), the more predictable that language. In our previous example, the language
with only two tokens is easier to predict than the language with four (you have to
predict among only two possible tokens compared to four). This is similar to how, if
you can perfectly predict what I will say next, what I say carries no new information.
Cross Entropy
When you train a language model on a dataset, your goal is to get the model to learn
the distribution of this training data. In other words, your goal is to get the model to
predict what comes next in the training data. A language model’s cross entropy on a
dataset measures how difficult it is for the language model to predict what comes
next in this dataset.
A model’s cross entropy on the training data depends on two qualities:
1. The training data’s predictability, measured by the training data’s entropy
2. How the distribution captured by the language model diverges from the true dis‐
tribution of the training data
Entropy and cross entropy share the same mathematical notation, H. Let P be the
true distribution of the training data, and Q be the distribution learned by the lan‐
guage model. Accordingly, the following is true:
• The training data’s entropy is, therefore, H(P).
• The divergence of Q with respect to P can be measured using the Kullback–Lei‐
bler (KL) divergence, which is mathematically represented as DKL (P | | Q).
120 | Chapter 3: Evaluation Methodology

[Visual content extracted via GLM-OCR]

Figure 3-4. Two languages describe positions within a square. Compared to the language on the left (a), the tokens on the right (b) carry more information, but they need more bits to represent them.

If your language has four tokens, shown as (b) in Figure 3-4, each token can give you a more specific position: upper-left, upper-right, lower-left, or lower-right. However, since there are now four tokens, you need two bits to represent them. The entropy of this language is 2. This language has higher entropy, since each token carries more information, but each token requires more bits to represent.

Intuitively, entropy measures how difficult it is to predict what comes next in a language. The lower a language’s entropy (the less information a token of a language carries), the more predictable that language. In our previous example, the language with only two tokens is easier to predict than the language with four (you have to predict among only two possible tokens compared to four). This is similar to how, if you can perfectly predict what I will say next, what I say carries no new information.

Cross Entropy

When you train a language model on a dataset, your goal is to get the model to learn the distribution of this training data. In other words, your goal is to get the model to predict what comes next in the training data. A language model’s cross entropy on a dataset measures how difficult it is for the language model to predict what comes next in this dataset.

A model’s cross entropy on the training data depends on two qualities:

1. The training data’s predictability, measured by the training data’s entropy
2. How the distribution captured by the language model diverges from the true distribution of the training data

Entropy and cross entropy share the same mathematical notation, $H$. Let $P$ be the true distribution of the training data, and $Q$ be the distribution learned by the language model. Accordingly, the following is true:

- The training data’s entropy is, therefore, $H(P)$.
- The divergence of $Q$ with respect to $P$ can be measured using the Kullback–Leibler (KL) divergence, which is mathematically represented as $D_{KL}(P \mid Q)$.
