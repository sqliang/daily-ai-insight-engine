---
title: AprilNEA/OpenLogi
source: https://github.com/AprilNEA/OpenLogi
author: []
published: ''
created: '2026-08-21'
manifest_dates:
- '2026-08-21'
- '2026-08-22'
- '2026-08-23'
- '2026-08-24'
- '2026-08-25'
description: '⚡️A native, local-first alternative to Logitech Options+, written in
  Rust 🦀 — remap buttons, DPI, and SmartShift over HID++. No account, no telemetry.https://openlogi.org
  Warning OpenLogi is under active development and not yet stable — features and config
  may still change. Give the repo a Star ⭐ and Watch 👀 it to get notified when a new
  release lands. English | 简体中文 | 日本語 | Deutsch | Français | 한국어 OpenLogi ⚡️ A native,
  local-first alternative to Logitech Options+, written in Rust 🦀Unlock the full capabilities
  of Logitech mice, keyboards, and webcams over HID++ and UVC Fed up with Options+?
  Try OpenLogi. Runs on macOS, Linux, and Windows. Beyond Options+ Things OpenLogi
  does that Options+ won''t: Stay light. Native Rust + GPUI. Run on Linux. Linux is
  a first-class platform in OpenLogi. Gestures on any button. Give the gesture role
  to any physical button — or turn gestures off entirely. Plain-text config. Everything
  is one TOML file you can sync between machines however you like. Script it. A real
  CLI alongside the GUI. Features Devices connected over Logi Bolt receivers, Unifying
  receivers, Bluetooth, or a wired connection, with battery percentage and charge
  state Button remapping via the OS input hook: a built-in action catalog plus custom
  keyboard shortcuts authored in the TOML config¹ Per-application profile overlays
  that auto-switch on app focus (macOS + Windows; Linux on X11 / XWayland only) Litra
  lights: power, brightness, and color temperature, with optional auto power that
  follows camera activity Mouse Capture and remap the middle, mode-shift, and thumbwheel
  buttons (middle everywhere, the rest where the device exposes them) Per-direction
  gesture bindings with live capture, on any capable button Actions Ring: a cursor-centred,
  eight-slot overlay of actions (ShowActionsRing), with per-application layouts DPI
  control with presets and Cycle / Set-preset actions (0x2201) SmartShift wheel: mode
  toggle, sensitivity, and a permanent-ratchet panel (0x2111) Per-device native scroll
  inversion (0x2121, supported devices) Keyboard Global F-key remapping: the same
  action catalog as the mouse, plus power-user actions — typed text, key combos, multi-step
  workflows (macOS + Windows) Static RGB lighting (0x8070 / 0x8080, supported devices)
  Camera Any Logitech UVC webcam (Brio, StreamCam, the C920 series, …), plug and play
  Live preview that opens the camera only while you watch — leaving it releases the
  camera entirely and the LED goes off Image controls written straight to the UVC
  hardware — zoom, focus, exposure, brightness, contrast, saturation, sharpness, white
  balance, tint, with auto-mode toggles for focus / exposure / white balance — so
  changes apply in Meet / Zoom / OBS and every other app using the camera One-click
  profiles: built-in Default / Streaming / Video call plus custom snapshots; settings
  persist per camera and are written back to the hardware on the next view ¹ Media
  key actions use D-Bus MPRIS on Linux; a handful of macOS-specific actions have no
  universal Linux equivalent and are no-ops. Windows maps platform actions to native
  equivalents where available. Install Important Quit Logi Options+ first: the two
  applications fight over HID++ access, and only one can own a given receiver at a
  time. macOS Requires macOS 13 or later. Download the signed, notarized .dmg from
  the latest release and drag OpenLogi.app to /Applications. Or install via Homebrew:
  brew install --cask openlogi The official Homebrew cask is the default installation
  path. To explicitly track the latest GitHub release from aprilnea/tap instead: brew
  tap aprilnea/tap brew install --cask aprilnea/tap/openlogi@latest openlogi@latest
  is maintained by OpenLogi''s release workflow and may update before the official
  cask autobump lands. Install either openlogi or openlogi@latest, not both. Linux
  Download the package for your distribution from the latest release: # Debian / Ubuntu
  sudo dpkg -i openlogi_*.deb # Fedora / RHEL sudo rpm -i openlogi-*.rpm # Arch Linux
  sudo pacman -U openlogi-*.pkg.tar.zst Packages are published for both x86_64/amd64
  and arm64/aarch64. NixOS users can instead import the repository''s module, which
  installs the package and udev rules and starts the agent with the graphical session:
  { inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable"; inputs.openlogi =
  { url = "github:AprilNEA/OpenLogi"; inputs.nixpkgs.follows = "nixpkgs"; }; outputs
  = { nixpkgs, openlogi, ... }: { nixosConfigurations.my-host = nixpkgs.lib.nixosSystem
  { system = "x86_64-linux"; # or aarch64-linux modules = [ openlogi.nixosModules.default
  { programs.openlogi.enable = true; } ]; }; }; } All Linux packages install udev
  rules that grant your user access to /dev/hidraw*, /dev/uinput and your Logitech
  mouse''s /dev/input/event* node without sudo. The NixOS module starts the agent
  automatically; after a .deb, .rpm, or .pkg.tar.zst installation, enable it for your
  user: systemctl --user enable --now openlogi-agent.service See docs/INSTALL-linux.md
  for complete NixOS options, manual / source installs, and distros without systemd.
  Windows Signed portable .zip archives and per-user .msi installers (x86_64 and arm64)
  are attached to each release. Both ship the GUI (OpenLogi.exe) together with the
  background agent (openlogi-agent.exe), which owns all device I/O. Keep the two files
  side by side when using the portable zip, or the GUI has nothing to connect to.
  Windows support has been validated end-to-end on Windows 11 with real hardware (a
  wired keyboard and a Unifying-receiver mouse), including install, in-place upgrade,
  and uninstall of the MSI. It is newer than the macOS build, so if you hit a rough
  edge please report it. The agent shows a system-tray icon (Show Main Window / Quit)
  so the app stays reachable after the main window is closed. To disable it on Windows,
  set show_in_menu_bar = false in the TOML [app_settings] block and restart the agent;
  the GUI toggle is currently macOS-only. To build from source, see DEVELOPMENT.md.
  Usage (CLI) See USAGE.md Configuration See CONFIGURATION.md Developing See DEVELOPMENT.md
  Acknowledgments Windows, cameras, and i18n by @davidbudnick — keyboard RGB, Windows
  support, Logitech webcam support Linux port by @cserby — Linux support Solaar by
  @pwr — open-source HID++ implementation Mouser by @TomBadash — a local, account-free
  Options+ replacement License The code in this repository is dual-licensed under
  either of Apache License, Version 2.0 (LICENSE-APACHE) MIT license (LICENSE-MIT)
  at your option. Third-party code crates/openlogi-hidpp is a vendored fork of hidpp
  by @lus, licensed 0BSD. Logo & brand assets Thanks to @kubai087 for designing the
  OpenLogi logo. The OpenLogi logo and app icon (the brand assets under design/) are
  © 2026 AprilNEA, all rights reserved, and are not covered by the MIT/Apache licenses
  above; see design/LICENSE. Forking the code grants no right to the OpenLogi name,
  logo, or icon; please don''t use them to represent your own projects, forks, or
  distributions without prior written permission. Not affiliated with Logitech. "Logitech",
  "MX Master", and "Options+" are trademarks of Logitech International S.A. Repo activity'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ee0cd95680ac6fbe
