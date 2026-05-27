---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 057
section-title: Understanding Language Modeling Metrics
source-location: pages 142-142
previous-section: AI Space/normalized/pdf/ai-engineering/sections/056-challenges-of-evaluating-foundation-models.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/058-entropy.md
classification: reusable-knowledge-candidate
---
# Understanding Language Modeling Metrics

6 While there’s a strong correlation, language modeling performance doesn’t fully explain downstream perfor‐
mance. This is an active area of research.
Figure 3-3. According to data sourced from my list of the 1,000 most popular AI reposi‐
tories on GitHub, evaluation lags behind other aspects of AI engineering in terms of
open source tools.
Understanding Language Modeling Metrics
Foundation models evolved out of language models. Many foundation models still
have language models as their main components. For these models, the performance
of the language model component tends to be well correlated to the foundation
model’s performance on downstream applications ( Liu et al., 2023 ). Therefore, a
rough understanding of language modeling metrics can be quite helpful in under‐
standing downstream performance.6
As discussed in Chapter 1, language modeling has been around for decades, popular‐
ized by Claude Shannon in his 1951 paper “Prediction and Entropy of Printed
English”. The metrics used to guide the development of language models haven’t
changed much since then. Most autoregressive language models are trained using
cross entropy or its relative, perplexity. When reading papers and model reports, you
might also come across bits-per-character (BPC) and bits-per-byte (BPB); both are
variations of cross entropy.
118 | Chapter 3: Evaluation Methodology

[Visual content extracted via GLM-OCR]

Understanding Language Modeling Metrics

Foundation models evolved out of language models. Many foundation models still have language models as their main components. For these models, the performance of the language model component tends to be well correlated to the foundation model’s performance on downstream applications (Liu et al., 2023). Therefore, a rough understanding of language modeling metrics can be quite helpful in understanding downstream performance.

As discussed in Chapter 1, language modeling has been around for decades, popularized by Claude Shannon in his 1951 paper “Prediction and Entropy of Printed English”. The metrics used to guide the development of language models haven’t changed much since then. Most autoregressive language models are trained using cross entropy or its relative, perplexity. When reading papers and model reports, you might also come across bits-per-character (BPC) and bits-per-byte (BPB); both are variations of cross entropy.

6 While there’s a strong correlation, language modeling performance doesn’t fully explain downstream performance. This is an active area of research.
