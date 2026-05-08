---
title: 'SensingAgents: A Multi-Agent Collaborative Framework for Robust IMU Activity
  Recognition'
source: https://arxiv.org/abs/2605.04608
author:
- '[[Naiyu Zheng, Tianlong Yu, Haochen Yin, Xiaoyi Fan, Xiping Hu, Zhimeng Yin]]'
published: '2026-05-07'
created: '2026-05-08'
description: 'arXiv:2605.04608v1 Announce Type: new Abstract: Human Activity Recognition
  (HAR) using Inertial Measurement Unit (IMU) sensors is a cornerstone of mobile health,
  smart environments, and human-computer interaction. However, current deep learning-based
  HAR models often struggle with heavy reliance on labeled data, position-specific
  ambiguity, and a lack of transparent reasoning. Inspired by the advanced agents
  framework, which emulates a collaborative agent using Large Language Models (LLMs),
  we propose SensingAgents, a novel multi-agent system for robust IMU activity recognition.
  SensingAgents organizes LLM-powered agents into specialized roles: a group of Analyst
  Agents for position-specific sensor analysis (arm, wrist, belt, pocket), a pair
  of Advocate Agents that resolves sensor conflicts through dynamic and static dialectical
  debates, and a Decision Agent that ensures reliability under sensor drift or failure.
  Evaluation on the Shoaib dataset demonstrates that SensingAgents significantly outperforms
  state-of-the-art single-agent and multi-agent LLM models, achieving an accuracy
  of 79.5% in a zero setting--29% higher than existing agent models and 9.4% higher
  than deep learning baselines--particularly in complex scenarios where multi-sensor
  data is conflicting or noisy. Our work highlights the potential of multi-agent collaborative
  reasoning for advancing the robustness and interpretability of ubiquitous sensing
  systems.'
tags:
- clippings
id: 8acd50b7cfaac637
source_type: academic_paper
tldr: SensingAgents 提出多智能体协作框架，通过 LLM 驱动的角色分工解决 IMU 活动识别的传感器冲突问题，零样本准确率达 79.5%。
objective_summary: 研究团队提出 SensingAgents，一个多智能体协作系统，将 LLM 智能体分为分析师、倡导者和决策者三种角色，用于鲁棒的
  IMU 人体活动识别。在 Shoaib 数据集上零样本准确率达 79.5%，比现有智能体模型高 29%，比深度学习基线高 9.4%。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - IMU
  - HAR
  - LLM
  - Multi-Agent System
  key_people: []
key_logic_flow:
- SensingAgents 提出了一个多智能体协作框架，专门用于基于 IMU 传感器数据的人体活动识别（HAR）任务。
- 框架将 LLM 驱动的智能体分为三类角色：分析师智能体按传感器佩戴位置（手臂、手腕、腰带、口袋）进行特定分析；倡导智能体通过动态和静态辩证辩论解决多传感器之间的冲突；决策智能体在传感器漂移或故障时保证识别的可靠性。
- 在 Shoaib 数据集上的零样本评估中，SensingAgents 达到 79.5% 的准确率，比现有单智能体和多智能体 LLM 模型高出 29 个百分点，比传统深度学习基线高出
  9.4 个百分点。
- 该方法特别适用于多传感器数据冲突或存在噪声的复杂场景，展示了多智能体协作推理在提升可穿戴传感系统鲁棒性和可解释性方面的潜力。
---

# Computer Science > Artificial Intelligence

# Title:SensingAgents: A Multi-Agent Collaborative Framework for Robust IMU Activity Recognition

View PDF HTML (experimental)Abstract:Human Activity Recognition (HAR) using Inertial Measurement Unit (IMU) sensors is a cornerstone of mobile health, smart environments, and human-computer interaction. However, current deep learning-based HAR models often struggle with heavy reliance on labeled data, position-specific ambiguity, and a lack of transparent reasoning. Inspired by the advanced agents framework, which emulates a collaborative agent using Large Language Models (LLMs), we propose SensingAgents, a novel multi-agent system for robust IMU activity recognition. SensingAgents organizes LLM-powered agents into specialized roles: a group of Analyst Agents for position-specific sensor analysis (arm, wrist, belt, pocket), a pair of Advocate Agents that resolves sensor conflicts through dynamic and static dialectical debates, and a Decision Agent that ensures reliability under sensor drift or failure. Evaluation on the Shoaib dataset demonstrates that SensingAgents significantly outperforms state-of-the-art single-agent and multi-agent LLM models, achieving an accuracy of 79.5% in a zero setting--29% higher than existing agent models and 9.4% higher than deep learning baselines--particularly in complex scenarios where multi-sensor data is conflicting or noisy. Our work highlights the potential of multi-agent collaborative reasoning for advancing the robustness and interpretability of ubiquitous sensing systems.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.