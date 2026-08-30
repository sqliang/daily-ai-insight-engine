---
title: Replit Introduces Free Mode (4 minute read)
source: https://replit.com/blog/replit-introduces-free-mode?utm_source=tldrai
author: []
published: ''
created: '2026-08-21'
manifest_dates:
- '2026-08-21'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: f647dfdee4e66dd6
source_type: news_media
tldr: Replit 于 2026 年 8 月 18 日推出 Free Mode，该模式由 OpenAI 的 GPT-5.6 Luna 驱动，日常聊天与任务不再消耗积分，Core
  订阅用户以每月 20 美元即可获得 30 倍创作量与每月 30 小时聊天额度，并配套全新 UI 与 Power/Max 分级模式。
objective_summary: Replit 于 2026 年 8 月 18 日发布 Free Mode 与全新 UI，以降低 AI 软件创作的使用门槛。Free
  Mode 由 OpenAI 的 GPT-5.6 Luna 模型驱动，日常任务不再消耗积分，Core 订阅用户以每月 20 美元可获得 30 倍创作量和每月 30
  小时聊天额度，用量限制每 5 小时重置一次。Replit 将原 Economy Mode 更名为 Power Mode，并保留 Max Mode 用于复杂任务，Pro
  用户享有更高的使用额度。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Replit
  - OpenAI
  technologies:
  - GPT-5.6 Luna
  key_people: []
key_logic_flow:
- Replit 于 2026 年 8 月 18 日宣布推出 Free Mode，该模式由 OpenAI 的 GPT-5.6 Luna 模型驱动，日常任务不再消耗订阅积分。
- Free Mode 允许 Core 订阅用户以每月 20 美元的价格将创作量提升 30 倍，并享受每月最多 30 小时的聊天额度。
- Core 与 Pro 用户均可使用 Free Mode，用量限制每 5 小时重置一次，Pro 用户拥有比 Core 用户更高的使用额度。
- 当任务变得复杂或高价值时，Replit Agent 会建议切换到 Power Mode 或 Max Mode，二者分别对应成本优化模型与高性能模型。
- Replit 同步发布了全新 UI，将构思、创建、发布与增长整合进一个解决方案，并支持在简单聊天与复杂构建之间无缝切换。
object_mentions:
- object_type: product
  name: Replit Free Mode
  canonical_name: Replit Free Mode
  url: https://replit.com/blog/replit-introduces-free-mode
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Replit 于 2026 年 8 月推出 Free Mode，由 OpenAI 的 GPT-5.6 Luna 模型驱动，让 Core 订阅用户每月 20
    美元即可获得 30 倍的创作量提升。
  article_id: f647dfdee4e66dd6
- object_type: product
  name: Replit Agent
  canonical_name: Replit Agent
  url: https://replit.com
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Replit Agent 是 Replit 的 AI 软件创建代理，Free Mode 是其一种新的使用方式，且在任务变复杂或高价值时会建议用户切换到 Power
    Mode 或 Max Mode。
  article_id: f647dfdee4e66dd6
- object_type: product
  name: Power Mode
  canonical_name: Replit Power Mode
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Power Mode 原名 Economy Mode，采用成本优化的模型处理日常任务，以相同成本提供与原模式相同或更强的速度与质量表现。
  article_id: f647dfdee4e66dd6
- object_type: product
  name: Max Mode
  canonical_name: Replit Max Mode
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Max Mode 使用高性能模型处理更复杂的工作，适用于大规模变更、更深推理和更长时间的构建场景。
  article_id: f647dfdee4e66dd6
- object_type: model
  name: GPT-5.6 Luna
  canonical_name: GPT-5.6 Luna
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Free Mode 由 OpenAI 的 GPT-5.6 Luna 模型驱动，让用户在日常聊天、构思与任务中无需再消耗积分。
  article_id: f647dfdee4e66dd6
