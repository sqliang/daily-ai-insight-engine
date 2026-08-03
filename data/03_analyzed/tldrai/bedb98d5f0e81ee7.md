---
title: AMD's Helios (4 minute read)
source: https://www.cnbc.com/2026/07/20/amd-helios-microsoft-ai-nvidia.html?utm_source=tldrai
author: []
published: ''
created: '2026-07-22'
manifest_dates:
- '2026-07-22'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: bedb98d5f0e81ee7
source_type: news_media
tldr: AMD 推出首款机架级 AI 系统 Helios，微软加入 Meta、OpenAI、Oracle 等客户行列。Helios 整合 AMD 自研 GPU、CPU、网络和软件，以最低每
  token 成本为目标，将于今年晚些时候开始出货。
objective_summary: 2026 年 7 月 20 日，AMD 宣布其首款机架级 AI 系统 Helios 即将出货，微软成为最新客户。Helios
  将 AMD 的 Instinct GPU、EPYC CPU、网络和软件整合为一体化系统，旨在以最低每 token 成本与 Nvidia 的 Grace Blackwell
  和 Vera Rubin 竞争。微软将在 Azure 数据中心部署 Helios 用于前沿模型推理，Meta、OpenAI、Oracle 和 Tata Consultancy
  Services 等也已承诺采用。Futurum Group 估计 Helios 单套系统成本在 500 万至 550 万美元之间，AMD 股价当日上涨超过 4%。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - AMD
  - Microsoft
  - Meta
  - OpenAI
  - Oracle
  - Tata Consultancy Services
  - SpaceX
  - Cohere
  - Nvidia
  - Futurum Group
  technologies:
  - Helios
  - Instinct GPU
  - EPYC
  - Venice
  - MI300X
  - Grace Blackwell
  - Vera Rubin
  - Maia
  key_people:
  - Forrest Norrod
  - Lisa Su
  - Satya Nadella
  - Daniel Newman
  - Jim Cramer
key_logic_flow:
- AMD 推出首款机架级 AI 系统 Helios，整合 GPU、CPU、网络和软件四大部分，旨在提供最低的每 token 成本。
- 微软宣布将采用 Helios 部署于 Azure 数据中心，用于前沿模型推理和 Azure AI 服务，同时新增两个基于 AMD Venice CPU 的计算实例，分别面向
  Agentic AI 和半导体设计。
- Meta 承诺部署高达 6 吉瓦的 AMD GPU，今年先以 1 吉瓦的 Helios 机架开局；OpenAI、Oracle 和 Tata Consultancy
  Services 也已承诺采用 Helios。
- Futurum Group 估计 Helios 单价在 500 万至 550 万美元之间，重量达 7000 磅，比 Nvidia Vera Rubin 更宽更重；Vera
  Rubin 估价为 350 万至 400 万美元。
- AMD 数据中心收入在 2026 年第一季度同比增长 57%，公司计划从 2027 年起实现数百亿美元的 AI 收入，其中大部分来自 Helios。
- Nvidia 控制着超过 95% 的数据中心 GPU 市场，AMD 仅占约 4.5%，但分析师认为 Helios 有望帮助 AMD 将份额提升至 20% 至 25%。
object_mentions:
- object_type: product
  name: AMD Helios
  canonical_name: AMD Helios
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - AMD 正在准备出货其首款专为人工智能设计的机架级系统 Helios，这是首个与 Nvidia Grace Blackwell 和 Vera Rubin 直接竞争的一体化系统。
  - 微软宣布将采用 Helios 系统部署于 Azure 数据中心，用于前沿模型推理和 Azure AI 服务，这是 Helios 获得的重要客户承诺。
  - Helios 整合了 AMD 自研的 GPU、CPU、网络和软件四大部分，AMD 表示该系统旨在提供最低的每 token 推理成本和最优总拥有成本。
  article_id: bedb98d5f0e81ee7
