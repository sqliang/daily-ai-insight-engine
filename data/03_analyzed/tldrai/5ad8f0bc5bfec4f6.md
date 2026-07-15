---
title: Meta's Watermelon Matches GPT-5.5 Benchmarks (3 minute read)
source: https://letsdatascience.com/news/metas-watermelon-matches-gpt-55-benchmarks-76a9460e?utm_source=tldrai
author: []
published: ''
created: '2026-07-04'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 5ad8f0bc5bfec4f6
manifest_dates:
- '2026-07-04'
- '2026-07-05'
source_type: news_media
tldr: Meta 内部模型 Watermelon 据称在基准测试中追上 GPT-5.5，但未经独立验证。
objective_summary: Alexandr Wang 在 Meta 内部全体会议上声称，正在训练中的 Watermelon 模型在 AI 基准测试中已追上
  OpenAI 的 GPT-5.5。该模型使用了比 Muse Spark 多一个数量级的算力。此消息源自 Business Insider 援引两名匿名知情人士，Meta
event_type: application_landing
epistemic_status: rumor_leak
entities:
  companies:
  - Meta
  - OpenAI
  - Business Insider
  technologies:
  - Watermelon
  - Muse Spark
  - GPT-5.5
  - GPT-5.6
  key_people:
  - Alexandr Wang
key_logic_flow:
- Meta 人工智能负责人 Alexandr Wang 在内部全体会议上声称，正在训练中的模型 Watermelon 在基准测试中已追上 OpenAI 的 GPT-5.5。
- Watermelon 使用了比此前模型 Muse Spark（内部代号 Avocado）多一个数量级的训练算力，表明 Meta 以算力规模为核心竞争策略。
- 该消息源自 Business Insider 援引两名匿名知情人士，Business Insider 未明确 Wang 引用了哪些具体基准测试。
- OpenAI 已于 2026 年 4 月发布 GPT-5.5，并于上月底发布 GPT-5.6。
- Meta 和 OpenAI 均未对 Business Insider 的报道作出官方回应或确认。
- 文章指出在 Meta 发布公开模型卡或可复现评估结果之前，该声称应被视为早期信号而非经过验证的事实。
extract_result: success
impact_score:
  score: 5.5
  reason: 该事件的核心信息——Meta 内部模型 Watermelon 追上 GPT-5.5——源自单一匿名信源的内部会议泄露，未经任何独立验证或官方确认。作为行业信号，它揭示了两点有价值的信息：一是
    Meta 正以数量级级别的算力投入（10× Muse Spark）追赶前沿，二是 Meta 内部对自身模型能力的自信声称。但该声称并未改变任何可验证的竞争格局——GPT-5.6
    已经发布，追赶 GPT-5.5 的宣称在时效上已打折扣。综合来看，这是一个重要的竞争态势信号，但远未达到范式转移级别，暂不足以改变开发者的模型选型决策。给分
    5.5（属于'重要产品线索，改变局部竞争叙事但非格局'的中等偏下区间）。
sentiment: neutral
developer_sentiment:
  tone: skeptical
  primary_focus: 未经第三方验证的内部基准声称，算力投入规模（10倍于前代）才是比 benchmark 数字更可靠的信号
hype_assessment:
  level: medium
  reason: 标题'追上 GPT-5.5'使用了典型的对标包装话术，存在明显的 PR 水分。但文章正文（包括 Business Insider 原文和转载方）多次强调该声称未经独立验证、未公开基准细节、未获官方回应，整体叙事在'放卫星'和'免责声明'之间摇摆。'caught
    up'一词具有较强误导性——追赶的是已被 GPT-5.6 超越的上一代模型。判定为 medium。
information_entropy: medium
domain_disruption:
  technical_innovation: 无实质技术突破——Watermelon 的核心策略是数量级的算力堆叠（比 Muse Spark 多 10 倍算力），属于规模扩展（scaling）范式下的继续推进，而非架构或算法创新。真正的技术信号在于
    Meta 愿意为追赶投入如此巨大的计算资源。
  business_model: 印证了 Meta 以算力规模为核心竞争壁垒的战略方向，进一步推高了前沿模型训练的资本门槛（数十亿美元级别芯片和数据中心投入），强化'算力即护城河'的行业叙事。对
    AI 创业公司而言，这意味着基座模型赛道的入场券价格继续上涨。
engineering_complexity: prototype
compound_value:
  score: 6.5
  reason: 该事件的核心投资信号并非 Watermelon 的具体基准分数，而是 Meta 以数量级算力投入追赶前沿模型的战略路径已获得内部验证。若 Watermelon
    最终经第三方复现确认，Meta 将成为仅次于 OpenAI/Anthropic 的第三极基础模型力量，且拥有独特的社交分发护城河（WhatsApp/Instagram/Facebook
    数十亿用户），长期复利效应显著——Meta 可以将前沿模型能力直接注入其产品矩阵，形成'模型+分发'的双重壁垒。但当前证据级别仅为匿名内部泄露（Business
    Insider 单一信源），无公开模型卡或可复现评估结果，存在乐观偏差和内部宣传风险。真正的复利积累取决于 Meta 能否在后续发布中兑现该声称，因此评分落在
    6-7 的中高区间，低于顶级（需要公开验证），但高于普通产品发布（因为算力规模路径本身就是一个可观察的结构性趋势）。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- Meta