source_type: community_discussion
tldr: OpenLogi 是一个用 Rust 编写的本地优先开源项目，作为 Logitech Options+ 的替代品，通过 HID++ 和 UVC 协议在
  macOS、Linux、Windows 上实现 Logitech 鼠标、键盘和摄像头的完整控制，当前仍处于活跃开发阶段。
objective_summary: OpenLogi 由 AprilNEA 开发，是一个用 Rust 编写的开源项目，定位为 Logitech Options+
  的本地优先替代品，当前处于活跃开发阶段且尚未稳定。它通过 HID++ 和 UVC 协议在 macOS、Linux 和 Windows 上支持 Logitech
  鼠标、键盘与网络摄像头，功能涵盖按钮重映射、手势、DPI 控制、SmartShift 滚轮、F 键重映射、RGB 灯效以及 UVC 图像参数直写。项目采用单一
  TOML 文件配置并附带 CLI，Linux 软件包内置免 sudo 的 udev 规则，NixOS 用户可通过模块直接启用。代码以 Apache 2.0 或
  MIT 双重许可证发布，但项目与 Logitech 无隶属关系。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - AprilNEA
  - Logitech
  technologies:
  - HID++
  - UVC
  - Rust
  - GPUI
  - TOML
  - MPRIS
  key_people:
  - AprilNEA
  - davidbudnick
  - cserby
  - pwr
  - TomBadash
  - lus
  - kubai087
