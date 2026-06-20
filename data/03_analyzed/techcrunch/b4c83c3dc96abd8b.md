---
title: Can tech companies learn to love cheaper AI models?
source: https://techcrunch.com/2026/06/09/can-tech-companies-learn-to-love-cheaper-models/
author:
- '[[Russell Brandom]]'
published: '2026-06-09'
created: '2026-06-10'
description: If those same AI workloads can be handled by cheaper models without affecting
  quality, it would mean a massive shift in the economics of AI.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: b4c83c3dc96abd8b
source_type: news_media
tldr: AI行业预测80%工作负载将在12-18个月内迁移到价格便宜99%的小模型
objective_summary: TechCrunch报道了AI行业从追求最大模型向成本敏感型模型选择的转变趋势。Coinbase联合创始人Brian Armstrong预测80%的AI工作负载将在12-18个月内转向便宜99%的模型。法律AI工具Harvey与Fireworks
  AI合作测试显示，组合使用Claude
event_type: capital_movement
epistemic_status: verified_fact
entities:
  companies:
  - Coinbase
  - Harvey
  - Fireworks AI
  - OpenAI
  - Anthropic
  - TechCrunch
  technologies:
  - Claude Opus
  - GLM 5.1
  - GPT-5.5
  - DeepSeek V4 Flash
  - GPT-5.4-mini
  key_people:
  - Brian Armstrong
  - Gabe Pereyra
key_logic_flow:
- AI行业长期以来以"模型越大越强"为基本假设，但不断攀升的成本正迫使企业重新审视更小、更便宜的模型。
- Coinbase联合创始人Brian Armstrong预测，未来12-18个月内80%的工作负载将运行在价格便宜99%的模型上，仅20%的工作负载继续使用最先进的模型。
- 若该预测成真，大部分成本节省将来自大型AI实验室，对即将进行IPO的OpenAI和Anthropic造成财务冲击。
- 法律AI工具Harvey与Fireworks AI合作测试显示，组合使用Claude Opus和Fireworks的GLM 5.1可在不降低质量的情况下将推理成本降低3倍。
- Harvey联合创始人Gabe Pereyra表示，质量的定义正在从"使用最强大的模型做所有事"演变为"用最合适的模型最高效地得到正确答案"。
- 真正的分界线不在于专有模型与开源模型之争，而在于大模型与小模型之分，用户可通过选择任一类小型模型来降低成本。
impact_score:
  score: 7.0
  reason: 该文章报道了AI行业从'越大越强'向成本敏感型模型选择的重大转变趋势。Coinbase联合创始人的80/20预测（80%工作负载在12-18个月内迁移到便宜99%的小模型）若成真，将根本性改变AI产业经济结构，直接影响OpenAI和Anthropic的IPO估值。Harvey与Fireworks
    AI的实证测试（3倍推理成本降低、无损质量）提供了可信的支撑数据。该趋势已从理论讨论进入实际部署验证阶段，虽非突发性范式转移，但其对AI产业链的冲击力在6-12个月内将持续放大。综合评定为7分。
sentiment: mixed
developer_sentiment:
  tone: excited
  primary_focus: 如何在多模型编排架构中实现无损的成本-质量最优解
hype_assessment:
  level: low
  reason: 文章基于可验证的行业预测（Coinbase联合创始人）和实际测试数据（Harvey+Fireworks AI的3倍成本降低），非空洞概念炒作。虽有'seismic
    change'等修饰性表述，但核心论点有事实支撑，属于对真实趋势的报道而非夸大PR宣传。
information_entropy: high
domain_disruption:
  technical_innovation: 多模型编排（Model Routing）架构的工程化落地——通过将简单任务路由到小型廉价模型、保留复杂任务给顶级大模型，实现系统级推理成本优化。核心挑战在于任务难度分类器的设计精度和路由延迟的权衡。
  business_model: 若80%工作负载迁移到便宜99%的小模型，大型AI实验室（OpenAI、Anthropic）的API收入结构将受严重冲击，其IPO估值逻辑需要重估。同时催生推理优化中间层（如Fireworks
    AI）和模型组合管理平台的新商业机会，推动AI服务从'全量使用最强模型'的奢侈模式走向'以任务匹配模型'的精细运营模式。
