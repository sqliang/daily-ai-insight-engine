---
title: '🤖 AI Agents Weekly: GPT-5.6 Family, Meta Muse Spark 1.1, Grok 4.5, SWE-1.7,
  Robostral Navigate, The Harness Effect, and More'
source: https://nlp.elvissaravia.com/p/ai-agents-weekly-gpt-56-family-meta
author: []
published: '2026-07-11'
created: '2026-07-14'
description: GPT-5.6 Family, Meta Muse Spark 1.1, Grok 4.5, SWE-1.7, Robostral Navigate,
  The Harness Effect, and More
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 5d9bcda5ffff8971
manifest_dates:
- '2026-07-14'
- '2026-07-15'
source_type: newsletter_rss
tldr: OpenAI 发布 GPT-5.6 系列模型（Sol/Terra/Luna）并推出 ChatGPT Work 智能体；Meta 发布 Muse Spark
  1.1 多模态推理模型并开放 Meta Model API。xAI、Cognition、Mistral 等公司相继发布编码模型，Google 和 Tencent
  分别开源了 Gemma 4 和 Hy3 模型。
objective_summary: 本期 AI Agents Weekly 报道了多项 AI 产品发布与更新。OpenAI 发布了 GPT-5.6 系列模型，包含旗舰版
  Sol、中端 Terra 和经济型 Luna，已在 ChatGPT、Codex 和 API 上线，同时推出了 ChatGPT Work 智能体和 GPT-Live
  语音产品。Meta Superintelligence Labs 发布了 Muse Spark 1.1 多模态推理模型，在 MCP Atlas 等智能体基准测试中取得
  SOTA 成绩，并首次向开发者开放了 Meta Model API。xAI 发布 Grok 4.5、Cognition 发布 SWE-1.7（推理速度 1000
  tok/s）、Mistral 发布 Robostral Navigate 等编码模型。Google 开源了 Gemma 4 模型，Tencent 开源了 295B
  参数的 Hy3 模型。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - OpenAI
  - Meta
  - xAI
  - Cognition
  - Mistral
  - Google
  - Tencent
  - Nous Research
  - Microsoft
  - Ternlight
  - Databricks
  - FrontierFinance
  - Sakana AI
  - Anthropic
  technologies:
  - GPT-5.6
  - MCP
  - VLM
  key_people: []
key_logic_flow:
- OpenAI 发布了 GPT-5.6 系列模型，包含 Sol、Terra 和 Luna 三个能力层级，已在 ChatGPT、Codex 和 API 上线，Sol
  定价为输入/输出每百万 token 5/30 美元。
- Meta Superintelligence Labs 发布了 Muse Spark 1.1 多模态推理模型，支持原生工具、MCP 服务器和自定义技能，可作为主智能体规划并委派任务给并行子智能体。
- Muse Spark 1.1 在 MCP Atlas 基准上取得 88.1 的 SOTA 分数，支持 100 万 token 上下文窗口，Meta Model
  API 定价为每百万输入/输出 token 1.25/4.25 美元。
- OpenAI 推出了 ChatGPT Work 智能体产品和 GPT-Live 语音产品，进一步扩展了 AI 代理在工作和语音场景中的应用。
- xAI 发布 Grok 4.5 编码模型、Cognition 发布 SWE-1.7（推理速度 1000 tok/s）、Mistral 发布 Robostral
  Navigate，多家公司聚焦编码能力的 AI 模型。
- Google 开源了 Gemma 4 模型，Tencent 开源了 295B 参数的 Hy3 模型，Microsoft 发布了用于智能体的 Flint 框架。
extract_result: success
object_mentions:
- object_type: model
  name: GPT-5.6 family (Sol, Terra, Luna)
  canonical_name: GPT-5.6
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - OpenAI 开始推出 GPT-5.6 系列模型 Sol、Terra 和 Luna，覆盖 ChatGPT、Codex 和 API。
  - Sol 是旗舰型号，Terra 匹配 GPT-5.5 且成本更低，Luna 速度最快价格最低。
  - GPT-5.6 是 Codex 和 ChatGPT Work 的默认大脑，针对长时间工具使用和编码进行优化。
  article_id: 5d9bcda5ffff8971
