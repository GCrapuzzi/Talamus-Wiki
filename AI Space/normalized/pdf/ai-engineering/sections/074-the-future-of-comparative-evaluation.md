---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 074
section-title: The Future of Comparative Evaluation
source-location: pages 179-179
previous-section: AI Space/normalized/pdf/ai-engineering/sections/073-challenges-of-comparative-evaluation.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/075-summary.md
classification: reusable-knowledge-candidate
---
# The Future of Comparative Evaluation

case. Let’s say we obtained the ranking that model B is better than model A. Any of
the following scenarios could be valid:
1. Model B is good, but model A is bad.
2. Both model A and model B are bad.
3. Both model A and model B are good.
You need other forms of evaluation to determine which scenario is true.
Imagine that we’re using model A for customer support, and model A can resolve
70% of all the tickets. Consider model B, which wins against A 51% of the time. It’s
unclear how this 51% win rate will be converted to the number of requests model B
can resolve. Several people have told me that in their experience, a 1% change in the
win rate can induce a huge performance boost in some applications but just a mini‐
mal boost in other applications.
When deciding to swap out A for B, human preference isn’t everything. We also care
about other factors like cost. Not knowing what performance boost to expect makes it
hard to do the cost–benefit analysis. If model B costs twice as much as A, compara‐
tive evaluation isn’t sufficient to help us determine if the performance boost from B
will be worth the added cost.
The Future of Comparative Evaluation
Given so many limitations of comparative evaluation, you might wonder if there’s a
future to it. There are many benefits to comparative evaluation. First, as discussed in
“Post-Training”  on page 78, people have found that it’s easier to compare two out‐
puts than to give each output a concrete score. As models become stronger, surpass‐
ing human performance, it might become impossible for human evaluators to give
model responses concrete scores. However, human evaluators might still be able to
detect the difference, and comparative evaluation might remain the only option. For
example, the Llama 2 paper shared that when the model ventures into the kind of
writing beyond the ability of the best human annotators, humans can still provide
valuable feedback when comparing two answers (Touvron et al., 2023).
Second, comparative evaluation aims to capture the quality we care about: human
preference. It reduces the pressure to have to constantly create more benchmarks to
catch up with AI’s ever-expanding capabilities. Unlike benchmarks that become
useless when model performance achieves perfect scores, comparative evaluations
will never get saturated as long as newer, stronger models are introduced.
Comparative evaluation is relatively hard to game, as there’s no easy way to cheat,
like training your model on reference data. For this reason, many trust the results of
public comparative leaderboards more than any other public leaderboards.
Ranking Models with Comparative Evaluation | 155
