---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 177
section-title: Feedback Limitations
source-location: pages 514-515
previous-section: AI Space/normalized/pdf/ai-engineering/sections/176-feedback-design.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/178-summary.md
classification: reusable-knowledge-candidate
---
# Feedback Limitations

12 The options suggested here are only to show how options can be rewritten. They haven’t been validated.
Feedback Limitations
There’s no doubt of the value of user feedback to an application developer. However,
feedback isn’t a free lunch. It comes with its own limitations.
Biases
Like any other data, user feedback has biases. It’s important to understand these bia‐
ses and design your feedback system around them. Each application has its own bia‐
ses. Here are a few examples of feedback biases to give you an idea of what to look out
for:
Leniency bias
Leniency bias is the tendency for people to rate items more positively than war‐
ranted, often to avoid conflict because they feel compelled to be nice or because
it’s the easiest option. Imagine you’re in a hurry, and an app asks you to rate a
transaction. You aren’t happy with the transaction, but you know that if you rate
it negatively, you’ll be asked to provide reasons, so you just choose positive to be
done with it. This is also why you shouldn’t make people do extra work for your
feedback.
On a five-star rating scale, four and five stars are typically meant to indicate a
good experience. However, in many cases, users may feel pressured to give fivestar ratings, reserving four stars for when something goes wrong. According to
Uber, in 2015, the average driver’s rating was 4.8, with scores below 4.6 putting
drivers at risk of being deactivated.
This bias isn’t necessarily a dealbreaker. Uber’s goal is to differentiate good driv‐
ers from bad drivers. Even with this bias, their rating system seems to help them
achieve this goal. It’s essential to look at the distribution of your user ratings to
detect this bias.
If you want more granular feedback, removing the strong negative connotation
associated with low ratings can help people break out of this bias. For example,
instead of showing users numbers one to five, show users options such as the fol‐
lowing:
• “Great ride. Great driver.”
• “Pretty good.”
• “Nothing to complain about but nothing stellar either.”
• “Could’ve been better.”
• “Don’t match me with this driver again.” 12
490 | Chapter 10: AI Engineering Architecture and User Feedback

Randomness
Users often provide random feedback, not out of malice, but because they lack
motivation to give more thoughtful input. For example, when two long responses
are shown side by side for comparative evaluation, users might not want to read
both of them and just click on one at random. In the case of Midjourney, users
might also randomly choose one image to generate variations.
Position bias
The position in which an option is presented to users influences how this option
is perceived. Users are generally more likely to click on the first suggestion than
the second. If a user clicks on the first suggestion, this doesn’t necessarily mean
that it’s a good suggestion.
When designing your feedback system, this bias can be mitigated by randomly
varying the positions of your suggestions or by building a model to compute a
suggestion’s true success rate based on its position.
Preference bias
Many other biases can affect a person’s feedback, some of which have been dis‐
cussed in this book. For example, people might prefer the longer response in a
side-by-side comparison, even if the longer response is less accurate—length is
easier to notice than inaccuracies. Another bias is recency bias, where people tend
to favor the answer they see last when comparing two answers.
It’s important to inspect your user feedback to uncover its biases. Understanding
these biases will help you interpret the feedback correctly, avoiding misleading prod‐
uct decisions.
Degenerate feedback loop
Keep in mind that user feedback is incomplete. You only get feedback on what you
show users.
In a system where user feedback is used to modify a model’s behavior, degenerate
feedback loops  can arise. A degenerate feedback loop can happen when the predic‐
tions themselves influence the feedback, which, in turn, influences the next iteration
of the model, amplifying initial biases.
Imagine you’re building a system to recommend videos. The videos that rank higher
show up first, so they get more clicks, reinforcing the system’s belief that they’re the
best picks. Initially, the difference between the two videos, A and B, might be minor,
but because A was ranked slightly higher, it got more clicks, and the system kept
boosting it. Over time, A’s ranking soared, leaving B behind. This feedback loop is
why popular videos stay popular, making it tough for new ones to break through.
This issue is known as “exposure bias,” “popularity bias,” or “filter bubbles,” and it’s a
well-studied problem.
User Feedback | 491
