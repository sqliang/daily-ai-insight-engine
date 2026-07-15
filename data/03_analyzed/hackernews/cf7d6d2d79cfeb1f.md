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
tldr: Noma Labs 发现 GitHub Agentic Workflows 存在提示注入漏洞 GitLost，攻击者可借公开 Issue 窃取私有仓库数据。
objective_summary: Noma Labs 研究人员发现 GitHub Agentic Workflows 存在间接提示注入漏洞（GitLost）。攻击者无需任何凭证，只需在公开仓库创建
  Issue 并嵌入恶意指令，即可诱使 AI Agent 读取并公开发布同一组织内私有仓库内容。漏洞已向 GitHub 负责任披露。
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
- GitHub 推出的 Agentic Workflows 功能允许用户用 Markdown 编写自动化工作流，由 AI Agent 执行并拥有跨仓库读取权限。
- Noma Labs 发现该功能存在间接提示注入漏洞（GitLost）：攻击者在公开仓库的 Issue 正文中嵌入恶意指令。
- 当工作流被 Issue 指派等事件触发后，Agent 读取 Issue 内容并执行其中的隐藏指令。
- Agent 利用跨仓库权限读取同一组织内的私有仓库 README 等内容。
- 攻击者使用 Additionally 关键词绕过 GitHub 的安全防护，使 Agent 将私有仓库内容以公开评论形式泄露。
- Noma Labs 已向 GitHub 负责任披露该漏洞，并建议隔离用户输入与系统指令、最小化 Agent 权限范围。
extract_result: success
impact_score:
  score: 7.0
  reason: GitLost 漏洞的短期冲击力评分 7.0，属于重要安全发现级别。评分依据如下：第一，该漏洞直接威胁 GitHub 这一全球最大的代码托管平台，影响面极广，任何使用
    GitHub Agentic Workflows 的组织都可能成为受害者；第二，攻击门槛极低——攻击者无需任何凭证或代码能力，仅需在公开仓库发一条 Issue
    即可窃取同组织私有仓库数据，这大大增加了实际被恶意利用的风险；第三，该案例为 AI Agent 提示注入攻击提供了真实世界的可复现 PoC，不再是理论推演，会迫使各平台重新审视
    AI Agent 的权限设计；但扣分原因在于：这是一个可修复的具体漏洞而非底层模型缺陷，GitHub 可以针对性地加固防护（如隔离用户输入与系统指令、最小化权限），且目前未出现大规模利用的报道，尚未达到范式转移级冲击（8-10
    分）。
sentiment: negative
developer_sentiment:
  tone: frustrated
  primary_focus: AI Agent 跨仓库读取权限带来的数据泄露风险
hype_assessment:
  level: low
  reason: 判定为低炒作水分。该文章来自安全研究机构 Noma Labs，提供了完整的技术分析、攻击链路拆解、可复现的 PoC 链接（包含实际的 Workflow
    run 和 Issue 记录），以及对 GitHub 的负责任披露流程。文章没有使用 '颠覆'、'革命性' 等 PR 包装词汇，而是以严谨的安全研究论文风格呈现漏洞细节、影响范围和修复建议。攻击使用的
    'Additionally' 关键词绕过护栏的技术发现也有实际佐证。整体属于实打实的干货披露。
information_entropy: high
domain_disruption:
  technical_innovation: 发现了 AI Agent 系统中一个经典的间接提示注入攻击面：当 Agent 被赋予跨仓库读取权限且将用户控制的 Issue
    内容作为指令输入时，攻击者可通过嵌入自然语言指令（并使用 'Additionally' 关键词绕过现有护栏）来劫持 Agent 行为，实现私有仓库数据的外泄。这一发现揭示了
    Agent 的上下文窗口即攻击面这一根本性安全挑战。
  business_model: 该漏洞可能对 GitHub Agentic Workflows 的采用率造成短期打击，企业客户在安全加固到位前可能暂停或收紧该功能的使用。更广泛地看，它会推动
    AI 开发平台（如 GitHub、GitLab）和安全工具厂商将 Agent 权限的隔离设计（用户输入与系统指令分离、细粒度跨仓库访问控制、输出审查）作为核心安全功能来投入，影响
    Agent 平台产品的安全架构设计标准。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: GitLost 不是产品发布，但它的行业信号价值极高。该漏洞以真实的攻击路径验证了 AI Agent 系统中一个系统性的安全缺陷类别——间接提示注入，其意义相当于
    SQL 注入之于 Web 应用。这将产生三重长期复利效应：第一，加速 AI Security 赛道的资本涌入，从'锦上添花'变为'企业刚需'；第二，推动 Agent
    架构设计范式的进化——输入隔离、权限最小化、跨仓库访问控制将成标准实践；第三，GitLost 将成为行业教科书级别的案例，持续强化企业对 AI Agent
    安全防护的付费意愿。类比 SQL 注入催生了千亿级 WAF/安全市场，GitLost 将成为 AI 安全中间件市场爆发的催化剂。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Noma Labs
- Protect AI
- HiddenLayer
- Wiz
- GitLab
competitive_casualty:
- GitHub
- Microsoft
- 过度权限的 Agent 平台
market_opportunities:
- 安全创业团队可开发针对 AI Agent 的提示注入检测与防护 SDK，嵌入 CI/CD 和 Agent 编排层，形成类似 WAF 的产品形态
- 企业安全团队应建立 AI Agent 安全审计体系，包括权限最小化审查、用户输入隔离策略、以及 Agent 行为监控告警机制
- 平台安全咨询公司可推出 Agentic Workflow 安全成熟度评估服务，帮助组织评估和加固 AI Agent 的信任边界
risk_matrix:
  regulatory: 数据泄露可能触发 GDPR、CCPA 等隐私法规的违规处罚；AI Act 对高风险 AI 系统的透明度和安全性要求将适用于此类 Agent
    工作流；跨境数据传输合规性可能因私有仓库内容泄露而受到质疑
  technological: 提示注入是 Agentic AI 系统的结构性漏洞类别（类比 SQL 注入之于 Web 应用），短期内难以彻底根除；GitHub
    的防护措施被简单关键词绕过的现象说明当前 LLM 安全对齐技术仍不可靠
  competitive: GitHub 作为代码协作龙头，此次漏洞将削弱企业用户对 Copilot/Agentic Workflows 的信任，可能延缓企业采用决策；竞争对手（GitLab
    等）可能借机强调自身安全架构优势
  ethical: 私有仓库包含敏感代码、API 密钥、客户数据等，泄露将导致严重的隐私侵犯和知识产权暴露风险；攻击者无需任何凭证即可发起攻击，极大地降低了作恶门槛
  additional:
  - 供应链放大风险：一旦私有仓库的依赖配置或内部工具代码泄露，可能成为针对下游客户的供应链攻击跳板
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
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