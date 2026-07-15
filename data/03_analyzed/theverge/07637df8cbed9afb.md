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
impact_score:
  score: 6.5
  reason: 该事件曝光了AI编程工具在用户不知情下自动上传完整代码库至云端的安全隐患，特别是上传了用户明确排除的文件和已从Git历史中删除的密钥，触及开发者最核心的代码安全红线。虽然SpaceXAI/Grok
    Build并非AI编程工具市场的绝对主力（影响力不及GitHub Copilot、Cursor等），但事件发生在AI编程助手普及率极高的当下，可能引发整个行业对数据隐私处理方式的信任危机。短期冲击力中等偏上，足以促使竞争对手审视自身数据上传策略。
sentiment: negative
developer_sentiment:
  tone: frustrated
  primary_focus: 工具在用户不知情下自动上传完整代码库，且包含被明确排除的文件和已删除的密钥等敏感信息
hype_assessment:
  level: low
  reason: '该事件有Cereblab的独立安全研究作为实证依据，The Register和The Verge双源交叉验证，且SpaceXAI已确认并关闭了该功能（返回disable_codebase_upload:
    true标志）。独立安全研究员Lukasz Olejnik提供了第三方权威点评。这是一个经过充分验证的安全事件，不存在PR包装或概念炒作成分。'
information_entropy: medium
domain_disruption:
  technical_innovation: 无
  business_model: AI编程工具行业面临数据信任危机——用户代码隐私从功能卖点升级为合规底线。此事件可能倒逼所有AI编程助手（Copilot、Cursor、Claude
    Code等）公开披露其代码上传范围和数据保留策略，提前建立透明机制以维护市场信任。
engineering_complexity: production_ready
compound_value:
  score: 2.5
  reason: 从VC视角审视，这是一起负外部性的安全事件，不具备正向复利积累效应。Grok Build被曝自动上传用户完整代码库至Google Cloud，数据保留量远超同类工具（如Claude
    Code），暴露出SpaceXAI在产品安全设计上的严重缺陷。核心投资逻辑链条如下：(1)事件本质是bug修复范畴，SpaceXAI已禁用该功能并承诺删除数据，技术层面不具备持续发酵的基础；(2)对SpaceXAI品牌信任造成一次性打击，但不足以改变AI编程工具赛道的竞争格局——用户切换成本低，且竞争对手早在隐私设计上占有优势；(3)Cereblab的发现虽然引发了行业讨论，但并未创造新的技术范式或商业模式；(4)唯一的长期边际影响是加速了企业客户对AI编程工具数据安全审查标准的收紧，但对整体市场规模的扩张或收缩影响有限。综合判断，该事件属于'爆发-修复-遗忘'的短周期事件，不具备3-5年的复利积累价值。
value_capture_layer: end_application
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- GitHub Copilot
- Cursor
competitive_casualty:
- SpaceXAI
- Grok Build
market_opportunities:
- 可为企业提供AI编程工具的数据安全审计与合规验证服务，帮助检测第三方AI工具是否存在过度数据上传行为
- 开发者可构建隐私优先的本地化AI编程助手，采用端侧推理方案从根本上避免代码库上传至云端
- 企业级AI开发工具的安全合规中间件存在创业机会，用于监控和拦截AI工具的非授权数据传输行为
risk_matrix:
  regulatory: 该事件触发GDPR等多国数据保护法规的合规风险，企业使用AI编程工具可能导致未经用户明确同意的源代码及敏感数据传输至第三方云存储，面临监管处罚和诉讼风险
  technological: AI编程工具普遍采用云端处理模式，类似的数据过度上传问题可能在其他同类工具中同样存在，损害整个AI辅助编程品类的技术可信度
  competitive: 该事件严重打击SpaceXAI的Grok Build在开发者社群中的信任基础，竞争对手（Claude Code、GitHub Copilot、Cursor等）可借此强化隐私安全优势，加速市场份额重构
  ethical: 工具擅自上传完整代码库（含Git历史中已删除的密钥、凭证、安全漏洞信息）严重侵犯用户隐私和数据主权，可能导致企业核心知识产权泄露及第三方数据泄露连锁反应
  additional:
  - Musk要求用户允许保留数据以'帮助调试问题'的表态与承诺'完全删除'自相矛盾，进一步削弱用户信任
  - SpaceXAI最初将不相关的/privacy命令定位为解决方案，暴露其在安全响应流程上的不成熟
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
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