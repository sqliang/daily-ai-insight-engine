---
title: NVIDIA Nemotron 3.5 Lightning and NeMo Switchyard Deliver Faster, Smarter,
  More Efficient Agentic AI
source: https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/
author:
- '[[Kari Briski]]'
published: '2026-08-11'
created: '2026-08-13'
manifest_dates:
- '2026-08-13'
- '2026-08-14'
description: As AI shifts from chatbots to autonomous agents, open models are serving
  market demands for full control over where AI runs and how it’s deployed and evolves.
  Today, NVIDIA is expanding its Nemotron 3 model family with Nemotron 3.5 Lightning,
  the highest-efficiency model in its class for long-running agentic AI workloads.
  This release follows Nemotron [&#8230;]
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: a8ba0b0ace9187db
source_type: tech_blog
tldr: NVIDIA 发布 Nemotron 3.5 Lightning 开源模型与 NeMo Switchyard 开源路由库，面向长周期 Agentic AI
  工作负载，提升速度、效率与部署灵活性。
objective_summary: NVIDIA 扩展 Nemotron 3 模型家族，推出 300 亿参数混合专家（MoE）开源模型 Nemotron 3.5
  Lightning，专为长周期、高并发的 Agentic AI 任务设计，宣称输出速度最高提升 4 倍、Agent 任务完成速度提升 30%。同时，NVIDIA
  发布开源库 NeMo Switchyard，支持在主流 Agent 工具中按任务将请求智能路由到最合适的模型，无需重写应用。二者面向 PC、工作站、数据中心和云端，旨在让企业获得对
  AI 部署位置与运行效率的更大控制权。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - NVIDIA
  technologies:
  - Nemotron 3.5 Lightning
  - NeMo Switchyard
  - Nemotron 3
  - Nemotron 3 Nano
  - Nemotron 3 Ultra
  - NVIDIA NeMo
  - GPT-5.6
  - mixture-of-experts
  - agentic AI
  key_people: []
key_logic_flow:
- NVIDIA 扩展 Nemotron 3 模型家族，发布 Nemotron 3.5 Lightning，这是一款 300 亿参数的混合专家（MoE）开源模型。
- 该模型定位长周期 Agentic AI 中的高容量专业任务，输出速度最高快 4 倍，Agent 任务完成速度提升 30%。
- NVIDIA 同步开源 NeMo Switchyard 库，用于在主流 Agent 工具中根据任务智能路由到最合适的模型。
- NeMo Switchyard 支持混合使用开源、专有和 NVIDIA 模型，开发者无需重写应用即可接入。
- 企业可基于自身需求构建路由器，并在 PC、工作站、数据中心和云等多环境中部署。
- 大型 Agent 系统趋向多模型协作：前沿推理模型负责规划，Nemotron 3.5 Lightning 等专业模型执行具体任务。
object_mentions:
- object_type: model
  name: Nemotron 3.5 Lightning
  canonical_name: Nemotron 3.5 Lightning
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - NVIDIA 扩展 Nemotron 3 模型家族，推出 Nemotron 3.5 Lightning，这是一个 300 亿参数的混合专家模型，专为长周期
    Agentic AI 工作负载设计。
  - Nemotron 3.5 Lightning 的输出速度最高可快 4 倍，Agent 任务完成速度提升 30%，并可用 NVIDIA NeMo 在企业自有数据上进一步后训练。
  article_id: a8ba0b0ace9187db
- object_type: project
  name: NeMo Switchyard
  canonical_name: NeMo Switchyard
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - NVIDIA 同步发布 NeMo Switchyard，这是一个开源库，用于在常见 Agent 工具中根据企业需求将请求智能路由到最合适的模型。
  - Switchyard 支持跨开源、专有和 NVIDIA 模型的混合部署，开发者无需重写应用即可接入。
  article_id: a8ba0b0ace9187db
- object_type: model
  name: Nemotron 3 Nano
  canonical_name: Nemotron 3 Nano
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Nemotron 3.5 Lightning 的发布紧随 Nemotron 3 Nano 之后，体现 NVIDIA 持续改进开放模型的承诺。
  article_id: a8ba0b0ace9187db
- object_type: model
  name: Nemotron 3 Ultra
  canonical_name: Nemotron 3 Ultra
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 文章将 Nemotron 3 Ultra 与 GPT-5.6 并列为可规划和编排工作流的前沿推理模型。
  article_id: a8ba0b0ace9187db
- object_type: model
  name: GPT-5.6
  canonical_name: GPT-5.6
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章提到 GPT-5.6 可作为前沿推理模型，与 Nemotron 3 Ultra 一起负责 Agent 工作流的规划与编排。
  article_id: a8ba0b0ace9187db
- object_type: product
  name: NVIDIA NeMo
  canonical_name: NVIDIA NeMo
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Nemotron 3.5 Lightning 可通过 NVIDIA NeMo 在企业自有领域数据、工具和工作流上进行后训练，以提升专业任务准确率。
  article_id: a8ba0b0ace9187db
extract_result: success
impact_score:
  score: 6.8
  reason: NVIDIA 发布 30B 参数 MoE 开源模型 Nemotron 3.5 Lightning，并配套 NeMo Switchyard 模型路由基础设施，直接切入长周期
    Agentic AI 的企业本地/混合部署市场，可能重塑企业在多模型协作中的选型与部署策略；不过 4x/30% 等性能倍数属于 PR 宣称，尚缺独立第三方验证，未达到
    ChatGPT 发布或 Transformer 论文级别的范式转移。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 开源 MoE 模型的真实推理效率、4x/30% 性能宣称的可复现性，以及 NeMo Switchyard 与现有 Agent 框架的集成成本
hype_assessment:
  level: medium
  reason: 原文使用 "highest-efficiency"、"smarter and more efficient"、"greater control"
    等 PR 强化词，并抛出 4x 输出速度、30% Agent 任务提速等量化宣称，但 excerpt 中未提供详细基准或消融实验；好在整体是具体产品发布（30B
    MoE、开源库、多环境部署），并非空洞的 AGI 概念炒作，因此水分评估为中等。
information_entropy: medium
domain_disruption:
  technical_innovation: 面向长周期 Agentic AI 的 30B 参数 MoE 开源模型，配合 NeMo Switchyard 实现跨开源、专有与
    NVIDIA 模型的任务级智能路由，支持"前沿推理模型负责规划、专业模型负责执行"的多模型协作架构。
  business_model: 强化 NVIDIA 在企业 AI 软件栈的地位，通过开源模型 + 路由工具降低企业封闭式 API 依赖，并在 PC、工作站、数据中心、云等多环境推动
    NVIDIA 硬件及 NeMo 平台的采用，形成"开源模型引流、硬件与平台变现"的闭环。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: 1) Agentic AI 正从单次对话转向长周期、高并发的多模型系统，对高性价比专用模型和智能路由产生结构性需求；2) NVIDIA 将 Nemotron
    3.5 Lightning 与 NeMo Switchyard 开源，降低企业试用门槛，实质是把模型与路由层作为 CUDA/NeMo/NIM 生态的“引流品”；3)
    若 4x 速度与 30% 任务完成加速的 benchmark 在真实工作负载中被验证，将直接拉动 RTX、DGX 及云端 NVIDIA GPU 实例的推理需求，并推动
    NeMo 微调和 NIM 推理服务采用；4) Switchyard 支持在开源/专有/NVIDIA 模型间灵活路由，表面是中间件创新，实则加深 NVIDIA
    作为 AI 部署“控制平面”的锁定；5) 长期复利来自 agent 数量增长带来的推理量指数级上升，以及企业围绕 NVIDIA 全栈构建工作流后的迁移成本；6)
    风险包括性能承诺待第三方验证、开源模型生态能否持续跟上 Llama/Mistral、路由库可能被 LangChain/LlamaIndex 等框架快速吸收，以及垂直整合面临的监管审视。综上
    7.5/10：大概率成为 agentic AI 基础设施的重要一环，但尚需市场采纳与生态健康度的持续验证。
