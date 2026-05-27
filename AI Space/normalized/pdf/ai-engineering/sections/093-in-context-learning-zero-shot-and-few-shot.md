---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 093
section-title: "In-Context Learning: Zero-Shot and Few-Shot"
source-location: pages 237-238
previous-section: AI Space/normalized/pdf/ai-engineering/sections/092-introduction-to-prompting.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/094-system-prompt-and-user-prompt.md
classification: reusable-knowledge-candidate
---
# In-Context Learning: Zero-Shot and Few-Shot

2 In late 2023, Stanford dropped robustness from their HELM Lite benchmark.
follow it. How to evaluate a model’s instruction-following capability is discussed in
Chapter 4.
How much prompt engineering is needed depends on how robust the model is to
prompt perturbation. If the prompt changes slightly—such as writing “5” instead of
“five”, adding a new line, or changing capitalization—would the model’s response be
dramatically different? The less robust the model is, the more fiddling is needed.
You can measure a model’s robustness by randomly perturbing the prompts to see
how the output changes. Just like instruction-following capability, a model’s robust‐
ness is strongly correlated with its overall capability. As models become stronger,
they also become more robust. This makes sense because an intelligent model should
understand that “5” and “five” mean the same thing. 2 For this reason, working with
stronger models can often save you headaches and reduce time wasted on fiddling.
Experiment with different prompt structures to find out which
works best for you. Most models, including GPT-4, empirically
perform better when the task description is at the beginning of the
prompt. However, some models, including Llama 3, seem to per‐
form better when the task description is at the end of the prompt.
In-Context Learning: Zero-Shot and Few-Shot
Teaching models what to do via prompts is also known as in-context learning. This
term was introduced by Brown et al. (2020) in the GPT-3 paper, “Language Models
Are Few-shot Learners” . Traditionally, a model learns the desirable behavior during
training—including pre-training, post-training, and finetuning—which involves
updating model weights. The GPT-3 paper demonstrated that language models can
learn the desirable behavior from examples in the prompt, even if this desirable
behavior is different from what the model was originally trained to do. No weight
updating is needed. Concretely, GPT-3 was trained for next token prediction, but the
paper showed that GPT-3 could learn from the context to do translation, reading
comprehension, simple math, and even answer SAT questions.
In-context learning allows a model to incorporate new information continually to
make decisions, preventing it from becoming outdated. Imagine a model that was
trained on the old JavaScript documentation. To use this model to answer questions
about the new JavaScript version, without in-context learning, you’d have to retrain
this model. With in-context learning, you can include the new JavaScript changes in
the model’s context, allowing the model to respond to queries beyond its cut-off date.
This makes in-context learning a form of continual learning.
Introduction to Prompting | 213

[Visual content extracted via GLM-OCR]

follow it. How to evaluate a model’s instruction-following capability is discussed in Chapter 4.

How much prompt engineering is needed depends on how robust the model is to prompt perturbation. If the prompt changes slightly—such as writing “5” instead of “five”, adding a new line, or changing capitalization—would the model’s response be dramatically different? The less robust the model is, the more fiddling is needed.

You can measure a model’s robustness by randomly perturbing the prompts to see how the output changes. Just like instruction-following capability, a model’s robustness is strongly correlated with its overall capability. As models become stronger, they also become more robust. This makes sense because an intelligent model should understand that “5” and “five” mean the same thing. For this reason, working with stronger models can often save you headaches and reduce time wasted on fiddling.

Experiment with different prompt structures to find out which works best for you. Most models, including GPT-4, empirically perform better when the task description is at the beginning of the prompt. However, some models, including Llama 3, seem to perform better when the task description is at the end of the prompt.

In-Context Learning: Zero-Shot and Few-Shot

Teaching models what to do via prompts is also known as in-context learning. This term was introduced by Brown et al. (2020) in the GPT-3 paper, “Language Models Are Few-shot Learners”. Traditionally, a model learns the desirable behavior during training—including pre-training, post-training, and finetuning—which involves updating model weights. The GPT-3 paper demonstrated that language models can learn the desirable behavior from examples in the prompt, even if this desirable behavior is different from what the model was originally trained to do. No weight updating is needed. Concretely, GPT-3 was trained for next token prediction, but the paper showed that GPT-3 could learn from the context to do translation, reading comprehension, simple math, and even answer SAT questions.

In-context learning allows a model to incorporate new information continually to make decisions, preventing it from becoming outdated. Imagine a model that was trained on the old JavaScript documentation. To use this model to answer questions about the new JavaScript version, without in-context learning, you’d have to retrain this model. With in-context learning, you can include the new JavaScript changes in the model’s context, allowing the model to respond to queries beyond its cut-off date. This makes in-context learning a form of continual learning.

2 In late 2023, Stanford dropped robustness from their HELM Lite benchmark.

Each example provided in the prompt is called a shot. Teaching a model to learn from
examples in the prompt is also called few-shot learning . With five examples, it’s 5shot learning. When no example is provided, it’s zero-shot learning.
Exactly how many examples are needed depends on the model and the application.
You’ll need to experiment to determine the optimal number of examples for your
applications. In general, the more examples you show a model, the better it can learn.
The number of examples is limited by the model’s maximum context length. The
more examples there are, the longer your prompt will be, increasing the inference
cost.
For GPT-3, few-shot learning showed significant improvement compared to zeroshot learning. However, for the use cases in Microsoft’s 2023 analysis , few-shot learn‐
ing led to only limited improvement compared to zero-shot learning on GPT-4 and a
few other models. This result suggests that as models become more powerful, they
become better at understanding and following instructions, which leads to better per‐
formance with fewer examples. However, the study might have underestimated the
impact of few-shot examples on domain-specific use cases. For example, if a model
doesn’t see many examples of the Ibis dataframe API  in its training data, including
Ibis examples in the prompt can still make a big difference.
Terminology Ambiguity: Prompt Versus Context
Sometimes, prompt and context are used interchangeably. In the GPT-3 paper
(Brown et al., 2020), the term context was used to refer to the entire input into a
model. In this sense, context is exactly the same as prompt.
However, in a long discussion on my Discord, some people argued that context is part
of the prompt. Context refers to the information a model needs to perform what the
prompt asks it to do. In this sense, context is contextual information.
To make it more confusing, Google’s PALM 2 documentation  defines context as the
description that shapes “how the model responds throughout the conversation. For
example, you can use context to specify words the model can or cannot use, topics to
focus on or avoid, or the response format or style.” This makes context the same as
the task description.
In this book, I’ll use prompt to refer to the whole input into the model, and context to
refer to the information provided to the model so that it can perform a given task.
214 | Chapter 5: Prompt Engineering
