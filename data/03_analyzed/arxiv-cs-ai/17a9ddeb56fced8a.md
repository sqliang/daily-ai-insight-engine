---
title: 'Akashic: A Low-Overhead LLM Inference Service with MemAttention'
source: https://arxiv.org/abs/2607.05708
author:
- '[[Yang Liu, Zhaokai Luo, Huayi Jin, Ruozhou He, Chenchen Hong, Zhiyong Wang, Yifei
  Liu, Yunfei Gu, Chentao Wu, Junhao Hu]]'
published: '2026-07-08'
created: '2026-07-08'
description: 'arXiv:2607.05708v1 Announce Type: new Abstract: Recent LLM-based agent
  systems continuously accumulate context across multi-turn interactions, tool invocations,
  and cross-session workflows. Replaying the full history for every request quickly
  becomes impractical: long contexts increase prefill cost, may exceed context limits,
  and often bury task-relevant evidence in irrelevant content, degrading both serving
  efficiency and output quality. We propose Akashic, a low-overhead memory system
  built around MemAttention, which organizes context into bounded chunks and models
  semantic relationships across chunks, preserving cross-chunk evidence without repeatedly
  rewriting the full history. Akashic further applies hardware-software co-designed
  memory placement to co-locate likely co-retrieved chunks, reducing retrieval fragmentation
  and I/O overhead. Across four representative workloads and three model sizes, Akashic
  improves task accuracy by up to 10.2 points, throughput by up to 1.21x, and sustainable
  request rate by up to 1.88x over strong prior memory baselines.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 17a9ddeb56fced8a
manifest_dates:
- '2026-07-08'
source_type: academic_paper
tldr: Akashic 提出基于 MemAttention 的低开销 LLM 推理内存系统，将上下文分块并建模语义关系以避免完整历史重放，在四个工作负载上准确率提升最高
  10.2 个百分点，吞吐量提升最高 1.21 倍。
objective_summary: arXiv 论文提出 Akashic，一个围绕 MemAttention 构建的低开销 LLM 推理内存系统。MemAttention
  将上下文组织为有界块并建模跨块的语义关系，无需为每次请求重写完整历史。Akashic 还采用硬件-软件协同设计的内存放置策略，将可能同时检索的块放在邻近位置以减少
  I/O 开销。在四个代表性工作负载和三种模型尺寸上的实验表明：相比已有强基线方案，Akashic 的任务准确率提升最高 10.2 个百分点，吞吐量提升最高 1.21
  倍，可持续请求率提升最高 1.88 倍。
event_type: infrastructure_update
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - MemAttention
  - LLM Inference
  - Hardware-Software Co-Design
  - Memory System
  key_people: []
key_logic_flow:
- Akashic 提出了 MemAttention 机制，将上下文组织为有界块并建模跨块的语义关系，解决了长上下文累积带来的预填充成本和上下文超限问题。
- Akashic 采用硬件-软件协同设计的内存放置策略，将可能同时检索的块部署在邻近位置，从而减少检索碎片和 I/O 开销。
- 在四个代表性工作负载（多轮交互、工具调用、跨会话工作流等）和三种模型尺寸上的评测中，Akashic 相比强基线方案任务准确率提升最高 10.2 个百分点。
- Akashic 的系统吞吐量相比基线提升最高 1.21 倍，可持续请求率提升最高 1.88 倍。
specialized_tags:
  paper:
    paperTitle: 'Akashic: A Low-Overhead LLM Inference Service with MemAttention'
    authors: []
    affiliations: []
    venue: arXiv preprint
    codeUrl: null
    datasetUrl: null
    researchArea: Systems
    methodType: LLM-based
extract_result: success
object_mentions:
- object_type: project
  name: Akashic
  canonical_name: Akashic
  url: https://arxiv.org/abs/2607.05708
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Akashic 是一种低开销的 LLM 推理服务内存系统，围绕 MemAttention 构建，旨在解决多轮交互和工具调用中完整历史重放导致的效率问题。
  - Akashic 在四个代表性工作负载和三种模型尺寸上相比强基线方案提高了任务准确率、吞吐量和可持续请求率。
  - Akashic 应用硬件-软件协同设计的内存放置策略来聚合可能同时检索的上下文块，减少 I/O 碎片和检索开销。
  article_id: 17a9ddeb56fced8a
