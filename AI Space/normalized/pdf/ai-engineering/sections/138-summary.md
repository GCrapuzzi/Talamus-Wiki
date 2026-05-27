---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 138
section-title: Summary
source-location: pages 385-386
previous-section: AI Space/normalized/pdf/ai-engineering/sections/137-finetuning-tactics.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/139-chapter-8.-dataset-engineering.md
classification: reusable-knowledge-candidate
---
# Summary

Prompt loss weight.    For instruction finetuning, each example consists of a prompt
and a response, both of which can contribute to the model’s loss during training.
During inference, however, prompts are usually provided by users, and the model
only needs to generate responses. Therefore, response tokens should contribute more
to the model’s loss during training than prompt tokens.
The prompt model weight determines how much prompts should contribute to this
loss compared to responses. If this weight is 100%, prompts contribute to the loss as
much as responses, meaning that the model learns equally from both. If this weight is
0%, the model learns only from responses. Typically, this weight is set to 10% by
default, meaning that the model should learn some from prompts but mostly from
responses.
Summary
Outside of the evaluation chapters, finetuning has been the most challenging chapter
to write. It touched on a wide range of concepts, both old (transfer learning) and new
(PEFT), fundamental (low-rank factorization) and experimental (model merging),
mathematical (memory calculation) and tactical (hyperparameter tuning). Arranging
all these different aspects into a coherent structure while keeping them accessible was
difficult.
The process of finetuning itself isn’t hard. Many finetuning frameworks handle the
training process for you. These frameworks can even suggest common finetuning
methods with sensible default hyperparameters.
However, the context surrounding finetuning is complex. It starts with whether you
should even finetune a model. This chapter started with the reasons for finetuning
and the reasons for not finetuning. It also discussed one question that I have been
asked many times: when to finetune and when to do RAG.
In its early days, finetuning was similar to pre-training—both involved updating the
model’s entire weights. However, as models increased in size, full finetuning became
impractical for most practitioners. The more parameters to update during finetuning,
the more memory finetuning needs. Most practitioners don’t have access to sufficient
resources (hardware, time, and data) to do full finetuning with foundation models.
Many finetuning techniques have been developed with the same motivation: to
achieve strong performance on a minimal memory footprint. For example, PEFT
reduces finetuning’s memory requirements by reducing the number of trainable
parameters. Quantized training, on the other hand, mitigates this memory bottleneck
by reducing the number of bits needed to represent each value.
After giving an overview of PEFT, the chapter zoomed into LoRA—why and how it
works. LoRA has many properties that make it popular among practitioners. On top
Summary | 361

of being parameter-efficient and data-efficient, it’s also modular, making it much eas‐
ier to serve and combine multiple LoRA models.
The idea of combining finetuned models brought the chapter to model merging; its
goal is to combine multiple models into one model that works better than these mod‐
els separately. This chapter discussed the many use cases of model merging, from ondevice deployment to model upscaling, and general approaches to model merging.
A comment I often hear from practitioners is that finetuning is easy, but getting data
for finetuning is hard. Obtaining high-quality annotated data, especially instruction
data, is challenging. The next chapter will dive into these challenges.
362 | Chapter 7: Finetuning
