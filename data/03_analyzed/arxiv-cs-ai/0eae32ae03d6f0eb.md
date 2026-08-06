---
title: 'Energy Efficiency of Locally Deployed LLMs: A Preliminary Quantitative GPU
  Power Benchmark on Consumer Hardware'
source: https://arxiv.org/abs/2608.00008
author:
- '[[Philipp M. Z\"ahl, Anika Hennig]]'
published: '2026-08-05'
created: '2026-08-05'
manifest_dates:
- '2026-08-05'
description: 'arXiv:2608.00008v1 Announce Type: new Abstract: The local deployment
  of large language models (LLMs) is gaining traction due to privacy concerns and
  the desire for on-premise inference. However, the energy costs on consumer hardware
  remain poorly characterized, as most benchmarks focus solely on accuracy. This paper
  presents a reproducible, hardware-level energy benchmark of nine open-source LLMs
  (1B to 7B parameters) executed on a single consumer GPU (RTX 4060Ti 16GB). Using
  the Ollama inference engine, GPU power draw was sampled at 2Hz via nvidia-smi across
  a fixed prompt set. We evaluate mean/peak power, total energy per prompt (J/prompt),
  energy per output token (J/token), and throughput (tok/s). Our findings suggest
  that factors beyond raw parameter count, including model architecture and quantization
  strategy, drive energy efficiency. Specifically, gemma3:1b and llama3.2:1b achieve
  the lowest energy cost (0.56 J/token and 0.65 J/token) and the highest throughput
  (>170 tok/s). In contrast, the 7B-Mistral model consumes up to 4.4x more energy
  per token than the most efficient model. Notably, qwen3.5:2b exhibits anomalously
  high per-prompt energy due to extended internal reasoning, highlighting the need
  to distinguish between token generation modes in efficiency metrics.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 0eae32ae03d6f0eb
source_type: academic_paper
tldr: 一篇 arXiv 预印本论文在 RTX 4060Ti 16GB 消费级 GPU 上用 Ollama 对九个 1B–7B 开源大模型做能耗基准测试，发现
  gemma3:1b 与 llama3.2:1b 能效最高（约 0.56–0.65 J/token），7B Mistral 能耗为最优模型的 4.4 倍。
objective_summary: 这篇 arXiv 论文针对本地部署大语言模型能源成本缺乏量化的现状，提出可复现的硬件级能耗基准方法。研究者以 Ollama 推理引擎在单张
  RTX 4060Ti 16GB GPU 上运行九个 1B–7B 开源模型，用 nvidia-smi 按 2Hz 采样功耗，评估 J/prompt、J/token
  与吞吐量等指标。结果表明模型架构与量化策略比参数量更影响能效：gemma3:1b 与 llama3.2:1b 每 token 能耗最低（0.56/0.65 J），吞吐量超过
  170 tok/s，而 7B Mistral 每 token 能耗为最优模型的 4.4 倍。qwen3.5:2b 因内部推理导致每提示能耗异常偏高，提示效率指标需区分生成模式。
event_type: infrastructure_update
epistemic_status: theoretical_claim
entities:
  companies:
  - NVIDIA
  - Ollama
  - Google
  - Meta
  - Mistral AI
  - Alibaba
  technologies:
  - LLM
  - GPU
  - quantization
  - nvidia-smi
  key_people: []
key_logic_flow:
- 该论文针对消费级硬件上本地部署大语言模型能源成本缺乏量化的问题，提出一套可复现的硬件级能耗基准测试方法。
- 基准测试在单张 RTX 4060Ti 16GB 消费级 GPU 上运行九个参数量为 1B 到 7B 的开源模型，使用 Ollama 推理引擎并以 nvidia-smi
  按 2Hz 频率采样 GPU 功耗。
- 论文评估了平均与峰值功耗、每个提示的总能量（J/prompt）、每个输出 token 的能量（J/token）以及吞吐量（tok/s）等指标。
- 结果显示 gemma3:1b 与 llama3.2:1b 能耗最低（分别约 0.56 J/token 和 0.65 J/token）且吞吐量最高（超过 170
  tok/s），而 7B Mistral 每 token 能耗为最优模型的 4.4 倍。
