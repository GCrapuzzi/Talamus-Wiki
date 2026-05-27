---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 125
section-title: When to Finetune
source-location: pages 335-335
previous-section: AI Space/normalized/pdf/ai-engineering/sections/124-finetuning-overview.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/126-reasons-to-finetune.md
classification: reusable-knowledge-candidate
---
# When to Finetune

Figure 7-1. Different finetuning techniques used to make different Code Llama models.
Image from the Rozière et al. (2024). Adapted from an original image licensed under
CC BY 4.0.
As an application developer, you might finetune a pre-trained model, but most likely,
you’ll finetune a model that has been post-trained. The more refined a model is and
the more relevant its knowledge is to your task, the less work you’ll have to do to
adapt it.
When to Finetune
Before jumping into different finetuning techniques, it’s necessary to consider
whether finetuning is the right option for you. Compared to prompt-based methods,
finetuning requires significantly more resources, not just in data and hardware, but
also in ML talent. Therefore, finetuning is generally attempted after extensive experi‐
ments with prompt-based methods. However, finetuning and prompting aren’t
mutually exclusive. Real-world problems often require both approaches.
Reasons to Finetune
The primary reason for finetuning is to improve a model’s quality, in terms of both
general capabilities and task-specific capabilities. Finetuning is commonly used to
improve a model’s ability to generate outputs following specific structures, such as
JSON or YAML formats.
A general-purpose model that performs well on a wide range of benchmarks might
not perform well on your specific task. If the model you want to use wasn’t suffi‐
ciently trained on your task, finetuning it with your data can be especially useful.
For example, an out-of-the-box model might be good at converting from text to the
standard SQL dialect but might fail with a less common SQL dialect. In this case,
finetuning this model on data containing this SQL dialect will help. Similarly, if the
model works well on standard SQL for common queries but often fails for customerspecific queries, finetuning the model on customer-specific queries might help.
When to Finetune | 311

[Visual content extracted via GLM-OCR]

As an application developer, you might finetune a pre-trained model, but most likely, you’ll finetune a model that has been post-trained. The more refined a model is and the more relevant its knowledge is to your task, the less work you’ll have to do to adapt it.

When to Finetune

Before jumping into different finetuning techniques, it’s necessary to consider whether finetuning is the right option for you. Compared to prompt-based methods, finetuning requires significantly more resources, not just in data and hardware, but also in ML talent. Therefore, finetuning is generally attempted after extensive experiments with prompt-based methods. However, finetuning and prompting aren’t mutually exclusive. Real-world problems often require both approaches.

Reasons to Finetune

The primary reason for finetuning is to improve a model’s quality, in terms of both general capabilities and task-specific capabilities. Finetuning is commonly used to improve a model’s ability to generate outputs following specific structures, such as JSON or YAML formats.

A general-purpose model that performs well on a wide range of benchmarks might not perform well on your specific task. If the model you want to use wasn’t sufficiently trained on your task, finetuning it with your data can be especially useful.

For example, an out-of-the-box model might be good at converting from text to the standard SQL dialect but might fail with a less common SQL dialect. In this case, finetuning this model on data containing this SQL dialect will help. Similarly, if the model works well on standard SQL for common queries but often fails for customer-specific queries, finetuning the model on customer-specific queries might help.
