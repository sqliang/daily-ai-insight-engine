---
title: Introducing Grok 4.6 (4 minute read)
source: https://x.ai/news/grok-4-6?utm_source=tldrai
author: []
published: ''
created: '2026-08-14'
manifest_dates:
- '2026-08-14'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: 967ffafc08f9e0fc
---

Grok 4.6 builds on Grok 4.5 with a particular focus on long-running agents and more ambitious interactive and visual work.

Today we are releasing **Grok 4.6**. Grok 4.6 builds on Grok 4.5 with a particular focus on long-running agents and more ambitious interactive and visual work. It stays with complex tasks across many steps, whether researching a topic, analyzing information, working across a codebase, or turning an idea into a polished application or work artifact.

Grok 4.6 achieves frontier intelligence across several agentic coding and knowledge work benchmarks. It matches GPT-5.6 Sol on the Artificial Analysis Intelligence Index, which is a composite score of nine benchmarks.

Grok 4.6 is available today in Cursor and Grok Build. We’re offering 2x included usage inside Grok Build and Cursor for the first week so you can start trying 4.6 immediately.

Grok 4.6 underwent a longer supplemental training run than Grok 4.5, with curated model-generated data for reasoning and advanced technical concepts, high-quality engineering data, and an improved optimizer and training recipe. This produced a stronger foundation for the SFT and RL stages that followed.

We then used Grok 4.5 to regenerate the SFT trajectories across reasoning efforts, agent harnesses, and domains such as STEM, software engineering, and knowledge work, and filtered out problematic traces with model-based checks. The resulting SFT checkpoint shows strong performance and improved behavior.

Grok 4.6 is trained on a wide range of agentic RL tasks, including knowledge work, general coding, and domain-specific environments for kernel optimization, web development, computer-aided design, and more.

We tested Grok 4.6 on projects designed to stretch its range and ability to sustain work over many steps. We found the model is especially strong at turning a broad product idea into a working first version. It can research unfamiliar domains, structure the application, implement the core interactions, and continue refining the result through several rounds of feedback.

On longer trajectories, we also started to see more self-testing and verification, with the model checking its own work before moving on.

Grok 4.6 produces stronger first passes on visual and interactive projects than we typically saw with Grok 4.5. Given a concrete product idea, it is able to establish structure and visual language for an application in one pass. This has made it especially useful for projects where the fastest route to a good result was to begin with something substantial and then iterate in the loop.

Grok 4.6’s safeguards have been improved and calibrated in line with the model’s capabilities.

Our safety stack is designed to maximize utility and security across legitimate use cases, allowing Grok 4.6 to be helpful and safe in domains such as vulnerability patching, accelerating the engineering design cycle, and augmenting AI research.

Our safeguard evaluation work reflects Grok 4.6’s expanded capabilities, with our widest-ever suite of pre-deployment testing for capabilities and safeguard calibration, as well as extensive post-deployment and third-party testing.

Grok 4.6 is available today in Cursor and Grok Build. It’s also available in the API and other partners like OpenRouter, Vercel, and Cloudflare.

Pricing starts at $2 per million input tokens and $6 per million output tokens. Additionally, there is a fast variant which is twice the price.

We’re offering 2x included usage inside Grok Build and Cursor for the first week so you can start trying 4.6 immediately.