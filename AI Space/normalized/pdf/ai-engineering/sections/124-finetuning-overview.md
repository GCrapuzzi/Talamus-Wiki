---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 124
section-title: Finetuning Overview
source-location: pages 332-334
previous-section: AI Space/normalized/pdf/ai-engineering/sections/123-chapter-7.-finetuning.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/125-when-to-finetune.md
classification: reusable-knowledge-candidate
---
# Finetuning Overview

techniques. I’ll focus particularly on one compelling category: adapter-based
techniques.
With prompt-based methods, knowledge about how ML models operate under the
hood is recommended but not strictly necessary. However, finetuning brings you to
the realm of model training, where ML knowledge is required. ML basics are beyond
the scope of this book. If you want a quick refresh, the book’s GitHub repository has
pointers to helpful resources. In this chapter, I’ll cover a few core concepts immedi‐
ately relevant to the discussion.
This chapter is the most technically challenging one for me to write, not because of
the complexity of the concepts, but because of the broad scope these concepts cover. I
suspect it might also be technically challenging to read. If, at any point, you feel like
you’re diving too deep into details that aren’t relevant to your work, feel free to skip.
There’s a lot to discuss. Let’s dive in!
Finetuning Overview
To finetune, you start with a base model that has some, but not all, of the capabilities
you need. The goal of finetuning is to get this model to perform well enough for your
specific task.
Finetuning is one way to do transfer learning, a concept first introduced by Bozinov‐
ski and Fulgosi  in 1976. Transfer learning focuses on how to transfer the knowledge
gained from one task to accelerate learning for a new, related task. This is conceptu‐
ally similar to how humans transfer skills: for example, knowing how to play the
piano can make it easier to learn another musical instrument.
An early large-scale success in transfer learning was Google’s multilingual translation
system ( Johnson et. al, 2016 ). The model transferred its knowledge of Portuguese–
English and English–Spanish translation to directly translate Portuguese to Spanish,
even though there were no Portuguese–Spanish examples in the training data.
Since the early days of deep learning, transfer learning has offered a solution for tasks
with limited or expensive training data. By training a base model on tasks with abun‐
dant data, you can then transfer that knowledge to a target task.
For LLMs, knowledge gained from pre-training on text completion (a task with
abundant data) is transferred to more specialized tasks, like legal question answering
or text-to-SQL, which often have less available data. This capability for transfer learn‐
ing makes foundation models particularly valuable.
308 | Chapter 7: Finetuning

Transfer learning improves sample efficiency , allowing a model to learn the same
behavior with fewer examples. A sample-efficient model learns effectively from fewer
samples. For example, while training a model from scratch for legal question answer‐
ing may need millions of examples, finetuning a good base model might only require
a few hundred.
Ideally, much of what the model needs to learn is already present in the base model,
and finetuning just refines the model’s behavior. OpenAI’s InstructGPT paper (2022)
suggested viewing finetuning as unlocking the capabilities a model already has but
that are difficult for users to access via prompting alone.
Finetuning isn’t the only way to do transfer learning. Another
approach is feature-based transfer . In this approach, a model is
trained to extract features from the data, usually as embedding vec‐
tors, which are then used by another model. I mention featurebased transfer briefly in Chapter 2, when discussing how part of a
foundation model can be reused for a classification task by adding
a classifier head.
Feature-based transfer is very common in computer vision. For
instance, in the second half of the 2010s, many people used models
trained on the ImagetNet dataset to extract features from images
and use these features in other computer vision tasks such as object
detection or image segmentation.
Finetuning is part of a model’s training process. It’s an extension of model pretraining. Because any training that happens after pre-training is finetuning, finetun‐
ing can take many different forms. Chapter 2  already discussed two types of
finetuning: supervised finetuning and preference finetuning. Let’s do a quick recap of
these methods and how you might leverage them as an application developer.
Recall that a model’s training process starts with pre-training, which is usually done
with self-supervision. Self-supervision allows the model to learn from a large amount
of unlabeled data. For language models, self-supervised data is typically just sequences
of text that don’t need annotations.
Before finetuning this pre-trained model with expensive task-specific data, you can
finetune it with self-supervision using cheap task-related data. For example, to fine‐
tune a model for legal question answering, before finetuning it on expensive annota‐
ted (question, answer) data, you can finetune it on raw legal documents. Similarly, to
finetune a model to do book summarization in Vietnamese, you can first finetune it
on a large collection of Vietnamese text. Self-supervised finetuning is also called con‐
tinued pre-training.
Finetuning Overview | 309

