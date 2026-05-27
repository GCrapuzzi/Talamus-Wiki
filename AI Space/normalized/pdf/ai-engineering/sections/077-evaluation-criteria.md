---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 077
section-title: Evaluation Criteria
source-location: pages 184-184
previous-section: AI Space/normalized/pdf/ai-engineering/sections/076-chapter-4.-evaluate-ai-systems.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/078-domain-specific-capability.md
classification: reusable-knowledge-candidate
---
# Evaluation Criteria

1 Recommendations can increase purchases, but increased purchases are not always because of good recom‐
mendations. Other factors, such as promotional campaigns and new product launches, can also increase pur‐
chases. It’s important to do A/B testing to differentiate impact. Thanks to Vittorio Cretella for the note.
Evaluation Criteria
Which is worse—an application that has never been deployed or an application that
is deployed but no one knows whether it’s working? When I asked this question at
conferences, most people said the latter. An application that is deployed but can’t be
evaluated is worse. It costs to maintain, but if you want to take it down, it might cost
even more.
AI applications with questionable returns on investment are, unfortunately, quite
common. This happens not only because the application is hard to evaluate but also
because application developers don’t have visibility into how their applications are
being used. An ML engineer at a used car dealership told me that his team built a
model to predict the value of a car based on the specs given by the owner. A year after
the model was deployed, their users seemed to like the feature, but he had no idea if
the model’s predictions were accurate. At the beginning of the ChatGPT fever, com‐
panies rushed to deploy customer support chatbots. Many of them are still unsure if
these chatbots help or hurt their user experience.
Before investing time, money, and resources into building an application, it’s impor‐
tant to understand how this application will be evaluated. I call this approach
evaluation-driven development . The name is inspired by test-driven development  in
software engineering, which refers to the method of writing tests before writing code.
In AI engineering, evaluation-driven development means defining evaluation criteria
before building.
Evaluation-Driven Development
While some companies chase the latest hype, sensible business decisions are still
being made based on returns on investment, not hype. Applications should demon‐
strate value to be deployed. As a result, the most common enterprise applications in
production are those with clear evaluation criteria:
• Recommender systems are common because their successes can be evaluated by
an increase in engagement or purchase-through rates.1
• The success of a fraud detection system can be measured by how much money is
saved from prevented frauds.
• Coding is a common generative AI use case because, unlike other generation
tasks, generated code can be evaluated using functional correctness.
160 | Chapter 4: Evaluate AI Systems
