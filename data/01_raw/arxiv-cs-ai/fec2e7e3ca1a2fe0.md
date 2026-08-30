---
title: 'When to Communicate: Belief Distributions and KL Divergence for Principled
  Gating in Multi-Agent RL'
source: https://arxiv.org/abs/2608.14559
author:
- '[[Teoman Kaman]]'
published: '2026-08-18'
created: '2026-08-18'
manifest_dates:
- '2026-08-18'
description: 'arXiv:2608.14559v1 Announce Type: new Abstract: Effective communication
  in multi-agent reinforcement learning requires agents to decide not only \textit{what}
  to communicate, but when? Existing approaches either communicate at every timestep
  or learn a binary gate through REINFORCE policy gradients \cite{singh2019}, a high-variance
  signal that produces unstable and uninterpretable gating behavior. I propose a principled
  alternative: agents communicate only when the KL divergence between their learned
  belief distributions exceeds a fixed threshold. Each agent maintains a belief distribution
  over a latent world state computed as a softmax over its LSTM hidden state, and
  communicates only when belief disagreement is large enough to justify information
  exchange. I evaluate this approach on the Predator-Prey benchmark from IC3Net \cite{singh2019}
  across two environment sizes with 5 seeds each, and on MPE simple\_spread \cite{lowe2017},
  comparing against IC3Net, CommNet, and an independent controller. On PP 10$\times$10,
  IC3Net outperforms KL-belief at all thresholds. On the harder PP 20$\times$20, a
  threshold ablation over $\varepsilon \in \{0.1, 0.3, 0.5, 1.0\}$ reveals an inverted
  U-shape: $\varepsilon=0.5$ achieves 73.84 average steps and 42\% success rate versus
  IC3Net''s 75.31 steps and 31\%, a gap of 1.47 steps and 11 percentage points with
  tighter seed variance. On MPE, the belief head improves mean reward by 12 points
  and reduces variance by 26$\times$ even when gating is inactive, suggesting two
  orthogonal contributions: principled gating when beliefs can converge, and improved
  latent representations that benefit coordination regardless.'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: fec2e7e3ca1a2fe0
---

# Computer Science > Artificial Intelligence

# Title:When to Communicate: Belief Distributions and KL Divergence for Principled Gating in Multi-Agent RL

View PDF HTML (experimental)Abstract:Effective communication in multi-agent reinforcement learning requires agents to decide not only \textit{what} to communicate, but when? Existing approaches either communicate at every timestep or learn a binary gate through REINFORCE policy gradients \cite{singh2019}, a high-variance signal that produces unstable and uninterpretable gating behavior. I propose a principled alternative: agents communicate only when the KL divergence between their learned belief distributions exceeds a fixed threshold. Each agent maintains a belief distribution over a latent world state computed as a softmax over its LSTM hidden state, and communicates only when belief disagreement is large enough to justify information exchange. I evaluate this approach on the Predator-Prey benchmark from IC3Net \cite{singh2019} across two environment sizes with 5 seeds each, and on MPE simple\_spread \cite{lowe2017}, comparing against IC3Net, CommNet, and an independent controller. On PP 10$\times$10, IC3Net outperforms KL-belief at all thresholds. On the harder PP 20$\times$20, a threshold ablation over $\varepsilon \in \{0.1, 0.3, 0.5, 1.0\}$ reveals an inverted U-shape: $\varepsilon=0.5$ achieves 73.84 average steps and 42\% success rate versus IC3Net's 75.31 steps and 31\%, a gap of 1.47 steps and 11 percentage points with tighter seed variance. On MPE, the belief head improves mean reward by 12 points and reduces variance by 26$\times$ even when gating is inactive, suggesting two orthogonal contributions: principled gating when beliefs can converge, and improved latent representations that benefit coordination regardless.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.