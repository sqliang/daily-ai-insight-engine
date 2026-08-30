---
title: A Multi-Agent Framework for Automated Coarse-Grained Molecular Dynamics of
  Polymers
source: https://arxiv.org/abs/2608.06694
author:
- '[[Joohee Choi, Junhyeong Lee, Seunghwa Ryu]]'
published: '2026-08-10'
created: '2026-08-10'
manifest_dates:
- '2026-08-10'
description: 'arXiv:2608.06694v1 Announce Type: new Abstract: Coarse-grained (CG)
  molecular dynamics extends polymer simulation beyond the scales accessible to all-atom
  (AA) methods, but bottom-up CG modeling is laborious. The CG resolution is a design
  choice, so a transferable parameter set is generally not available and the potentials
  are derived anew for each polymer mapping. Here we present CGMas, a multi-agent
  framework that automates topology construction, equilibration, mapping, potential
  derivation, and validation from a natural-language specification of the polymer
  and target resolution. A large-language-model (LLM) reasoning agent infers the AA
  topology from polymer name, while layered self-correction resolves physical errors
  common to unsaturated, heteroatom-containing, and polar polymers. Downstream agents
  equilibrate the system, map it onto CG representation, derive potentials through
  Boltzmann inversion, and benchmark the model against its atomistic reference. CGMas
  completed all 27 homopolymer and copolymer tasks, matched the AA density to within
  5% in 22, and reduced simulation from 38-88 min to 1 min, establishing agentic LLMs
  as a route to automated polymer coarse-graining.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: d7d0dac2abf3d0a6
source_type: academic_paper
tldr: 介绍 CGMas，一个基于大语言模型的多智能体框架，可从聚合物的自然语言描述自动完成粗粒化分子动力学的建模全流程。它完成全部 27 个均聚物与共聚物任务，其中
  22 个密度与全原子参考误差在 5% 以内，并将模拟耗时从 38-88 分钟压缩至约 1 分钟。
objective_summary: CGMas 是一个自动化的聚合物粗粒化分子动力学建模多智能体框架，相关论文发表于 arXiv（编号 2608.06694）。它由大语言模型推理智能体根据聚合物名称推断全原子拓扑结构，并采用分层自纠正机制解决不饱和、含杂原子和极性聚合物的常见物理错误。下游智能体依次完成系统平衡、粗粒化映射、玻尔兹曼反演势能推导以及相对全原子参考的基准验证。实验结果显示，CGMas
  成功完成全部 27 个均聚物与共聚物任务，其中 22 个任务密度与全原子参考偏差在 5% 以内，并将建模时间从 38-88 分钟缩短至约 1 分钟。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Coarse-Grained Molecular Dynamics
  - LLM
  - Boltzmann inversion
  - all-atom simulation
  - homopolymer
  - copolymer
  key_people: []
key_logic_flow:
- 粗粒化分子动力学虽能超越全原子方法扩展聚合物模拟尺度，但自下而上的粗粒化建模过程繁琐，需要针对每种聚合物映射重新推导势能参数。
- CGMas 框架由大语言模型推理智能体根据聚合物名称推断全原子拓扑结构，并采用分层自纠正机制处理不饱和、含杂原子和极性聚合物的物理错误。
- 下游智能体依次执行系统平衡、映射到粗粒化表示、通过玻尔兹曼反演推导势能，以及与全原子参考模型进行基准对比验证。
- 实验覆盖 27 个均聚物与共聚物任务，其中 22 个任务的密度与全原子参考值偏差在 5% 以内。
- CGMas 将单次建模时间从 38-88 分钟缩短至约 1 分钟，验证了智能体大语言模型作为自动化聚合物粗粒化路线的可行性。
object_mentions:
- object_type: project
  name: CGMas
  canonical_name: CGMas
  url: https://arxiv.org/abs/2608.06694
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - CGMas 是一个多智能体框架，能够自动完成拓扑构建、平衡、映射、势能推导与验证等粗粒化建模流程。
  - 该框架从聚合物的自然语言描述出发推断全原子拓扑，并通过分层自纠正机制解决常见物理错误。
  - CGMas 完成了全部 27 个均聚物与共聚物任务，其中 22 个密度与全原子参考偏差在 5% 以内。
  article_id: d7d0dac2abf3d0a6
- object_type: paper
  name: A Multi-Agent Framework for Automated Coarse-Grained Molecular Dynamics of
    Polymers
  canonical_name: CGMas paper (arXiv 2608.06694)
  url: https://arxiv.org/abs/2608.06694
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文发表于 arXiv，编号 2608.06694，提出以智能体大语言模型实现自动化聚合物粗粒化建模的路线。
  - 该论文报告 CGMas 将模拟建模时间从 38-88 分钟降至约 1 分钟，并建立了智能体 LLM 用于聚合物粗粒化的可行性依据。
  article_id: d7d0dac2abf3d0a6
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:A Multi-Agent Framework for Automated Coarse-Grained Molecular Dynamics of Polymers

View PDF HTML (experimental)Abstract:Coarse-grained (CG) molecular dynamics extends polymer simulation beyond the scales accessible to all-atom (AA) methods, but bottom-up CG modeling is laborious. The CG resolution is a design choice, so a transferable parameter set is generally not available and the potentials are derived anew for each polymer mapping. Here we present CGMas, a multi-agent framework that automates topology construction, equilibration, mapping, potential derivation, and validation from a natural-language specification of the polymer and target resolution. A large-language-model (LLM) reasoning agent infers the AA topology from polymer name, while layered self-correction resolves physical errors common to unsaturated, heteroatom-containing, and polar polymers. Downstream agents equilibrate the system, map it onto CG representation, derive potentials through Boltzmann inversion, and benchmark the model against its atomistic reference. CGMas completed all 27 homopolymer and copolymer tasks, matched the AA density to within 5% in 22, and reduced simulation from 38-88 min to 1 min, establishing agentic LLMs as a route to automated polymer coarse-graining.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.