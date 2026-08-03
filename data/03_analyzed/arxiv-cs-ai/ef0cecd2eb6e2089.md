---
title: 'SonicSampler: Unified Tile-Aware Kernels for LLM Sampling and Speculative
  Verification'
source: https://arxiv.org/abs/2607.20475
author:
- '[[Pragaash Ponnusamy, Shivam Sahni, Jue Wang, Tri Dao]]'
published: '2026-07-24'
created: '2026-07-24'
manifest_dates:
- '2026-07-24'
description: 'arXiv:2607.20475v1 Announce Type: new Abstract: Sampling in LLM inference
  comprises a combinatorial set of logit processing, token selection, and verification
  operations for speculative decoding. However, existing implementations either accelerate
  only subsets of this pipeline, rely on multiple kernel launches, or assume homogeneous
  sampling behavior across a batch, limiting support for dynamic serving workloads
  and preventing efficient CUDA Graph execution. We present $\textbf{SonicSampler}$,
  a unified suite of tile-aware Triton kernels that vertically fuses the complete
  sampling pipeline into a fixed, workload-aware execution model. Our kernels support
  dynamic per-request sampling behaviors, including grammar-constrained decoding,
  repetition, frequency and presence penalties, logit bias, temperature scaling, top-$k$
  / top-$p$ / min-$p$ filtering, and speculative verification - within a single batched
  kernel while remaining fully CUDA Graph-compatible. Central to our approach is a
  novel hierarchical two-stage top-$k$ algorithm that achieves up to $\textbf{10x
  speedup}$ over competitive baselines and exploits the low-entropy structure of LLM
  outputs to enable efficient selection over large vocabularies. Across heterogeneous
  speculative decoding workloads, SonicSampler achieves up to $\textbf{16x speedup}$
  over state-of-the-art baselines while preserving flexible batched execution.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ef0cecd2eb6e2089
source_type: academic_paper
tldr: SonicSampler 提出了一套基于 Triton 的统一 tile 感知内核套件，将 LLM 推理的完整采样流水线垂直融合为单一负载感知执行模型，支持动态逐请求采样行为和推测解码验证，在异构推测解码工作负载上最高实现
  16 倍加速。
objective_summary: 该论文提出了 SonicSampler，一套基于 Triton 的统一 tile 感知内核套件，用于 LLM 推理中的采样操作。它将包括对数概率处理、令牌选择和推测解码验证在内的完整采样流水线垂直融合到单一批处理内核中，支持动态逐请求采样行为（包括语法约束解码、重复惩罚、温度缩放和
  top-k/top-p/min-p 过滤）。SonicSampler 采用一种新颖的分层两阶段 top-k 算法，利用 LLM 输出的低熵结构实现高效的大词汇表选择，在竞争基线之上实现最高
  10 倍加速，并在异构推测解码工作负载上达到最高 16 倍加速。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM
  - Triton
  - CUDA
  - CUDA Graph
  - speculative decoding
  - top-k filtering
  - top-p filtering
  - min-p filtering
  key_people: []
key_logic_flow:
- SonicSampler 是一套基于 Triton 的统一 tile 感知内核套件，将 LLM 推理采样流水线（对数处理、令牌选择、验证）垂直融合为单一批处理内核。
- 该方案支持动态逐请求采样行为，包括语法约束解码、重复/频率/存在惩罚、对数偏差、温度缩放、top-k/top-p/min-p 过滤以及推测解码验证。
- SonicSampler 在单个内核中实现完整的采样流水线，同时保持完全 CUDA Graph 兼容性，避免了多内核启动带来的额外开销。
- 核心创新是一种分层两阶段 top-k 算法，利用 LLM 输出的低熵结构实现高效的大词汇表选择，在竞争基线之上实现最高 10 倍加速。
- 在异构推测解码工作负载上，SonicSampler 相比最先进基线实现了最高 16 倍加速，同时保持了灵活的批处理执行能力。
object_mentions:
- object_type: paper
  name: 'SonicSampler: Unified Tile-Aware Kernels for LLM Sampling and Speculative
    Verification'
  canonical_name: SonicSampler
  url: https://arxiv.org/abs/2607.20475
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - SonicSampler 是一套基于 Triton 的统一 tile 感知内核套件，将 LLM 推理的完整采样流水线垂直融合为单一批处理内核。
  - 该方案支持动态逐请求采样行为，包括语法约束解码、重复/频率/存在惩罚、温度缩放和 top-k/top-p/min-p 过滤等操作。
  - SonicSampler 采用分层两阶段 top-k 算法，在竞争基线之上实现最高 10 倍加速，在异构推测解码工作负载上达到最高 16 倍加速。
  article_id: ef0cecd2eb6e2089
extract_result: success
impact_score:
  score: 6.5
  reason: SonicSampler 定位清晰——解决 LLM 推理中被忽视的采样阶段瓶颈。其核心价值在于将分散的多内核采样流水线（对数处理、top-k/top-p/min-p
    过滤、推测验证）垂直融合为单一 CUDA Graph 兼容的 Triton 内核，这在工程层面是扎实的贡献。10x（top-k）和 16x（推测解码）的加速比数据有明确定义的基线对比，不是端到端加速而是特定操作加速，但仍能在高吞吐推理场景中显著降低采样延迟和
    GPU 空闲碎片时间。当前 LLM 推理引擎（vLLM、TensorRT-LLM、SGLang）都在逐算子优化采样阶段，此类工作很可能被主流引擎采纳。但这不是范式突破（如
    FlashAttention 之于 attention），而是对已有工程路径的系统性改进。综合评定 6.5 分：改变局部竞争格局级别的贡献。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 采样阶段单内核融合 + CUDA Graph 兼容，能否被 vLLM/SGLang 快速集成并带来真实推理吞吐提升
