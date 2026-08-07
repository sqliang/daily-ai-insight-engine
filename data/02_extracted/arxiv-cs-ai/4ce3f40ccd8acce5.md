---
title: 'NeuMoSync: End-to-End Neuromodulatory Control for Plasticity and Adaptability
  in Continual Learning'
source: https://arxiv.org/abs/2608.04358
author:
- '[[Seyed Roozbeh Razavi Rohani, Khashayar Khajavi, Wesley Chung, Mandana Samiei,
  Mo Chen]]'
published: '2026-08-06'
created: '2026-08-06'
manifest_dates:
- '2026-08-06'
description: 'arXiv:2608.04358v1 Announce Type: new Abstract: Continual learning (CL)
  requires models to learn tasks sequentially, yet deep neural networks often suffer
  from plasticity loss and poor knowledge transfer, which can impede their long-term
  adaptability. Drawing high-level inspiration from global neuromodulatory mechanisms
  in the brain, we introduce Neuromodulation and Synchronization (NeuMoSync), a novel
  architecture that integrates dynamic, neuron-specific modulation into deep neural
  networks to enhance their adaptability and plasticity. NeuMoSync extends standard
  neural network architectures with learnable feature vectors for each neuron that
  track network-wide historical context and with a module operating at a higher level
  of abstraction. This module synthesizes neuron-specific signals, conditioned on
  both current inputs and the network''s evolving state, to adaptively regulate activation
  dynamics and synaptic plasticity. Evaluated on diverse CL benchmarks, including
  memorization (Random Label CIFAR-10 and Random Label MNIST), concept drift (Shuffle
  CIFAR-10 and Shuffle Mini-ImageNet), class-incremental learning (Class Split ImageNet
  and Class Split CIFAR-100), and domain-incremental learning (Permuted MNIST), NeuMoSync
  demonstrates strong performance in retaining plasticity and achieves improvements
  in both forward and backward adaptation compared with existing methods. Ablation
  studies validate the necessity of each component, while analysis of the learned
  modulatory signals reveals interpretable coordination patterns across tasks. Our
  work underscores the potential of integrating global coordination mechanisms into
  deep learning systems to advance robust, adaptive continual learning. The code is
  publicly available at https://github.com/RoozbehRazavi/NeuMoSync.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 4ce3f40ccd8acce5
source_type: academic_paper
tldr: NeuMoSync 是一种受大脑全局神经调制机制启发的端到端持续学习架构，通过为每个神经元引入可学习的特征向量并增加高层调制模块，动态调控激活过程与突触可塑性，在记忆保持、概念漂移、类增量与域增量学习等多类基准上改善了可塑性保持与前向/后向适应，代码已公开。
objective_summary: NeuMoSync（Neuromodulation and Synchronization）是 arXiv 论文 2608.04358
  提出的持续学习架构，针对深度神经网络在按顺序学习任务时的可塑性丧失与知识迁移不足问题。它为每个神经元增加可学习的特征向量以追踪网络级历史上下文，并引入更高抽象层次的模块，根据当前输入与网络演化状态合成神经元特异性调制信号。论文在随机标签
  CIFAR-10/MNIST、Shuffle CIFAR-10/Mini-ImageNet、Class Split ImageNet/CIFAR-100 与 Permuted
  MNIST 等基准上评估，报告称其在可塑性保持、前向与后向适应上优于现有方法。消融实验验证了各组件的必要性，对学习到的调制信号的分析揭示了跨任务的可解释协调模式。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - NeuMoSync
  - Continual Learning
  - Neuromodulation
  - Synaptic Plasticity
  - Class-Incremental Learning
  - Domain-Incremental Learning
  key_people: []
key_logic_flow:
- 持续学习要求模型按顺序学习多个任务，但深度神经网络普遍存在可塑性丧失与知识迁移不足的问题，制约了长期适应性。
- 受大脑全局神经调制机制启发，论文提出 NeuMoSync 架构，为标准神经网络引入每个神经元可学习的特征向量，以追踪网络级历史上下文。
- NeuMoSync 通过一个高层抽象模块，根据当前输入与网络演化状态合成神经元特异性信号，动态调控激活动态与突触可塑性。
- 论文在记忆保持、概念漂移、类增量学习与域增量学习等多类基准上评估，NeuMoSync 报告在可塑性保持及前向与后向适应上优于现有方法。
- 消融实验验证了各组成组件的必要性，对学习到的调制信号的分析揭示了跨任务的可解释协调模式。
object_mentions:
- object_type: paper
  name: 'NeuMoSync: End-to-End Neuromodulatory Control for Plasticity and Adaptability
    in Continual Learning'
  canonical_name: NeuMoSync
  url: https://arxiv.org/abs/2608.04358
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - NeuMoSync 通过每个神经元可学习的特征向量与高层抽象模块，根据当前输入和网络演化状态动态调控激活动态与突触可塑性。
  - NeuMoSync 在随机标签 CIFAR-10/MNIST、Shuffle CIFAR-10/Mini-ImageNet、Class Split ImageNet/CIFAR-100
    与 Permuted MNIST 等基准上评估了可塑性与前向后向适应表现。
  article_id: 4ce3f40ccd8acce5
- object_type: project
  name: NeuMoSync code
  canonical_name: NeuMoSync code
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 论文摘要声明代码已公开提供，但摘要文本中链接仅以占位符形式呈现，未给出具体的仓库地址。
  article_id: 4ce3f40ccd8acce5
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:NeuMoSync: End-to-End Neuromodulatory Control for Plasticity and Adaptability in Continual Learning

View PDF HTML (experimental)Abstract:Continual learning (CL) requires models to learn tasks sequentially, yet deep neural networks often suffer from plasticity loss and poor knowledge transfer, which can impede their long-term adaptability. Drawing high-level inspiration from global neuromodulatory mechanisms in the brain, we introduce Neuromodulation and Synchronization (NeuMoSync), a novel architecture that integrates dynamic, neuron-specific modulation into deep neural networks to enhance their adaptability and plasticity. NeuMoSync extends standard neural network architectures with learnable feature vectors for each neuron that track network-wide historical context and with a module operating at a higher level of abstraction. This module synthesizes neuron-specific signals, conditioned on both current inputs and the network's evolving state, to adaptively regulate activation dynamics and synaptic plasticity. Evaluated on diverse CL benchmarks, including memorization (Random Label CIFAR-10 and Random Label MNIST), concept drift (Shuffle CIFAR-10 and Shuffle Mini-ImageNet), class-incremental learning (Class Split ImageNet and Class Split CIFAR-100), and domain-incremental learning (Permuted MNIST), NeuMoSync demonstrates strong performance in retaining plasticity and achieves improvements in both forward and backward adaptation compared with existing methods. Ablation studies validate the necessity of each component, while analysis of the learned modulatory signals reveals interpretable coordination patterns across tasks. Our work underscores the potential of integrating global coordination mechanisms into deep learning systems to advance robust, adaptive continual learning. The code is publicly available at this https URL.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.