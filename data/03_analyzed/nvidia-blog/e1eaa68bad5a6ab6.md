---
title: How NVIDIA’s Inference Software Stack Powers the Lowest Token Cost
source: https://blogs.nvidia.com/blog/inference-software-lowest-token-cost/
author:
- '[[Amr Elmeleegy]]'
published: '2026-06-30'
created: '2026-07-01'
description: 'As organizations move from AI pilots to production AI factories, infrastructure
  decisions have shifted from peak chip specifications to cost per token: how many
  useful tokens they can deliver per dollar, per watt and within required latency
  targets. Codesigned with NVIDIA GPUs, CPUs, networking and systems, and strengthened
  by a broad open source ecosystem, NVIDIA’s [&#8230;]'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: e1eaa68bad5a6ab6
manifest_dates:
- '2026-07-01'
- '2026-07-02'
- '2026-07-03'
source_type: tech_blog
tldr: NVIDIA 推理软件栈在 Blackwell 上将 DeepSeek V4 token 成本降低 5 倍
objective_summary: NVIDIA 官方博客介绍了其推理软件栈如何通过 TensorRT-LLM、Dynamo 等框架与 Blackwell GPU
  协同设计，在一月内将 DeepSeek V4 token 成本降低 5 倍。Baseten、Cognition、Deep Infra、Together AI
event_type: infrastructure_update
epistemic_status: pr_statement
entities:
  companies:
  - NVIDIA
  - Baseten
  - Cognition
  - Deep Infra
  - DigitalOcean
  - Hippocratic AI
  - Together AI
  - Cursor
  technologies:
  - TensorRT-LLM
  - NVIDIA Dynamo
  - Blackwell
  key_people: []
key_logic_flow:
- 企业 AI 基础设施决策标准已从芯片峰值规格转向每 token 成本（每美元、每瓦特可产出的有用 token 数量）。
- NVIDIA 推理软件栈与其 GPU、CPU、网络和系统协同设计，并依托开源生态持续提升硬件性能。
- 在 Blackwell 平台上，NVIDIA 的软件堆栈仅一个月就将 DeepSeek V4 模型的 token 成本降低了 5 倍。
- Baseten 使用 TensorRT-LLM 在 Blackwell GPU 上服务 DeepSeek V4 Pro，通过专有运行时优化实现每秒 token
  数提升高达 50%。
- Cognition 使用 NVIDIA Dynamo 推理框架管理推理 GPU，无需自建基础设施即可扩展强化学习工作负载。
- DigitalOcean 帮助 Hippocratic AI 在 Blackwell GPU 上使用 NVIDIA 推理软件，将医疗 AI 推理吞吐量提升 30%
  并保持亚秒级首次响应时间。
extract_result: success
impact_score:
  score: 6.5
  reason: NVIDIA 声称在 Blackwell 上一个月内将 DeepSeek V4 token 成本降低 5 倍，虽然来自官方 PR 存在宣传成分，但
    TensorRT-LLM 和 Dynamo 的全栈协同优化思路有真实技术支撑，且 Baseten、Together AI 等明确客户案例增加了可信度。这个事件反映了
    AI 基础设施竞争从芯片峰值算力向每 token 成本转移的趋势，对 AI 推理市场格局有重要影响，但并非范式级突破（本质是工程优化的延续而非理论创新）。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: TensorRT-LLM + Blackwell 组合能否在真实生产环境中兑现 5 倍成本降低
hype_assessment:
  level: medium
  reason: 文章来自 NVIDIA 官方博客，本质是 PR 性质的技术宣传。虽然引用了多个客户案例（Baseten、Cognition、DigitalOcean、Together
    AI）增加了可信度，但'5 倍降低'是端到端系统级优化在一月内的累计结果，未必代表每个用户都能复现，且未披露基准配置和测量方法。'每 token 成本'叙事有一定颠覆性包装成分，但底层技术（TensorRT-LLM、Dynamo
    框架）本身是成熟的工程产出，不是空洞炒作。
information_entropy: medium
domain_disruption:
  technical_innovation: NVIDIA 推理软件栈的核心创新在于 TensorRT-LLM 和 Dynamo 框架与 Blackwell GPU
    的协同设计（codesign），通过编译优化、KV cache 管理、动态批处理、GPU 编排等系统级手段而非单一算子加速来实现 token 成本降低。这种垂直整合的软硬件协同优化路径正在成为
    AI 推理基础设施的标准范式。
  business_model: 推动 AI 基础设施采购决策标准从'芯片峰值规格'转向'每美元/每瓦特产出 token 数'，这将重塑推理云服务商的定价策略和竞争维度。对中小型
    AI 公司而言，意味着可以依赖 NVIDIA 生态（如 Baseten、Together AI）获得与大厂相当的成本效率，无需自建推理基础设施。
engineering_complexity: production_ready
compound_value:
  score: 8.5
  reason: NVIDIA 推理软件栈（TensorRT-LLM + Dynamo + Blackwell 协同设计）展现出极强的复利效应，投资逻辑如下：第一，软件与硬件的正向飞轮——一个月内将
    DeepSeek V4 token 成本降低 5 倍，这意味着随着未来 Rubin 等新架构推出，每代硬件迭代都会叠加软件优化进一步放大优势，复利曲线陡峭；第二，客户锁定效应持续加深——Baseten、Together
    AI、Cognition、Deep Infra 等关键推理服务商直接在 NVIDIA 软件栈上构建业务，从框架依赖（TensorRT-LLM）到推理编排（Dynamo）形成双层绑定，迁移成本随时间递增；第三，开源策略反而强化护城河——TensorRT-LLM
    开源吸引社区贡献和生态采用，但核心优化与 NVIDIA 硬件深度耦合，社区贡献最终反哺 NVIDIA 平台而非削弱它；第四，Agentic AI 工作负载复杂性上升（多轮推理、子
    agent 编排、长上下文管理）使得软件栈对推理经济学的主导权越来越大，这让 NVIDIA 从硬件公司进化为'硬件+推理操作系统'的复合平台。3-5 年后，推理软件栈大概率仍是整个
    AI 基础设施中不可替代的基石。
value_capture_layer: hardware_compute
moat_impact: strengthens_monopoly
key_beneficiaries:
- NVIDIA
- Baseten
- Together AI
- Cognition
- Deep Infra
- DigitalOcean
competitive_casualty:
- AMD
- Intel
- Groq
- Cerebras
- d-Matrix
- 独立推理引擎创业公司
market_opportunities:
- 企业可将推理成本优化作为核心卖点，为垂直行业（医疗、编码、金融）提供基于 Blackwell + TensorRT-LLM 的专有推理加速服务，类似 Hippocratic
  AI 在医疗场景实现 30% 吞吐提升的路径
- 随着 agentic AI 多智能体协作架构的普及，NVIDIA Dynamo 类推理编排框架的二次开发与托管服务存在蓝海机会，帮助中小团队无需自建即可管理大规模推理
  GPU 集群
- 创业者可围绕 'token 成本计量与优化' 构建 SaaS 工具，为企业提供跨 GPU 平台的推理成本监控、对比分析和自动调优建议，成为 AI Factory
  时代的 FinOps 工具
risk_matrix:
  regulatory: Blackwell GPU 和 TensorRT-LLM 可能受美国对华出口管制影响，限制特定市场客户的使用；NVIDIA 软件栈的强绑定属性可能引发反垄断关注
  technological: 开源推理框架（vLLM、SGLang）和 AMD ROCm、Intel 等竞品正在快速追赶，若开放生态在 Blackwell 级别实现同等优化，NVIDIA
    软件护城河将被削弱
  competitive: AWS Trainium、Google TPU 等自研芯片配合自有软件栈正形成替代方案，大型云厂商可能通过垂直整合降低对 NVIDIA
    推理软件栈的依赖
  ethical: 低成本推理可能加速 AI 深度伪造、自动化编码 Agent 带来的就业冲击等负面应用扩散，医疗等敏感场景的推理错误责任归属问题尚不明确
  additional:
  - NVIDIA 博客为 PR 声明性质，5 倍成本降低是在特定模型（DeepSeek V4）和限定条件下取得，泛化能力需独立验证
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
---

As organizations move from AI pilots to production AI factories, infrastructure decisions have shifted from peak chip specifications to cost per token: how many useful tokens they can deliver per dollar, per watt and within required latency targets.

Codesigned with NVIDIA GPUs, CPUs, networking and systems, and strengthened by a broad open source ecosystem, NVIDIA’s full-stack inference software continuously improves hardware performance. On the NVIDIA Blackwell platform, the software stack has already reduced token costs by up to 5x on the DeepSeek V4 model in just one month.

Leading companies and inference providers are already seeing the compounding value of NVIDIA’s inference software stack on Blackwell:

- Baseten used the NVIDIA TensorRT-LLM open source library to serve DeepSeek V4 Pro on Blackwell GPUs for reasoning, coding and long-context workloads, applying proprietary runtime optimizations to deliver up to 50% more tokens per second.
- Cognition is using the NVIDIA Dynamo inference framework to manage inference GPUs, giving its team a ready-made path to scale reinforcement learning workloads without needing to build that infrastructure from scratch.
- Deep Infra uses the NVIDIA inference software stack to serve frontier open source models performantly on Blackwell from day zero, including DeepSeek V4.
- DigitalOcean helped Hippocratic AI use NVIDIA inference software on Blackwell GPUs to serve healthcare AI faster and more efficiently, increasing inference throughput by 30% while maintaining a sub-half-second time to first response across 10 million patient calls.
- Together AI used NVIDIA TensorRT-LLM on Blackwell to help Cursor accelerate the path from model optimizations to production endpoints for its real-time coding experience.

**Why Software Matters for Inference Economics**

Traditional web, search and software-as-a-service workloads were relatively predictable: A user might load a page, refresh a feed or update a business record. These requests typically followed similar software paths, reading from or writing to a database, and scaled by adding more of the same servers.

Agentic AI is different.

Agents can reason, plan, call tools, spin up specialist subagents and manage massive context across multi-turn workflows. They turn a single request into a distributed computing problem that can span hundreds of subagents, thousands of tasks and multiple large language models, running across GPUs, CPUs, DPUs and storage systems.

The software stack determines whether that complexity turns into wasted capacity or lower cost per token.

Lower cost per token comes from turning individual optimizations into system-level performance. NVIDIA’s inference software stack does this by connecting three layers: