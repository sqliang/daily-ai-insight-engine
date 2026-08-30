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
pipeline_stage: ingested
id: a8ba0b0ace9187db
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