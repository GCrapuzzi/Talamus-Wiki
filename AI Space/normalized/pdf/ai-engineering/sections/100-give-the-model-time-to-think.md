---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 100
section-title: Give the Model Time to Think
source-location: pages 251-252
previous-section: AI Space/normalized/pdf/ai-engineering/sections/099-break-complex-tasks-into-simpler-subtasks.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/101-iterate-on-your-prompts.md
classification: reusable-knowledge-candidate
---
# Give the Model Time to Think

One downside of prompt decomposition is that it can increase the latency perceived
by users, especially for tasks where users don’t see the intermediate outputs. With
more intermediate steps, users have to wait longer to see the first output token gener‐
ated in the final step.
Prompt decomposition typically involves more model queries, which can increase
costs. However, the cost of two decomposed prompts might not be twice that of one
original prompt. This is because most model APIs charge per input and output token,
and smaller prompts often incur fewer tokens. Additionally, you can use cheaper
models for simpler steps. For example, in customer support, it’s common to use a
weaker model for intent classification and a stronger model to generate user respon‐
ses. Even if the cost increases, the improved performance and reliability can make it
worthwhile.
As you work to improve your application, your prompt can quickly become complex.
You might need to provide more detailed instructions, add more examples, and con‐
sider edge cases. GoDaddy (2024) found that the prompt for their customer support
chatbot bloated to over 1,500 tokens after one iteration. After decomposing the
prompt into smaller prompts targeting different subtasks, they found that their
model performed better while also reducing token costs.
Give the Model Time to Think
You can encourage the model to spend more time to, for a lack of better words,
“think” about a question using chain-of-thought (CoT) and self-critique prompting.
CoT means explicitly asking the model to think step by step, nudging it toward a
more systematic approach to problem solving. CoT is among the first prompting
techniques that work well across models. It was introduced in “Chain-of-Thought
Prompting Elicits Reasoning in Large Language Models” ( Wei et al., 2022 ), almost a
year before ChatGPT came out. Figure 5-6  shows how CoT improved the perfor‐
mance of models of different sizes (LaMDA, GPT-3, and PaLM) on different bench‐
marks. LinkedIn found that CoT also reduces models’ hallucinations.
Prompt Engineering Best Practices | 227

Figure 5-6. CoT improved the performance of LaMDA, GPT-3, and PaLM on MAWPS
(Math Word Problem Solving), SVAMP (sequence variation analysis, maps, and phy‐
logeny), and GSM-8K benchmarks. Screenshot from Wei et al., 2022. This image is
licensed under CC BY 4.0.
The simplest way to do CoT is to add “think step by step” or “explain your decision”
in your prompt. The model then works out what steps to take. Alternatively, you can
specify the steps the model should take or include examples of what the steps should
look like in your prompt. Table 5-4 shows four CoT response variations to the same
original prompt. Which variation works best depends on the application.
228 | Chapter 5: Prompt Engineering

[Visual content extracted via GLM-OCR]

The simplest way to do CoT is to add “think step by step” or “explain your decision” in your prompt. The model then works out what steps to take. Alternatively, you can specify the steps the model should take or include examples of what the steps should look like in your prompt. Table 5-4 shows four CoT response variations to the same original prompt. Which variation works best depends on the application.
