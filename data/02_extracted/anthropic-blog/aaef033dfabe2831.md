---
title: Fable Safeguards Jailbreak Framework
source: https://www.anthropic.com/news/fable-safeguards-jailbreak-framework
author: []
published: '2026-07-03'
created: '2026-07-03'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: aaef033dfabe2831
manifest_dates:
- '2026-07-03'
- '2026-07-04'
- '2026-07-05'
- '2026-07-06'
- '2026-07-07'
- '2026-07-08'
source_type: tech_blog
tldr: Anthropic 在重新部署 Claude Fable 5 后，发布了其网络安全分类器的详细说明，并与 Glasswing 合作提出了一个 AI 越狱严重性评估框架草案，同时在
  HackerOne 上启动了安全漏洞报告项目。
objective_summary: Anthropic 在重新部署 Claude Fable 5 后，公开了该模型配套的网络安全分类器的详细说明，将网络安全使用行为分为四个类别以区分防御性和攻击性用途。同时，Anthropic
  与 Glasswing 合作发布了一个 AI 越狱严重性评估框架的早期草案，旨在为不同严重程度的越狱行为建立统一的风险描述标准。此外，Anthropic 在 HackerOne
  上启动了漏洞报告项目，邀请安全研究人员提交在 Fable 5 中发现的潜在网络越狱漏洞。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - Glasswing
  technologies:
  - safety classifiers
  - AI jailbreak
  - cybersecurity safeguards
  key_people: []
key_logic_flow:
- Anthropic 在重新部署 Claude Fable 5 后，发布了其网络安全分类器的详细说明，列出了这些分类器旨在预防和未涵盖的危害类型。
- Anthropic 与 Glasswing 合作提出了一个 AI 越狱严重性评估框架草案，旨在为不同严重程度的越狱行为建立统一的风险描述标准。
- 网络安全领域对 AI 安全措施具有特殊挑战性，因为许多网络安全能力具有双重用途，既可防御也可攻击。
- Anthropic 不打算阻止 Fable 5 的所有网络安全活动，而是训练分类器区分四个类别的网络安全使用场景。
- Anthropic 在 HackerOne 上启动了漏洞报告项目，邀请安全研究员提交在 Fable 5 中发现的潜在网络越狱漏洞。
- Anthropic 希望通过与学术界、业界、公民社会和政府的讨论，建立能够实现技术防御用途同时防止滥用的标准。
extract_result: success
object_mentions:
- object_type: product
  name: Fable Safeguards
  canonical_name: Fable Safeguards
  url: https://www.anthropic.com/news/fable-safeguards-jailbreak-framework
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Anthropic 在重新部署 Claude Fable 5 后，发布了其网络安全分类器的详细说明，这些分类器用于检测和阻止危险的网络安全相关使用。
  - 这些分类器将网络安全使用分为四个类别，从最明显有潜在危害到最明显良性的用途，以区分防御性和攻击性行为。
  article_id: aaef033dfabe2831
- object_type: project
  name: AI Jailbreak Severity Framework
  canonical_name: AI Jailbreak Severity Framework
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Anthropic 与 Glasswing 合作提出了一个 AI 越狱严重性评估框架草案，旨在让 AI 开发者与政府用一致的术语讨论每次越狱的风险。
  - 该框架反映了 Anthropic 当前的思考，其目标是引发学术界、业界、公民社会和政府关于如何划定风险界限的讨论。
  article_id: aaef033dfabe2831
- object_type: project
  name: Fable 5 HackerOne Cyber Jailbreak Program
  canonical_name: Fable 5 HackerOne cyber jailbreak program
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Anthropic 在 HackerOne 上启动了一个项目，允许安全研究人员提交他们在 Fable 5 中发现的安全越狱漏洞以供审查。
  article_id: aaef033dfabe2831
---

# More details on Fable 5’s cyber safeguards and our jailbreak framework

Claude Fable 5 has been re-deployed and is now available globally for all users. We’re taking this opportunity to share further information in two areas.

First, we provide more information on the **cybersecurity safeguards**—specifically, the *safety classifiers*—that we launched with the model. These are the AI systems that accompany the model that detect and block dangerous (or potentially dangerous) cybersecurity uses. Here, we provide a detailed list of the types of harms Fable 5’s classifiers are, and are not, designed to prevent.

Second, we lay out an early draft version of **our proposed AI jailbreak severity framework**, on which we’ve been working with our Glasswing partners. AI jailbreaks are unusual ways of prompting an AI model to bypass its safeguards, thus unblocking the behaviors (like dangerous or potentially dangerous cybersecurity tasks) we seek to prevent.

Jailbreaks vary in severity: sometimes they only unblock minor undesirable behaviors, and sometimes they unblock a wide range of harmful outputs, making a model much more dangerous. Yet there is no agreed-upon framework for describing a given jailbreak’s severity. Such a framework would allow AI developers to speak to governments (and vice versa) in consistent terms about the risks posed by each jailbreak.

What we’re sharing today reflects our current thinking. Our hope is to spark a helpful discussion across academia, industry, civil society, and government about how and where these lines should be drawn. We welcome feedback and critique on this framework at cyber-safeguards@anthropic.com. We’ve also launched a HackerOne program where security researchers can submit potential cyber jailbreaks they discover in Fable 5 for our review.

We believe that by working together, we can establish a standard that enables the defensive uses of this technology while preventing its misuse.

## Fable 5’s cyber safeguards

Areas such as cybersecurity are particularly challenging for AI safeguards because they are often *dual use*. That is, many cybersecurity capabilities can be used for benign *or* harmful purposes. For example, we want to allow cyber defenders to use our models to scan their codebases to find software vulnerabilities—but this same capability could, in the wrong hands, be the precursor to a cyberattack.

For that reason, we do not intend to block *all* cybersecurity-related activities for Fable 5. Instead, we train our safety classifiers to discern between four categories of cybersecurity use, from the most clearly potentially dangerous to the most clearly potentially benign. These are summarized in the table below: