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
pipeline_stage: ingested
id: f9dacd28a2b408bd
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