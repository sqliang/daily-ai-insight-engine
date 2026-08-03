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
pipeline_stage: ingested
id: e34a1c7cb7f4eedc
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