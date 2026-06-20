---
title: itsfatduck/optimizerDuck
source: https://github.com/itsfatduck/optimizerDuck
author: []
published: ''
created: '2026-06-16'
description: 'Free, open-source Windows optimization tool for performance, privacy,
  and simplicity. optimizerDuck optimizerDuck is a free, open-source Windows optimization
  tool focused on performance, privacy, and simplicity. Getting Started | How It Works
  | FAQ English | Tiếng Việt | 繁體中文 | 简体中文 | Русский | Français | 한국어 | Español |
  日本語 | Polski | Português (BR) ⭐ Star History If optimizerDuck helped improve your
  PC, consider giving the repo a ⭐ and sharing it with others. Every star helps motivate
  future improvements. Quick Start Download from GitHub Releases Run the .exe directly,
  no installation required Choose the optimizations you want, apply them, and restart
  your PC when you''re ready Tip Always create a system restore point before making
  changes. Note Language Native Name Translator 🇺🇸 English (United States) English
  Primary & recommended 🇻🇳 Vietnamese Tiếng Việt itsfatduck 🇹🇼 Traditional Chinese
  正體中文 abc0922001 🇨🇳 Simplified Chinese 简体中文 wcxu21 🇷🇺 Russian Русский Foodhead 🇫🇷
  French Français Robocnop 🇰🇷 Korean 한국어 klfnn 🇪🇸 Spanish Español thexxtt 🇯🇵 Japanese
  日本語 zerofrip 🇵🇱 Polish Polski dudus2000 🇧🇷 Portuguese (Brazil) Português (Brasil)
  mhanelia Want to add your language? See CONTRIBUTING.md (Japanese). What optimizerDuck
  Does Windows itself is fine. But a clean install also comes with services, telemetry,
  pre-installed apps, and scheduled tasks you''ve probably never heard of, all quietly
  running in the background, consuming your CPU, RAM, and disk. At the same time,
  some features that could actually help you get the most out of your hardware aren''t
  enabled by default. optimizerDuck gives you a single interface to clean up the bloat
  and unlock the good stuff. It applies targeted system tweaks to reduce overhead
  and block unwanted behavior, and bundles several management tools so you can see
  what is running, remove what you do not want, and revert any change if something
  goes wrong. Note Every optimization can be applied manually. optimizerDuck just
  makes it easier for you to apply these optimizations. System Optimizations Over
  30 tweaks across 6 categories, each with a clear description and risk rating so
  you know exactly what each change does before applying it. Category What it covers
  Performance Service host tuning based on your RAM, process priority adjustments,
  keyboard latency reduction, and multimedia scheduler tweaks for smoother gaming
  Privacy Disable Windows telemetry, error reporting, advertising ID, location tracking,
  Cortana, Copilot, and content delivery suggestions GPU Vendor-specific registry
  tweaks for AMD, NVIDIA, and Intel GPUs, covering power states, clock gating, and
  display latency Power Disable hibernation and fast startup, turn off USB selective
  suspend, install a custom high-performance power plan, and disable power throttling
  Bloatware & Services Block OEM app reinstall behavior and fine-tune startup types
  for 200+ Windows services User Experience Remove menu show delays, disable visual
  effects like taskbar animations and transparency for a snappier feel Note The optimizations
  here are researched from well-known tools with large user bases, nothing is AI-generated
  or blindly added. Every tweak is chosen for real-world impact. Customize No need
  to dig through the registry, just toggles, dropdowns, and number inputs presented
  in one place. Organized into four categories: Desktop: Show or hide icons (This
  PC, Recycle Bin, Network, User Files, Control Panel), remove shortcut arrow overlays
  Preferences: Taskbar alignment, widgets, Task View and End Task buttons, clock seconds,
  dark mode, file extensions, hidden files, clipboard history, compact view, snap
  assist, item checkboxes, classic context menu, and Bing search Gaming: Game Mode,
  Game Bar, background recording, mouse acceleration, fullscreen optimizations, hardware-accelerated
  GPU scheduling System: Enable Num Lock on boot Built-in Tools Tool What it does
  System Dashboard View your CPU, RAM, GPU, storage drives, and OS details in one
  panel Startup Manager See every app and task that launches at boot, toggle them
  on or off, and open their file location Scheduled Tasks Browse, run, stop, enable,
  disable, or delete Windows scheduled tasks Disk Cleanup Scan and clear temp files,
  system cache, Windows Update leftovers, prefetch, thumbnails, recycle bin, crash
  dumps, and old Windows installations Bloatware Remover Lists all removable AppX
  packages with risk badges (Safe, Caution, Unknown), so you can pick what to remove
  Safety Changing system settings carries risk. optimizerDuck is built around reversibility
  and user control. See the Privacy Policy for details on our data practices. Automatic
  backups: Every change writes a revert file to a local folder. You can restore individual
  tweaks or roll back everything One-click revert: Undo any applied optimization from
  the UI with a single click Risk ratings: Each tweak is labeled Safe, Moderate, or
  Risky based on its potential impact No defaults applied: Nothing runs until you
  select it. The tool does not enable anything on its own Restore point prompt: Before
  your first optimization, the app suggests creating a Windows restore point FAQ Is
  optimizerDuck safe to use? Yes. optimizerDuck is fully open-source (GPL v3), meaning
  anyone can inspect, audit, or build the source code themselves. Every release is
  built automatically by GitHub Actions from the public source; no hidden modifications,
  no unsigned binaries injected after build. If you prefer, you can clone the repo
  and build the .exe yourself with a single dotnet build. The app does not collect
  any telemetry, usage data, or personal information. See the Privacy Policy. Does
  optimizerDuck actually improve performance, reduce latency, or speed up my network?
  It can help. Every optimization in optimizerDuck is researched from well-known tools,
  community guides, and hardware vendor recommendations, nothing is AI-generated,
  blindly added, or made up. Each tweak addresses a real setting that Windows configures
  conservatively by default (e.g., service host grouping, GPU power states, network
  throttling, process scheduling). There are no fake registry hacks here, every change
  has a documented purpose and real-world impact backed by community testing and vendor
  documentation. Why does Windows SmartScreen / Defender flag the download? optimizerDuck
  is not code-signed because code signing certificates are expensive for open-source
  projects. When Windows encounters an unsigned executable downloaded from the internet,
  SmartScreen displays a warning by default. This is normal and does not mean the
  file is unsafe. To bypass, click "More info" > "Run anyway". If you are still concerned:
  Build the .exe yourself from source Submit the binary to online sandboxes like ANY.RUN
  for independent verification Can I revert changes if something goes wrong? Yes.
  Every optimization creates a revert file before applying. You can undo individual
  tweaks or roll back everything from the UI with one click. The app also suggests
  creating a Windows System Restore point before your first optimization. Does this
  work on Windows 10 and Windows 11? Yes. optimizerDuck supports Windows 10 (x64)
  and Windows 11 (x64). Do I need administrator rights? Yes. optimizerDuck modifies
  system settings and the Windows registry, so it requires administrator privileges
  to run. Does optimizerDuck collect my data? No. The app contains zero telemetry,
  analytics, or phone-home functionality. It runs entirely offline and does not send
  any data anywhere. Why does Task Manager show 100% CPU after applying the power
  plan? (#29) A known Task Manager display bug triggered by non-default power plans,
  it incorrectly reports 100% CPU on some systems while actual load is normal. Visual
  only, does not affect real performance or cause overheating. If unwanted, simply
  toggle off this optimization. Technical Details Framework: WPF on .NET 10, using
  the WPF UI library for Fluent design Revert system: Four revert step types (Registry,
  Service, Scheduled Task, Shell) with JSON-persisted state and thread-safe file I/O
  Theming: Dark (default), Light, and High Contrast modes with Mica backdrop support
  No installer: Runs as a single .exe, no installation required Backup system: Local
  folder-based backup for every change, with one-click restore Discovery: Optimization
  and Feature categories are discovered automatically via reflection + custom attributes,
  no manual registration needed No telemetry: The app does not collect any user data
  Documentation Official Documentation Guides, optimization details, and usage tips.
  Contribute Bug reports, new optimizations, docs improvements, and translations are
  all welcome. See CONTRIBUTING.md (Japanese). Community Tip Join our Discord server
  for support, tips, and discussions with other users and contributors. If optimizerDuck
  helped your PC: ⭐ Star the repo 💬 Join Discord for support 🐞 Report bugs on GitHub
  🎁 Support the project here Links 🌐 Website 📖 Documentation 💬 Discord 🐞 Issues Bug
  reports, feature suggestions, translations, and sharing your experience all help
  the project. Disclaimer optimizerDuck is provided "as is", without warranty of any
  kind. By using this tool, you agree that the authors are not liable for system instability,
  data loss, or issues caused by third-party software or user modifications. Always
  create a restore point before applying changes. Note optimizerDuck modifies system
  settings and the Windows registry. Use at your own risk. We recommend backing up
  important data and creating a restore point before making changes. See Terms of
  Service, Privacy Policy, and Disclaimer for more information. License GPL v3 LicenseSee
  LICENSE. Thanks to all Contributors'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: adcf8c426e4c5ca5
source_type: community_discussion
tldr: optimizerDuck 发布免费开源 Windows 优化工具，提供30+项系统性能与隐私优化
objective_summary: itsfatduck 在 GitHub 上发布了 optimizerDuck，一款基于 .NET 10 的 WPF 开源 Windows
  优化工具。该工具提供6大类30余项系统优化，支持 Windows 10/11 x64，无需安装即可运行，并内置备份还原机制。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies: []
  technologies: []
  key_people:
  - itsfatduck
key_logic_flow:
- optimizerDuck 是一款免费开源的 Windows 优化工具，基于 GPL v3 协议发布，代码通过 GitHub Actions 自动构建。
- 工具提供超过30项优化项目，涵盖性能、隐私、GPU、电源、臃肿软件与服务、用户体验共6个类别，每项优化附有风险评级。
- 所有优化均源自社区验证和硬件厂商文档，非 AI 生成或盲目添加，且未预设任何默认启用项。
- 工具内置系统仪表盘、启动管理器、计划任务管理、磁盘清理和 AppX 臃肿软件移除等管理工具。
- 每项修改自动生成 JSON 格式备份文件，支持单次或一键全部还原，首次运行提示创建系统还原点。
- 软件基于 .NET 10 的 WPF 框架开发，支持 Windows 10/11 x64，单文件运行无需安装，不收集任何遥测数据。
impact_score:
  score: 1.5
  reason: 该事件为通用 Windows 系统优化工具发布，与 AI 行业无直接关联。工具明确声明优化项来自社区验证和厂商文档而非 AI 生成，未涉及任何
    AI/ML 技术栈。对 AI 行业短期竞争格局和范式无任何可察觉影响，属于社区实用工具分享范畴。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 开源 Windows 优化工具的实用性和代码可审查性
hype_assessment:
  level: low
  reason: 项目 README 描述客观务实，未出现颠覆性、革命性等 PR 滥用词汇。每项优化均标注风险等级，明确声明非 AI 生成、无默认启用项、不收集遥测数据，功能说明与风险提示充分透明。
information_entropy: medium
domain_disruption:
  technical_innovation: 无。该项目是基于 .NET 10 WPF 框架开发的系统优化工具集合，技术实现为常规注册表修改和服务管理，未包含 AI
    领域技术突破。
  business_model: 无。项目采用 GPL v3 开源协议免费分发，不收集遥测数据，不涉及 SaaS 或商业化模式，对商业模式无重塑影响。
engineering_complexity: production_ready
compound_value:
  score: 2.5
  reason: optimizerDuck 是个人开发者维护的免费开源工具，无商业模式、无网络效应、无数据积累机制。价值完全绑定于开发者个人维护意愿，缺乏可持续的资本注入路径。虽然工具本身实用性不错（30+项优化、备份还原机制），但
    Windows 优化工具赛道极其拥挤且免费替代品众多（如 Chris Titus Tech Utility、O&O ShutUp10++ 等），用户迁移成本为零。不具备任何长期复利积累的能力，3-5年内大概率被同类工具淹没或被
    Windows 原生功能迭代覆盖。
value_capture_layer: end_application
moat_impact: democratizes_access
key_beneficiaries:
- Windows 开源工具生态
competitive_casualty:
- CCleaner (Gen Digital)
- IObit Advanced SystemCare
- 商业 Windows 优化/清理软件
market_opportunities:
- 企业IT服务商可借鉴其风险评级+自动备份设计范式，开发面向合规审计场景的系统优化管理平台
- 开源社区可基于该项目构建Windows隐私合规检测工具，帮助企业和个人用户评估并满足GDPR等隐私法规要求
- 其"社区验证+硬件厂商文档"的优化项筛选模式可复制到Linux/macOS系统优化工具的协作开发中
risk_matrix:
  regulatory: 工具提供禁用Windows遥测、Cortana、Copilot等功能，在欧盟等地区可辅助GDPR合规，但在企业IT环境中未经审批的优化操作可能违反内部合规政策；微软可能通过Windows更新对抗非官方系统修改
  technological: .NET 10强依赖限制了工具在旧版Windows上的可用性；Windows功能更新可能改变注册表键值路径或服务名称，导致部分优化项失效或产生副作用；部分优化可能随Windows版本迭代变得多余
  competitive: Windows优化工具市场已十分拥挤，包括Chris Titus Windows Utility（开源）、O&O ShutUp10、WPD等同类产品，功能差异化空间有限；微软自身也在持续改善Windows开箱体验，减少臃肿软件和过度遥测
  ethical: 无明显伦理风险。工具完全开源（GPL v3）、不收集遥测数据、用户自主选择优化项、内置自动备份和一键还原机制，设计上充分尊重用户知情权和选择权
  additional:
  - 项目主要由个人开发者 itsfatduck 维护，长期可持续性存疑，存在"bus factor"风险
  - 多语言翻译依赖社区志愿者贡献，存在翻译覆盖不全或版本更新后翻译滞后的风险
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: monitor
---

**optimizerDuck is a free, open-source Windows optimization tool focused on performance, privacy, and simplicity.**

**Getting Started | How It Works | FAQ**

**English** | Tiếng Việt | 繁體中文 | 简体中文 | Русский | Français | 한국어 | Español | 日本語 | Polski | Português (BR)

## ⭐ Star History

If optimizerDuck helped improve your PC, consider giving the repo a ⭐ and sharing it with others. Every star helps motivate future improvements.

- Download from
**GitHub Releases** - Run the
`.exe`

directly, no installation required - Choose the optimizations you want, apply them, and restart your PC when you're ready

Tip

Always create a **system restore point** before making changes.

Note

| Language | Native Name | Translator | |
|---|---|---|---|
| 🇺🇸 | English (United States) | English | Primary & recommended |
| 🇻🇳 | Vietnamese | Tiếng Việt | itsfatduck |
| 🇹🇼 | Traditional Chinese | 正體中文 | abc0922001 |
| 🇨🇳 | Simplified Chinese | 简体中文 | wcxu21 |
| 🇷🇺 | Russian | Русский | Foodhead |
| 🇫🇷 | French | Français | Robocnop |
| 🇰🇷 | Korean | 한국어 | klfnn |
| 🇪🇸 | Spanish | Español | thexxtt |
| 🇯🇵 | Japanese | 日本語 | zerofrip |
| 🇵🇱 | Polish | Polski | dudus2000 |
| 🇧🇷 | Portuguese (Brazil) | Português (Brasil) | mhanelia |

Want to add your language? See CONTRIBUTING.md (Japanese).


Windows itself is fine. But a clean install also comes with services, telemetry, pre-installed apps, and scheduled tasks you've probably never heard of, all quietly running in the background, consuming your CPU, RAM, and disk. At the same time, some features that could actually help you get the most out of your hardware aren't enabled by default.

optimizerDuck gives you a single interface to clean up the bloat and unlock the good stuff.

It applies targeted system tweaks to reduce overhead and block unwanted behavior, and bundles several management tools so you can see what is running, remove what you do not want, and revert any change if something goes wrong.

Note

Every optimization can be applied manually. optimizerDuck just makes it easier for you to apply these optimizations.

Over 30 tweaks across 6 categories, each with a clear description and risk rating so you know exactly what each change does before applying it.

| Category | What it covers |
|---|---|
Performance |
Service host tuning based on your RAM, process priority adjustments, keyboard latency reduction, and multimedia scheduler tweaks for smoother gaming |
Privacy |
Disable Windows telemetry, error reporting, advertising ID, location tracking, Cortana, Copilot, and content delivery suggestions |
GPU |
Vendor-specific registry tweaks for AMD, NVIDIA, and Intel GPUs, covering power states, clock gating, and display latency |
Power |
Disable hibernation and fast startup, turn off USB selective suspend, install a custom high-performance power plan, and disable power throttling |
Bloatware & Services |
Block OEM app reinstall behavior and fine-tune startup types for 200+ Windows services |
User Experience |
Remove menu show delays, disable visual effects like taskbar animations and transparency for a snappier feel |

Note

The optimizations here are researched from well-known tools with large user bases, nothing is AI-generated or blindly added. Every tweak is chosen for real-world impact.

No need to dig through the registry, just toggles, dropdowns, and number inputs presented in one place. Organized into four categories:

**Desktop**: Show or hide icons (This PC, Recycle Bin, Network, User Files, Control Panel), remove shortcut arrow overlays**Preferences**: Taskbar alignment, widgets, Task View and End Task buttons, clock seconds, dark mode, file extensions, hidden files, clipboard history, compact view, snap assist, item checkboxes, classic context menu, and Bing search**Gaming**: Game Mode, Game Bar, background recording, mouse acceleration, fullscreen optimizations, hardware-accelerated GPU scheduling**System**: Enable Num Lock on boot

| Tool | What it does |
|---|---|
System Dashboard |
View your CPU, RAM, GPU, storage drives, and OS details in one panel |
Startup Manager |
See every app and task that launches at boot, toggle them on or off, and open their file location |
Scheduled Tasks |
Browse, run, stop, enable, disable, or delete Windows scheduled tasks |
Disk Cleanup |
Scan and clear temp files, system cache, Windows Update leftovers, prefetch, thumbnails, recycle bin, crash dumps, and old Windows installations |
Bloatware Remover |
Lists all removable AppX packages with risk badges (Safe, Caution, Unknown), so you can pick what to remove |

Changing system settings carries risk. optimizerDuck is built around reversibility and user control.

See the Privacy Policy for details on our data practices.

**Automatic backups**: Every change writes a revert file to a local folder. You can restore individual tweaks or roll back everything**One-click revert**: Undo any applied optimization from the UI with a single click**Risk ratings**: Each tweak is labeled Safe, Moderate, or Risky based on its potential impact**No defaults applied**: Nothing runs until you select it. The tool does not enable anything on its own**Restore point prompt**: Before your first optimization, the app suggests creating a Windows restore point

Yes. optimizerDuck is fully **open-source** (GPL v3), meaning anyone can inspect, audit, or build the source code themselves. Every release is built automatically by **GitHub Actions** from the public source; no hidden modifications, no unsigned binaries injected after build. If you prefer, you can clone the repo and build the `.exe`

yourself with a single `dotnet build`

.

The app does **not** collect any telemetry, usage data, or personal information. See the Privacy Policy.

It can help. Every optimization in optimizerDuck is **researched from well-known tools, community guides, and hardware vendor recommendations**, nothing is AI-generated, blindly added, or made up. Each tweak addresses a real setting that Windows configures conservatively by default (e.g., service host grouping, GPU power states, network throttling, process scheduling).

There are no fake registry hacks here, every change has a documented purpose and real-world impact backed by community testing and vendor documentation.

optimizerDuck is not code-signed because code signing certificates are expensive for open-source projects. When Windows encounters an unsigned executable downloaded from the internet, SmartScreen displays a warning by default. This is normal and does **not** mean the file is unsafe.

To bypass, click **"More info" > "Run anyway"**. If you are still concerned:

- Build the
`.exe`

yourself from source - Submit the binary to online sandboxes like ANY.RUN for independent verification

Yes. Every optimization creates a revert file before applying. You can undo individual tweaks or roll back everything from the UI with one click. The app also suggests creating a Windows System Restore point before your first optimization.

Yes. optimizerDuck supports **Windows 10 (x64)** and **Windows 11 (x64)**.

Yes. optimizerDuck modifies system settings and the Windows registry, so it requires administrator privileges to run.

No. The app contains zero telemetry, analytics, or phone-home functionality. It runs entirely offline and does not send any data anywhere.

A known Task Manager display bug triggered by non-default power plans, it incorrectly reports 100% CPU on some systems while actual load is normal. Visual only, does **not** affect real performance or cause overheating. If unwanted, simply toggle off this optimization.

**Framework**: WPF on .NET 10, using the WPF UI library for Fluent design**Revert system**: Four revert step types (Registry, Service, Scheduled Task, Shell) with JSON-persisted state and thread-safe file I/O**Theming**: Dark (default), Light, and High Contrast modes with Mica backdrop support**No installer**: Runs as a single .exe, no installation required**Backup system**: Local folder-based backup for every change, with one-click restore**Discovery**: Optimization and Feature categories are discovered automatically via reflection + custom attributes, no manual registration needed**No telemetry**: The app does not collect any user data

Guides, optimization details, and usage tips.

Bug reports, new optimizations, docs improvements, and translations are all welcome. See CONTRIBUTING.md (Japanese).

If optimizerDuck helped your PC:

- ⭐ Star the repo
- 💬 Join Discord for support
- 🐞 Report bugs on GitHub
- 🎁 Support the project here

- 🌐 Website
- 📖 Documentation
- 💬 Discord
- 🐞 Issues

Bug reports, feature suggestions, translations, and sharing your experience all help the project.

optimizerDuck is provided **"as is"**, without warranty of any kind.

By using this tool, you agree that the authors are not liable for system instability, data loss, or issues caused by third-party software or user modifications.

Always create a **restore point** before applying changes.

Note

optimizerDuck modifies system settings and the Windows registry. Use at your own risk. We recommend backing up important data and creating a restore point before making changes.

See Terms of Service, Privacy Policy, and Disclaimer for more information.