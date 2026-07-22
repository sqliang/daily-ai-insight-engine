---
title: Claude Design Anthropic Labs
source: https://www.anthropic.com/news/claude-design-anthropic-labs
author: []
published: '2026-05-28'
created: '2026-06-01'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 0dba0c3d7be35ac4
source_type: tech_blog
tldr: Anthropic 发布 Claude Design，这是一款基于 Claude Opus 4.7 的视觉设计协作产品，支持创建原型、幻灯片、营销素材等视觉作品，已面向
  Pro、Max、Team 和 Enterprise 订阅用户开放研究预览。
objective_summary: 2026年7月21日，Anthropic 通过官方博客宣布推出 Anthropic Labs 的首款产品 Claude Design。该产品由
  Claude Opus 4.7 视觉模型驱动，用户可通过自然语言描述需求，与 Claude 协作创作设计稿、原型、幻灯片和一页纸等视觉作品。Claude Design
  支持导入团队设计系统、从代码库读取品牌规范，并提供内联评论、直接编辑和自定义滑块等精细化控制功能。该产品以研究预览形式面向 Claude Pro、Max、Team
  和 Enterprise 订阅用户逐步开放。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Anthropic
  technologies:
  - Claude Opus 4.7
  key_people: []
key_logic_flow:
- Anthropic 推出 Anthropic Labs 的首款产品 Claude Design，这是一款基于 Claude Opus 4.7 的视觉设计协作工具。
- Claude Design 以研究预览形式向 Claude Pro、Max、Team 和 Enterprise 订阅用户逐步开放。
- 用户可以通过自然语言描述需求，由 Claude 搭建初版，再通过对话、内联评论、直接编辑或自定义滑块进行精细化调整。
- Claude Design 在 onboarding 阶段通过读取团队代码库和设计文件自动构建设计系统，后续项目自动使用统一的颜色、字体和组件。
- 团队已将 Claude Design 用于交互原型、产品线框图、设计探索、提案演示、营销物料和前沿设计等多种场景。
- 用户可以从文本提示、上传文件或代码库导入内容，最终可导出为 PPTX 或发送到 Canva。
extract_result: success
object_mentions:
- object_type: product
  name: Claude Design
  canonical_name: Claude Design
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Anthropic 推出了 Anthropic Labs 的首款产品 Claude Design，允许用户与 Claude 协作创建设计稿、原型、幻灯片等视觉作品。
  - Claude Design 由 Claude Opus 4.7 驱动，以研究预览形式面向 Claude Pro、Max、Team 和 Enterprise
    订阅用户开放。
  - Claude Design 支持导入团队设计系统，用户可通过内联评论、直接编辑和自定义滑块进行精细化调整。
  article_id: 0dba0c3d7be35ac4
- object_type: model
  name: Claude Opus 4.7
  canonical_name: Claude Opus 4.7
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Claude Design 由 Anthropic 目前最强的视觉模型 Claude Opus 4.7 驱动。
  article_id: 0dba0c3d7be35ac4
- object_type: product
  name: Claude Code
  canonical_name: Claude Code
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 产品经理可以把功能流程草图交给 Claude Code 进行实现，或者与设计师协作进一步细化。
  article_id: 0dba0c3d7be35ac4
impact_score:
  score: 6.5
  reason: 该产品将Claude从文本/代码助手扩展到视觉设计领域，定位清晰且具备差异化亮点：自动从代码库构建设计系统、与Claude Code的线框图到代码交付闭环。这些功能填补了现有AI设计工具（如Galileo
    AI、Visily）与开发工作流之间的断层。但作为研究预览版、逐步开放而非全面上线，且设计工具赛道竞争激烈（Figma已有AI功能、Canva深度集成AI），短期内不至于改写格局，更多是Anthropic平台能力的战略性扩展。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: Claude Code 的线框图到代码交付闭环，以及自动从代码库构建设计系统的能力
hype_assessment:
  level: low
  reason: 文章没有使用'颠覆性'、'革命性'等PR高频词汇，而是通过列出具体的应用场景（原型设计、线框图、演示文稿、营销物料）和功能细节（入职构建设计系统、导入DOCX/PPTX/XLSX、行内评论、滑块控制）来展示产品能力。明确标注为研究预览版，语调务实。
