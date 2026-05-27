---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 045
section-title: Post-Training
source-location: pages 102-103
previous-section: AI Space/normalized/pdf/ai-engineering/sections/044-model-size.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/046-supervised-finetuning.md
classification: reusable-knowledge-candidate
---
# Post-Training

21 A friend used this analogy: a pre-trained model talks like a web page, not a human.
22 RL fundamentals are beyond the scope of this book, but the highlight is that RL lets you optimize against
difficult objectives like human preference.
Post-Training
Post-training starts with a pre-trained model. Let’s say that you’ve pre-trained a
foundation model using self-supervision. Due to how pre-training works today, a
pre-trained model typically has two issues. First, self-supervision optimizes the model
for text completion, not conversations.21 If you find this unclear, don’t worry, “Super‐
vised Finetuning” on page 80 will have examples. Second, if the model is pre-trained
on data indiscriminately scraped from the internet, its outputs can be racist, sexist,
rude, or just wrong. The goal of post-training is to address both of these issues.
Every model’s post-training is different. However, in general, post-training consists
of two steps:
1. Supervised finetuning  (SFT): Finetune the pre-trained model on high-quality
instruction data to optimize models for conversations instead of completion.
2. Preference finetuning: Further finetune the model to output responses that align
with human preference. Preference finetuning is typically done with reinforce‐
ment learning (RL). 22 Techniques for preference finetuning include reinforce‐
ment learning from human feedback  (RLHF) (used by GPT-3.5 and Llama 2 ),
DPO (Direct Preference Optimization) (used by Llama 3 ), and reinforcement
learning from AI feedback (RLAIF) (potentially used by Claude).
Let me highlight the difference between pre-training and post-training another way.
For language-based foundation models, pre-training optimizes token-level quality,
where the model is trained to predict the next token accurately. However, users don’t
care about token-level quality—they care about the quality of the entire response.
Post-training, in general, optimizes the model to generate responses that users prefer.
Some people compare pre-training to reading to acquire knowledge, while posttraining is like learning how to use that knowledge.
Watch out for terminology ambiguity. Some people use the term
instruction finetuning to refer to supervised finetuning, while some
other people use this term to refer to both supervised finetuning
and preference finetuning. To avoid ambiguity, I will avoid the
term instruction finetuning in this book.
As post-training consumes a small portion of resources compared to pre-training
(InstructGPT used only 2% of compute for post-training and 98% for pre-training),
78 | Chapter 2: Understanding Foundation Models

[Visual content extracted via GLM-OCR]

Post-Training

Post-training starts with a pre-trained model. Let’s say that you’ve pre-trained a foundation model using self-supervision. Due to how pre-training works today, a pre-trained model typically has two issues. First, self-supervision optimizes the model for text completion, not conversations. If you find this unclear, don’t worry, “Supervised Finetuning” on page 80 will have examples. Second, if the model is pre-trained on data indiscriminately scraped from the internet, its outputs can be racist, sexist, rude, or just wrong. The goal of post-training is to address both of these issues.

Every model’s post-training is different. However, in general, post-training consists of two steps:

1. Supervised finetuning (SFT): Finetune the pre-trained model on high-quality instruction data to optimize models for conversations instead of completion.

2. Preference finetuning: Further finetune the model to output responses that align with human preference. Preference finetuning is typically done with reinforcement learning (RL). Techniques for preference finetuning include reinforcement learning from human feedback (RLHF) (used by GPT-3.5 and Llama 2), DPO (Direct Preference Optimization) (used by Llama 3), and reinforcement learning from AI feedback (RLAIF) (potentially used by Claude).

Let me highlight the difference between pre-training and post-training another way. For language-based foundation models, pre-training optimizes token-level quality, where the model is trained to predict the next token accurately. However, users don’t care about token-level quality—they care about the quality of the entire response. Post-training, in general, optimizes the model to generate responses that users prefer. Some people compare pre-training to reading to acquire knowledge, while post-training is like learning how to use that knowledge.

Watch out for terminology ambiguity. Some people use the term instruction finetuning to refer to supervised finetuning, while some other people use this term to refer to both supervised finetuning and preference finetuning. To avoid ambiguity, I will avoid the term instruction finetuning in this book.

As post-training consumes a small portion of resources compared to pre-training (InstructGPT used only 2% of compute for post-training and 98% for pre-training),

21 A friend used this analogy: a pre-trained model talks like a web page, not a human.

22 RL fundamentals are beyond the scope of this book, but the highlight is that RL lets you optimize against difficult objectives like human preference.

you can think of post-training as unlocking the capabilities that the pre-trained
model already has but are hard for users to access via prompting alone.
Figure 2-10 shows the overall workflow of pre-training, SFT, and preference finetun‐
ing, assuming you use RLHF for the last step. You can approximate how well a model
aligns with human preference by determining what steps the model creators have
taken.
Figure 2-10. The overall training workflow with pre-training, SFT, and RLHF.
If you squint, Figure 2-10  looks very similar to the meme depicting the monster
Shoggoth with a smiley face in Figure 2-11:
1. Self-supervised pre-training results in a rogue model that can be considered an
untamed monster because it uses indiscriminate data from the internet.
2. This monster is then supervised finetuned on higher-quality data—Stack Over‐
flow, Quora, or human annotations—which makes it more socially acceptable.
3. This finetuned model is further polished using preference finetuning to make it
customer-appropriate, which is like giving it a smiley face.
Post-Training | 79

[Visual content extracted via GLM-OCR]

you can think of post-training as unlocking the capabilities that the pre-trained model already has but are hard for users to access via prompting alone.

Figure 2-10 shows the overall workflow of pre-training, SFT, and preference finetuning, assuming you use RLHF for the last step. You can approximate how well a model aligns with human preference by determining what steps the model creators have taken.

Figure 2-10. The overall training workflow with pre-training, SFT, and RLHF.

If you squint, Figure 2-10 looks very similar to the meme depicting the monster Shoggoth with a smiley face in Figure 2-11:

1. Self-supervised pre-training results in a rogue model that can be considered an untamed monster because it uses indiscriminate data from the internet.
2. This monster is then supervised finetuned on higher-quality data—Stack Overflow, Quora, or human annotations—which makes it more socially acceptable.
3. This finetuned model is further polished using preference finetuning to make it customer-appropriate, which is like giving it a smiley face.
