---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 129
section-title: Memory Bottlenecks
source-location: pages 343-343
previous-section: AI Space/normalized/pdf/ai-engineering/sections/128-finetuning-and-rag.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/130-backpropagation-and-trainable-parameters.md
classification: reusable-knowledge-candidate
---
# Memory Bottlenecks

doesn’t happen only in the beginning. It should be present during every step of the
process:
1. Try to get a model to perform your task with prompting alone. Use the prompt
engineering best practices covered in Chapter 5 , including systematically ver‐
sioning your prompts.
2. Add more examples to the prompt. Depending on the use case, the number of
examples needed might be between 1 and 50.
3. If your model frequently fails due to missing information, connect it to data
sources that can supply relevant information. When starting with RAG, begin by
using basic retrieval methods like term-based search. Even with simple retrieval,
adding relevant and accurate knowledge should lead to some improvement in
your model’s performance.
4. Depending on your model’s failure modes, you might explore one of these next
steps:
a. If the model continues having information-based failures, you might want to
try even more advanced RAG methods, such as embedding-based retrieval.
b. If the model continues having behavioral issues, such as it keeps generating
irrelevant, malformatted, or unsafe responses, you can opt for finetuning.
Embedding-based retrieval increases inference complexity by introducing
additional components into the pipeline, while finetuning increases the com‐
plexity of model development but leaves inference unchanged.
5. Combine both RAG and finetuning for even more performance boost.
If, after considering all the pros and cons of finetuning and other alternate tech‐
niques, you decide to finetune your model, the rest of the chapter is for you. First,
let’s look into the number one challenge of finetuning: its memory bottleneck.
Memory Bottlenecks
Because finetuning is memory-intensive, many finetuning techniques aim to mini‐
mize their memory footprint. Understanding what causes this memory bottleneck is
necessary to understand why and how these techniques work. This understanding, in
turn, can help you select a finetuning method that works best for you.
Besides explaining finetuning’s memory bottleneck, this section also introduces for‐
mulas for back-of-the-napkin calculation of the memory usage of each model. This
calculation is useful in estimating what hardware you’d need to serve or finetune a
model.
Memory Bottlenecks | 319
