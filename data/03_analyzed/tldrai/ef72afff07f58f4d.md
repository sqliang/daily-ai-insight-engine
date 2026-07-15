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
tldr: Cognition 发布 Devin Fusion，双智能体并行架构实现 35% 成本降低
objective_summary: Cognition 在其博客中宣布推出 Devin Fusion，一种多模型路由架构。该架构并行运行前沿模型主智能体与低成本"副手"模型，主智能体负责关键决策并动态委派任务。在
  FrontierCode 编码基准上保持前沿性能的同时降低 35% 成本，与 Fable 5 搭配时成本降低 41%。
event_type: framework_tools
epistemic_status: pr_statement
entities:
  companies:
  - Cognition
  technologies:
  - Devin Fusion
  - FrontierCode
  - Fable 5
  - Opus
  - GPT-5.5
  key_people: []
key_logic_flow:
- Devin Fusion 的核心架构是并行运行两个智能体：一个使用前沿模型（主智能体），另一个使用低成本"副手"模型，两者各自拥有独立工具集和缓存的上下文。
- 主智能体负责制定计划、解读模糊性、最终审查等关键决策，默认情况下应最小化自身操作，将任务委托给副手并监控执行。
- 该架构解决了传统模型路由的三个问题：保留真实前沿智能而非仅优化基准分数、可泛化到单提示任务之外的复杂场景、通过保持各自独立缓存避免切换模型时的高成本缓存未命中。
- 在 FrontierCode 编码基准测试中，Devin Fusion 保持前沿和 Fable 5 级性能的同时降低了 35% 成本。
- 使用轻量级分类器在任务执行过程中动态判断何时需要切换回主智能体或改用不同模型，实现动态会话中路由。
- Fable 5 在该多智能体设置中表现尤为出色，比纯 Fable 5 方案便宜 41%，表明副手模式将随基础模型进步而变得更有效。
extract_result: success
impact_score:
  score: 6.5
  reason: 该事件属于重要的产品功能发布，影响集中于AI编程助手细分赛道。评分依据：1) Devin Fusion的双智能体并行架构（sidekick模式）解决了一个真实工程痛点——低成本模型与前沿模型之间的高效路由，特别是独立缓存上下文的方案避免了传统模型切换的高昂缓存未命中开销，这算得上工程架构上的实质性创新；2)
    35-41%的成本降低幅度可观，有量化数据支撑，且结合Fable 5的协同效应暗示了该范式的可扩展性；3) 但所有数据来自Cognition自家的FrontierCode基准测试，缺乏独立第三方验证，且产品目前处于预览阶段，尚未经受大规模用户检验。综合判断，该发布对AI编程助手赛道的局部竞争格局有明显重塑力（存量对手如Cursor、Copilot需跟进应对），但尚未达到行业范式转移的级别。
sentiment: positive
developer_sentiment:
  tone: skeptical
  primary_focus: 35%成本降低的基准测试是否在真实编码场景中可复现，以及独立缓存上下文在实际工程中的稳定性
hype_assessment:
  level: medium
  reason: 存在一定包装但非空壳炒作。判定依据：1) 识别到'lighting money on fire''substantially better'等煽动性PR用语，以及推出新的自定基准FrontierCode替代通用基准的营销策略；2)
    然而核心架构描述（双智能体并行+独立缓存上下文+动态路由分类器）有实质技术含量，指出了模型路由领域三个真实痛点（基准过拟合、单提示泛化不足、缓存未命中），这些分析对一线AI工程师有信息价值；3)
    整体呈现'有干货但在自家测试环境里包装了营销话术'的中等水分状态。
information_entropy: medium
domain_disruption:
  technical_innovation: 双智能体并行架构的核心突破在于让主智能体与低成本'副手'智能体各自维护独立的工具集和缓存上下文，主智能体负责计划制定、模糊性解读和最终审查等关键决策，默认最小化自身操作并将任务委派给副手。这解决了传统模型路由的三个根本问题：保留真正的前沿智能而非仅优化基准分数、可泛化到复杂多步骤任务而非局限于单提示场景、避免了模型切换时的高成本缓存未命中（因为各自上下文独立缓存）。动态会话中路由通过轻量级分类器实时判断何时需要切换回主智能体或改用不同模型，是关键的工程落地创新。
  business_model: 通过降低35-41%的API调用成本，AI编程助手的经济账从'每个任务都要烧昂贵模型'变为'大多数任务由廉价副手完成、关键决策由前沿模型把关'的分层计费模式，有望推动AI编码工具从高端实验品向日常生产工具转变。这一模式可能促使Cursor、GitHub
    Copilot等竞品跟进类似的混合路由策略，引发行业性的成本下降竞争和定价模式重塑。
engineering_complexity: prototype
compound_value:
  score: 8.0
  reason: Devin Fusion 的核心架构洞见——并行运行前沿模型主智能体与低成本副手模型，且各自维护独立缓存上下文——解决了一个根本性且日益恶化的问题：AI
    Agent 的成本失控。该模式的复利效应体现在三个层面：第一，动态路由中的轻量级分类器会随数据积累持续优化，形成数据飞轮；第二，Fable 5 实验证明，基础模型越强，副手模式的成本节省越显著（41%
    vs 35%），这意味着随时间推移该架构的价值不降反升；第三，该模式不仅适用于编码 Agent，可泛化至任何需要多步骤推理的 Agent 场景，具备成为 Agent
    架构默认范式的潜力。最主要的风险在于 Cognition 将该模式作为闭源产品功能而非开放标准，限制了生态扩散速度。但作为一家 Agent 公司的核心基础设施，其在
    3-5 年内大概率是行业标杆级架构设计。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Cognition
- Anthropic
- OpenAI
competitive_casualty:
- Cursor
- GitHub Copilot
- Replit Agent
- 单一模型路由方案提供商
market_opportunities:
- 企业AI工程团队可借鉴Devin Fusion的双智能体并行架构，在内部AI工作流中实现成本优化，通过将前沿模型委派给关键决策、低成本模型处理常规任务来降低AI基础设施支出
- 创业者可基于"副手"模式开发通用型模型路由中间件，为中小团队提供动态模型选择与缓存共享的开源或SaaS解决方案
- AI Agent平台可集成类似的动态会话中路由（lightweight classifier），根据任务复杂度实时切换模型，提升用户体验同时控制推理成本
risk_matrix:
  regulatory: 依赖多个第三方模型API可能涉及数据跨境传输合规问题，需关注各模型提供商的隐私政策和数据使用条款
  technological: 缓存5分钟过期限制是工程化瓶颈，若无法有效解决将影响实际部署效果；该架构依赖特定模型组合（如Fable 5），模型API定价或可用性变化可能削弱优势
  competitive: Anthropic、OpenAI等模型提供商可能直接在API层内置类似路由能力，挤压第三方路由方案的生存空间；LangChain等LLM编排框架也可能快速跟进实现类似模式
  ethical: 低成本副手模型可能在非关键任务中积累偏差决策，尤其在代码审查等场景存在引入隐式缺陷的风险
  additional:
  - 模型API定价变动风险——当前成本优势建立在特定模型价差基础上，若上游调价则优势可能被快速侵蚀
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
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