- object_type: product
  name: Nvidia Grace Blackwell
  canonical_name: Nvidia Grace Blackwell
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Helios 是首个直接与 Nvidia 广受欢迎的 Grace Blackwell 和 Vera Rubin 机架级系统竞争的同类产品。
  article_id: bedb98d5f0e81ee7
- object_type: product
  name: Nvidia Vera Rubin
  canonical_name: Nvidia Vera Rubin
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Futurum Group 估计 Nvidia 第二代机架级系统 Vera Rubin 单价在 350 万至 400 万美元之间，低于 Helios 的 500
    万至 550 万美元。
  article_id: bedb98d5f0e81ee7
- object_type: product
  name: AMD Instinct GPU
  canonical_name: AMD Instinct GPU
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - AMD 表示前十大 AI 公司中有八家在其 Instinct GPU 上运行工作负载，包括 OpenAI、Cohere 和 SpaceXAI。
  - 每个 Helios 计算托盘配备四块 Instinct GPU，由一颗 EPYC CPU 驱动，构成系统的核心算力单元。
  article_id: bedb98d5f0e81ee7
- object_type: product
  name: AMD MI300X
  canonical_name: AMD MI300X
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 微软在 2023 年率先采用了 AMD 的 MI300X GPU，该芯片是当时与 Nvidia AI 芯片直接竞争的产品。
  article_id: bedb98d5f0e81ee7
- object_type: product
  name: Microsoft Azure AI
  canonical_name: Microsoft Azure AI
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 微软 CEO Satya Nadella 表示正在扩展 Azure 基础设施组合以纳入 AMD Helios，为客户提供构建下一代 AI 应用程序所需的性能和选择。
  - Helios 系统将用于支持 Azure AI 服务以及微软 AI 客户的前沿模型推理工作负载。
  article_id: bedb98d5f0e81ee7
- object_type: product
  name: AMD Venice CPU
  canonical_name: AMD Venice CPU
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 微软将新增两个基于 AMD 最新 Venice CPU 的计算实例，一个面向 Agentic AI 和数据管道，另一个面向半导体设计。
  article_id: bedb98d5f0e81ee7
- object_type: product
  name: Microsoft Maia
  canonical_name: Microsoft Maia
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 微软在其数据中心内部署了自研的 Maia 芯片，与 AMD 芯片形成互补的计算资源布局。
  article_id: bedb98d5f0e81ee7
extract_result: success
impact_score:
  score: 7.5
  reason: AMD Helios 是 AMD 首款机架级 AI 系统，直接对标 Nvidia Grace Blackwell 和 Vera Rubin，标志着
    AI 基础设施市场从 Nvidia 单极垄断向双雄竞争格局转变的关键节点。Nvidia 目前控制 95%+ 的数据中心 GPU 市场，而 Helios 获得微软、Meta、OpenAI、Oracle
    等顶级客户的公开承诺部署，分析师预计有望帮助 AMD 将份额提升至 20-25%。这一变化将直接影响全球 AI 算力的定价结构（最低每 token 成本）和供应链弹性，属于改变局部竞争格局的重大事件。虽非
    ChatGPT 发布级别的范式转移，但对 AI 基础设施产业链有深远影响。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: Nvidia 之外的 viable AI 推理硬件替代方案及其每 token 成本优势
hype_assessment:
  level: medium
  reason: 文章存在一定程度的 PR 包装，如 'lowest cost per token' 和 'significant benefits' 等宣称性表述，这些是
    AMD 高管的自我宣称而非独立第三方验证。但整体内容有坚实的客户承诺（微软、Meta、OpenAI 等）、具体技术参数（18 计算托盘、4 Instinct
    GPU 配 1 EPYC CPU）、分析师定价估算（500-550 万美元）和出货时间表（今年晚些时候）支撑，并非空洞的概念炒作。综合判定为中等包装程度。
