---
title: 'PlanFlip: Attacking Multi-Agent LLM Systems via Planning-Phase Prompt Injection'
source: https://arxiv.org/abs/2607.16199
author:
- '[[Yuhang Wang]]'
published: '2026-07-21'
created: '2026-07-21'
manifest_dates:
- '2026-07-21'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: a0eaebcb1a97f78f
---

# Computer Science > Artificial Intelligence

# Title:PlanFlip: Attacking Multi-Agent LLM Systems via Planning-Phase Prompt Injection

View PDF HTML (experimental)Abstract:Multi-agent LLM systems increasingly rely on a Planner to decompose goals into sub-task sequences that downstream Executor and Critic agents execute and audit. We identify the planning phase as a critical attack surface: a single injection into the Planner's context achieves cascade amplification, corrupting all downstream sub-tasks simultaneously. We introduce PlanFlip, a framework comprising four planning-phase prompt injection attacks -- GoalSubstitution (PF-1), PriorityInversion (PF-2), ContextPollution (PF-3), and RoleConfusion (PF-4) -- each disguised as plausible tool outputs to evade keyword filters. Evaluating nine frontier LLMs across 3,479 episodes, we uncover three findings: (1) capability amplifies vulnerability -- GPT-5 achieves the highest attack success rate (ASR = 0.68), contradicting the assumption that stronger models are inherently more secure; (2) homogeneous pipelines exhibit a correlated-agent blind spot -- GPT-4o and Llama-3.3-70B show ASR near 0 yet Stealth = 1.00 and StepShift > 0, with attacks restructuring plans while the same-backbone Critic reports alignment (two independent judges confirm -0.20 to -0.32 semantic deviation, r = 0.943); (3) reasoning-augmented models resist injections -- DeepSeek-R1 achieves StepShift = 0.00 across all attacks. We propose GoalAnchorCheck (D1) and CrossAgentConsensus (D2), achieving detection rates up to 1.00 and outperforming same-backbone baselines in 15 of 16 cells. Our key insight: heterogeneous model diversity is a security prerequisite for multi-agent systems; redundancy within a homogeneous backbone provides no protection against planning-phase attacks.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.