---
title: 'BrainBench: Benchmarking Large Language Models for Comprehensive EEG Understanding'
source: https://arxiv.org/abs/2608.04156
author:
- '[[Yangxuan Zhou, Sha Zhao, Yuning Chen, Chen Wu, Jiquan Wang, Shijian Li, Gang
  Pan]]'
published: '2026-08-06'
created: '2026-08-06'
manifest_dates:
- '2026-08-06'
description: 'arXiv:2608.04156v1 Announce Type: new Abstract: Electroencephalography
  (EEG) analysis extends beyond assigning predefined labels to recordings; it requires
  workflows connecting natural-language instructions, signal processing, quantitative
  evidence, and scientific interpretation. We term this capability \emph{comprehensive
  EEG understanding}. Existing evaluations, however, primarily target isolated decoding
  tasks or system-specific demonstrations, leaving the competence of large language
  models (LLMs) insufficiently quantified. We introduce \benchmarkname{}, a unified
  benchmark for comprehensive, instruction-conditioned EEG understanding. It comprises
  four subsets---Foundational Analysis, Sleep Assessment, Neurocognitive Assessment,
  and Physiological Integration---covering 17 datasets, \numcases{} tasks, and over
  \numinstances{} real-data instances. Given an instruction and EEG recordings with
  optional physiological signals, a system must perform the analysis and produce a
  scientifically grounded report and, when required, artifacts. Outputs are assessed
  through numerical, categorical, set, sequence, semantic, and artifact validation.
  We evaluate \nummodels{} representative LLMs across more than 100K executions under
  two paradigms: autonomous code execution with CodeAct and structured agentic analysis
  with BrainAgent. Results vary substantially across models, subsets, difficulty levels,
  and execution paradigms, showing that EEG competence depends on the model and its
  operationalization. \benchmarkname{} provides a reproducible testbed for advancing
  LLM-based EEG understanding. The code and benchmark will be released soon, with
  evaluation results continuously updated.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: b2ea7a5c1ad9daad
source_type: academic_paper
tldr: BrainBench 是 arXiv 上发布的一个综合脑电图（EEG）理解基准，包含基础分析、睡眠评估、神经认知评估和生理整合四个子集，覆盖 17 个数据集和大量真实实例。研究者在超过
  10 万次执行中评估了多种大语言模型，结果显示不同模型、子集与执行范式下的 EEG 能力差异显著。
objective_summary: 这篇 arXiv 论文提出了 BrainBench，一个面向全面、指令条件下的 EEG 理解能力的统一基准。该基准包含基础分析、睡眠评估、神经认知评估与生理整合四个子集，覆盖
  17 个数据集。系统需依据指令与 EEG 记录生成科学报告，输出通过数值、类别、集合、序列、语义和产物六种方式验证。研究者在 CodeAct 自主代码执行与 BrainAgent
  结构化智能体分析两种范式下进行了超过 10 万次执行，结果显示 EEG 能力高度依赖模型及其操作化方式。论文称代码与基准将很快发布，评测结果会持续更新。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM
  - EEG
  - CodeAct
  - BrainAgent
  - BrainBench
  key_people: []
key_logic_flow:
- 论文认为 EEG 分析不能停留在给记录贴预定义标签，而需要连接自然语言指令、信号处理、定量证据与科学解释的完整工作流，并将这一能力称为全面 EEG 理解。
- 现有评测主要针对孤立的解码任务或系统特定演示，导致大语言模型在 EEG 上的能力未被充分量化。
- BrainBench 包含基础分析、睡眠评估、神经认知评估和生理整合四个子集，覆盖 17 个数据集和大量真实数据实例。
- 系统需根据指令与 EEG 记录生成科学报告及所需产物，输出通过数值、类别、集合、序列、语义和产物六种方式验证。
- 研究者在 CodeAct 自主代码执行与 BrainAgent 结构化智能体分析两种范式下评估了多个代表性大语言模型，总执行次数超过 10 万次。
- 结果显示不同模型、子集、难度层级和执行范式下表现差异显著，BrainBench 为推进基于大语言模型的 EEG 理解提供了可复现的测试平台。
object_mentions:
- object_type: project
  name: BrainBench
  canonical_name: BrainBench
  url: https://arxiv.org/abs/2608.04156
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - BrainBench 是论文提出的统一基准，用于全面、指令条件下的 EEG 理解评测，包含四个子集并覆盖 17 个数据集。
  - 论文在超过 10 万次执行中评估了多个代表性大语言模型，结果显示模型在不同子集、难度和范式下表现差异显著。
  article_id: b2ea7a5c1ad9daad
