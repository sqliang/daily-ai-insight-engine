---
title: Meet your new Slack coworker — Claude
source: https://www.therundown.ai/p/meet-your-new-slack-coworker-claude
author:
- '[[Zach Mink]]'
published: '2026-06-24'
created: '2026-06-24'
description: 'PLUS: Build a Clippy-like desktop pet for Codex'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: dbdce0f8b0fb62b6
source_type: newsletter_rss
tldr: Anthropic 推出 Claude Tag，可在 Slack 中被 @ 调用处理团队任务
objective_summary: Anthropic 于 2026 年 6 月 24 日发布 Claude Tag 功能，用户可在 Slack 频道中通过 @Claude
  分配任务，AI 自动分解任务阶段、使用授权工具执行并回复，支持跨频道上下文学习和环境模式主动跟进，适用于工程到营销等多领域任务。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  technologies:
  - Claude Tag
  - Claude Code
  - Claude Cowork
  - LLM
  key_people:
  - Andrej Karpathy
key_logic_flow:
- Anthropic 推出 Claude Tag 功能，团队可在 Slack 频道中通过 @Claude 标签调用 AI 处理任务。
- Claude Tag 将任务自动分解为多个阶段，使用经授权的工具和数据逐步完成，完成后在频道中回复结果。
- Claude 可跨频道构建上下文并学习团队工作模式，但仅在拥有访问权限的频道中执行操作。
- Claude Tag 具备环境模式（ambient mode），可主动从相关频道获取信息并跟进已沉寂但需关注的任务。
- Andrej Karpathy 评价 Claude Tag 为 LLM UI/UX 的第三次重大重新设计。
extract_result: success
impact_score:
  score: 7.0
  reason: 这是一次重要的产品发布，短期内将显著改变 AI 在团队协作中的落地形态。Claude Tag 将此前仅限于个人开发者（Claude Code）和个人桌面（Claude
    Cowork）的代理能力带入 Slack——这一企业沟通的核心阵地。其价值在于：① 降低 AI 协作门槛，非技术团队也能在自然对话流中调度 AI 执行复杂任务；②
    环境模式（ambient mode）和跨频道上下文学习是真实的产品创新，比单纯的 'AI 聊天机器人' 进了一大步；③ Karpathy 将其称为 LLM
    UI/UX 第三次重大重新设计具有信号意义。但不足以达到 8 分以上的范式转移级别，因为 Slack bot 集成并非全新概念，只是 Claude 在代理能力成熟度上做到了质的飞跃。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 团队级 AI 代理工作流范式——在 Slack 中 @AI 执行多阶段任务，标志着 AI 从 '个人工具' 向 '团队协作者' 的转变
hype_assessment:
  level: medium
  reason: 产品本身是实打实的干货，已正式上线可使用。但 '3rd major redesign of LLM UI UX' 这一表述存在一定 PR 包装成分——Slack
    bot 集成并非全新概念，此前已有多个 AI 助手通过 Slack API 实现类似功能。Claude Tag 真正的差异化在于代理能力深度（任务自动分解、工具调用、环境模式），而非交互范式层面的彻底革命。
information_entropy: high
domain_disruption:
  technical_innovation: 环境模式（ambient mode）与跨频道上下文学习的结合是核心突破。传统 Slack bot 仅被动响应 @提及，而
    Claude Tag 可主动从有访问权限的频道获取信息，追踪已沉寂但需要关注的任务。这本质上是一种 '主动代理' 架构——LLM 从 '指令-响应' 范式升级为
    '持续感知-有条件介入' 范式，对任务编排和上下文窗口管理提出了更高的工程要求。
  business_model: 直接冲击一批 'AI 同事/代理员工' 创业公司。此前市场上存在大量定位于 Slack 内 AI 助手的初创企业（如各种 agentic
    coworker 产品），Anthropic 凭借品牌认知度和底层模型能力优势，可能快速吞噬这个细分市场。同时也为 Slack/企业协作软件的 AI 集成设定了新基准，迫使竞品（如
    Microsoft Copilot、Google Gemini for Workspace）加速迭代。
engineering_complexity: production_ready
compound_value:
  score: 8.5
  reason: Claude Tag 将 AI Agent 嵌入 Slack 这一企业协作高频场景，具备极强的数据网络效应和组织级锁定能力。团队越使用，Claude
    积累的跨频道上下文越丰富，理解团队工作模式越深，切换成本指数级上升，形成 'context moat'。Ambient mode 和跨频道主动跟进能力使产品从被动工具进化为主动协作成员，显著提升粘性和不可替代性。Karpathy
    评价为 'LLM UI/UX 第三次重大重新设计'，暗示交互范式的代际跃迁。从资本视角看，这是 Anthropic 从卖模型能力向卖企业工作流基础设施的战略升维——一旦成为企业协作的
    '隐形同事'，定价权和续约率将远超 API 调用付费模式。主要风险在于：依赖 Slack 生态（非自有渠道）、Microsoft/Google 在企业协作
    AI 的强力反制、以及企业数据隐私合规挑战。但考虑到 Slack 在企业端的广泛渗透和 Anthropic 的先发优势，3-5 年内大概率成为企业 AI Agent
    的标配入口。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- Slack (Salesforce)
