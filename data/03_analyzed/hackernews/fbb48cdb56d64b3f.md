---
title: Delphi 13 Community Edition Is Now Available
source: https://blogs.embarcadero.com/delphi-13-community-edition-is-now-available/
author:
- '[[layer8]]'
published: '2026-08-12'
created: '2026-08-12'
manifest_dates:
- '2026-08-12'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: fbb48cdb56d64b3f
source_type: community_discussion
tldr: Embarcadero 正式发布免费的 Delphi 13 Community Edition，该版本基于 Delphi 13 Florence，面向学生、爱好者和符合条件的初创团队，并新增了
  64 位 IDE、语言特性、FireMonkey 与 VCL 改进以及 Android 15 / iOS 18 移动平台支持。
objective_summary: Embarcadero 宣布推出 Delphi 13 Community Edition，这是 Delphi 13 Florence
  的免费社区版本，替代此前的 Delphi 12.1 Community Edition。该版本在语言、IDE、框架和平台层面均有改进，包括新增 64 位 IDE、64
  位 Delphi 语言服务器、FireMonkey 增强、VCL 改进，以及对 Android API 35 和 iOS 18 的支持。社区版面向学生、爱好者、年收入低于
  5000 美元的个人开发者，以及年收入低于 5000 美元且团队不超过 5 人的初创组织，提供一年期有限商业使用许可。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Embarcadero
  technologies:
  - Delphi
  - Delphi 13
  - Delphi 13 Florence
  - Delphi 12.1
  - FireMonkey
  - VCL
  - Skia4Delphi
  - WebView2
  - Android SDK
  - Android NDK
  - Java2OP
  - WinRT
  - GetIt
  - Classic Delphi CodeInsight
  key_people: []
key_logic_flow:
- Embarcadero 发布 Delphi 13 Community Edition，作为基于 Delphi 13 Florence 的免费开发环境版本。
- 该版本面向学生、爱好者、独立开发者及符合条件的小型团队，提供一年期有限商业许可。
- 语言层面新增三元条件表达式、NameOf 内置函数、is not / not in 运算符、{$PUSHOPT}/{$POPOPT} 编译指令、noreturn
  指令及泛型约束改进。
- IDE 首次在社区版中同时提供 32 位与 64 位版本，并配备 64 位语言服务器、Focus Mode、分屏编辑与 GetIt 包版本选择。
- FireMonkey 框架获得 Display Link 服务、GPU 位图加速、新组件及触控滚动增强；VCL 框架改进了标题栏样式、控件与 WebView2
  集成。
- 移动平台支持更新至 Android API 35（含 Android 15 的 16 KB 页面）与 iOS 18（含 Apple Silicon 模拟器）。
object_mentions:
- object_type: product
  name: Delphi 13 Community Edition
  canonical_name: Delphi 13 Community Edition
  url: https://blogs.embarcadero.com/delphi-13-community-edition-is-now-available/
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Embarcadero 正式宣布推出 Delphi 13 Community Edition，这是 Delphi 专业开发环境的最新免费版本。
  - Delphi 13 Community Edition 基于 Delphi 13 Florence，将社区版从 12.1 升级至 13.0。
  - 该版本为学生、爱好者、独立开发者和符合条件的初创团队提供 Delphi 语言和框架改进的访问权限。
  article_id: fbb48cdb56d64b3f
- object_type: product
  name: Delphi 13 Florence
  canonical_name: Delphi 13 Florence
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Delphi 13 Community Edition 基于 Delphi 13 Florence，是社区版的底层专业版本。
  - 从 Delphi 12.1 Community Edition 升级到 Delphi 13 Community Edition 可获得 12.2、12.3
    和 13.0 的语言与框架改进。
  article_id: fbb48cdb56d64b3f
- object_type: product
  name: RAD Studio
  canonical_name: RAD Studio
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章末尾提到可通过 RAD Studio、Delphi 或 C++Builder 缩短开发时间并更快上市。
  - RAD Studio 与 Delphi、C++Builder 并列为 Embarcadero 的商用开发工具产品线。
  article_id: fbb48cdb56d64b3f
- object_type: product
  name: C++Builder Community Edition
  canonical_name: C++Builder Community Edition
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章末尾提供两个下载入口：Free Delphi Community Edition 与 Free C++Builder Community Edition。
  - C++Builder Community Edition 被定位为与 Delphi Community Edition 并列的免费社区版本。
  article_id: fbb48cdb56d64b3f
