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
tldr: 论文证明聚合指标会错误排序科学候选方案，提出搜索纪律协议作为外部控制循环
objective_summary: arXiv 发表论文，证明当科学有效性是多维的但验证仅使用单一聚合指标时，聚合指标可能将科学上无效的候选方案排在第一位。作者在生态系统人口统计模型的火任务上演示了该反转现象，并提出搜索纪律协议作为外部控制循环，在代理决策后审计候选方案的分解行为。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies: []
  key_people: []
key_logic_flow:
- 自主研究代理使用聚合指标来评估科学候选方案，但当科学有效性存在于分解结构中时，聚合指标可能将错误的候选方案排在第一位。
- 指标提升的同时底层结构可能发生反转，导致基于该指标做出的决策接受了一个暗中破坏模型的候选方案。
- 作者在生态系统人口统计模型（Ecosystem Demography model）的火任务上演示了这一反转现象：全局分数接近的两个候选方案中，高分方案导致受保护的北方森林区域崩溃，而次优方案则保全了它们。
- 论文指出不应将最终决策权交给生成候选方案的代理，因为优化分数的代理最不可能发现分数本身的错误。
- 建议将决策移至外部控制循环，在代理决策后审计每个候选方案的分解行为，可以降级代理本应接受的候选方案，也可以重新打开代理已声明完成的运行。
- 该论文的核心贡献是发现了聚合指标反转现象本身，并提出了基于可审查的候选效果证据而非分数进行决策的搜索纪律协议。
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