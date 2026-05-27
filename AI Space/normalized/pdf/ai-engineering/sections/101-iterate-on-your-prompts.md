---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 101
section-title: Iterate on Your Prompts
source-location: pages 253-253
previous-section: AI Space/normalized/pdf/ai-engineering/sections/100-give-the-model-time-to-think.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/102-evaluate-prompt-engineering-tools.md
classification: reusable-knowledge-candidate
---
# Iterate on Your Prompts

Table 5-4. A few CoT prompt variations to the same original query. The CoT additions are
in bold.
Original query Which animal is faster: cats or dogs?
Zero-shot CoT Which animal is faster: cats or dogs? Think step by step before arriving at an answer.
Zero-shot CoT Which animal is faster: cats or dogs? Explain your rationale before giving an answer.
Zero-shot CoT Which animal is faster: cats or dogs? Follow these steps to find an answer:
1. Determine the speed of the fastest dog breed.
2. Determine the speed of the fastest cat breed.
3. Determine which one is faster.
One-shot CoT
(one example is
included in the
prompt)
Which animal is faster: sharks or dolphins?
1. The fastest shark breed is the shortfin mako shark, which can reach speeds around 74 km/h.
2. The fastest dolphin breed is the common dolphin, which can reach speeds around 60 km/h.
3. Conclusion: sharks are faster.
Which animal is faster: cats or dogs?
Self-critique means asking the model to check its own outputs. This is also known as
self-eval, as discussed in Chapter 3. Similar to CoT, self-critique nudges the model to
think critically about a problem.
Similar to prompt decomposition, CoT and self-critique can increase the latency per‐
ceived by users. A model might perform multiple intermediate steps before the user
can see the first output token. This is especially challenging if you encourage the
model to come up with steps on its own. The resulting sequence of steps can take a
long time to finish, leading to increased latency and potentially prohibitive costs.
Iterate on Your Prompts
Prompt engineering requires back and forth. As you understand a model better, you
will have better ideas on how to write your prompts. For example, if you ask a model
to pick the best video game, it might respond that opinions differ and no video game
can be considered the absolute best. Upon seeing this response, you can revise your
prompt to ask the model to pick a game, even if opinions differ.
Each model has its quirks. One model might be better at understanding numbers,
whereas another might be better at roleplaying. One model might prefer system
instructions at the beginning of the prompt, whereas another might prefer them at
the end. Play around with your model to get to know it. Try different prompts. Read
the prompting guide provided by the model developer, if there’s any. Look for other
people’s experiences online. Leverage the model’s playground if one is available. Use
the same prompt on different models to see how their responses differ, which can
give you a better understanding of your model.
Prompt Engineering Best Practices | 229
