---
title: Search Discipline for Long-Horizon Research Agents
source: https://arxiv.org/abs/2606.11522
author:
- '[[Adithya Srinivasan, Devesh Paragiri]]'
published: '2026-06-11'
created: '2026-06-11'
description: 'arXiv:2606.11522v1 Announce Type: new Abstract: Autoresearch agents
  now propose, evaluate, and select scientific candidates against a metric, and that
  metric is usually an aggregate reduced over a heterogeneous space of regions, slices,
  or cohorts. We show that when scientific validity lives in that disaggregated structure,
  the aggregate can rank the wrong candidate first. The headline number improves while
  the structure underneath inverts, so a decision made on the number accepts a candidate
  that quietly breaks the model. The failure is not domain-specific. It appears wherever
  a candidate''s validity is multi-dimensional but its verifier is a single reduction.
  We demonstrate the inversion on a fire-model task in the Ecosystem Demography model.
  The highest-scoring candidate and a slightly lower one are within noise of each
  other on global score, yet the top-scoring one collapses the protected boreal regions
  while the other preserves them. What separates them is the per-region behavior,
  not the headline number. This decision should not be left to the agent that produced
  the candidates. The agent optimizing the score is the last party likely to catch
  the score being wrong, and a prompt has no remaining turn once the agent has stopped.
  We move the decision to an external control loop that audits each candidate on its
  disaggregated behavior and acts after the agent has decided. It can demote a candidate
  the agent would have accepted, and it can reopen a run the agent had declared finished.
  Our contribution is the inversion finding itself, and a search-discipline protocol
  that decides on reviewable candidate-effect evidence instead of the score.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: b8fefd5fda42649d
source_type: academic_paper
tldr: 该论文发现，在长周期自主研究智能体中，基于单一聚合指标对多维科学候选方案进行排名时，可能将结构上错误的候选方案排在首位，产生"全局分数提升但底层结构反转"的反直觉现象。作者提出将决策权转移至外部控制回路的"搜索纪律"协议，基于分组候选效果证据进行审计而非依赖聚合分数。
objective_summary: 来自 arXiv 的学术论文 Search Discipline for Long-Horizon Research Agents
  揭示了自主研究智能体在评估多维科学候选方案时的"聚合误导"问题：当验证指标是一个单一聚合值（如全局分数）而候选方案的有效性具有多维结构时，该聚合值可能将结构上错误的候选方案排在首位，使得全局分数看似提升但底层区域结构已然反转。研究者在生态系统人口模型（Ecosystem
  Demography model）的火灾模拟任务中验证了这一现象——全局得分最高的候选方案导致北方保护区崩溃，而得分稍低的方案却能保护这些区域。论文提出了一种"搜索纪律"协议，将决策权从生成候选方案的智能体转移至外部控制回路，由该审计环路基于分组候选效果证据而非聚合分数进行决策。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Ecosystem Demography model
  key_people: []
key_logic_flow:
- 论文指出，当自主研究智能体使用单一聚合指标评估多个科学候选方案时，该聚合指标可能将实际上结构错误的候选方案排在第一。
- 这种"聚合误导"具体表现为全局分数提升但底层区域结构发生反转，导致基于全局分数的决策可能默默破坏模型的有效性。
- 研究者在生态系统人口模型的火灾模拟任务中验证了该现象：全局得分最高的候选方案导致北方保护区崩溃，而得分稍低的方案却能保护这些区域。
- 论文认为这一决策不应由生成候选方案的同一智能体负责，因为优化聚合分数的智能体最不可能发现分数本身的错误。
- 论文提出"搜索纪律"协议（search-discipline protocol），将决策权移至外部控制回路，由该审计环路基于分组候选效果证据进行判断。
- 该外部控制回路可以降级智能体本应接受的候选方案，也可以重新开启智能体已声明完成的任务运行。
extract_result: success
object_mentions:
- object_type: paper
  name: Search Discipline for Long-Horizon Research Agents
  canonical_name: Search Discipline for Long-Horizon Research Agents
  url: https://arxiv.org/abs/2606.11522
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文发表在 arXiv 上，揭示了自主研究智能体在评估多维科学候选方案时使用单一聚合指标可能导致错误排名的"聚合误导"问题。
  - 论文的核心贡献是发现了聚合排名与底层结构反转之间的矛盾现象，并提出了一种名为"搜索纪律"的解决方案协议。
  - 研究者通过生态系统人口模型的火灾模拟任务，实证展示了全局分数看似正常但底层保护区域已被破坏的具体案例。
  article_id: b8fefd5fda42649d
- object_type: project
  name: search-discipline protocol
  canonical_name: Search Discipline Protocol
  url: null
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - 搜索纪律协议是一个外部控制回路，它在智能体完成决策后审计每个候选方案的分组行为，而非依赖单一聚合分数。
  - 该协议可以降级智能体本应接受的候选方案，也可以重新开启智能体已声明完成的任务。
  - 论文将搜索纪律定位为基于可审查的候选效果证据进行决策的机制，而非由生成候选方案的同一智能体自我评判。
  article_id: b8fefd5fda42649d
---

# Computer Science > Artificial Intelligence

# Title:Search Discipline for Long-Horizon Research Agents

View PDF HTML (experimental)Abstract:Autoresearch agents now propose, evaluate, and select scientific candidates against a metric, and that metric is usually an aggregate reduced over a heterogeneous space of regions, slices, or cohorts. We show that when scientific validity lives in that disaggregated structure, the aggregate can rank the wrong candidate first. The headline number improves while the structure underneath inverts, so a decision made on the number accepts a candidate that quietly breaks the model. The failure is not domain-specific. It appears wherever a candidate's validity is multi-dimensional but its verifier is a single reduction.

We demonstrate the inversion on a fire-model task in the Ecosystem Demography model. The highest-scoring candidate and a slightly lower one are within noise of each other on global score, yet the top-scoring one collapses the protected boreal regions while the other preserves them. What separates them is the per-region behavior, not the headline number.

This decision should not be left to the agent that produced the candidates. The agent optimizing the score is the last party likely to catch the score being wrong, and a prompt has no remaining turn once the agent has stopped. We move the decision to an external control loop that audits each candidate on its disaggregated behavior and acts after the agent has decided. It can demote a candidate the agent would have accepted, and it can reopen a run the agent had declared finished. Our contribution is the inversion finding itself, and a search-discipline protocol that decides on reviewable candidate-effect evidence instead of the score.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.