- Salesforce
competitive_casualty:
- 独立 AI Agent 初创公司
- Microsoft Copilot for Teams
- 传统企业聊天机器人平台
- 无界面 LLM 中间件厂商
market_opportunities:
- 企业可围绕 Claude Tag 构建 Slack 专属的 AI 工作流自动化模板，覆盖工程冲刺管理、营销排期、客户跟进等高频协作场景，打包为可复用的行业解决方案
- 建议创业团队关注 Slack + AI Agent 集成生态中的安全审计与合规监控工具，因为 AI 跨频道操作会带来数据访问权限管理的刚需
- AI 培训与变革管理咨询服务将迎来新需求——帮助企业团队设计 @Claude 的任务分配规范、权限策略和异常处理流程
risk_matrix:
  regulatory: 数据跨境与隐私合规风险：Claude Tag 可跨频道读取企业内部对话数据，经 Anthropic 处理，需关注 GDPR、CCPA 等法规下的数据处理协议和用户知情同意要求
  technological: 平台锁定风险：深度依赖 Anthropic API 和 Slack 生态，若 OpenAI/Google 推出竞品集成至 Teams/Discord，可能分化生态；Claude
    Tag 当前功能成熟度（幻觉率、工具调用可靠性）仍需检验
  competitive: 巨头入场挤压：Microsoft Copilot for Teams、Google Gemini for Workspace 均在同一赛道，Slack
    自身也可能自建 AI 原生功能；大量 AI 虚拟同事初创公司面临生态级碾压
  ethical: 就业冲击与信任风险：AI 逐步接管协调型任务可能减少初级/协调类岗位需求；AI 在跨频道异步回复中出现事实错误或不当回复将直接影响团队信任和决策质量
  additional:
  - Slack 平台政策变更风险（API 限流、费用调整、功能限制可能影响集成稳定性）
  - 定价不确定性：尚无明确定价模型，企业预算规划面临不确定性
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
---

Good morning, AI enthusiasts. Your Slack workspace has a new coworker — Claude.

Anthropic just debuted Claude Tag, which brings the agentic capabilities previously limited to Claude Code and Cowork into Slack channels, enabling entire teams to simply tag the AI to handle tasks ranging from engineering to marketing.

The Rundown: Anthropic just launched Claude Tag, a new way to make its AI assistant available inside Slack, letting teams tag it like a teammate to handle tasks asynchronously and build context across channels, codebases, and tools over time.

The details:

While Claude Code brought agentic capabilities to individuals, Claude Tag takes it to teams, with the AI handling tasks for members in a Slack channel.

You just have to tag @Claude with the task, and the AI will break it into stages, work through them using approved tools and data, and respond when done.

Claude learns over time, builds context about the work being done, and can even take action across different channels — but only where it has access.

It also uses an ambient mode, where Claude fetches information from relevant channels and follows up on tasks that have gone quiet and may need attention.

Why it matters: Andrej Karpathy calls Claude Tag the “3rd major redesign of LLM UI UX,” and it’s hard to disagree. Going from chat and desktop to Slack — where most business context and tools live — is a natural next step. With Anthropic already rolling it out today, this release will surely hurt more than a few “agentic coworker” startups.

The Rundown: HubSpot’s free, comprehensive “How to Use ChatGPT at Work” guide provides 100+ ready-to-use prompts to help professionals boost efficiency and adopt AI-driven workflows.

Inside, you’ll find:

A quick crash course to master ChatGPT in under 30 minutes

Practical industry use cases to spark real-world inspiration

100+ prompts to streamline tasks and accelerate productivity

Expert tips to tackle common AI roadblocks with confidence

The Rundown: Meta is doubling down on the AI wearable space with the launch of “Meta Glasses,” a new $299 line of smart glasses built in partnership with EssilorLuxottica and powered by its Muse Spark AI out of the box.

The details:

Meta Glasses come in three designs — Meta Adventurer, Meta Fury, and Meta Glasses by Kylie — spanning 26 styles across colors, lenses, and frames.

The Kylie variant, at $399, is designed to be a fan-favorite with an embedded gem, a custom chime, and the option to use Kylie Jenner’s voice for Meta AI.

The glasses use Meta’s Muse Spark AI, promising smarter answers, better visual understanding, turn-by-turn navigation, and live translation.

While the hardware remains the same as previous models, the price is the highlight, with Meta ditching the Ray-Ban/Oakley branding for affordability.