extract_result: success
impact_score:
  score: 6.0
  reason: Replit 是 AI 应用构建赛道的代表性玩家，本次将积分计费改为订阅制分层计价、日常任务零积分消耗，属于定价与产品体验层面的重要升级，可能促使
    Cursor、Copilot、Bolt 等竞品跟进类似的订阅制分层策略；同时 Free Mode 由 GPT-5.6 Luna 驱动，印证了模型推理成本下降已足以支撑日常任务大规模免费化。但该事件本质是现有产品内的功能与商业化调整，不构成技术范式转移，行业冲击范围限于
    AI 开发工具赛道，故给出 6 分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 日常任务不再消耗积分、订阅制下创作量大幅提升，个人开发者最关心 30x 的实际体验与免费额度的真实边界
hype_assessment:
  level: medium
  reason: 文章通篇使用 'The possibility is here'、'Insanely fast' 等情绪化表达，'30x more' 属于典型营销倍数口径（未说明基线任务与计费口径），'Free
    Mode' 名为免费实为订阅权益，且引用的用户证言全部来自 Early Access User，存在明显包装成分；但产品确实提供了实质变化——新模型接入（GPT-5.6
    Luna）、Free/Power/Max 三层定价分级、全新 UI——并非空壳炒作，故判定为中等炒作水分。
information_entropy: medium
domain_disruption:
  technical_innovation: 基于模型能力分层的任务路由架构：将日常低复杂度任务路由到 OpenAI GPT-5.6 Luna（成本优化型模型）实现零积分运行，复杂任务动态切换至
    Power/Max 高性能档，属于工程层面的推理成本优化设计；其本质依赖底层模型推理成本的大幅下降，而非全新算法突破。
  business_model: Replit 将 AI 编程从按量计费的'积分经济'转向订阅制分层定价，让日常使用边际成本归零，显著降低个人开发者与学习者的使用门槛，可能带动
    AI 编程工具赛道跟进类似的订阅制分层计费模式，重塑 AI 开发工具的成本结构与竞争格局。
engineering_complexity: production_ready
compound_value:
  score: 8.0
  reason: 投资逻辑：1）模型层商品化（GPT-5.6 作为可替换引擎）使价值向应用层迁移，Replit 用免费模式+订阅捆绑抢占分发入口，符合'模型降价→应用层复利'的经典路径；2）Free
    Mode 将计费范式从按 token 计量转向按订阅打包（30倍创作量、5小时重置窗口），培养高频使用习惯，沉淀社区网络效应与数据飞轮，具备跨周期积累属性；3）风险点在于底层模型深度依赖
    OpenAI，若 OpenAI/Anthropic 下探应用层，Replit 议价权受限；4）3-5 年维度上，若 Replit 能维持'构思-创建-发布-增长'全链路的心智占有，有望成为
    AI 软件创作的基础入口之一。综合 8.0 分，处于'细分赛道基础设施'偏强位置，仍需持续验证付费转化与用户留存。
value_capture_layer: end_application
moat_impact: creates_new_moat
key_beneficiaries:
- Replit
- OpenAI
- 独立开发者与小团队
competitive_casualty:
- Bolt
- Lovable
- 按 token/积分计费的中小 AI 编程工具
- 传统低代码平台（如 Bubble）
market_opportunities:
- AI 编程助手定价正从按量计费转向订阅制扁平模式，可借鉴 Replit 的 Free/Power/Max 三级设计，开发自适应模型路由中间层，按任务复杂度自动匹配性价比最优模型，帮助企业降低
  AI 使用成本
- GPT-5.6 Luna 支撑免费模式表明前沿模型推理成本已降至可支撑订阅制，创业者可沿此成本曲线寻找此前不经济的新场景，如面向个人开发者与中小团队的低价 AI
  自动化与创意工具