- object_type: model
  name: Muse Spark 1.1
  canonical_name: Muse Spark
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Meta Superintelligence Labs 发布了 Muse Spark 1.1 多模态推理模型，专为智能体任务设计。
  - Muse Spark 1.1 在 MCP Atlas（88.1）、JobBench（54.7）等基准测试中取得 SOTA 成绩。
  - 该模型支持 100 万 token 上下文窗口，适用于长时间多模态工作场景。
  article_id: 5d9bcda5ffff8971
- object_type: product
  name: ChatGPT Work
  canonical_name: ChatGPT Work
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - OpenAI 推出了 ChatGPT Work 智能体，由 GPT-5.6 作为默认大脑驱动。
  article_id: 5d9bcda5ffff8971
- object_type: product
  name: Meta Model API
  canonical_name: Meta Model API
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Meta 首次向开发者开放了 Meta Model API，目前处于公开预览阶段。
  - Meta Model API 定价为每百万输入/输出 token 1.25/4.25 美元，新账户可获 20 美元免费额度。
  article_id: 5d9bcda5ffff8971
- object_type: model
  name: Grok 4.5
  canonical_name: Grok 4.5
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - xAI 发布了 Grok 4.5 模型，专注于提升编码能力。
  article_id: 5d9bcda5ffff8971
- object_type: model
  name: SWE-1.7
  canonical_name: SWE-1.7
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Cognition 发布了 SWE-1.7 模型，推理速度达到每秒 1000 个 token。
  article_id: 5d9bcda5ffff8971
- object_type: model
  name: Robostral Navigate
  canonical_name: Robostral Navigate
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Mistral 发布了 Robostral Navigate 模型，作为新推出的 AI 产品之一。
  article_id: 5d9bcda5ffff8971
- object_type: product
  name: GPT-Live
  canonical_name: GPT-Live
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - OpenAI 推出了 GPT-Live 语音产品，扩展了 AI 语音交互能力。
  article_id: 5d9bcda5ffff8971
- object_type: model
  name: Gemma 4
  canonical_name: Gemma 4
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Google 开源了 Gemma 4 模型，供开发者使用。
  article_id: 5d9bcda5ffff8971
- object_type: model
  name: Hy3
  canonical_name: Hy3
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Tencent 开源了 295B 参数的 Hy3 模型。
  article_id: 5d9bcda5ffff8971
- object_type: product
  name: Codex
  canonical_name: Codex
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - GPT-5.6 成为 Codex 的默认大脑，Codex 桌面应用将合并到 ChatGPT 的 Windows 和 Mac 应用中。
  article_id: 5d9bcda5ffff8971
- object_type: project
  name: Flint
  canonical_name: Flint
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Microsoft 发布了用于智能体的 Flint 框架和工具。
  article_id: 5d9bcda5ffff8971
- object_type: project
  name: Hermes Agent
  canonical_name: Hermes Agent
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Nous Research 将 Hermes Agent 部署到了云端。
  article_id: 5d9bcda5ffff8971
- object_type: product
  name: Cloud Run sandboxes
  canonical_name: Cloud Run sandboxes
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Google 推出了 Cloud Run sandboxes 沙箱产品。
  article_id: 5d9bcda5ffff8971
- object_type: product
  name: Ternlight
  canonical_name: Ternlight
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Ternlight 实现了在浏览器中运行嵌入向量计算的功能。
  article_id: 5d9bcda5ffff8971
impact_score:
  score: 7.0
  reason: 核心事件是OpenAI正式推出GPT-5.6系列（Sol/Terra/Luna三档能力层级）和Meta首次向开发者开放Muse Spark 1.1
    API。评分依据：① GPT-5.6是GPT-5代的渐进式升级（Terra仅匹配GPT-5.5水平），但Sol/Terra/Luna层级化产品策略是重要的商业创新，让开发者按需选择能力/成本平衡点，这改变了API经济的定价范式；②
    Muse Spark 1.1在多个Agent基准测试（MCP Atlas 88.1、JobBench 54.7超越Opus 4.8和GPT-5.5）取得SOTA，且Meta首次开放API定价仅为$1.25/4.25，显著低于OpenAI，这打破了AI模型API市场的双寡头格局，预示着价格战升级；③
    两者都聚焦Agent优化（GPT-5.6为Codex和ChatGPT Work设计，Muse Spark支持主智能体+并行子智能体编排），说明Agent能力已成为模型竞争的主战场。综合来看，这是重要的产品发布和竞争格局重塑事件，但不属于范式转移级别（并非ChatGPT发布或Transformer论文那样的根本性变革）。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: Meta首次开放Muse Spark 1.1 API的定价仅为OpenAI同级模型的1/4，叠加GPT-5.6的层级化定价体系，将大幅降低Agent应用的模型调用成本
