---
title: DiffusionGemma Technical Report
source: https://arxiv.org/abs/2608.00146
author:
- '[[gmays]]'
published: '2026-08-20'
created: '2026-08-20'
manifest_dates:
- '2026-08-20'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ffb2d30bbc94ba4a
source_type: community_discussion
tldr: DiffusionGemma 是一个实验性开源权重语言模型，采用离散扩散机制并行迭代精炼 256 个 token 的块，绕开自回归模型的顺序解码瓶颈；在单块
  NVIDIA H100 上每秒约输出 1500 个 token，训练预算不足原模型的 10%。
objective_summary: DiffusionGemma 是基于 mixture-of-experts 架构的 Gemma 4（3.8B 激活参数、25.2B
  总参数）微调得到的实验性开源权重语言模型。其两阶段训练流程以不足原模型 10% 的 token 预算完成，第一阶段用监督微调教授双向去噪，第二阶段将强化学习与采样器蒸馏结合以同时改进生成质量和推理效率。在单块
  NVIDIA H100 GPU 上，该模型每次前向传播约生成 20 个 token、每秒约输出 1500 个 token，显著快于采用最先进投机解码的自回归模型，并保留思维模式、多模态输入和长上下文支持。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Google DeepMind
  - NVIDIA
  technologies:
  - discrete diffusion
  - mixture-of-experts
  - speculative decoding
  - reinforcement learning
  - sampler distillation
  - supervised fine-tuning
  key_people: []
key_logic_flow:
- DiffusionGemma 是一种使用离散扩散机制生成文本的实验性开源权重语言模型。
- 与逐 token 解码的自回归模型不同，它并行迭代精炼 256 个 token 的块，从而绕开顺序解码瓶颈。
- 该模型通过在 mixture-of-experts 架构的 Gemma 4 模型上微调获得，总训练 token 预算不足原模型的 10%。
- 两阶段训练中，第一阶段用监督微调学习双向去噪，第二阶段将强化学习与采样器蒸馏结合，同时改进生成质量与推理效率。
- 在完整评测套件上，模型每次前向传播约生成 20 个 token，在单块 NVIDIA H100 上每秒约输出 1500 个 token，快于采用投机解码的自回归模型。
- 模型保留思维模式、多模态输入和长上下文支持，仍可进行自回归生成且性能降级较小，指向混合扩散-自回归解码方向。
object_mentions:
- object_type: model
  name: DiffusionGemma
  canonical_name: DiffusionGemma
  url: https://arxiv.org/abs/2608.00146
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - DiffusionGemma 是实验性的开源权重语言模型，使用离散扩散在并行块中迭代精炼 256 个 token，而非逐 token 顺序解码。
  - 在单块 NVIDIA H100 GPU 上，DiffusionGemma 每秒约输出 1500 个 token，大幅快于采用最先进投机解码的自回归模型。
  article_id: ffb2d30bbc94ba4a
- object_type: model
  name: Gemma 4
  canonical_name: Gemma 4
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - DiffusionGemma 由 mixture-of-experts 架构的 Gemma 4 模型微调而来，该模型拥有 3.8B 激活参数和 25.2B
    总参数。
  article_id: ffb2d30bbc94ba4a
extract_result: success
impact_score:
  score: 7.3
  reason: 该技术报告首次将离散扩散解码推进到 25.2B 参数 MoE 的实用规模，以单块 H100 每秒约 1500 token 的输出速度展示了相对'自回归+投机解码'的显著优势，且训练预算不足原模型的
    10%，有望重构高吞吐/长文本推理的成本结构并开辟混合扩散-自回归解码路线。但它仍处于'实验性开源权重'阶段，存在质量权衡、配套 serving 生态未成熟，短期更多影响研究与推理工程方向而非直接改变终端产品格局，因此落在'重要发布'与'范式转移'之间。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 开源权重 + 单卡 H100 每秒 1500 token 的推理吞吐，以及训练成本不足原模型 10% 的高效两阶段训练管线
hype_assessment:
  level: low
  reason: 论文给出可验证的具体数据（每次前向约 20 token、1500 tok/s、训练预算<10%）与完整评测套件，措辞相对克制，未滥用'颠覆'等营销词汇；'新帕累托前沿'的表述有实验数据支撑而非空洞口号，干货占比高。
information_entropy: high
domain_disruption:
  technical_innovation: 离散扩散在 LLM 上的规模化工程落地：以 256-token 块为单位的并行迭代精炼取代逐 token 自回归解码，配合'双向去噪
    SFT + 强化学习与采样器蒸馏'两阶段训练，在极低训练预算下获得数量级解码加速；同时保留思维模式、多模态输入与长上下文支持，并验证了与自回归兼容的混合扩散-AR
    解码路径。
  business_model: 将单 GPU 推理吞吐提升一到两个数量级，意味着单块 H100 即可支撑高并发/长文本生成场景，直接重构云端推理的单位算力成本与硬件规划；开源权重形式可能让中小团队以极低成本获得接近顶配的生成速度，冲击以
    API 按 token 计价的现有商业模式，并促使投机解码等加速方案向扩散路线迁移。