key_logic_flow:
- OpenLogi 是一个用 Rust 原生编写、本地优先的 Logitech Options+ 替代品，通过 HID++ 和 UVC 协议控制 Logitech
  鼠标、键盘与网络摄像头，目前处于活跃开发阶段。
- 它支持 macOS、Linux、Windows 三大平台，覆盖 Logi Bolt、Unifying 接收器、蓝牙和有线等多种连接方式，并显示电池百分比与充电状态。
- 鼠标功能包括按钮重映射、手势绑定、Actions Ring 操作环、DPI 控制、SmartShift 滚轮和原生滚动方向反转。
- 键盘支持全局 F 键重映射与静态 RGB 灯效，摄像头功能则直接向 UVC 硬件写入曝光、白平衡、缩放等图像控制参数。
- 配置采用单一 TOML 文件并提供 CLI，Linux 软件包安装的 udev 规则让用户免 sudo 访问 HID 设备节点。
- 项目采用 Apache 2.0 或 MIT 双重许可证发布，但品牌资产不在此授权范围内，且与 Logitech 无隶属关系。
object_mentions:
- object_type: project
  name: AprilNEA/OpenLogi
  canonical_name: AprilNEA/OpenLogi
  url: https://github.com/AprilNEA/OpenLogi
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - OpenLogi 是一个用 Rust 编写的原生、本地优先的 Logitech Options+ 替代品，通过 HID++ 和 UVC 协议控制 Logitech
    鼠标、键盘和网络摄像头。
  - 项目支持 macOS、Linux 和 Windows，覆盖 Logi Bolt、Unifying 接收器、蓝牙与有线连接，并显示电池百分比和充电状态。
  - 配置集中在一个 TOML 文件中并附带 CLI，Linux 软件包内置免 sudo 的 udev 规则，NixOS 用户可通过模块直接启用。
  article_id: ee0cd95680ac6fbe
- object_type: project
  name: Solaar
  canonical_name: Solaar
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Solaar 由 @pwr 开发，是一个开源的 HID++ 协议实现，OpenLogi 在 README 中将其列为设计参考。
  article_id: ee0cd95680ac6fbe
- object_type: project
  name: Mouser
  canonical_name: Mouser
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Mouser 由 @TomBadash 开发，是一个本地运行、无需账号的 Logitech Options+ 替代品，OpenLogi 将其列为参考项目。
  article_id: ee0cd95680ac6fbe
- object_type: product
  name: Logitech Options+
  canonical_name: Logitech Options+
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Logitech Options+ 是 Logitech 官方的外设配置软件，OpenLogi 定位为它的原生本地替代品，并提醒用户使用时需先退出 Options+。
  article_id: ee0cd95680ac6fbe
- object_type: project
  name: hidpp
  canonical_name: lus/hidpp
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - crates/openlogi-hidpp 是 OpenLogi 对 @lus 所开发 hidpp 仓库的 vendored fork，采用 0BSD 许可证。
  article_id: ee0cd95680ac6fbe
extract_result: success
impact_score:
  score: 3.0
  reason: 评分依据：该事件是一个垂直领域开源工具（Logitech 外设控制替代品）的社区发布，不属于 AI 行业范式转移，也未改变局部竞争格局。其对 AI
    行业短期的直接冲击很小，但在 Linux/macOS 外设控制这一长期被厂商专有软件忽视的细分市场上，提供了扎实的本地优先开源方案，可能获得一定社区关注并对
    Logitech 等厂商的软件策略形成微弱压力。介于'日常更新/小圈子'与'重要产品发布'之间，综合评定为 3.0 分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: Linux 用户终于获得 Logitech 外设的一等公民级开源控制方案（免 sudo + 全功能）
hype_assessment:
  level: low
  reason: 判定依据：项目 README 明确标注 'under active development and not yet stable'，主动提示功能可能变更，未使用'颠覆'、'革命性'等
    PR 滥用词汇；每项功能均附带具体 HID++ 特性 ID（如 0x2201 DPI、0x2111 SmartShift、0x8070 RGB）与 UVC
    参数说明，属于可验证的务实技术陈述，含水量极低。