information_entropy: high
domain_disruption:
  technical_innovation: AMD 首次将自研 Instinct GPU、EPYC CPU、网络和软件四部分整合为一体化机架级系统，以 '最低每
    token 成本' 为设计目标，在推理场景中强调内存带宽和容量优势，直接挑战 Nvidia 统一计算平台的主导地位。Helios 每个计算托盘配备 4 颗
    Instinct GPU + 1 颗 EPYC CPU，系统重达 7000 磅，体现了 AMD 从芯片供应商到系统平台商的架构级跃迁。
  business_model: Helios 将 AMD 从单一的 AI 芯片供应商转变为端到端系统平台商，直接复制 Nvidia DGX/Grace Blackwell
    的高附加值系统商业模式。若成功将市场份额从 4.5% 提升至 20-25%，将在数百亿美元的 AI 数据中心市场引入实质性竞争，可能显著降低 AI 推理的每
    token 成本，改变当前由 Nvidia 垄断定价的产业生态。
engineering_complexity: production_ready
compound_value:
  score: 7.8
  reason: AMD Helios 是首个在机架级系统层面正面挑战 NVIDIA Grace Blackwell/Vera Rubin 的产品，整合了 AMD
    自研的 GPU、CPU、网络和软件四要素，以'最低每 token 成本'为核心价值主张直接切中 AI 推理市场爆发期的最关键需求。从长期复利角度看：(1)
    微软、Meta、OpenAI、Oracle、TCS 等顶级客户的明确采购承诺提供了数百亿美元的可见收入基本盘，Meta 一家就承诺最高 6 吉瓦的 AMD
    GPU 部署；(2) AMD 在 CPU 领域的深厚积累（EPYC/Venice）使其在系统集成层面具备 NVIDIA 所没有的差异化优势，NVIDIA 的
    CPU 战略仍在调整中；(3) AMD 数据中心收入同比增长 57%，公司计划从 2027 年起实现数百亿美元 AI 收入，表明其已进入增长正循环。若 AMD
    能如分析师预期将 GPU 市场份额从 4.5% 提升至 20-25%，Helios 将成为 AI 基础设施不可或缺的第二极，具备极强的长期复利效应。但需关注的风险：Helios
    单套成本（500-550 万美元）高于 Vera Rubin（350-400 万美元），在价格竞争中需以性能/TCO 证明自身价值；CUDA 软件生态壁垒仍是
    AMD 最大的结构性挑战；大规模交付可靠性有待验证。综合评估，Helios 有望成为 AI 推理基础设施的长期基石产品，复利效应显著但执行风险不可忽视。
value_capture_layer: hardware_compute
moat_impact: democratizes_access
key_beneficiaries:
- AMD
- Microsoft
- Meta
- OpenAI
- Oracle
competitive_casualty:
- NVIDIA
- Intel
- 中小型 AI 芯片初创公司
market_opportunities:
- AI推理基础设施买方应系统评估AMD Helios的每token成本优势，将其纳入多供应商采购策略以增强对Nvidia的议价能力，预计2027年起AMD将冲击20-25%的GPU市场份额
- 关注AMD ROCm软件生态成熟度拐点，提前构建跨平台AI推理管线（CUDA+ROCm）的工程能力，避免单一架构锁定风险，尤其适合推理密集型应用场景
- 基于AMD Venice CPU + Helios组合的垂直优化机会浮现，半导体设计自动化（EDA）和Agentic AI工作流等场景可率先获得端到端架构优化红利
risk_matrix:
  regulatory: 中美芯片出口管制持续收紧，Helios涉及的先进GPU和CPU跨境部署可能面临许可证审查，影响全球客户的部署节奏和市场覆盖范围
  technological: AMD ROCm软件生态成熟度和开发者工具链与CUDA仍有显著差距，独立第三方性能基准尚未发布，实际推理性能和每token成本优势有待验证
  competitive: Nvidia控制超过95%的数据中心GPU市场，CUDA生态锁效应极强，且Vera Rubin定价（$3.5M-$4M）低于Helios（$5M-$5.5M），价格上更具侵略性
  ethical: 单套系统重达7000磅、单价超500万美元，AI算力进一步向少数超大规模企业集中，加剧算力资源分配不均与能源消耗的环境影响
  additional:
  - Helios供应链依赖台积电先进封装产能，产能瓶颈可能导致出货延迟或配额限制，影响客户部署时间表
