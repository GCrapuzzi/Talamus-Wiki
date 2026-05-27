---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 134
section-title: Finetuning Techniques
source-location: pages 356-356
previous-section: AI Space/normalized/pdf/ai-engineering/sections/133-quantization.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/135-parameter-efficient-finetuning.md
classification: reusable-knowledge-candidate
---
# Finetuning Techniques

21 Personal anecdote: much of my team’s work at NVIDIA was on mixed precision training. See “Mixed Preci‐
sion Training for NLP and Speech Recognition with OpenSeq2Seq”  (Huyen et al., NVIDIA Developer Tech‐
nical Blog, October 2018).
are kept in lower precision.21 You can also have less-sensitive weight values computed
in lower precision and more-sensitive weight values computed in higher precision.
For example, LLM-QAT ( Liu et al., 2023 ) quantizes weights and activations into 4
bits but keeps embeddings in 16 bits.
The portions of the model that should be in lower precision can be set automatically
using the automatic mixed precision (AMP) functionality offered by many ML frame‐
works.
It’s also possible to have different phases of training in different precision levels. For
example, a model can be trained in higher precision but finetuned in lower precision.
This is especially common with foundation models, where the team training a model
from scratch might be an organization with sufficient compute for higher precision
training. Once the model is published, developers with less compute access can fine‐
tune that model in lower precision.
Finetuning Techniques
I hope that the previous section has made clear why finetuning large-scale models is
so memory-intensive. The more memory finetuning requires, the fewer people who
can afford to do it. Techniques that reduce a model’s memory footprint make fine‐
tuning more accessible, allowing more people to adapt models to their applications.
This section focuses on memory-efficient finetuning techniques, which centers
around parameter-efficient finetuning.
I’ll also cover model merging, an exciting but more experimental approach to creat‐
ing custom models. While model merging is generally not considered finetuning, I
include it in this section because it’s complementary to finetuning. Finetuning tailors
one model to specific needs. Model merging combines multiple models, often fine‐
tuned models, for the same purpose.
While combining multiple models isn’t a new concept, new types of models and fine‐
tuning techniques have inspired many creative model-merging techniques, making
this section especially fun to write about.
Parameter-Efficient Finetuning
In the early days of finetuning, models were small enough that people could finetune
entire models. This approach is called full finetuning. In full finetuning, the number
of trainable parameters is exactly the same as the number of parameters.
332 | Chapter 7: Finetuning
