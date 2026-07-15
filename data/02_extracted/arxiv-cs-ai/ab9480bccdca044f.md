---
title: Automated Data Readiness for Scientific AI
source: https://arxiv.org/abs/2607.02771
author:
- '[[Sean R. Wilkinson, Valentine G. Anantharaj, Jong Youl Choi, Ketan Maheshwari,
  Marshall McDonnell, Massimiliano Lupo Pasini, Polina Shpilker, Renan Souza, Patrick
  Widener, Sarp Oral, Wesley Brewer]]'
published: '2026-07-07'
created: '2026-07-07'
description: 'arXiv:2607.02771v1 Announce Type: new Abstract: Leadership computing
  facilities steward large-scale scientific datasets that routinely require substantial
  transformation before serving as AI training data. However, no existing framework
  fully unifies automated transformation, readiness assessment, provenance tracking,
  and agent-native deployment. We present REDI, an open-source framework that addresses
  this gap through a unified five-stage pipeline (ingest, preprocess, transform, structure,
  and output) with per-stage instrumentation for reproducibility and deployment as
  an agent-callable skill; companion tool SetGo automates FAIR compliance and catalog
  publication. Evaluated across climate, proteomics, materials science, and nuclear
  fusion, REDI transforms all datasets from raw to AI-ready, with outputs validated
  against domain-expert references, and preliminary results show near-ideal parallel
  scaling to 100 nodes on Frontier for the climate case. Provenance-instrumented profiling
  reveals file I/O as the dominant pipeline cost, with format selection a first-order
  optimization lever. These results establish REDI as a cross-domain platform providing
  automated data readiness for scientific AI, transforming data preparation bottlenecks
  into reproducible, reusable community assets.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ab9480bccdca044f
manifest_dates:
- '2026-07-07'
source_type: academic_paper
tldr: REDI 是开源科学 AI 数据准备框架，通过五阶段流水线自动化数据集转换与就绪度评估。
objective_summary: 作者提出 REDI 开源框架，通过五阶段流水线（摄取、预处理、变换、结构、输出）自动化科学数据集的 AI 就绪度评估与转换，并配套
  SetGo 工具实现 FAIR 合规。在气候、蛋白质组学、材料科学和核聚变四个领域验证了全量数据转换成功，在 Frontier 超算上实现百节点近理想并行扩展。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - REDI
  - SetGo
  - FAIR
  key_people: []
key_logic_flow:
- 作者提出了 REDI，一个统一的开源框架，通过五阶段流水线（摄取、预处理、变换、结构、输出）实现科学数据集从原始格式到 AI 训练就绪的自动化转换。
- REDI 支持每个阶段的溯源仪器化以保证可重复性，并可作为智能体可调用的技能进行部署。
- 配套工具 SetGo 实现了 FAIR（可发现、可访问、可互操作、可复用）数据原则的自动化合规检查和目录发布。
- REDI 在气候科学、蛋白质组学、材料科学和核聚变四个领域进行了评估，所有数据集均成功从原始格式转换为 AI 就绪格式，且输出结果通过领域专家参考数据验证。
- 初步实验结果显示在 Frontier 超算上气候数据用例达到近理想的百节点并行扩展性能。
- 溯源仪器化分析揭示文件 I/O 是流水线的主要成本瓶颈，数据格式选择是首要优化杠杆。
specialized_tags:
  paper:
    paperTitle: Automated Data Readiness for Scientific AI
    authors: []
    affiliations: []
    venue: arXiv preprint
    codeUrl: null
    datasetUrl: null
    researchArea: Systems
    methodType: empirical
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Automated Data Readiness for Scientific AI

View PDF HTML (experimental)Abstract:Leadership computing facilities steward large-scale scientific datasets that routinely require substantial transformation before serving as AI training data. However, no existing framework fully unifies automated transformation, readiness assessment, provenance tracking, and agent-native deployment. We present REDI, an open-source framework that addresses this gap through a unified five-stage pipeline (ingest, preprocess, transform, structure, and output) with per-stage instrumentation for reproducibility and deployment as an agent-callable skill; companion tool SetGo automates FAIR compliance and catalog publication. Evaluated across climate, proteomics, materials science, and nuclear fusion, REDI transforms all datasets from raw to AI-ready, with outputs validated against domain-expert references, and preliminary results show near-ideal parallel scaling to 100 nodes on Frontier for the climate case. Provenance-instrumented profiling reveals file I/O as the dominant pipeline cost, with format selection a first-order optimization lever. These results establish REDI as a cross-domain platform providing automated data readiness for scientific AI, transforming data preparation bottlenecks into reproducible, reusable community assets.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.