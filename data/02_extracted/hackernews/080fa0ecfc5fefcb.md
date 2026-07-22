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
tldr: Optocam Zero 是一个基于 Raspberry Pi Zero 的开源数字相机项目，全部使用市售组件和 3D 打印外壳，支持自动对焦、8 种滤镜和
  GIF 录制，已在 GitHub 上公开所有硬件文件和软件安装指南。
objective_summary: 开发者 dorukkumkumoglu 在 GitHub 上发布了 Optocam Zero 项目，这是一款基于 Raspberry
  Pi Zero 的紧凑型数码相机。该相机使用市售组件组装，外壳完全 3D 打印，具备 2592×2592 像素 JPEG 拍照、自动对焦、8 种滤镜、GIF 录制等功能，并通过自定义热点界面实现快速图像传输。项目仓库包含完整的物料清单、逐步组装指南、3D
  打印文件和软件安装程序。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Raspberry Pi
  technologies: []
  key_people:
  - dorukkumkumoglu
key_logic_flow:
- Optocam Zero 是一款基于 Raspberry Pi Zero 的紧凑型数码相机，全部使用市售组件和 3D 打印外壳制造。
- 相机具备 2592×2592 像素 JPEG 拍摄、自动对焦摄像头模块、8 种照片滤镜和 GIF 录制功能。
- 电池续航约 70-80 分钟，采用 14500 型锂电池并通过 USB-C 充电，设备可在充电时使用。
- 图像通过自定义热点界面实现快速传输，已针对移动端和桌面端进行优化。
- 项目仓库公开了完整的 3D 打印文件、物料清单、详细组装指南和软件安装程序，方便他人自行构建。
- 相机尺寸为 51×71×18mm，配备 1.4 英寸 240×240 像素 LCD 显示屏，启动时间约 22 秒。
extract_result: success
object_mentions:
- object_type: project
  name: dorukkumkumoglu/optocamzero
  canonical_name: optocamzero
  url: https://github.com/dorukkumkumoglu/optocamzero
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Optocam Zero 是一个基于 Raspberry Pi Zero 的紧凑型数码相机项目，全部使用市售组件和 3D 打印外壳制造。
  - 项目仓库包含完整的硬件文件、物料清单、详细逐步组装指南和软件安装程序，供他人自行构建。
  - 相机具备自动对焦模块、8 种滤镜、GIF 录制功能和自定义热点图像传输界面。
  article_id: 080fa0ecfc5fefcb
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