engineering_complexity: production_ready
compound_value:
  score: 7.8
  reason: 该趋势的核心是'智能模型路由与成本优化'正在重塑AI价值链。随着模型供给端快速多元化（开源/闭源、大/小模型），能够在保证输出质量的前提下自动选择最优性价比模型的中间层基础设施将产生显著的网络效应——模型越多、选择越复杂，路由层价值越大。Harvey与Fireworks
    AI的联合测试已验证3倍推理成本降低而质量无损，证明该方向存在明确的PMF。长期来看，这一趋势具有强复利效应：应用层公司因成本下降而扩大AI使用规模，进一步催生对更精细路由能力的需求。但风险在于若头部模型大幅降价或小模型能力快速趋同，路由层的溢价空间可能被压缩，因此评分落在高置信但非顶格的区间。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Fireworks AI
- Harvey
- DeepSeek
- AI应用层公司
competitive_casualty:
- OpenAI
- Anthropic
- 高价闭源API模型提供商
market_opportunities:
- 创业者可开发智能模型路由/编排中间件，根据任务复杂度动态调度大模型与小模型，帮助企业实现数倍的成本优化
- 法律、医疗等专业领域可借鉴Harvey与Fireworks AI的混合模型策略，构建行业专属的多模型协同推理方案，兼顾质量与成本
- 模型性价比评估与基准测试工具将成为新刚需，帮助企业在模型选择上做数据驱动的ROI量化决策
risk_matrix:
  regulatory: 若企业从美国模型切换到中国模型（如DeepSeek），可能触发出口管制、数据跨境传输等合规风险；不同 jurisdictions 的监管要求差异也会增加模型选型的法律复杂度
  technological: 小模型在复杂推理、长上下文、多步推理等场景的能力边界尚未充分定义，存在'隐性降级'风险——用户可能在特定任务中未察觉质量损失，从而积累潜在错误
  competitive: 大型AI实验室（OpenAI、Anthropic）面临商业模式冲击，可能通过捆绑销售、API锁定协议、独家模型条款等策略对抗成本压力，挤压第三方优化工具和模型路由方案的生存空间
  ethical: 企业在未充分验证的情况下盲目切换小模型处理关键任务（如法律文书、医疗诊断），可能因模型能力不足导致错误输出，引发严重的社会后果和责任纠纷
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
---

The AI boom has been built on a basic assumption: Bigger models are more powerful, and the most powerful models win. Now, the industry is about to learn what happens if that assumption starts to break.

Mounting costs have already pressured users to give smaller and cheaper models a second look. This cost-conscious model-shopping is new and it’s unclear how it will affect the industry, but the impact is likely to be significant.

One prediction, laid out best by Coinbase co-founder Brian Armstrong, is that it will result in the vast majority of tasks shifting to cheaper models.

“[D]emand for intelligence is near infinite, but 80% of workloads will be running on 99% cheaper models within 12-18 months,” Armstrong wrote on X. “20% of workloads will still run on latest gen models where IQ maxing is important.”

It’s hard to overstate what a significant shift it will be for the AI industry if Armstrong’s prediction comes true.

Before now, most AI companies have competed on quality, which has meant defaulting to the most advanced available model. If those same jobs can be handled by cheaper models without affecting quality, it would mean a massive shift in the economics of AI. And critically, much of the savings would be coming out of the pockets of the big labs, dealing a financial blow to OpenAI and Anthropic just as they’re heading for their IPOs.

It’s a potentially seismic change in the industry, resting on one basic question: Are companies ready to switch to smaller models?

Initial tests suggest that, when the system is arranged right, cheaper models could sub in without any sacrifice in quality. In a recent test by the legal AI tool Harvey, the company was able to reduce inference costs by 3x without reducing quality. The test, performed in partnership with the inference platform Fireworks AI, combined Claude Opus and Fireworks’ GLM 5.1, and shifted to Opus for the most intensive tasks. The result was a significantly lower load in terms of server time and overall cost.

“Quality comes first, and in legal it always will,” Harvey co-founder Gabe Pereyra told TechCrunch, referring to the AI legal services his startup provides. “However, the definition of quality is evolving from simply using the most powerful model for everything, to using the best model that gets the right answer most efficiently.”

This trend is often framed in terms of major labs versus Chinese models or open-weight ones, but that misses the bigger point. The real divide isn’t between proprietary and open models; it’s between large models and small ones. You can save money by switching from GPT-5.5 to DeepSeek’s V4 Flash, but switching to GPT-5.4-mini works just as well.

There’s an active price war going on between in-house inference from the big labs and independently served open-weight models. For the bigger question of small versus large, it doesn’t really matter which kind of small model wins out.