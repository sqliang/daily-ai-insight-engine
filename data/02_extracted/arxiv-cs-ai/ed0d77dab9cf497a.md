---
title: 'Hallucination as Exploit: Evidence-Carrying Multimodal Agents'
source: https://arxiv.org/abs/2605.19192
author:
- '[[Guijia Zhang, Hao Zheng, Harry Yang]]'
published: '2026-05-20'
created: '2026-05-21'
description: 'arXiv:2605.19192v1 Announce Type: new Abstract: Multimodal agents use
  screenshots, documents, and webpages to choose tool calls. When a false visual claim
  triggers a click, email, extraction, or transfer, hallucination becomes an authorization
  failure rather than an answer-quality error. We formalize this failure mode as hallucination-to-action
  conversion: an unsupported perceptual claim supplies the precondition that makes
  a privileged action appear permitted. We propose evidence-carrying multimodal agents
  (ECA), which treat free-form model text as inadmissible evidence. ECA decomposes
  each tool call into action-critical predicates, obtains typed certificates from
  constrained DOM/OCR/AX verifiers, and lets a deterministic gate grant only the privileges
  those certificates support. The architecture does not hide perception error; it
  converts opaque model belief into named verifier, schema, and implementation residuals.
  Verifier red-teaming over 1,900 attacks exposes this residual directly: four targeted
  hardening steps reduce gate bypass from 15% to 1.3%. With content-derived certificates,
  ECA obtains 0% unsafe-action rate on a 200-task end-to-end pipeline (Wilson 95%
  upper bound 2.67%) and a 120-task browser proof-of-concept (upper bound 4.3%). A
  direct HACR audit on 500 stratified task keys shows that unsupported action-critical
  claims reach unsafe execution for naive agents (100.0%) and prompt-only defense
  (49.6%), but not for ECA. Oracle-certificate replay on 7,488 GPT-5.4 benchmark traces
  serves as a gate-correctness sanity check, and neural judge baselines remain bypassable
  under the same threat model. The resulting principle is simple: model language may
  propose actions, but external evidence must authorize them.'
tags:
- clippings
extraction_status: success
id: ed0d77dab9cf497a
source_type: academic_paper
tldr: 该论文将多模态智能体的幻觉问题重新定义为授权失败，并提出证据携带型多模态智能体（ECA）架构。ECA通过受约束的验证器提供类型化证书，由确定性门控决定授权，在1,900次红队攻击中将门控绕过率从15%降至1.3%，并在200项任务上实现0%的不安全动作率。
objective_summary: 该arXiv论文于2026年5月提交，作者形式化定义了多模态智能体因视觉幻觉触发危险工具调用的"幻觉到行动转换"模式。他们提出证据携带型多模态智能体（ECA）架构，将模型自由文本视为不可采纳证据，通过DOM/OCR/AX验证器提供类型化证书，由确定性门控仅授予证书支持的权限。在1,900次验证器红队攻击中，经四轮定向加固将门控绕过率从15%降至1.3%；ECA在200项任务端到端流水线上实现0%不安全动作率（Wilson
  95%上限2.67%），在500项任务HACR审计中朴素智能体不安全执行率为100.0%，仅提示词防御为49.6%，ECA为0%。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - ECA
  - DOM/OCR/AX
  - HACR
  - GPT-5.4
  key_people: []
key_logic_flow:
- 论文将多模态智能体的幻觉问题重新定义为授权失败而非回答质量错误，并提出"幻觉到行动转换"的形式化框架：不支持的感知主张为特权动作提供了看似允许的前提条件。
- 作者提出证据携带型多模态智能体（ECA）架构，将模型自由文本视为不可采纳证据，通过受约束的DOM/OCR/AX验证器获取类型化证书，由确定性门控仅授予证书支持的权限。
- 在1,900次攻击的验证器红队测试中，经过四轮定向加固步骤，门控绕过率从15%降至1.3%，证明该残差可直接暴露并修复。
- ECA在200项任务的端到端流水线上实现了0%的不安全动作率（Wilson 95%置信区间上限2.67%），在120项任务的浏览器概念验证中同样实现0%（上限4.3%）。
- 在500个分层任务键上的直接HACR审计显示，朴素智能体的不安全执行率为100.0%，仅靠提示词防御为49.6%，而ECA为0%。
- 在7,488条GPT-5.4基准轨迹上的预言机证书重放验证了门控正确性，同时神经判别器基线在相同威胁模型下仍可被绕过。
pipeline_stage: fact_extracted
extract_result: success
object_mentions:
- object_type: paper
  name: 'Hallucination as Exploit: Evidence-Carrying Multimodal Agents'
  canonical_name: 'Hallucination as Exploit: Evidence-Carrying Multimodal Agents'
  url: https://arxiv.org/abs/2605.19192
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文形式化定义了多模态智能体中幻觉成为授权失败而非回答质量错误的故障模式，并命名为'幻觉到行动转换'。
  - 论文在1,900次红队攻击上验证了ECA门控机制，经四轮定向加固将绕过率从15%降至1.3%。
  - ECA架构在200项任务端到端流水线上实现0%不安全动作率，Wilson 95%置信区间上限为2.67%。
  article_id: ed0d77dab9cf497a
- object_type: project
  name: Evidence-Carrying Multimodal Agents (ECA)
  canonical_name: Evidence-Carrying Multimodal Agents (ECA)
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - ECA将每个工具调用分解为行动关键谓词，从受约束的DOM/OCR/AX验证器获取类型化证书，并由确定性门控仅授权证书支持的操作。
  - ECA的核心原则是：模型语言可以提议行动，但外部证据必须授权它们。
  - 在500项任务的HACR审计中，ECA实现了0%的不安全执行率，而朴素智能体为100.0%，仅提示词防御为49.6%。
  article_id: ed0d77dab9cf497a
---

# Computer Science > Artificial Intelligence

# Title:Hallucination as Exploit: Evidence-Carrying Multimodal Agents

View PDF HTML (experimental)Abstract:Multimodal agents use screenshots, documents, and webpages to choose tool calls. When a false visual claim triggers a click, email, extraction, or transfer, hallucination becomes an authorization failure rather than an answer-quality error. We formalize this failure mode as hallucination-to-action conversion: an unsupported perceptual claim supplies the precondition that makes a privileged action appear permitted. We propose evidence-carrying multimodal agents (ECA), which treat free-form model text as inadmissible evidence. ECA decomposes each tool call into action-critical predicates, obtains typed certificates from constrained DOM/OCR/AX verifiers, and lets a deterministic gate grant only the privileges those certificates support. The architecture does not hide perception error; it converts opaque model belief into named verifier, schema, and implementation residuals. Verifier red-teaming over 1,900 attacks exposes this residual directly: four targeted hardening steps reduce gate bypass from 15% to 1.3%. With content-derived certificates, ECA obtains 0% unsafe-action rate on a 200-task end-to-end pipeline (Wilson 95% upper bound 2.67%) and a 120-task browser proof-of-concept (upper bound 4.3%). A direct HACR audit on 500 stratified task keys shows that unsupported action-critical claims reach unsafe execution for naive agents (100.0%) and prompt-only defense (49.6%), but not for ECA. Oracle-certificate replay on 7,488 GPT-5.4 benchmark traces serves as a gate-correctness sanity check, and neural judge baselines remain bypassable under the same threat model. The resulting principle is simple: model language may propose actions, but external evidence must authorize them.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.