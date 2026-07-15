---
title: Claude Sonnet 5 (4 minute read)
source: https://www.anthropic.com/news/claude-sonnet-5?utm_source=tldrai
author: []
published: ''
created: '2026-07-02'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: c3db664df3eb2dfa
manifest_dates:
- '2026-07-02'
source_type: news_media
tldr: Anthropic 发布 Claude Sonnet 5，具更强智能体能力，性能接近 Opus 4.8 但价格更低。
objective_summary: Anthropic 于 2026 年 7 月 15 日发布 Claude Sonnet 5，该模型在推理、工具使用、编程和知识工作方面较
  Sonnet 4.6 显著提升，性能接近 Opus 4.8。定价为每百万输入 token 2 美元、输出 10 美元（优惠至 8 月 31 日），之后调整为 3
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  technologies: []
  key_people: []
key_logic_flow:
- Claude Sonnet 5 是 Anthropic 发布的最新 Sonnet 系列模型，具备更强的智能体能力，在推理、工具使用、编程和知识工作上较 Sonnet
  4.6 显著提升。
- Sonnet 5 性能接近 Opus 4.8，但定价更低，优惠期价格为每百万输入 token 2 美元、输出 token 10 美元。
- 模型即日起在所有套餐中可用，包括 Free、Pro、Max、Team 和 Enterprise 计划，同时在 Claude Code 和 Claude Platform
  中提供。
- 在安全评估中，Sonnet 5 的不良行为率低于 Sonnet 4.6，网络安防能力远低于 Opus 模型，更适合智能体场景使用。
- 早期测试伙伴反馈一致认为 Sonnet 5 能自主完成复杂多步骤任务，包括代码调试、Salesforce 操作、法律研究和浏览器操作等。
- Sonnet 5 支持通过扩展思考调整推理努力水平，用户可在不同成本和性能之间灵活权衡。
extract_result: success
impact_score:
  score: 7.5
  reason: Claude Sonnet 4.6 已是开发者社区广泛使用的模型，Sonnet 5 在推理、工具使用、编码等智能体关键维度上显著超越前代，且性能接近
    Opus 4.8 但定价更低（输入 $2/M → $3/M，输出 $10/M → $15/M），这意味着开发者可以用 Sonnet 级别的成本获得接近 Opus
    级别的智能体能力。该模型立即可用并覆盖所有套餐，配合 extended thinking 机制进一步扩展了性价比选择空间。这不是范式转移，但会实质性地改变
    AI 应用的智能体能力基线——大量中低端智能体应用将直接从这次升级中受益，同时对 OpenAI、Google 等同级模型形成明显的竞争压力。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: Opus 级智能体能力下沉到 Sonnet 价格带，性价比大幅跃升
hype_assessment:
  level: medium
  reason: 文章提供了详细的基准对比（BrowseComp、OSWorld-Verified 的 effort 曲线）、具体定价策略和多个早期测试伙伴的真实用例反馈，存在实质内容。但作为官方发布博文，不可避免地使用了
    'much more agentic'、'substantial improvement' 等积极措辞，且所有合作伙伴评价均为正面，存在选择性呈现。性能数据虽可信，但缺少第三方独立评测的验证，需警惕
    PR 包装成分。
information_entropy: high
domain_disruption:
  technical_innovation: Sonnet 5 的核心突破在于将此前 Opus 模型才具备的高水平智能体能力（自主规划、多步工具调用、代码调试、自我验证）压缩到了更低成本的
    Sonnet 模型上，同时引入了 extended thinking 机制允许用户在不同推理努力水平与成本之间动态权衡，扩展了模型的能力-成本帕累托前沿。
  business_model: $2/$10 的优惠定价（后续 $3/$15）直接拉低了智能体类应用的 token 成本，使得此前因 Opus 价格过高而无法规模化的智能体场景（如自动化代码审查、法律研究、保险理赔处理）具备了商业可行性。这将对依赖
    API 调用的 AI 应用生态产生价格重塑效应，迫使竞争对手调整定价策略。
engineering_complexity: production_ready
compound_value:
  score: 8.0
  reason: Claude Sonnet 5 的发布是一次典型的'性能民主化+定价挤压'策略——以接近 Opus 4.8 的 agentic 能力（推理、工具使用、编程、知识工作），以
    Sonnet 级别的价格（优惠期 $2/$10 per M token）推向市场。其复合价值逻辑在于：(1) 扩展思考机制允许用户弹性调整推理努力水平，覆盖从轻量到高难度
    agentic 工作负载，形成灵活的定价-性能曲线，拓宽 TAM；(2) 早期测试伙伴（Lovable、ClickHouse、Pace 等）反馈高度一致，表明模型在真实多步骤任务中已跨越自主完成的能力阈值，从'辅助工具'进化为'执行层'；(3)
    安全评估改善（不良行为率降低、网络安全能力弱于 Opus）降低了企业部署的治理阻力，加速 enterprise adoption；(4) 全线产品铺开（Free/Pro/Max/Team/Enterprise
    + Claude Code + API）形成平台锁定。但模型层竞争烈度极高，OpenAI/Google 必然快速跟进，长期复利的关键在于 Anthropic
    能否将模型性能优势转化为生态网络效应——即开发者工具链（Claude Code、MCP 等）的粘性和用户数据飞轮——而非仅靠模型基准领先。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- 构建 AI Agent 的应用开发者与初创公司
