---
title: How NVIDIA scales expertise with ChatGPT Work
source: https://openai.com/index/nvidia/chatgpt-work
author: []
published: Tue, 18 Aug 2026 00:00:00 GMT
created: '2026-08-19'
manifest_dates:
- '2026-08-19'
- '2026-08-20'
- '2026-08-21'
description: NVIDIA teams use ChatGPT Work to reduce manual tasks, connect fast-moving
  signals, and scale successful workflows globally.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: baf07daff59f271b
source_type: tech_blog
tldr: OpenAI 发布客户案例：NVIDIA 用 ChatGPT Work 自动化 GTC 大会筹备等重复性工作，GTM 团队每周节省约 16 小时；市场部工作流每周将
  25-40 条外部 AI 动态提炼为 5-8 条可行动信号，原型制作周期从 2-3 周缩短至 3-5 天。
objective_summary: OpenAI 发布官方客户案例，介绍 NVIDIA 内部如何规模化使用 ChatGPT Work。GTM 团队的 Will Daney
  将 GTC 筹备中约 40% 的手工分析工作自动化，工作流每周运行两次，12 周周期内每周节省约 16 小时，并分享给旧金山、台北、欧洲和华盛顿特区的团队定制使用。市场部
  AI 运营团队的 Rachita Jain 用工作流每周把 25-40 条外部 AI 更新提炼为 5-8 条可行动信号，原型制作时间从 2-3 周缩短到 3-5
  天。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - NVIDIA
  - OpenAI
  technologies:
  - ChatGPT Work
  key_people:
  - Will Daney
  - Rachita Jain
key_logic_flow:
- OpenAI 发布客户案例，介绍 NVIDIA 知识工作者用 ChatGPT Work 减少信息整理时间、更多精力用于行动。
- NVIDIA GTM 团队的 Will Daney 将 GTC 大会筹备中约 40% 的手工分析工作自动化，工作流每周运行两次，12 周周期内每周节省约 16
  小时。
- Will Daney 拥有的工作流可随活动变化自行调整，无需等待采购新工具，并分享给旧金山、台北、欧洲和华盛顿特区的团队按本地需求定制。
- NVIDIA 市场部 AI 运营团队的 Rachita Jain 用 ChatGPT Work 结合外部来源与内部上下文，每周将 25-40 条外部 AI 更新提炼为
  5-8 条可行动信号。
- 使用 ChatGPT Work 制作可用原型的时间从原先的 2-3 周缩短到 3-5 天。
object_mentions:
- object_type: product
  name: ChatGPT Work
  canonical_name: ChatGPT Work
  url: https://openai.com/chatgpt/work/
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - OpenAI 官方客户案例介绍 NVIDIA 员工通过 ChatGPT Work 自动化 GTC 大会筹备等重复性工作流程。
  - GTM 团队员工 Will Daney 用 ChatGPT Work 将 GTC 筹备中约 40% 的手工分析工作自动化，12 周周期内每周节省约 16 小时。
  - 市场部 AI 运营团队的 Rachita Jain 用 ChatGPT Work 每周将 25-40 条外部 AI 更新提炼为 5-8 条可行动信号。
  article_id: baf07daff59f271b
extract_result: success
impact_score:
  score: 3.5
  reason: 这是一篇 OpenAI 官方的客户案例营销内容，而非产品发布或技术突破。其行业信号意义在于：NVIDIA 作为顶级标杆客户为 ChatGPT Work
    的企业采纳提供背书，且给出的量化指标（GTC 筹备周期每周节省约16小时、原型制作从2-3周缩短至3-5天）为'agentic 工作流在企业知识工作中的 ROI'提供了具体参照，对
    OpenAI 与 Microsoft Copilot 等企业 AI 助手竞品的格局有一定边际影响。但事件本身不含新技术、无公开 API 或定价变化，也未被独立第三方验证，属于标杆客户背书级别的日常更新，未改变局部竞争格局。故评分为3.5。
sentiment: positive
developer_sentiment:
  tone: skeptical
  primary_focus: ChatGPT Work 工作流自动化能力的真实边界与量化收益的可验证性
hype_assessment:
  level: medium
  reason: 全文虽未滥用'颠覆''革命性'等词，但本质是 OpenAI 挑选的成功客户故事，存在明显选择性呈现：量化指标（每周节省16小时、40%分析自动化、25-40条提炼为5-8条）均出自当事人自述且无对照组、无成本投入或失败案例披露，属于典型的营销案例模板；'active
    intelligence''passive reading into active intelligence'等表述带有包装话术色彩。数据具体但不可独立核验，判定为存在一定包装。
