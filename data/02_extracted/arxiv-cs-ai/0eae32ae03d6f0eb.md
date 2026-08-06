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