- object_type: project
  name: FireMonkey
  canonical_name: FireMonkey
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - FireMonkey 是 Delphi 多设备开发的基础框架，支持从同一套代码库构建 Windows、macOS、iOS 和 Android 原生应用。
  - Delphi 13 中的 FireMonkey 新增了 Display Link 服务、GPU 加速位图复制、TMaskEdit 和 TApplicationEvents
    组件。
  article_id: fbb48cdb56d64b3f
- object_type: project
  name: VCL
  canonical_name: VCL
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - VCL 是 Delphi 用于 Windows 原生开发的框架，社区版同样包含该框架。
  - Delphi 13 改进了 VCL 的样式化标题栏、TControlList、TFormTabsBar、TToggleSwitch 和 TEdgeBrowser
    中的 WebView2 集成。
  article_id: fbb48cdb56d64b3f
- object_type: project
  name: Skia4Delphi
  canonical_name: Skia4Delphi
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - FireMonkey 改进列表中包括更新后的 Skia4Delphi 集成。
  - Skia4Delphi 为 Delphi 应用提供 Skia 图形库的渲染能力支持。
  article_id: fbb48cdb56d64b3f
extract_result: success
impact_score:
  score: 3.5
  reason: Delphi 13 Community Edition 是 Embarcadero 旗下成熟 RAD 开发工具的免费版本更新，对 Delphi/Pascal
    生态及跨平台原生应用开发者是实质性进展。但事件发生在 AI 行业语境下，其技术栈（Object Pascal、VCL/FireMonkey）与当前大模型、AI
    基础设施、Agent 等主流赛道关联度极低，不具备改变 AI 竞争格局或引发范式转移的潜力。因此综合评估为日常产品更新级别，对 AI 行业短期冲击力有限。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: Delphi 生态的免费可用性与移动端（Android 15 / iOS 18）支持能否吸引新开发者
hype_assessment:
  level: low
  reason: 文章以功能清单和许可说明为主，未使用 '颠覆'、'革命性'、'改变游戏规则' 等夸张 PR 词汇；对新增语言特性、IDE 改进、框架更新的描述具体且可验证，整体水分较低。
information_entropy: medium
domain_disruption:
  technical_innovation: 对 AI 行业几乎无直接技术冲击；本质是成熟 RAD 工具的语言、IDE、框架与移动平台迭代，新增 64 位 IDE、条件表达式、NameOf
    内置函数、FireMonkey/VCL 改进及 Android API 35 / iOS 18 支持。
  business_model: 采用 'Community Edition 免费 + 商业版付费' 的 freemium 模式，通过年收入与团队规模限制（低于
    5000 美元、不超过 5 人）扩大初学者、爱好者和小型初创团队的用户基数，再向 Professional/Enterprise/Architect 版本转化。
engineering_complexity: production_ready
compound_value:
  score: 3.0
  reason: Delphi 13 Community Edition 是 Embarcadero 在成熟/衰退期的典型获客与防守动作：通过免费层扩大漏斗、降低现有用户流失，并锁定学生、爱好者与收入/团队规模受限的小微初创进入其专有生态。然而该事件本身并不改变
    AI 或现代软件开发的基础格局，Delphi 的市场份额与增长动能长期下滑，严格的年收入低于 5000 美元及 ≤5 人团队限制也大幅压缩了商业化转化空间。其价值更偏向一次性用户获取与生态维护，而非可积累、可扩展的行业基础设施，长期复利效应有限。
value_capture_layer: end_application
moat_impact: strengthens_monopoly
key_beneficiaries:
- Embarcadero
competitive_casualty:
- Microsoft .NET MAUI
- Flutter
- React Native
- Qt
market_opportunities:
- 中小团队可借助免费的 Delphi 13 Community Edition 以单一 Pascal/Delphi 代码库快速覆盖 Windows、macOS、iOS、Android
  原生应用，降低跨平台开发初始成本
- 教育培训与外包服务商可围绕 Delphi 13 的新语言特性、64 位 IDE 和 FireMonkey/VCL 改进开发入门课程与模板项目，填补 Pascal
  生态技能供给缺口
