---
title: Memory Reward Inflation in Self-Improving LLM Agents
source: https://arxiv.org/abs/2608.00017
author:
- '[[Mohammad Asadolahi, Amir Amini, Samira Talebi, Amirfarhad Farhadi, Azadeh Zamanifar]]'
published: '2026-08-05'
created: '2026-08-05'
manifest_dates:
- '2026-08-05'
description: 'arXiv:2608.00017v1 Announce Type: new Abstract: Self-improving LLM agents
  increasingly learn from experience without updating any weights. Each episode is
  stored in an external memory, scored, and retrieved for similar future tasks to
  shape later behavior. Viewed through a reward lens, the stored score is a proxy
  reward for an implicit, non-parametric policy. Each retrieved episode then becomes
  a policy-improvement step whose reliability hinges on how that score is produced.
  In deployment, ground-truth labels are unavailable, so the stored reward is at best
  an LLM assessment. This substitution creates a failure mode, the *Echo Gap*, across
  the memory-based self-improving agents and model families studied. Incorrect episodes
  receive inflated rewards; thus, the agent preferentially reuses the very mistakes
  it has most confident in. Because the error compounds through memory rather than
  averaging out and the confirming judge''s errors remain correlated with the original
  self-grading bias, so it cannot identify which memories are overvalued. The missing
  property is formalized as the *Error-Independence Assumption* (EIA), which we prove
  is a *necessary* condition for correcting the inflation, not merely a description
  of a good verifier: a usable signal must track truth *and* decorrelate its error
  from the memory bias, and the recoverable payoff is a closed-form function of exactly
  those two quantities. We further show the inflation compounds not only when retrieval
  ranks by the stored score but also under plain similarity retrieval which is the
  regime the deployed agent uses. Finally, the answer-free de-inflation algorithm
  LUCID delivers a consistent end-to-end gain on the BIRD text-to-SQL benchmark. It
  raises execution accuracy to $56.9\%$, above both a Memento-style self-graded agent
  ($54.0\%$, a $+2.9$-point mean gain across seeds) and a memory-less agent of identical
  architecture ($52.4\%$).'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: e6ffe48eb1b057ea
source_type: academic_paper
tldr: 论文研究自改进 LLM 智能体的记忆奖励膨胀问题：存储评分由 LLM 自我评估而非真值产生，导致错误记忆被高估并反复复用，形成 Echo Gap 失效模式。论文形式化必要条件误差独立性假设
  EIA，并给出无答案去膨胀算法 LUCID，在 BIRD 基准上将执行准确率提升至 56.9%。
objective_summary: 该论文研究无需权重更新的自改进 LLM 智能体：每个回合被存入外部记忆并评分，后续检索相似回合以塑造行为，存储评分充当隐式非参数策略的代理奖励。由于部署时真值标签不可用，存储奖励仅来自
  LLM 自评，由此产生名为 Echo Gap 的失效模式，错误回合获得膨胀奖励并被高置信度复用。论文证明误差独立性假设 EIA 是纠正该膨胀的必要条件，并给出无答案去膨胀算法
  LUCID。在 BIRD 文本到 SQL 基准上，LUCID 将执行准确率提升至 56.9%，超过 Memento 风格自评分智能体的 54.0% 与无记忆基线的
  52.4%。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM Agents
  - external memory
  - text-to-SQL
  - Echo Gap
  - EIA
  - similarity retrieval
  key_people: []
key_logic_flow:
- 自改进 LLM 智能体在不更新权重的情况下，将每个回合存入外部记忆并评分，后续检索相似回合以塑造行为，存储评分充当隐式非参数策略的代理奖励。
- 部署时真值标签不可用，存储奖励最多只是 LLM 评估，这种替换引发名为 Echo Gap 的失效模式，错误回合获得膨胀奖励并被优先复用。
- 误差通过记忆不断累积而非平均抵消，且确认者的误差与原自我评分偏差保持相关，因此系统无法识别哪些记忆被高估。
- 论文将缺失的性质形式化为误差独立性假设 EIA，并证明它是纠正奖励膨胀的必要条件，可用信号必须既追踪真值又与记忆偏差去相关。
- 膨胀不仅在按存储分数排序检索时累积，在纯相似度检索这一部署智能体实际使用的模式下同样发生。
- 无答案去膨胀算法 LUCID 在 BIRD 文本到 SQL 基准上带来一致的端到端收益，执行准确率达 56.9%，高于 Memento 风格自评分智能体的 54.0%
  和无记忆智能体的 52.4%。
object_mentions:
- object_type: paper
  name: Memory Reward Inflation in Self-Improving LLM Agents
  canonical_name: Memory Reward Inflation in Self-Improving LLM Agents
  url: https://arxiv.org/abs/2608.00017
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文研究自改进 LLM 智能体的记忆奖励膨胀问题，提出 Echo Gap 失效模式与误差独立性假设 EIA，并给出去膨胀算法 LUCID。
  article_id: e6ffe48eb1b057ea
- object_type: project
  name: LUCID
  canonical_name: LUCID
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文提出的无答案去膨胀算法 LUCID 在 BIRD 文本到 SQL 基准上带来一致的端到端收益，将执行准确率提升至 56.9%。
  article_id: e6ffe48eb1b057ea
- object_type: dataset
  name: BIRD
  canonical_name: BIRD
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - BIRD 是论文用于评估 LUCID 的文本到 SQL 基准，LUCID 在该基准上达到 56.9% 的执行准确率。
  article_id: e6ffe48eb1b057ea
- object_type: project
  name: Memento
  canonical_name: Memento
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Memento 风格的自评分智能体被作为对比基线，在 BIRD 基准上达到 54.0% 的执行准确率，比 LUCID 低 2.9 个百分点。
  article_id: e6ffe48eb1b057ea
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Memory Reward Inflation in Self-Improving LLM Agents

View PDF HTML (experimental)Abstract:Self-improving LLM agents increasingly learn from experience without updating any weights. Each episode is stored in an external memory, scored, and retrieved for similar future tasks to shape later behavior. Viewed through a reward lens, the stored score is a proxy reward for an implicit, non-parametric policy. Each retrieved episode then becomes a policy-improvement step whose reliability hinges on how that score is produced. In deployment, ground-truth labels are unavailable, so the stored reward is at best an LLM assessment. This substitution creates a failure mode, the *Echo Gap*, across the memory-based self-improving agents and model families studied. Incorrect episodes receive inflated rewards; thus, the agent preferentially reuses the very mistakes it has most confident in. Because the error compounds through memory rather than averaging out and the confirming judge's errors remain correlated with the original self-grading bias, so it cannot identify which memories are overvalued. The missing property is formalized as the *Error-Independence Assumption* (EIA), which we prove is a *necessary* condition for correcting the inflation, not merely a description of a good verifier: a usable signal must track truth *and* decorrelate its error from the memory bias, and the recoverable payoff is a closed-form function of exactly those two quantities. We further show the inflation compounds not only when retrieval ranks by the stored score but also under plain similarity retrieval which is the regime the deployed agent uses. Finally, the answer-free de-inflation algorithm LUCID delivers a consistent end-to-end gain on the BIRD text-to-SQL benchmark. It raises execution accuracy to $56.9\%$, above both a Memento-style self-graded agent ($54.0\%$, a $+2.9$-point mean gain across seeds) and a memory-less agent of identical architecture ($52.4\%$).

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.