- object_type: project
  name: BrainAgent
  canonical_name: BrainAgent
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 论文将 BrainAgent 作为结构化智能体分析范式，与 CodeAct 自主代码执行范式并列用于评测大语言模型的 EEG 理解能力。
  article_id: b2ea7a5c1ad9daad
- object_type: project
  name: CodeAct
  canonical_name: CodeAct
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 论文在两种范式下评估大语言模型，其中 CodeAct 代表自主代码执行范式，用于执行 EEG 分析任务。
  article_id: b2ea7a5c1ad9daad
extract_result: success
impact_score:
  score: 5.0
  reason: 该论文为 LLM×EEG 交叉领域提供了首个综合性的指令条件化评测基准，覆盖 17 个数据集、四个子集、六种输出验证方式和 10 万+次执行，有望填补该细分领域缺乏标准化评测的空白，属于垂直赛道的重要基础设施性贡献。但影响范围局限于脑电分析这一小圈子子领域，且基准代码尚未开源、社区短期内无法直接复现与采用，既不像大模型发布那样改变局部竞争格局，也不构成范式转移，故评分落在中等区间。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 基准与评测代码尚未开源，六种输出验证机制和 CodeAct/BrainAgent 双范式的可复现性与实际落地效果
hype_assessment:
  level: low
  reason: 标题中的"Comprehensive（全面）"一词带有一定包装色彩，但论文整体表述克制，未滥用"颠覆""革命"等空洞词汇；文中给出了 17 个数据集、六类输出验证、10
    万+次执行的具体量化规模，信息密度扎实。主要水分隐患在于代码和基准尚未发布、评测结果持续更新的承诺有待兑现，"全面理解"的宣称需待社区复现检验，综合判定为实打实的干货为主、略有修饰。
information_entropy: high
domain_disruption:
  technical_innovation: 将 EEG 分析从"贴预定义标签"的解码式评测升级为"自然语言指令—信号处理—定量证据—科学解释"的完整工作流评测，首创数值/类别/集合/序列/语义/产物六种输出验证机制，并把"操作化方式"（CodeAct
    自主代码执行 vs BrainAgent 结构化智能体）作为独立自变量纳入对比，揭示模型能力与其工程化方式强耦合，这在该领域属首次系统性量化。
  business_model: 在神经科技与临床脑电分析赛道，标准化评测基准有望成为 LLM 驱动 EEG 分析工具采购与选型的行业标尺，间接催生面向睡眠评估、神经认知评估等场景的
    AI 辅助分析产品市场；基准开源后若被社区广泛采用，可能形成事实标准并重塑该垂直赛道的竞争与定价格局。
engineering_complexity: prototype
compound_value:
  score: 6.0
  reason: 作为 LLM×EEG 交叉领域的首个综合基准，具备成为细分赛道标准测试平台的潜力：覆盖 17 个数据集、四类评测子集（基础分析/睡眠评估/神经认知评估/生理整合）与六种输出验证机制，并以
    CodeAct 和 BrainAgent 两种智能体范式做了超过 10 万次执行，数据与标注资产具有长期复利效应；同时承诺持续更新评测结果，若被学术与产业界广泛采纳，可沉淀为神经科技
    LLM 应用的准入门槛。但当前基准与代码尚未正式发布，认识论状态仍为理论声明，且评测基准天然面临被更权威/更全面基准迭代取代的寿命风险，长期价值高度依赖社区采纳率，故评分落在'细分基础设施需持续验证'区间。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- OpenAI
