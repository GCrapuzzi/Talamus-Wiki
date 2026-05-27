---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 062
section-title: Perplexity Interpretation and Use Cases
source-location: pages 146-148
previous-section: AI Space/normalized/pdf/ai-engineering/sections/061-perplexity.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/063-exact-evaluation.md
classification: reusable-knowledge-candidate
---
# Perplexity Interpretation and Use Cases

8 One reason many people might prefer natural log over log base 2 is because natural log has certain properties
that makes its math easier. For example, the derivative of natural log ln(x) is 1/x.
The perplexity of a language model (with the learned distribution Q) on this dataset
is defined as:
PPL (P, Q) = 2H (P ,Q)
If cross entropy measures how difficult it is for a model to predict the next token,
perplexity measures the amount of uncertainty it has when predicting the next token.
Higher uncertainty means there are more possible options for the next token.
Consider a language model trained to encode the 4 position tokens, as in Figure 3-4
(b), perfectly. The cross entropy of this language model is 2 bits. If this language
model tries to predict a position in the square, it has to choose among 2 = 4 possible
options. Thus, this language model has a perplexity of 4.
So far, I’ve been using bit as the unit for entropy and cross entropy. Each bit can rep‐
resent 2 unique values, hence the base of 2 in the preceding perplexity equation.
Popular ML frameworks, including TensorFlow and PyTorch, use nat (natural log) as
the unit for entropy and cross entropy. Nat uses the base of e, the base of natural log‐
arithm.8 If you use nat as the unit, perplexity is the exponential of e:
PPL (P, Q) = e H (P ,Q)
Due to the confusion around bit and nat, many people report perplexity, instead of
cross entropy, when reporting their language models’ performance.
Perplexity Interpretation and Use Cases
As discussed, cross entropy, perplexity, BPC, and BPB are variations of language
models’ predictive accuracy measurements. The more accurately a model can predict
a text, the lower these metrics are. In this book, I’ll use perplexity as the default
language modeling metric. Remember that the more uncertainty the model has in
predicting what comes next in a given dataset, the higher the perplexity.
What’s considered a good value for perplexity depends on the data itself and how
exactly perplexity is computed, such as how many previous tokens a model has access
to. Here are some general rules:
122 | Chapter 3: Evaluation Methodology

More structured data gives lower expected perplexity
More structured data is more predictable. For example, HTML code is more pre‐
dictable than everyday text. If you see an opening HTML tag like <head>, you
can predict that there should be a closing tag, </head>, nearby. Therefore, the
expected perplexity of a model on HTML code should be lower than the expected
perplexity of a model on everyday text.
The bigger the vocabulary, the higher the perplexity
Intuitively, the more possible tokens there are, the harder it is for the model to
predict the next token. For example, a model’s perplexity on a children’s book
will likely be lower than the same model’s perplexity on War and Peace. For the
same dataset, say in English, character-based perplexity (predicting the next
character) will be lower than word-based perplexity (predicting the next word),
because the number of possible characters is smaller than the number of possible
words.
The longer the context length, the lower the perplexity
The more context a model has, the less uncertainty it will have in predicting the
next token. In 1951, Claude Shannon evaluated his model’s cross entropy by
using it to predict the next token conditioned on up to 10 previous tokens. As of
this writing, a model’s perplexity can typically be computed and conditioned on
between 500 and 10,000 previous tokens, and possibly more, upperbounded by
the model’s maximum context length.
For reference, it’s not uncommon to see perplexity values as low as 3 or even lower. If
all tokens in a hypothetical language have an equal chance of happening, a perplexity
of 3 means that this model has a 1 in 3 chance of predicting the next token correctly.
Given that a model’s vocabulary is in the order of 10,000s and 100,000s, these odds
are incredible.
Other than guiding the training of language models, perplexity is useful in many
parts of an AI engineering workflow. First, perplexity is a good proxy for a model’s
capabilities. If a model’s bad at predicting the next token, its performance on down‐
stream tasks will also likely be bad. OpenAI’s GPT-2 report shows that larger models,
which are also more powerful models, consistently give lower perplexity on a range of
datasets, as shown in Table 3-1 . Sadly, following the trend of companies being
increasingly more secretive about their models, many have stopped reporting their
models’ perplexity.
Understanding Language Modeling Metrics | 123

