---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 178
section-title: Summary
source-location: pages 516-518
previous-section: AI Space/normalized/pdf/ai-engineering/sections/177-feedback-limitations.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/179-epilogue.md
classification: reusable-knowledge-candidate
---
# Summary

A degenerate feedback loop can alter your product’s focus and use base. Imagine that
initially, a small number of users give feedback that they like cat photos. The system
picks up on this and starts generating more photos with cats. This attracts cat lovers,
who give more feedback that cat photos are good, encouraging the system to generate
even more cats. Before long, your application becomes a cat haven. Here, I use cat
photos as an example, but the same mechanism can amplify other biases, such as rac‐
ism, sexism, and preference for explicit content.
Acting on user feedback can also turn a conversational agent into, for lack of a better
word, a liar. Multiple studies have shown that training a model on user feedback can
teach it to give users what it thinks users want, even if that isn’t what’s most accurate
or beneficial ( Stray, 2023 ). Sharma et al. (2023)  show that AI models trained on
human feedback tend toward. sycophancy. They are more likely to present user
responses matching this user’s view.
User feedback is crucial for improving user experience, but if used indiscriminately, it
can perpetuate biases and destroy your product. Before incorporating feedback into
your product, make sure that you understand the limitations of this feedback and its
potential impact.
Summary
If each previous chapter focused on a specific aspect of AI engineering, this chapter
looked into the process of building applications on top of foundation models as a
whole.
The chapter consisted of two parts. The first part discussed a common architecture
for AI applications. While the exact architecture for an application might vary, this
high-level architecture provides a framework for understanding how different com‐
ponents fit together. I used the step-by-step approach in building this architecture to
discuss the challenges at each step and the techniques you can use to address them.
While it’s necessary to separate components to keep your system modular and main‐
tainable, this separation is fluid. There are many ways components can overlap in
functionalities. For example, guardrails can be implemented in the inference service,
the model gateway, or as a standalone component.
Each additional component can potentially make your system more capable, safer, or
faster but will also increase the system’s complexity, exposing it to new failure modes.
One integral part of any complex system is monitoring and observability. Observabil‐
ity involves understanding how your system fails, designing metrics and alerts
around failures, and ensuring that your system is designed in a way that makes these
failures detectable and traceable. While many observability best practices and tools
from software engineering and traditional machine learning are applicable to AI
492 | Chapter 10: AI Engineering Architecture and User Feedback

engineering applications, foundation models introduce new failure modes, which
require additional metrics and design considerations.
At the same time, the conversational interface enables new types of user feedback,
which you can leverage for analytics, product improvement, and the data flywheel.
The second part of the chapter discussed various forms of conversational feedback
and how to design your application to effectively collect it.
Traditionally, user feedback design has been seen as a product responsibility rather
than an engineering one, and as a result, it is often overlooked by engineers. How‐
ever, since user feedback is a crucial source of data for continuously improving AI
models, more AI engineers are now becoming involved in the process to ensure they
receive the data they need. This reinforces the idea from Chapter 1 that, compared to
traditional ML engineering, AI engineering is moving closer to product. This is
because of both the increasing importance of data flywheel and product experience as
competitive advantages.
Many AI challenges are, at their core, system problems. To solve them, it’s often nec‐
essary to step back and consider the system as a whole. A single problem might be
addressed by different components working independently, or a solution could
require the collaboration of multiple components. A thorough understanding of the
system is essential to solving real problems, unlocking new possibilities, and ensuring
safety.
Summary | 493
