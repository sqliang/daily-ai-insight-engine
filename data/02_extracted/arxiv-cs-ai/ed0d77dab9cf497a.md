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
tldr: 提出证据携带多模态智能体(ECA)架构，用外部验证证书替代模型自由文本来授权敏感操作，将幻觉攻击面从100%降至0%。
objective_summary: 论文于2026年5月发表，将多模态智能体的幻觉问题重新定义为授权失败而非回答质量错误，提出ECA架构：将工具调用拆解为动作关键谓词，通过DOM/OCR/AX验证器获取类型化证书，由确定性门控决定授权。在1900+攻击红队测试中，绕过率从15%降至1.3%；端到端200任务管道实现0%不安全操作率。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - ECA
  - Multimodal Agents
  - DOM
  - OCR
  - AX
  - GPT-5.4
  - HACR
  key_people: []
key_logic_flow:
- 多模态智能体通过截屏、文档、网页选择工具调用时，错误的视觉声明可触发点击、邮件、提取或转账等特权操作，构成授权失败而非简单的回答质量错误。
- 将这一失败模式形式化为幻觉到行动转换(HAC)：未经证实的感知声明充当了使特权行动看似合法的前提条件。
- 提出证据携带多模态智能体(ECA)架构：将模型自由文本视为不可采纳的证据，每个工具调用被分解为动作关键谓词。
- ECA通过受限的DOM/OCR/AX验证器获取类型化证书，由确定性门控仅授予证书支持的权限，将不透明的模型信念转化为命名的验证器、模式和实现残差。
- 在1900+次攻击的验证器红队测试中，四轮定向加固将门控绕过率从15%降至1.3%，端到端200任务管道实现0%不安全操作率（Wilson 95%置信上界2.67%）。
- 对500个分层任务键的HACR审计表明：朴素智能体100.0%的不安全执行率，纯提示防御降至49.6%，而ECA为0%；神经法官基线在同一威胁模型下仍然可被绕过。
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