hype_assessment:
  level: low
  reason: 文章未使用'革命性'、'颠覆性'等PR夸大词汇，以事实报道为主。OpenAI和Meta的发布均为实际可用的产品（GPT-5.6已集成至ChatGPT/Codex/API，Muse
    Spark 1.1 API处于公开预览）。基准测试分数具体可验证（MCP Atlas 88.1、JobBench 54.7等），定价信息明确透明（$1.25~$5/百万输入Token）。属于真实产品发布和工程进展的正常报道，无明显水分。
information_entropy: high
domain_disruption:
  technical_innovation: GPT-5.6的Sol/Terra/Luna层级化架构允许同一代模型在能力和成本间弹性切换，针对长周期工具调用和代码生成场景专门优化；Muse
    Spark 1.1的多智能体编排能力（主智能体规划+并行子智能体委派）结合原生工具调用和MCP服务器集成，代表了Agent架构从单智能体向协作式多智能体系统演进的技术方向
  business_model: Meta首次开放模型API是重大商业策略转变，以$1.25/4.25的激进定价（约为GPT-5.6同等能力的1/4）进入市场，配合$20免费额度降低开发者试错门槛，可能引发AI模型API市场的价格战和商业模式重塑；OpenAI的Sol/Terra/Luna三级定价（$1~5/$6~30）则创造了精细化的价格歧视体系，按任务难度自动路由，这是API经济中分层服务模式（tiered
    service model）的成熟案例
engineering_complexity: production_ready
compound_value:
  score: 8.0
  reason: 本次事件的核心价值在于两大信号的交汇：第一，OpenAI的GPT-5.6三档分级（Sol/Terra/Luna）标志着基础模型的产品化进入成熟期——通过耐久层级实现能力阶梯与定价的精确匹配，开发者对某个层级的投资会形成平台依赖和升级路径锁定，相比单模型发布具有显著更强的复利效应。第二，Meta以SOTA
    Agent基准成绩和激进的定价（$1.25/$4.25，约为OpenAI Luna级的40-70%）首次开放API，标志着模型层竞争从纯能力军备竞赛升级为'定价策略×生态绑定×Agent优化'的多维竞争。两者都押注Agent作为核心场景且均支持MCP协议，这将加速模型层的标准化和商品化，长期看能建立开发者生态粘性的平台将捕获最大价值。综合评估：结构性变化而非一次性事件，复利效应强但需观察Meta
    API的长期承诺和OpenAI定价权的可持续性。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- OpenAI
