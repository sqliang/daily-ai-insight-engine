---
title: Devin Fusion (8 minute read)
source: https://cognition.com/blog/devin-fusion?utm_source=tldrai
author: []
published: ''
created: '2026-07-01'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: ef72afff07f58f4d
---

Engineering teams are lighting money on fire.

It's no longer sustainable to use the most expensive models on every task. But existing tools for mixing models suck. They look nice on most benchmarks but fail to write code you'd actually merge.

At Cognition, we specialize in routing across frontier models without sacrificing intelligence. Today, we're sharing our work on a new kind of multi-model harness, **Devin Fusion**, that is substantially better at mixing models while reducing costs and maintaining intelligence on real-world usage. We found it maintains **frontier and Fable 5-level performance at 35% lower cost** on FrontierCode, a new state-of-the-art coding benchmark that measures both code correctness and quality.

In the rest of this post, we break down why good model routing is so hard, and the two techniques that make it all work: **the "sidekick" approach and dynamic mid-session routing**.

We welcome you to try Devin Fusion in preview at app.devin.ai/signup.

The key idea behind our architecture is to run two parallel agents: one with a frontier model, the other with a more cost-effective "sidekick" model. Both are fully capable agents with their own toolsets and ability to gather & act on their own context.

As the task progresses, the main agent decides which tasks to give the sidekick and which tasks to do itself. Making sidekick work well in practice, however, requires deeply tuning the interaction patterns. We've found that the main agent should take minimal actions, and only read what is absolutely necessary. By default it should delegate and monitor, while making the significant decisions: the plan, the interpretation of ambiguity, the final review.

This approach fixes the primary problems with more basic model routing:

**It retains real frontier intelligence rather than "benchmark-score" intelligence.**Routers often over-fit to specific benchmarks. By keeping a frontier model in the mix, the sidekick approach continues to benefit from frontier model creativity and general intelligence.**It generalizes beyond single-prompt tasks and question-answering.**Model routers often route to a single model for the entire task. Prompts often do not contain enough information about the task to properly discern difficulty. Moreover, the user might have difficult followups to simple initial prompts. Being able to move between the smart model and sidekick dynamically makes this system much more robust.**It avoids costly cache misses when routing between models.**We've previously explored a "Smart Friend" tool, and Anthropic released a similar "Advisor" tool. The core of both these ideas is to give one model a tool to query another model for helpful advice. The catch? Upon every call to the other model, the context for the task is not shared in a way that is cached, and you pay a very expensive price. In the sidekick setup, both the main model and sidekick model maintain their own persistent, cached contexts.

Of course, there are many implementation details we had to overcome to achieve the capabilities of Devin Fusion. For example, most cached inputs only have a 5-minute expiry. We encourage the reader to think about how to engineer around this. We'd love to trade notes!

Recent models, and Fable 5 especially, perform unusually well in these multi-agent setups. Fable delegates work more intelligently, requests context more efficiently, and plans more precisely, all of which yield a larger cost improvement with minimal impact on intelligence. This suggests that the sidekick pattern is one that will become more useful as base models get better.

In our testing, Fusion with Fable 5 is 41% cheaper than a pure Fable 5 harness, versus 35% with Opus and GPT-5.5-level models. That gap may look modest, but we believe it understates the real difference. The non-Fable numbers reflect many rounds of tuning of the Devin Fusion harness; the Fable 5 numbers don't, since access was cut off before we could apply them.*

To better understand how the sidekick works, we inspected how using sidekick impacts cost and performance on a representative sample of FrontierCode tasks. Here we present both good and bad examples of sidekick usage.

With sidekick in your arsenal, you must still make sure to choose the right models for the task. We decide on different models for the main agent or sidekick depending on task type and complexity. It can be dangerous, however, to choose a model at the start and then realize later on that a different one would be better suited. Similarly, you might also want to move the task from the sidekick back to the main agent if it is proving too challenging. To handle these cases, we use lightweight classifiers during task execution to signal when we need to switch to the main agent or use a different model entirely.