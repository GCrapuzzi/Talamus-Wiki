---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 054
section-title: Summary
source-location: pages 135-136
previous-section: AI Space/normalized/pdf/ai-engineering/sections/053-the-probabilistic-nature-of-ai.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/055-chapter-3.-evaluation-methodology.md
classification: reusable-knowledge-candidate
---
# Summary

The two hypotheses discussed complement each other. The self-delusion hypothesis
focuses on how self-supervision causes hallucinations, whereas the mismatched inter‐
nal knowledge hypothesis focuses on how supervision causes hallucinations.
If we can’t stop hallucinations altogether, can we at least detect when a model halluci‐
nates so that we won’t serve those hallucinated responses to users? Well, detecting
hallucinations isn’t that straightforward either—think about how hard it is for us to
detect when another human is lying or making things up. But people have tried. We
discuss how to detect and measure hallucinations in Chapter 4.
Summary
This chapter discussed the core design decisions when building a foundation model.
Since most people will be using ready-made foundation models instead of training
one from scratch, I skipped the nitty-gritty training details in favor of modeling fac‐
tors that help you determine what models to use and how to use them.
A crucial factor affecting a model’s performance is its training data. Large models
require a large amount of training data, which can be expensive and time-consuming
to acquire. Model providers, therefore, often leverage whatever data is available. This
leads to models that can perform well on the many tasks present in the training data,
which may not include the specific task you want. This chapter went over why it’s
often necessary to curate training data to develop models targeting specific languages,
especially low-resource languages, and specific domains.
After sourcing the data, model development can begin. While model training often
dominates the headlines, an important step prior to that is architecting the model.
The chapter looked into modeling choices, such as model architecture and model
size. The dominating architecture for language-based foundation models is trans‐
former. This chapter explored the problems that the transformer architecture was
designed to address, as well as its limitations.
The scale of a model can be measured by three key numbers: the number of parame‐
ters, the number of training tokens, and the number of FLOPs needed for training.
Two aspects that influence the amount of compute needed to train a model are the
model size and the data size. The scaling law helps determine the optimal number of
parameters and number of tokens given a compute budget. This chapter also looked
at scaling bottlenecks. Currently, scaling up a model generally makes it better. But
how long will this continue to be true?
Due to the low quality of training data and self-supervision during pre-training, the
resulting model might produce outputs that don’t align with what users want. This is
addressed by post-training, which consists of two steps: supervised finetuning and
preference finetuning. Human preference is diverse and impossible to capture in a
single mathematical formula, so existing solutions are far from foolproof.
Summary | 111

This chapter also covered one of my favorite topics: sampling, the process by which a
model generates output tokens. Sampling makes AI models probabilistic. This proba‐
bilistic nature is what makes models like ChatGPT and Gemini great for creative
tasks and fun to talk to. However, this probabilistic nature also causes inconsistency
and hallucinations.
Working with AI models requires building your workflows around their probabilistic
nature. The rest of this book will explore how to make AI engineering, if not deter‐
ministic, at least systematic. The first step toward systematic AI engineering is to
establish a solid evaluation pipeline to help detect failures and unexpected changes.
Evaluation for foundation models is so crucial that I dedicated two chapters to it,
starting with the next chapter.
112 | Chapter 2: Understanding Foundation Models
