---
title: 'FreeInk: Open ecosystem for e-readers'
source: https://freeink.org/
author:
- '[[FriedPickles]]'
published: '2026-07-21'
created: '2026-07-22'
manifest_dates:
- '2026-07-22'
description: 'Article URL: https://freeink.org/ Comments URL: https://news.ycombinator.com/item?id=48996318
  Points: 552 # Comments: 120'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: e34a1c7cb7f4eedc
source_type: community_discussion
tldr: FreeInk 是一个开源电子纸阅读器生态项目，提供从硬件（开源 PCB 板 de-link）到社区固件再到硬件无关 SDK 的全栈开源方案，支持 ESP32-S3
  芯片和 EPUB 格式，物料成本约 60 美元，无需订阅或账户。
objective_summary: FreeInk 于其官网发布了一个完整的开源电子纸阅读器生态，包含社区固件（EPUB 2/3 渲染、WiFi 传输、KOReader
  同步、焦点阅读模式等）、硬件无关 SDK（通过 EInkDisplay、InputManager 等通用 API 抽象底层设备细节）以及开源硬件 de-link（基于
  ESP32-S3 的手工可焊 PCB，KiCad 原理图和物料清单全部公开）。项目兼容 Xteink X4/X3、M5Stack PaperColor、LilyGo
  T5 S3 等多款已有设备，所有层均以开放许可公开发布。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - ESP32-S3
  - EPUB 2 & 3
  - KOReader Sync
  - Calibre
  - OPDS
  - KiCad
  - TLS 1.3
  key_people: []
key_logic_flow:
- FreeInk 是一个开源集体，旨在构建电子纸阅读器的完整软件、固件和硬件栈，每个层面均以开放许可公开发布。
- 项目提供社区固件，支持 EPUB 2 和 3 渲染、可配置排版、WiFi 传输、Calibre 集成、KOReader 同步以及焦点阅读模式。
- FreeInk 提供一套硬件无关的 SDK，通过 EInkDisplay、InputManager、BatteryMonitor 等通用 API 抽象不同设备的显示控制器和波形等底层细节。
- de-link 是项目的开源硬件核心，基于 ESP32-S3 的紧凑 PCB，支持手工焊接，物料成本约 60 美元，KiCad 原理图与物料清单全部公开。
- 项目兼容多款已有电子纸设备，包括 Xteink X4/X3、M5Stack PaperColor、LilyGo T5 S3、M5Paper v1.1 等，新增设备只需添加配置文件和驱动配置。
- 从渲染引擎到充电电路，项目的每一层都公开文档并采用开放许可，鼓励社区复刻、审计和扩展。
object_mentions:
- object_type: project
  name: FreeInk
  canonical_name: FreeInk
  url: https://freeink.org/
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - FreeInk 是一个开源集体，构建电子纸阅读器的软件、固件和硬件栈，每个层面均以开放许可公开发布并接受社区贡献。
  - 项目提供社区固件、硬件无关 SDK 和开源硬件板 de-link，所有层都可被任何人复刻、扩展和定制。
  article_id: e34a1c7cb7f4eedc
- object_type: product
  name: de-link
  canonical_name: de-link
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - de-link 是 FreeInk 的开源硬件核心，基于 ESP32-S3 的紧凑 PCB，支持手工焊接且物料成本约 60 美元。
  - 该 PCB 包含 MCP73832 充电管理、DW01A 电池保护、可选前置灯和 24 针电子纸接口，KiCad 原理图和物料清单全部公开。
  article_id: e34a1c7cb7f4eedc
- object_type: project
  name: FreeInk SDK
  canonical_name: FreeInk SDK
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - FreeInk 提供硬件无关的 SDK，通过 EInkDisplay、InputManager 等通用 API 抽象不同电子纸设备的显示控制器和波形等底层细节。
  - 新增设备只需添加配置文件和驱动参数作为数据，而无需修改通用驱动代码路径。
  article_id: e34a1c7cb7f4eedc
