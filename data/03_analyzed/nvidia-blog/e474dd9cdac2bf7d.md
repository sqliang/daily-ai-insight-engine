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
impact_score:
  score: 7.8
  reason: NVIDIA发布NemoClaw开放蓝图并非单纯的技术公告，而是一个正在被Cadence、Dassault、Siemens、Synopsys、Ansys五大工业软件巨头同时采用的行业级方案。RTL验证从数周缩短到数小时的量化结果表明这不是概念验证，而是有明确ROI的落地案例。这标志着AI代理从通用聊天场景正式进入高门槛的CAE/EDA工业工程领域，对半导体、航空、汽车、制造等垂直行业的自动化进程有实质性推动。虽然不是ChatGPT级别的范式转移，但在工业工程AI自动化这一垂直赛道上具有转折点意义。评分：7.8
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: OpenShell安全运行时如何治理工业级AI代理的文件/网络/工具访问权限
hype_assessment:
  level: low
  reason: 文章没有使用'颠覆'、'革命性'等PR套话，而是提供了具体的技术架构说明（OpenShell运行时、OpenClaw/Hermes编排框架、模型路由器、NeMo定制库）、多条部署路径（DGX
    Spark/数据中心/云）、以及五大工业软件厂商的明确落地案例和量化效果（RTL验证从数周到数小时）。这些可验证的具体细节表明干货含量高，不存在概念炒作。判定：low
information_entropy: high
domain_disruption:
  technical_innovation: NemoClaw的核心创新在于为工业工程领域提供了'安全优先的AI代理运行时'（OpenShell），通过策略引擎逐层管控代理对文件系统、网络和工具的访问权限，解决了企业最关心的安全治理问题。同时通过模型路由器支持多种前沿模型、并提供NeMo库实现领域定制化，使得CAE/EDA这类高专业度的工程软件能够被AI代理安全地编排和调用。
  business_model: 工业软件正从'工具授权许可'向'AI代理即服务'模式演进。Dassault Systèmes产品化3DEXPERIENCE Agentic
    Platform是典型信号——未来工程软件的价值可能不再仅由软件功能决定，而是由AI代理对复杂工作流的自主编排能力决定。这对西门子、达索、Cadence等传统工业软件巨头的商业模式有重塑效应，也可能催生一批垂直领域的AI工程代理SaaS服务。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: NemoClaw 作为开放蓝图，定位在工业工程领域自主 AI 代理的安全运行时和编排层。长期复利逻辑如下：(1) 工业软件生态具有极高的迁移成本，一旦
    Cadence、Siemens、Dassault 等巨头将核心工作流（RTL 验证、3D 仿真、EDA 设计）构建在 NemoClaw 之上，NVIDIA
    将获得持久的分成和锁定效应，这一层不是简单的 API 调用而是深度集成的运行依赖；(2) 安全运行时 OpenShell 解决了企业采用 AI 代理的关键障碍——文件/网络/工具访问的策略管控，这是从概念验证到生产部署的必过关卡；(3)
    NVIDIA 通过 DGX Spark（个人 AI 超算）+ NeMo（模型定制）+ NemoClaw（代理运行时）构建了从硬件到模型到代理的完整飞轮，三条护城河叠加形成复合壁垒；(4)
    开放蓝图策略降低了 ISV 的绑定顾虑，有助于快速铺开生态。风险在于：开放模式可能导致碎片化，工业软件巨头长期可能自建运行时层。综合判断具备极强的细分赛道基础设施潜力，但发布时间尚短，需观察
    6-12 个月后的实际生产部署渗透率再确认复利效应强度。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- NVIDIA
- Cadence
- Siemens
- Dassault Systèmes
- Synopsys
competitive_casualty:
- 传统 CAE/EDA 脚本自动化工具
- 非 NVIDIA 生态的通用 Agent 编排框架
- 小型工业 AI 工程初创公司
market_opportunities:
- 工业软件厂商可基于NemoClaw快速构建行业专属AI工程助手（如EDA设计、CAE仿真、PCB布局等垂直场景），将核心工具链升级为自主代理平台，显著缩短工程周期并形成差异化竞争力
- 围绕OpenShell安全运行时为企业提供合规审计、策略定制与部署咨询服务——受监管行业（航空航天、汽车、半导体）对AI代理的文件/网络/工具访问管控有刚性需求，这是一块高附加值服务市场
- 中小型CAE/EDA工具商可基于NemoClaw开放蓝图为自有工具链快速补足多工具编排和AI代理能力，避免在Cadence/Synopsys/Siemens等巨头主导的AI代理生态中被边缘化
risk_matrix:
  regulatory: NVIDIA GPU出口管制可能限制NemoClaw在中国等市场的工业软件客户采用，受制裁实体需评估合规替代方案；此外AI代理自动生成的工程设计方案可能引发知识产权归属与责任界定问题
  technological: 当前NemoClaw高度依赖NVIDIA GPU生态（DGX Spark等），若竞争对手推出非NVIDIA绑定的开源替代框架或Llama等开源模型在工程领域追平性能，可能削弱其技术护城河
  competitive: Synopsys（含Ansys）、Cadence、Siemens三家巨头已率先卡位，中小工具商面临生态挤压与人才争夺压力；同时Meta、Google等也在推通用AI代理框架，可能分流社区关注度
  ethical: 自主AI工程师可能替代大量传统CAE/EDA工程设计与验证岗位，引发就业冲击与技能重塑压力；AI自动生成的RTL代码和仿真结果若出错的追责归属尚不明确
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: strategic_invest
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