confidence:
  impact: medium
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: AMD Helios
  canonical_name: AMD Helios
  url: null
  positioning: AMD 推出的首款机架级 AI 系统，整合自研 Instinct GPU、EPYC CPU、网络和软件，以最低每 token 成本为目标直接挑战
    Nvidia 统治地位。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 微软 Azure 数据中心
  - Meta
  - OpenAI
  - Oracle
  - 塔塔咨询服务
  product_signal: 整合自研 GPU、CPU、网络和软件四大部分，每计算托盘配备四块 Instinct GPU 由一颗 EPYC CPU 驱动，旨在提供最低每
    token 推理成本和最优总拥有成本。
  market_signal: 微软成为最新客户，Meta 承诺部署 6 吉瓦 AMD GPU 且首年以 1 吉瓦 Helios 机架开局，Futurum Group
    估价单套 500 万至 550 万美元，AMD 股价当日涨超 4%。
  differentiation: 对比 Nvidia Vera Rubin（估价 350-400 万美元），Helios 强调更低每 token 成本和更高内存带宽，但单价高出约
    150 万美元且物理尺寸更大更重。
  watch_reason: 作为 AMD 首个全栈自研 AI 机架系统，Helios 已获微软、Meta、OpenAI、Oracle 等头部客户承诺，有望将 AMD
    数据中心 GPU 市占率从 4.5% 提升至 20%-25%，是多年来对 Nvidia 统治地位的最有力挑战。
  risk_notes:
  - Helios 单价 500 万至 550 万美元，显著高于 Nvidia Vera Rubin 的 350-400 万美元，在价格敏感市场中面临竞争劣势。
  - AMD 数据中心 GPU 市场份额仅 4.5%，CUDA 生态和软件工具链与 Nvidia 差距显著，现有客户迁移存在较高技术壁垒。
  score: 9.0
  article_ids:
  - bedb98d5f0e81ee7
  evidence_snippets:
  - AMD 正在准备出货其首款专为人工智能设计的机架级系统 Helios，这是首个与 Nvidia Grace Blackwell 和 Vera Rubin 直接竞争的一体化系统。
  - 微软宣布将采用 Helios 系统部署于 Azure 数据中心，用于前沿模型推理和 Azure AI 服务，这是 Helios 获得的重要客户承诺。
  - Helios 整合了 AMD 自研的 GPU、CPU、网络和软件四大部分，AMD 表示该系统旨在提供最低的每 token 推理成本和最优总拥有成本。
- object_type: product
  name: Nvidia Grace Blackwell
  canonical_name: Nvidia Grace Blackwell
  url: null
  positioning: Nvidia 推出的机架级 AI 系统，在数据中心 GPU 市场占据超 95% 的统治地位，是 AMD Helios 的首要对标竞品。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI 企业与云服务提供商
  product_signal: 作为 Nvidia 机架级系统产品线的核心成员，与后继系统 Vera Rubin 共同构成 Nvidia AI 基础设施的完整产品矩阵。
  market_signal: Nvidia 控制数据中心 GPU 市场超 95% 份额，Grace Blackwell 是该市场的事实标准，拥有最广泛的客户部署基础。
  differentiation: 相较于 AMD Helios 强调每 token 成本和内存带宽优势，Grace Blackwell 拥有成熟的 CUDA 软件生态和更高市场接受度。
  watch_reason: Grace Blackwell 作为 Helios 的直接对标竞品，其市场表现和迭代节奏是衡量 AMD 新产品竞争力的关键参照系，将直接反映
    AI 芯片竞争格局的变化。
  risk_notes:
  - Grace Blackwell 在本文中仅作为竞品对比提及，缺乏独立产品动态信息，分析完整性有限。
  - Nvidia 正从 Grace Blackwell 向 Vera Rubin 迭代，前代产品可能逐步退出市场焦点。
  score: 4.0
  article_ids:
  - bedb98d5f0e81ee7
  evidence_snippets:
  - Helios 是首个直接与 Nvidia 广受欢迎的 Grace Blackwell 和 Vera Rubin 机架级系统竞争的同类产品。
- object_type: product
  name: Nvidia Vera Rubin
  canonical_name: Nvidia Vera Rubin
  url: null
  positioning: Nvidia 第二代机架级 AI 系统，作为 Grace Blackwell 的后继产品在 AI 基础设施市场维持竞争优势。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 大规模 AI 企业和云服务商
  product_signal: 作为 Nvidia 第二代机架级系统，相较前代 Grace Blackwell 在性能和架构上进一步升级，用于应对来自 AMD
    Helios 的竞争压力。
  market_signal: Futurum Group 估价 Vera Rubin 单价 350 万至 400 万美元，低于 Helios 的 500 万至
    550 万美元，在定价上保持优势。
  differentiation: 相比 Helios 定价更低且拥有成熟生态体系，但在内存带宽和每 token 推理成本方面 AMD 声称 Helios 具有优势。
  watch_reason: Vera Rubin 是 Nvidia 保持 AI 硬件市场主导地位的关键产品，其与 Helios 的竞争将决定未来 AI 基础设施市场的格局走向。
  risk_notes:
  - Vera Rubin 在本文中仅作为定价对比参照，缺乏产品本身的技术细节和性能数据。
  - AMD Helios 的推出可能迫使 Nvidia 加速迭代或调整定价策略以维持竞争力。
  score: 4.0
  article_ids:
  - bedb98d5f0e81ee7
  evidence_snippets:
  - Futurum Group 估计 Nvidia 第二代机架级系统 Vera Rubin 单价在 350 万至 400 万美元之间，低于 Helios 的 500
    万至 550 万美元。
- object_type: product
  name: AMD Instinct GPU
  canonical_name: AMD Instinct GPU
  url: null
  positioning: AMD 针对 AI 和高性能计算推出的数据中心 GPU 系列，是 Helios 机架级系统的核心算力组件。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI 企业与数据中心运营商
  product_signal: 每个 Helios 计算托盘配备四块 Instinct GPU 由一颗 EPYC CPU 驱动，前十大 AI 公司中有八家在其上运行工作负载。
  market_signal: AMD 称前十大 AI 公司中有八家在 Instinct GPU 上运行工作负载，包括 OpenAI、Cohere 和 SpaceXAI，客户基础持续扩大。
  differentiation: 作为 Helios 核心组件，Instinct GPU 与自研 CPU、网络和软件深度整合，在推理场景的内存带宽和每 token
    成本上区别于 Nvidia GPU。
  watch_reason: Instinct GPU 作为 AMD AI 战略的硬件核心，其性能和客户采用率直接决定 Helios 系统的市场竞争力，是 AMD
    提升市占率的关键载体。
  risk_notes:
  - Instinct GPU 在软件生态和开发者工具链方面与 Nvidia CUDA 相比仍有显著差距。
  - 前十大 AI 公司中有八家使用 Instinct GPU，但实际采购规模和部署深度尚不明确。
  score: 6.0
  article_ids:
  - bedb98d5f0e81ee7
  evidence_snippets:
  - AMD 表示前十大 AI 公司中有八家在其 Instinct GPU 上运行工作负载，包括 OpenAI、Cohere 和 SpaceXAI。
  - 每个 Helios 计算托盘配备四块 Instinct GPU，由一颗 EPYC CPU 驱动，构成系统的核心算力单元。