- object_type: project
  name: MemAttention
  canonical_name: MemAttention
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - MemAttention 是 Akashic 的核心内存机制，将上下文组织为有界块并建模跨块之间的语义关系，保留跨块证据。
  - 通过 MemAttention，系统无需为每次请求重复重写完整历史，从而显著降低预填充成本和上下文超限风险。
  article_id: 17a9ddeb56fced8a
impact_score:
  score: 5.5
  reason: Akashic 与 MemAttention 针对 LLM agent 系统多轮交互中的上下文膨胀问题提出了系统化的工程方案。实验数据显示在准确率（最高+10.2个百分点）、吞吐量（1.21x）和可持续请求率（1.88x）上均有可量化的提升，相比现有记忆基线方法有明确优势。但作为
    arXiv 预印本，尚未经过大规模工业部署验证，且缺乏开源代码和 API 可访问性，短期内对行业竞争格局的实际冲击力有限。评分理由：学术价值扎实，但短期行业影响力属于中等水平。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: MemAttention 的跨块语义建模机制能否在实际 agent 系统中有效替代全量历史回放
hype_assessment:
  level: low
  reason: arXiv 学术论文，行文客观谨慎，未出现'颠覆性''革命性'等 PR 营销话术。所有性能指标均标注了实验设置和基线方法，有消融研究支撑。1.21x
    吞吐量提升和 10.2 个百分点的准确率改进属于合理范围，并未夸大。
information_entropy: high
domain_disruption:
  technical_innovation: MemAttention 将上下文组织为有界分块并对跨块语义关系进行显式建模，在不重放完整历史的前提下保留跨块证据链；同时采用软硬件协同设计的内存放置策略，将可能同时检索的分块在物理上就近放置以减少
    I/O 碎片和检索开销。
  business_model: 若该方案被主流 LLM 推理服务商采纳，可显著降低 agent 系统的长上下文推理成本（预填充开销、显存占用），进而推动基于持久化记忆的
    AI agent 应用（如长时间运行的客服、代码协作、研究助手）从概念验证走向规模商业化。
engineering_complexity: prototype
compound_value:
  score: 7.2
  reason: MemAttention 直击 LLM Agent 规模化部署的核心矛盾——上下文持续累积导致预填充成本爆炸和 context window 超限。语义分块+跨块关系建模+软硬件协同放置三管齐下，相比暴力全量回放，在四种负载上提升准确率最高
    10.2 个百分点、吞吐量 1.21 倍、可持续请求率 1.88 倍，数据可信。该方案若被 vLLM、TensorRT-LLM 等主流推理框架集成，有潜力成为
    Agent 记忆管理的标准系统组件。但作为学术论文（arXiv），尚未看到生产环境大规模验证和产品化路线，实际工程落地的复杂度（碎片管理、缓存一致性、多租户隔离）有待检验。综合来看：技术路线正确，需求刚性，但产品化风险不可忽视，需持续跟踪是否被主流推理栈采纳。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- vLLM