value_capture_layer: hardware_compute
moat_impact: strengthens_monopoly
key_beneficiaries:
- NVIDIA
- NVIDIA NeMo
- NVIDIA NIM
- 搭载 NVIDIA GPU 的云服务商 (AWS/Azure/GCP)
competitive_casualty:
- OpenAI
- Anthropic
- Cohere
- AI21 Labs
- AMD
- Intel
- 独立模型路由/Agent 编排初创公司
market_opportunities:
- 企业可基于 Nemotron 3.5 Lightning 的开源 MoE 架构，针对代码审查、安全告警、客服等垂直场景做领域微调，打造私有化部署的高效 Agent
  工作节点。
- 模型路由与编排工具迎来落地窗口，创业者可在 NeMo Switchyard 之外提供跨厂商、带可观测性与成本优化的第三方路由器或 Agent 中间件。
- 基础设施服务商可围绕 NVIDIA 软硬件栈构建“本地工作站+云端”混合 Agent 部署方案，满足企业对数据主权和低延迟的并行需求。
risk_matrix:
  regulatory: NVIDIA 开源模型可能受美国 AI 模型出口管制及芯片禁运政策影响，企业用户在欧盟部署高自主性 Agent 时需关注《AI 法案》高风险系统合规要求。
  technological: MoE 架构对推理框架和显存优化要求较高，4 倍速度与 30% 任务完成提升等宣称需独立基准验证，且存在被后续更大模型或新架构快速迭代覆盖的风险。
  competitive: Meta Llama、Google Gemma 及 OpenAI 等厂商持续加码开源/闭源 Agent 模型，NVIDIA 软硬件捆绑策略可能加剧生态锁定并引发反垄断审查。
  ethical: 长周期自主 Agent 的大规模应用可能放大错误决策、安全漏洞与偏见歧视风险，同时“永远在线”的智能体或对客服、运维等岗位带来就业冲击。
  additional:
  - NVIDIA 生态锁定风险
  - PR 声明中的性能数据可能存在营销夸大
  - 多模型路由的透明度与可解释性不足
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: monitor
object_insights:
- object_type: project
  name: NeMo Switchyard
  canonical_name: NeMo Switchyard
  url: null
  positioning: NVIDIA 开源的智能路由库，面向主流 Agent 工具，支持企业按任务将请求路由到最合适的模型。
  technical_signal: 开源库支持跨开源、专有和 NVIDIA 模型混合部署，开发者无需重写应用即可接入多模型协作架构。
  adoption_signal: 面向 PC、工作站、数据中心和云等多环境部署，企业可基于自身需求构建自定义路由器。
  ecosystem_relevance: 作为多模型 Agent 系统的基础设施组件，Switchyard 可将前沿推理模型与 Nemotron 等专业模型衔接成协作流水线。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: NeMo Switchyard 直接切中企业在多模型 Agent 部署中的路由与编排痛点，其开源策略有助于降低 vendor lock-in
    风险并吸引社区共建，一旦形成生态标准，有望成为 Agentic AI 时代连接推理模型与专业执行模型的关键基础设施。
  risk_notes:
  - 实际落地效果取决于企业模型组合的复杂度、集成成本以及与现有 Agent 工具的兼容程度。
  - 路由决策质量将直接影响下游 Agent 任务的准确性、整体响应延迟以及多模型协同的稳定性。
  score: 8.0
  article_ids:
  - a8ba0b0ace9187db
  evidence_snippets:
  - NVIDIA 同步发布 NeMo Switchyard，这是一个开源库，用于在常见 Agent 工具中根据企业需求将请求智能路由到最合适的模型。
  - Switchyard 支持跨开源、专有和 NVIDIA 模型的混合部署，开发者无需重写应用即可接入。