information_entropy: high
domain_disruption:
  technical_innovation: 通过逆向 Logitech HID++ 协议，以 Rust + GPUI 原生架构实现跨平台（含 Linux 一等公民）的鼠标/键盘/摄像头全功能控制；摄像头部分直接向
    UVC 硬件写入曝光、白平衡等图像参数，改动可即时作用于 Meet/Zoom/OBS 等所有消费方，绕开了厂商专有软件层。
  business_model: 以 MIT/Apache 双许可开源模式直接替代厂商捆绑销售的专有软件 Options+，并通过 Homebrew cask、deb/rpm/arch
    包、NixOS 模块等全渠道分发，挑战硬件厂商以软件锁定用户生态的策略；对 AI/软件行业本身的商业模式影响有限，更多体现开源社区对闭源驱动工具的胜利。
engineering_complexity: prototype
compound_value:
  score: 4.0
  reason: 本地优先的 Logitech 外设控制工具，价值捕获集中在终端应用层，缺乏平台效应与网络效应，长期复利天花板有限。但并非昙花一现：项目沉淀了 HID++/UVC
    协议逆向知识与跨平台 Rust 控制栈，且 Linux 上 Logitech 官方不提供 Options+，存在持续刚需——在 NixOS 等重度用户社区已形成事实标准雏形。若社区维护活跃度能跨过活跃开发期，有望成为开源世界操控
    Logitech 硬件的细分基础设施；但依赖单一硬件生态、纯免费分发、无商业模式，3-5 年后难以成为行业基石，故给 4 分（细分赛道潜力待验证）。
value_capture_layer: end_application
moat_impact: democratizes_access
key_beneficiaries:
- Linux 桌面生态（发行版/NixOS 社区）
- Logitech 外设用户群体
- Rust 桌面生态（GPUI）
- Solaar 等同生态 HID++ 开源项目
competitive_casualty:
- Logi Options+（Logitech 专有软件）
- Logitech 的软件生态锁定与遥测数据收集策略
market_opportunities:
- 针对对 Logitech Options+ 不满的开发者与极客群体，可围绕 OpenLogi 构建多机 TOML 配置同步、配置模板市场或企业批量部署等周边服务，将'设备配置即代码'变现
- 其'本地优先 + HID++/UVC 硬件直写 + 纯文本配置 + CLI'的产品模式可复制到其他外设品牌或设备品类（如机械键盘、RGB 灯控、游戏外设），形成开源外设控制生态的创业机会
- 在 Linux 开发者工作站与本地 AI 设备管理场景中，这类免 sudo、可脚本化的外设控制工具可作为整机交付方案（如 NixOS 模块、DevContainer
  镜像）的组成部分进行集成
risk_matrix:
  regulatory: 逆向工程 Logitech 私有 HID++ 协议存在潜在法律风险（尽管 Solaar 等先例显示 Logitech 尚未对同类项目提起诉讼）；项目名与文档中使用
    Logitech 商标，存在商标合规风险；品牌资产被明确排除在双许可授权之外，可能限制其生态的商业化路径
  technological: 项目处于活跃开发且未稳定阶段，配置格式与 API 可能频繁变动；HID++ 协议随 Logitech 新硬件/固件迭代需持续逆向维护，存在跟进失效风险；GUI
    基于较新的 GPUI 框架，生态成熟度与长期可维护性有限
  competitive: 直面 Solaar（Linux 下成熟开源竞品）、Logitech Options+/G HUB 官方软件及 Piper/libratbag
    等替代品的竞争；若 Logitech 官方加强 Linux 支持或更新 HID++ 协议，将显著挤压该项目生存空间
  ethical: 本地优先设计显著降低隐私与遥测风险，但硬件级 HID/UVC 参数直写若配置不当可能造成设备异常或误操作；与 Options+ 并发运行会争抢
    HID++ 设备访问权导致冲突
  additional:
  - 项目由单一维护者主导，存在维护者失联或项目停滞的 bus-factor 风险
  - Linux 安装包内置的 udev 规则授予用户对 /dev/hidraw* 等设备节点访问权，若被恶意软件利用可能扩大攻击面
confidence:
  impact: medium
  compound: low
  hype: high
