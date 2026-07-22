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
pipeline_stage: fact_extracted
id: ef72afff07f58f4d
manifest_dates:
- '2026-07-01'
source_type: news_media
tldr: Cognition 发布 Devin Fusion 多模型路由架构，采用主模型与辅助模型并行的"sidekick"方案，在 FrontierCode 编码基准上实现前沿级性能的同时将成本降低
  35%。
objective_summary: Cognition 于 2026 年 7 月发布 Devin Fusion，这是一种多模型智能体协作架构。其核心是让一个前沿模型作为主智能体负责规划与关键决策，一个成本更低的辅助智能体并行处理常规任务，两者各自维护独立的持久化缓存上下文。在
  Cognition 自建的前沿编码基准 FrontierCode 上，该系统以比纯前沿模型方案低 35% 的成本保持了同等水平的性能。Fable 5 在该架构下表现尤为突出，成本降幅达
  41%。该系统已在 app.devin.ai/signup 开放预览。
event_type: framework_tools
epistemic_status: pr_statement
entities:
  companies:
  - Cognition
  technologies:
  - Devin Fusion
  - FrontierCode
  - Fable 5
  - Smart Friend
  - GPT-5.5
  - Opus
  key_people: []
key_logic_flow:
- Cognition 发布 Devin Fusion 多模型路由系统，采用主模型与辅助模型并行运行的双智能体架构。
- 主智能体使用前沿模型，负责规划、模糊信息解读和最终审查；辅助智能体使用低成本模型，处理常规编程任务。
- 在自建的前沿编码基准 FrontierCode 上，Devin Fusion 以比纯前沿模型方案低 35% 的成本保持了同等性能水平。
- 与"Smart Friend"或"Advisor"等工具方案不同，辅助模型维护自己的持久化缓存上下文，避免了模型切换时的缓存未命中成本。
- Fable 5 在该架构下表现尤为出色，成本降幅达 41%，且智能性几乎不受影响。
- 系统在任务执行过程中使用轻量级分类器动态判断是否需要切换主模型或更换模型类型，以应对任务复杂度变化。
extract_result: success
object_mentions:
- object_type: product
  name: Devin Fusion
  canonical_name: Devin Fusion
  url: https://app.devin.ai/signup
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Cognition 发布 Devin Fusion 多模型路由系统，采用主模型与辅助模型并行的双智能体架构。
  - 在 FrontierCode 基准上以 35% 更低的成本保持了前沿模型级别的编码性能。
  - Devin Fusion 已在 app.devin.ai/signup 开放预览。
  article_id: ef72afff07f58f4d
- object_type: dataset
  name: FrontierCode
  canonical_name: FrontierCode
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Cognition 使用新基准 FrontierCode 衡量代码正确性与质量。
  - Devin Fusion 在 FrontierCode 上以 35% 更低的成本保持了前沿模型级别性能。
  article_id: ef72afff07f58f4d
- object_type: model
  name: Fable 5
  canonical_name: Fable 5
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Fable 5 在多智能体架构中表现出色，能更智能地分配任务、更高效地请求上下文。
  - Fusion 搭配 Fable 5 比纯 Fable 5 方案成本降低 41%，智能性几乎不受影响。
  article_id: ef72afff07f58f4d
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