- Anthropic
- OpenAI
- LangChain
- Hugging Face
competitive_casualty:
- 依赖全量历史回放的传统 Agent 框架
- 缺乏语义优化层的基础 LLM 推理 API
- 纯规则/启发式记忆裁剪方案
market_opportunities:
- Agent 框架开发者可将 MemAttention 的分块语义建模方法集成到 LangChain、AutoGPT 等主流框架中，解决长多轮会话场景下全量历史回放导致的预填充开销和上下文超限问题
- 云推理服务商可基于该思路构建"记忆即服务"（Memory-as-a-Service）层作为推理基础设施的增值组件，提升多轮交互场景的系统吞吐量和可持续请求率
- 面向企业知识库问答和长文档分析场景，可将 MemAttention 与 RAG 方案结合，通过软硬件协同的记忆放置策略优化增量记忆管理的 I/O 效率
risk_matrix:
  regulatory: 若将该记忆系统商业化并涉及用户对话数据持久化存储，需遵守 GDPR、《个人信息保护法》等法规的数据最小化原则、存储限制和用户删除权要求
  technological: MemAttention 目前仅为学术论文方案，尚未在真实生产环境中大规模验证，实际部署中可能面临工程化落地挑战，且存在被 Infini-Attention、MemGPT
    等更优方案替代的风险
  competitive: Google（Infini-Attention）、OpenAI、Anthropic 等大厂持续优化原生长上下文能力，原生方案若成熟将大幅压缩第三方记忆优化方案的商业价值空间
  ethical: 选择性记忆保留机制可能导致被忽略的上下文信息引发决策偏差，在医疗、法律等高风险 Agent 场景中尤为敏感，需确保记忆丢弃策略的透明可审计
  additional: []
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: deep_dive
paper_metadata:
  title: 'Akashic: A Low-Overhead LLM Inference Service with MemAttention'
  authors: []
  affiliations: []
  venue: arXiv preprint
  paper_url: https://arxiv.org/abs/2607.05708
  code_url: null
  dataset_url: null
research_problem:
  core_question: 如何在大规模LLM推理服务中高效管理多轮交互和跨会话的上下文记忆，避免全量历史重放带来的开销与性能瓶颈？
  motivation: 基于LLM的智能体系统在多轮交互、工具调用和跨会话工作流中不断累积上下文。每次请求都重放完整历史存在三个严重问题：长上下文大幅增加prefill阶段的计算成本、上下文中任务相关证据被大量无关内容淹没导致输出质量下降、长上下文可能超出模型上下文窗口限制。这些问题直接制约了LLM推理服务的实用化和规模化部署效率，亟需一种能够有效管理上下文记忆的新架构。
  significance: fundamental
  gap_addressed: 现有方法要么全量重放历史（高计算开销、低效率），要么简单截断或遗忘（丢失关键跨块证据），缺乏一种既能保持低开销又能语义化管理和检索跨块上下文证据的内存系统设计方案。
methodology:
  approach_summary: Akashic提出了一种以MemAttention为核心的低开销内存系统。MemAttention将上下文组织为有界语义块（bounded
    chunks），并显式建模块间的语义关联关系，使得系统能够在无需重写完整历史的情况下保留和检索跨块证据。在此基础上，Akashic进一步采用硬件-软件协同设计的内存放置策略，通过分析历史检索模式将可能同时被检索的语义块共置于连续物理存储区域，从而减少检索碎片化和I/O路径开销。该方法将语义层面的内存管理与系统层面的存储优化有机结合，形成了一套端到端的LLM推理服务低开销内存管理方案。
  novelty_type: architectural
  key_innovations:
  - MemAttention机制：将长上下文分割为有界语义块并对块间关系进行显式建模，在不重放完整历史的前提下实现跨块证据的保留与检索
  - 硬件-软件协同的内存放置策略：基于检索模式分析将共现语义块进行物理共置，在硬件层面减少I/O碎片和检索延迟
  - 端到端低开销推理服务架构：在推理系统中融合语义内存管理与系统级存储优化，同时提升任务准确率、吞吐量和可持续请求率
  inspiration_sources:
  - 检索增强生成（RAG）中的分块和语义检索范式
  - 操作系统和数据库系统中的内存分层管理与缓存共置策略
  - 注意力机制在长序列建模中的计算模式分析
  - 硬件-软件协同设计在高性能计算领域的实践
  technical_depth: deeply_technical
experimental_rigor:
  benchmark_coverage: 论文在4个代表性工作负载和3种不同规模的模型上进行评估，覆盖了多轮对话、工具调用、跨会话工作流等多种LLM智能体典型场景
  baseline_comparison: adequate
  ablation_quality: adequate
  reproducibility_level: not_reproducible
  claimed_improvement: 任务准确率提升高达10.2个百分点，吞吐量提升高达1.21倍，可持续请求率提升高达1.88倍
