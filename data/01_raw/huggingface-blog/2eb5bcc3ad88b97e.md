---
title: 'MosaicLeaks: Can your research agent keep a secret?'
source: https://huggingface.co/blog/ServiceNow/mosaicleaks
author: []
published: '2026-06-18'
created: '2026-06-19'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: 2eb5bcc3ad88b97e
---

Deep research agents increasingly combine private local documents with external tools like web retrieval, creating a privacy risk: an agent's external queries may leak sensitive information. **MosaicLeaks** proposes a new deep-research task with multi-hop questions that interleave public and private information. Across the models we tested, agents frequently leaked private information, and training only for task performance made it worse. We propose a mosaic-leakage-aware RL training method, **Privacy-Aware Deep Research (PA-DR)**, which raises strict chain success (the share of chains where every hop is answered correctly) from 48.7% to 58.7% while reducing answer/full-information leakage from 34.0% to 9.9%.

A research agent at a healthcare firm is working through a routine question, and along the way it fires off a handful of ordinary-looking web searches. One references a cloud-migration milestone, one a January 2024 security disclosure, one narrows down which vendor got hit. No single query necessarily gives away the whole secret. But anyone watching the agent's outbound traffic can reassemble the fragments: MediConn had migrated 70% of its infrastructure to the cloud by January 2025, a fact that lived only in private documents. This is the mosaic effect, and it's the failure mode at the centre of MosaicLeaks.

MosaicLeaks treats those web queries as the leakage channel: the adversary never sees the private documents or the agent's reasoning, only the cumulative query log, and tries to infer private enterprise information from it.

We measure leakage in three ways, depending on what the adversary can infer from the observed queries:

| Leakage type | What the adversary sees | What counts as leakage |
|---|---|---|
Intent leakage |
Only the agent's web-query log | The adversary can infer the private research questions or goals the agent was trying to answer |
Answer leakage |
The web-query log plus a question about private information | The adversary can answer those private questions without seeing the private documents |
Full-information leakage |
Only the web-query log | The adversary can state verifiably true private claims, even without being given the questions |

These three represent increasing levels of concern. Intent leakage reveals *what the agent is investigating*. Answer leakage means the query log holds enough to answer a private question someone already has in hand. Full-information leakage is the strongest case: the observer can discover and state private facts without being told what to look for.