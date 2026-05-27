---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 083
section-title: Model Selection Workflow
source-location: pages 203-204
previous-section: AI Space/normalized/pdf/ai-engineering/sections/082-model-selection.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/084-model-build-versus-buy.md
classification: reusable-knowledge-candidate
---
# Model Selection Workflow

Criteria Metric Benchmark Hard requirement Ideal
Code generation
capability
pass@1 HumanEval > 90% > 95%
Factual
consistency
Internal GPT metric Internal hallucination
dataset
> 0.8 > 0.9
Now that you have your criteria, let’s move on to the next step and use them to select
the best model for your application.
Model Selection
At the end of the day, you don’t really care about which model is the best. You care
about which model is the best for your applications. Once you’ve defined the criteria
for your application, you should evaluate models against these criteria.
During the application development process, as you progress through different adap‐
tation techniques, you’ll have to do model selection over and over again. For exam‐
ple, prompt engineering might start with the strongest model overall to evaluate
feasibility and then work backward to see if smaller models would work. If you decide
to do finetuning, you might start with a small model to test your code and move
toward the biggest model that fits your hardware constraints (e.g., one GPU).
In general, the selection process for each technique typically involves two steps:
1. Figuring out the best achievable performance
2. Mapping models along the cost–performance axes and choosing the model that
gives the best performance for your bucks
However, the actual selection process is a lot more nuanced. Let’s explore what it
looks like.
Model Selection Workflow
When looking at models, it’s important to differentiate between hard attributes (what
is impossible or impractical for you to change) and soft attributes (what you can and
are willing to change).
Hard attributes are often the results of decisions made by model providers (licenses,
training data, model size) or your own policies (privacy, control). For some use cases,
the hard attributes can reduce the pool of potential models significantly.
Soft attributes are attributes that can be improved upon, such as accuracy, toxicity, or
factual consistency. When estimating how much you can improve on a certain
attribute, it can be tricky to balance being optimistic and being realistic. I’ve had sit‐
uations where a model’s accuracy hovered around 20% for the first few prompts.
Model Selection | 179

However, the accuracy jumped to 70% after I decomposed the task into two steps. At
the same time, I’ve had situations where a model remained unusable for my task even
after weeks of tweaking, and I had to give up on that model.
What you define as hard and soft attributes depends on both the model and your use
case. For example, latency is a soft attribute if you have access to the model to opti‐
mize it to run faster. It’s a hard attribute if you use a model hosted by someone else.
At a high level, the evaluation workflow consists of four steps (see Figure 4-5):
1. Filter out models whose hard attributes don’t work for you. Your list of hard
attributes depends heavily on your own internal policies, whether you want to
use commercial APIs or host your own models.
2. Use publicly available information, e.g., benchmark performance and leader‐
board ranking, to narrow down the most promising models to experiment with,
balancing different objectives such as model quality, latency, and cost.
3. Run experiments with your own evaluation pipeline to find the best model,
again, balancing all your objectives.
4. Continually monitor your model in production to detect failure and collect feed‐
back to improve your application.
Figure 4-5. An overview of the evaluation workflow to evaluate models for your
application.
180 | Chapter 4: Evaluate AI Systems

[Visual content extracted via GLM-OCR]

However, the accuracy jumped to 70% after I decomposed the task into two steps. At the same time, I’ve had situations where a model remained unusable for my task even after weeks of tweaking, and I had to give up on that model.

What you define as hard and soft attributes depends on both the model and your use case. For example, latency is a soft attribute if you have access to the model to optimize it to run faster. It’s a hard attribute if you use a model hosted by someone else.

At a high level, the evaluation workflow consists of four steps (see Figure 4-5):

1. Filter out models whose hard attributes don’t work for you. Your list of hard attributes depends heavily on your own internal policies, whether you want to use commercial APIs or host your own models.
2. Use publicly available information, e.g., benchmark performance and leaderboard ranking, to narrow down the most promising models to experiment with, balancing different objectives such as model quality, latency, and cost.
3. Run experiments with your own evaluation pipeline to find the best model, again, balancing all your objectives.
4. Continually monitor your model in production to detect failure and collect feedback to improve your application.

Figure 4-5. An overview of the evaluation workflow to evaluate models for your application.
