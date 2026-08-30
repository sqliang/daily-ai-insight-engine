---
title: SAREF-based Ontology for Distributed AI Workflows across the Edge-Fog-Cloud
  Continuum
source: https://arxiv.org/abs/2608.26160
author:
- '[[Viorica Rozina Chifu, Tudor Cioara, Vasile Ofrim, Liana Toderean, Ionut Anghel,
  Laura Daniele, Cornelis Bouter]]'
published: '2026-08-28'
created: '2026-08-28'
manifest_dates:
- '2026-08-28'
description: 'arXiv:2608.26160v1 Announce Type: new Abstract: Nowadays semantic models
  provide limited support for representing distributed AI workflows and their execution
  across heterogeneous edge, fog, and cloud environments. Therefore, AI processes
  and resources are often described using incompatible semantic representations, affecting
  the interoperability, orchestration, and reuse. To address these challenges, this
  paper proposes a SAREF-compliant ontology for representing distributed AI workflows
  across the edge-fog-cloud continuum. We extend the SAREF4SYST ontology with concepts
  for modeling AI pipelines, executable AI jobs, computational resources, deployment
  constraints, and communication relationships, providing a unified semantic model
  of both AI workflows and heterogeneous computing infrastructures. The ontology enables
  semantic interoperability, automated reasoning, and resource-aware orchestration
  of distributed AI applications while remaining fully aligned with the ETSI SAREF
  ecosystem. The ontology is evaluated using proof-of-concept smart grid energy services
  orchestration scenarios and validated using competency questions showing its ability
  to support AI workflow deployment, execution reasoning, and workload adaptation
  across heterogeneous edge, fog, and cloud environments. All competency questions
  were successfully validated using SPARQL querying and semantic reasoning. Experimental
  results demonstrate deployment success rates of 90-100% with average orchestration
  decision times below 80 ms across heterogeneous edge-fog-cloud environments, highlighting
  its effectiveness on ensuring semantic interoperability for distributed AI orchestration.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 53e4ec1cfa13a4ec
source_type: academic_paper
tldr: 论文提出一个符合ETSI SAREF标准的本体，用于跨边缘-雾-云连续体表示分布式AI工作流，扩展SAREF4SYST建模AI流水线、可执行作业与计算资源。实验显示部署成功率达90%至100%，平均编排决策时间低于80毫秒。
objective_summary: 该arXiv论文针对现有语义模型难以表示分布式AI工作流及其在异构边缘、雾和云环境中执行的问题，提出一个符合SAREF标准的本体。该本体扩展SAREF4SYST，引入AI流水线、可执行AI作业、计算资源、部署约束和通信关系的建模概念，实现AI工作流与异构基础设施的统一语义描述。研究团队用智能电网能源服务编排场景进行概念验证，通过SPARQL查询和语义推理成功验证全部能力问题。实验表明部署成功率达90%至100%，平均编排决策时间低于80毫秒。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - ETSI
  technologies:
  - SAREF
  - SAREF4SYST
  - SPARQL
  - Edge-Fog-Cloud
  key_people: []
key_logic_flow:
- 论文指出现有语义模型对分布式AI工作流及其在异构边缘、雾和云环境中的执行支持有限，导致AI流程与资源常用不兼容的语义表示，影响互操作性、编排与复用。
- 论文提出一个符合SAREF标准的本体，用于表示跨边缘-雾-云连续体的分布式AI工作流，并与ETSI SAREF生态系统完全对齐。
- 该本体在SAREF4SYST基础上扩展了AI流水线、可执行AI作业、计算资源、部署约束与通信关系的概念，提供AI工作流与异构计算基础设施的统一语义模型。
- 该本体支持语义互操作、自动推理与资源感知的编排，研究团队通过智能电网能源服务编排场景进行概念验证。
- 研究团队使用能力问题并通过SPARQL查询与语义推理完成验证，所有能力问题均成功通过。
- 实验结果显示部署成功率达90%至100%，平均编排决策时间低于80毫秒，证明其对分布式AI编排语义互操作的有效性。
object_mentions:
- object_type: paper
  name: SAREF-based Ontology for Distributed AI Workflows across the Edge-Fog-Cloud
    Continuum
  canonical_name: SAREF Ontology for Distributed AI Workflows
  url: https://arxiv.org/abs/2608.26160
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文提出一个符合ETSI SAREF标准的本体，用于表示跨边缘-雾-云连续体的分布式AI工作流，以解决语义互操作与编排问题。
  - 实验结果显示该本体在异构边缘-雾-云环境中部署成功率达90%至100%，平均编排决策时间低于80毫秒。
  article_id: 53e4ec1cfa13a4ec
