---
title: Cerebras stock plunges after earnings as CEO says margin outlook was misunderstood
source: https://techcrunch.com/2026/06/24/cerebras-stock-plunges-after-earnings-as-ceo-says-margin-outlook-was-misunderstood/
author:
- '[[Aisha Malik]]'
published: '2026-06-24'
created: '2026-06-25'
description: In its first earnings report since going public, the AI chipmaker forecast
  a narrower gross margin in its core business, scaring investors.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 935096bdef6eacfd
source_type: news_media
tldr: Cerebras 上市后首份财报超预期，但因利润率指引低于预期股价暴跌近20%。
objective_summary: Cerebras Systems 发布上市后首份财报，Q1 营收 1.93 亿美元（同比增 94%），净亏损从 2390 万收窄至
  1400 万。但由于全年核心业务毛利率指引仅为 38%-41%（低于 Q1 的 47%），股价次日下跌约 20% 至接近 IPO 价格。
event_type: capital_movement
epistemic_status: verified_fact
entities:
  companies:
  - Cerebras Systems
  technologies: []
  key_people:
  - Andrew Feldman
key_logic_flow:
- Cerebras Systems 发布上市以来首份 Q1 财报，营收 1.93 亿美元同比增长 94%，净亏损从 2390 万美元收窄至 1400 万美元，业绩超预期。
- 公司在财报中给出全年核心业务毛利率指引为 38%-41%，显著低于 Q1 报告的 47%，引发市场担忧。
- 受利润率指引影响，Cerebras 股价次日下跌约 20%，创上市以来新低，接近 IPO 发行价。
- CEO Andrew Feldman 表示投资者误解了利润率指引，称公司为加快产能部署，需从一家大客户处临时回租设备，这将拖累今年的利润率。
- 回租设备的决策原因是公司正在建设和部署自有数据中心产能，在此之前通过回租方式提前释放更多可用算力。
extract_result: success
impact_score:
  score: 3.5
  reason: 评分依据：Cerebras 作为 AI 芯片领域的重要玩家（晶圆级芯片架构），其上市后首份财报引发股价暴跌近 20%，对 AI 硬件赛道的二级市场情绪有一定打击，可能传导至其他未盈利
    AI 芯片公司的估值预期。但本质上是一起公司级别的财务事件，不涉及任何技术突破或竞争格局的根本性改变。营收同比增长 94% 表明业务仍在高速扩张，利润率指引下降的原因（设备回租）属短期财务安排而非产品竞争力恶化。综合来看，属于局部市场情绪事件，行业影响范围有限。
sentiment: negative
developer_sentiment:
  tone: neutral
  primary_focus: Cerebras 财务波动是否会影响其软件生态（CSL/SDK）的长期维护和开发者支持力度
hype_assessment:
  level: low
  reason: 判定依据：本文为 TechCrunch 对 Cerebras 财报的客观报道，包含具体的营收、亏损、毛利率等硬数据，CEO 也对利润率指引做了合理解释（设备回租）。无任何
    PR 包装或概念炒作成分，属于典型的企业财务新闻报道。
information_entropy: medium
domain_disruption:
  technical_innovation: 无，纯财务事件，不涉及技术突破或架构创新
  business_model: 设备回租模式值得关注：AI 芯片公司在产能爬坡期通过向客户回租自研设备来提前释放算力，这种轻资产+重资产混合运营策略可能成为芯片公司加速市场渗透的参考范式
engineering_complexity: production_ready
compound_value:
  score: 3.5
  reason: 该事件本质上是市场对短期利润率指引的过度反应引发的股价波动，而非基本面恶化。Cerebras Q1营收同比增94%、净亏损收窄至1400万美元，业务增长强劲；利润率指引承压源于为加速产能部署而采取的临时设备回租策略，属于扩张期的战术性选择而非结构性缺陷。此事件不具备长期复利积累效应，但作为AI芯片赛道的一个真实商业信号，折射出该赛道的核心矛盾：产能军备竞赛必然伴随短期利润率稀释，这对评估硬件创业公司的单位经济模型和风险收益特征有参考意义。长期复利价值低，除非该策略能被证明是更高效的产能扩张范式。
value_capture_layer: hardware_compute
moat_impact: strengthens_monopoly
key_beneficiaries:
- NVIDIA
competitive_casualty:
- Cerebras Systems (短期股价承压)
- AI芯片初创企业 (Groq、SambaNova等，同受资本强度和利润率质疑)
market_opportunities:
- AI芯片公司通过售后回租（sale-leaseback）模式加速产能部署的财务创新值得关注，可为数据中心基础设施融资领域带来新的结构化产品机会
- Cerebras 营收同比增94%表明非NVIDIA路线的专用AI芯片（晶圆级芯片）仍存在差异化市场需求，创业者可关注AI推理/训练细分场景的芯片替代方案
- 毛利率指引低于预期反映AI芯片行业价格战和产能建设成本压力，建议关注面向AI芯片公司的数据中心建设与运维服务商的投资机会
risk_matrix:
  regulatory: 美国对华AI芯片出口管制政策可能进一步收紧，Cerebras 作为新兴AI芯片厂商若涉及中国客户或将面临合规风险，如BIS实体清单扩展
  technological: Cerebras 采用晶圆级芯片（WSC）架构，与NVIDIA GPU及新兴ASIC路线存在技术替代竞争。若主流架构持续占据生态优势，其专用路线可能面临市场边缘化风险
  competitive: NVIDIA 持续主导AI芯片市场，AMD、英特尔及大批AI芯片创业公司形成激烈竞争。毛利率指引从47%降至38%-41%预示着行业价格战和产能投入期的盈利压力
  ethical: 无
  additional:
  - 售后回租设备安排虽能短期释放算力，但可能引发对财务报表透明度和会计准则的额外审查
  - 股价接近IPO发行价且创上市新低，若持续低迷可能影响后续融资能力和员工期权激励
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: monitor
---

Shares of Cerebras Systems dropped almost 20% on Wednesday, even after the company delivered better-than-expected first-quarter earnings on Tuesday.

That’s because in its first earnings report since going public, the AI chipmaker forecast a narrower gross margin in its core business, guiding for a full-year margin of 38% to 41%, compared with the 47% reported in the first quarter. The stock hit a new low on Wednesday, almost hitting the company’s IPO price.

Cerebras CEO Andrew Feldman told CNBC that investors had misunderstood the company’s margin guidance, noting that Cerebras will need to rent back some equipment from one of its largest customers.

The company said during its earnings call that it decided to make more capacity available sooner by temporarily renting its own systems back from an existing customer while it builds out and deploys its own data center capacity. The company said this would cut into profit margins this year.

According to the company’s earnings report, revenue for the quarter reached $193 million, up 94% year-over-year. Net loss narrowed to $14 million, down from $23.9 million a year earlier.