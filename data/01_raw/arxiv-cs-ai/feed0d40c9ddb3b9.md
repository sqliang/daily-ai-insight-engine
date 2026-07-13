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
pipeline_stage: ingested
id: feed0d40c9ddb3b9
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