- 年收入接近许可门槛的初创企业应评估将 Delphi 作为早期 MVP 技术栈的可行性，并提前规划商业化后的授权升级路径
risk_matrix:
  regulatory: 无显著监管风险，但需遵守 Community Edition 的一年期有限商业许可条款，避免超范围商业使用引发授权合规问题
  technological: Delphi 生态相对小众，人才储备和第三方库规模远逊于主流跨平台框架，存在技能招聘难、社区资源少、长期维护成本上升的风险
  competitive: Flutter、React Native、.NET MAUI 等现代跨平台方案已形成庞大生态，Delphi 在开发者心智、人才市场与开源组件上处于劣势
  ethical: 无
  additional:
  - 厂商锁定风险：深度绑定 Embarcadero 的 IDE、编译器与授权模式，迁移至其他技术栈成本较高
  - 许可边界模糊风险：年营收 5,000 美元、团队 5 人以下的资格认定可能随业务增长快速失效，需提前规划付费版预算
  - 长期可持续性风险：Delphi 属于传统开发工具，未来版本迭代与社区活跃度存在不确定性
confidence:
  impact: medium
  compound: low
  hype: low
actionable_insight: monitor
object_insights:
- object_type: product
  name: Delphi 13 Community Edition
  canonical_name: Delphi 13 Community Edition
  url: https://blogs.embarcadero.com/delphi-13-community-edition-is-now-available/
  positioning: Embarcadero 推出的 Delphi 13 Florence 免费社区版本，面向学生、爱好者和符合条件的初创团队提供原生应用开发能力。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 学生
  - 爱好者
  - 年收入低于5000美元的个人开发者
  - 年收入低于5000美元且团队不超过5人的初创组织
  product_signal: 基于 Delphi 13 Florence，首次在社区版中同时提供 32 位与 64 位 IDE，并新增语言特性、FireMonkey
    与 VCL 改进及 Android 15/iOS 18 支持。
  market_signal: 作为免费社区版本替代 Delphi 12.1 Community Edition，提供一年期有限商业许可，是 Embarcadero
    扩大开发者生态和用户转化的重要举措。
  differentiation: 在免费社区版本中提供专业 IDE、可视化设计器、集成编译器调试器、VCL 和 FireMonkey 跨平台框架，覆盖 Windows、macOS、iOS
    和 Android 原生开发。
  watch_reason: 该产品是 Embarcadero 扩大 Delphi 开发者生态的关键免费入口，其 64 位 IDE、移动平台更新和许可条件变化可能显著影响学生、独立开发者和小型团队的工具选择，值得跟踪其采用率与后续版本策略。
  risk_notes:
  - 社区版存在年收入和团队规模限制，商业扩展后需迁移至付费版本。
  - 在跨平台开发工具市场中面临 Flutter、React Native 等现代框架的竞争压力。
  score: 7.0
  article_ids:
  - fbb48cdb56d64b3f
  evidence_snippets:
  - Embarcadero 正式宣布推出 Delphi 13 Community Edition，这是 Delphi 专业开发环境的最新免费版本。
  - Delphi 13 Community Edition 基于 Delphi 13 Florence，将社区版从 12.1 升级至 13.0。
  - 该版本为学生、爱好者、独立开发者和符合条件的初创团队提供 Delphi 语言和框架改进的访问权限。
- object_type: product
  name: Delphi 13 Florence
  canonical_name: Delphi 13 Florence
  url: null
  positioning: Delphi 13 Florence 是 Embarcadero 的专业版 Delphi 开发环境，作为 Delphi 13 Community
    Edition 的底层商业版本。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 专业开发者
  - 企业开发团队
  product_signal: 社区版用户可通过升级获得 12.2、12.3 和 13.0 的语言与框架改进，包括 64 位 IDE、FireMonkey 增强、VCL
    改进及移动平台支持。
  market_signal: 作为 Delphi 13 Community Edition 的商业基础版本，其功能迭代直接影响社区版的能力边界和市场定位。
  differentiation: 与社区版相比，提供专业、企业和架构师等无限制商业许可及额外能力，面向更大规模和商业化项目。
  watch_reason: Delphi 13 Florence 是社区版的底层专业版本，其语言、IDE 和框架改进会同步赋能社区版用户，跟踪其版本节奏有助于判断
    Embarcadero 对原生跨平台开发工具市场的投入力度。
  risk_notes:
  - 文章未直接介绍 Florence 专业版的定价和完整功能差异，信息主要来自社区版上下文。
  - 传统原生开发工具市场面临云原生和 Web 跨平台方案的竞争。
  score: 5.0
  article_ids:
  - fbb48cdb56d64b3f
  evidence_snippets:
  - Delphi 13 Community Edition 基于 Delphi 13 Florence，是社区版的底层专业版本。
  - 从 Delphi 12.1 Community Edition 升级到 Delphi 13 Community Edition 可获得 12.2、12.3
    和 13.0 的语言与框架改进。
