---
title: SpaceXAI&#8217;s Grok programming tool was uploading its users&#8217; entire
  codebase to cloud storage
source: https://www.theverge.com/ai-artificial-intelligence/965600/spacexai-grok-build-repository-upload
author:
- '[[Stevie Bonifield]]'
published: '2026-07-14'
created: '2026-07-15'
manifest_dates:
- '2026-07-15'
description: SpaceXAI's Grok Build AI coding tool was spotted uploading users' entire
  codebases to Google Cloud before it was reported, and the company turned it off.
  The Register reports that Cereblab published findings on Monday showing how the
  Grok Build CLI was packaging and uploading entire code repositories, "including
  files it was told not to open [&#8230;]
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 07637df8cbed9afb
source_type: news_media
tldr: SpaceXAI的Grok Build工具被曝自动上传用户完整代码库至云端
objective_summary: 安全研究机构Cereblab发现SpaceXAI的Grok Build CLI工具在用户不知情时将完整代码仓库打包上传至Google
  Cloud，数据量远超同类工具。问题曝光后SpaceXAI关闭了该功能，Elon Musk承诺删除所有已上传数据。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - SpaceXAI
  - Google Cloud
  - Cereblab
  - King's College London
  technologies:
  - Grok Build
  - CLI
  key_people:
  - Elon Musk
  - Lukasz Olejnik
key_logic_flow:
- Cereblab研究发现SpaceXAI的Grok Build CLI工具会自动打包并上传用户完整代码仓库至Google Cloud，数据保留量远超Claude
  Code等同类工具。
- 上传内容包括被明确告知不要打开的文件以及已从Git历史记录中删除的密钥等敏感信息。
- '问题曝光后SpaceXAI禁用了代码库上传功能，服务器返回disable_codebase_upload: true标志，代码库上传不再触发。'
- Elon Musk在X平台回应称所有此前上传的数据将被"完全彻底删除"，同时要求用户允许保留数据以"帮助调试问题"。
- 独立安全研究员Lukasz Olejnik确认此类数据保留属于"过度"行为，可能泄露专有源代码、安全漏洞信息、个人数据和凭证。
- SpaceXAI最初将/privacy命令定位为解决方案，但Cereblab指出该命令是会话级保留开关，并非修复此问题的控制项。
extract_result: success
---

SpaceXAI’s Grok Build AI coding tool was spotted uploading users’ entire codebases to Google Cloud before it was reported, and the company turned it off. *The Register* reports that Cereblab published findings on Monday showing how the Grok Build CLI was packaging and uploading entire code repositories, “including files it was told not to open and secrets deleted from history,” significantly more data retention than similar tools like Claude Code.

# SpaceXAI’s Grok programming tool was uploading its users’ entire codebase to cloud storage

Elon Musk says that all previously uploaded data will be deleted.

Elon Musk says that all previously uploaded data will be deleted.

The researchers say that as of Monday, their tests show SpaceXAI’s servers returning a “disable_codebase_upload: true” flag, and the codebase upload “no longer fires.”

Elon Musk responded to the incident in a post on X claiming that all data Grok Build previously uploaded will be “completely and utterly deleted.” Musk also said in a separate post that “privacy settings are always respected,” but asked users to allow SpaceXAI to retain their data, saying it’s “helpful for debugging issues.”

Dr. Lukasz Olejnik, an independent security researcher at King’s College London, confirmed to *The Verge* that this amount of data retention is “excessive,” adding that the data potentially at risk could include “proprietary source code, information about security vulnerabilities, personal data, infrastructure details, [and] credentials.”

SpaceXAI initially responded to the issue with a post saying that, “If [zero data retention] is disabled, the /privacy command is available in the CLI to disable data retention, which also deletes previously synced data.” However, Cereblab points out that “/privacy is a per-session retention toggle, not the switch that fixed this, so it shouldn’t be pointed to as the control.”

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.