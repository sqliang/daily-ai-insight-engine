---
title: 'GitLost: We Tricked GitHub''s AI Agent into Leaking Private Repos'
source: https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/
author:
- '[[ColinEberhardt]]'
published: '2026-07-08'
created: '2026-07-08'
description: 'Article URL: https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/
  Comments URL: https://news.ycombinator.com/item?id=48827858 Points: 165 # Comments:
  57'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: cf7d6d2d79cfeb1f
manifest_dates:
- '2026-07-08'
source_type: community_discussion
tldr: Noma Labs 发现 GitHub Agentic Workflows 存在提示注入漏洞（GitLost），攻击者可通过在公开仓库发布恶意 Issue，诱导
  AI 代理读取并公开泄露同一组织内的私有仓库数据。
objective_summary: Noma Labs 的安全研究人员在 GitHub 新推出的 Agentic Workflows 中发现了一个严重的提示注入漏洞并命名为
  GitLost。该漏洞利用 AI 代理会读取 Issue 内容的特性，攻击者无需任何凭证即可在公开仓库中提交恶意 Issue，诱使拥有跨仓库只读权限的 AI 代理将私有仓库数据读取后以公开评论形式发布。研究人员发现添加
  'Additionally' 关键词可以绕过 GitHub 的安全防护机制。Noma Labs 已向 GitHub 负责任披露此漏洞，并提供了可复现的 PoC
  链接。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - GitHub
  - Noma Labs
  technologies:
  - GitHub Agentic Workflows
  - GitHub Actions
  - prompt injection
  key_people: []
key_logic_flow:
- Noma Labs 发现 GitHub Agentic Workflows 存在提示注入漏洞，命名为 GitLost。
- 攻击者无需身份验证即可在公开仓库中提交恶意 Issue，利用 AI 代理读取同一组织内的私有仓库数据。
- 触发漏洞的工作流配置为在 Issue 被分配时运行，代理以跨仓库只读权限访问组织内其他仓库。
- 研究人员发现添加 'Additionally' 关键词可以绕过 GitHub 的安全防护，使代理重新调整输出而非拒绝执行。
- 泄露的私有仓库数据通过 AI 代理以公开评论形式发布在公共仓库中，任何互联网用户均可访问。
- Noma Labs 建议 AI 系统构建者永远不要将用户控制的内容视为可信指令输入，并严格限制代理的权限范围。
extract_result: success
object_mentions:
- object_type: product
  name: GitHub Agentic Workflows
  canonical_name: GitHub Agentic Workflows
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - GitHub 近期推出的 Agentic Workflows 结合了 GitHub Actions 与 AI 代理，允许团队使用 Markdown 编写工作流。
  - 该产品允许 AI 代理读取 Issue、调用工具并访问同一组织内的其他公开和私有仓库。
  article_id: cf7d6d2d79cfeb1f
- object_type: project
  name: GitLost
  canonical_name: GitLost
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Noma Labs 将发现的 GitHub Agentic Workflows 提示注入漏洞命名为 GitLost。
  - 该漏洞利用 AI 代理的上下文窗口即攻击面的特性，将用户控制的 Issue 内容武器化为恶意指令。
  article_id: cf7d6d2d79cfeb1f
- object_type: project
  name: sasinomalabs/poc
  canonical_name: sasinomalabs/poc
  url: https://github.com/sasinomalabs/poc
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Noma Labs 提供了包含工作流复现和实时证据的公开 PoC 仓库 sasinomalabs/poc。
  - 泄漏数据包括 sasinomalabs/poc（公开仓库）和 sasinomalabs/testlocal（私有仓库）中 README.md 的内容。
  article_id: cf7d6d2d79cfeb1f
- object_type: project
  name: GrafanaGhost
  canonical_name: GrafanaGhost
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Noma Labs 在文章末尾提及了 GrafanaGhost 等其他自主智能体 AI 漏洞研究项目。
  article_id: cf7d6d2d79cfeb1f
- object_type: project
  name: DockerDash
  canonical_name: DockerDash
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Noma Labs 在文章末尾提及了 DockerDash 等其他自主智能体 AI 漏洞研究项目。
  article_id: cf7d6d2d79cfeb1f
- object_type: project
  name: Context Crush
  canonical_name: Context Crush
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Noma Labs 在文章末尾提及了 Context Crush 等其他自主智能体 AI 漏洞研究项目。
  article_id: cf7d6d2d79cfeb1f
- object_type: project
  name: GeminiJack
  canonical_name: GeminiJack
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - Noma Labs 在文章末尾提及了 GeminiJack 等其他自主智能体 AI 漏洞研究项目。
  article_id: cf7d6d2d79cfeb1f
---

**TL;DR**: Noma Labs discovered a critical prompt injection vulnerability within GitHub’s new Agentic Workflows, allowing an unauthenticated attacker to silently pull data from private repositories by posting a crafted GitHub Issue in a public repository belonging to the same organization as the private repositories. Noma Labs named the vulnerability GitLost.


