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
pipeline_stage: fact_extracted
id: e6cab715f2bf4fbc
source_type: academic_paper
tldr: RagTester 是一种针对检索增强生成（RAG）系统的自动化端到端测试方法，通过覆盖导向的测试生成，在 72,000 次测试执行中检测出 21,633
  个失败，比基线方法多 6.6%，并在 24 种配置中的 20 种上表现更优。
objective_summary: arXiv 论文提出 RagTester，一种面向检索增强生成（RAG）系统的自动化端到端测试方法。该方法自动生成检索文档、测试输入与预期输出，执行测试并采用
  LLM 作为裁判评估答案，其测试生成策略覆盖复杂段落、不支持查询与文档覆盖率三类标准。论文使用 8 个 LLM 与 6 个嵌入模型构成 24 种兼容配置进行评估，在
  72,000 次测试执行中检测出 21,633 个失败，比基线多 6.6%，并在 24 种配置中的 20 种上优于基线。检测出的失败类型包括检索不准确、不支持的回答、检索上下文利用不完整以及复杂段落理解困难。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - RAG
  - LLM-as-a-Judge
  - Embedding Model
  key_people: []
key_logic_flow:
- RagTester 是一种面向 RAG 系统的自动化端到端测试方法，能够自动生成检索文档、测试输入与预期输出，并执行测试。
- 该方法的测试生成策略专门针对复杂段落、不支持查询与文档覆盖率三类标准进行设计。
- 评估实验使用 8 个 LLM 与 6 个嵌入模型组合成 24 种兼容配置，并与一种基线测试输入生成器进行对比。
- 在 72,000 次测试执行中，RagTester 检测出 21,633 个失败，比基线多 6.6%，且在 24 种配置中的 20 种上表现优于基线。
- 检测出的失败类型包括检索不准确、对不支持问题的回答、检索上下文利用不完整以及复杂段落理解困难。
- 研究结果表明，覆盖导向的测试生成能够有效暴露检索与生成组件交互导致的失败，可用于 RAG 配置的部署前评估。
object_mentions:
- object_type: project
  name: RagTester
  canonical_name: RagTester
  url: https://arxiv.org/abs/2608.00054
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - RagTester 是一种面向检索增强生成系统的自动化端到端测试方法，能够生成检索文档、测试输入和预期输出并执行测试。
  - 在 72,000 次测试执行中，RagTester 检测出 21,633 个失败，比基线测试输入生成器多 6.6%，并在 24 种配置中的 20 种上表现更优。
  article_id: e6cab715f2bf4fbc
extract_result: success
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