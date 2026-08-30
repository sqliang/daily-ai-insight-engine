---
title: Binance now lets AI agents trade, but keeping them in check is largely up to
  users
source: https://techcrunch.com/2026/08/20/binance-now-lets-ai-agents-trade-but-keeping-them-in-check-is-largely-up-to-users/
author:
- '[[Jagmeet Singh]]'
published: '2026-08-20'
created: '2026-08-20'
manifest_dates:
- '2026-08-20'
description: Binance's Agent OS works with tools including ChatGPT, Claude Code, and
  Cursor.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: bb72d97feb83ab4b
source_type: news_media
tldr: 币安周四推出 Agent OS 平台，让 AI 代理接入其金融基础设施代表用户分析市场并执行交易，兼容 ChatGPT、Codex、Claude Code、Cursor
  及 MCP。风控主要依赖用户，通过默认禁提款的子账户限制代理权限与资金规模。
objective_summary: 币安（全球最大加密货币交易所，注册用户超 3 亿）于 2026 年 8 月 20 日推出 Agent OS 平台，允许开发者将
  AI 应用与代理连接到其金融基础设施，代表用户分析市场并执行交易。平台整合了币安现有 API、Binance Wallet Agentic Hub、x402 交易验证、Binance
  Skill Hub，并新增对 MCP 的支持，兼容 ChatGPT、Codex、Claude Code 和 Cursor。币安通过可配置的专用子账户（默认禁止提款）将访问控制权交给用户，用户可决定代理每笔订单需审批或自主执行，转入子账户的资金即构成交易上限。币安表示无法查看代理交易的推理过程，现有子账户
  API 的安全、风控与反洗钱政策在 Agent OS 上线时同样适用。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Binance
  - OpenAI
  - Anthropic
  technologies:
  - MCP
  - x402
  - AI Agent
  key_people:
  - Jeff Li
key_logic_flow:
- 币安于周四推出 Agent OS 平台，允许开发者将 AI 应用与代理接入其金融基础设施，实现代表用户分析市场和执行交易。
- 该平台整合了币安现有 API、Binance Wallet Agentic Hub、x402 交易验证、Binance Skill Hub，并新增对 Model
  Context Protocol（MCP）的支持。
- Agent OS 兼容 OpenAI 的 ChatGPT 和 Codex、Anthropic 的 Claude Code 以及 Cursor，用户可授权这些代理访问市场数据、查看账户信息并执行交易。
- 币安将风控责任主要交给用户，通过专用子账户对代理进行访问控制，子账户默认禁止提款以形成资金保护沙箱。
- 用户可选择代理每笔订单需审批或配置权限后自主执行，币安不设单独的亏损上限，转入子账户的金额即为实际限制。
- 币安无法查看代理交易的推理过程，只能监控交易结果，对错误信息或操纵的影响可见性有限，子账户是对抗提示注入攻击的主要防线。
object_mentions:
- object_type: product
  name: Agent OS
  canonical_name: Binance Agent OS
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 币安于本周四推出名为 Agent OS 的平台，允许开发者将 AI 应用和代理连接到币安的金融基础设施，让 AI 代理代表用户分析市场并执行交易。
  - Agent OS 将访问控制放在账户级别，用户通过专用子账户为代理配置现货或期货交易权限，默认阻止从子账户提款。
  article_id: bb72d97feb83ab4b
- object_type: product
  name: Binance Wallet Agentic Hub
  canonical_name: Binance Wallet Agentic Hub
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Agent OS 整合了币安现有的 Binance Wallet Agentic Hub 工具，作为连接 AI 代理与币安金融基础设施的组成部分。
  article_id: bb72d97feb83ab4b
- object_type: project
  name: Binance x402
  canonical_name: Binance x402
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Agent OS 纳入币安 x402 交易验证与支付促进器 API，为 AI 代理的交易执行提供验证能力。
  article_id: bb72d97feb83ab4b
- object_type: product
  name: Binance Skill Hub
  canonical_name: Binance Skill Hub
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Agent OS 整合了币安 Skill Hub，使开发者能够将技能接入到代理的金融操作流程中。
  article_id: bb72d97feb83ab4b
- object_type: project
  name: MCP
  canonical_name: Model Context Protocol (MCP)
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Agent OS 新增了对 Model Context Protocol（MCP）的支持，并可与 ChatGPT、Codex、Claude Code 和 Cursor
    等工具配合使用。
  article_id: bb72d97feb83ab4b
- object_type: product
  name: Codex
  canonical_name: OpenAI Codex
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Agent OS 支持 OpenAI 的 Codex，用户可授权该代理访问市场数据、查看账户信息并执行交易。
  article_id: bb72d97feb83ab4b
- object_type: product
  name: Claude Code
  canonical_name: Claude Code
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Agent OS 支持 Anthropic 的 Claude Code，让用户授权代理在币安平台进行市场分析与交易操作。
  article_id: bb72d97feb83ab4b
- object_type: product
  name: Cursor
  canonical_name: Cursor
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Agent OS 支持 Cursor 工具，用户可授权该代理访问市场数据、查看账户信息并执行交易。
  article_id: bb72d97feb83ab4b
- object_type: product
  name: ChatGPT
  canonical_name: ChatGPT
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Agent OS 支持 OpenAI 的 ChatGPT，用户可授权该代理访问市场数据、查看账户信息并执行交易。
  article_id: bb72d97feb83ab4b
extract_result: success
---

Binance, the world’s largest crypto exchange with more than 300 million registered users, on Thursday launched a platform that lets AI agents analyze markets and execute trades on users’ behalf, bringing autonomous AI directly into the business of managing real money.

Called Agent OS, the platform lets developers connect AI applications and agents to Binance’s financial infrastructure. It brings the exchange’s existing tools and services such as Binance APIs, Binance Wallet Agentic Hub, Binance x402 transaction verification and payment facilitator API, and Binance Skill Hub, along with newly introduced support for its Model Context Protocol (MCP). The platform also works with tools including OpenAI’s ChatGPT and Codex, Anthropic’s Claude Code, and Cursor, allowing users to authorize agents to access market data, view account information, and execute trades.

However, as the AI race moves away from chatbots that answer questions to agents capable of taking action, Binance is putting much of the responsibility for keeping them in check on users, who ultimately have to decide what agents can access and trade and set limits on what they can do.

“Instead of total freedom, we put the power in users’ hands to give them the granular access control of what they can do through the agent,” said Jeff Li, vice president of product at Binance, in an interview. “We put [the control] at the account level to protect the users’ funds.”

Binance does that primarily through dedicated “sub-accounts”, which users can assign to agents and configure for specific activities, such as spot or futures trading. Withdrawals from those sub-accounts are blocked by default, Li told TechCrunch, creating a sandbox around an agent’s activity.

Users can also choose whether an AI agent must seek approval for every order or can execute trades autonomously once its permissions are configured, a Binance representative said. Binance does not impose a separate cap on how much an AI agent can trade or lose, so the amount a user transfers into the sub-account effectively serves as the limit.

Asked whether Binance can see what leads an agent to make a particular trade, Li said the reasoning happens outside its systems, either on the user’s computer or within their chosen AI application. “We really cannot see the reasoning of what the user’s action is,” he said.

That means Binance can monitor an agent’s resulting trading activity, but has limited visibility into whether a decision was influenced by faulty information or manipulation.

Li again pointed to the sub-account as the main line of defense when asked what would happen if an agent were manipulated through a prompt-injection attack or otherwise compromised. Binance also said its existing security, risk-control, and anti-money-laundering policies for subaccount APIs apply to Agent OS at launch.