## Introduction

GitHub recently launched GitHub Agentic Workflows, pairing GitHub Actions (GitHub’s automation system for running tasks in response to repository events) with an AI agent backed by Claude or GitHub Copilot. GitHub Agentic Workflows allow teams to write their GitHub workflows in plain Markdown, and the GitHub agent reads issues, calls tools, and responds on its own.


As a vulnerability researcher with a security development background, one of the first questions that came to mind after this launch was fundamental and straightforward: What will happen when the GitHub agent reads something it should not trust?

The answer is a textbook indirect prompt-injection attack, the kind of attack that quietly sends private data to anyone on the internet. Prompt injection is a class of attack in which an adversary hides malicious instructions inside the content read by an AI agent. That content causes the agent to follow those hidden instructions instead of the ones its operator intended.

## What are GitHub Agentic Workflows?

GitHub Agentic Workflows let teams automate their interactions with code repositories using natural language. Workflows live in Markdown (.md) files, are compiled into YAML (a common configuration file format), Actions files with the .yml extension, and run with the help of an AI agent with configurable permissions. The GitHub agent can read issues, call tools, and access other repositories within an organization.

## GitLost Vulnerability Overview

The root cause of the GitLost vulnerability is, by now, a familiar one in agentic AI systems: prompt injection. In most agentic prompt injection attacks, the agent treats the wrong content as a trusted source of instructions and allows itself to be misdirected or misused. This happens when the system fails to maintain a strict trust boundary between system-level directives and untrusted user data. In this specific case, any malicious actor can create a GitHub Issue and, in the issue body, hide commands in plain English that GitHub’s agent will follow.

The vulnerable Github Agentic Workflow Noma Labs discovered was configured to:

- Trigger the workflow on issues.assigned events in GitHub
- Read the issue
**Title**and**Body** - Post a comment in response using the add-comment tool
- Run with read access to other repositories (public and private) in the organization

To exploit this vulnerability, the attacker needed no coding skills, access, or credentials. All that was needed was to open an issue in a public repository belonging to an organization that uses GitHub’s Agentic Workflow setup and wait.




## The Attack Flow

Let’s take a look at the exact attack flow that Noma Labs vulnerability researchers succeeded with:


First, they crafted a GitHub issue that looked completely innocent, consisting of a plausible-looking request from a VP Sales after meeting with a customer, as shown below:


** In this specific example, the workflow action was triggered when the issue was assigned**, but our testing confirmed it works the same way for other GitHub workflow actions.

Then, after a GitHub automation assigned the issue, an event-triggered workflow caused the agent to fetch the contents of README.md from both the poc (public) and testlocal (private) repositories.


Finally, the GitHub agent then posted them as a public comment on the issue in the public repository, which anyone could access and read.

## The “Additional” Exploit

GitHub had restrictive guardrails in place to prevent exactly this scenario, but they failed to protect the repositories as intended. Testing GitHub repeatedly with variations, as an attacker would, and adding the keyword **“Additionally”** triggered unintended behavior in the model, causing it to reframe its output rather than refuse it. Essentially, by tricking the model, I was able to ensure that GitHub’s guardrails did not work as intended and didn’t prevent the data leak.


## Vulnerability Proof of Concept

With the goal of full transparency, Noma Lab’s confirmed findings, including our workflow reproductions and live evidence, can be found here:

**Workflow run**: https://github.com/sasinomalabs/poc/actions/runs/23909666039**Issue**: https://github.com/sasinomalabs/poc/issues/153

The leaked data included the contents of README.md from:

- sasinomalabs/poc (public repo)
- sasinomalabs/remote-ping (public repo, no README confirmed)
- sasinomalabs/testlocal (private repo)

## Why it Matters

GitLost perfectly illustrates one of the fundamental security challenges every organization faces with agentic AI systems. The agent’s context window is also its attack surface. Any content the agent reads, whether issues, pull requests, comments, or files, can be weaponized if the agent treats that content as instructional input.

Traditional security models typically assume that trust boundaries are enforced by code. In agentic systems, trust boundaries are partly enforced by the model’s behavior, and models are inherently instruction-following. Prompt injection attacks have become, to agentic AI, what SQL injections were to web applications: a systematic, category-wide vulnerability class that requires the same systematic strategies and defenses.

## Noma Recommendations for Builders/AI Security Officers:

- Never treat user-controlled content as trusted instruction input for an AI agent
- Scope permissions to the minimum required. Agents with cross-repository access are especially high-value targets
- Restrict what any agent can post publicly, especially in response to issue content
- Sanitize or isolate user input from the instruction context before passing it to the model

## Responsible Disclosure

GitLost was responsibly disclosed to GitHub. Vulnerability details are shared here with their knowledge.

*Found this interesting? Subscribe for more agentic AI vulnerability research by Noma Labs, or check out: *GrafanaGhost, DockerDash, Context Crush, GeminiJack. *Looking for an effective Agentic AI Security Solution? Contact us to arrange a demo of Noma’s comprehensive solution.*