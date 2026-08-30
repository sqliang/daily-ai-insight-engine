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