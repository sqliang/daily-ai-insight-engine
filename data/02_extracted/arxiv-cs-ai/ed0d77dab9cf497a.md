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
tldr: 论文提出证据携带型多模态智能体（ECA），用确定性门控阻止AI幻觉导致未授权操作。
objective_summary: 一篇arXiv论文形式化了多模态智能体中幻觉引发未授权操作的安全漏洞，并提出ECA架构：将工具调用的前提条件分解为关键谓词，通过DOM/OCR/AX验证器获取类型化证书，由确定性门控仅授权证书支持的权限。在1900次攻击测试中，四次加固将门控绕过率从15%降至1.
event_type: policy_and_safety
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - ECA
  - HACR
  - DOM
  - OCR
  - AX
  - GPT-5.4
  key_people: []
key_logic_flow:
- 论文将多模态智能体中的幻觉问题重新定义为授权失败而非答案质量错误：虚假视觉断言触发点击、邮件、提取或转账等特权操作。
- 形式化提出了hallucination-to-action conversion（HACR）这一失效模式，即无证据支持的感知断言为特权操作提供了看似允许的前提条件。
- 提出证据携带型多模态智能体（ECA）架构，将模型自由文本视为不可采纳证据，工具调用需通过约束性DOM/OCR/AX验证器获取类型化证书。
- 确定性门控机制仅授予证书支持的权限，将不透明的模型信念转化为可追溯的验证器残留（verifier residuals）。
- 通过1900次红队攻击进行验证器对抗测试，四次针对性加固将门控绕过率从15%降至1.3%。
- 200任务端到端管线中ECA获得0%不安全操作率（Wilson 95%置信上限2.67%），500任务分层HACR审计显示朴素智能体unsafe execution率为100%，纯提示防御为49.6%，ECA为0%。
pipeline_stage: fact_extracted
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