- object_type: project
  name: SAREF4SYST
  canonical_name: SAREF4SYST
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 论文在SAREF4SYST本体基础上扩展建模AI流水线、可执行AI作业、计算资源、部署约束与通信关系的概念，形成统一语义模型。
  article_id: 53e4ec1cfa13a4ec
- object_type: project
  name: ETSI SAREF
  canonical_name: SAREF
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 该本体完全对齐ETSI SAREF生态体系，通过SPARQL查询与语义推理成功验证了全部能力问题。
  article_id: 53e4ec1cfa13a4ec
extract_result: success
impact_score:
  score: 2.5
  reason: 该论文提出面向边缘-雾-云连续体的 SAREF 兼容本体，属于语义互操作与 AI 编排交叉领域的增量学术贡献。虽然为分布式 AI 工作流提供了与
    ETSI 标准对齐的统一语义建模方案，但本体技术行业落地周期长、实际采用高度依赖标准生态的推广力度，且现有编排格局已被 Kubernetes 系工具主导，语义本体短期内难以形成替代性冲击。实验仅覆盖智能电网单一概念验证场景，部署成功率与决策时延指标也缺乏与主流编排框架的横向对比，短期行业影响力有限。基于以上分析，给出
    2.5 分。
sentiment: neutral
developer_sentiment:
  tone: skeptical
  primary_focus: 本体驱动的语义编排相比 Kubernetes/KubeEdge 等既有方案的真实增益与迁移落地成本
hype_assessment:
  level: low
  reason: 全文采用克制的学术表述，未出现'颠覆''革命性'等 PR 滥用词汇；所有关键声明（部署成功率 90-100%、平均编排决策时间低于 80ms）均有概念验证实验数据支撑，并采用能力问题、SPARQL
    查询与语义推理完成系统性验证，属于实打实的学术干货，不存在概念包装。
information_entropy: high
domain_disruption:
  technical_innovation: 在 SAREF4SYST 基础上扩展出 AI 流水线、可执行 AI 作业、计算资源、部署约束与通信关系等建模原语，将
    AI 工作流与异构边缘-雾-云基础设施收敛到统一语义模型，使部署位置选择、执行条件等编排决策可从语义推理中自动推导，实现资源感知的自动化编排，属于工程标准化层面的扎实增量创新。
  business_model: 通过与 ETSI SAREF 标准生态对齐，为跨厂商、跨云边端的 AI 编排互操作提供标准化语义底座，有潜力降低多供应商环境下的平台锁定效应，催生基于语义互操作的编排中间件市场；但本体商业化路径漫长，短期内更多体现为学术与标准组织层面的影响力。
engineering_complexity: prototype
compound_value:
  score: 4.0
  reason: 该本体若被 ETSI SAREF 生态正式采纳，有潜力成为边缘-雾-云连续体上分布式 AI 编排的语义互操作基础设施，具备长期复利效应——语义标准一旦沉淀为行业事实标准，其网络效应和切换成本会随时间累积。但当前仅为概念验证（theoretical_claim），智能电网
    PoC、90%-100% 部署成功率与 80ms 编排时延均为实验室环境数据，从学术论文到 ETSI 标准采纳再到产业规模化落地的路径漫长且不确定性高；开放标准本身的商业变现主体不明确，价值捕获取决于整个
    SAREF 生态的采纳速度。VC 视角下应将其视为'跟踪标的'而非'当期回报标的'，关键验证节点是是否进入 ETSI 标准化流程以及头部云厂商/能源企业是否将其纳入产品路线图，故落在'有潜力成为细分赛道基础设施但需持续验证'区间下沿，给
    4 分。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- ETSI
