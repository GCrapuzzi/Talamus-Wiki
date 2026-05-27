---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 094
section-title: System Prompt and User Prompt
source-location: pages 239-241
previous-section: AI Space/normalized/pdf/ai-engineering/sections/093-in-context-learning-zero-shot-and-few-shot.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/095-context-length-and-context-efficiency.md
classification: reusable-knowledge-candidate
---
# System Prompt and User Prompt

Today, in-context learning is taken for granted. A foundation model learns from a
massive amount of data and should be able to do a lot of things. However, before
GPT-3, ML models could do only what they were trained to do, so in-context learn‐
ing felt like magic. Many smart people pondered at length why and how in-context
learning works (see “How Does In-context Learning Work?”  by the Stanford AI Lab).
François Chollet, the creator of the ML framework Keras, compared a foundation
model to a library of many different programs . For example, it might contain one
program that can write haikus and another that can write limericks. Each program
can be activated by certain prompts. In this view, prompt engineering is about find‐
ing the right prompt that can activate the program you want.
System Prompt and User Prompt
Many model APIs give you the option to split a prompt into a system prompt and a
user prompt. You can think of the system prompt as the task description and the user
prompt as the task. Let’s go through an example to see what this looks like.
Imagine you want to build a chatbot that helps buyers understand property disclo‐
sures. A user can upload a disclosure and ask questions such as “How old is the
roof?” or “What is unusual about this property?” You want this chatbot to act like a
real estate agent. You can put this roleplaying instruction in the system prompt, while
the user question and the uploaded disclosure can be in the user prompt.
System prompt:  You’re an experienced real estate agent. Your job is to
read each disclosure carefully, fairly assess the condition of the
property based on this disclosure, and help your buyer understand the
risks and opportunities of each property. For each question, answer
succinctly and professionally.
User prompt:
Context: [disclosure.pdf]
Question: Summarize the noise complaints, if any, about this property.
Answer:
Almost all generative AI applications, including ChatGPT, have system prompts.
Typically, the instructions provided by application developers are put into the system
prompt, while the instructions provided by users are put into the user prompt. But
you can also be creative and move instructions around, such as putting everything
into the system prompt or user prompt. You can experiment with different ways to
structure your prompts to see which one works best.
Given a system prompt and a user prompt, the model combines them into a single
prompt, typically following a template. As an example, here’s the template for the
Llama 2 chat model:
Introduction to Prompting | 215

3 Usually, deviations from the expected chat template cause the model performance to degrade. However, while
uncommon, it can cause the model perform better, as shown in a Reddit discussion.
<s>[INST] <<SYS>>
{{ system_prompt }}
<</SYS>>
{{ user_message }} [/INST]
If the system prompt is “Translate the text below into French” and the user prompt is
“How are you?”, the final prompt input into Llama 2 should be:
<s>[INST] <<SYS>>
Translate the text below into French
<</SYS>>
How are you? [/INST]
A model’s chat template, discussed in this section, is different from
a prompt template used by application developers to populate
(hydrate) their prompts with specific data. A model’s chat template
is defined by the model’s developers and can usually be found in
the model’s documentation. A prompt template can be defined by
any application developer.
Different models use different chat templates. The same model provider can change
the template between model versions. For example, for the Llama 3 chat model, Meta
changed the template to the following:
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
{{ system_prompt }}<|eot_id|><|start_header_id|>user<|end_header_id|>
{{ user_message }}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
Each text span between <| and |>, such as <|begin_of_text|> and
<|start_header_id|>, is treated as a single token by the model.
Accidentally using the wrong template can lead to bewildering performance issues.
Small mistakes when using a template, such as an extra new line, can also cause the
model to significantly change its behaviors.3
216 | Chapter 5: Prompt Engineering

[Visual content extracted via GLM-OCR]

If the system prompt is “Translate the text below into French” and the user prompt is “How are you?”, the final prompt input into Llama 2 should be:

<s>[INST] <<SYS>>
Translate the text below into French
<<SYS>>

How are you? [/INST]

A model’s chat template, discussed in this section, is different from a prompt template used by application developers to populate (hydrate) their prompts with specific data. A model’s chat template is defined by the model’s developers and can usually be found in the model’s documentation. A prompt template can be defined by any application developer.

