---
title: 'FirstResearch: Auditable Question Formation for LLM Scientific Discovery Agents'
source: https://arxiv.org/abs/2607.05682
author:
- '[[Yufeng Wang]]'
published: '2026-07-08'
created: '2026-07-08'
description: 'arXiv:2607.05682v1 Announce Type: new Abstract: LLM systems for scientific
  discovery increasingly assist with ideation, literature synthesis, experiment planning,
  and report generation, but the first research question they propose can remain difficult
  to audit: it may sound plausible without exposing the mechanism, falsifier, or assumption
  that a scientist should inspect. We introduce FirstResearch, a first-principles
  research-question formation framework for scientific LLM agents whose core artifact
  is a structured Research Question Certificate. The certificate records primitive
  definitions, assumptions, a mechanism model, a tension or contradiction, a falsifiable
  hypothesis, a minimal decisive test, and a failure update rule, making the proposed
  question inspectable before downstream execution. On ten LLM-agent research topics,
  FirstResearch outperforms controlled prompt-level baselines inspired by AI co-scientist,
  Agent Laboratory, and AI Scientist-v2 under a primary DeepSeek-blind-judge protocol.
  A Gemini-2.5-Flash independent-judge rescore of the same 40 baseline packages preserves
  the system-level ranking, with FirstResearch scoring 4.86/5 versus 4.38/5 for the
  strongest baseline and Pearson agreement of 0.865 on average score. A one-repeat
  ablation checkpoint further suggests that the certificate-centered core is the strongest
  component: certificate-only scoring reaches 4.90/5 under DeepSeek and 4.88/5 under
  Gemini, while removing certificates drops below 1/5 under both judges. These results
  are preliminary and use LLM judges rather than human domain experts, but they support
  a narrow scientific-discovery claim: explicit derivation constraints are a promising
  mechanism for making LLM-generated scientific questions more auditable. Code, prompts,
  saved outputs, and reproduction scripts are available at https://github.com/louiswang524/FirstResearch.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: feed0d40c9ddb3b9
manifest_dates:
- '2026-07-08'
source_type: academic_paper
tldr: FirstResearch 是一个面向科学发现 LLM 代理的研究问题形成框架，通过结构化"研究问题证书"记录原始定义、假设、机制模型和可证伪假设，使问题在下游执行前可被审计。在十个主题上的实验显示其得分（4.86/5）优于
  AI co-scientist 等基线方法。
objective_summary: 研究人员提出了 FirstResearch，一个基于一阶原理的科学问题生成框架，专为 LLM 驱动的科学发现代理设计。该框架的核心产出是"研究问题证书"，包含原始定义、假设、机制模型、张力矛盾、可证伪假设、最小决定性测试和失败更新规则七项结构化内容。在十个
  LLM 代理研究主题上，FirstResearch 在 DeepSeek 盲评审协议下优于 AI co-scientist、Agent Laboratory 和
  AI Scientist-v2 等基线方法，Gemini-2.5-Flash 独立重评也确认了该排名（4.86/5 vs 最强基线 4.38/5，Pearson
  一致性 0.865）。消融实验显示证书机制是最强组件，去除证书后得分降至 1/5 以下。结果尚属初步且使用 LLM 评审而非人类专家。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - DeepSeek
  - Google
  technologies:
  - LLM
  - FirstResearch
  - AI co-scientist
  - Agent Laboratory
  - AI Scientist-v2
  - Gemini-2.5-Flash
  key_people: []
key_logic_flow:
- FirstResearch 是一个面向科学发现 LLM 代理的一阶研究问题形成框架，其核心产出是结构化的"研究问题证书"。
- 该证书记录了原始定义、假设、机制模型、张力或矛盾、可证伪假设、最小决定性测试和失败更新规则七项内容，使提出的问题在下游执行前可被科学家检查。
- 在十个 LLM 代理研究主题上，FirstResearch 在 DeepSeek 盲评审协议下优于 AI co-scientist、Agent Laboratory
  和 AI Scientist-v2 等基线方法。