- Siemens
- Schneider Electric
- Eclipse EdgeX Foundry
competitive_casualty:
- 依赖厂商锁定的闭源 IoT 编排平台
- 传统能源管理系统(EMS/SCADA)厂商
market_opportunities:
- 面向智慧电网、智慧楼宇等 ETSI SAREF 生态的垂直行业，可基于该本体开发 AI 工作流语义编排中间件，以统一语义层连接异构边缘、雾、云设备并实现商业化交付
- 建议关注边缘 AI 与语义互操作交叉方向的创业机会，将此类本体能力封装为云原生生态（如 KubeEdge、K3s）的适配插件，降低异构环境编排的集成门槛
- 对物联网标准化与边缘计算领域的咨询从业者，可深入研究 SAREF4SYST 扩展方法论，将其语义建模思路迁移至智慧城市、工业物联网等相邻垂直领域
risk_matrix:
  regulatory: 本体遵循 ETSI SAREF 标准，落地欧盟智慧电网等关键基础设施场景时需关注《人工智能法案》(AI Act) 对关键基础设施 AI
    系统的合规要求，以及数据驻留与网络安全相关法规
  technological: 语义本体/知识图谱路线面临被 Kubernetes 云原生生态及基于大模型的动态服务发现方案替代的风险；论文目前仅为理论声明与单一场景概念验证，跨域泛化能力存疑
  competitive: 云厂商（AWS IoT、Azure IoT、Google）与开源编排社区已主导边缘编排格局，标准化本体作为后来者面临生态挤压；若缺乏主流编排框架适配，存在被边缘化的风险
  ethical: 该本体用于智慧电网等关键基础设施的 AI 编排，推理或编排决策出错可能危及能源供应的安全性与可靠性；分布式场景下数据处理还涉及用户用电数据的隐私保护问题
  additional:
  - 实验仅在单一智能电网场景验证，场景与样本多样性不足，宣称的 90%-100% 部署成功率外推价值有限
confidence:
  impact: medium
  compound: low
  hype: high
actionable_insight: monitor
object_insights:
- object_type: project
  name: SAREF4SYST
  canonical_name: SAREF4SYST
  url: null
  positioning: SAREF4SYST是ETSI SAREF生态中面向系统建模的标准本体扩展，为智能系统与设备提供基础语义描述能力，是本文分布式AI工作流本体的扩展基座。
  technical_signal: 该本体扩展SAREF4SYST，引入AI流水线、可执行作业、计算资源与部署约束等概念，实现AI工作流与异构基础设施的统一语义建模。
  adoption_signal: 论文以智能电网能源服务编排为概念验证场景，全部能力问题通过SPARQL查询与语义推理验证，部署成功率达90%至100%。
  ecosystem_relevance: SAREF4SYST隶属ETSI SAREF标准生态，本文方案与其完全对齐，延续了SAREF在物联网语义互操作领域的标准影响力。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: SAREF4SYST作为ETSI标准本体系列的组成部分，正被用于扩展分布式AI工作流语义建模，实验展现出90%至100%的部署成功率和低于80毫秒的编排决策时间。若该方向持续演进，有望推动AI编排走向标准化语义互操作，值得跟踪其行业采纳与标准演进。
  risk_notes:
  - 论文仅以智能电网单一场景验证本体能力，结论对更多行业的泛化性尚待检验。
  - SAREF4SYST作为引用基础本体，本文扩展停留在学术概念验证，尚未形成正式标准或得到广泛行业部署。
  - 实验数据来自概念验证环境，大规模异构边缘-雾-云生产环境的可靠性仍需更多实证。
  score: 5.0
  article_ids:
  - 53e4ec1cfa13a4ec
  evidence_snippets:
  - 论文在SAREF4SYST本体基础上扩展建模AI流水线、可执行AI作业、计算资源、部署约束与通信关系的概念，形成统一语义模型。
---

# Computer Science > Artificial Intelligence

# Title:SAREF-based Ontology for Distributed AI Workflows across the Edge-Fog-Cloud Continuum

View PDFAbstract:Nowadays semantic models provide limited support for representing distributed AI workflows and their execution across heterogeneous edge, fog, and cloud environments. Therefore, AI processes and resources are often described using incompatible semantic representations, affecting the interoperability, orchestration, and reuse. To address these challenges, this paper proposes a SAREF-compliant ontology for representing distributed AI workflows across the edge-fog-cloud continuum. We extend the SAREF4SYST ontology with concepts for modeling AI pipelines, executable AI jobs, computational resources, deployment constraints, and communication relationships, providing a unified semantic model of both AI workflows and heterogeneous computing infrastructures. The ontology enables semantic interoperability, automated reasoning, and resource-aware orchestration of distributed AI applications while remaining fully aligned with the ETSI SAREF ecosystem. The ontology is evaluated using proof-of-concept smart grid energy services orchestration scenarios and validated using competency questions showing its ability to support AI workflow deployment, execution reasoning, and workload adaptation across heterogeneous edge, fog, and cloud environments. All competency questions were successfully validated using SPARQL querying and semantic reasoning. Experimental results demonstrate deployment success rates of 90-100% with average orchestration decision times below 80 ms across heterogeneous edge-fog-cloud environments, highlighting its effectiveness on ensuring semantic interoperability for distributed AI orchestration.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.