9 If you’re unsure what SFT (supervised finetuning) and RLHF (reinforcement learning from human feedback)
mean, revisit Chapter 2.
10 Quantization is discussed in Chapter 7.
Table 3-1. Larger GPT-2 models consistently give lower perplexity on different datasets.
Source: OpenAI, 2018.
LAMBADA
(PPL)
LAMBADA
(ACC)
CBT-CN
(ACC)
CBT-NE
(ACC)
WikiText2
(PPL)
PTB
(PPL)
enwiki8
(BPB)
text8
(BPC)
WikiText103
(PBL)
IBW
(PPL)
SOTA 99.8 59.23 85.7 82.3 39.14 46.54 0.99 1.08 18.3 21.8
117M 35.13 45.99 87.65 83.4 29.41 65.85 1.16 1.17 37.50 75.20
345M 15.60 55.48 92.35 87.1 22.76 47.33 1.01 1.06 26.37 55.72
762M 10.87 60.12 93.45 88.0 19.93 40.31 0.97 1.02 22.05 44.575
1542M 8.63 63.24 93.30 89.05 18.34 35.76 0.93 0.98 17.48 42.16
Perplexity might not be a great proxy to evaluate models that have
been post-trained using techniques like SFT and RLHF. 9 Posttraining is about teaching models how to complete tasks. As a
model gets better at completing tasks, it might get worse at predict‐
ing the next tokens. A language model’s perplexity typically increa‐
ses after post-training. Some people say that post-training collapses
entropy. Similarly, quantization—a technique that reduces a
model’s numerical precision and, with it, its memory footprint—
can also change a model’s perplexity in unexpected ways. 10
Recall that the perplexity of a model with respect to a text measures how difficult it is
for this model to predict this text. For a given model, perplexity is the lowest for texts
that the model has seen and memorized during training. Therefore, perplexity can be
used to detect whether a text was in a model’s training data. This is useful for detect‐
ing data contamination—if a model’s perplexity on a benchmark’s data is low, this
benchmark was likely included in the model’s training data, making the model’s
performance on this benchmark less trustworthy. This can also be used for
deduplication of training data: e.g., add new data to the existing training dataset only
if the perplexity of the new data is high.
Perplexity is the highest for unpredictable texts, such as texts expressing unusual
ideas (like “my dog teaches quantum physics in his free time”) or gibberish (like
“home cat go eye”). Therefore, perplexity can be used to detect abnormal texts.
Perplexity and its related metrics help us understand the performance of the underly‐
ing language model, which is a proxy for understanding the model’s performance on
downstream tasks. The rest of the chapter discusses how to measure a model’s perfor‐
mance on downstream tasks directly.
124 | Chapter 3: Evaluation Methodology

[Visual content extracted via GLM-OCR]

Perplexity might not be a great proxy to evaluate models that have been post-trained using techniques like SFT and RLHF. Post-training is about teaching models how to complete tasks. As a model gets better at completing tasks, it might get worse at predicting the next tokens. A language model’s perplexity typically increases after post-training. Some people say that post-training collapses entropy. Similarly, quantization—a technique that reduces a model’s numerical precision and, with it, its memory footprint—can also change a model’s perplexity in unexpected ways.

Recall that the perplexity of a model with respect to a text measures how difficult it is for this model to predict this text. For a given model, perplexity is the lowest for texts that the model has seen and memorized during training. Therefore, perplexity can be used to detect whether a text was in a model’s training data. This is useful for detecting data contamination—if a model’s perplexity on a benchmark’s data is low, this benchmark was likely included in the model’s training data, making the model’s performance on this benchmark less trustworthy. This can also be used for deduplication of training data: e.g., add new data to the existing training dataset only if the perplexity of the new data is high.

Perplexity is the highest for unpredictable texts, such as texts expressing unusual ideas (like “my dog teaches quantum physics in his free time”) or gibberish (like “home cat go eye”). Therefore, perplexity can be used to detect abnormal texts.

Perplexity and its related metrics help us understand the performance of the underlying language model, which is a proxy for understanding the model’s performance on downstream tasks. The rest of the chapter discusses how to measure a model’s performance on downstream tasks directly.

9 If you’re unsure what SFT (supervised finetuning) and RLHF (reinforcement learning from human feedback) mean, revisit Chapter 2.

10 Quantization is discussed in Chapter 7.