actionable_insight: monitor
object_insights:
- object_type: project
  name: AprilNEA/OpenLogi
  canonical_name: AprilNEA/OpenLogi
  url: https://github.com/AprilNEA/OpenLogi
  positioning: 本地优先、用 Rust 原生编写的 Logitech Options+ 开源替代品，通过 HID++ 与 UVC 协议在三大平台实现罗技外设的完整控制。
  technical_signal: 采用 Rust + GPUI 原生实现，通过 HID++ 与 UVC 协议直写硬件，支持单一 TOML 文件配置、CLI 脚本化及跨平台包分发。
  adoption_signal: 项目处于活跃开发阶段尚未稳定，已提供 macOS 签名公证安装包、官方 Homebrew cask 与 Linux 各发行版软件包，并有
    NixOS 模块支持。
  ecosystem_relevance: 填补 Logitech Options+ 不支持 Linux 的生态空缺，与 Solaar、Mouser 等开源 HID++
    工具形成互补，并通过 udev 规则与 NixOS 模块融入 Linux 发行版生态。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: OpenLogi 以本地优先、跨平台姿态切入 Logitech 官方软件的空档，尤其在 Linux 生态具有独特价值，且功能横跨鼠标、键盘、摄像头三类外设，进展值得持续跟踪。
  risk_notes:
  - 项目处于活跃开发阶段且尚未稳定，功能与配置格式仍可能发生变动。
  - 与 Logitech Options+ 抢占 HID++ 访问权，二者同时运行会冲突，用户须先退出官方软件。
  - 品牌资产不随代码开源，项目与 Logitech 无隶属关系，长期硬件兼容性存在不确定性。
  score: 8.0
  article_ids:
  - ee0cd95680ac6fbe
  evidence_snippets:
  - OpenLogi 是一个用 Rust 编写的原生、本地优先的 Logitech Options+ 替代品，通过 HID++ 和 UVC 协议控制 Logitech
    鼠标、键盘和网络摄像头。
  - 项目支持 macOS、Linux 和 Windows，覆盖 Logi Bolt、Unifying 接收器、蓝牙与有线连接，并显示电池百分比和充电状态。
  - 配置集中在一个 TOML 文件中并附带 CLI，Linux 软件包内置免 sudo 的 udev 规则，NixOS 用户可通过模块直接启用。
- object_type: project
  name: Solaar
  canonical_name: Solaar
  url: null
  positioning: 一个开源的 HID++ 协议实现项目，由 @pwr 开发，是 Logitech 设备在 Linux 控制生态中的成熟参考实现。
  technical_signal: 作为 OpenLogi 的设计参考，Solaar 提供了成熟的 HID++ 协议实现，是 Linux 上罗技设备控制的代表性开源方案。
  adoption_signal: 被 OpenLogi 等新一代项目在 README 中列为设计参考，侧面反映其在开源社区已具备一定的认可度与影响力。
  ecosystem_relevance: Solaar 属于 Logitech HID++ 协议的开源生态，其实现为后续跨平台替代方案提供了可复用的协议基础与设计参照。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Solaar 作为 HID++ 协议的开源参考实现，其成熟度与设计决策会持续影响 OpenLogi 等新一代替代品的演进方向，值得在
    Logitech 开源生态语境中保持观察。
  risk_notes:
  - 文章仅将其列为设计参考，缺乏对 Solaar 自身功能、维护与社区状态的直接信息，独立跟踪依据有限。
  score: 4.0
  article_ids:
  - ee0cd95680ac6fbe
  evidence_snippets:
  - Solaar 由 @pwr 开发，是一个开源的 HID++ 协议实现，OpenLogi 在 README 中将其列为设计参考。
- object_type: project
  name: Mouser
  canonical_name: Mouser
  url: null
  positioning: 一个由 @TomBadash 开发的本地运行、无需账号的 Logitech Options+ 替代品，被 OpenLogi 在 README
    中列为参考项目。
  technical_signal: 强调本地运行与免账号的使用方式，属于不依赖云端服务的 Logitech 外设配置方案。
  adoption_signal: 被 OpenLogi 列为参考项目，表明其在同类 Logitech Options+ 替代品中具备一定的设计参考价值。
  ecosystem_relevance: 与 OpenLogi、Solaar 同属 Logitech Options+ 的开源替代生态，共同推动外设配置脱离官方软件绑定。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Mouser 代表免账号、本地优先的 Logitech Options+ 替代方向，与 OpenLogi 形成设计对照，其取舍可反映该细分开源生态的演进趋势，值得一并观察。
  risk_notes:
  - 文章仅将其作为参考项目提及，缺乏功能细节与维护状态信息，独立跟踪价值有限。
  score: 4.0
  article_ids:
  - ee0cd95680ac6fbe
  evidence_snippets:
  - Mouser 由 @TomBadash 开发，是一个本地运行、无需账号的 Logitech Options+ 替代品，OpenLogi 将其列为参考项目。
- object_type: product
  name: Logitech Options+
  canonical_name: Logitech Options+
  url: null
  positioning: Logitech 官方的外设配置软件，是 OpenLogi 等开源项目瞄准替代的既有产品，提供鼠标、键盘与摄像头等罗技设备的官方管理入口。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 使用 Logitech 外设的普通用户
  - 依赖官方软件统一管理外设的企业用户
  product_signal: 作为官方配套软件，Options+ 提供 Logitech 外设的完整配置能力，但与 OpenLogi 竞争 HID++ 访问权，二者不能同时运行。
  market_signal: Logitech 官方软件在 Linux 平台缺位，且被替代品定位为臃肿方案，这为本地优先的 OpenLogi 等开源项目留下了市场空档。
  differentiation: 与开源替代品的核心差异在于官方授权与硬件兼容性保证，但平台支持范围受限，在 Linux 等场景存在明显短板。
  watch_reason: Logitech Options+ 作为 OpenLogi 等开源项目的直接对标产品，其功能演进、平台支持与产品策略变化将直接影响替代方案的生存空间，值得持续跟踪。
  risk_notes:
  - 官方软件的功能与平台策略受 Logitech 商业决策影响，开源替代方案的兼容窗口存在不确定性。
  score: 3.0
  article_ids:
  - ee0cd95680ac6fbe
  evidence_snippets:
  - Logitech Options+ 是 Logitech 官方的外设配置软件，OpenLogi 定位为它的原生本地替代品，并提醒用户使用时需先退出 Options+。
---

Warning

**OpenLogi is under active development** and not yet stable — features and config may still change. Give the repo a **Star** ⭐ and **Watch** 👀 it to get notified when a new release lands.

**⚡️ A native, local-first alternative to Logitech Options+, written in Rust 🦀Unlock the full capabilities of Logitech mice, keyboards, and webcams over HID++ and UVC**


Fed up with Options+? Try OpenLogi.

Runs on macOS, Linux, and Windows.

Things OpenLogi does that Options+ won't:

**Stay light.**Native Rust + GPUI.**Run on Linux.**Linux is a first-class platform in OpenLogi.**Gestures on any button.**Give the gesture role to any physical button — or turn gestures off entirely.**Plain-text config.**Everything is one TOML file you can sync between machines however you like.**Script it.**A real CLI alongside the GUI.

- Devices connected over Logi Bolt receivers, Unifying receivers, Bluetooth, or a wired connection, with battery percentage and charge state
- Button remapping via the OS input hook: a built-in action catalog plus custom keyboard shortcuts authored in the TOML config¹
- Per-application profile overlays that auto-switch on app focus (macOS + Windows; Linux on X11 / XWayland only)
- Litra lights: power, brightness, and color temperature, with optional auto power that follows camera activity

**Mouse**

- Capture and remap the middle, mode-shift, and thumbwheel buttons (middle everywhere, the rest where the device exposes them)
- Per-direction gesture bindings with live capture, on any capable button
- Actions Ring: a cursor-centred, eight-slot overlay of actions (
`ShowActionsRing`

), with per-application layouts - DPI control with presets and Cycle / Set-preset actions (
`0x2201`

) - SmartShift wheel: mode toggle, sensitivity, and a permanent-ratchet panel (
`0x2111`

) - Per-device native scroll inversion (
`0x2121`

, supported devices)

**Keyboard**

- Global F-key remapping: the same action catalog as the mouse, plus power-user actions — typed text, key combos, multi-step workflows (macOS + Windows)
- Static RGB lighting (
`0x8070`

/`0x8080`

, supported devices)

**Camera**

- Any Logitech UVC webcam (Brio, StreamCam, the C920 series, …), plug and play
- Live preview that opens the camera only while you watch — leaving it releases the camera entirely and the LED goes off
- Image controls written straight to the UVC hardware — zoom, focus, exposure, brightness, contrast, saturation, sharpness, white balance, tint, with auto-mode toggles for focus / exposure / white balance — so changes apply in Meet / Zoom / OBS and every other app using the camera
- One-click profiles: built-in Default / Streaming / Video call plus custom snapshots; settings persist per camera and are written back to the hardware on the next view