- qwen3.5:2b 因内部推理扩展而出现异常偏高的每提示能耗，说明能效指标需要区分 token 生成模式。
object_mentions:
- object_type: paper
  name: 'Energy Efficiency of Locally Deployed LLMs: A Preliminary Quantitative GPU
    Power Benchmark on Consumer Hardware'
  canonical_name: Energy Efficiency of Locally Deployed LLMs
  url: https://arxiv.org/abs/2608.00008
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文提出一套可复现的硬件级能耗基准测试，用于量化消费级 GPU 上本地部署大语言模型的能源成本。
  article_id: 0eae32ae03d6f0eb
- object_type: project
  name: Ollama
  canonical_name: Ollama
  url: https://ollama.com
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - 基准测试使用 Ollama 推理引擎运行九个参数量从 1B 到 7B 的开源大语言模型，并通过 nvidia-smi 以 2Hz 频率采样 GPU 功耗。
  article_id: 0eae32ae03d6f0eb
- object_type: model
  name: gemma3:1b
  canonical_name: Gemma 3 1B
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 结果显示 gemma3:1b 达到最低的每 token 能耗约 0.56 J，同时吞吐量超过 170 tok/s，是能效最高的模型之一。
  article_id: 0eae32ae03d6f0eb
- object_type: model
  name: llama3.2:1b
  canonical_name: Llama 3.2 1B
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 结果显示 llama3.2:1b 达到约 0.65 J/token 的低能耗，吞吐量同样超过 170 tok/s，位列能效最高的模型。
  article_id: 0eae32ae03d6f0eb
- object_type: model
  name: qwen3.5:2b
  canonical_name: Qwen 3.5 2B
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 论文指出 qwen3.5:2b 因内部推理扩展而表现出异常偏高的每提示能耗，说明效率指标需要区分 token 生成模式。
  article_id: 0eae32ae03d6f0eb
- object_type: model
  name: Mistral 7B
  canonical_name: Mistral 7B
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 论文指出 7B 规模的 Mistral 模型每 token 能耗最高，比能效最优的模型多消耗约 4.4 倍的能量。
  article_id: 0eae32ae03d6f0eb
extract_result: success
impact_score:
  score: 3.5
  reason: 该论文属于初步实证基准研究，覆盖范围仅单张消费级 GPU（RTX 4060Ti）、单一推理引擎（Ollama）和 1B–7B 小模型，样本量有限且自述为
    preliminary；其价值在于提出可复现的硬件级能效测量方法，并为本地部署实践者提供模型选型的量化依据，但它不引入新的训练/推理范式、不构成产品发布，也未改变任何竞争格局，属于边缘部署细分领域的基础数据积累，短期行业冲击有限。综合判定
    3.5 分。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 小模型本地部署的能效选型：模型架构与量化策略对能耗的影响是否真的大于参数量
hype_assessment:
  level: low
  reason: 论文标题与摘要自述为'初步'（Preliminary）定量基准，方法透明可复现（nvidia-smi 2Hz 采样、固定提示集、明确定义 J/prompt
    与 J/token），并主动披露 qwen3.5:2b 因推理扩展导致每提示能耗异常这一混杂因素；全文无'颠覆''革命性'等 PR 用语，属于脚踏实地的实证测量工作，不存在概念包装。
information_entropy: medium
domain_disruption:
  technical_innovation: 未提出新的模型架构或训练方法，创新点在于可复现的消费级 GPU 能耗基准方法学：以 nvidia-smi 2Hz 采样
    + Ollama 固定提示集，同步测量平均/峰值功率、J/prompt、J/token 与吞吐量；关键实证发现是模型架构与量化策略比参数量更能驱动能效，并识别出推理模式（reasoning
    token）对每提示能耗指标的混杂效应，为后续能效基准设计提供了方法参考。
  business_model: 为本地/端侧 AI 部署提供能耗成本的量化选型依据，对隐私敏感企业、on-premise 推理场景的运营成本（opex）测算有直接参考价值，可间接影响边缘推理的商业化定价与模型推荐策略（如
    Ollama 生态的默认模型选择）；但属于积累型参考数据，短期内对商业模式重塑有限。