- Anthropic
- Google DeepMind
- Emotiv
- BrainCo
competitive_casualty:
- 传统 EEG 信号分析软件厂商
- Natus Medical
- Compumedics
- 闭源神经数据分析平台
market_opportunities:
- 面向临床 EEG 报告自动化的垂直 AI 产品（睡眠评估、神经认知评估）存在落地空间，BrainBench 可作为能力验证与选型的评测标准，创业者可基于该基准打磨面向神经科/睡眠中心的诊断辅助工具
- CodeAct 自主代码执行范式可推广到 EEG 之外的生物医学信号分析（心电、肌电、脑磁图），具备跨领域的通用工具链商业化潜力
- 脑机接口与神经科技赛道中，LLM 驱动的神经信号理解评估基础设施（评测即服务）存在创业机会，可为下游厂商提供标准化能力认证
risk_matrix:
  regulatory: EEG 属于敏感医疗健康数据，若模型输出用于临床诊断报告，将面临 FDA/NMPA 等医疗器械监管审批，并受 HIPAA、个人信息保护法等患者隐私合规约束
  technological: LLM 在医学信号分析中存在幻觉与误判风险，且可能被 EEGNet、神经 Transformer 等专用模型或传统信号处理管线替代；基准论文尚未发布代码，方法可复现性存疑
  competitive: 脑电分析领域已有专用深度模型与既有医疗 AI 公司布局，通用 LLM 未必占据优势；若 OpenAI、Google 等巨头推出更全面的评测基准或专用
    EEG 模型，可能挤压本基准的影响力与采用率
  ethical: 脑电信号蕴含敏感神经与心理状态信息，存在隐私泄露与数据滥用风险；模型误诊可能导致错误临床决策伤害患者；自动化分析可能冲击脑电图技师、神经电生理人员的就业
  additional:
  - 论文为 arXiv 预印本且认识论状态为理论性主张，未经同行评审，代码与基准数据集尚未正式发布
confidence:
  impact: medium
  compound: medium
  hype: medium
actionable_insight: monitor
object_insights:
- object_type: project
  name: BrainBench
  canonical_name: BrainBench
  url: https://arxiv.org/abs/2608.04156
  positioning: BrainBench 是一个面向全面 EEG 理解能力的统一评测基准，通过四个子集与 17 个数据集评测大语言模型在指令条件下的脑电图分析能力。
  technical_signal: 基准覆盖基础分析、睡眠评估、神经认知评估与生理整合四个子集，输出通过数值、类别、集合、序列、语义和产物六种方式验证，评测设计较为系统。
  adoption_signal: 论文称代码与基准将很快发布，评测结果会持续更新，但目前尚未开源，社区采用情况有待观察。
  ecosystem_relevance: 该基准将 EEG 分析从贴标签扩展到连接自然语言指令、信号处理与科学解释的完整工作流，为 EEG-AI 评测提供了可复现测试平台。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: BrainBench 是少有的将 EEG 理解定义为完整工作流并系统化评测大语言模型的统一基准，其四子集、六重验证设计与超过 10
    万次执行规模为后续研究提供了可复现基线，值得持续跟踪其开源发布与评测结果更新。
  risk_notes:
  - 论文声称代码与基准将很快发布，但当前尚未开源，评测的可复现性有待验证。
  - 基准覆盖 17 个数据集与大量真实实例，但 EEG 数据获取与标注质量可能影响评测的泛化性与公平性。
  - 评测结果高度依赖模型及其执行范式，能力差异可能难以直接归因于模型本身的 EEG 理解水平。
  score: 6.0
  article_ids:
  - b2ea7a5c1ad9daad
  evidence_snippets:
  - BrainBench 是论文提出的统一基准，用于全面、指令条件下的 EEG 理解评测，包含四个子集并覆盖 17 个数据集。
  - 论文在超过 10 万次执行中评估了多个代表性大语言模型，结果显示模型在不同子集、难度和范式下表现差异显著。
---

# Computer Science > Artificial Intelligence

# Title:BrainBench: Benchmarking Large Language Models for Comprehensive EEG Understanding

View PDF HTML (experimental)Abstract:Electroencephalography (EEG) analysis extends beyond assigning predefined labels to recordings; it requires workflows connecting natural-language instructions, signal processing, quantitative evidence, and scientific interpretation. We term this capability \emph{comprehensive EEG understanding}. Existing evaluations, however, primarily target isolated decoding tasks or system-specific demonstrations, leaving the competence of large language models (LLMs) insufficiently quantified. We introduce \benchmarkname{}, a unified benchmark for comprehensive, instruction-conditioned EEG understanding. It comprises four subsets---Foundational Analysis, Sleep Assessment, Neurocognitive Assessment, and Physiological Integration---covering 17 datasets, \numcases{} tasks, and over \numinstances{} real-data instances. Given an instruction and EEG recordings with optional physiological signals, a system must perform the analysis and produce a scientifically grounded report and, when required, artifacts. Outputs are assessed through numerical, categorical, set, sequence, semantic, and artifact validation. We evaluate \nummodels{} representative LLMs across more than 100K executions under two paradigms: autonomous code execution with CodeAct and structured agentic analysis with BrainAgent. Results vary substantially across models, subsets, difficulty levels, and execution paradigms, showing that EEG competence depends on the model and its operationalization. \benchmarkname{} provides a reproducible testbed for advancing LLM-based EEG understanding. The code and benchmark will be released soon, with evaluation results continuously updated.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.