¹ Media key actions use D-Bus MPRIS on Linux; a handful of macOS-specific actions have no universal Linux equivalent and are no-ops. Windows maps platform actions to native equivalents where available.

Important

Quit **Logi Options+** first: the two applications fight over HID++ access, and only one can own a given receiver at a time.

Requires macOS 13 or later.

Download the signed, notarized `.dmg`

from the latest release and drag `OpenLogi.app`

to `/Applications`

.

Or install via Homebrew:

`brew install --cask openlogi`

The official Homebrew cask is the default installation path. To explicitly
track the latest GitHub release from `aprilnea/tap`

instead:

```
brew tap aprilnea/tap
brew install --cask aprilnea/tap/openlogi@latest
```

`openlogi@latest`

is maintained by OpenLogi's release workflow and may update
before the official cask autobump lands. Install either `openlogi`

or
`openlogi@latest`

, not both.

Download the package for your distribution from the latest release:

```
# Debian / Ubuntu
sudo dpkg -i openlogi_*.deb
# Fedora / RHEL
sudo rpm -i openlogi-*.rpm
# Arch Linux
sudo pacman -U openlogi-*.pkg.tar.zst
```

Packages are published for both `x86_64`

/`amd64`

and `arm64`

/`aarch64`

.

NixOS users can instead import the repository's module, which installs the package and udev rules and starts the agent with the graphical session:

```
{
inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
inputs.openlogi = {
url = "github:AprilNEA/OpenLogi";
inputs.nixpkgs.follows = "nixpkgs";
};
outputs = { nixpkgs, openlogi, ... }: {
nixosConfigurations.my-host = nixpkgs.lib.nixosSystem {
system = "x86_64-linux"; # or aarch64-linux
modules = [
openlogi.nixosModules.default
{ programs.openlogi.enable = true; }
];
};
};
}
```

All Linux packages install udev rules that grant your user access to
`/dev/hidraw*`

, `/dev/uinput`

and your Logitech mouse's `/dev/input/event*`

node without `sudo`

. The NixOS module starts the agent automatically; after a
`.deb`

, `.rpm`

, or `.pkg.tar.zst`

installation, enable it for your user:

`systemctl --user enable --now openlogi-agent.service`

See docs/INSTALL-linux.md for complete NixOS options, manual / source installs, and distros without systemd.

Signed portable `.zip`

archives and per-user `.msi`

installers (x86_64 and
arm64) are attached to each release. Both ship the GUI (`OpenLogi.exe`

)
together with the background agent (`openlogi-agent.exe`

), which owns all
device I/O. Keep the two files side by side when using the portable zip, or
the GUI has nothing to connect to.

Windows support has been validated end-to-end on Windows 11 with real
hardware (a wired keyboard and a Unifying-receiver mouse), including
install, in-place upgrade, and uninstall of the MSI. It is newer than the
macOS build, so if you hit a rough edge please
report it. The agent shows a
system-tray icon (Show Main Window / Quit) so the app stays reachable after
the main window is closed. To disable it on Windows, set
`show_in_menu_bar = false`

in the TOML `[app_settings]`

block and restart the
agent; the GUI toggle is currently macOS-only.

To build from source, see DEVELOPMENT.md.

See USAGE.md

See CONFIGURATION.md

See DEVELOPMENT.md

**Windows, cameras, and i18n**by @davidbudnick — keyboard RGB, Windows support, Logitech webcam support**Linux port**by @cserby — Linux support- Solaar by @pwr — open-source HID++ implementation
- Mouser by @TomBadash — a local, account-free Options+ replacement

The code in this repository is dual-licensed under either of

- Apache License, Version 2.0 (LICENSE-APACHE)
- MIT license (LICENSE-MIT)

at your option.

`crates/openlogi-hidpp`

is a vendored fork of `hidpp`

by @lus, licensed 0BSD.

Thanks to @kubai087 for designing the OpenLogi
logo. The OpenLogi logo and app icon (the brand assets under
`design/`

) are © 2026 AprilNEA, all rights reserved, and are not covered by the MIT/Apache
licenses above; see `design/LICENSE`

. Forking the code grants
no right to the OpenLogi name, logo, or icon; please don't use them to represent
your own projects, forks, or distributions without prior written permission.

**Not affiliated with Logitech.** "Logitech", "MX Master", and "Options+" are trademarks of Logitech International S.A.