- object_type: product
  name: RAD Studio
  canonical_name: RAD Studio
  url: null
  positioning: RAD Studio 是 Embarcadero 的商用快速应用开发工具套件，与 Delphi 和 C++Builder 并列。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 企业开发团队
  - 商业应用开发者
  product_signal: 文章仅提及 RAD Studio 可缩短开发时间并更快上市，未提供具体功能或版本更新信息。
  market_signal: 作为 Embarcadero 商用产品线的一部分，与 Delphi 和 C++Builder 共同构成其开发工具市场布局。
  differentiation: 与免费社区版形成互补，面向需要完整商业许可和企业级支持的用户。
  watch_reason: 文章对 RAD Studio 仅作末尾附带提及，缺乏具体产品动态，跟踪价值较低，仅作为 Embarcadero 产品组合上下文参考。
  risk_notes:
  - 文章未提供 RAD Studio 的具体更新或功能细节，信息非常有限。
  - 无法判断其与社区版或竞争产品的当前差异化优势。
  score: 3.0
  article_ids:
  - fbb48cdb56d64b3f
  evidence_snippets:
  - 文章末尾提到可通过 RAD Studio、Delphi 或 C++Builder 缩短开发时间并更快上市。
  - RAD Studio 与 Delphi、C++Builder 并列为 Embarcadero 的商用开发工具产品线。
- object_type: product
  name: C++Builder Community Edition
  canonical_name: C++Builder Community Edition
  url: null
  positioning: C++Builder Community Edition 是 Embarcadero 提供的免费 C++ 原生应用开发社区版本，与 Delphi
    Community Edition 并列。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - C++ 学习者
  - C++ 爱好者
  - 小型 C++ 开发团队
  product_signal: 文章仅在下载入口处提及，未提供该版本的具体功能、版本号或更新内容。
  market_signal: 与 Delphi Community Edition 共同构成 Embarcadero 的免费开发者入口策略。
  differentiation: 面向偏好 C++ 语言的开发者，与 Delphi Community Edition 在语言生态上形成区分。
  watch_reason: 文章对 C++Builder Community Edition 仅作并列提及，缺乏具体动态，跟踪价值有限，仅作为 Embarcadero
    免费产品线布局的参考。
  risk_notes:
  - 文章未提供 C++Builder Community Edition 的版本或功能更新细节。
  - C++ 跨平台开发市场存在 Qt、.NET MAUI 等竞争方案。
  score: 3.0
  article_ids:
  - fbb48cdb56d64b3f
  evidence_snippets:
  - 文章末尾提供两个下载入口：Free Delphi Community Edition 与 Free C++Builder Community Edition。
  - C++Builder Community Edition 被定位为与 Delphi Community Edition 并列的免费社区版本。
---

Embarcadero is pleased to announce the availability of Delphi 13 Community Edition, the latest free edition of our professional Delphi development environment.

Delphi 13 Community Edition is based on Delphi 13 Florence and brings the Community Edition forward from version 12.1. This gives students, hobbyists, independent developers, and eligible startups access to the Delphi language and framework improvements delivered in versions 12.2, 12.3, and 13.0—including updated support for today’s mobile platforms.

Table of Contents

**What Is Delphi Community Edition?**

Delphi Community Edition is a full-featured, free edition of Delphi for building native applications with the Delphi language. It includes a professional IDE, visual designers, integrated compilers and debuggers, the VCL framework for Windows development, and the FireMonkey framework for creating native applications from a shared codebase across Windows, macOS, iOS, and Android.

It is designed for students, hobbyists, freelancers, and small teams that meet the Community Edition license requirements.

**What’s New Since Delphi 12.1?**

Moving from Delphi 12.1 Community Edition to Delphi 13 Community Edition delivers a substantial collection of language, IDE, framework, and platform improvements.

