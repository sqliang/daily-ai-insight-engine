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
tldr: 乐鑫科技发布ESP32-S31芯片，集成Wi-Fi 6、蓝牙5.4、Thread/Zigbee和千兆以太网，搭载双核RISC-V处理器
objective_summary: 乐鑫科技推出ESP32-S31系统级芯片，集成2.4GHz Wi-Fi 6(802.11ax)、IEEE 802.15.4(Thread/Zigbee)、蓝牙5.4
  LE和1000Mbps以太网MAC，搭载双核32位RISC-V处理器(320MHz/6.
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - Espressif
  technologies:
  - Wi-Fi 6
  - 802.11ax
  - IEEE 802.15.4
  - Thread
  - Zigbee
  - Bluetooth 5.4
  - LE Audio
  - Bluetooth Mesh 1.1
  - RISC-V
  - SIMD
  - DDR PSRAM
  - TEE
  - TRNG
  - PUF
  - ESP-IDF
  - ESP-Matter
  - Matter
  - LC3
  - JPEG
  - PPA
  - 2D-DMA
  key_people: []
key_logic_flow:
- ESP32-S31同时集成2.4GHz Wi-Fi 6(802.11ax)、IEEE 802.15.4(Thread/Zigbee)、蓝牙5.4 LE(含LE
  Audio和Bluetooth Mesh 1.1)以及1000Mbps以太网MAC，兼顾无线与有线连接。
- 搭载双核32位RISC-V处理器，主频320MHz，其中一个核心具有128位SIMD数据通路，提供6.86 CoreMark/MHz性能，配备512KB SRAM并支持250MHz
  8位DDR PSRAM。
- 提供DVP摄像头接口(8-16位)和多种LCD显示接口(8-24位并行RGB/I8080/MOTO6800)，内置JPEG编解码器、PPA和2D-DMA硬件加速器，支持多达14路电容触摸传感。
- 集成TRNG和基于RAM的PUF硬件安全能力，支持安全启动、闪存和PSRAM加密、AES/RSA/ECDSA密码加速器，并通过TEE和APM实现软件隔离。
- 软件方面支持ESP-IDF、ESP-Matter、ESP-BLE-AUDIO和ESP-GMF等开源框架，可配合ESP Private Agents平台或直接对接常用LLM构建支持语音交互的AI终端设备。
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