[Visual content extracted via GLM-OCR]

Transfer learning improves sample efficiency, allowing a model to learn the same behavior with fewer examples. A sample-efficient model learns effectively from fewer samples. For example, while training a model from scratch for legal question answering may need millions of examples, finetuning a good base model might only require a few hundred.

Ideally, much of what the model needs to learn is already present in the base model, and finetuning just refines the model’s behavior. OpenAI’s InstructGPT paper (2022) suggested viewing finetuning as unlocking the capabilities a model already has but that are difficult for users to access via prompting alone.

Finetuning isn’t the only way to do transfer learning. Another approach is feature-based transfer. In this approach, a model is trained to extract features from the data, usually as embedding vectors, which are then used by another model. I mention feature-based transfer briefly in Chapter 2, when discussing how part of a foundation model can be reused for a classification task by adding a classifier head.

Feature-based transfer is very common in computer vision. For instance, in the second half of the 2010s, many people used models trained on the ImagetNet dataset to extract features from images and use these features in other computer vision tasks such as object detection or image segmentation.

Finetuning is part of a model’s training process. It’s an extension of model pre-training. Because any training that happens after pre-training is finetuning, finetuning can take many different forms. Chapter 2 already discussed two types of finetuning: supervised finetuning and preference finetuning. Let’s do a quick recap of these methods and how you might leverage them as an application developer.

Recall that a model’s training process starts with pre-training, which is usually done with self-supervision. Self-supervision allows the model to learn from a large amount of unlabeled data. For language models, self-supervised data is typically just sequences of text that don’t need annotations.

Before finetuning this pre-trained model with expensive task-specific data, you can finetune it with self-supervision using cheap task-related data. For example, to finetune a model for legal question answering, before finetuning it on expensive annotated (question, answer) data, you can finetune it on raw legal documents. Similarly, to finetune a model to do book summarization in Vietnamese, you can first finetune it on a large collection of Vietnamese text. Self-supervised finetuning is also called continued pre-training.

As discussed in Chapter 1 , language models can be autoregressive or masked. An
autoregressive model predicts the next token in a sequence using the previous tokens
as the context. A masked model fills in the blank using the tokens both before and
after it. Similarly, with supervised finetuning, you can also finetune a model to pre‐
dict the next token or fill in the blank. The latter, also known as infilling finetuning, is
especially useful for tasks such as text editing and code debugging. You can finetune a
model for infilling even if it was pre-trained autoregressively.
The massive amount of data a model can learn from during self-supervised learning
outfits the model with a rich understanding of the world, but it might be hard for
users to extract that knowledge for their tasks, or the way the model behaves might be
misaligned with human preference. Supervised finetuning uses high-quality annota‐
ted data to refine the model to align with human usage and preference.
During supervised finetuning , the model is trained using (input, output) pairs: the
input can be an instruction and the output can be a response. A response can be
open-ended, such as for the task of book summarization. A response can be also
close-ended, such as for a classification task. High-quality instruction data can be
challenging and expensive to create, especially for instructions that require factual
consistency, domain expertise, or political correctness. Chapter 8  discusses how to
acquire instruction data.
A model can also be finetuned with reinforcement learning to generate responses that
maximize human preference. Preference finetuning requires comparative data that
typically follows the format (instruction, winning response, losing response).
It’s possible to finetune a model to extend its context length. Long-context finetuning
typically requires modifying the model’s architecture, such as adjusting the positional
embeddings. A long sequence means more possible positions for tokens, and posi‐
tional embeddings should be able to handle them. Compared to other finetuning
techniques, long-context finetuning is harder to do. The resulting model might also
degrade on shorter sequences.
Figure 7-1 shows the making of different Code Llama models ( Rozière et al., 2024 ),
from the base model Llama 2, using different finetuning techniques. Using longcontext finetuning, they were able to increase the model’s maximum context length
from 4,096 tokens to 16,384 tokens to accommodate longer code files. In the image,
instruction finetuning refers to supervised finetuning.
Finetuning can be done by both model developers and application developers. Model
developers typically post-train a model with different finetuning techniques before
releasing it. A model developer might also release different model versions, each fine‐
tuned to a different extent, so that application developers can choose the version that
works best for them.
310 | Chapter 7: Finetuning