- object_type: project
  name: KOReader
  canonical_name: KOReader
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - FreeInk 固件支持通过 KOReader Sync 协议同步阅读进度和位置，使阅读进度可在不同设备间保持一致。
  article_id: e34a1c7cb7f4eedc
- object_type: project
  name: Calibre
  canonical_name: Calibre
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - FreeInk 支持通过专用的 Calibre 插件直接从 Calibre 软件发送 EPUB 文件到阅读器设备上。
  article_id: e34a1c7cb7f4eedc
extract_result: success
---

# An open ecosystem for e-readers.

Free Ink is an open-source collective building the software, firmware and hardware for e-paper readers. Every layer ships in the open, so anyone can pick it up, extend it, and make it their own.

Open standards · open parts

- ESP32-S3
- EPUB 2 & 3
- GoodDisplay e-paper
- WiFi book transfer
- KOReader Sync
- Calibre plugin
- OPDS catalogs
- USB-C charging
- microSD storage
- Warm / cool frontlight
- Focus Reading
- Right-to-left layout
- Custom fonts
- OTA updates
- KiCad source
- 3D-printed case
- Swappable battery
- Hand-solderable
- No DRM
- Open hardware

## An e-reader experience tuned to how you read.

Community-built, fully open-source firmware for budget e-paper readers, with more features, more control, and an open base anyone can build on.

- EPUB 2 and 3 rendering
- Parses EPUB 2 and 3, applies embedded CSS, and lays out chapters in your font, size and margins. Pages are cached to SD on first open, so every reopen is near-instant.
- Configurable typography
- Noto Serif and Noto Sans built in, plus any font loaded from your SD card. Tune size, spacing, margins, hyphenation, alignment and anti-aliasing.
- WiFi transfer and sync
- The reader runs an upload server over WiFi. Drop EPUBs in from any browser, send straight from Calibre, and keep your place across devices with KOReader sync.
- Bookmark any passage
- Hold Confirm anywhere to drop a bookmark. Every saved spot remembers its page and reading percentage, so you can flip back to a favourite line in a tap.
- Focus Reading
- Bolds the front of each word to guide your eye and set your pace, with grayscale anti-aliasing and tiled rendering for fast, crisp page turns.
- Speaks your language
- Full right-to-left layout for Hebrew and Arabic, plus translated menus in Spanish, French, German, Italian, Portuguese, Russian, Ukrainian, Polish and more.

## One firmware API. Any e-paper device.

FreeInk is a hardware-independent SDK for building e-paper reader firmware. It abstracts the controller, waveforms, pins and peripherals behind a stable facade, so one generic codebase drives many devices, and a new board is a profile and a config, not a rewrite.

- Hardware-independent by design
- Every device-specific detail lives behind small injectable interfaces: the display controller, waveforms and LUTs, GPIOs, bus speeds, touch, frontlight and audio. The firmware calls one generic API and gets device-specific behavior.
- Clean, stable API
- A small, consistent surface across EInkDisplay, InputManager, BatteryMonitor, SDCardManager and BoardConfig. Firmware targets one library path and stays decoupled from the hardware underneath it.
- New devices are data, not code
- Adding a board means adding a profile and a driver config, supplying pins, geometry, waveforms and voltages as values rather than editing the generic driver. Per-device tuning stays out of the shared code path.
- Composable builds
- A build is composed along two axes: devices and capabilities. Touch, frontlight, color and audio are gated by flags and default on only when a device needs them, so each binary stays as tight as possible.
- Touch and frontlight built in
- Capacitive touch for CHSC6x and GT911 controllers, plus PWM frontlight with warm / cool control. The InputManager exposes raw touch points and the app owns rotation.
- TLS 1.3 networking
- SecureNet bundles wolfSSL compiled from source for TLS 1.3 + PSA, bypassing the stubbed system mbedTLS so the reader can reach TLS-1.3-only servers like KOReader sync.