**New Delphi Language Features**

Delphi 13 introduces several useful additions to the Delphi language, available across the supported target platforms:

- A new conditional expression, or ternary operator, implemented with the if keyword
- The new NameOf intrinsic, which returns the name of an identifier as a string
- New is not and not in operators for clearer and more natural expressions
- New {$PUSHOPT} and {$POPOPT} compiler directives for saving and restoring compiler options
- A new noreturn directive for procedures that do not return control to their caller
- Improvements to generic type constraints
- An implicit Self parameter in the Initialize and Finalize operators of custom managed records

These additions make Delphi code more expressive while retaining the language’s readability and strong native-code foundations.

**A More Capable Development Environment**

Delphi 13 Community Edition includes the updated 32-bit IDE and the **new 64-bit IDE** for developing and debugging 64-bit Windows applications. The 64-bit IDE provides a much larger address space, which is particularly valuable when working with large projects.

The IDE also includes:

- A 64-bit Delphi language server for improved support for large projects
- Search and filtering in key IDE panes, including the Project Manager, Structure view, Messages, and Event Log
- Focus Mode for a distraction-free code editing experience
- Editor scrollbar annotations for changes, bookmarks, errors, and warnings
- Split editor views
- The option to use the reintroduced Classic Delphi CodeInsight engine
- GetIt package versioning, allowing developers to select a specific available version of a package
- Numerous improvements to Delphi code tooling, debugging, IDE responsiveness, stability, and quality

**FireMonkey Improvements**

FireMonkey remains the foundation for Delphi multi-device development. Since Delphi 12.1, it has gained a broad set of enhancements, including:

- A new Display Link service for smoother and more stable animations
- Faster bitmap copying through GPU acceleration
- A new TMaskEdit component
- A new TApplicationEvents component
- New alignment options for centering controls
- Additional scrolling, bounce, and touch interaction controls
- Extended spell-checking support
- Updated Skia4Delphi integration
- General performance, platform integration, and quality improvements

**VCL Improvements for Windows**

Delphi 13 also advances the VCL framework for native Windows development with:

- Styled custom title bars
- Improvements to TControlList, TFormTabsBar, and TToggleSwitch
- Scrolling support for TActionMainMenuBar
- Updated WebView2 integration in TEdgeBrowser
- Expanded and refreshed Windows and WinRT API support

**Updated Mobile Platform Support**

One of the most important benefits of Delphi 13 Community Edition is updated mobile development support.

For Android, Delphi 13 supports building native 32-bit and 64-bit ARM applications with an updated Android toolchain. It targets Android API level 35 and includes support for Android 15 features such as 16 KB memory page sizes. It also improves Android SDK and NDK integration, deployment tooling, Java library import, and the Java2OP bridge.

For Apple platforms, Delphi 13 supports native iOS applications for iOS 18, including development for both physical devices and the iOS Simulator on Apple Silicon Macs. The release also includes expanded iOS API headers and updated platform integration.

Delphi developers can therefore continue to use a shared FireMonkey codebase while targeting current Android and iOS devices with native applications.

**Who Can Use Delphi Community Edition?**

Delphi Community Edition is intended for:

- Students learning programming and native application development
- Hobbyists building applications for personal use
- Freelance developers and individual developers earning less than US$5,000 per year from their applications
- Startups and organizations with annual revenue below US$5,000 and teams of up to five developers

Delphi Community Edition is free of charge, comes with a one-year term license, and includes a limited commercial-use license. If you are unsure whether you qualify, review the Community Edition License FAQ. Community Edition is not intended as an extended trial and should not be used by an organization that already has regular commercial Delphi licenses.

Once your development or business needs move beyond the Community Edition limits, Delphi Professional, Enterprise, and Architect offer unrestricted commercial licenses and additional capabilities.

**Download Delphi 13 Community Edition**

Whether you are discovering Delphi for the first time, learning native application development, or updating from Delphi 12.1 Community Edition, Delphi 13 Community Edition gives you a modern, productive environment for building fast native applications for Windows and mobile platforms.

Download Delphi 13 Community Edition today and start building: **Download Now**

Reduce development time and get to market faster with RAD Studio, Delphi, or C++Builder.

Design. Code. Compile. Deploy.

Free Delphi Community Edition Free C++Builder Community Edition