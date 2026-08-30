---
title: 'Back to the Future: A workbook time machine for spread sheet creation benchmarks'
source: https://arxiv.org/abs/2608.07873
author:
- '[[Mansi Uniyal, Agamdeep Singh, Ananya Singha, Priyanshu Gupta, Mukul Singh, Gust
  Verbruggen, Vu Le, Sumit Gulwani]]'
published: '2026-08-12'
created: '2026-08-12'
manifest_dates:
- '2026-08-12'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ac2b1a4ff6a65efd
source_type: academic_paper
tldr: 论文提出“工作簿时光机”自动构建电子表格生成基准，生成含 150 项任务的 wtmbench，用于评估 LLM 在 Excel 中创建公式、图表等派生对象的能力。
objective_summary: 研究人员在 arXiv 发表论文，提出 workbook time machine 流水线，可从公开工作簿语料自动生成（输入工作簿、输出工作簿、查询）三元组，覆盖公式、图表、数据透视表和条件格式四类对象。据此整理出
  wtmbench 基准，共 150 个任务，查询粒度分为三个层级。实验评估了现有电子表格操作智能体与基线，结果表明查询具体程度、智能体编排方式以及控制电子表格的接口
  API 会显著影响 LLM 在 Excel 任务上的表现。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - LLM
  - workbook time machine
  - wtmcorpus
  - wtmbench
  - Excel
  key_people: []
key_logic_flow:
- 论文提出 workbook time machine 流水线，用于自动构建评估语言模型电子表格生成能力的基准。
- 该流水线作用于公开工作簿语料，生成 wtmcorpus 三元组集合，涵盖公式、图表、数据透视表和条件格式四种对象类型。
- 从 wtmcorpus 中筛选出 wtmbench，包含 150 个任务，并按查询具体程度分为三个层级。
- 研究者在 wtmbench 上评估现有电子表格操作智能体与基线方法。
- 实验发现，查询粒度、智能体编排策略以及控制电子表格的接口 API 是影响 LLM Excel 任务表现的关键因素。
object_mentions:
- object_type: paper
  name: 'Back to the Future: A workbook time machine for spread sheet creation benchmarks'
  canonical_name: 'Back to the Future: A workbook time machine for spreadsheet creation
    benchmarks'
  url: https://arxiv.org/abs/2608.07873
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - '标题为 Back to the Future: A workbook time machine for spread sheet creation benchmarks
    的论文发表于 arXiv，摘要介绍了工作簿时光机流水线及其生成的 wtmcorpus 与 wtmbench。'
  article_id: ac2b1a4ff6a65efd
- object_type: project
  name: workbook time machine
  canonical_name: workbook time machine
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文摘要指出，他们引入了 workbook time machine，这是一个自动构建基准的流水线，用于评估语言模型在电子表格中创建派生对象的能力。
  article_id: ac2b1a4ff6a65efd
- object_type: dataset
  name: wtmcorpus
  canonical_name: wtmcorpus
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 将该流水线应用于公开工作簿语料后，产生了 wtmcorpus，它是由（输入工作簿、输出工作簿、查询）三元组组成的集合，覆盖四种对象类型和不同复杂度。
  article_id: ac2b1a4ff6a65efd
- object_type: dataset
  name: wtmbench
  canonical_name: wtmbench
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 研究者从 wtmcorpus 中整理出 wtmbench，这是一个包含 150 个任务的评测基准，查询描述按照三个具体程度层级进行组织。
  article_id: ac2b1a4ff6a65efd
- object_type: product
  name: Microsoft Excel
  canonical_name: Microsoft Excel
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 实验评估现有电子表格操作智能体与基线后，摘要指出查询具体程度、智能体编排以及用于控制电子表格的接口 API 会显著影响 LLM 在 Excel 任务上的表现。
  article_id: ac2b1a4ff6a65efd
extract_result: success
impact_score:
  score: 5.5
  reason: 该论文属于办公自动化/Agent 评测基础设施方向，为 LLM 在 Excel 中生成公式、图表、透视表、条件格式等派生对象提供了首个系统化的自动化基准构建方法学与
    150 任务评测集。它对电子表格 Agent 的研发者和评估者具有直接参考价值，能够局部改变该细分领域的评测标准；但影响范围主要局限于办公 Agent/企业自动化/LLM
    工具使用社区，尚未达到改变整个行业范式的程度。因此评为 5.5 分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 是否提供可复用的基准数据与代码，以及 150 个任务能否真实覆盖复杂办公场景
hype_assessment:
  level: low
  reason: 标题借用了《回到未来》的电影名，属于修辞层面；摘要与方法描述较为克制，未出现 '颠覆'、'革命性'、'超越人类' 等 PR 滥用词汇。研究明确声明其贡献是构建流水线与基准（wtmcorpus/wtmbench）并评估现有基线，结论限定在查询粒度、智能体编排和接口
    API 对性能的影响，整体水分较低。