- Replit 将构思、创建、发布与增长整合为全链路解决方案，提示'从想法到上线'的一站式产品仍有缺口，可结合多 Agent 编排打造面向非开发者的垂直快速交付服务
risk_matrix:
  regulatory: 监管风险总体较低，但需关注：Replit 托管大量 AI 生成应用，若出现违规或侵权内容，平台责任认定可能趋严；欧盟 AI Act 对
    AI 编程辅助工具的透明度与责任划分仍在讨论；Replit 与 OpenAI 的深度绑定关系长期看可能招致反垄断与公平竞争审查
  technological: Free Mode 重度依赖 OpenAI GPT-5.6 Luna 单一模型，存在供应商锁定风险——若 OpenAI 调整定价、淘汰该模型，或开源模型（DeepSeek、Qwen
    等）追平能力，Replit 的成本结构与'30 倍创作量'承诺将承压
  competitive: AI 编码赛道竞争激烈，Cursor、GitHub Copilot、Windsurf 等对手可能跟进订阅制或发动价格战；更关键的是 OpenAI
    既是模型供应商又是潜在直接竞争者（Codex/ChatGPT 编码），使 Replit 的议价与差异化空间受限
  ethical: '''30 倍创作量''意味着更多未经专业审查的 AI 生成代码与应用涌入，可能放大安全漏洞与质量风险；用户专有代码交由第三方模型处理存在商业秘密与隐私泄露隐患，制约企业级采用；低门槛大规模
    AI 生成软件或加速初级开发岗位替代'
  additional:
  - 该事件为 PR 声明，'30 倍'系营销口径，实测额度可能受隐性限制，若与用户预期不符易引发舆论反噬；每 5 小时重置的计量方式不够透明，存在体验困惑风险
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: monitor
object_insights:
- object_type: product
  name: Replit Free Mode
  canonical_name: Replit Free Mode
  url: https://replit.com/blog/replit-introduces-free-mode
  positioning: Replit 推出的免费使用模式，由 GPT-5.6 Luna 驱动，日常任务不再消耗积分，让订阅用户以固定月费获得大幅提升的 AI
    软件创作额度。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Core 订阅用户
  - Pro 订阅用户
  - 高频日常 AI 创作的个人开发者与团队
  product_signal: 日常聊天、构思与任务不再消耗积分，Core 订阅用户每月 20 美元可获 30 倍创作量与 30 小时聊天额度，用量限制每 5
    小时重置一次。
  market_signal: 将免费档从入门体验升级为高质量生产力工具，以 20 美元月费切入大众 AI 软件创作市场，降低使用门槛并扩大订阅价值。
  differentiation: 与按积分计费的传统模式不同，Free Mode 让日常任务零成本运行，把复杂任务分流至 Power 与 Max 模式，形成分级计费体系。
  watch_reason: Replit 正从按量计费转向订阅内免费模式，反映 AI 应用层在模型成本下降后的定价范式转变，其分级模式设计与用户接受度值得持续跟踪。
  risk_notes:
  - 免费模式依赖 OpenAI GPT-5.6 Luna 单一大模型供应商，若模型成本或供应条款变动，可能影响该模式的可持续性。
  - 用量限制每 5 小时重置的机制较为复杂，重度用户可能仍需频繁切换 Power 或 Max 模式，体验存在摩擦。
  score: 8.0
  article_ids:
  - f647dfdee4e66dd6
  evidence_snippets:
  - Replit 于 2026 年 8 月推出 Free Mode，由 OpenAI 的 GPT-5.6 Luna 模型驱动，让 Core 订阅用户每月 20
    美元即可获得 30 倍的创作量提升。
- object_type: product
  name: Replit Agent
  canonical_name: Replit Agent
  url: https://replit.com
  positioning: Replit 的 AI 软件创建代理，负责将用户意图转化为可运行的应用，并根据任务复杂度自动推荐 Power、Max 等分级模式。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Replit 订阅用户
  - 在 Replit 上构建软件的个人开发者与团队
  product_signal: Agent 能理解工作全貌，在 Free Mode 下快速给出答案、建议与反馈，当任务变复杂或高价值时会主动建议切换至更高性能模式。
  market_signal: Replit 将 Agent 作为订阅免费模式的核心载体，通过降低使用门槛扩大用户基数，进而推动其 AI 软件创建平台的规模化增长。
  differentiation: Agent 根据任务复杂度自动建议切换 Power 或 Max 模式，以分级模式兼顾日常效率与复杂构建，区别于单一计费模式的竞品。
  watch_reason: Replit Agent 是平台体验的核心入口，其分级模式与免费策略的配合方式直接决定了 AI 软件创建工具的可用性与商业化平衡，值得持续观察其演进。
  risk_notes:
  - Agent 在不同模式间的切换依赖其自动判断，若判断不准可能造成用户成本或体验波动，影响信任度。
  score: 7.0
  article_ids:
  - f647dfdee4e66dd6
  evidence_snippets:
  - Replit Agent 是 Replit 的 AI 软件创建代理，Free Mode 是其一种新的使用方式，且在任务变复杂或高价值时会建议用户切换到 Power
    Mode 或 Max Mode。
- object_type: product
  name: Power Mode
  canonical_name: Replit Power Mode
  url: null
  positioning: Replit 的分级创作模式之一，由成本优化模型驱动，专注日常高频任务，在相同成本下提供更快或更优的速度与质量表现。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 日常高频任务的 Replit 用户
  - 对成本敏感的个人开发者
  product_signal: Power Mode 是原 Economy Mode 的更名升级，面向日常任务提供成本优化的速度与质量平衡，配合 Free Mode
    之外的持续构建场景。
  market_signal: Replit 通过更名与能力升级重新定位中档计费档位，丰富订阅体系的分级选择，以吸引对成本敏感的重度用户。
  differentiation: 以成本优化模型主打日常任务，与 Free Mode 的免费档和 Max Mode 的高性能档形成三级分层，覆盖不同复杂度与预算需求。
  watch_reason: Power Mode 作为中档计费层级，其定价与性能平衡直接反映 AI 应用层成本结构的演变，是观察 Replit 商业化策略与用户分层的关键样本。
  risk_notes:
  - Power Mode 采用成本优化模型，在复杂或长链路任务上的表现可能不如 Max Mode，存在任务错配风险。
  score: 6.0
  article_ids:
  - f647dfdee4e66dd6
  evidence_snippets:
  - Power Mode 原名 Economy Mode，采用成本优化的模型处理日常任务，以相同成本提供与原模式相同或更强的速度与质量表现。
- object_type: product
  name: Max Mode
  canonical_name: Replit Max Mode
  url: null
  positioning: Replit 面向复杂构建任务的高性能创作模式，使用更强模型支撑大规模变更、深层推理与长时间构建场景。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要复杂构建与深度推理的 Replit 用户
  - 进行大规模代码变更的专业开发者
  product_signal: Max Mode 调用高性能模型处理复杂工作，适合大规模代码变更与更深推理，是 Replit 分级模式中的顶配能力档。
  market_signal: Max Mode 为复杂高价值任务提供性能兜底，支撑 Replit 分级计费体系中的高端场景，其使用量反映平台复杂构建需求强度。
  differentiation: 与 Free Mode 和 Power Mode 不同，Max Mode 侧重深度推理与长构建，满足对质量要求最高的复杂任务场景。
  watch_reason: Max Mode 定义了 Replit 平台的能力上限，其性能表现与定价直接反映顶级 AI 模型在软件创建场景的落地效果，值得持续跟踪其复杂构建需求。
  risk_notes:
  - 高性能模型通常对应更高成本，Max Mode 的计费或额度限制可能制约其在高价值任务上的普及。
  score: 6.0
  article_ids:
  - f647dfdee4e66dd6
  evidence_snippets:
  - Max Mode 使用高性能模型处理更复杂的工作，适用于大规模变更、更深推理和更长时间的构建场景。
---

Title: Replit Introduces Free Mode to Expand What is Possible with AI

URL Source: https://replit.com/blog/replit-introduces-free-mode

Published Time: 2026-08-18T17:59:25.518Z

Markdown Content:
AI models are now capable and affordable enough to make once-unreachable outcomes practical. The opportunity for everyone to pursue and collaborate on ambitious ideas, spend less time on busywork, and raise the quality and creative output across disciplines is nearly here.

The possibility is here. But for most people, the reality is not.

[Replit users](https://replit.com/customers) are already building million-dollar businesses, replacing legacy software and saving hundreds of thousands of dollars, and increasing their everyday potential by creating high-quality software, designs, slides, and more.

But using AI today still means choosing models, managing context, watching usage, and juggling a growing collection of sprawling tools. Intelligence is now abundant, but access remains complicated.

That’s why today we’re launching a faster, more cost efficient, and capable Replit:

*   **Create up to 30X more with Free Mode:**Free Mode is a new way to use Agent that lets you create 30x more with just your monthly subscription. Spend less time thinking about usage and more time bringing ideas to life.
*   **A new UI built to get you straight to the outcome fast**: You can ideate, create, launch, and grow all in one solution, as Replit seamlessly transitions between simple chat and tasks to complex builds.

## **Create up to 30X more on Free Mode**

[Video 7](https://www.youtube.com/watch?v=gTzEh7fBe6o)

As models become more capable and cost-effective, people’s ability to create will only expand.

**Free Mode**, powered by OpenAI’s GPT-5.6 Luna, will allow everyone to create more for just the cost of their monthly subscription.

When you’re in Free Mode, every day tasks will no longer use credits, so whether you’re chatting, ideating, or running everyday tasks, you can create with freedom. This pairs the world’s most powerful AI software creation tool and agent with a mode designed for fast, high-value everyday tasks, giving users a true all-in-one option.

Core subscribers will now be able to **create 30X more than before** on Replit using Free Mode, as well as up to 30 hours per month of chat. For just $20 per month, creating real, high-quality projects at scale with AI is now accessible.

![Image 1: Create up to 30x more in Free Mode - Replit](https://cdnimg.replit.com/images/bj34pdbp/migration/f707d7986df0852dcd1a3f3d42ba1c31204f409e-2880x1506.png?w=3840&q=80&fit=max&auto=format)

> _**“We’re past the point of free options being a starting point. With Free Mode you’re getting quality, ready to put in front of people and start getting business.”**
> ~ Ken G (Early Access User)_

> _**“I was trying to find the outer limits of Free Mode. I haven’t yet. My choices are bolder because I’m not worrying about burning tokens.”**
> ~ Ruth H (Early Access User)_

Core and Pro users can use Free Mode until they reach their usage limits - which reset every 5 hours - or continue building in Power or Max Modes. Pro users will have even greater usage limits than Core customers.

![Image 2: Agent modes](https://cdnimg.replit.com/images/bj34pdbp/migration/b98442d9ddac5f1199398710ae47cd68f5be1694-2524x1378.png?w=3840&q=80&fit=max&auto=format)

If your work progresses to a more complex or high-value task, Replit Agent may suggest switching to our other Agent Modes, Power Mode and Max Mode.

*   **Power Mode** (formerly Economy Mode) uses cost-optimized models for everyday tasks, and delivers a strong balance of speed and quality. When using Power Mode, you will get the same, or greater performance you got in the former Economy Mode, for the same cost.
*   **Max Mode**uses higher-performance models for more complex work, which can be best for larger changes, deeper reasoning, and longer builds.

[Video 8](https://www.youtube.com/watch?v=JBxJahTvopA)

## **A Faster User Experience That Goes Straight to the Outcome**

For AI adoption to accelerate, users need an experience that just works - fast, efficient, accurate, high-quality, and grounded in the context of their world.

We’ve redesigned the Replit experience to make it your daily driver: an intelligent, always-on collaborator that understands you, works at your speed, and can handle everything from quick questions and data analysis to complex builds and great designs.

[Video 9](https://cdn.sanity.io/files/bj34pdbp/migration/0973a0b20e35d2360a3cdeb4a466f18200b1b12c.mp4)
With Replit, users can now get fast, accurate answers, suggestions, feedback, and analysis in seconds - without consuming usage credits in free mode. Because Agent understands the full context of your work, it can help you plan, ideate, shape, optimize, and explore ideas before shifting to a more complex build.

> **“Insanely fast!”**
> ~ Steve P (Early Access User)