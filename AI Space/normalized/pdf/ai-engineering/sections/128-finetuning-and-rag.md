---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 128
section-title: Finetuning and RAG
source-location: pages 340-342
previous-section: AI Space/normalized/pdf/ai-engineering/sections/127-reasons-not-to-finetune.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/129-memory-bottlenecks.md
classification: reusable-knowledge-candidate
---
# Finetuning and RAG

Figure 7-2. Instead of including examples in each prompt, which increases cost and
latency, you finetune a model on these examples.
Finetuning and RAG
Once you’ve maximized the performance gains from prompting, you might wonder
whether to do RAG or finetuning next. The answer depends on whether your model’s
failures are information-based or behavior-based.
If the model fails because it lacks information, a RAG system that gives the model
access to the relevant sources of information can help . Information-based failures hap‐
pen when the outputs are factually wrong or outdated. Here are two example scenar‐
ios in which information-based failures happen:
The model doesn’t have the information.
Public models are unlikely to have information private to you or your organiza‐
tion. When a model doesn’t have the information, it either tells you so or halluci‐
nates an answer.
The model has outdated information.
If you ask: “How many studio albums has Taylor Swift released?” and the correct
answer is 11, but the model answers 10, it can be because the model’s cut-off date
was before the release of the latest album.
The paper “Fine-Tuning or Retrieval?”  by Ovadia et al. (2024) demonstrated that for
tasks that require up-to-date information, such as questions about current events,
RAG outperformed finetuned models. Not only that, RAG with the base model
316 | Chapter 7: Finetuning

[Visual content extracted via GLM-OCR]

Finetuning and RAG

Once you’ve maximized the performance gains from prompting, you might wonder whether to do RAG or finetuning next. The answer depends on whether your model’s failures are information-based or behavior-based.

If the model fails because it lacks information, a RAG system that gives the model access to the relevant sources of information can help. Information-based failures happen when the outputs are factually wrong or outdated. Here are two example scenarios in which information-based failures happen:

The model doesn’t have the information.
Public models are unlikely to have information private to you or your organization. When a model doesn’t have the information, it either tells you so or hallucinates an answer.

The model has outdated information.
If you ask: “How many studio albums has Taylor Swift released?” and the correct answer is 11, but the model answers 10, it can be because the model’s cut-off date was before the release of the latest album.

The paper “Fine-Tuning or Retrieval?” by Ovadia et al. (2024) demonstrated that for tasks that require up-to-date information, such as questions about current events, RAG outperformed finetuned models. Not only that, RAG with the base model

5 Some people, such as the authors of the Llama 3.1 paper (Dubey et al., 2024), adhere to “the principle that
post-training should align the model to ‘know what it knows’ rather than add knowledge.”
outperformed RAG with finetuned models, as shown in Table 7-2. This finding indi‐
cates that while finetuning can enhance a model’s performance on a specific task, it
may also lead to a decline in performance in other areas.
Table 7-2. RAG outperforms finetuning on a question-answering task about current events,
curated by Ovadia et al. (2024). FT-reg and FT-par refer to two different finetuning
approaches the author used.
Base model Base model + RAG FT-reg FT-par FT-reg + RAG FT-par + RAG
Mistral-7B 0.481 0.875 0.504 0.588 0.810 0.830
Llama 2-7B 0.353 0.585 0.219 0.392 0.326 0.520
Orca 2-7B 0.456 0.876 0.511 0.566 0.820 0.826
On the other hand, if the model has behavioral issues, finetuning might help . One
behavioral issue is when the model’s outputs are factually correct but irrelevant to the
task. For example, you ask the model to generate technical specifications for a soft‐
ware project to provide to your engineering teams. While accurate, the generated
specs lack the details your teams need. Finetuning the model with well-defined tech‐
nical specifications can make the outputs more relevant.
Another issue is when it fails to follow the expected output format. For example, if
you asked the model to write HTML code, but the generated code didn’t compile, it
might be because the model wasn’t sufficiently exposed to HTML in its training data.
You can correct this by exposing the model to more HTML code during finetuning.
Semantic parsing is a category of tasks whose success hinges on the model’s ability to
generate outputs in the expected format and, therefore, often requires finetuning.
Semantic parsing is discussed briefly in Chapters 2 and 6. As a reminder, semantic
parsing means converting natural language into a structured format like JSON.
Strong off-the-shelf models are generally good for common, less complex syntaxes
like JSON, YAML, and regex. However, they might not be as good for syntaxes with
fewer available examples on the internet, such as a domain-specific language for a less
popular tool or a complex syntax.
In short, finetuning is for form, and RAG is for facts . A RAG system gives your model
external knowledge to construct more accurate and informative answers. A RAG sys‐
tem can help mitigate your model’s hallucinations. Finetuning, on the other hand,
helps your model understand and follow syntaxes and styles. 5 While finetuning can
potentially reduce hallucinations if done with enough high-quality data, it can also
worsen hallucinations if the data quality is low.
When to Finetune | 317

