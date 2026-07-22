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
tldr: arXiv 论文提出 REDI 开源框架，通过统一五阶段管道实现科学数据集到 AI 训练数据的自动化转换，并配套 SetGo 工具实现 FAIR 合规；在气候、蛋白质组学、材料科学和核聚变四个领域验证了有效性。
objective_summary: 这篇发表于 arXiv 的论文提出了 REDI，一个开源的自动化数据准备框架，通过统一五阶段管道（摄取、预处理、变换、结构化和输出）将大规模科学数据集自动转换为
  AI 训练数据。每个阶段都配备了可重复性仪表化记录，并支持作为智能体可调用技能部署。配套工具 SetGo 用于自动化 FAIR 合规和目录发布。研究团队在气候、蛋白质组学、材料科学和核聚变四个领域进行了评估，所有数据集均成功从原始状态转换至
  AI 可用状态，输出结果经领域专家参考标准验证，且在 Frontier 超级计算机上展示了接近理想的 100 节点并行扩展能力。文件 I/O 被识别为管道的主要瓶颈，格式选择成为关键优化手段。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - REDI
  - SetGo
  - FAIR
  - AI training
  - parallel computing
  key_people: []
key_logic_flow:
- 现有框架无法统一实现自动化转换、就绪评估、溯源追踪和智能体原生部署，这是一个关键空白。
- REDI 通过五阶段管道（摄取、预处理、变换、结构化和输出）填补了这一空白，每阶段都包含可重复性的仪表化记录。
- 配套工具 SetGo 用于自动化 FAIR 合规检查和数据目录发布。
- 在气候、蛋白质组学、材料科学和核聚变四个科学领域验证了 REDI 的有效性，所有数据集均从原始状态成功转换为 AI 可用状态。
- 在 Frontier 超级计算机的气候场景测试中，REDI 展现了接近理想的 100 节点并行扩展能力。
- 文件 I/O 被确定为管道的主要性能瓶颈，格式选择成为首要优化杠杆。
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
object_mentions:
- object_type: project
  name: REDI
  canonical_name: REDI
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - REDI 是一个统一五阶段管道的开源框架，涵盖数据摄取、预处理、变换、结构化和输出阶段。
  - REDI 每阶段都配备可重复性仪表化记录，并支持作为智能体可调用技能进行部署。
  - 在 Frontier 超级计算机上，REDI 在气候场景中展现了接近理想的 100 节点并行扩展能力。
  article_id: ab9480bccdca044f
- object_type: project
  name: SetGo
  canonical_name: SetGo
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - SetGo 是 REDI 的配套工具，用于自动化 FAIR 合规性检查和数据目录发布。
  article_id: ab9480bccdca044f
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