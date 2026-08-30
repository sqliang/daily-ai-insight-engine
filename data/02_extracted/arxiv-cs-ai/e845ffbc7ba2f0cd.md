---
title: World models of environment, agent and joint agent-environment systems
source: https://arxiv.org/abs/2608.20401
author:
- '[[Manuel Baltieri, Filippo Torresan, Yivan Zhang, Alexander Boyd, Fernando E. Rosas]]'
published: '2026-08-24'
created: '2026-08-24'
manifest_dates:
- '2026-08-24'
description: 'arXiv:2608.20401v1 Announce Type: new Abstract: World models are a central
  component of model-based reinforcement learning. They are usually discussed in terms
  of what variables they predict, such as observations, rewards, states, latent or
  information states. We argue that there is a prior distinction: which channel they
  model. We consider three cases: the environment channel $O_{:} \mid A_{:}$, the
  agent channel $A_{:} \mid O_{:}$, and the realised joint process $(A, O)_{:}$, equivalently
  viewed as a channel with no inputs. Using computational mechanics, we define canonical
  predictive models for these three cases as $\epsilon$-transducers or $\epsilon$-machines.
  Canonical environment models recover standard predictive state representations,
  while the other two give analogous notions of canonical models for the agent and
  the joint system. We then build canonical support-restricted environment and agent
  models induced by closed-loop coupling, whose predictive equivalences range over
  continuations supported by the realised interaction. The key structural result is
  that canonical support-restricted environment states factor through the canonical
  joint causal states, and their transition structure is induced directly from the
  joint model; the agent-side construction is dual. Finally, we give a POMDP/controller
  example in which the unrestricted environment model has infinitely many states while
  the canonical support-restricted model induced by the coupling is finite. The framework
  clarifies what different world models are models of, and how coupling and support
  restriction can change their canonical predictive structure and complexity.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: e845ffbc7ba2f0cd
source_type: academic_paper
tldr: 该 arXiv 论文提出世界模型研究应优先区分所建模的通道，即环境通道、智能体通道与联合过程三类，并用计算力学定义了三类情况的规范预测模型。论文进一步证明闭环耦合诱导的支持受限模型可显著降低状态复杂度，示例中从无限状态降为有限。
objective_summary: 该论文（arXiv 2608.20401）属于人工智能领域，研究基于模型的强化学习中的世界模型。作者主张在讨论世界模型预测什么变量之前，应先区分其建模的通道，将模型分为环境通道、智能体通道与实际联合过程三类。论文运用计算力学为三类情况定义规范预测模型（ε-转导器或
  ε-机器），并构建闭环耦合诱导的支持受限环境与智能体模型。核心结构结果表明支持受限环境状态可经联合因果状态分解，且论文以 POMDP/控制器示例展示无限制模型状态无限而受限模型有限。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - World Models
  - Model-Based Reinforcement Learning
  - Computational Mechanics
  - ε-transducers
  - ε-machines
  - POMDP
  - Predictive State Representations
  - Causal States
  key_people: []
key_logic_flow:
- 论文主张世界模型研究存在一个先于“预测什么变量”的区分，即“建模哪个通道”，并将世界模型分为环境通道、智能体通道与联合过程三类。
- 作者使用计算力学为三类情况定义规范预测模型，分别表示为 ε-转导器（ε-transducers）或 ε-机器（ε-machines）。
- 规范环境模型恢复了标准的预测状态表示，而另外两类为智能体与联合系统提供了对应的规范模型概念。
- 论文构建了由闭环耦合诱导的规范支持受限环境与智能体模型，其预测等价关系覆盖实际交互所支持的延续。
- 关键结构结果是规范支持受限环境状态可通过规范联合因果状态分解，其转移结构直接由联合模型诱导，智能体侧构造与之对偶。
- 论文给出 POMDP/控制器示例，其中无限制环境模型具有无限多个状态，而由耦合诱导的规范支持受限模型是有限的。
object_mentions:
- object_type: paper
  name: World models of environment, agent and joint agent-environment systems
  canonical_name: arXiv 2608.20401 World models of environment, agent and joint agent-environment
    systems
  url: https://arxiv.org/abs/2608.20401
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文定义了世界模型所建模的三种通道，即环境通道、智能体通道以及实际联合过程。
  - 论文以 POMDP/控制器示例说明无限制环境模型状态无限，而耦合诱导的支持受限模型有限。
  article_id: e845ffbc7ba2f0cd
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:World models of environment, agent and joint agent-environment systems

View PDFAbstract:World models are a central component of model-based reinforcement learning. They are usually discussed in terms of what variables they predict, such as observations, rewards, states, latent or information states. We argue that there is a prior distinction: which channel they model. We consider three cases: the environment channel $O_{:} \mid A_{:}$, the agent channel $A_{:} \mid O_{:}$, and the realised joint process $(A, O)_{:}$, equivalently viewed as a channel with no inputs. Using computational mechanics, we define canonical predictive models for these three cases as $\epsilon$-transducers or $\epsilon$-machines. Canonical environment models recover standard predictive state representations, while the other two give analogous notions of canonical models for the agent and the joint system. We then build canonical support-restricted environment and agent models induced by closed-loop coupling, whose predictive equivalences range over continuations supported by the realised interaction. The key structural result is that canonical support-restricted environment states factor through the canonical joint causal states, and their transition structure is induced directly from the joint model; the agent-side construction is dual. Finally, we give a POMDP/controller example in which the unrestricted environment model has infinitely many states while the canonical support-restricted model induced by the coupling is finite. The framework clarifies what different world models are models of, and how coupling and support restriction can change their canonical predictive structure and complexity.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.