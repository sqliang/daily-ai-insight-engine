---
title: ESP32-S31
source: https://www.espressif.com/en/products/socs/esp32-s31
author:
- '[[volemo]]'
published: '2026-06-03'
created: '2026-06-04'
description: 'Article URL: https://www.espressif.com/en/products/socs/esp32-s31 Comments
  URL: https://news.ycombinator.com/item?id=48385965 Points: 251 # Comments: 141'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: f9dacd28a2b408bd
source_type: community_discussion
tldr: 乐鑫科技（Espressif Systems）发布 ESP32-S31 双核 RISC-V SoC，集成 Wi-Fi 6、蓝牙 5.4 LE Audio、Thread/Zigbee
  和千兆以太网，支持高级 HMI、摄像头与 LCD 显示，配备 TEE 与 PUF 安全能力，适用于 AI 语音与智能交互设备。
objective_summary: 乐鑫科技发布了 ESP32-S31 系统级芯片，该芯片采用双核 32 位 RISC-V 架构，主频 320 MHz，集成 2.4
  GHz Wi-Fi 6、蓝牙 5.4 LE Audio、IEEE 802.15.4（Thread/Zigbee）以及千兆以太网 MAC。芯片配备 512 KB
  SRAM、支持 8 位 DDR PSRAM，提供 DVP 摄像头接口和最高 24 位并行 RGB LCD 支持，内置 JPEG 编解码器和 2D-DMA 等硬件加速器。安全方面集成
  TRNG、PUF、TEE 和 APM 能力。该 SoC 将通过 ESP-IDF、ESP-Matter、ESP-BLE-AUDIO 和 ESP-GMF 等开源框架获得软件支持，并可与
  LLM 配合构建 AI 语音与智能交互设备。
event_type: infrastructure_update
epistemic_status: pr_statement
entities:
  companies:
  - Espressif Systems
  technologies:
  - RISC-V
  - Wi-Fi 6
  - 802.11ax
  - IEEE 802.15.4
  - Thread
  - Zigbee
  - Bluetooth 5.4 LE
  - LE Audio
  - Bluetooth Mesh 1.1
  - SIMD
  - JPEG
  - PPA
  - 2D-DMA
  - LC3
  - TRNG
  - PUF
  - TEE
  - APM
  - AES-128/256
  - RSA
  - ECDSA
  - ECC
  - ESP-IDF
  - ESP-Matter
  - ESP-BLE-AUDIO
  - ESP-GMF
  key_people: []
key_logic_flow:
- ESP32-S31 是一款双核 32 位 RISC-V SoC，主频 320 MHz，具备 60 个 GPIO 和 128 位 SIMD 数据通路。
- 该芯片同时支持 2.4 GHz Wi-Fi 6、蓝牙 5.4 LE Audio、Thread/Zigbee 和千兆以太网 MAC，覆盖无线与有线连接。
- 芯片提供 DVP 摄像头接口和最高 24 位并行 RGB LCD 支持，内置 JPEG 编解码器、PPA 和 2D-DMA 硬件加速器。
- 安全方面集成了 TRNG、RAM 基 PUF、安全启动、闪存与 PSRAM 加密、TEE 和 APM 隔离机制。
- ESP32-S31 将通过 ESP-IDF、ESP-Matter、ESP-BLE-AUDIO 和 ESP-GMF 等开源框架获得软件生态支持。
- 该 SoC 可配合 ESP Private Agents 平台或直接与 LLM 交互，用于构建 AI 语音和智能交互设备。
extract_result: success
object_mentions:
- object_type: product
  name: ESP32-S31
  canonical_name: ESP32-S31
  url: https://www.espressif.com/en/products/socs/esp32-s31
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - ESP32-S31 是乐鑫科技发布的双核 RISC-V SoC，集成 Wi-Fi 6、蓝牙 5.4 LE Audio 和千兆以太网 MAC。
  - 该芯片提供 60 个 GPIO、DVP 摄像头接口和最高 24 位并行 RGB LCD 支持。
  - ESP32-S31 可配合 LLM 构建 AI 语音与智能交互设备。
  article_id: f9dacd28a2b408bd
- object_type: project
  name: ESP-IDF
  canonical_name: ESP-IDF
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - ESP32-S31 将通过乐鑫的开源 IoT 开发框架 ESP-IDF 获得软件支持。
  article_id: f9dacd28a2b408bd
