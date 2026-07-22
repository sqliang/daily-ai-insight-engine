---
title: 'The token bill comes due: Inside the industry scramble to manage AI’s runaway
  costs'
source: https://techcrunch.com/2026/06/05/the-token-bill-comes-due-inside-the-industry-scramble-to-manage-ais-runaway-costs/
author:
- '[[Rebecca Bellan]]'
published: '2026-06-05'
created: '2026-06-07'
description: '"The whole conversation shifted from tokenmaxxing and ''go fast'' to
  ''we need guardrails, how do we control this?''"'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: be8abe6f7bf0dfa0
source_type: news_media
tldr: 企业因AI token消费失控面临预算危机：Uber在4月就用完全年AI编码预算，微软撤回开发者Claude Code许可，Priceline续约Cursor费用涨4-5倍。Linux
  Foundation宣布成立Tokenomics Foundation，旨在为AI token成本建立类似FinOps的标准化管理框架。
objective_summary: TechCrunch报道了AI token成本飙升导致的企业预算危机。Uber在2026年4月之前已耗尽全年AI编码预算；微软在启用数月后撤销了开发者的Claude
  Code许可；Priceline续约Cursor合同费用上涨4到5倍。OpenAI企业负责人Alexander Embiricos表示客户对话已从功能询问转向成本控制诉求。Linux
  Foundation于本周宣布成立Tokenomics Foundation，致力于为AI token消费建立类似FinOps的成本管控标准。多位企业高管公开讨论了从追求速度到寻求防护栏和治理手段的行业转变。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Uber
  - Microsoft
  - Priceline
  - OpenAI
  - Linux Foundation
  - FinOps Foundation
  - Anthropic
  - Google
  technologies:
  - AI agents
  - tokenomics
  key_people:
  - Alexander Embiricos
  - J.R. Storment
  - Chris Reed
key_logic_flow:
- Uber在2026年4月之前就已耗尽全年AI编码预算，显示出企业AI token消耗速度远超预期。
- 微软在启用开发者Claude Code许可数月后撤销了该许可，反映出企业开始收紧AI工具的使用权限。
- Priceline续约Cursor的合同费用上涨了4到5倍，体现了AI编码工具成本急速攀升的趋势。
- OpenAI企业负责人Alexander Embiricos指出，企业客户关注点已从'能做什么'转向'花费太多，需要可见性和审计能力'。
- Linux Foundation本周宣布成立Tokenomics Foundation，致力于为AI token消费建立标准化的成本管理和治理框架。
- FinOps Foundation执行董事J.R. Storment表示企业正从追求速度转向寻求防护栏和支出控制手段。
extract_result: success
object_mentions:
- object_type: project
  name: Tokenomics Foundation
  canonical_name: Tokenomics Foundation
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Linux Foundation本周宣布组建Tokenomics Foundation，旨在为AI token消费建立类似FinOps的成本管控标准化框架。
  - 新标准组织由FinOps Foundation执行董事J.R. Storment推动，目标直指企业AI token预算超支的生存危机。
  article_id: be8abe6f7bf0dfa0
- object_type: product
  name: Claude Code
  canonical_name: Claude Code
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 微软在启用几个月后撤销了其开发者的Claude Code许可，这是企业收紧AI工具使用的标志性案例。
  - 该案例与其他预算失控事件并列出现，共同揭示了企业AI工具成本失控的普遍性问题。
  article_id: be8abe6f7bf0dfa0
- object_type: product
  name: Cursor
  canonical_name: Cursor
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Priceline员工向TechCrunch透露，该公司的常规Cursor续约合同费用上涨了4到5倍。
  - Priceline高级IT财务总监Chris Reed用'像快克可卡因一样'来形容企业对AI工具的成本依赖困境。
  article_id: be8abe6f7bf0dfa0
- object_type: project
  name: FinOps Foundation
  canonical_name: FinOps Foundation
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - FinOps Foundation是Linux Foundation旗下的项目，其云成本管理框架被Tokenomics Foundation视为核心参考模板。
  - 该基金会执行董事J.R. Storment表示2026年4月和5月已频繁听到企业AI预算超支3倍的生存危机报告。
  article_id: be8abe6f7bf0dfa0
- object_type: model
  name: Claude Opus 4.5
  canonical_name: Claude Opus 4.5
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Anthropic发布的Claude Opus 4.5是2025年11月推动agentic工具能力提升并加剧token消费的新模型之一。
  article_id: be8abe6f7bf0dfa0
- object_type: model
  name: GPT-5.1
  canonical_name: GPT-5.1
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - OpenAI发布的GPT-5.1与同期新模型一起显著改进了agentic工具能力，进而导致企业token消费量成倍增长。
  article_id: be8abe6f7bf0dfa0
- object_type: model
  name: Gemini 3 Pro
  canonical_name: Gemini 3 Pro
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Google的Gemini 3 Pro与Claude Opus 4.5和GPT-5.1同期发布，被文章列为推动token消费暴涨的驱动因素之一。
  article_id: be8abe6f7bf0dfa0
---

Across the industry, companies are starting to balk at the price of AI. Uber blew through its entire 2026 AI coding budget by April. Microsoft revoked its developers’ Claude Code licenses months after enabling them. A Priceline employee told TechCrunch that a routine Cursor contract renewal came back 4-5x more expensive.

Even though per-token prices have fallen, the push for more AI adoption and increasingly autonomous agents have driven token consumption higher and higher. Companies that gorged themselves in early 2025 on all-you-can-eat subscriptions are now scrambling to understand where their money is going, pull back spending, and figure out whether they can salvage some ROI from the wreckage of their budgets.

Meanwhile, a market is forming to meet them there. Startups, established vendors, and a new standards body are all racing to give companies the tools and language to track what they spend.

“Six months ago, I would have a conversation with a customer and it would be all about ‘What can it do? Is it good enough?’” Alexander Embiricos, OpenAI’s head of enterprise, told TechCrunch at an event in New York City this week. “Our conversations are never about that now. Now the conversations are about, ‘hey, we’re spending so much. What visibility do you have? What auditability do you have? What token controls do you have? What is the efficiency of your models?’”

It’s against this backdrop that the Linux Foundation this week unveiled plans for the Tokenomics Foundation, a new standards body that aims to instill the same cost discipline around AI tokens that FinOps did for cloud spend.

“In April and May, I started hearing from companies: ‘Oh my god, we are 3x over our entire 2026 token budget and it’s only April,’” J.R. Storment, executive director of the FinOps Foundation, a project under the Linux Foundation, told TechCrunch. “We started hearing existential crises, and the whole conversation shifted from tokenmaxxing and ‘go fast’ to ‘we need guardrails, how do we control this?’”

The cries heard round the tech world followed fervent demands from CEOs pushing their teams to use the best models and move fast, costs be damned. New models released in November like Anthropic’s Claude Opus 4.5, OpenAI’s GPT-5.1, and Google’s Gemini 3 Pro brought significant improvements to agentic tools, which have multiplied consumption. It’s how one company reportedly found itself with a $500 million Claude bill after forgetting to set usage limits for employees.

“It’s like the crack-cocaine epidemic,” said Chris Reed, senior director of IT finance at Priceline, noting the company had begun placing token limits on certain groups. “They let you try it to get you hooked on it, and now you’re kind of beholden to it.”