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
pipeline_stage: ingested
id: bb72d97feb83ab4b
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