information_entropy: low
domain_disruption:
  technical_innovation: 无实质技术突破。背后反映的技术趋势是 agentic workflow（定时运行、可拥有可定制的自动化流程）与内部/外部知识融合（RAG
    语义比对）已从工程工具下沉为知识工作者的日常能力——即'由员工自主构建并跨团队复制工作流'的范式在真实业务场景中跑通，无需等待采购新工具即可随业务变化迭代。
  business_model: 展示了 AI 工作流对传统企业软件（手工报表、CRM 分析、市场情报整理）的替代潜力，OpenAI 借此从'对话助手'向'企业业务流程自动化平台'演进，切入信息整合与商业智能赛道，与
    Microsoft Copilot 及各 agent 编排平台形成正面竞争；对企业采购而言，'员工自建工作流'模式可能改写 IT 部门集中采购软件的预算逻辑。
engineering_complexity: production_ready
compound_value:
  score: 6.5
  reason: 事件本质是 OpenAI 企业级产品 ChatGPT Work 的标杆客户案例，属于 PR 声明，信息增量有限；但量化数据提供了企业 Agent
    工作流采用的关键信号：NVIDIA GTM 团队 40% 手工分析被自动化、12 周周期内每周节省 16 小时、原型周期从 2-3 周压缩到 3-5 天。投资逻辑上，复利价值不在单次案例本身，而在'工作流一旦被团队内化并跨地域共享，即形成内嵌组织流程的转换成本与自我复制效应'——用户用自有数据+内部上下文构建的工作流会随业务/事件自动迭代、可复制给其他区域团队，且无需采购新工具，这正是
    OpenAI 在知识工作者市场建立长期粘性与网络效应的机制。给 6.5 分而非更高：单客户、PR 声明、且 NVIDIA 与 OpenAI 存在算力/资本层面的利益关联，营销放大成分需打折；复利假设（工作流沉淀为企业基础设施）仍需更多跨行业、跨规模客户案例验证。
value_capture_layer: end_application
moat_impact: creates_new_moat
key_beneficiaries:
- OpenAI
- NVIDIA
- Microsoft
competitive_casualty:
- UiPath、Automation Anywhere 等传统 RPA 厂商
- 独立 Agent 工作流初创公司
- 传统数据分析/商业智能工具厂商
market_opportunities:
- 企业 AI 工作流自动化已被 NVIDIA 这类头部科技公司验证为真实刚需，可针对会议会展筹备、GTM 运营、竞品情报等高频重复场景开发可复用的 AI Agent
  工作流模板或垂直解决方案