- object_type: project
  name: ESP-Matter
  canonical_name: ESP-Matter
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - ESP32-S31 将通过 ESP-Matter 框架支持 Matter 协议设备开发。
  article_id: f9dacd28a2b408bd
- object_type: project
  name: ESP-BLE-AUDIO
  canonical_name: ESP-BLE-AUDIO
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - ESP32-S31 将通过 ESP-BLE-AUDIO 框架获得蓝牙音频应用支持。
  article_id: f9dacd28a2b408bd
- object_type: project
  name: ESP-GMF
  canonical_name: ESP-GMF
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - ESP32-S31 将通过 ESP-GMF 框架获得多媒体应用支持。
  article_id: f9dacd28a2b408bd
- object_type: product
  name: ESP Private Agents
  canonical_name: ESP Private Agents
  url: null
  confidence: low
  article_role: ecosystem_context
  evidence_snippets:
  - ESP32-S31 可与 ESP Private Agents 平台配合使用构建 AI 客户端设备。
  article_id: f9dacd28a2b408bd
---

### Comprehensive Connectivity

ESP32-S31 integrates both
**wireless and wired** connectivity for
versatile networking. It supports 2.4 GHz Wi-Fi 6 (802.11ax)
for
**enhanced transmission efficiency and reduced power
consumption**, making it ideal for battery-powered and always-connected
devices. IEEE 802.15.4 enables Thread and Zigbee protocols,
and Bluetooth® 5.4 (LE) supports LE Audio for
high-quality, low-power audio streaming, Direction Finding,
and Bluetooth Mesh 1.1 for scalable many-to-many device
communication. While Bluetooth Classic (BR/EDR) ensures
compatibility with legacy audio devices and low-latency HMI
applications. Also, the 1000 Mbps Ethernet MAC provides
stable, high-bandwidth wired connectivity for IoT
applications.

### System and Memory

ESP32-S31 is a
**dual-core 32-bit RISC-V** microcontroller
running at **320 MHz** with MMU support
providing 6.86 CoreMark/MHz processing performance and
**60 GPIOs** for design flexibility. One core
features a wide 128-bit data path with SIMD instructions,
enabling fast parallel processing. The SoC provides 512 KB
SRAM and 250 MHz 8-bit DDR PSRAM connectivity with
simultaneous flash and PSRAM access. Multiple dedicated SPI
interfaces, compatible with high-speed Octal SPI mode,
enable flexible external memory expansion.

### Advanced HMI Support

ESP32-S31 provides comprehensive human-machine interface
capabilities for rich multimedia applications. It features a
DVP camera interface (8 to 16-bit) and versatile LCD support
(8 to 24-bit parallel RGB, I8080, MOTO6800), supporting
conversion between RGB565, YUV422, YUV420, and YUV411.
Dedicated hardware accelerators including JPEG codec, PPA,
and 2D-DMA enable
**efficient image processing and display updates**. Combined with up to 14 capacitive touch sensing channels,
the ESP32-S31 is ideal for
**smart displays, video doorbells, multimedia
panels**, and applications requiring
**seamless touch, visual, and audio integration**.

### Flexible Audio Integration

The ESP32-S31 delivers versatile audio capabilities across
wireless and wired interfaces. Bluetooth 5.4 LE Audio
enables high-quality, low-power streaming with
**LC3 codec and multi-stream audio**, while
Bluetooth Classic (BR/EDR) ensures compatibility with
headphones, speakers, and automotive systems. Dual I2S
controllers with hardware-level Bluetooth audio
synchronization provide precise timing and minimal latency,
eliminating software-based synchronization complexity.

### Security

ESP32-S31 provides robust hardware-based security for
applications with stringent industry requirements. A
standout highlight is the integration of TRNG and RAM-based
PUF capabilities, providing a strong foundation for key
generation and device security. It also supports secure
boot, flash and PSRAM encryption, and cryptographic
accelerators including AES-128/256, RSA, ECDSA, and ECC. In
addition, an ECDSA-based digital signature peripheral
protects private keys from software access, while
**TEE** and APM enable software isolation for
secure multi-application deployment.

### Software Availability

ESP32-S31 will be supported through Espressif's open-source IoT Development Framework ESP-IDF、ESP-Matter (for Matter devices), ESP-BLE-AUDIO and ESP-GMF (for multimedia applications). ESP32-S31 will also work with the ESP Private Agents platform as well as directly with common LLMs to build client devices that run or interact with AI agents to create voice-enabled and intelligent applications.