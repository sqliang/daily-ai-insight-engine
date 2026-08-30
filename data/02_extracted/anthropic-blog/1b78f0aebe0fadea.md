---
title: Usage Policy Update
source: https://www.anthropic.com/news/usage-policy-update
author: []
published: '2026-08-26'
created: '2026-08-27'
manifest_dates:
- '2026-08-27'
- '2026-08-28'
- '2026-08-29'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 1b78f0aebe0fadea
source_type: tech_blog
tldr: Anthropic 更新了使用政策（Usage Policy），新增针对恶意网络与基础设施入侵的禁止条款，收窄对政治内容的全面限制范围，并修订执法用途的表述。新政策于
  2025 年 9 月 15 日生效。
objective_summary: Anthropic 基于用户反馈、产品变化、监管进展与执法优先事项更新了使用政策，为 Claude 的使用方式提供更清晰的框架，新政策于
  2025 年 9 月 15 日生效。更新新增了禁止恶意计算机、网络与基础设施入侵行为的章节，并发布了面向代理式（agentic）使用的补充指引。政策取消了历史上对游说与竞选内容的全面禁止，改为仅禁止欺骗性或破坏民主进程、涉及选民和竞选定向的用途。政策还修订了执法用途相关表述，移除了此前针对后台工具和分析应用的各类例外条款。
event_type: policy_and_safety
epistemic_status: pr_statement
entities:
  companies:
  - Anthropic
  technologies:
  - Claude
  - Claude Code
  - Computer Use
  - Agentic AI
  key_people: []
key_logic_flow:
- Anthropic 基于用户反馈、产品变化、监管进展和执法优先事项更新了使用政策，所有变更将于 2025 年 9 月 15 日生效。
- 针对代理式 AI 能力带来的规模化滥用、恶意软件生成和网络攻击风险，政策新增了禁止恶意计算机、网络与基础设施入侵活动的章节。
- 公司发布了关于使用政策如何适用于代理式用途的补充指南，提供代理场景下禁止活动的具体示例，但不替代使用政策本身。
- 政策取消了历史上对游说和竞选内容的全面禁止，改为仅禁止欺骗性或破坏民主进程、以及涉及选民和竞选定向的用途，以支持合法的政策研究与政治写作。
- 政策修订了执法用途相关表述，移除了此前针对后台办公工具和分析应用的各类例外，使允许的用途更易于理解。
object_mentions:
- object_type: product
  name: Claude
  canonical_name: Claude
  url: https://www.anthropic.com/claude
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Anthropic 表示此次使用政策更新为 Claude 的使用方式提供清晰框架，相关变更将于 2025 年 9 月 15 日生效。
  - 政策取消了历史上对游说与竞选内容的全面禁止，改为仅禁止欺骗性或破坏民主进程的用途，从而支持合法的政策研究与政治写作。
  article_id: 1b78f0aebe0fadea
- object_type: product
  name: Claude Code
  canonical_name: Claude Code
  url: https://www.anthropic.com/claude-code
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Anthropic 指出其已发布包括 Claude Code 和 Computer Use 在内的代理式工具，这些工具也带来规模化滥用与网络攻击的新风险。
  article_id: 1b78f0aebe0fadea
- object_type: product
  name: Computer Use
  canonical_name: Computer Use
  url: https://www.anthropic.com/news/computer-use
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Anthropic 在文章中提及已发布 Computer Use 等代理式工具，并据此更新使用政策以约束相关的恶意用途。
  article_id: 1b78f0aebe0fadea
- object_type: paper
  name: 'Detecting and Countering Malicious Uses of Claude: March 2025'
  canonical_name: 'Detecting and Countering Malicious Uses of Claude: March 2025'
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - '文章引用其首份威胁情报报告《Detecting and Countering Malicious Uses of Claude: March 2025》，指出代理能力带来规模化滥用、恶意软件生成与网络攻击等风险。'
  article_id: 1b78f0aebe0fadea
extract_result: success
---

# Usage policy update

Today, we’re sharing some updates to our Usage Policy that reflect the growing capabilities and evolving usage of our products. Our Usage Policy serves as a framework for how Claude should and shouldn’t be used, providing clear guidance for everyone who uses Anthropic’s products.

In this update, our goal is to provide greater clarity and detail on our Policy based on user feedback, product changes, regulatory developments, and our enforcement priorities. These changes will take effect on September 15, 2025.

Below is a summary of some of the changes, and you can view the new Usage Policy here.

**Addressing cybersecurity and agentic use**

Over the past year, we’ve seen rapid advances in agentic capabilities. We've released our own agentic tools like Claude Code and Computer Use, and our models power many of the world's leading coding agents.

These powerful capabilities introduce new risks, including potential for scaled abuse, malware creation, and cyber attacks, as shared in our first threat intelligence report, *Detecting and Countering Malicious Uses of Claude: March 2025*.

To address these risks, we've added a section to our Usage Policy outlining the malicious computer, network, and infrastructure compromise activities that are prohibited by Anthropic. We continue to support use cases that strengthen cybersecurity, such as discovering vulnerabilities with the system owner's consent.

We’ve also published a new article to our Help Center on how our Usage Policy applies to agentic use more broadly. This supplementary guidance provides concrete examples of prohibited activities in agentic contexts, and is not meant to replace or supersede our Usage Policy.

**Revisiting broad restrictions on political content**

Our Usage Policy has historically contained broad prohibitions on all types of lobbying or campaign content. We believed this stance was appropriate given the unknown risks of AI-generated content on influencing democratic processes, and these are still prominent risks we take seriously.

We’ve heard from users that this blanket approach also limited legitimate use of Claude for policy research, civic education, and political writing. We're now tailoring our restrictions to specifically prohibit use cases that are deceptive or disruptive to democratic processes, or involve voter and campaign targeting. This approach enables legitimate political discourse and research while prohibiting activity that is misleading or invasive.

**Updating our language on law enforcement use**

Our previous Usage Policy language on law enforcement included various exceptions for back-office tools and analytical applications, which occasionally made it difficult to understand which use cases were permitted.