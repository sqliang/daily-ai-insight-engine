---
title: 'Optocam Zero: a Pi Zero based digital camera made using off the shelf components'
source: https://github.com/dorukkumkumoglu/optocamzero
author:
- '[[iamnothere]]'
published: '2026-06-22'
created: '2026-06-24'
description: 'Article URL: https://github.com/dorukkumkumoglu/optocamzero Comments
  URL: https://news.ycombinator.com/item?id=48634778 Points: 176 # Comments: 47'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 080fa0ecfc5fefcb
source_type: community_discussion
tldr: 基于树莓派Zero的开源DIY数码相机项目，可自行3D打印组装
objective_summary: Doruk Kumkumoglu 在 GitHub 发布了 Optocam Zero 项目，一款基于 Raspberry Pi
  Zero 的紧凑型数码相机，使用现成组件和3D打印外壳构建。支持 2592×2592 像素拍摄、8种滤镜、GIF录制、Wi-Fi传输、USB-C充电，续航约70-80分钟。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Raspberry Pi Foundation
  - Kodak
  technologies:
  - Raspberry Pi Zero
  - 3D printing
  - USB-C
  key_people:
  - Doruk Kumkumoglu
key_logic_flow:
- Optocam Zero 是一款基于 Raspberry Pi Zero 的紧凑型开源数码相机，全部设计文件和软件代码托管在 GitHub。
- 相机使用现成的电子组件和完全3D打印的外壳（除紧固件外），降低了DIY门槛。
- 核心规格：2592×2592像素JPEG拍摄、1.4英寸240×240 LCD屏幕、15-20fps实时预览、22秒启动时间。
- 功能特性包括：8种照片滤镜、GIF录制播放、自定义热点传输界面、屏幕自动调光省电、USB-C充电（可边用边充）、可更换14500锂电池（续航70-80分钟）。
- 项目仓库包含完整物料清单(BOM)、分步组装指南(PDF)、3D打印文件(STL/Bambu Studio项目)和相机软件安装程序。
- 设计灵感来源于 Kodak 等玩具相机，强调便携（51×71×18mm）、趣味性和直觉化操作。
extract_result: success
---

Optocam Zero is a Raspberry Pi Zero based compact digital camera made using off the shelf components.

I designed Optocam Zero to have a very compact, carry everywhere and have fun sort of camera. As I was inspired by Kodak charmera and similar toy cameras, I wanted it to be feel playful, enjoyable and be intuitive to use. I also aimed to make it relatively easy to build so that others can also build one and have fun with it. That's why all the case parts are easily printable and for the electronics it uses off the shelf components that are easy to find.

- Very compact and easy to carry in your pocket.
- Intuitive and simple camera interface and controls.
- Uses autofocus camera module.
- 8 photo filters included.
- Easy and fast image transfer through custom hotspot interface. Optimized both for mobile and desktop.
- Screen dimming when inactive to preserve battery.
- USB-C charging. Device can be used while charging.
- Interchangable battery.
- Off the shelf/ common components for the electronics.
- Fully 3D printed case parts (apart from fasteners).
- 3D printable TPU protective sleeve and lanyard design is available.
**NEW**- GIF recording and playback.

- 2592x2592px Jpeg image capture. Image saves in the background while preview stays active.
- 240x240px 1.4 inch lcd display.
- Consistent 15–20 fps camera preview on the screen.
- 22 seconds boot time.
- Uses 14500 type li-ion battery.
- 70–80 minutes of use per charge.
- Dimensions: 51×71×18mm (excluding camera and screen bump)

Everything you need to build an Optocam Zero yourself is included in this repo.

All the 3d print files, Required parts list, and detailed step by step build guide can be found under the hardware folder.

If you're considering building one, check the BOM to get an idea of the cost for required tools and parts. Also, have a look at the build guide, it will give you a clear idea of what the build involves.

See the hardware folder for:

- Bill of materials.
- Build guide (PDF).
- Bambu Studio project files ready to print for transparent PETG or PETG / PETG-CF.
- Individual .stls for camera parts.
- CAD file for customization.

See the software folder for:

- Optocam Zero camera software installer and installation guide.
- Camera controls information.