---
title: 'A Year in LLM Serving: Workload Evolution, Caching and Load-Balancing'
source: https://arxiv.org/abs/2608.13573
author:
- '[[William Nixon, Jon Durbin, Florian Standhartinger, Haryadi S. Gunawi, Juncheng
  Yang]]'
published: '2026-08-17'
created: '2026-08-17'
manifest_dates:
- '2026-08-17'
description: 'arXiv:2608.13573v1 Announce Type: new Abstract: Large Language Model
  (LLM) serving has become a critical cloud workload, and realistic traces are essential
  for motivating and benchmarking serving systems. However, existing LLM serving workload
  studies remain limited in scale and scope. They often observe short time periods
  and provide limited visibility into how users interact with models in production.
  As a result, they do not fully capture how LLM serving workloads evolve over time
  or how user-model interactions shape production traffic. In this work, we further
  the understanding of real-world LLM serving workloads through both a global characterization
  and a longitudinal study of a one-year production trace from Chutes. Unlike prior
  studies, our trace captures full production behavior across many models and users,
  including both popular and long-tail models. We analyze the workload from aggregate,
  temporal, model-level, and user-level perspectives, revealing workload evolution
  and user-model structure that are typically hidden behind aggregate views. To support
  future research, we will release the full one-year trace with the paper, enabling
  downstream studies of production behavior without relying on sampled or synthetically
  generated workloads.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 6df4b4be97cf4ca6
source_type: academic_paper
tldr: 一篇 arXiv 论文对 Chutes 平台一年期 LLM serving 生产 trace 做全局特征刻画与纵向研究，从聚合、时间、模型级和用户级四个视角揭示工作负载演化，并计划随论文发布完整
  trace 数据。
objective_summary: 该论文以 Chutes 平台一年期生产 trace 为研究对象，对真实 LLM serving 工作负载进行全局特征刻画与纵向研究。该
  trace 覆盖多模型多用户的完整生产行为，包含流行模型与长尾模型。作者从聚合、时间、模型级和用户级四个视角分析工作负载的演化规律与用户-模型结构，并宣布将随论文发布完整的一年期
  trace，使下游研究无需依赖采样或合成工作负载。
event_type: infrastructure_update
epistemic_status: theoretical_claim
entities:
  companies:
  - Chutes
  technologies:
  - LLM serving
  - LLM
  key_people: []
key_logic_flow:
- 现有 LLM serving 工作负载研究在规模和范围上有限，多只观察短时段，对生产环境中用户与模型的交互方式可见性不足。
- 本文基于 Chutes 平台的一年期生产 trace 进行全局特征刻画与纵向研究，突破了以往研究的尺度限制。
- 该 trace 记录了多个模型和用户的生产行为，既涵盖流行模型也包含长尾模型。
- 研究从聚合、时间、模型级和用户级四个视角分析工作负载，揭示通常被聚合视图隐藏的演化规律与用户-模型结构。
- 作者将随论文发布完整的一年期 trace，支持后续无需依赖采样或合成数据的生产行为研究。
object_mentions:
- object_type: paper
  name: 'A Year in LLM Serving: Workload Evolution, Caching and Load-Balancing'
  canonical_name: 'A Year in LLM Serving: Workload Evolution, Caching and Load-Balancing'
  url: https://arxiv.org/abs/2608.13573
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文对 Chutes 平台一年期生产 trace 进行全局特征刻画与纵向研究，并计划随论文发布完整的一年期 trace 数据。
  article_id: 6df4b4be97cf4ca6
- object_type: dataset
  name: Chutes one-year production trace
  canonical_name: Chutes one-year LLM serving production trace
  url: null
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - 该 trace 覆盖多个模型和用户的完整生产行为，包括流行模型与长尾模型，作者将随论文发布完整数据。
  article_id: 6df4b4be97cf4ca6
extract_result: success
impact_score:
  score: 5.5
  reason: 该论文发布的是 Chutes 平台一年期多模型多用户的生产 serving trace，并承诺随论文开放完整数据。从短期行业影响看，它不直接改变竞争格局，但真实生产
    trace 是 serving 系统研究（缓存、负载均衡、调度）的稀缺基础设施，有望像 Azure 公开 trace 一样成为社区基准数据集，推动下游工程优化，属于研究社区层面的高价值事件。评分依据：数据发布具有基础设施意义但需时间转化为行业实践，故定在中等偏上。
sentiment: neutral
developer_sentiment:
  tone: excited
  primary_focus: 完整一年期真实生产 trace 能否成为 serving 系统基准研究的标准数据集
hype_assessment:
  level: low
  reason: 论文表述克制、学术化，未使用'颠覆'或'革命性'等 PR 措辞；基于真实生产数据而非合成数据，且明确承诺开放完整 trace，供下游验证，属于实打实的干货。判定依据：无概念炒作词汇，贡献可复现可验证。
