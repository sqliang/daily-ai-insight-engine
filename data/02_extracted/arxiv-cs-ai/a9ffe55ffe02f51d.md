---
title: CFD-Guided Detection of Concept Drift in Multimodal Physiologic Signals
source: https://arxiv.org/abs/2608.07759
author:
- '[[Farouk Ganiyu Adewumi, Timothy Oladunni, Rochak Ghimire, Kosisochukwu Ogbuanya,
  Sanaa Reeves, Sandy Akoy]]'
published: '2026-08-12'
created: '2026-08-12'
manifest_dates:
- '2026-08-12'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: a9ffe55ffe02f51d
source_type: academic_paper
tldr: arXiv 论文提出 PECS 生理信号稳定性框架，通过对比模型内部变化与 ECG/PPG/呼吸信号的可测量变化来检测可穿戴心电 AI 的概念漂移，并在
  BIDMC 与 MIMIC 数据集上分别达到 0.8786 和 0.9560 的漂移分类准确率。
objective_summary: 研究者针对可穿戴心电 AI 在真实环境中受运动、呼吸、姿势、传感器接触和临床恶化影响而产生信号分布变化的问题，提出了 PECS
  框架。该框架以心电图（ECG）为主信号，光电容积脉搏波（PPG）提供脉搏与血管信息，仅在 ECG 与 PPG 不一致时引入呼吸信号。研究在 PTB-XL（试点与全量）、BIDMC
  和 MIMIC 波形队列上验证，发现跨模态信号组合需根据数据规模与场景选择，并非越多越好。PECS 在扩展 BIDMC 上达到 0.8786 的漂移分类准确率，在
  MIMIC 上达到 0.9560，优于所评估的基线方法。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - PECS
  - ECG
  - PPG
  - respiration signal
  - concept drift detection
  - multimodal physiologic signals
  - wearable cardiovascular AI
  key_people: []
key_logic_flow:
- 可穿戴心血管 AI 的真实 ECG 信号会因运动、呼吸、姿势、传感器接触和临床状态变化而出现分布漂移。
- 论文提出 PECS 框架，通过比较模型内部变化与信号的可测量变化来决定是否保持、更改或标记不确定性预测。
- PECS 以 ECG 为主信号，PPG 为辅信号，仅在 ECG 与 PPG 不一致时引入呼吸信号。
- 在 PTB-XL 试点与全量分析、BIDMC 和 MIMIC 波形队列上的实验表明，最优跨模态信号组合随数据规模与场景变化。
- PECS 的漂移分类准确率在扩展 BIDMC 上为 0.8786，在 MIMIC 上为 0.9560，超过所评估的漂移检测基线实现。
object_mentions:
- object_type: paper
  name: CFD-Guided Detection of Concept Drift in Multimodal Physiologic Signals
  canonical_name: CFD-Guided Detection of Concept Drift in Multimodal Physiologic
    Signals
  url: https://arxiv.org/abs/2608.07759
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文标题为《CFD-Guided Detection of Concept Drift in Multimodal Physiologic Signals》，摘要提出
    PECS 框架并报告了在多个数据集上的验证结果。
  article_id: a9ffe55ffe02f51d
- object_type: project
  name: PECS
  canonical_name: PECS
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - PECS 被定义为一种生理信号稳定性框架，用于比较模型内部变化与 ECG、PPG、呼吸信号的可测量变化，以判断是否保留、修改或标记预测。
  article_id: a9ffe55ffe02f51d
- object_type: dataset
  name: PTB-XL
  canonical_name: PTB-XL
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 研究在 PTB-XL 的试点和全量分析中测试了 PECS，并发现不同数据规模下选出的域对存在差异。
  article_id: a9ffe55ffe02f51d
- object_type: dataset
  name: BIDMC
  canonical_name: BIDMC waveform cohort
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - PECS 在扩展 BIDMC 波形队列上达到 0.8786 的漂移分类准确率。
  article_id: a9ffe55ffe02f51d
- object_type: dataset
  name: MIMIC
  canonical_name: MIMIC waveform cohort
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - PECS 在 MIMIC 波形队列上取得 0.9560 的漂移分类准确率，并用于评估呼吸信号在 ECG 与 PPG 分歧场景中的作用。
  article_id: a9ffe55ffe02f51d
extract_result: success
---

# Electrical Engineering and Systems Science > Signal Processing

# Title:CFD-Guided Detection of Concept Drift in Multimodal Physiologic Signals

View PDF HTML (experimental)Abstract:Cardiovascular AI models can classify clean elec- trocardiogram (ECG) signals, but real wearable signals change because of motion, breathing, posture, sensor contact, and true clinical deterioration. This paper asks when a model should keep its prediction, change it, or flag uncertainty. We propose a physiologic stability framework, called PECS, that compares changes inside the model with measurable changes in the signal. ECG is treated as the main cardiac signal, photoplethysmography (PPG) adds pulse and vascular information, and respiration is used only when ECG and PPG disagree. We test the framework on PTB-XL at pilot and full scales and on synchronized BIDMC and MIMIC waveform cohorts. The PTB-XL pilot and full- scale analyses selected different domain pairs, and the strongest cross-modal pair also changed across BIDMC and MIMIC, showing that adding every available signal is not always the best choice. PECS outperformed the evaluated drift-detection baseline implementations, reaching drift classification accuracy (DCA) of 0.8786 on expanded BIDMC and 0.9560 on MIMIC. The MIMIC results also showed that respiration can help during disagreement cases, but it should be used selectively rather than as an automatic override. Overall, the results support PECS as a candidate monitoring framework for wearable cardiovascular AI while highlighting the need for scale-aware domain selection and interpretable trust routing

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.