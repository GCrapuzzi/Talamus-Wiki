---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 174
section-title: User Feedback
source-location: pages 498-498
previous-section: AI Space/normalized/pdf/ai-engineering/sections/173-ai-pipeline-orchestration.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/175-extracting-conversational-feedback.md
classification: reusable-knowledge-candidate
---
# User Feedback

7 One key disadvantage of launching an open source application instead of a commercial application is that it’s
a lot harder to collect user feedback. Users can take your open source application and deploy it themselves,
and you have no idea how the application is used.
As you advance to the later stages of your application development process, you
might decide that an orchestrator can make your life easier. Here are three aspects to
keep in mind when evaluating orchestrators:
Integration and extensibility
Evaluate whether the orchestrator supports the components you’re already using
or might adopt in the future. For example, if you want to use a Llama model,
check if the orchestrator supports that. Given how many models, databases, and
frameworks there are, it’s impossible for an orchestrator to support everything.
Therefore, you’ll also need to consider an orchestrator’s extensibility. If it doesn’t
support a specific component, how hard is it to change that?
Support for complex pipelines
As your applications grow in complexity, you might need to manage intricate
pipelines involving multiple steps and conditional logic. An orchestrator that
supports advanced features like branching, parallel processing, and error han‐
dling will help you manage these complexities efficiently.
Ease of use, performance, and scalability
Consider the user-friendliness of the orchestrator. Look for intuitive APIs, com‐
prehensive documentation, and strong community support, as these can signifi‐
cantly reduce the learning curve for you and your team. Avoid orchestrators that
initiate hidden API calls or introduce latency to your applications. Additionally,
ensure that the orchestrator can scale effectively as the number of applications,
developers, and traffic grows.
User Feedback
User feedback has always played a critical role in software applications in two key
ways: evaluating the application’s performance and informing its development. How‐
ever, in AI applications, user feedback takes on an even more significant role. User
feedback is proprietary data, and data is a competitive advantage. A well-designed
user feedback system is necessary to create the data flywheel discussed in Chapter 8.7
User feedback can be used not only to personalize models for individual users but
also to train future iterations of the models. As data becomes increasingly scarce, pro‐
prietary data is more valuable than ever. A product that launches quickly and attracts
users early can gather data to continually improve models, making it difficult for
competitors to catch up.
474 | Chapter 10: AI Engineering Architecture and User Feedback