- object_type: product
  name: AMD MI300X
  canonical_name: AMD MI300X
  url: null
  positioning: AMD 此前推出的旗舰 AI 加速 GPU，微软于 2023 年率先采用，为 AMD 在 AI 芯片市场建立客户关系奠定基础。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI 训练和推理场景的企业客户
  product_signal: MI300X 是 AMD 此前与 Nvidia AI 芯片直接竞争的产品，微软在 2023 年率先采用，为后续 Helios 客户关系奠定基础。
  market_signal: 微软在 2023 年率先采用 MI300X，标志着云巨头开始寻求 Nvidia 之外的 AI 芯片替代方案。
  differentiation: 作为 Helios 的前代 GPU 产品，MI300X 为 AMD 积累了企业级 AI 客户信任，但其系统级整合程度不及 Helios
    的全栈方案。
  watch_reason: MI300X 是 AMD AI GPU 路线图中的关键里程碑，其客户采用经验直接推动了 Helios 系统的市场策略和产品设计。
  risk_notes:
  - MI300X 在本文中仅作为历史背景提及，缺乏当前市场表现和竞争定位的独立信息。
  - 随着 Helios 推出和新一代 Instinct GPU 问世，MI300X 可能逐步退出主力产品线。
  score: 3.0
  article_ids:
  - bedb98d5f0e81ee7
  evidence_snippets:
  - 微软在 2023 年率先采用了 AMD 的 MI300X GPU，该芯片是当时与 Nvidia AI 芯片直接竞争的产品。
- object_type: product
  name: Microsoft Azure AI
  canonical_name: Microsoft Azure AI
  url: null
  positioning: 微软的云 AI 服务平台，通过整合 AMD Helios 系统扩展基础设施组合，为前沿模型推理和 AI 应用提供算力支撑。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Azure AI 客户
  - 微软内部模型开发团队
  product_signal: Azure 将部署 Helios 用于前沿模型推理和 Azure AI 服务，同时新增两个基于 AMD Venice CPU 的计算实例分别面向
    Agentic AI 和半导体设计。
  market_signal: 微软 CEO 亲自宣布扩展 Azure 基础设施组合纳入 AMD Helios，体现云巨头同时采纳多家芯片供应商以降低对 Nvidia
    依赖的战略。
  differentiation: Azure AI 通过同时部署自研 Maia 芯片、AMD Helios 和 Nvidia GPU，构建多元化 AI 算力底座以降低单一供应商依赖风险。
  watch_reason: Azure AI 对 Helios 的采用是 AMD 打入云基础设施市场的关键里程碑，其实际部署效果将直接影响其他云厂商的采购决策和竞争格局。
  risk_notes:
  - Azure 同时部署 Maia 自研芯片、AMD Helios 和 Nvidia GPU，Helios 面临来自微软内部和外部竞品的双重竞争。
  - 文章未披露 Azure 部署 Helios 的具体规模和时间表，实际影响尚待验证。
  score: 5.0
  article_ids:
  - bedb98d5f0e81ee7
  evidence_snippets:
  - 微软 CEO Satya Nadella 表示正在扩展 Azure 基础设施组合以纳入 AMD Helios，为客户提供构建下一代 AI 应用程序所需的性能和选择。
  - Helios 系统将用于支持 Azure AI 服务以及微软 AI 客户的前沿模型推理工作负载。
---

After a decade-long comeback, chip giant Advanced Micro Devices is preparing to ship its first rack-scale system for artificial intelligence, called Helios, to a growing list of customers that now includes Microsoft.

It's the first rival to Nvidia's wildly popular Grace Blackwell and Vera Rubin systems, and is aiming to give the world's most valuable chipmaker its first real competition in years.

Microsoft announced Monday it will use the Helios system in its data centers, joining Meta, OpenAI, Oracle and others in a race to grab as much compute as possible.

