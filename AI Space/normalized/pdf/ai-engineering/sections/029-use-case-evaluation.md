---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 029
section-title: Use Case Evaluation
source-location: pages 53-55
previous-section: AI Space/normalized/pdf/ai-engineering/sections/028-planning-ai-applications.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/030-setting-expectations.md
classification: reusable-knowledge-candidate
---
# Use Case Evaluation

19 Smaller startups, however, might have to prioritize product focus and can’t afford to have even one person to
“look around.”
told me that they encouraged their teams to experiment with AI applications to
upskill themselves.
However, if you’re doing this for a living, it might be worthwhile to take a step back
and consider why you’re building this and how you should go about it. It’s easy to
build a cool demo with foundation models. It’s hard to create a profitable product.
Use Case Evaluation
The first question to ask is why you want to build this application. Like many busi‐
ness decisions, building an AI application is often a response to risks and opportuni‐
ties. Here are a few examples of different levels of risks, ordered from high to low:
1. If you don’t do this, competitors with AI can make you obsolete.  If AI poses a
major existential threat to your business, incorporating AI must have the highest
priority. In the 2023 Gartner study, 7% cited business continuity as their reason
for embracing AI. This is more common for businesses involving document pro‐
cessing and information aggregation, such as financial analysis, insurance, and
data processing. This is also common for creative work such as advertising, web
design, and image production. You can refer to the 2023 OpenAI study, “GPTs
are GPTs” ( Eloundou et al., 2023), to see how industries rank in their exposure to
AI.
2. If you don’t do this, you’ll miss opportunities to boost profits and productivity.
Most companies embrace AI for the opportunities it brings. AI can help in most,
if not all, business operations. AI can make user acquisition cheaper by crafting
more effective copywrites, product descriptions, and promotional visual content.
AI can increase user retention by improving customer support and customizing
user experience. AI can also help with sales lead generation, internal communi‐
cation, market research, and competitor tracking.
3. You’re unsure where AI will fit into your business yet, but you don’t want to be left
behind. While a company shouldn’t chase every hype train, many have failed by
waiting too long to take the leap (cue Kodak, Blockbuster, and BlackBerry).
Investing resources into understanding how a new, transformational technology
can impact your business isn’t a bad idea if you can afford it. At bigger compa‐
nies, this can be part of the R&D department.19
Once you’ve found a good reason to develop this use case, you might consider
whether you have to build it yourself. If AI poses an existential threat to your busi‐
ness, you might want to do AI in-house instead of outsourcing it to a competitor.
Planning AI Applications | 29

However, if you’re using AI to boost profits and productivity, you might have plenty
of buy options that can save you time and money while giving you better
performance.
The role of AI and humans in the application
What role AI plays in the AI product influences the application’s development and its
requirements. Apple has a great document explaining different ways AI can be used
in a product. Here are three key points relevant to the current discussion:
Critical or complementary
If an app can still work without AI, AI is complementary to the app. For exam‐
ple, Face ID wouldn’t work without AI-powered facial recognition, whereas
Gmail would still work without Smart Compose.
The more critical AI is to the application, the more accurate and reliable the AI
part has to be. People are more accepting of mistakes when AI isn’t core to the
application.
Reactive or proactive
A reactive feature shows its responses in reaction to users’ requests or specific
actions, whereas a proactive feature shows its responses when there’s an opportu‐
nity for it. For example, a chatbot is reactive, whereas traffic alerts on Google
Maps are proactive.
Because reactive features are generated in response to events, they usually, but
not always, need to happen fast. On the other hand, proactive features can be
precomputed and shown opportunistically, so latency is less important.
Because users don’t ask for proactive features, they can view them as intrusive or
annoying if the quality is low. Therefore, proactive predictions and generations
typically have a higher quality bar.
Dynamic or static
Dynamic features are updated continually with user feedback, whereas static fea‐
tures are updated periodically. For example, Face ID needs to be updated as peo‐
ple’s faces change over time. However, object detection in Google Photos is likely
updated only when Google Photos is upgraded.
In the case of AI, dynamic features might mean that each user has their own
model, continually finetuned on their data, or other mechanisms for personaliza‐
tion such as ChatGPT’s memory feature, which allows ChatGPT to remember
each user’s preferences. However, static features might have one model for a
group of users. If that’s the case, these features are updated only when the shared
model is updated.
30 | Chapter 1: Introduction to Building AI Applications with Foundation Models

20 A running joke in the early days of generative AI is that AI startups are OpenAI or Claude wrappers.
It’s also important to clarify the role of humans in the application. Will AI provide
background support to humans, make decisions directly, or both? For example, for a
customer support chatbot, AI responses can be used in different ways:
• AI shows several responses that human agents can reference to write faster
responses.
• AI responds only to simple requests and routes more complex requests to
humans.
• AI responds to all requests directly, without human involvement.
Involving humans in AI’s decision-making processes is called human-in-the-loop.
Microsoft (2023) proposed a framework for gradually increasing AI automation in
products that they call Crawl-Walk-Run:
1. Crawl means human involvement is mandatory.
2. Walk means AI can directly interact with internal employees.
3. Run means increased automation, potentially including direct AI interactions
with external users.
The role of humans can change over time as the quality of the AI system improves.
For example, in the beginning, when you’re still evaluating AI capabilities, you might
use it to generate suggestions for human agents. If the acceptance rate by human
agents is high, for example, 95% of AI-suggested responses to simple requests are
used by human agents verbatim, you can let customers interact with AI directly for
those simple requests.
AI product defensibility
If you’re selling AI applications as standalone products, it’s important to consider
their defensibility. The low entry barrier is both a blessing and a curse. If something is
easy for you to build, it’s also easy for your competitors. What moats do you have to
defend your product?
In a way, building applications on top of foundation models means providing a layer
on top of these models. 20 This also means that if the underlying models expand in
capabilities, the layer you provide might be subsumed by the models, rendering your
application obsolete. Imagine building a PDF-parsing application on top of ChatGPT
based on the assumption that ChatGPT can’t parse PDFs well or can’t do so at scale.
Your ability to compete will weaken if this assumption is no longer true. However,
even in this case, a PDF-parsing application might still make sense if it’s built on top
Planning AI Applications | 31
