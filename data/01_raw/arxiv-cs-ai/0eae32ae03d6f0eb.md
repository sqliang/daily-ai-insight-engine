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
pipeline_stage: ingested
id: 0eae32ae03d6f0eb
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