If your model has both information and behavior issues, start with RAG. RAG is typ‐
ically easier since you won’t have to worry about curating training data or hosting the
finetuned models. When doing RAG, start with simple term-based solutions such as
BM25 instead of jumping straight into something that requires vector databases.
RAG can also introduce a more significant performance boost than finetuning. Ova‐
dia et al. (2024) showed that for almost all question categories in the MMLU bench‐
mark, RAG outperforms finetuning for three different models: Mistral 7B, Llama
2-7B, and Orca 2-7B.
However, RAG and finetuning aren’t mutually exclusive. They can sometimes be
used together to maximize your application’s performance. In the same experiment,
Ovadia et al. (2024) showed that incorporating RAG on top of a finetuned model can
boost its performance on the MMLU benchmark 43% of the time. It’s important to
note that in this experiment, using RAG with finetuned models doesn’t improve the
performance 57% of the time, compared to using RAG alone.
There’s no universal workflow for all applications. Figure 7-3 shows some paths an
application development process might follow over time. The arrow indicates what
next step you might try. This figure is inspired by an example workflow shown by
OpenAI (2023).
Figure 7-3. Example application development flows. After simple retrieval (such as
term-based retrieval), whether to experiment with more complex retrieval (such as
hybrid search) or finetuning depends on each application and its failure modes.
So the workflow to adapt a model to a task might work as follows. Note that before
any of the adaptation steps, you should define your evaluation criteria and design
your evaluation pipeline, as discussed in Chapter 4. This evaluation pipeline is what
you’ll use to benchmark your progress as you develop your application. Evaluation
318 | Chapter 7: Finetuning

[Visual content extracted via GLM-OCR]

If your model has both information and behavior issues, start with RAG. RAG is typically easier since you won’t have to worry about curating training data or hosting the finetuned models. When doing RAG, start with simple term-based solutions such as BM25 instead of jumping straight into something that requires vector databases.

RAG can also introduce a more significant performance boost than finetuning. Ovadia et al. (2024) showed that for almost all question categories in the MMLU benchmark, RAG outperforms finetuning for three different models: Mistral 7B, Llama 2-7B, and Orca 2-7B.

However, RAG and finetuning aren’t mutually exclusive. They can sometimes be used together to maximize your application’s performance. In the same experiment, Ovadia et al. (2024) showed that incorporating RAG on top of a finetuned model can boost its performance on the MMLU benchmark 43% of the time. It’s important to note that in this experiment, using RAG with finetuned models doesn’t improve the performance 57% of the time, compared to using RAG alone.

There’s no universal workflow for all applications. Figure 7-3 shows some paths an application development process might follow over time. The arrow indicates what next step you might try. This figure is inspired by an example workflow shown by OpenAI (2023).

Figure 7-3. Example application development flows. After simple retrieval (such as term-based retrieval), whether to experiment with more complex retrieval (such as hybrid search) or finetuning depends on each application and its failure modes.

So the workflow to adapt a model to a task might work as follows. Note that before any of the adaptation steps, you should define your evaluation criteria and design your evaluation pipeline, as discussed in Chapter 4. This evaluation pipeline is what you’ll use to benchmark your progress as you develop your application. Evaluation