information_entropy: medium
domain_disruption:
  technical_innovation: 首个覆盖多模型多用户、包含长尾模型的一年期真实生产 serving trace 数据集，从聚合、时间、模型级、用户级四个视角揭示负载演化规律与用户-模型结构，为缓存命中率优化、负载均衡与调度策略研究提供此前缺失的真实数据基础，弥补了现有研究短时段、小规模的空白。
  business_model: 对推理服务生态而言，开放生产 trace 有望沉淀为 serving 系统领域的事实标准基准数据集，提升 Chutes 在学术与工程社区的话语权；长期可借数据驱动缓存与调度优化，降低推理服务成本结构，对
    MaaS（模型即服务）和云推理平台的商业竞争力形成间接影响。
engineering_complexity: production_ready
compound_value:
  score: 7.0
  reason: 该事件的核心资产是一年期、多模型多用户的生产级 LLM serving trace 数据集。在 serving 工作负载研究普遍依赖短时段采样或合成数据的背景下，这套完整真实数据一旦被社区广泛采用，有望成为
    serving 系统优化领域的基准数据集，具备类似 ImageNet 之于 CV 的长期复利效应。LLM serving 是 AI 基础设施的刚需环节，工作负载理解直接决定
    GPU 利用率、KV 缓存命中率与负载均衡效率，进而影响整个算力层的成本结构，因此研究价值向商业价值的传导路径清晰。但扣分项在于：这是单一平台（Chutes）的学术性发布，数据代表性存在偏差风险，尚无法确认其能否成为行业公认标准，且从学术贡献到可量化的商业壁垒之间存在较长验证周期，故落在'有潜力成为细分赛道基础设施'区间的上沿而非确定性基石级别。
value_capture_layer: hardware_compute
moat_impact: democratizes_access
key_beneficiaries:
- Chutes
- vLLM
- SGLang
- Together AI
- Fireworks AI
competitive_casualty:
- 依赖合成或采样工作负载做优化的 serving 初创公司
- 闭源 serving 基准测试服务
- 缺乏真实生产数据的专用推理优化厂商
market_opportunities:
- 基础设施团队可利用该一年期生产 trace 建立贴近真实负载的 serving 基准测试，针对性优化 KV-cache 策略与请求路由算法，直接降低单 token
  推理成本
- 对从事 LLM 网关与推理编排的创业者而言，trace 中长尾模型与用户-模型结构是设计多模型调度、缓存分层与计费策略的关键输入，可借此形成差异化竞争
- 研究者和工程师可基于该公开 trace 深耕 serving 可观测性与容量规划方向，沉淀可复用的分析方法论与开源基准工具
risk_matrix:
  regulatory: trace 数据若包含用户请求内容或可识别信息，可能面临 GDPR、个人信息保护法等数据隐私监管风险，需关注发布前的脱敏处理与授权声明
  technological: LLM serving 技术演进迅速（如 prefill/decode 分离、新注意力机制、推测解码），该 trace 反映的缓存与负载均衡模式可能随架构迭代而过时，结论外推需谨慎
  competitive: Chutes 为单一平台，其用户与模型分布存在平台偏差；若大型云厂商或主流模型提供商发布更大规模 trace，本数据集的基准价值可能被稀释
  ethical: 真实生产 trace 的发布可能暴露用户行为模式与模型使用偏好，存在隐私泄露与数据被滥用于竞争情报分析的风险，需评估匿名化程度
  additional:
  - 数据代表性风险：单一平台一年期 trace 难以覆盖推理需求的结构性突变（如新模型发布、价格调整引发的流量迁移），下游研究泛化时需注意
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: deep_dive
---

# Computer Science > Artificial Intelligence

# Title:A Year in LLM Serving: Workload Evolution, Caching and Load-Balancing

View PDFAbstract:Large Language Model (LLM) serving has become a critical cloud workload, and realistic traces are essential for motivating and benchmarking serving systems. However, existing LLM serving workload studies remain limited in scale and scope. They often observe short time periods and provide limited visibility into how users interact with models in production. As a result, they do not fully capture how LLM serving workloads evolve over time or how user-model interactions shape production traffic.

In this work, we further the understanding of real-world LLM serving workloads through both a global characterization and a longitudinal study of a one-year production trace from Chutes. Unlike prior studies, our trace captures full production behavior across many models and users, including both popular and long-tail models. We analyze the workload from aggregate, temporal, model-level, and user-level perspectives, revealing workload evolution and user-model structure that are typically hidden behind aggregate views. To support future research, we will release the full one-year trace with the paper, enabling downstream studies of production behavior without relying on sampled or synthetically generated workloads.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.