- NVIDIA
- AMD
competitive_casualty:
- OpenAI
- Anthropic
- 小型基础模型初创公司
market_opportunities:
- 若 Watermelon 确如声称达到 GPT-5.5 水平，Meta 开源生态将获得重大能力跃升，可提前布局基于 Llama 架构的垂直行业微调与私有化部署方案
- 算力军备竞赛持续升级为 GPU 集群运营、分布式训练优化服务以及数据中心基础设施供应商带来明确的商业化窗口
- 独立第三方 AI 基准验证和模型评测服务的需求将随各厂商未经验证的性能声称增多而上升，存在评测平台型创业机会
risk_matrix:
  regulatory: 匿名来源的内部基准声称如最终无法兑现，Meta 可能面临投资者诉讼或欧盟 AI Act 对模型性能声明的透明度问责风险
  technological: 单一匿名信源的内部声称未经独立复现验证，存在严重的乐观框架偏差风险；Watermelon 仍在训练中，实际能力、发布时程均不确定
  competitive: Meta 以超大规模算力投入追赶 OpenAI，若 Watermelon 成功将加剧头部模型厂商的价格战和生态挤压；OpenAI 已发布
    GPT-5.6，进一步拉高了追赶门槛
  ethical: 量级级算力投入加剧能源消耗与环境争议；未经验证的内部声称通过媒体泄露可能误导行业投资决策与模型选型判断
  additional:
  - 信息不对称风险：报道仅依赖两名匿名知情人士，无法排除商业情报战中信息被策略性操控或夸大的可能性
confidence:
  impact: medium
  compound: low
  hype: medium
actionable_insight: monitor
---

Meta's superintelligence chief **Alexandr Wang** told employees in a town hall that the company's upcoming model, codenamed **Watermelon**, has "caught up" with OpenAI's **GPT-5.5** on closely followed AI benchmarks, according to Business Insider, which cited two people familiar with the matter. Wang reportedly said Watermelon is still in training and uses "an order of magnitude more compute" than **Muse Spark** (Meta's April model, internally codenamed Avocado), which had trailed rival models despite solid benchmark scores. Business Insider notes it was not clear which benchmarks Wang cited, and neither Meta nor OpenAI has confirmed the claim. For practitioners, an internal, single-sourced benchmark claim is not equivalent to a published, reproducible evaluation and should be treated as an early signal, not a verified result, until Meta releases the model publicly.

An unconfirmed internal benchmark claim from Meta's AI leadership is a reminder that town-hall statements are not evaluation artifacts: until Meta publishes reproducible results or a model card for Watermelon, "caught up with GPT-5.5" is a single-sourced assertion, not verified parity. For practitioners tracking the frontier-model race, the more concrete signal here is the compute trajectory Wang described, not the benchmark claim itself.

According to Business Insider, **Alexandr Wang** told Meta employees in a town hall that the company's upcoming model, codenamed **Watermelon**, "has caught up" with OpenAI's **GPT-5.5** based on closely followed AI benchmarks, citing two people familiar with the matter. Business Insider reports Wang said Watermelon, the successor to Avocado (Meta's internal codename for Muse Spark), is "currently in training" and "uses an order of magnitude more compute than Avocado." OpenAI released GPT-5.5 in April and introduced GPT-5.6 late last month, per Business Insider. Meta declined to comment and OpenAI did not respond to a request for comment. Investing.com, redistributing the Business Insider report, added that it was not immediately clear which benchmarks Wang was citing.

Meta released Muse Spark in April 2026, its first major model since hiring Wang, and it performed well on some benchmarks while still falling short of leading rivals overall. Wang's description of Watermelon using "an order of magnitude more compute" than Muse Spark points to continued aggressive scaling as Meta's primary lever, consistent with the company's reported multibillion-dollar spending on chips and data centers under Zuckerberg's direct oversight of AI development.

Treat this as a leading indicator, not a procurement signal. Internal benchmark claims announced without published methodology, evaluation datasets, or third-party replication carry a real risk of optimistic framing. Wait for a public model card, an official benchmark table, or independent evaluations before factoring Watermelon into model-selection or capacity-planning decisions.

Meta has not given a release timeline for Watermelon. Watch for a public launch announcement, published benchmark results, and whether the model narrows the gap with GPT-5.5 and GPT-5.6 on independently run evaluations rather than internally cited ones.

## Key Points

- 1Meta's AI chief told staff Watermelon has matched GPT-5.5 on internal benchmarks, per a single Business Insider report citing anonymous sources.
- 2Wang described Watermelon as using far more training compute than April's Muse Spark, underscoring compute scaling as Meta's core strategy.
- 3Practitioners should wait for published benchmarks or independent evaluations before treating the parity claim as verified for deployment decisions.

## Scoring Rationale

Notable signal in the Meta-OpenAI frontier-model race given Meta's competitive stakes, but the claim rests on a single anonymous-sourced town-hall statement with no published benchmark data, and neither company confirmed specifics, so it stays provisional pending independent verification.

## Sources

Public references used for this report.

Practice with real Ad Tech data

90 SQL & Python problems · 15 industry datasets