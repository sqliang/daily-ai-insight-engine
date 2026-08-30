---
title: SAREF-based Ontology for Distributed AI Workflows across the Edge-Fog-Cloud
  Continuum
source: https://arxiv.org/abs/2608.26160
author:
- '[[Viorica Rozina Chifu, Tudor Cioara, Vasile Ofrim, Liana Toderean, Ionut Anghel,
  Laura Daniele, Cornelis Bouter]]'
published: '2026-08-28'
created: '2026-08-28'
manifest_dates:
- '2026-08-28'
description: 'arXiv:2608.26160v1 Announce Type: new Abstract: Nowadays semantic models
  provide limited support for representing distributed AI workflows and their execution
  across heterogeneous edge, fog, and cloud environments. Therefore, AI processes
  and resources are often described using incompatible semantic representations, affecting
  the interoperability, orchestration, and reuse. To address these challenges, this
  paper proposes a SAREF-compliant ontology for representing distributed AI workflows
  across the edge-fog-cloud continuum. We extend the SAREF4SYST ontology with concepts
  for modeling AI pipelines, executable AI jobs, computational resources, deployment
  constraints, and communication relationships, providing a unified semantic model
  of both AI workflows and heterogeneous computing infrastructures. The ontology enables
  semantic interoperability, automated reasoning, and resource-aware orchestration
  of distributed AI applications while remaining fully aligned with the ETSI SAREF
  ecosystem. The ontology is evaluated using proof-of-concept smart grid energy services
  orchestration scenarios and validated using competency questions showing its ability
  to support AI workflow deployment, execution reasoning, and workload adaptation
  across heterogeneous edge, fog, and cloud environments. All competency questions
  were successfully validated using SPARQL querying and semantic reasoning. Experimental
  results demonstrate deployment success rates of 90-100% with average orchestration
  decision times below 80 ms across heterogeneous edge-fog-cloud environments, highlighting
  its effectiveness on ensuring semantic interoperability for distributed AI orchestration.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 53e4ec1cfa13a4ec
source_type: academic_paper
tldr: 论文提出一个符合ETSI SAREF标准的本体，用于跨边缘-雾-云连续体表示分布式AI工作流，扩展SAREF4SYST建模AI流水线、可执行作业与计算资源。实验显示部署成功率达90%至100%，平均编排决策时间低于80毫秒。
objective_summary: 该arXiv论文针对现有语义模型难以表示分布式AI工作流及其在异构边缘、雾和云环境中执行的问题，提出一个符合SAREF标准的本体。该本体扩展SAREF4SYST，引入AI流水线、可执行AI作业、计算资源、部署约束和通信关系的建模概念，实现AI工作流与异构基础设施的统一语义描述。研究团队用智能电网能源服务编排场景进行概念验证，通过SPARQL查询和语义推理成功验证全部能力问题。实验表明部署成功率达90%至100%，平均编排决策时间低于80毫秒。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - ETSI
  technologies:
  - SAREF
  - SAREF4SYST
  - SPARQL
  - Edge-Fog-Cloud
  key_people: []
key_logic_flow:
- 论文指出现有语义模型对分布式AI工作流及其在异构边缘、雾和云环境中的执行支持有限，导致AI流程与资源常用不兼容的语义表示，影响互操作性、编排与复用。
- 论文提出一个符合SAREF标准的本体，用于表示跨边缘-雾-云连续体的分布式AI工作流，并与ETSI SAREF生态系统完全对齐。
- 该本体在SAREF4SYST基础上扩展了AI流水线、可执行AI作业、计算资源、部署约束与通信关系的概念，提供AI工作流与异构计算基础设施的统一语义模型。
- 该本体支持语义互操作、自动推理与资源感知的编排，研究团队通过智能电网能源服务编排场景进行概念验证。
- 研究团队使用能力问题并通过SPARQL查询与语义推理完成验证，所有能力问题均成功通过。
- 实验结果显示部署成功率达90%至100%，平均编排决策时间低于80毫秒，证明其对分布式AI编排语义互操作的有效性。
object_mentions:
- object_type: paper
  name: SAREF-based Ontology for Distributed AI Workflows across the Edge-Fog-Cloud
    Continuum
  canonical_name: SAREF Ontology for Distributed AI Workflows
  url: https://arxiv.org/abs/2608.26160
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文提出一个符合ETSI SAREF标准的本体，用于表示跨边缘-雾-云连续体的分布式AI工作流，以解决语义互操作与编排问题。
  - 实验结果显示该本体在异构边缘-雾-云环境中部署成功率达90%至100%，平均编排决策时间低于80毫秒。
  article_id: 53e4ec1cfa13a4ec
- object_type: project
  name: SAREF4SYST
  canonical_name: SAREF4SYST
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 论文在SAREF4SYST本体基础上扩展建模AI流水线、可执行AI作业、计算资源、部署约束与通信关系的概念，形成统一语义模型。
  article_id: 53e4ec1cfa13a4ec
- object_type: project
  name: ETSI SAREF
  canonical_name: SAREF
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 该本体完全对齐ETSI SAREF生态体系，通过SPARQL查询与语义推理成功验证了全部能力问题。
  article_id: 53e4ec1cfa13a4ec
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:SAREF-based Ontology for Distributed AI Workflows across the Edge-Fog-Cloud Continuum

View PDFAbstract:Nowadays semantic models provide limited support for representing distributed AI workflows and their execution across heterogeneous edge, fog, and cloud environments. Therefore, AI processes and resources are often described using incompatible semantic representations, affecting the interoperability, orchestration, and reuse. To address these challenges, this paper proposes a SAREF-compliant ontology for representing distributed AI workflows across the edge-fog-cloud continuum. We extend the SAREF4SYST ontology with concepts for modeling AI pipelines, executable AI jobs, computational resources, deployment constraints, and communication relationships, providing a unified semantic model of both AI workflows and heterogeneous computing infrastructures. The ontology enables semantic interoperability, automated reasoning, and resource-aware orchestration of distributed AI applications while remaining fully aligned with the ETSI SAREF ecosystem. The ontology is evaluated using proof-of-concept smart grid energy services orchestration scenarios and validated using competency questions showing its ability to support AI workflow deployment, execution reasoning, and workload adaptation across heterogeneous edge, fog, and cloud environments. All competency questions were successfully validated using SPARQL querying and semantic reasoning. Experimental results demonstrate deployment success rates of 90-100% with average orchestration decision times below 80 ms across heterogeneous edge-fog-cloud environments, highlighting its effectiveness on ensuring semantic interoperability for distributed AI orchestration.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.