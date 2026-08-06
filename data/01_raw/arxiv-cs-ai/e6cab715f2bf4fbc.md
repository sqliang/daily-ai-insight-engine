---
title: 'RAG-TESTER: Automated End-to-End Testing of Retrieval-Augmented Large Language
  Models'
source: https://arxiv.org/abs/2608.00054
author:
- '[[Ange Maiztegi, Jon Ayerdi, Miren Illarramendi, Aitor Arrieta]]'
published: '2026-08-05'
created: '2026-08-05'
manifest_dates:
- '2026-08-05'
description: 'arXiv:2608.00054v1 Announce Type: new Abstract: Retrieval-Augmented
  Generation (RAG) enables Large Language Models (LLMs) to use external and domain-specific
  knowledge, but its reliability depends on the interaction between the generative
  model, embedding model, retrieval mechanism, and prompt construction strategy. We
  present RagTester, an automated end-to-end testing approach for RAG systems. RagTester
  generates retrieval documents, test inputs, and expected outputs; executes the tests;
  and evaluates the resulting answers using an LLM as a judge. Its test-generation
  strategy targets complex passages, unsupported queries, and document-coverage criteria.
  We evaluate RagTester using eight LLMs and six embedding models, yielding 24 compatible
  configurations, and compare it with a baseline test-input generator. Across 72,000
  test executions, RagTester detected 21,633 failures, 6.6% more than the baseline,
  and outperformed it in 20 of the 24 configurations. The detected failures include
  inaccurate retrieval, unsupported answers, incomplete use of retrieved context,
  and difficulties interpreting complex passages. These results show that coverage-oriented
  test generation can effectively expose failures caused by the interaction between
  retrieval and generation components and support the assessment of RAG configurations
  before deployment.'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: e6cab715f2bf4fbc
---

# Computer Science > Artificial Intelligence

# Title:RAG-TESTER: Automated End-to-End Testing of Retrieval-Augmented Large Language Models

View PDF HTML (experimental)Abstract:Retrieval-Augmented Generation (RAG) enables Large Language Models (LLMs) to use external and domain-specific knowledge, but its reliability depends on the interaction between the generative model, embedding model, retrieval mechanism, and prompt construction strategy. We present RagTester, an automated end-to-end testing approach for RAG systems. RagTester generates retrieval documents, test inputs, and expected outputs; executes the tests; and evaluates the resulting answers using an LLM as a judge. Its test-generation strategy targets complex passages, unsupported queries, and document-coverage criteria. We evaluate RagTester using eight LLMs and six embedding models, yielding 24 compatible configurations, and compare it with a baseline test-input generator. Across 72,000 test executions, RagTester detected 21,633 failures, 6.6% more than the baseline, and outperformed it in 20 of the 24 configurations. The detected failures include inaccurate retrieval, unsupported answers, incomplete use of retrieved context, and difficulties interpreting complex passages. These results show that coverage-oriented test generation can effectively expose failures caused by the interaction between retrieval and generation components and support the assessment of RAG configurations before deployment.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.