engineering_complexity: prototype
compound_value:
  score: 4.5
  reason: 该事件本身是一篇初步基准论文（单一 RTX 4060Ti GPU、单一 Ollama 引擎、9 个 1B–7B 模型），样本面窄、方法论尚待大规模复现，作为独立知识资产复利有限，很快会被更全面的基准超越。但其真正价值在于为'边缘/本地部署'趋势提供了可量化的能耗选择标准——确立'架构与量化策略比参数量更决定能效'这一认知，将能耗从隐性成本变为模型选型的显性维度。这支撑的
    edge AI / on-premise 推理赛道具备长期复利：随隐私监管强化、推理成本下探，本地部署从极客玩法走向企业刚需，能耗基准方法论有望沉淀为该细分赛道的评估基础设施。综合来看，处于'有潜力成为细分赛道标准但需持续验证'区间，给
    4.5 分。
value_capture_layer: foundation_model
moat_impact: democratizes_access
key_beneficiaries:
- Ollama
- Google (Gemma)
- Meta (Llama)
- NVIDIA
- Hugging Face
competitive_casualty:
- Mistral AI
- 云优先推理服务商
- 高功耗边缘推理硬件方案
market_opportunities:
- 创业者可基于此类硬件级能耗基准方法论，开发面向企业本地化 LLM 部署的能效选型工具，按 J/token 与硬件成本自动推荐最优的模型+量化组合
- 建议关注消费级与边缘 AI 设备的绿电优化软件机会，如针对 Ollama/Llama.cpp 等本地推理引擎的功耗感知调度与量化策略自动调优插件
- 开源社区可共建标准化的 LLM 能耗基准数据集（类似 Hugging Face 模型卡的能效评分），形成 '绿色 AI' 选型基础设施与生态位
risk_matrix:
  regulatory: 无
  technological: 该基准依赖 nvidia-smi 2Hz 采样与特定消费级 GPU、驱动及量化库组合，结论普适性有限；随 GPU 架构与推理引擎演进，文中具体数值可能快速过时；qwen3.5:2b
    等异常数据也暴露出'每 token 能耗'指标存在测量口径缺陷，该方法本身可能被更严谨的基准框架替代
  competitive: NVIDIA/AMD/Qualcomm 等芯片厂商与云厂商可能各自发布有利口径的能耗基准，形成营销竞争；若 Ollama/Llama.cpp
    等推理引擎内置能效评分功能，可能挤压第三方基准工具的生存空间
  ethical: 能耗数据存在被厂商选择性引用以进行绿色营销（greenwashing）的风险，需警惕'能效评分'沦为营销话术而非客观工程指标
  additional:
  - 论文为未经同行评审的 arXiv 预印本，仅覆盖单张消费级 GPU 与单一推理引擎，样本代表性有限，结论需更多硬件与场景下的复现验证
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: monitor
---

# Computer Science > Artificial Intelligence

# Title:Energy Efficiency of Locally Deployed LLMs: A Preliminary Quantitative GPU Power Benchmark on Consumer Hardware

View PDF HTML (experimental)Abstract:The local deployment of large language models (LLMs) is gaining traction due to privacy concerns and the desire for on-premise inference. However, the energy costs on consumer hardware remain poorly characterized, as most benchmarks focus solely on accuracy. This paper presents a reproducible, hardware-level energy benchmark of nine open-source LLMs (1B to 7B parameters) executed on a single consumer GPU (RTX 4060Ti 16GB). Using the Ollama inference engine, GPU power draw was sampled at 2Hz via nvidia-smi across a fixed prompt set. We evaluate mean/peak power, total energy per prompt (J/prompt), energy per output token (J/token), and throughput (tok/s). Our findings suggest that factors beyond raw parameter count, including model architecture and quantization strategy, drive energy efficiency. Specifically, gemma3:1b and llama3.2:1b achieve the lowest energy cost (0.56 J/token and 0.65 J/token) and the highest throughput (>170 tok/s). In contrast, the 7B-Mistral model consumes up to 4.4x more energy per token than the most efficient model. Notably, qwen3.5:2b exhibits anomalously high per-prompt energy due to extended internal reasoning, highlighting the need to distinguish between token generation modes in efficiency metrics.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.