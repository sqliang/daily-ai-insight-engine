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
tldr: NVIDIA发布NemoClaw开放蓝图，助力工业软件巨头构建安全自主AI工程师
objective_summary: NVIDIA在GTC Taipei发布NemoClaw开放蓝图，用于构建工业工程领域的自主AI代理，包含安全运行时和前沿模型。Cadence、Dassault
  Systèmes、Siemens、Synopsys等工业软件厂商正基于该蓝图构建CAE/EDA领域的AI工程师，
event_type: framework_tools
epistemic_status: verified_fact
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
  - DGX Spark
  - CAE
  - EDA
  - RTL
  - ChipStack
  - 3DEXPERIENCE
  - Fuse EDA
  key_people: []
key_logic_flow:
- NVIDIA在GTC Taipei上发布NemoClaw开放蓝图，这是一个用于构建专业化、长时间运行AI代理的框架，包含安全运行时OpenShell和前沿模型支持。
- NemoClaw提供多种编排框架集成选项（OpenClaw和Hermes）、模型路由器以及NVIDIA NeMo库用于模型定制化。
- 用户可通过NVIDIA DGX Spark个人AI超级计算机、企业数据中心和云服务提供商部署NemoClaw。
- Cadence基于NemoClaw构建自主RTL工程师，协调Cadence ChipStack进行设计与验证，将RTL验证时间从数周缩短到数小时。
- Dassault Systèmes正将3DEXPERIENCE Agentic Platform产品化，基于NemoClaw和OpenShell运行自主设计、仿真和制造代理。
- Siemens将NemoClaw和OpenShell集成到Fuse EDA AI Agent中，用于半导体、3D集成电路和PCB系统设计的多工具工作流编排。
extract_result: success
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