- object_type: product
  name: NVIDIA NeMo
  canonical_name: NVIDIA NeMo
  url: null
  positioning: NVIDIA 的模型定制与企业级训练平台，用于在自有领域数据、工具和工作流上对 Nemotron 等模型进行后训练。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 希望在自有领域数据、工具和工作流上后训练模型的企业与 AI 团队
  product_signal: 支持对 Nemotron 3.5 Lightning 等开源模型进行后训练，以提升专业任务的准确率。
  market_signal: 面向企业私有化部署与垂直领域定制需求，是 NVIDIA 端云一体 Agentic AI 战略的重要组成部分。
  differentiation: 与 Nemotron 模型家族深度集成，为企业提供从基础模型到领域适配的一站式开源定制能力。
  watch_reason: NVIDIA NeMo 是 Nemotron 开源模型商业化的关键承载平台，企业私有化后训练需求旺盛，其能力与 Switchyard、Lightning
    的协同将决定 NVIDIA 在 Agentic AI 工具链中的话语权。
  risk_notes:
  - 本次文章仅简要提及 NeMo 的后训练能力，缺少定价、版本更新与生态规模等具体信息。
  - 作为已有产品，需关注其与 Nemotron 3.5 Lightning 的集成深度是否形成显著竞争优势。
  score: 6.0
  article_ids:
  - a8ba0b0ace9187db
  evidence_snippets:
  - Nemotron 3.5 Lightning 可通过 NVIDIA NeMo 在企业自有领域数据、工具和工作流上进行后训练，以提升专业任务准确率。