hype_assessment:
  level: low
  reason: 论文采用标准的学术写作风格，技术细节充分（分层两阶段 top-k 算法、tile 感知内存布局、CUDA Graph 兼容性设计），提供了与多个基线（torch.multinomial、vLLM
    采样、推测解码基线）的系统性对比，加速比声明有明确的条件和上下文限定。论文中未出现'颠覆''革命性'等 PR 色彩词汇，属于扎实的工程优化工作。
information_entropy: high
domain_disruption:
  technical_innovation: 核心创新在于两点：(1) 利用 LLM 输出 logits 的'低熵结构'——即大多数概率质量集中在少数 token
    上——设计了一款分层两阶段 top-k 算法，大幅减少了大词汇表上的排序开销；(2) 将完整采样流水线（惩罚/偏置/温度/过滤/验证）垂直融合为单一 tile
    感知 Triton 内核，消除多内核启动开销并保持 CUDA Graph 兼容。这本质上是系统级的'算子融合 + 算法结构感知优化'。
  business_model: 无直接影响。但若被主流推理引擎集成，可降低 LLM 服务的解码延迟和 GPU 占用，从而降低每 token 推理成本，间接提升云推理服务的利润率或降价空间。
engineering_complexity: prototype
compound_value:
  score: 7.2
  reason: SonicSampler 满足 VC 评估中'高复利潜力'的核心特征：它解决的 LLM 推理采样瓶颈是每一家部署大模型的公司都必然面对的通用问题，而非某个垂直场景的局部优化。其基于
    Triton 的实现具有跨硬件可移植性（不绑定特定 GPU 架构），且采用 MIT 友好的开源路线，这意味着一旦被 vLLM / TensorRT-LLM
    / SGLang 等主流推理框架集成，就会自动触达全球数千个生产部署，形成极强的网络效应和生态锁定——后续版本迭代向下兼容，集成者迁移成本高。16x 的推测解码加速直接转化为更低的每
    token 成本和更低的端到端延迟，这在 LLM 推理价格战持续加剧的当下是结构性竞争优势。不过扣分点在于：作为学术界产出的优化内核，维护持续性依赖社区贡献而非商业实体驱动，且头部云厂商（Google、AWS）可能自研同等或更优的内核方案，长期来看该项目的商业价值大概率通过被主流框架吸收而间接释放，而非独立成为一家公司。整体而言是
    3-5 年维度上大概率成为开源推理栈标准组件的'高概率、中弹性'标的。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- vLLM
- NVIDIA
- Together AI
- Fireworks AI
- Anthropic
- OpenAI
competitive_casualty:
- 闭源推理优化厂商（如 Deci AI、Cerebras 推断栈中的专有采样组件）
- 未集成高效采样内核的传统 ML 推理框架
market_opportunities:
- 推理服务提供商可集成 SonicSampler 的融合采样内核，直接降低 LLM 推理延迟和计算成本，在相同硬件上提升吞吐量，形成运维成本竞争优势
- 开源社区可基于该分层 top-k 算法开发通用 Triton 采样库，为 vLLM、SGLang 等主流推理框架提供即插即用的加速插件，降低社区采纳门槛
- 企业 AI 基础设施团队可借鉴其 tile 感知的垂直融合设计思路，将同类优化扩展到 MoE 路由、注意力掩码计算等相邻推理环节
risk_matrix:
  regulatory: 无
  technological: 高度依赖 NVIDIA CUDA 和 Triton 编译器生态，非 NVIDIA 平台（AMD ROCm、Apple Metal）移植存不确定性；若未来
    GPU 架构引入专用采样硬件单元，当前软件优化的相对优势可能被削弱
  competitive: NVIDIA 可能自有同类 cuDNN/TensorRT 采样优化方案尚未公开；vLLM 等主流框架内部已有采样实现，外部方案需突破集成壁垒才能获得广泛采用；Meta、Google
    内部亦有类似工程优化团队，公开方案面临大厂资源碾压风险
  ethical: 无——该技术属于基础设施层性能优化，本身不引入歧视偏见、深度伪造或隐私侵犯等伦理问题，相反其节能加速效果对环境有潜在正面意义
  additional: []
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: deep_dive
---

# Computer Science > Artificial Intelligence

# Title:SonicSampler: Unified Tile-Aware Kernels for LLM Sampling and Speculative Verification

View PDF HTML (experimental)Abstract:Sampling in LLM inference comprises a combinatorial set of logit processing, token selection, and verification operations for speculative decoding. However, existing implementations either accelerate only subsets of this pipeline, rely on multiple kernel launches, or assume homogeneous sampling behavior across a batch, limiting support for dynamic serving workloads and preventing efficient CUDA Graph execution. We present $\textbf{SonicSampler}$, a unified suite of tile-aware Triton kernels that vertically fuses the complete sampling pipeline into a fixed, workload-aware execution model. Our kernels support dynamic per-request sampling behaviors, including grammar-constrained decoding, repetition, frequency and presence penalties, logit bias, temperature scaling, top-$k$ / top-$p$ / min-$p$ filtering, and speculative verification - within a single batched kernel while remaining fully CUDA Graph-compatible. Central to our approach is a novel hierarchical two-stage top-$k$ algorithm that achieves up to $\textbf{10x speedup}$ over competitive baselines and exploits the low-entropy structure of LLM outputs to enable efficient selection over large vocabularies. Across heterogeneous speculative decoding workloads, SonicSampler achieves up to $\textbf{16x speedup}$ over state-of-the-art baselines while preserving flexible batched execution.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.