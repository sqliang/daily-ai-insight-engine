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
tldr: Anthropic 公布 Claude Fable 5 网络安全分类器详情及 AI 越狱严重性分级框架草案
objective_summary: Anthropic 在重新部署 Claude Fable 5 后，公开了其网络安全分类器的具体防护范围，并与 Glasswing
  合作提出了 AI 越狱严重性分级框架草案，旨在建立业界统一的越狱风险评估标准，同时启动了 HackerOne 漏洞奖励计划。
event_type: policy_and_safety
epistemic_status: pr_statement
entities:
  companies:
  - Anthropic
  - Glasswing
  - HackerOne
  technologies:
  - safety classifiers
  - AI jailbreak
  key_people: []
key_logic_flow:
- Anthropic 宣布 Claude Fable 5 已重新部署并向全球所有用户开放使用。
- Anthropic 公开了 Fable 5 的网络安全分类器（safety classifiers）详细信息，列出了其设计用于防范和不予防范的具体危害类型。
- 网络安全能力具有双重用途（dual use），同一能力可被用于良性或恶意目的。
- Anthropic 与 Glasswing 合作提出了 AI 越狱严重性分级框架的早期草案，旨在建立统一的越狱风险评估标准。
- 越狱攻击的严重程度差异很大，但目前业界缺乏统一的描述框架来评估其风险。
- Anthropic 启动了 HackerOne 漏洞奖励计划，邀请安全研究人员提交 Fable 5 中发现的潜在网络越狱漏洞。
extract_result: success
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