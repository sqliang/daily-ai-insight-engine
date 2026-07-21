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
tldr: SpaceXAI的Grok Build AI编码工具被发现将用户完整代码仓库上传至Google Cloud存储，包括被指示忽略的文件和已删除的密钥，该功能被曝光后已关闭，Elon
  Musk声称所有已上传数据将被彻底删除。
objective_summary: Cereblab于周一发布研究结果，发现SpaceXAI的Grok Build CLI工具将用户完整代码仓库打包并上传至Google
  Cloud，其数据保留量远超同类工具。SpaceXAI随后在服务器端返回disable_codebase_upload:true标志并关闭上传功能。Elon Musk在X平台回应称所有已上传数据将被彻底删除，同时请求用户允许保留数据以便调试。独立安全研究员Lukasz
  Olejnik确认此数据保留量已构成过度收集。
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
  - Dr. Lukasz Olejnik
key_logic_flow:
- Cereblab发布研究结果，显示SpaceXAI的Grok Build CLI工具会将用户的完整代码仓库打包并上传至Google Cloud存储。
- 该工具上传的数据包括被明确指示不要打开的文件以及已从版本历史中删除的密钥，数据保留量远超类似工具如Claude Code。
- SpaceXAI在问题曝光后关闭了该功能，服务器端返回disable_codebase_upload:true标志，代码库上传功能不再触发。
- Elon Musk在X平台回应称所有已上传数据将被彻底删除，但同时请求用户允许保留数据，称其有助于调试问题。
- 独立安全研究员Lukasz Olejnik确认此数据保留量属于过度收集，可能泄露专有源代码、安全漏洞信息、个人数据、基础设施详情和凭证。
- SpaceXAI最初建议用户通过/privacy命令关闭数据保留，但Cereblab指出该命令仅为会话级保留开关，并非真正修复此问题的控制项。
extract_result: success
object_mentions:
- object_type: product
  name: Grok Build
  canonical_name: SpaceXAI Grok Build
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - SpaceXAI的Grok Build CLI工具被发现将用户完整代码仓库打包并上传至Google Cloud存储，包括被指示不要打开的文件和已从历史记录中删除的密钥。
  - Cereblab的测试显示，SpaceXAI的服务器在问题曝光后返回disable_codebase_upload:true标志，代码库上传功能已不再触发。
  - Elon Musk回应称Grok Build之前上传的所有数据将被彻底删除，但他同时请求用户允许SpaceXAI保留数据以用于调试。
  article_id: 07637df8cbed9afb
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