- ‘员工自主搭建工作流 + 跨区域分享定制’的模式表明，企业内部 AI 工作流的分享协作平台（模板市场、版本管理、权限与合规治理）存在明确的落地机会
- 将海量外部行业动态自动提炼为少量可行动信号的情报蒸馏能力需求真实，可面向市场部、战略部、销售团队打造垂直化 AI 竞争情报与决策支持产品
risk_matrix:
  regulatory: 员工将客户名单、内部战略等企业敏感数据输入第三方 AI 平台（OpenAI），面临数据出境与数据合规审查风险；厂商宣传的量化收益（如每周节省
    16 小时）若缺乏可验证口径，可能触发广告营销合规审查。
  technological: 对 ChatGPT Work 单一平台存在技术锁定风险：底层模型迭代、接口变更或服务中断都可能使已构建的工作流失效；Anthropic
    Claude、微软 Copilot、Google Gemini 等竞品能力快速追赶，先发架构优势可能被稀释。
  competitive: OpenAI 与微软、Google、Anthropic 在企业级 AI 助理赛道正面竞争，巨头入场将加剧价格战与生态挤压；NVIDIA
    同时是这些竞争对手的 GPU 供应商，其站台案例可能引发供应链中立性与利益冲突争议。
  ethical: 企业将客户名单、内部战略等保密数据交给第三方 AI 处理，存在隐私与保密泄露风险；AI 提炼的‘可行动信号’可能带有偏见或幻觉，若未经人工校验直接驱动业务决策，可能造成误导性行动。
  additional:
  - 该案例为厂商公关声明，收益数据为自述口径，存在选择性披露与样本偏差风险，决策者不应直接套用其量化结果
  - NVIDIA 既是 AI 基础设施供应商又是 ChatGPT Work 客户，存在既当裁判又当运动员的潜在利益冲突，案例的客观性需打折看待
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: monitor
object_insights:
- object_type: product
  name: ChatGPT Work
  canonical_name: ChatGPT Work
  url: https://openai.com/chatgpt/work/
  positioning: ChatGPT Work 是 OpenAI 面向企业的智能工作流产品，帮助知识工作者自动化重复性信息整理流程，并将外部信息与内部上下文结合生成可行动信号。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 企业知识工作者
  - GTM（市场进入）与销售团队
  - 市场部 AI 运营团队
  - 解决方案架构师
  product_signal: NVIDIA 案例显示 ChatGPT Work 可将 GTC 筹备中约 40% 的手工分析工作自动化，每周运行两次，12 周周期内每周节省约
    16 小时。
  market_signal: OpenAI 以 NVIDIA 官方客户案例背书企业级 AI 工作流产品，展示其在头部企业场景的规模化落地与可量化 ROI。
  differentiation: 与一次性自动化工具不同，ChatGPT Work 支持员工自主拥有并迭代工作流，可随活动变化调整，且能在跨区域团队间复制定制，无需等待采购新工具。
  watch_reason: ChatGPT Work 是 OpenAI 面向企业 AI 工作流市场的重要产品卡位，NVIDIA 案例提供可量化的效率提升与跨团队复制实证，可持续反映企业知识工作者采用
    AI 的深度及 OpenAI 在 B 端产品化的进展。
  risk_notes:
  - 客户案例由 OpenAI 官方发布，属于厂商自述型证据，实际部署规模与长期收益仍需独立验证。
  - NVIDIA 属头部科技客户，其采用路径与收益可能不代表中小企业部署 ChatGPT Work 的普遍情况。
  score: 6.0
  article_ids:
  - baf07daff59f271b
  evidence_snippets:
  - OpenAI 官方客户案例介绍 NVIDIA 员工通过 ChatGPT Work 自动化 GTC 大会筹备等重复性工作流程。
  - GTM 团队员工 Will Daney 用 ChatGPT Work 将 GTC 筹备中约 40% 的手工分析工作自动化，12 周周期内每周节省约 16 小时。
  - 市场部 AI 运营团队的 Rachita Jain 用 ChatGPT Work 每周将 25-40 条外部 AI 更新提炼为 5-8 条可行动信号。
---

16

Hours saved per week using ChatGPT Work during the GTC planning cycle

3–5

Days to create a working prototype with ChatGPT Work, compared to 2–3 weeks previously

5–8

Actionable signals surfaced per week by ChatGPT Work from 25–40 external AI updates

At NVIDIA, ChatGPT Work is helping knowledge workers spend less time assembling information and more time acting on it.

For teams like GTM and solutions architecture, ChatGPT has become part of how work gets organized, automated, and scaled. For GTM, it transforms recurring operational processes, while solutions architects are using it to connect fast-moving external developments with NVIDIA’s internal priorities.

Will Daney helps NVIDIA’s global sales, business development, and product leaders execute and measure their strategies. One of his recurring responsibilities is supporting the field organization around GTC, NVIDIA’s global AI conference.

Previously, preparing for GTC required extensive work in spreadsheets: assembling account lists, tracking registrations, and helping teams identify the actions needed to create a productive experience for customers and partners. During the lead-up to the event, Will estimates that manual analysis consumed about 40% of his time. Today, he has turned much of that work into an automated ChatGPT Work process that runs twice a week. Across the 12-week GTC planning cycle, the workflow saves about 16 hours per week.

“I’m able to give time back, work with the actual field team, get to know them better, and help them figure out how to help our customers be more successful,” Will says.

And because he owns the workflow, he can adapt it as the event changes without waiting for a new tool to be purchased, implemented, and maintained. He can also share the underlying process with teams in other regions. Colleagues supporting events in San Jose, Taipei, Europe, and Washington, DC have received his ChatGPT workflows and customized them for their local needs.

“With ChatGPT, I think the real key is that I’m able to take a workflow I’ve already developed and I’m able to automate it event over event with little to no overhead.”

Rachita Jain works on the AI operations team within NVIDIA’s marketing organization, where she builds AI workflows and helps teams adopt new tools. Her challenge is keeping pace with an industry where new models, benchmarks, and research appear every day.

The information is readily available. The harder task is determining which developments matter to NVIDIA and connecting them with internal projects, conversations, and priorities. Rachita built a workflow with ChatGPT Work that reviews trusted external sources alongside internal context, identifies meaningful areas of overlap, and surfaces insights that can inform action. Each week, it distills roughly 25–40 external AI updates into 5–8 actionable signals.

“ChatGPT helped me change passive reading into active intelligence,” she says.