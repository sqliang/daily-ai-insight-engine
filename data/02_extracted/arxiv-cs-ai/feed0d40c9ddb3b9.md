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
tldr: FirstResearch 提出可审计的研究问题证书框架，让 LLM 科学发现 Agent 的问题生成过程透明可核查。
objective_summary: 该论文提出 FirstResearch 框架，通过结构化"研究问题证书"记录定义、假设、机制、矛盾、可证伪假设等要素，使 LLM
  生成的科研问题可审计。在 10 个研究主题上，该框架以 4.86/5 分优于基线方法（最高 4.38），但结果基于 LLM 评判而非人类专家评审。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - DeepSeek
  - Google
  technologies:
  - LLM
  - Research Question Certificate
  key_people: []
key_logic_flow:
- LLM 科学发现系统在提出研究问题时缺乏可审计性，问题看似合理但无法暴露其机制、可证伪条件和假设。
- FirstResearch 框架的核心是结构化的研究问题证书，包含原始定义、假设、机制模型、矛盾/张力、可证伪假设、最小决定性测试和失败更新规则七要素。
- 在 10 个 LLM Agent 研究主题上，FirstResearch 在 DeepSeek 盲评协议下优于 AI co-scientist、Agent Laboratory
  和 AI Scientist-v2 等基线方法。
- Gemini-2.5-Flash 独立重评保留了相同排名，FirstResearch 得分 4.86/5，最强基线 4.38/5，Pearson 一致性 0.865。
- 消融实验表明证书核心是最强组件：仅证书方案达 4.90/5，移除证书后评分降至 1/5 以下。
- 研究结果具有初步性，使用 LLM 评判而非人类领域专家，但表明显式推导约束是提升 LLM 科研问题可审计性的有效机制。
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