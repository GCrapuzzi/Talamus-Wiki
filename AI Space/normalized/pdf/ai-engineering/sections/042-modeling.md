---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 042
section-title: Modeling
source-location: pages 82-82
previous-section: AI Space/normalized/pdf/ai-engineering/sections/041-domain-specific-models.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/043-model-architecture.md
classification: reusable-knowledge-candidate
---
# Modeling

5 ML fundamentals related to model training are outside the scope of this book. However, when relevant to the
discussion, I include some concepts. For example, self-supervision—where a model generates its own labels
from the data—is covered in Chapter 1, and backpropagation—how a model’s parameters are updated during
training based on the error—is discussed in Chapter 7.
Modeling
Before training a model, developers need to decide what the model should look like.
What architecture should it follow? How many parameters should it have? These
decisions impact not only the model’s capabilities but also its usability for
downstream applications.5 For example, a 7B-parameter model will be vastly easier to
deploy than a 175B-parameter model. Similarly, optimizing a transformer model for
latency is very different from optimizing another architecture. Let’s explore the fac‐
tors behind these decisions.
Model Architecture
As of this writing, the most dominant architecture for language-based foundation
models is the transformer architecture ( Vaswani et al., 2017 ), which is based on the
attention mechanism. It addresses many limitations of the previous architectures,
which contributed to its popularity. However, the transformer architecture has its
own limitations. This section analyzes the transformer architecture and its alterna‐
tives. Because it goes into the technical details of different architectures, it can be
technically dense. If you find any part too deep in the weeds, feel free to skip it.
Transformer architecture
To understand the transformer, let’s look at the problem it was created to solve. The
transformer architecture was popularized on the heels of the success of the seq2seq
(sequence-to-sequence) architecture. At the time of its introduction in 2014, seq2seq
provided significant improvement on then-challenging tasks: machine translation
and summarization. In 2016, Google incorporated seq2seq into Google Translate , an
update that they claimed to have given them the “largest improvements to date for
machine translation quality”. This generated a lot of interest in seq2seq, making it the
go-to architecture for tasks involving sequences of text.
At a high level, seq2seq contains an encoder that processes inputs and a decoder that
generates outputs. Both inputs and outputs are sequences of tokens, hence the name.
Seq2seq uses RNNs (recurrent neural networks) as its encoder and decoder. In its
most basic form, the encoder processes the input tokens sequentially, outputting the
final hidden state that represents the input. The decoder then generates output
tokens sequentially, conditioned on both the final hidden state of the input and the
previously generated token. A visualization of the seq2seq architecture is shown in
the top half of Figure 2-4.
58 | Chapter 2: Understanding Foundation Models