Different models use different chat templates. The same model provider can change the template between model versions. For example, for the Llama 3 chat model, Meta changed the template to the following:

```html
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
{{ system_prompt }}<|eot_id|><|start_header_id|>user<|end_header_id|>
{{ user_message }}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
```

Each text span between `<| and |>`, such as `<|begin_of_text|>` and `<|start_header_id|>`, is treated as a single token by the model.

Accidentally using the wrong template can lead to bewildering performance issues. Small mistakes when using a template, such as an extra new line, can also cause the model to significantly change its behaviors.³

³ Usually, deviations from the expected chat template cause the model performance to degrade. However, while uncommon, it can cause the model perform better, as shown in a Reddit discussion.

4 If you spend enough time on GitHub and Reddit, you’ll find many reported chat template mismatch issues,
such as this one. I once spent a day debugging a finetuning issue only to realize that it was because a library I
used didn’t update the chat template for the newer model version.
5 To avoid users making template mistakes, many model APIs are designed so that users don’t have to write
special template tokens themselves.
Here are a few good practices to follow to avoid problems with
mismatched templates:
• When constructing inputs for a foundation model, make sure
that your inputs follow the model’s chat template exactly.
• If you use a third-party tool to construct prompts, verify that
this tool uses the correct chat template. Template errors are,
unfortunately, very common. 4 These errors are hard to spot
because they cause silent failures—the model will do some‐
thing reasonable even if the template is wrong.5
• Before sending a query to a model, print out the final prompt
to double-check if it follows the expected template.
Many model providers emphasize that well-crafted system prompts can improve per‐
formance. For example, Anthropic documentation says, “when assigning Claude a
specific role or personality through a system prompt, it can maintain that character
more effectively throughout the conversation, exhibiting more natural and creative
responses while staying in character.”
But why would system prompts boost performance compared to user prompts?
Under the hood, the system prompt and the user prompt are concatenated into a single
final prompt before being fed into the model . From the model’s perspective, system
prompts and user prompts are processed the same way. Any performance boost that
a system prompt can give is likely because of one or both of the following factors:
• The system prompt comes first in the final prompt, and the model might just be
better at processing instructions that come first.
• The model might have been post-trained to pay more attention to the system
prompt, as shared in the OpenAI paper “The Instruction Hierarchy: Training
LLMs to Prioritize Privileged Instructions” ( Wallace et al., 2024 ). Training a
model to prioritize system prompts also helps mitigate prompt attacks, as dis‐
cussed later in this chapter.
Introduction to Prompting | 217

[Visual content extracted via GLM-OCR]

Here are a few good practices to follow to avoid problems with mismatched templates:

• When constructing inputs for a foundation model, make sure that your inputs follow the model’s chat template exactly.

• If you use a third-party tool to construct prompts, verify that this tool uses the correct chat template. Template errors are, unfortunately, very common. These errors are hard to spot because they cause silent failures—the model will do something reasonable even if the template is wrong.

• Before sending a query to a model, print out the final prompt to double-check if it follows the expected template.

Many model providers emphasize that well-crafted system prompts can improve performance. For example, Anthropic documentation says, “when assigning Claude a specific role or personality through a system prompt, it can maintain that character more effectively throughout the conversation, exhibiting more natural and creative responses while staying in character.”

But why would system prompts boost performance compared to user prompts? Under the hood, the system prompt and the user prompt are concatenated into a single final prompt before being fed into the model. From the model’s perspective, system prompts and user prompts are processed the same way. Any performance boost that a system prompt can give is likely because of one or both of the following factors:

• The system prompt comes first in the final prompt, and the model might just be better at processing instructions that come first.

• The model might have been post-trained to pay more attention to the system prompt, as shared in the OpenAI paper “The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions” (Wallace et al., 2024). Training a model to prioritize system prompts also helps mitigate prompt attacks, as discussed later in this chapter.

---

4 If you spend enough time on GitHub and Reddit, you’ll find many reported chat template mismatch issues, such as this one. I once spent a day debugging a finetuning issue only to realize that it was because a library I used didn’t update the chat template for the newer model version.

5 To avoid users making template mistakes, many model APIs are designed so that users don’t have to write special template tokens themselves.