engineering_complexity: prototype
compound_value:
  score: 7.5
  reason: 从资本视角看，DiffusionGemma 直接击中 AI 产业最核心的经济瓶颈——推理成本与延迟。自回归串行解码是过去数年推理成本居高不下的结构性原因，而离散扩散把解码从逐
    token 串行变为 256 token 块级并行精炼，在单卡 H100 上实现约 1500 token/s，显著快于最先进的投机解码方案，意味着单位 token
    的算力成本可能迎来数量级下降。真正的复利点在于训练方法论：以不足原模型 10% 的 token 预算将现成 AR 模型微调为扩散模型，证明这条路线不需要从零预训练的巨额资本开支，具备被广泛复制并成为标准训练范式的潜力——一旦扩散微调成为行业惯例，围绕它的工具链、评估标准与推理服务将沉淀为长期基础设施。风险在于当前仍是实验性技术报告，规模仅
    3.8B 激活参数，超大参数规模与复杂 agentic 任务上的稳定性、生成质量上限尚未验证；若 3-5 年内扩散-自回归混合解码被证明可扩展到前沿模型，它大概率成为推理基础设施的基石，故给予
    7.5 分。
value_capture_layer: foundation_model
moat_impact: democratizes_access
key_beneficiaries:
- Google DeepMind
- NVIDIA
- Hugging Face
- Together AI
- 开源模型生态
competitive_casualty:
- 投机解码类推理加速公司
- 重 token 预算从零预训练的闭源模型厂商
market_opportunities:
- 可基于该开源权重模型开发面向实时交互场景（语音助手、实时编码辅助、高频 Agent 循环）的低延迟推理服务，利用单卡每秒约 1500 token 的吞吐优势抢占体验敏感型应用市场
- 创业者可围绕扩散式并行解码构建推理加速中间件或混合扩散-自回归解码工具，帮助现有 LLM 应用在不更换主模型的前提下降低推理成本与延迟
- 鉴于其训练预算不足原模型的 10%，建议关注低资源条件下将 AR 模型改造为扩散模型的微调方法论，可作为垂直行业低成本快速定制专属模型的可行路径
risk_matrix:
  regulatory: 开源权重模型分发需关注 Gemma 使用条款与潜在出口管制合规要求；同时 1500 token/s 的高吞吐生成能力可能被用于规模化制造虚假信息，触发内容治理与平台责任监管
  technological: 模型仍属实验性质，扩散解码在长文本一致性、事实性上可能存在质量折损，且论文明确指向混合扩散-自回归方向，说明纯扩散路线可能被更优范式部分替代
  competitive: 头部实验室（OpenAI、Anthropic、Meta 等）可能迅速跟进发布更高性能的扩散或混合解码模型，形成生态挤压；同时推理性能高度依赖
    NVIDIA 单卡算力，存在硬件生态锁定风险
  ethical: 高吞吐文本生成将显著降低批量生成垃圾内容、深度伪造文本与操纵舆论的成本，可能放大内容滥用与信息污染问题
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
---

# Computer Science > Computation and Language

# Title:DiffusionGemma Technical Report

View PDF HTML (experimental)Abstract:We introduce DiffusionGemma, an experimental open-weight language model that uses discrete diffusion to generate text at exceptionally high speed. Rather than decoding one token at a time, DiffusionGemma iteratively refines blocks of 256 tokens in parallel, avoiding the sequential decoding bottleneck of conventional autoregressive (AR) large language models. Instead of training from scratch, we obtain DiffusionGemma by fine-tuning the mixture-of-experts Gemma 4 model with 3.8B activated and 25.2B total parameters. Our compute-efficient two-stage training pipeline uses fewer than 10% of the starting AR model's total training token budget. The first stage uses supervised fine-tuning to teach bidirectional denoising, while the second stage combines reinforcement learning with sampler distillation to jointly improve generation quality and inference efficiency. DiffusionGemma establishes a new Pareto frontier for the trade-off between generation speed and model capability. Averaged across our full evaluation suite, it generates around 20 tokens per forward pass and achieves roughly 1,500 output tokens per second on a single NVIDIA H100 GPU, which is substantially faster than AR models even with state-of-the-art speculative decoding. DiffusionGemma also retains the starting model's support for thinking mode, multimodal inputs, and long contexts. Despite diffusion fine-tuning, it remains capable of AR generation with only minor performance degradation, suggesting a path toward hybrid diffusion-AR decoding.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.