---

As AI shifts from chatbots to autonomous agents, open models are serving market demands for full control over where AI runs and how it’s deployed and evolves.

Today, NVIDIA is expanding its Nemotron 3 model family with Nemotron 3.5 Lightning, the highest-efficiency model in its class for long-running agentic AI workloads. This release follows Nemotron 3 Nano and reflects NVIDIA’s commitment to continually improving open models for greater accuracy and speed.

Built for specialized tasks within larger multi-agent systems, Nemotron 3.5 Lightning, a 30-billion-parameter mixture-of-experts model, helps create smarter and more efficient agentic applications.

Also, NVIDIA is releasing NeMo Switchyard, an open source library for smart routing inside popular agent tools. Enterprises can use it to build a router based on their specific needs. When deployed, NeMo Switchyard can intelligently direct each request to the most capable and suitable model for the job, across developers’ own mix of open, proprietary and NVIDIA models, without requiring developers to rewrite their applications.

Together, Nemotron 3.5 Lightning and NeMo Switchyard deliver greater control over how AI is deployed, where it runs and how efficiently it operates — across PCs, workstations, data centers and the cloud.

**Always-On Agents Need a System of Models **

Modern agentic systems — always-on agents — increasingly operate as systems of models, or model ensembles, with different models specialized for different tasks.

NVIDIA Nemotron open models are designed for this architecture. A frontier reasoning model such as Nemotron 3 Ultra or GPT-5.6 may plan and orchestrate a workflow, while smaller specialized models like Nemotron 3.5 Lightning can perform targeted tasks such as code review, tool use, security alert monitoring and answering billing questions.

**Powering High-Volume Specialized Tasks With Nemotron 3.5 Lightning**

NVIDIA Nemotron 3.5 Lightning is a fully customizable open model built for high-volume tasks powering always-on agents. It was developed with contributions from the Nemotron Coalition, whose members provided evaluation methodologies, inference software and datasets to help advance the model.

The model delivers up to 4x faster output speed, leading to 30% faster agentic task completion compared with other models in its class. And because it’s open and customizable, Nemotron 3.5 Lightning can be easily post-trained with NVIDIA NeMo on an organization’s own domain data, tools and workflows to improve accuracy for specialized tasks.