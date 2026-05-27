---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 060
section-title: Bits-per-Character and Bits-per-Byte
source-location: pages 145-145
previous-section: AI Space/normalized/pdf/ai-engineering/sections/059-cross-entropy.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/061-perplexity.md
classification: reusable-knowledge-candidate
---
# Bits-per-Character and Bits-per-Byte

• The model’s cross entropy with respect to the training data is therefore:
H (P, Q) = H (P) + DKL (P | | Q).
Cross entropy isn’t symmetric. The cross entropy of Q with respect to P— H(P, Q)—is
different from the cross entropy of P with respect to Q— H(Q, P).
A language model is trained to minimize its cross entropy with respect to the training
data. If the language model learns perfectly from its training data, the model’s cross
entropy will be exactly the same as the entropy of the training data. The KL diver‐
gence of Q with respect to P will then be 0. You can think of a model’s cross entropy
as its approximation of the entropy of its training data.
Bits-per-Character and Bits-per-Byte
One unit of entropy and cross entropy is bits. If the cross entropy of a language
model is 6 bits, this language model needs 6 bits to represent each token.
Since different models have different tokenization methods—for example, one model
uses words as tokens and another uses characters as tokens—the number of bits per
token isn’t comparable across models. Some use the number of bits-per-character
(BPC) instead. If the number of bits per token is 6 and on average, each token con‐
sists of 2 characters, the BPC is 6/2 = 3.
One complication with BPC arises from different character encoding schemes. For
example, with ASCII, each character is encoded using 7 bits, but with UTF-8, a char‐
acter can be encoded using anywhere between 8 and 32 bits. A more standardized
metric would be bits-per-byte (BPB), the number of bits a language model needs to
represent one byte of the original training data. If the BPC is 3 and each character is 7
bits, or ⅞ of a byte, then the BPB is 3 / (⅞) = 3.43.
Cross entropy tells us how efficient a language model will be at compressing text. If
the BPB of a language model is 3.43, meaning it can represent each original byte (8
bits) using 3.43 bits, this language model can compress the original training text to
less than half the text’s original size.
Perplexity
Perplexity is the exponential of entropy and cross entropy. Perplexity is often short‐
ened to PPL. Given a dataset with the true distribution P, its perplexity is defined as:
PPL (P) = 2H (P )
Understanding Language Modeling Metrics | 121