- Gemini-2.5-Flash 独立评审对相同 40 个基线包的重新评分保持了系统级排名，FirstResearch 得分为 4.86/5，最强基线得分为 4.38/5，Pearson
  一致性达 0.865。
- 消融实验表明仅使用证书核心即可达到 4.90/5（DeepSeek）和 4.88/5（Gemini），而去除证书后得分降至 1/5 以下。
- 这些结果尚属初步阶段且使用 LLM 评审而非人类领域专家，但表明显式推导约束是让 LLM 生成科学问题更具可审计性的有前景机制。
specialized_tags:
  paper:
    paperTitle: 'FirstResearch: Auditable Question Formation for LLM Scientific Discovery
      Agents'
    authors: []
    affiliations: []
    venue: arXiv preprint
    codeUrl: null
    datasetUrl: null
    researchArea: Other
    methodType: LLM-based
extract_result: success
object_mentions:
- object_type: paper
  name: 'FirstResearch: Auditable Question Formation for LLM Scientific Discovery
    Agents'
  canonical_name: FirstResearch
  url: https://arxiv.org/abs/2607.05682
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - FirstResearch 是一个面向科学发现 LLM 代理的一阶研究问题形成框架，其核心产出是结构化的研究问题证书。
  - 在十个 LLM 代理研究主题上，FirstResearch 在 DeepSeek 盲评审协议下优于 AI co-scientist、Agent Laboratory
    和 AI Scientist-v2 等基线方法。
  - 消融实验表明仅使用证书核心即可达到 4.90/5（DeepSeek）和 4.88/5（Gemini），而去除证书后得分降至 1/5 以下。
  article_id: feed0d40c9ddb3b9
- object_type: project
  name: Research Question Certificate
  canonical_name: Research Question Certificate
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 研究问题证书记录了原始定义、假设、机制模型、张力或矛盾、可证伪假设、最小决定性测试和失败更新规则七项内容。
  - 消融实验表明证书机制是 FirstResearch 的最强组件，仅使用证书即可保持最高评分。
  article_id: feed0d40c9ddb3b9
---

# Computer Science > Artificial Intelligence

# Title:FirstResearch: Auditable Question Formation for LLM Scientific Discovery Agents

View PDF HTML (experimental)Abstract:LLM systems for scientific discovery increasingly assist with ideation, literature synthesis, experiment planning, and report generation, but the first research question they propose can remain difficult to audit: it may sound plausible without exposing the mechanism, falsifier, or assumption that a scientist should inspect. We introduce FirstResearch, a first-principles research-question formation framework for scientific LLM agents whose core artifact is a structured Research Question Certificate. The certificate records primitive definitions, assumptions, a mechanism model, a tension or contradiction, a falsifiable hypothesis, a minimal decisive test, and a failure update rule, making the proposed question inspectable before downstream execution. On ten LLM-agent research topics, FirstResearch outperforms controlled prompt-level baselines inspired by AI co-scientist, Agent Laboratory, and AI Scientist-v2 under a primary DeepSeek-blind-judge protocol. A Gemini-2.5-Flash independent-judge rescore of the same 40 baseline packages preserves the system-level ranking, with FirstResearch scoring 4.86/5 versus 4.38/5 for the strongest baseline and Pearson agreement of 0.865 on average score. A one-repeat ablation checkpoint further suggests that the certificate-centered core is the strongest component: certificate-only scoring reaches 4.90/5 under DeepSeek and 4.88/5 under Gemini, while removing certificates drops below 1/5 under both judges. These results are preliminary and use LLM judges rather than human domain experts, but they support a narrow scientific-discovery claim: explicit derivation constraints are a promising mechanism for making LLM-generated scientific questions more auditable. Code, prompts, saved outputs, and reproduction scripts are available at this https URL.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.