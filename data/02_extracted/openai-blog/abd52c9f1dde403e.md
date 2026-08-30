---
title: Advancing price-performance for developers with GPT‑5.6 in Kiro
source: https://openai.com/index/gpt-5-6-in-kiro
author: []
published: Mon, 24 Aug 2026 12:00:00 GMT
created: '2026-08-25'
manifest_dates:
- '2026-08-25'
- '2026-08-26'
- '2026-08-27'
description: GPT‑5.6 is now available in Kiro, helping developers plan, build, review,
  and test software with better price-performance.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: abd52c9f1dde403e
source_type: tech_blog
tldr: OpenAI 发布公告，GPT-5.6 模型家族（含 Sol、Terra、Luna）现已集成至软件开发代理 Kiro，用于规划、构建、评审和测试工作流；经
  OpenAI 与 AWS 联合优化，在 Terminal-Bench 2.1 上任务成本降低约 82%。
objective_summary: OpenAI 在官网发布公告，宣布 GPT-5.6 模型家族（Sol、Terra、Luna）正式集成至软件开发代理 Kiro。Kiro
  将高层意图转化为明确需求、技术设计与可执行任务，使模型在长周期开发工作中理解团队标准与代码库上下文。OpenAI 与 AWS 联合优化了 Kiro 环境，在 Terminal-Bench
  2.1 基准上 GPT-5.6 Terra 完成任务可降低约 82% 的成本。双方表示将继续合作改进 OpenAI 模型在 Kiro 中的性能。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - OpenAI
  - AWS
  technologies:
  - GPT-5.6
  - GPT-5.6 Sol
  - GPT-5.6 Terra
  - GPT-5.6 Luna
  - Terminal-Bench 2.1
  - spec-driven development
  - property-based testing
  key_people: []
key_logic_flow:
- OpenAI 宣布 GPT-5.6 模型家族（Sol、Terra、Luna）现已集成到软件开发代理 Kiro 中，用于团队规划、构建、评审和测试软件的工作流。
- GPT-5.6 强调每个 token 产出更多有效工作，提供更强的性能价格比，适合长周期、基于团队需求与代码库上下文的开发任务。
- Kiro 将高层意图转化为清晰需求、技术设计和可执行任务，为模型提供结构化上下文以提升对系统实现目标的理解。
- 开发者可通过规格驱动开发、跨代码库上下文、关键检查点评审和基于属性的测试来完成复杂多步编码任务。
- 在 Terminal-Bench 2.1 上，OpenAI 与 AWS 联合测试显示 GPT-5.6 Terra 在 Kiro 中完成任务可降低约 82% 的成本。
- OpenAI 与 AWS 表示将继续合作，优化 OpenAI 模型在 Kiro 中的性能，帮助开发者从 AI 编码中获得更多价值。
object_mentions:
- object_type: product
  name: Kiro
  canonical_name: Kiro
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Kiro 是 OpenAI 与 AWS 合作优化的软件开发代理，将 GPT-5.6 模型引入团队规划、构建、评审和测试的开发流程。
  - Kiro 将高层意图转化为明确需求、技术设计和可执行任务，为 GPT-5.6 提供结构化上下文以完成复杂编码工作。
  article_id: abd52c9f1dde403e
- object_type: model
  name: GPT-5.6
  canonical_name: GPT-5.6
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - GPT-5.6 模型家族现已在 Kiro 中可用，包含 Sol、Terra 和 Luna 三个系列，帮助开发者以更少迭代产出更高质量的代码。
  - GPT-5.6 宣称从每个 token 中产出更多有效工作，提供更强的性能价格比，并可承载复杂任务的按需能力。
  article_id: abd52c9f1dde403e
- object_type: model
  name: GPT-5.6 Terra
  canonical_name: GPT-5.6 Terra
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 在 Terminal-Bench 2.1 上，OpenAI 与 AWS 联合测试显示 GPT-5.6 Terra 在 Kiro 中完成成功任务可带来约 82%
    的成本降低。
  article_id: abd52c9f1dde403e
- object_type: project
  name: Terminal-Bench 2.1
  canonical_name: Terminal-Bench 2.1
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - OpenAI 与 AWS 使用 Terminal-Bench 2.1 基准测试评估 GPT-5.6 Terra 在 Kiro 环境中的任务完成表现。
  article_id: abd52c9f1dde403e
extract_result: success
---

The GPT‑5.6 model family is now available in Kiro, a software development agent that brings engineering rigor and quality to AI-native coding at scale. For Kiro users, the update brings OpenAI’s latest flagship model series, including Sol, Terra, and Luna, into the development workflows where teams plan, build, review, and test software. Together, these models can help developers produce higher-quality code with fewer iterations and better value per token.

GPT‑5.6 delivers more useful work from every token, with stronger performance per dollar and on-demand capability for complex tasks. In Kiro, developers can apply these capabilities to long-running development work grounded in their requirements, codebase, and team standards.

Kiro turns high-level intent into clear requirements, technical designs, and executable tasks. This structured context helps GPT‑5.6 understand what a team is building, how the system should work, and what the final implementation needs to accomplish.

With GPT‑5.6 in Kiro, developers can:

- Turn product ideas and requirements into structured implementation plans.
- Complete complex, multi-step coding tasks with greater consistency.
- Bring structure to AI coding with spec-driven development.
- Work with context from across their codebase and established team standards.
- Review and refine the model’s work at key checkpoints before changes are implemented.
- Check correctness of implementation using property-based testing.

OpenAI and AWS have also worked together to optimize the Kiro environment and OpenAI models. Testing found that on Terminal-Bench 2.1, GPT‑5.6 Terra completed successful tasks in Kiro at roughly 82% cost reduction. Kiro’s spec-driven approach grounds the model in clear requirements, technical designs, and task context from the start, so it arrives at working solutions faster, with fewer missteps along the way. For developers, that means more finished work, less wasted effort, and better value from every coding session.

OpenAI and AWS will continue working together to improve the performance of OpenAI models in Kiro and help developers get more value from AI across the software development lifecycle.