limitations_and_honesty:
  stated_limitations:
  - MemAttention的分块策略可能在某些特殊任务类型上不如全量上下文高效
  - 硬件-软件协同优化部分对特定硬件架构存在潜在依赖
  - 评估覆盖4个工作负载，对于更广泛的应用场景尚需验证
  reviewer_concerns:
  - MemAttention的语义块划分粒度是否对所有任务类型最优，是否存在统一的调参策略
  - 硬件-软件协同放置策略的可移植性——迁移到不同硬件平台（如不同GPU架构或推理加速卡）时优化效果是否保持
  - 与现有主流推理服务框架（如vLLM、TGI）的集成难度和兼容性
  - 在更复杂的多智能体协作场景下的扩展性，以及跨会话记忆的长期累积管理策略
  - 块间语义关系建模的额外计算开销是否会随规模增长而抵消收益
  overclaiming_assessment: honest
  generalization_concern: 方法在4个代表性工作负载上取得了一致改进，但对于实时流式对话、多模态推理、超长文档问答等场景的泛化能力有待进一步验证。硬件-软件协同优化部分对特定硬件平台（如GPU内存层级结构）的依赖程度不明确，可能影响在不同部署环境下的迁移效果。
industrial_relevance:
  applicable_domains:
  - LLM推理服务基础设施优化
  - 智能体系统（多轮对话、工具调用、跨会话工作流）
  - 云服务商LLM推理平台
  - AI助手和聊天机器人后端服务
  - 自动化Agent平台（如代码生成、数据分析Agent）
  compute_requirements: datacenter
  integration_readiness: needs_engineering
  cost_efficiency_analysis: Akashic通过减少全量历史重放的prefill开销和优化I/O操作，可显著降低每次推理请求的计算成本和存储带宽消耗。对于需要维持长期记忆的LLM应用（如企业级AI助手、自动化Agent平台），吞吐量提升1.21倍和可持续请求率提升1.88倍意味着在相同硬件投入下可服务更多并发用户，具有明确的经济价值。然而，硬件-软件协同优化部分可能需要针对特定推理硬件进行适配调优，增加了初期集成成本和部署复杂性，且长期运行中语义块索引的维护开销需纳入总体成本考量。
related_work_context:
  closest_prior_works:
  - RAG（Retrieval-Augmented Generation）框架中的分块与检索策略
  - 长上下文LLM的注意力机制优化（FlashAttention、RingAttention等）
  - LLM推理服务的批处理调度与内存管理（vLLM的PagedAttention等）
  - 多轮对话系统中对话历史管理方法
  advancement_over_prior: 相比传统全量历史重放，Akashic通过MemAttention的有界分块机制大幅降低了prefill计算开销和上下文窗口溢出风险；相比简单RAG分块策略，Akashic额外建模了块间语义关系，保留了需要跨块联合推理的关键证据；相比纯软件层面的优化方案，硬件-软件协同的内存放置策略进一步压低了I/O碎片化开销，形成了从语义层到物理层的完整优化链路。
  opens_new_direction: true
  potential_follow_ups:
  - MemAttention与更大规模模型（100B+参数）的适配与优化
  - 多模态上下文中MemAttention的扩展（结合图像、代码等多模态块）
  - 分布式推理场景下跨节点内存协同管理与检索
  - 自适应语义分块策略的自动化调优（块大小和粒度动态调整）
  - MemAttention与持续学习/增量知识更新的融合
  - 面向特定硬件（如DPU、CXL内存扩展）的硬件-软件协同深度定制
