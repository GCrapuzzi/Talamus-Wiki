---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 058
section-title: Entropy
source-location: pages 143-143
previous-section: AI Space/normalized/pdf/ai-engineering/sections/057-understanding-language-modeling-metrics.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/059-cross-entropy.md
classification: reusable-knowledge-candidate
---
# Entropy

7 As discussed in Chapter 1, a token can be a character, a word, or part of a word. When Claude Shannon intro‐
duced entropy in 1951, the tokens he worked with were characters. Here’s entropy in his own words: “ The
entropy is a statistical parameter which measures, in a certain sense, how much information is produced on
the average for each letter of a text in the language. If the language is translated into binary digits (0 or 1) in
the most efficient way, the entropy is the average number of binary digits required per letter of the original
language.”
All four metrics—cross entropy, perplexity, BPC, and BPB—are closely related. If you
know the value of one, you can compute the other three, given the necessary infor‐
mation. While I refer to them as language modeling metrics, they can be used for any
model that generates sequences of tokens, including non-text tokens.
Recall that a language model encodes statistical information (how likely a token is to
appear in a given context) about languages. Statistically, given the context “I like
drinking __”, the next word is more likely to be “tea” than “charcoal”. The more stat‐
istical information that a model can capture, the better it is at predicting the next
token.
In ML lingo, a language model learns the distribution of its training data. The better
this model learns, the better it is at predicting what comes next in the training data,
and the lower its training cross entropy. As with any ML model, you care about its
performance not just on the training data but also on your production data. In gen‐
eral, the closer your data is to a model’s training data, the better the model can per‐
form on your data.
Compared to the rest of the book, this section is math-heavy. If you find it confusing,
feel free to skip the math part and focus on the discussion of how to interpret these
metrics. Even if you’re not training or finetuning language models, understanding
these metrics can help with evaluating which models to use for your application.
These metrics can occasionally be used for certain evaluation and data deduplication
techniques, as discussed throughout this book.
Entropy
Entropy measures how much information, on average, a token carries. The higher the
entropy, the more information each token carries, and the more bits are needed to
represent a token.7
Let’s use a simple example to illustrate this. Imagine you want to create a language to
describe positions within a square, as shown in Figure 3-4. If your language has only
two tokens, shown as (a) in Figure 3-4, each token can tell you whether the position is
upper or lower. Since there are only two tokens, one bit is sufficient to represent
them. The entropy of this language is, therefore, 1.
Understanding Language Modeling Metrics | 119
