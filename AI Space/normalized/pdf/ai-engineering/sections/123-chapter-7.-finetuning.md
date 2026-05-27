---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 123
section-title: Chapter 7. Finetuning
source-location: pages 331-331
previous-section: AI Space/normalized/pdf/ai-engineering/sections/122-summary.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/124-finetuning-overview.md
classification: reusable-knowledge-candidate
---
# Chapter 7. Finetuning

CHAPTER 7
Finetuning
Finetuning is the process of adapting a model to a specific task by further training the
whole model or part of the model. Chapters 5 and 6 discuss prompt-based methods,
which adapt a model by giving it instructions, context, and tools. Finetuning adapts a
model by adjusting its weights.
Finetuning can enhance various aspects of a model. It can improve the model’s
domain-specific capabilities, such as coding or medical question answering, and can
also strengthen its safety. However, it is most often used to improve the model’s
instruction-following ability, particularly to ensure it adheres to specific output styles
and formats.
While finetuning can help create models that are more customized to your needs, it
also requires more up-front investment. A question I hear very often is when to fine‐
tune and when to do RAG. After an overview of finetuning, this chapter will discuss
the reasons for finetuning and the reasons for not finetuning, as well as a simple
framework for thinking about choosing between finetuning and alternate methods.
Compared to prompt-based methods, finetuning incurs a much higher memory foot‐
print. At the scale of today’s foundation models, naive finetuning often requires more
memory than what’s available on a single GPU. This makes finetuning expensive and
challenging to do. As discussed throughout this chapter, reducing memory require‐
ments is a primary motivation for many finetuning techniques. This chapter dedi‐
cates one section to outlining factors contributing to a model’s memory footprint,
which is important for understanding these techniques.
A memory-efficient approach that has become dominant in the finetuning space is
PEFT (parameter-efficient finetuning). This chapter explores PEFT and how it differs
from traditional finetuning; this chapter also provides an overview of its evolving