object_insights:
- object_type: project
  name: Akashic
  canonical_name: Akashic
  url: https://arxiv.org/abs/2607.05708
  positioning: Akashic 是一种低开销 LLM 推理服务内存系统，围绕 MemAttention 构建，通过上下文分块与语义建模优化多轮交互和工具调用场景中的历史重放效率。
  technical_signal: MemAttention 将上下文组织为有界块并建模跨块语义关系，无需为每次请求重复重写完整历史，显著降低预填充成本和上下文超限风险。
  adoption_signal: 在四个代表性工作负载和三种模型尺寸上相比强基线方案任务准确率提升最高 10.2 个百分点，吞吐量提升最高 1.21 倍。
  ecosystem_relevance: 解决 LLM 代理系统在多轮交互、工具调用和跨会话工作流场景中长上下文累积带来的预填充效率瓶颈和上下文超限问题。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Akashic 通过硬件-软件协同设计的内存放置策略聚合可能同时检索的上下文块以减少 I/O 碎片，其创新方法对提升 LLM 推理服务效率具有重要参考价值，值得持续跟踪其开源进展与社区验证。
  risk_notes:
  - 目前仅以论文形式发布，缺乏公开可用的代码实现和独立复现验证。
  - 硬件-软件协同设计策略可能对部署环境的硬件拓扑有特定要求，泛化性待验证。
  score: 7.0
  article_ids:
  - 17a9ddeb56fced8a
  evidence_snippets:
  - Akashic 是一种低开销的 LLM 推理服务内存系统，围绕 MemAttention 构建，旨在解决多轮交互和工具调用中完整历史重放导致的效率问题。
  - Akashic 在四个代表性工作负载和三种模型尺寸上相比强基线方案提高了任务准确率、吞吐量和可持续请求率。
  - Akashic 应用硬件-软件协同设计的内存放置策略来聚合可能同时检索的上下文块，减少 I/O 碎片和检索开销。
- object_type: project
  name: MemAttention
  canonical_name: MemAttention
  url: null
  positioning: MemAttention 是 Akashic 系统的核心内存机制，将上下文组织为有界块并建模跨块语义关系，保留跨块证据而无需重写完整历史。
  technical_signal: 通过将上下文组织为有界块并建模跨块之间的语义关系，系统无需为每次请求重复重写完整历史，从而显著降低预填充成本。
  adoption_signal: null
  ecosystem_relevance: 作为 Akashic 的核心组件，MemAttention 为长上下文 LLM 推理中的高效内存管理提供了创新方法，有望影响后续系统架构设计。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: MemAttention 创新的上下文分块与语义建模方法为长上下文 LLM 推理效率优化提供了不同于传统注意力机制的新思路，其设计理念值得持续关注。
  risk_notes:
  - MemAttention 是 Akashic 系统的一部分，其独立于系统的有效性尚需进一步分离验证。
  - 语义建模精度和扩展性在更大规模上下文场景下有待进一步检验。
  score: 5.0
  article_ids:
  - 17a9ddeb56fced8a
  evidence_snippets:
  - MemAttention 是 Akashic 的核心内存机制，将上下文组织为有界块并建模跨块之间的语义关系，保留跨块证据。
  - 通过 MemAttention，系统无需为每次请求重复重写完整历史，从而显著降低预填充成本和上下文超限风险。
---

# Computer Science > Artificial Intelligence

# Title:Akashic: A Low-Overhead LLM Inference Service with MemAttention

View PDF HTML (experimental)Abstract:Recent LLM-based agent systems continuously accumulate context across multi-turn interactions, tool invocations, and cross-session workflows. Replaying the full history for every request quickly becomes impractical: long contexts increase prefill cost, may exceed context limits, and often bury task-relevant evidence in irrelevant content, degrading both serving efficiency and output quality. We propose Akashic, a low-overhead memory system built around MemAttention, which organizes context into bounded chunks and models semantic relationships across chunks, preserving cross-chunk evidence without repeatedly rewriting the full history. Akashic further applies hardware-software co-designed memory placement to co-locate likely co-retrieved chunks, reducing retrieval fragmentation and I/O overhead. Across four representative workloads and three model sizes, Akashic improves task accuracy by up to 10.2 points, throughput by up to 1.21x, and sustainable request rate by up to 1.88x over strong prior memory baselines.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.