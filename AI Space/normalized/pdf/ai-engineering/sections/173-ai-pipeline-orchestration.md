---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 173
section-title: AI Pipeline Orchestration
source-location: pages 496-497
previous-section: AI Space/normalized/pdf/ai-engineering/sections/172-monitoring-and-observability.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/174-user-feedback.md
classification: reusable-knowledge-candidate
---
# AI Pipeline Orchestration

6 Because of this, some orchestrator tools want to be gateways. In fact, so many tools seem to want to become
end-to-end platforms that do everything.
found a typo and fixed it. A simple logic should be sufficient to catch when your
application’s system prompt changes.
User behavior changes
Over time, users adapt their behaviors to the technology. For example, people
have already figured out how to frame their queries to get better results on Goo‐
gle Search or how to make their articles rank higher on search results. People liv‐
ing in areas with self-driving cars have already figured out how to bully selfdriving cars into giving them the right of way ( Liu et al., 2020 ). It’s likely that
your users will change their behaviors to get better results out of your applica‐
tion. For example, your users might learn to write instructions to make the
responses more concise. This might cause a gradual drop in response length over
time. If you look only at metrics, it might not be obvious what caused this grad‐
ual drop. You need investigations to understand the root cause.
Underlying model changes
When using a model through an API, it’s possible that the API remains
unchanged while the underlying model is updated. As mentioned in Chapter 4,
model providers might not always disclose these updates, leaving it to you to
detect any changes. Different versions of the same API can have a significant
impact on performance. For instance, Chen et al. (2023) observed notable differ‐
ences in benchmark scores between the March 2023 and June 2023 versions of
GPT-4 and GPT-3.5. Likewise, Voiceflow reported a 10% performance drop
when switching from the older GPT-3.5-turbo-0301 to the newer GPT-3.5turbo-1106.
AI Pipeline Orchestration
An AI application can get fairly complex, consisting of multiple models, retrieving
data from many databases, and having access to a wide range of tools. An orchestra‐
tor helps you specify how these different components work together to create an endto-end pipeline. It ensures that data flows seamlessly between components. At a high
level, an orchestrator operates in two steps, components definition and chaining:
Components definition
You need to tell the orchestrator what components your system uses, including
different models, external data sources for retrieval, and tools that your system
can use. A model gateway can make it easier to add a model. 6 You can also tell
the orchestrator if you use any tools for evaluation and monitoring.
472 | Chapter 10: AI Engineering Architecture and User Feedback

Chaining
Chaining is basically function composition: it combines different functions
(components) together. In chaining (pipelining), you tell the orchestrator the
steps your system takes from receiving the user query until completing the task.
Here’s an example of the steps:
1. Process the raw query.
2. Retrieve the relevant data based on the processed query.
3. Combine the original query and the retrieved data to create a prompt in the
format expected by the model.
4. The model generates a response based on the prompt.
5. Evaluate the response.
6. If the response is considered good, return it to the user. If not, route the
query to a human operator.
The orchestrator is responsible for passing data between components. It should pro‐
vide toolings that help ensure that the output from the current step is in the format
expected by the next step. Ideally, it should notify you when this data flow is disrup‐
ted due to errors such as component failures or data mismatch failures.
An AI pipeline orchestrator is different from a general workflow
orchestrator, like Airflow or Metaflow.
When designing the pipeline for an application with strict latency requirements, try
to do as much in parallel as possible. For example, if you have a routing component
(deciding where to send a query) and a PII removal component, both can be done at
the same time.
There are many AI orchestration tools, including LangChain, LlamaIndex, Flowise,
Langflow, and Haystack. Because retrieval and tool use are common application pat‐
terns, many RAG and agent frameworks are also orchestration tools.
While it’s tempting to jump straight to an orchestration tool when starting a project,
you might want to start building your application without one first.  Any external tool
brings additional complexity. An orchestrator can abstract away critical details of
how your system works, making it hard to understand and debug your system.
AI Engineering Architecture | 473

[Visual content extracted via GLM-OCR]

Chaining

Chaining is basically function composition: it combines different functions (components) together. In chaining (pipelining), you tell the orchestrator the steps your system takes from receiving the user query until completing the task. Here’s an example of the steps:

1. Process the raw query.
2. Retrieve the relevant data based on the processed query.
3. Combine the original query and the retrieved data to create a prompt in the format expected by the model.
4. The model generates a response based on the prompt.
5. Evaluate the response.
6. If the response is considered good, return it to the user. If not, route the query to a human operator.

The orchestrator is responsible for passing data between components. It should provide toolings that help ensure that the output from the current step is in the format expected by the next step. Ideally, it should notify you when this data flow is disrupted due to errors such as component failures or data mismatch failures.

An AI pipeline orchestrator is different from a general workflow orchestrator, like Airflow or Metaflow.

When designing the pipeline for an application with strict latency requirements, try to do as much in parallel as possible. For example, if you have a routing component (deciding where to send a query) and a PII removal component, both can be done at the same time.

There are many AI orchestration tools, including LangChain, LlamaIndex, Flowise, Langflow, and Haystack. Because retrieval and tool use are common application patterns, many RAG and agent frameworks are also orchestration tools.

While it’s tempting to jump straight to an orchestration tool when starting a project, you might want to start building your application without one first. Any external tool brings additional complexity. An orchestrator can abstract away critical details of how your system works, making it hard to understand and debug your system.