information_entropy: medium
domain_disruption:
  technical_innovation: 提出 workbook time machine 流水线，从公开电子表格语料自动生成（输入工作簿、输出工作簿、查询）三元组，覆盖公式、图表、数据透视表和条件格式四类对象，并按查询具体程度分为三个层级，系统化解决了电子表格生成任务缺乏标准化评测数据的问题。
  business_model: 为电子表格 AI Agent、办公 Copilot 和企业自动化工具提供了可量化的评测基准，有助于降低评估成本、加速产品迭代，并可能推动垂直领域
    Agent（如 Excel 助手）在企业 SaaS 市场的竞争与落地。
engineering_complexity: prototype
compound_value:
  score: 5.5
  reason: 该论文针对高价值场景（Excel 电子表格）提出了可复用的自动化基准构建流水线，能够降低评估 LLM 表格操作能力的成本，加速电子表格智能体的研发与产品化，具备成为细分赛道基础设施的潜力。然而它本质上仍是学术成果/数据集，缺乏直接的商业模式、网络效应和数据飞轮；随着模型能力快速迭代，150
    任务规模的 wtmbench 可能被更复杂基准取代，因此长期复利价值中等，需要后续持续验证和扩展。
value_capture_layer: end_application
moat_impact: democratizes_access
key_beneficiaries:
- Microsoft
- Google
- OpenAI
- Anthropic
competitive_casualty:
- 传统 RPA 厂商
- 缺乏 AI 能力的电子表格插件/SaaS 厂商
market_opportunities:
- 面向企业财务、运营和数据分析场景的 Excel/电子表格 AI Agent 自动化工具存在明确落地空间，可围绕公式生成、图表制作、透视表与条件格式四类任务构建垂直工作流
- 基于公开工作簿语料自动生成（输入-输出-查询）三元组的流水线方法，可复用于办公自动化、低代码平台和 RPA 领域的训练数据合成与评测集服务
- 查询粒度分层与接口 API 选择对智能体表现影响显著，为设计和销售电子表格自动化 SDK/API 中间件提供了产品差异化切入点
risk_matrix:
  regulatory: 无
  technological: 基准测试方法可能被后续更大规模或更贴近真实办公场景的数据集超越，且 wtmbench 能否成为行业通用标准存在较大不确定性
  competitive: 微软、Google 等办公软件巨头及众多 AI 表格助手产品（如 Excel Copilot、 Numerous 等）已占据生态入口，第三方电子表格智能体面临获客和集成壁垒
  ethical: 电子表格自动化能力提升可能进一步替代初级数据处理和报表岗位，引发就业结构冲击；若将方法应用于企业内部工作簿，需关注敏感数据泄露与隐私合规
  additional:
  - 学术基准向工业界迁移时可能存在分布偏移，公开语料难以覆盖企业私有复杂模板
  - 评测结果受 API、提示策略和智能体编排方式影响较大，不同厂商的排行榜可能缺乏可比性
confidence:
  impact: medium
  compound: low
  hype: medium
actionable_insight: monitor
object_insights:
- object_type: project
  name: workbook time machine
  canonical_name: workbook time machine
  url: null
  positioning: 面向电子表格生成任务的自动化基准构建流水线，通过从公开工作簿语料生成三元组，系统评估 LLM 在 Excel 中创建公式、图表等派生对象的能力。
  technical_signal: 基于公开工作簿语料自动生成（输入工作簿、输出工作簿、查询）三元组，覆盖公式、图表、数据透视表和条件格式四类对象，并按查询具体程度划分三个层级。
  adoption_signal: 已整理为包含 150 个任务的 wtmbench 基准，并在现有电子表格操作智能体与基线方法上完成实验评估。
  ecosystem_relevance: 填补了 LLM 在电子表格领域能力评估的基准空白，为办公自动化智能体、电子表格 AI 工具的研发与选型提供了可量化的测试依据。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该流水线将工作簿语料自动转化为结构化评测任务，既降低了领域专用基准的构建成本，又揭示了查询粒度、智能体编排和接口 API 对 LLM
    Excel 任务表现的关键影响，值得持续跟踪其在办公自动化与智能体评估生态中的应用进展。
  risk_notes:
  - 项目目前主要面向研究评测场景，工程化落地与工具链成熟度尚不明确。
  - 公开工作簿语料的版权与数据隐私问题可能成为规模化应用的潜在约束。
  score: 7.0
  article_ids:
  - ac2b1a4ff6a65efd
  evidence_snippets:
  - 论文摘要指出，他们引入了 workbook time machine，这是一个自动构建基准的流水线，用于评估语言模型在电子表格中创建派生对象的能力。
---

# Computer Science > Artificial Intelligence

# Title:Back to the Future: A workbook time machine for spread sheet creation benchmarks

View PDF HTML (experimental)Abstract:We introduce the workbook time machine, a pipeline that automatically creates benchmarks evaluating the ability of language models to create derived objects in spreadsheets (formulas, charts, pivot tables, and conditional formatting). Applied to public workbook corpora, it produces wtmcorpus--a collection of (input workbook, output workbook, query) triples spanning four artifact types and varying complexity. From this corpus we curate wtmbench, a 150-task evaluation benchmark with queries at three levels of specificity. We evaluate existing spreadsheet manipulation agents and baselines on wtmbench across artifact types, step complexity, and instruction granularity. Our evaluations show that query specificity, agent orchestration, and interface API used to control spreadsheets play a big role in LLM performance on Excel tasks.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.