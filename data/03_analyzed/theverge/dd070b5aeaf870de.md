---
title: Google’s NotebookLM can sum up your research in a TikTok-style clip
source: https://www.theverge.com/tech/959778/google-notebooklm-ai-clips
author:
- '[[Emma Roth]]'
published: '2026-06-30'
created: '2026-07-01'
description: 'Google''s NotebookLM is adding a new way to catch up on your notes:
  TikTok-style AI videos. The new feature is rolling out to Google AI Ultra and Pro
  subscribers, allowing NotebookLM to generate 60-second vertical AI clips based on
  the sources you upload to the app. The example shared by Google details Australia''s
  unsuccessful war [&#8230;]'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: dd070b5aeaf870de
manifest_dates:
- '2026-07-01'
source_type: news_media
tldr: Google NotebookLM 新增 TikTok 风格 AI 短视频功能
objective_summary: Google 向 NotebookLM 的 AI Ultra 和 Pro 订阅用户推出 AI Clips 功能，可根据用户上传的资料自动生成带
  AI 图像和旁白的 60 秒竖版短视频，目前仅支持英文，免费用户即将获得支持。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Google
  technologies:
  - NotebookLM
  - AI Clips
  key_people: []
key_logic_flow:
- Google 为 NotebookLM 新增了 AI Clips 功能，可根据用户上传的资料生成 60 秒竖版 AI 短视频。
- 该功能面向 Google AI Ultra 和 Pro 付费订阅用户开放，免费用户后续也会获得支持。
- 生成的视频包含 AI 生成的图像和旁白，风格类似 TikTok 短视频。
- 此前 NotebookLM 已支持 AI 播客、电影式视频和可视化讲解等交互方式。
- 该功能目前仅支持英文，用户可在网页端或 App 中选择笔记本后通过 Studio 面板生成视频。
extract_result: success
impact_score:
  score: 3.5
  reason: 该事件是 Google NotebookLM 的一项产品功能更新，在其已有的 AI 播客、电影式视频和可视化讲解等输出格式基础上新增竖版短视频格式。这属于日常产品迭代范畴：功能面向付费订阅用户逐步开放，仅支持英文，且短视频格式对严肃研究场景的价值有限。既未改变
    AI 行业竞争格局，也未引入底层技术突破。参考评分标准，属于 '日常更新，小圈子自嗨' 的区间上限（3.5分）。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: 短视频格式在严肃研究场景下的实用性存疑，更期待 NotebookLM 在深度分析能力上的改进而非输出形式的花样
hype_assessment:
  level: medium
  reason: 功能本身是真实可用的产品更新，但 'TikTok-style' 的称呼明显借势短视频热度进行包装宣传。本质上 NotebookLM 此前已具备多模态输出能力（AI播客、电影式视频），AI
    Clips 只是新增了一个竖版格式维度，并非革命性创新。The Verge 的报道较为客观地描述了功能范围与限制，但 Google 的产品宣发中存在典型的
    PR 包装成分——将体验优化包装为新一代交互范式。
information_entropy: medium
domain_disruption:
  technical_innovation: 无本质技术突破。AI Clips 整合了文本摘要、AI 图像生成（基于 Imagen 系列模型）、语音合成等既有成熟技术，将多模态输出维度从横版扩展到竖版短视频。技术架构上属于产品层面的
    feature 集成，不涉及底层模型架构或训练范式的创新。
  business_model: 将新功能置于付费墙后（AI Ultra/Pro 订阅），有助于提升 NotebookLM 的付费转化率，并推动其定位从 '研究辅助工具'
    向 '轻量内容生成平台' 延伸。但对 AI 行业整体商业模式或 SaaS 生态的影响有限，更多是 Google 生态内的功能差异化策略。
engineering_complexity: production_ready
compound_value:
  score: 5.0
  reason: NotebookLM 的 AI Clips 功能本身是增量特性，而非平台级创新。但其长期复利价值体现在两个维度：一是 NotebookLM 正在构建'文本→多模态输出'的能力矩阵（播客/电影视频/短剧/可视化讲解），每种新模态都增强用户粘性和数据飞轮效应；二是短视频形态天然适配移动端与社交传播，可能为
    NotebookLM 带来新的用户增长入口。然而，该功能技术门槛不高（可被 Synthesia 等 AI 视频工具快速复制），且依赖 Google 生态内的封闭用户群（付费订阅），短期内难以形成独立商业闭环。综合评估：作为
    NotebookLM 生态的有机组成有 5 分潜力，但独立复利效应有限。
value_capture_layer: end_application
moat_impact: democratizes_access
key_beneficiaries:
- Google
- NotebookLM 付费用户（研究人员/学生/知识工作者）
competitive_casualty:
- Synthesia
- HeyGen
- Runway
- 传统知识管理工具（Evernote/Notion 等，若缺乏 AI 视频能力）
market_opportunities:
- 知识类短视频创作者可基于 NotebookLM AI Clips 模式开发自动化内容生产工作流，将研究报告、论文或课程资料一键转为短视频摘要
- 企业培训与内部知识管理场景可参考此功能，开发将内部文档、培训手册自动转化为短视频学习材料的效率工具
- 教育科技领域可借鉴该交互范式，打造面向学生的文献阅读辅助工具，将长篇学术论文自动提炼为60秒竖版知识卡片视频
risk_matrix:
  regulatory: AI 生成短视频涉及的内容真实性标识义务（如深度合成标注）在不同司法辖区要求不一，若旁白或图像出现事实性错误可能面临虚假信息传播监管风险
  technological: AI 图像生成质量和旁白自然度仍有提升空间，若输出效果不佳可能影响用户留存；竞争对手可快速复制同类功能，技术壁垒有限
  competitive: 短视频平台（TikTok、YouTube Shorts）及 AI 助手产品（ChatGPT、Copilot）均可能推出类似的知识短视频生成功能，NotebookLM
    面临多方向竞争挤压
  ethical: AI 自动生成的旁白和图像可能包含幻觉或事实错误，短视频的快速消费特性降低了用户的批判性核查意愿，容易加速 misinformation 传播
  additional: []
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: monitor
---

Google’s NotebookLM is adding a new way to catch up on your notes: TikTok-style AI videos. The new feature is rolling out to Google AI Ultra and Pro subscribers, allowing NotebookLM to generate 60-second vertical AI clips based on the sources you upload to the app.

# Google’s NotebookLM can sum up your research in a TikTok-style clip

The 60-second videos summarize your sources with AI-generated images and narration.

The 60-second videos summarize your sources with AI-generated images and narration.

The example shared by Google details Australia’s unsuccessful war on emus, pairing paper cutout-style AI art of emus with narration. It adds to some of the other ways NotebookLM lets you interact with your research, including by generating AI podcasts, cinematic videos, and visual explainers.

To generate a 60-second clip, head to NotebookLM on the web or app, select a notebook, and then choose “Video” from the Studio column on the right side of the screen. From there, select “Short,” choose the topic you’d like NotebookLM to focus on (or enter your own), and then hit the “Generate” button.

The feature is rolling out in English only for now, with support for free users coming “soon.”

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.