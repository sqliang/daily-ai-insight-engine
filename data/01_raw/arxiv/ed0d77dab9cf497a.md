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