- Meta
- Anthropic
competitive_casualty:
- 中小模型提供商（Cohere、AI21等）
- 非MCP协议的Agent中间件
- xAI
market_opportunities:
- 创业者可基于OpenAI GPT-5.6系列的分层定价策略（Sol/Terra/Luna），设计差异化的AI产品方案：用Luna做高频低延迟的原型验证和简单任务，用Terra处理中等复杂度场景，用Sol攻克高价值困难任务，从而在成本可控的前提下覆盖更广泛的客户需求
- Meta Muse Spark 1.1以显著低于GPT-5.6的价格（输出Token仅4.25美元/百万）提供100万Token上下文窗口和MCP协议支持，开发者应优先评估该模型构建需要长上下文理解与多工具编排的复杂Agent应用，尤其是在金融分析、法律文档处理等场景中具备性价比优势
- Muse Spark 1.1的主智能体委派子智能体架构在多项Agent基准测试中取得SOTA，产品团队可借鉴其多智能体协作范式，针对企业级自动化工作流（如跨系统数据整合、多步骤审批流程）开发定制化的Agent编排方案
risk_matrix:
  regulatory: Meta首次向开发者开放Model API，多模态推理模型在内容安全、深度伪造风险方面面临各国AI监管审查压力；OpenAI分层定价可能引发反垄断关注，尤其是在API市场形成价格歧视或排他性竞争时
  technological: GPT-5.6系列的快速迭代可能使GPT-5.5及更早模型迅速贬值，持有上一代模型投资或基于其构建产品的团队面临技术负债风险；Muse
    Spark 1.1的基准测试成绩尚未在大规模生产环境中得到充分验证，实际稳定性存疑
  competitive: 一周内OpenAI、Meta、xAI、Mistral、Google等多巨头密集发布新模型，市场进入白热化竞争阶段，中小模型厂商面临被生态挤压的生存危机；AI模型价格快速下降趋势明显，盈利模式面临挑战
  ethical: Agent自主性和多模态能力的显著提升增加了被用于复杂社会工程攻击、深度伪造和自动化虚假信息传播的风险；AI Agent在金融等敏感领域的自主决策若缺乏足够安全护栏，可能导致重大经济损失和信任危机
  additional: []
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: ChatGPT Work
  canonical_name: ChatGPT Work
  url: null
  positioning: OpenAI 推出的 AI 智能体产品，由 GPT-5.6 旗舰模型驱动，面向工作场景的自动化任务处理。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 知识工作者
  - 开发者
  - 企业团队
  product_signal: 作为 OpenAI 首个面向工作场景的专用智能体，深度集成 GPT-5.6 模型，专注于长时程工具使用和编码任务。
  market_signal: ChatGPT Work 是 GPT-5.6 的首个垂直场景产品，标志着 OpenAI 从对话式 AI 向智能体平台转型的关键一步。
  differentiation: 与 Codex 和 ChatGPT 深度协同，以 GPT-5.6 旗舰能力为驱动，填补了 OpenAI 在工作场景专用智能体的产品空白。
  watch_reason: ChatGPT Work 是 OpenAI 从对话式 AI 向主动智能体转型的关键产品，GPT-5.6 系列模型的迭代直接决定了其能力天花板，值得持续跟踪其对企业工作流程的渗透速度和使用场景的扩展方向。
  risk_notes:
  - 作为新产品，ChatGPT Work 的实际企业采用率和场景覆盖效果尚无公开数据验证。
  - 智能体产品的准确性和可靠性在复杂工作场景中仍存在潜在风险。
  score: 8.0
  article_ids:
  - 5d9bcda5ffff8971
  evidence_snippets:
  - OpenAI 推出了 ChatGPT Work 智能体，由 GPT-5.6 作为默认大脑驱动。
- object_type: product
  name: Meta Model API
  canonical_name: Meta Model API
  url: null
  positioning: Meta 首次向开发者开放的模型 API 服务，基于 Muse Spark 1.1 多模态推理模型，目前处于公开预览阶段。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI 应用开发者
  - 企业 AI 团队
  - 智能体系统开发者
  product_signal: 支持原生工具、MCP 服务器和自定义技能，可作为主智能体规划并委派任务给并行子智能体，定价为每百万输入/输出 token 1.25/4.25
    美元。
  market_signal: 以极具竞争力的定价策略进入 API 市场（约为 GPT-5.6 Sol 的 1/4），新账户提供 20 美元免费额度，直接对标 OpenAI
    的 API 服务生态。
  differentiation: 延续 Meta 开源开放战略，Muse Spark 1.1 在 MCP Atlas（88.1）等智能体基准上取得 SOTA，同时支持
    100 万 token 上下文窗口，在性价比上形成差异化优势。
  watch_reason: Meta Model API 标志着 Meta 从模型开源向 API 商业服务延伸的战略转型，其定价策略和 Muse Spark 1.1
    在智能体基准测试中的 SOTA 表现，可能对现有大模型 API 市场竞争格局产生重要影响。
  risk_notes:
  - API 目前处于公开预览阶段，生产环境的稳定性、可用性和 SLA 保障尚待验证。
  - Meta 在面向开发者的 API 平台运营和生态建设方面经验有限，开发者采用率存在不确定性。
  score: 7.0
  article_ids:
  - 5d9bcda5ffff8971
  evidence_snippets:
  - Meta 首次向开发者开放了 Meta Model API，目前处于公开预览阶段。
  - Meta Model API 定价为每百万输入/输出 token 1.25/4.25 美元，新账户可获 20 美元免费额度。
