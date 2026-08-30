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