- Claude API 生态系统
competitive_casualty:
- OpenAI GPT-4o 系列
- Google Gemini 系列
- 传统 RPA 厂商 (UiPath, Automation Anywhere)
- 中小型基础模型公司
market_opportunities:
- 开发者工具和自动化工作流赛道迎来重大利好，可基于 Sonnet 5 构建全自主的多步骤代码调试、测试与修复管线，为中小团队提供此前只有大模型才能实现的智能体能力
- 法律、保险等知识密集型行业可快速将 Sonnet 5 集成到文档分析、案例研究和流程自动化系统中，利用其卓越的多步骤推理能力和较低的成本替代传统人工操作
- 创业公司可利用 Sonnet 5 的扩展思考（extended thinking）机制，针对不同成本敏感度的客户场景提供差异化服务质量——从低成本的快速推理到高精度的深度分析
risk_matrix:
  regulatory: 欧盟 AI Act 等法规对强智能体能力模型的合规要求趋严，自主执行多步骤任务的模型可能面临更高的透明度审计和人类监督义务
  technological: 无
  competitive: OpenAI 和 Google 等竞争对手可能在短期内推出同等价位但性能更优的模型，导致价格战和技术快速迭代，Sonnet 5 的成本优势窗口期有限
  ethical: 模型自主执行复杂多步骤任务的能力增强，若发生错误决策或偏见放大将更难追踪和问责；企业级智能体的大规模部署可能加速中低端知识工作的岗位替代
  additional:
  - 对 Anthropic API 的依赖风险——定价和可用性策略可能随时调整，单一供应商锁定影响长期架构规划
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: strategic_invest
---

# Introducing Claude Sonnet 5

Claude Sonnet 5 is built to be the most agentic Sonnet model yet. It can make plans, use tools like browsers and terminals, and run autonomously at a level that, just a few months ago, required larger and more expensive models.

For many developers, the agentic AI era began with Sonnet-class models: Claude Sonnet 3.5, 3.6, and 3.7 were the first models that showed impressive skills in coding and tool use. More recently, though, the clearest gains in agentic capabilities have been in our Opus-class models.

Sonnet 5 narrows the gap: its performance is close to that of Opus 4.8, but at lower prices. It’s a substantial improvement over its predecessor, Sonnet 4.6, on important aspects of agentic performance like reasoning, tool use, coding, and knowledge work:

Our safety assessments found that Sonnet 5 shows an overall lower rate of undesirable behaviors than Sonnet 4.6, and is generally safer to use in agentic contexts. Evaluations also show that it has a much lower ability to perform cybersecurity tasks than our current Opus models.

From today, Claude Sonnet 5 is available across all plans: it is the default model for Free and Pro plans, and is available to Max, Team, and Enterprise users. It’s also available in Claude Code and on the Claude Platform, where it launches with introductory pricing of $2 per million input tokens and $10 per million output tokens through August 31, 2026, after which it will be priced at $3 per million input tokens and $15 per million output tokens. Developers can use `claude-sonnet-5`

via the Claude API.

## Working with Claude Sonnet 5

The charts below compare the performance of Sonnet 5 with Sonnet 4.6 and Opus 4.8 at different effort levels on the agentic search evaluation BrowseComp and the computer use evaluation OSWorld-Verified. Sonnet 5 (orange line) is a strict improvement over Sonnet 4.6 (gray line) and covers a much wider range of cost-performance options than Opus 4.8 (yellow line). It provides substantially improved cost efficiency at medium effort; its higher-effort performance can match Opus 4.8 on some tasks. Between Sonnet 5 and Opus 4.8, users can adjust the effort level to find the right balance of cost and performance.

Feedback from our early access partners has been consistent: Sonnet 5 is much more agentic than its predecessors. Testers described how it finishes complex tasks where previous Sonnet models would stop short, how it checks its own output without explicitly being asked, and how it does all this agentic work at an attractive price point:

Claude Sonnet 5 gives our agents a strong execution layer for multi-step software engineering work. It handles sustained coding, tool use, and debugging well across messy technical contexts, and has been especially useful for workflows where follow-through and technical grounding matter.

We handed Claude Sonnet 5 a two-part job—update Salesforce account tiers, send a launch announcement to enterprise contacts—and it finished end to end. That used to stall halfway. For day-to-day automation, it’s a no-brainer.

Claude Sonnet 5 gets more done with less. Same output quality, fewer steps to get there. It refuses unsafe requests cleanly and consistently, too. At Lovable, we’re putting powerful tools in the hands of millions of builders. A model that knows when to say no is just as important as one that knows how to build.

We ran Claude Sonnet 5 against dozens of our most challenging real pull requests, and it carried each one through to a tested, verified result on its own — freeing our engineers to focus on the judgment, the decision, and the final sign-off.

I asked Claude Sonnet 5 to investigate a bug. Unprompted, it wrote a reproducing test, implemented the fix, then stashed it to confirm the bug came back without the change. All in a single pass.

With Claude Sonnet 5, agents stay on plan, follow our conventions, and ship clean multi-step changes, all at an efficient cost.

Claude Sonnet 5 is at its best on brownfield code—race conditions, hidden tests, the parts nobody wants to touch. It traces a failure to its actual root cause and ships a durable fix instead of patching the symptom.

Claude Sonnet 5 sits on the Pareto frontier for Eve’s plaintiff-law tasks. We see the clearest gains in legal research and analysis, at a price-to-performance ratio that made the choice to migrate easy.

ClickHouse agents explore live data and produce insights on the fly, so time-to-insight matters when testing new models. Claude Sonnet 5 reasons in tighter steps and gets our users to answers noticeably faster. That speed is a difference our customers feel.

At Pace, our computer-use agents run insurance workflows—submission intake, FNOL, loss runs—on the systems our operations teams already use. Claude Sonnet 5 consistently takes the right action and does it quickly, which is what real insurance work demands.

## Safety evaluations