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