AMD will begin shipping to customers, including Microsoft, later this year. Shares of AMD climbed more than 4% on Monday. Microsoft stock climbed more than 1%.

Details about financial terms or the amount of compute capacity weren't disclosed.

"We are expanding the Azure infrastructure portfolio with AMD Helios to give customers the performance, scale and choice they need to build and run the next generation of AI applications," Microsoft CEO Satya Nadella wrote in a press release.

The new Helios system will power frontier model inference for Microsoft, its AI customers and support Azure AI services. Microsoft will also add two new computing instances run on AMD's latest "Venice" central processing units, or CPUs, one for agentic AI and data pipelines, and another for semiconductor design.

It's the continuation of a longtime partnership, with AMD chips powering Microsoft's Surface PCs and Xbox gaming consoles for many years. In 2023, Microsoft was also the first to adopt AMD's MI300X graphics processing unit, or GPU, that rivaled Nvidia's AI chips. Microsoft also deploys its own Maia chips in its data centers.

Like its peers, Microsoft needs as much compute as possible, especially as it ramps up its own model development and allocates more computing capacity to research and development. In June, it announced seven models built in-house. Microsoft's AI efforts thus far have seen mixed results, from its 365 Copilot AI assistant to its GitHub Copilot coding agent. It's the worst-performing "Magnificent Seven" stock so far this year.

Microsoft is part of a growing number of big companies turning to AMD for AI acceleration. AMD says eight of the top 10 AI companies run workloads on its Instinct GPUs, including OpenAI, Cohere and Elon Musk's SpaceXAI, which is part of SpaceX.

In February, Meta* *announced it'll use up to 6 gigawatts of AMD GPUs over time, starting with 1 gigawatt deployed on Helios racks later this year. OpenAI and Oracle also made major commitments to deploy Helios this year, with India's largest IT company, Tata Consultancy Services, committing to use it as well.

CNBC got the world's first detailed look inside a Helios system, from the Texas data center lab where it's being developed and tested.

### 'Lowest cost per token'

Named for an ancient Greek god who pulls the sun across the sky with the help of four horses, Helios brings together four things AMD does in-house: GPUs, CPUs, networking and software.

"We're very focused on providing the best total cost of ownership, the lowest cost per token, all in," data center head Forrest Norrod told CNBC about AMD's first-generation system. "And our customers are telling us that we're achieving that."

In May, AMD CEO Lisa Su told CNBC's Jim Cramer that Helios has "significant benefits" over Nvidia's rack-scale systems, "when you're talking about inference and when you're talking about memory bandwidth and memory capabilities."

While AMD wouldn't comment on cost, the Futurum Group estimates Helios will cost between $5 million and $5.5 million. That's compared with Futurum estimates of $3.5 million to $4 million for Nvidia's second-generation rack-scale system, Vera Rubin.

At up to 7,000 pounds, Helios is also wider and heavier than Nvidia's Vera Rubin.

Nvidia controls more than 95% of the data center GPU market, according to the Futurum Group. AMD only holds some 4.5% of the market, but Helios could change that.

"I think there's a serious case in which AMD does great and can get to 20% and 25%. And by the way, this is hundreds of billions of dollars of revenue," said Daniel Newman, analyst and CEO of the Futurum Group.

In the first quarter of 2026, data centers made up the majority of AMD's revenue, up 57% year over year. AMD told CNBC that it plans to book tens of billions in data center AI revenue starting in 2027, the majority coming from Helios.

In data center CPU market share, Intel remains the clear leader, but AMD has steadily been gaining ground. This CPU leadership sets AMD apart from Nvidia, which launched its first server CPU in 2021 and shifted strategies to renew focus on the chips this year.

### 'A very different AMD'

Norrod called Helios "our baby," as he showed CNBC the system's core chips. Each of its 18 compute trays has four Instinct GPUs powered by a single EPYC central processing unit.