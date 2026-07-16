---
title: Microsoft patches record number of security vulnerabilities, citing its use
  of AI
source: https://techcrunch.com/2026/07/15/microsoft-patches-record-number-of-security-vulnerabilities-citing-its-use-of-ai/
author:
- '[[Zack Whittaker]]'
published: '2026-07-15'
created: '2026-07-16'
manifest_dates:
- '2026-07-16'
description: Microsoft's monthly release of security fixes, dubbed Patch Tuesday,
  resolved a record 570 security vulnerabilities across the company's product line,
  thanks to discoveries with AI.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 9fe6b6cefcefa5fe
source_type: news_media
tldr: 微软在本周"Patch Tuesday"发布570个安全补丁，创历史最高纪录，覆盖Windows、Office等产品线，其中包含至少两个已被积极利用的零日漏洞。微软称补丁数量激增的原因是AI帮助安全团队发现更多此前未被发现的代码漏洞。
objective_summary: 微软于2026年7月15日发布了570个安全补丁，创下历史新高。这些补丁覆盖Windows、Office等多个产品线，其中至少两个零日漏洞已被黑客利用：一个影响Windows
  Server，允许攻击者将受限用户权限提升至系统管理员；另一个影响SharePoint文件共享服务器，美国CISA警告该漏洞正被积极利用以入侵组织机构。微软Windows负责人Pavan
  Davuluri表示，AI帮助安全团队发现更多此前未被发现的漏洞，导致每月安全更新数量大幅增加。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - Microsoft
  - CISA
  technologies:
  - AI
  key_people:
  - Pavan Davuluri
key_logic_flow:
- 微软在2026年7月15日的"Patch Tuesday"例行更新中发布了570个安全补丁，创下该公司单月补丁数量的历史最高纪录。
- 这些补丁覆盖Windows、Office等主要产品线，其中包含至少两个被黑客积极利用的零日漏洞。
- 一个零日漏洞影响Windows Server，允许攻击者将受限用户权限提升至系统管理员级别。
- 另一个零日漏洞影响SharePoint文件共享服务器，美国网络安全机构CISA警告该漏洞正被黑客用于入侵目标组织机构。
- 微软Windows负责人Pavan Davuluri表示，AI正在帮助安全团队发现更多此前未被发现的漏洞，因此客户将在每次安全更新中看到更高数量的补丁。
- 安全研究人员正在使用日益先进的AI模型来挖掘可能在软件代码中存在数年甚至更久的潜伏漏洞。
object_mentions:
- object_type: product
  name: Windows Server
  canonical_name: Microsoft Windows Server
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 文章明确指出一个零日漏洞影响Windows Server，允许黑客将权限从受限用户提升至系统管理员。
  article_id: 9fe6b6cefcefa5fe
- object_type: product
  name: SharePoint
  canonical_name: Microsoft SharePoint
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 文章指出一个零日漏洞影响SharePoint文件共享服务器，CISA警告黑客正利用该漏洞入侵组织机构。
  article_id: 9fe6b6cefcefa5fe
extract_result: success
---

Microsoft released a record number of security patches for Windows, Office, and other tech product lines this week, citing the use of AI to aid the discovery of code vulnerabilities.

The technology and cloud giant issued patches for 570 security flaws on Tuesday as part of its monthly scheduled release of fixes, which security researchers have long dubbed “Patch Tuesday.”

At least two of the vulnerabilities are classified as zero-days, meaning that they were exploited before Microsoft was made aware of them. One bug affecting Windows Server allows hackers to escalate their privileges from a limited user to a system administrator. Another bug affects the SharePoint file sharing server — the U.S. government’s cybersecurity agency CISA has warned hackers were actively exploiting the bug to compromise organizations.

Krebs on Security first reported the news.

The huge patch update comes a week after Microsoft said in a blog post that it expected its usual batch of monthly security patches to be far higher in number than before. The company cited its use of AI to help its employees uncover previously undiscovered security bugs in its software.

“As AI helps defenders discover more issues, customers will see a higher volume of security updates included in each security release,” said Windows boss Pavan Davuluri.

As AI models become more advanced and focused on cybersecurity issues, security researchers are using them to uncover vulnerabilities that may have been dormant in software code for years, if not longer. Parts of Microsoft’s Windows code dates back decades.