- object_type: product
  name: GPT-Live
  canonical_name: GPT-Live
  url: null
  positioning: OpenAI 推出的实时语音交互 AI 产品，扩展了 ChatGPT 生态在语音场景的应用边界。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 语音交互用户
  - 实时对话场景用户
  - ChatGPT 现有活跃用户
  product_signal: 作为 OpenAI 的语音 AI 产品，GPT-Live 借助 GPT-5.6 模型能力扩展了 ChatGPT 生态的实时语音交互场景。
  market_signal: 语音 AI 交互是 AI 产品的重要增长赛道，OpenAI 通过 GPT-Live 与 ChatGPT Work 形成文本—语音产品矩阵，巩固生态护城河。
  differentiation: 以 GPT-5.6 模型能力为语音交互底座，与 ChatGPT 生态深度绑定，但当前产品细节有限，差异化程度尚待观察。
  watch_reason: GPT-Live 代表了 AI 从文本交互向多模态语音交互的重要扩展方向，但产品能力、定价策略和市场竞争定位目前信息有限，需持续关注
    OpenAI 在该领域的后续产品发布和用户反馈。
  risk_notes:
  - GPT-Live 的产品细节、技术架构和商业模式尚未公开，难以全面评估其竞争力。
  - 语音 AI 交互领域已有多个成熟竞品，GPT-Live 面临激烈的市场竞争和用户预期挑战。
  score: 6.0
  article_ids:
  - 5d9bcda5ffff8971
  evidence_snippets:
  - OpenAI 推出了 GPT-Live 语音产品，扩展了 AI 语音交互能力。
---

# 🤖 AI Agents Weekly: GPT-5.6 Family, Meta Muse Spark 1.1, Grok 4.5, SWE-1.7, Robostral Navigate, The Harness Effect, and More

### GPT-5.6 Family, Meta Muse Spark 1.1, Grok 4.5, SWE-1.7, Robostral Navigate, The Harness Effect, and More

In today’s issue:

OpenAI ships the GPT-5.6 family

Meta releases Muse Spark 1.1

OpenAI launches ChatGPT Work agent

xAI releases Grok 4.5 for coding

Cognition ships SWE-1.7 at 1000 tok/s

Mistral drops Robostral Navigate

Harness design sets agent economics

OpenAI launches GPT-Live voice

Google open-sources Gemma 4

Tencent open-sources 295B Hy3

Google ships Cloud Run sandboxes

Nous puts Hermes Agent in the cloud

Microsoft releases Flint for agents

Ternlight runs embeddings in-browser

GPT-5.6 proves 50-year math conjecture

Databricks benchmarks coding agents

OpenAI audits SWE-Bench Pro

FrontierFinance benchmarks agent analysts

Paper turns memory into navigation

GitLost tricks GitHub’s AI agent

Anthropic finds a global workspace

Sakana replays Picbreeder with VLMs


And all the top AI dev news, papers, and tools.

## Top Stories

### OpenAI Ships the GPT-5.6 Family

OpenAI began rolling out its GPT-5.6 family, Sol, Terra, and Luna, across ChatGPT, Codex, and the API.

**Capability tiers:**The number marks the generation while Sol, Terra, and Luna are durable tiers that advance on their own cadence. Sol is the flagship for the hardest tasks, Terra matches GPT-5.5 at lower cost, and Luna is the fastest and cheapest.**Built for agents:**GPT-5.6 is the new default brain behind Codex and ChatGPT Work, tuned for long-horizon tool use and coding.**Pricing:**Sol runs 5 dollars/30 dollars per million input/output tokens, Terra 2.50 dollars/15 dollars, and Luna 1 dollar/6 dollars.**Rollout:**Live now in ChatGPT, Codex, and the API, with the Codex desktop app merging into the ChatGPT app on Windows and Mac.

### Meta Releases Muse Spark 1.1

Meta Superintelligence Labs released Muse Spark 1.1, a multimodal reasoning model built for agentic tasks, and opened the Meta Model API to developers for the first time.

**Agent orchestration:**Works with native tools, MCP servers, and custom skills, and can act as a main agent that plans and delegates work to parallel subagents.**Agentic benchmarks:**Posts SOTA scores on MCP Atlas (88.1), JobBench (54.7 vs Opus 4.8 at 48.4 and GPT-5.5 at 38.3), and Humanity’s Last Exam with tools (62.1 vs Opus 4.8 at 57.9), plus FinanceBench.**Long context:**Supports a 1M-token context window for long-horizon, multimodal work.**Open API and pricing:**Meta Model API is in public preview at 1.25 dollars/4.25 dollars per million input/output tokens, with 20 dollars in free credits for new accounts.