information_entropy: medium
domain_disruption:
  technical_innovation: 通过入职阶段读取代码库和设计文件自动构建团队级设计系统，使后续所有项目自动应用团队色彩、字体和组件，实现了开发与设计资产的双向同步。结合Claude
    Opus 4.7的多模态视觉能力，支持从文本提示、上传文档到网页抓取的多元化输入，以及行内评论、滑块调节等细粒度控制机制。
  business_model: 将设计工具嵌入Claude订阅体系（Pro/Max/Team/Enterprise），增强了订阅粘性；与Claude Code形成'设计→开发'内部闭环，可能重塑中小团队从设计到开发的协作流程，对Figma、Sketch、Canva等传统设计工具形成差异化竞争压力。
engineering_complexity: prototype
compound_value:
  score: 7.5
  reason: Claude Design 是 Anthropic 从语言/代码模态向视觉模态的关键战略扩展，复利效应体现在三层：1）设计系统自动构建功能（读取代码库+设计文件）创造强企业锁定——团队将色彩/字体/组件体系托管后迁移成本极高；2）与
    Claude Code 形成'线框稿→生产代码'闭环，这是 Figma 等传统工具无法复制的差异化工作流，打通了设计到开发的全链路；3）对话式设计大幅降低非设计师（PM、创始人、市场人员）的创作门槛，潜在
    TAM 远超传统设计工具。但设计工具的护城河本质是生态（模板市场、插件体系、社区协作）和像素级精度控制，纯 AI 能力不足以自动赢得市场。当前仅为研究预览版，团队协作功能和第三方集成尚需验证。若生态建设成功，3-5
    年后大概率成为 AI-native 设计工具赛道的基础设施级产品。
value_capture_layer: end_application
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
competitive_casualty:
- Figma
- Canva
- Adobe XD
market_opportunities:
- 设计团队可利用 Claude Design 的代码库自动构建设计系统能力，大幅降低设计规范维护成本，实现设计与开发的一致性
- 产品经理和创始人可借助 Claude Design 将线框稿直接交付 Claude Code 实现，形成从设计到代码的闭环工作流，显著缩短原型到产品的周期
- 营销人员可基于 Claude Design 快速生成品牌一致的演示文稿和营销物料并导出 PPTX/Canva，适合中小团队以更低成本完成专业级视觉输出
risk_matrix:
  regulatory: 无
  technological: Claude Design 当前为研究预览版，功能稳定性和规模化能力尚未验证；若 Figma AI、Canva AI 或 Adobe
    Firefly 等竞品率先推出类似的设计系统自动构建能力，可能削弱其先发优势
  competitive: Figma、Canva、Adobe 等设计平台巨头均已布局 AI 辅助设计功能，且拥有更深的用户生态和插件网络；Anthropic 在
    B 端设计协作工具赛道缺乏原有用户基础，获客成本较高
  ethical: AI 生成的视觉作品可能无意中复制已有版权设计元素，带来品牌一致性和知识产权风险；若企业过度依赖 AI 设计，可能削弱初级设计师的成长通道和创意多样性
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: Claude Design
  canonical_name: Claude Design
  url: https://www.anthropic.com/news/claude-design-anthropic-labs
  positioning: Anthropic Labs 推出的首款产品，基于 Claude Opus 4.7 视觉模型，用户通过自然语言描述需求与 AI 协作完成设计稿、原型和幻灯片等视觉作品。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 设计师
  - 产品经理
  - 创业者
  - 市场营销人员
  product_signal: 支持导入团队设计系统、从代码库读取品牌规范，提供内联评论、直接编辑和自定义滑块等控制功能，可导出 PPTX 或发送到 Canva。
  market_signal: 以研究预览形式面向 Claude Pro、Max、Team 和 Enterprise 订阅用户逐步开放，是 Anthropic 从对话
    AI 向设计创作领域的关键产品扩展。
  differentiation: 与传统设计工具不同，用户通过自然语言描述需求即可生成初版，再通过对话、内联评论或滑块逐步迭代完善，无需掌握专业设计软件技能。
  watch_reason: 作为 Anthropic Labs 的首款产品，Claude Design 代表了 Anthropic 从对话 AI 向视觉创作工具的重要横向扩展，其用户采纳速度、对
    Figma 和 Canva 等设计工具市场的影响以及团队协作深度均值得持续跟踪。
  risk_notes:
  - 当前仅以研究预览形式发布，正式版功能、定价和可用性时间表尚未公布。
  - 在复杂设计场景和多团队协作中的实际表现尚需大规模用户验证。
  score: 8.0
  article_ids:
  - 0dba0c3d7be35ac4
  evidence_snippets:
  - Anthropic 推出了 Anthropic Labs 的首款产品 Claude Design，允许用户与 Claude 协作创建设计稿、原型、幻灯片等视觉作品。
  - Claude Design 由 Claude Opus 4.7 驱动，以研究预览形式面向 Claude Pro、Max、Team 和 Enterprise
    订阅用户开放。
  - Claude Design 支持导入团队设计系统，用户可通过内联评论、直接编辑和自定义滑块进行精细化调整。
- object_type: product
  name: Claude Code
  canonical_name: Claude Code
  url: null
  positioning: Anthropic 推出的 AI 编程助手，本文中作为 Claude Design 工作流的下游协作工具被提及，接收设计稿和流程草图进行代码实现。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 开发者
  - 产品经理
  product_signal: 与 Claude Design 打通设计到开发流程，产品经理可将功能流程草图直接传递至 Claude Code 进行代码实现，减少设计到开发的手动转换成本。
  market_signal: null
  differentiation: 定位为 Claude Design 视觉输出后直接进入代码实现的桥梁，无需传统的手工切图和代码编写衔接环节。
  watch_reason: Claude Code 被纳入 Claude Design 工作流表明 Anthropic 正在构建从设计到开发的端到端 AI 工具链，值得跟踪其与其他设计工具的生态整合进展以及对现有开发工作流的替代程度。
  risk_notes:
  - 本文中仅作为工作流参考被提及，缺乏关于 Claude Code 自身的功能更新信息。
  - 从设计到代码的自动转换在复杂业务逻辑场景下的准确性和可控性尚不明确。
  score: 5.0
  article_ids:
  - 0dba0c3d7be35ac4
  evidence_snippets:
  - 产品经理可以把功能流程草图交给 Claude Code 进行实现，或者与设计师协作进一步细化。
---

# Introducing Claude Design by Anthropic Labs

Today, we’re launching Claude Design, a new Anthropic Labs product that lets you collaborate with Claude to create polished visual work like designs, prototypes, slides, one-pagers, and more.

Claude Design is powered by our most capable vision model, Claude Opus 4.7, and is available in research preview for Claude Pro, Max, Team, and Enterprise subscribers. We’re rolling out to users gradually throughout the day.

## Design with Claude

Even experienced designers have to ration exploration—there's rarely time to prototype a dozen directions, so you limit yourself to a few. And for founders, product managers, and marketers with an idea but not a design background, creating and sharing those ideas can be daunting.

Claude Design gives designers room to explore widely and everyone else a way to produce visual work. Describe what you need and Claude builds a first version. From there, you refine through conversation, inline comments, direct edits, or custom sliders (made by Claude) until it’s right. When given access, Claude can also apply your team’s design system to every project automatically, so the output is consistent with the rest of your company’s designs.

Teams have been using Claude Design for:

**Realistic prototypes:**Designers can turn static mockups into easily-shareable interactive prototypes to gather feedback and user-test, without code review or PRs.**Product wireframes and mockups:**Product Managers can sketch out feature flows and hand them off to Claude Code for implementation, or share them with designers to refine further.**Design explorations:**Designers can quickly create a wide range of directions to explore.**Pitch decks and presentations:**Founders and Account Executives can go from a rough outline to a complete, on-brand deck in minutes, and then export as a PPTX or send to Canva.**Marketing collateral:**Marketers can create landing pages, social media assets, and campaign visuals, then loop in designers to polish.**Frontier design**: Anyone can build code-powered prototypes with voice, video, shaders, 3D and built-in AI.

## How it works

Claude Design follows a natural creative flow.

**Your brand, built in.** During onboarding, Claude builds a design system for your team by reading your codebase and design files. Every project after that uses your colors, typography, and components automatically. You can refine the system over time, and teams can maintain more than one.

**Import from anywhere.** Start from a text prompt, upload images and documents (DOCX, PPTX, XLSX), or point Claude at your codebase. You can also use the web capture tool to grab elements directly from your website so prototypes look like the real product.

**Refine with fine-grained controls.** Comment inline on specific elements, edit text directly, or use adjustment knobs to tweak spacing, color, and layout live. Then ask Claude to apply your changes across the full design.