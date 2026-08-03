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
impact_score:
  score: 6.5
  reason: ESP32-S31 是乐鑫在 IoT MCU 领域的重要产品升级，首次在 S 系列中集成 Wi-Fi 6、Thread/Zigbee、蓝牙 5.4
    LE Audio 和千兆以太网 MAC 于单颗 RISC-V 芯片中。这对智能家居、Matter 生态和 AIoT 终端设备市场有显著的竞争格局影响——竞争对手（如瑞昱、联发科、Silicon
    Labs）需要在中低端市场做出回应。但并非范式转移级别的冲击，因为 ESP32 系列本就处于市场主导地位，此次升级更多是连接能力密度的提升而非架构革命。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: RISC-V 双核架构 + Wi-Fi 6 + Thread/Zigbee + 千兆以太网的全集成方案，以及 ESP-IDF 生态对
    Matter 和 AI 终端设备的支持能力
hype_assessment:
  level: low
  reason: 乐鑫的发布内容以详细技术规格为主——给出了明确的主频（320MHz）、性能基准（6.86 CoreMark/MHz）、接口位数（DVP 8-16bit、LCD
    8-24bit）、安全方案（TEE、PUF、TRNG）等可验证指标，没有使用'颠覆''革命'等 PR 话术，信息客观且可溯源。
information_entropy: high
domain_disruption:
  technical_innovation: 将 Wi-Fi 6（802.11ax）、IEEE 802.15.4（Thread/Zigbee）、蓝牙 5.4 LE
    Audio 和千兆以太网 MAC 集成到单颗低成本 RISC-V MCU 中，同时提供 TEE 硬件隔离和 RAM 基 PUF 安全方案，在 IoT 边缘侧实现了前所未有的连接密度和安全基线。128
    位 SIMD 数据通路和 2D-DMA/JPEG/PPA 硬件加速器使该芯片有能力承载实时图像处理和语音交互工作负载。
  business_model: 强化了乐鑫在 Matter 智能家居标准和 AIoT 终端设备领域的平台化地位。单芯片全栈方案（Wi-Fi + Thread +
    BLE + 以太网 + 音视频接口）可降低 OEM 的 BOM 成本和集成复杂度，推动智能家居设备从多芯片分立方案向单 SoC 方案演进。配合 ESP Private
    Agents 平台和 LLM 对接能力，为低成本 AI 终端（智能面板、可视门铃、语音助手）开辟了新的市场空间。
engineering_complexity: production_ready
compound_value:
  score: 8.0
  reason: ESP32-S31 延续了乐鑫 ESP32 系列的平台化复利策略，每一代新芯片都向后兼容 ESP-IDF 开源生态，开发者迁移成本极低。增量价值体现在三方面：一是
    Wi-Fi 6 + Thread/Zigbee/Matter 三模无线加千兆以太网，变成 IoT 连接的全能平台；二是双核 RISC-V + 128-bit
    SIMD + 摄像头/显示接口 + JPEG 硬件加速，使其能承载边缘 AI 推理和多媒体交互负载；三是硬件级 TEE/PUF/TRNG 安全能力，打开工业和商业场景。当前
    Matter 协议正加速智能家居互联标准化，边缘端小模型推理需求爆发，ESP32-S31 作为同时覆盖连接、计算、多媒体、安全的单芯片方案，定价大概率延续乐鑫的高性价比策略，有望在
    3-5 年内成为 AIoT 终端设备的默认选择之一。但芯片尚未量产交付，存在流片与市场教育的时间风险，因此未给满分。
value_capture_layer: hardware_compute
moat_impact: creates_new_moat
key_beneficiaries:
- Espressif
- RISC-V International
- Matter 协议生态厂商
- 智能家居 ODM/OEM 厂商
competitive_casualty:
- STMicroelectronics (STM32 系列传统 MCU 线)
- Microchip (缺乏无线集成的 PIC/AVR 系列)
- Realtek (IoT Wi-Fi MCU 产品线)
- 博通/Cypress (物联网 Wi-Fi + Bluetooth 芯片线)
market_opportunities:
- 智能家居厂商可基于ESP32-S31的Wi-Fi 6+Thread/Zigbee+以太网多模连接和Matter协议支持，开发新一代全屋智能中控面板和网关产品
- 利用芯片集成的摄像头接口、LCD显示引擎和蓝牙LE Audio，可打造面向视频门铃、智能音箱和带屏交互终端的低成本AI边缘设备
- 依托ESP Private Agents平台和LLM对接能力，开发者可构建支持本地语音交互的AI终端，抢占边缘AI推理消费级市场先机
risk_matrix:
  regulatory: 搭载摄像头、麦克风和AI能力的终端设备需满足各国数据隐私法规（GDPR、中国个人信息保护法等）；Wi-Fi 6和Matter认证流程可能延长产品上市周期
  technological: RISC-V软件生态（工具链、中间件、调试器）成熟度仍不及ARM架构，部分AI推理场景可能需要外部NPU或DSP辅助，无法完全在片内闭环
  competitive: AIoT边缘芯片赛道拥挤，NXP i.MX RT系列、STM32MP系列和联发科Filogic系列均有近似定位，乐鑫需依靠开发者社区生态和开源策略维持差异化
  ethical: 集成摄像头、触摸传感和语音采集能力的终端设备若安全机制（TEE/PUF）实施不完善，存在用户隐私数据泄露和未经授权监控的社会风险
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: strategic_invest
object_insights:
- object_type: product
  name: ESP32-S31
  canonical_name: ESP32-S31
  url: https://www.espressif.com/en/products/socs/esp32-s31
  positioning: ESP32-S31是乐鑫科技推出的双核RISC-V SoC，集成Wi-Fi 6、蓝牙5.4 LE Audio和千兆以太网，面向AI语音与智能交互设备市场。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 智能显示与多媒体终端厂商
  - AI语音交互设备开发者
  - 智能家居及物联网设备制造商
  product_signal: 集成Wi-Fi 6、蓝牙5.4 LE Audio、Thread/Zigbee和千兆以太网MAC，支持DVP摄像头与24位并行RGB
    LCD接口，配备JPEG编解码器、PPA和2D-DMA等硬件加速器。
  market_signal: 面向AI语音与智能交互设备市场，可配合LLM构建端侧AI应用，拓展了MCU在生成式AI时代的应用边界。
  differentiation: 在单一SoC上同时提供Wi-Fi 6、蓝牙5.4 LE Audio和千兆以太网三种连接方案，并配备TEE与PUF硬件安全能力，连接全面性在同类MCU中领先。
  watch_reason: ESP32-S31是乐鑫在AI端侧部署的关键产品，通过集成Wi-Fi 6和千兆以太网满足AI语音设备对高带宽低延迟连接的需求，配合ESP
    Private Agents平台可直接对接LLM，为智能家居和交互设备带来端侧AI推理能力，有望开辟MCU在智能语音终端领域的新市场空间。
  risk_notes:
  - 芯片量产时间和定价策略尚未公布，市场投放节奏存在不确定性。
  - 端侧AI SoC市场竞争激烈，面临高通、联发科等成熟方案在生态和算力上的竞争压力。
  score: 7.0
  article_ids:
  - f9dacd28a2b408bd
  evidence_snippets:
  - ESP32-S31 是乐鑫科技发布的双核 RISC-V SoC，集成 Wi-Fi 6、蓝牙 5.4 LE Audio 和千兆以太网 MAC。
  - 该芯片提供 60 个 GPIO、DVP 摄像头接口和最高 24 位并行 RGB LCD 支持。
  - ESP32-S31 可配合 LLM 构建 AI 语音与智能交互设备。
  - 该 SoC 可配合 ESP Private Agents 平台或直接与 LLM 交互，用于构建 AI 语音和智能交互设备。
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