### Supported devices

| Device | MCU | Controller | Panel | Status |
|---|---|---|---|---|
| Xteink X4 | ESP32-C3 | SSD1677 | 800×480 B/W + 4-level gray | |
| Xteink X3 | ESP32-C3 | UC8253 | 792×528 B/W + 4-level gray | |
| de-link | ESP32-S3 | SSD1677 | 800×480 B/W + gray, frontlight | |
| M5Stack PaperColor | ESP32-S3 | ED2208 | 400×600 Spectra-6 color | |
| Murphy M3 | ESP32-S3 | UC8253 | 240×416 B/W, touch + frontlight | |
| LilyGo T5 S3 | ESP32-S3 | ED047TC1 | 960×540 16-gray, touch, I²C gauge | |
| Sticky | ESP32-S3 | SSD1677 | 3.97″ 800×480 B/W, GT911 touch, sensor suite | |
| M5Paper v1.1 | ESP32 (classic) | IT8951E | 540×960 16-gray, GT911 touch |

Related devices can share a single firmware build, detected and configured at runtime, while new controllers slot in as a standalone driver behind the facade.

## An e-reader you can actually open.

de-link is the open hardware core of the project: a compact, hand-solderable ESP32-S3 board with published KiCad schematics and a full bill of materials. Charging, battery protection, an optional frontlight and a 24-pin e-paper interface, all on one PCB you can build for around $60.

- Compute
- ESP32-S3 at 240 MHz, dual-core, with WiFi, BLE, 16 MB flash and optional PSRAM
- Display
- 24-pin SPI e-paper for GoodDisplay panels (3.97″, 4.26″, 7.5″ and up)
- Storage
- microSD over a 4-bit SDMMC interface, for your whole library offline
- Power
- Bring-your-own LiPo with overcharge and overdischarge protection, charged over USB-C (OTG)
- Charging
- MCP73832 charge controller, with DW01A and FS8205A cell protection
- Frontlight
- Optional series LED frontlight with cool / warm control and PWM brightness
- Controls
- Dual 4-switch resistor ladders plus a reset button
- Expansion
- Multi-function GPIO broken out for modules and your own hacks

## A foundation anyone can build on.

From the rendering engine to the charging circuit, every layer is documented and open. It all adds up to a shared foundation the whole community can build on, fix and extend.

- Open formats, open files
- Books are plain files on an SD card, in open standards you can read, copy and keep on any device, forever.
- Open all the way down
- Software, firmware and hardware are public and permissively licensed. Fork it, audit it, build on it.
- Repairable by design
- Hand-solderable parts, a published BOM and a swappable battery. Fix it instead of landfilling it.
- Truly yours
- Own it outright, with no subscriptions and no accounts. The device and its software stay yours.
- Built by the community
- Developed in the open by readers and tinkerers, with nightly builds, shared themes and contributions welcome.
- Endlessly hackable
- Spare GPIO, custom fonts, themeable menus. Make it weird, make it fast, make it yours.

## Open from pixels to PCB.

Every layer is public and permissively licensed. Read and audit the community firmware, then build, repair and remix the board. The whole stack ships in the open.

- ~$60
- Rough cost to build your own
- 10+
- Interface languages
- USB-C
- Standard-cable charging
- 100%
- Open schematics & BOM

▰ software + hardware, in the open

## Let’s build something together.

Whether you want to collaborate, need a hand with your device, have a custom build in mind, or want to partner up — we’d love to hear from you.

- Collaboration
- Building something in the open e-reader space? Let’s join forces on firmware, tooling, or research.
- Device support
- Stuck on a flash, a board revision, or a feature on your reader? Reach out and we’ll help you sort it.
- Custom development
- Need bespoke firmware, a port to new hardware, or a feature built to spec? Tell us what you have in mind.
- Partnerships
- Manufacturers, distributors, and communities welcome. Let’s talk about shipping open devices together.