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
pipeline_stage: fact_extracted
id: fec2e7e3ca1a2fe0
source_type: academic_paper
tldr: 论文提出基于 KL 散度阈值的原则性通信门控方法，让多智能体仅在信念分布分歧超过阈值时才通信。在 Predator-Prey 20×20 上 ε=0.5
  达到 73.84 平均步数和 42% 成功率，优于 IC3Net 的 75.31 步和 31%。
objective_summary: 该 arXiv 论文研究多智能体强化学习中的通信时机问题，指出现有方法要么每步都通信，要么通过 REINFORCE 学习高方差的二元门控。作者提出让每个智能体维护基于
  LSTM 隐藏状态 softmax 计算的信念分布，仅在分布间 KL 散度超过阈值时通信，并在 Predator-Prey 与 MPE simple_spread
  上对比 IC3Net、CommNet 与独立控制器。在 Predator-Prey 10×10 上 IC3Net 全面占优，但在更难的 20×20 上 ε=0.5
  取得 73.84 平均步数与 42% 成功率，优于 IC3Net 的 75.31 步与 31%；在 MPE 上信念头即使门控未激活也使奖励提升 12 点、方差降低
  26 倍。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Multi-Agent Reinforcement Learning
  - KL Divergence
  - REINFORCE
  - LSTM
  - Belief Distributions
  - IC3Net
  - CommNet
  - MPE
  - Predator-Prey
  key_people: []
key_logic_flow:
- 论文指出多智能体强化学习的通信时机问题：现有方法或每步都通信，或用 REINFORCE 学习二元门控，后者高方差导致不稳定且不可解释的门控行为。
- 作者提出原则性门控替代方案：每个智能体维护对潜在世界状态的信念分布，该分布是 LSTM 隐藏状态的 softmax，仅在信念分歧的 KL 散度超过固定阈值时通信。
- 方法在 IC3Net 的 Predator-Prey 基准（两种环境规模，各 5 个种子）和 MPE simple_spread 上评估，与 IC3Net、CommNet
  和独立控制器对比。
- 在 PP 10×10 上 IC3Net 在所有阈值下优于 KL-belief；在更难的 PP 20×20 上，阈值消融（ε∈{0.1,0.3,0.5,1.0}）呈倒
  U 型，ε=0.5 达到 73.84 平均步数和 42% 成功率。
- 相比 IC3Net 的 75.31 步与 31% 成功率，ε=0.5 领先 1.47 步和 11 个百分点且种子方差更小；在 MPE 上信念头在门控未激活时仍提升平均奖励
  12 点、方差降低 26 倍。
- 作者认为存在两个正交贡献：信念可收敛时的原则性门控，以及改善协调的潜在表征提升。
object_mentions:
- object_type: paper
  name: 'When to Communicate: Belief Distributions and KL Divergence for Principled
    Gating in Multi-Agent RL'
  canonical_name: 'When to Communicate: Belief Distributions and KL Divergence for
    Principled Gating in Multi-Agent RL'
  url: https://arxiv.org/abs/2608.14559
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文提出基于 KL 散度阈值的原则性通信门控方法，智能体仅在信念分布分歧超过阈值时通信，并在 Predator-Prey 与 MPE simple_spread
    基准上进行了验证。
  article_id: fec2e7e3ca1a2fe0
- object_type: model
  name: IC3Net
  canonical_name: IC3Net
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - IC3Net 是论文的主要对比基线，通过 REINFORCE 策略梯度学习二元通信门控，论文指出其高方差信号导致不稳定且不可解释的门控行为。
  article_id: fec2e7e3ca1a2fe0
- object_type: model
  name: CommNet
  canonical_name: CommNet
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - CommNet 是论文的对比基线之一，与 IC3Net、独立控制器一同在 Predator-Prey 和 MPE 基准上与所提方法进行性能比较。
  article_id: fec2e7e3ca1a2fe0
- object_type: dataset
  name: MPE simple_spread
  canonical_name: MPE
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - MPE simple_spread 是多智能体粒子环境中的基准任务，论文在该环境中验证了信念头在门控未激活时仍能提升平均奖励 12 点并将方差降低 26 倍。
  article_id: fec2e7e3ca1a2fe0
extract_result: success
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