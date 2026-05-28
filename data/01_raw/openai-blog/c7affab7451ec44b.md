---
title: Building self-improving tax agents with Codex
source: https://openai.com/index/building-self-improving-tax-agents-with-codex
author: []
published: '2026-05-27'
created: '2026-05-28'
description: See how OpenAI, Thrive, and Crete built a self-improving tax agent with
  Codex, automating filings, improving accuracy, and accelerating workflows.
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: c7affab7451ec44b
---

*How Thrive Holdings and OpenAI co-developed Tax AI for Crete accountants by fusing practitioner expertise with a Codex-driven loop*

Real-world systems behave differently in production than they do in a lab, breaking in ways that are hard to anticipate before deployment. Teams often discover those failures after launch, then spend weeks inspecting edge cases, adjusting prompts, and translating production feedback into durable product improvements. The feedback loop is manual and slow, and only improves when an engineer advances it. But today, with thoughtfully designed eval infrastructure, direct access to practitioners and real world environments, and the frontier agentic capabilities of Codex, you can build agents that self-improve.

In this post, we’ll unpack how we used Codex to build this type of agent. Over the past six months, OpenAI forward deployed engineers and researchers along with Thrive Holdings’ engineers collaborated to build Tax AI alongside and for __Crete__(opens in a new window)’s network of 30+ accounting firms to help prepare increasingly complex tax returns. Instead of relying on engineers to find and fix each failure, Tax AI uses Codex to turn production use into structured signals that fuel autonomous improvement.

Crete practitioners prepare tens of thousands of tax returns each season which requires working through millions of underlying documents. For medium- to large-complexity filings, data entry alone can take eight hours per return, often involving messy data sources, prior-year documents, and manual extraction and calculation. They pointed us to tax preparation as a significant bottleneck during the busiest stretch of tax season.

To solve this problem, Tax AI processed 7,000 tax returns across the Crete firms that participated in the pilot this tax season. The system automates much of the time-intensive process of preparing 1040 and 1041 tax returns, but even more compelling than the efficiency gains is that the system itself is measurably better than the version that was first deployed three months ago.

In Tax AI, practitioners upload source files along with any client-specific notes. Tax AI then creates a tax engine submission, ready for review. It saves practitioners about a third of their time on tax preparation, drafts returns with up to 97% accuracy, and increases throughput by about 50%, creating more room for them to spend time with clients.

We can quantify this improvement by understanding how accurately Tax AI can complete a return without needing correction later. We measure accuracy by checking what share of returns reach 75%, 90%, or 100% correct field completion. At launch, only a quarter of returns were at 75% correct field completion, but within six weeks, 86% hit that mark. The system showed even faster growth at the 90% and 100% correct field completion levels. These thresholds give us a practical view of how much practitioner follow-up different returns still require.