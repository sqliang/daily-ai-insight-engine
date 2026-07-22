---
title: Industrial Software Leaders Build Secure, Autonomous AI Engineers With NVIDIA
  NemoClaw
source: https://blogs.nvidia.com/blog/industrial-software-leaders-secure-autonomous-ai-engineers-nemoclaw/
author:
- '[[Timothy Costa]]'
published: '2026-06-02'
created: '2026-06-04'
description: 'Accelerated computing has revolutionized industrial engineering, compressing
  simulation times from weeks to hours. Today’s remaining challenges sit in the end-to-end
  workflow surrounding the simulations: computer-aided design, meshing, simulation
  setup and debugging, as well as post-processing and generating summary reports of
  these processes. At GTC Taipei at COMPUTEX, NVIDIA and more than a dozen engineering
  software [&#8230;]'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: e474dd9cdac2bf7d
source_type: tech_blog
tldr: NVIDIA 在 GTC Taipei 上发布 NemoClaw 开放蓝图，联合 Cadence、Dassault Systèmes、Siemens、Synopsys
  等十余家工业软件厂商，基于安全运行时 OpenShell 构建自主 AI 工程师，将 RTL 验证等工程流程从数周压缩至数小时。
objective_summary: NVIDIA 在 GTC Taipei 上发布 NemoClaw 开放蓝图，该蓝图用于构建专业化、长运行的自主 AI 工程师代理，配备了多种编排框架集成选项、模型路由器和
  NVIDIA NeMo 定制库，其核心采用开源运行时 OpenShell 在每一层执行基于策略的安全控制。Cadence 基于 NemoClaw 构建自主 RTL
  工程师，将验证时间从数周降至数小时。Dassault Systèmes 正在将 3DEXPERIENCE Agentic Platform 产品化，Siemens
  将 NemoClaw 集成到 Fuse EDA AI Agent 中，Synopsys 也在 Ansys Icepak 等产品中应用该技术。
event_type: framework_tools
epistemic_status: pr_statement
entities:
  companies:
  - NVIDIA
  - Cadence
  - Dassault Systèmes
  - Siemens
  - Synopsys
  - Ansys
  technologies:
  - NemoClaw
  - OpenShell
  - OpenClaw
  - Hermes
  - NeMo
  - RTL
  - CAE
  - EDA
  - DGX Spark
  key_people: []
key_logic_flow:
- NVIDIA 在 GTC Taipei 上发布 NemoClaw 开放蓝图，该蓝图用于构建专业化、长运行的自主 AI 工程师代理。
- NemoClaw 包含多种编排框架集成选项（如 OpenClaw 和 Hermes）、模型路由器和 NVIDIA NeMo 定制库，支持从 DGX Spark
  到企业数据中心和云服务等多种部署方式。
- NemoClaw 核心采用开源运行时 OpenShell，在每一层执行基于策略的安全控制，管理代理对文件、网络和工具的访问。
- Cadence 基于 NemoClaw 构建自主 RTL 工程师，通过编排 ChipStack 将 RTL 验证时间从数周缩短至数小时。
- Dassault Systèmes 正在将 3DEXPERIENCE Agentic Platform 产品化，在 NemoClaw 和 OpenShell 的安全环境中运行设计、仿真和制造相关的自主代理。
- Siemens 和 Synopsys 分别将 NemoClaw 集成到 Fuse EDA AI Agent 和 Ansys Icepak 中，覆盖半导体设计、3D
  IC 和 PCB 系统设计等工作流程。
extract_result: success
object_mentions:
- object_type: product
  name: NVIDIA NemoClaw
  canonical_name: NVIDIA NemoClaw
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - NemoClaw 是 NVIDIA 在 GTC Taipei 上发布的开放蓝图，用于构建专业化、长运行的自主 AI 工程师代理，包含多种编排框架集成选项、模型路由器和
    NVIDIA NeMo 定制库。
  - NemoClaw 支持从 NVIDIA DGX Spark 个人 AI 超级计算机到企业数据中心和云服务提供商的多种部署方式。
  article_id: e474dd9cdac2bf7d
- object_type: project
  name: NVIDIA OpenShell
  canonical_name: NVIDIA OpenShell
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - OpenShell 是 NemoClaw 核心的开源运行时，负责在每一层执行基于策略的安全控制，管理代理对文件、网络和工具的访问权限。
  article_id: e474dd9cdac2bf7d
- object_type: product
  name: Cadence ChipStack
  canonical_name: Cadence ChipStack
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Cadence 正在基于 NemoClaw 构建自主 RTL 工程师，该工程师编排 Cadence ChipStack 进行设计和验证，将 RTL 验证时间从数周缩短至数小时。
  article_id: e474dd9cdac2bf7d
- object_type: product
  name: 3DEXPERIENCE Agentic Platform
  canonical_name: 3DEXPERIENCE Agentic Platform
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Dassault Systèmes 正在将 3DEXPERIENCE Agentic Platform 产品化，以运行设计、仿真和制造相关的长运行自主代理，该平台由
    NVIDIA NemoClaw 和 OpenShell 提供安全环境支撑。
  article_id: e474dd9cdac2bf7d
- object_type: product
  name: Fuse EDA AI Agent
  canonical_name: Fuse EDA AI Agent
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Siemens 正在将 NVIDIA NemoClaw 和 OpenShell 集成到 Fuse EDA AI Agent 中，使其能够规划和编排跨半导体、3D
    IC 和 PCB 系统设计的多工具工作流。
  article_id: e474dd9cdac2bf7d
- object_type: product
  name: NVIDIA DGX Spark
  canonical_name: NVIDIA DGX Spark
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 用户可以通过 NVIDIA DGX Spark 个人 AI 超级计算机，以及企业数据中心和云服务提供商来部署和运行 NemoClaw 自主 AI 工程师代理。
  article_id: e474dd9cdac2bf7d
- object_type: product
  name: Ansys Icepak
  canonical_name: Ansys Icepak
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Ansys Icepak 作为 Synopsys 产品组合的一部分，正在 COMPUTEX 展会上演示，被用于 NemoClaw 自主 AI 工程师中进行网格划分、仿真和优化
    GPU 电子冷却设计。
  article_id: e474dd9cdac2bf7d
---

Accelerated computing has revolutionized industrial engineering, compressing simulation times from weeks to hours.

Today’s remaining challenges sit in the end-to-end workflow surrounding the simulations: computer-aided design, meshing, simulation setup and debugging, as well as post-processing and generating summary reports of these processes.

At GTC Taipei at COMPUTEX, NVIDIA and more than a dozen engineering software providers are showcasing how autonomous AI agents automate this entire workflow.

These AI engineers are based on NVIDIA NemoClaw, an open blueprint for building specialized, long-running agents with a secure runtime and frontier models.

NemoClaw includes a choice of harness — meaning it can be integrated with various orchestration frameworks enterprises use to deploy and coordinate agents, such as OpenClaw and Hermes — as well as a model router and NVIDIA NeMo libraries for customization.

Users can easily deploy NemoClaw from NVIDIA DGX Spark personal AI supercomputers, as well as through enterprise data centers and cloud service providers. NVIDIA OpenShell — the open source runtime at its core — governs how each agent accesses files, networks and tools, enforcing policy-based security at every layer.

**Industrial Engineering Leaders Build AI Agents Across Design, Engineering, Simulation**

Industrial software leaders are building AI engineers for computer-aided engineering (CAE) and electronic design automation (EDA) use cases across automotive, aerospace, semiconductors and manufacturing.

Cadence is building an autonomous register-transfer level (RTL) engineer with NemoClaw that orchestrates Cadence Design Systems ChipStack for design and verification. The workflow was featured yesterday in a GTC Taipei keynote demo and is cutting time for RTL verification — a key step in digital circuit design — from weeks to hours.

Dassault Systèmes is actively productizing the 3DEXPERIENCE Agentic Platform to operate long-running and autonomous agents for design, simulation and manufacturing operations, in a secured environment powered by NVIDIA NemoClaw and OpenShell.

Siemens is integrating NVIDIA NemoClaw and OpenShell into Fuse EDA AI Agent, a purpose-built autonomous agent that plans and orchestrates domain-scoped multi-tool workflows across semiconductor, 3D integrated circuit and printed circuit board system design.

Synopsys is collaborating with NVIDIA to apply agents to end-to-end engineering workflows with NVIDIA NemoClaw. Ansys Icepak, part of the Synopsys portfolio, is being demoed on the COMPUTEX show floor this week, used within a NemoClaw-based autonomous AI engineer to mesh, simulate and optimize GPU electronics cooling designs.

*Image courtesy of Synopsys.*

**Startups Extend the Reach of Agentic AI**

In addition, cutting-edge startups are building AI engineers for their workflows — all using NVIDIA NemoClaw.