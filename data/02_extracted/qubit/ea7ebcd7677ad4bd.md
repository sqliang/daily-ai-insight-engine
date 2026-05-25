---
title: 腾讯混元开源全新翻译模型Hy-MT2 ，上线小程序「腾讯Hy翻译」
source: https://www.qbitai.com/2026/05/422068.html
author:
- '[[闻乐]]'
published: '2026-05-21'
created: '2026-05-22'
description: 最大提升体现在指令遵循能力上
tags:
- clippings
extraction_status: success
id: ea7ebcd7677ad4bd
source_type: news_media
tldr: 腾讯混元开源Hy-MT2翻译模型系列，支持33种语言互译，并上线「腾讯Hy翻译」小程序。
objective_summary: 2026年5月21日，腾讯混元宣布开源Hy-MT2多语言翻译模型系列（1.8B/7B/30B-A3B三个尺寸），同时上线「腾讯Hy翻译」微信小程序。Hy-MT2在FLORES-200评测中接近Gemini
  3.1 Pro水平，最大提升体现在指令遵循能力。1.8B模型通过AngelSlim 1.
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Tencent
  - Google
  - Microsoft
  - ARM
  - Qualcomm
  - Intel
  - 沐曦
  - 天数智芯
  technologies:
  - Hy-MT2
  - AngelSlim
  - FLORES-200
  - IFMT Bench
  - Sherry
  - MoE
  - 1.25-bit量化
  - 4-bit量化
  - 8-bit量化
  - FP16
  - WMT26
  key_people: []
key_logic_flow:
- 2026年5月21日，腾讯混元正式开源Hy-MT2翻译模型系列，包含1.8B（端侧轻量）、7B（均衡实力）和30B-A3B（专业效果）三个尺寸，支持33种语言互译。
- Hy-MT2在FLORES-200通用翻译评测中接近Gemini 3.1 Pro水平，7B和30B-A3B在开源模型中达到最佳效果，1.8B轻量模型超越微软等主流商业翻译API。
- 相比上一代Hy-MT1.5，Hy-MT2的最大提升在于指令遵循能力，能更准确理解用户对术语、风格和输出格式的具体要求，IFMT Bench测试集已同步开源。
- Hy-MT2采用混元自研AngelSlim极端量化方案，提供1.25-bit、2-bit、4-bit、8-bit和FP16版本，1.8B模型仅需440MB存储空间，基于Sherry框架在苹果A15上推理速度提升1.5倍。
- 「腾讯Hy翻译」微信小程序同步上线，支持语音输入、自定义翻译风格和指令，可通过提前下载端侧模型实现离线翻译。
- Hy-MT2已在GitHub、HuggingFace、ModelScope和腾讯云等平台开源，ARM、高通、Intel、沐曦、天数智芯等多个硬件平台支持部署，腾讯混元同时与WMT26合作举办翻译赛事。
pipeline_stage: fact_extracted
---

# 腾讯混元开源全新翻译模型Hy-MT2 ，上线小程序「腾讯Hy翻译」

最大提升体现在指令遵循能力上


5月21日，腾讯混元宣布开源全新翻译模型Hy-MT2并上线翻译小程序「腾讯Hy翻译」。Hy-MT2 是支持 33 种语言互译的多语言模型，其中7B 和 30B-A3B模型在各类翻译任务上达到了开源模型最佳效果，超越了几十倍参数量的模型，轻量级的 1.8B 模型也超越了微软等主流商业 API，且得益于 AngelSlim 1.25-bit 极端量化，仅需 440MB 存储空间，可以轻松部署在主流手机芯片上支持本地推理，相比Hy-MT1.5推理速度提升 1.5 倍。


Hy-MT2 包含 3个尺寸的模型 Hy-MT2-1.8B、Hy-MT2-7B、Hy-MT2-30B-A3B，分别侧重端侧轻量部署、均衡实力以及专业效果。

「腾讯Hy翻译」小程序基于 Hy-MT2 打造，相比其他翻译工具，不仅支持语音输入，还优化了自定义翻译风格和指令的能力，让翻译结果更符合预期，实用性更强。同时，用户不仅可以在联网环境下体验高速版的混元翻译模型，也可以通过提前下载端侧翻译模型，在无网络或者弱网络场景中使用离线翻译，解决了部分应用场景中网络条件受限的问题。

在通用翻译能力评测中，Hy-MT2系列三个模型在 FLORES-200 平均表现上已经非常接近目前行业表现最好的翻译模型 （Gemini 3.1 Pro ）。同时，Hy-MT2-7B 和 Hy-MT2-30B-A3B 的实测得分已经超过国内主要的通用大模型，在轻量级模型的横向对比中，Hy-MT2-1.8B 也整体优于头部商业翻译 API。

保持通用翻译能力的同时，Hy-MT2 进一步面向真实业务场景和专业领域翻译进行优化。

在真实场景测试集上，Hy-MT2-30B-A3B 效果已经超过 Gemini 3.1 Pro，特别在垂直领域的测试集中，Hy-MT2-30B-A3B在金融、政治、教育几个领域的翻译效果已经部分超过主流翻译模型。


相比上一版本模型，Hy-MT2的最大提升体现在指令遵循能力上，模型能够更准确地理解并执行用户关于术语、风格和输出格式等方面的具体要求。腾讯混元自建数据集 IFMT Bench 测试结果表明，Hy-MT2-7B 和 Hy-MT2-30B-A3B的翻译效果已经超越等相近尺寸开源模型，接近 Gemini 3.1 Pro。目前这一测试集也已经开源。


指令遵循能力见下面的例子，通过“个性化设定：翻译结果简洁精炼，去掉冗余表达，每句不超过15个字”，模型可以很好的遵循指令，让翻译结果更符合要求。

本次升级的 Hy-MT2 模型进一步探索极低比特量化方案，除 4-bit、8-bit 和 FP16 版本外，Hy-MT2 还基于混元自研技术提供了 1.25-bit 和 2-bit 版本，以适配不同硬件环境下的部署需求。基于混元自研 Sherry 框架实现的 1.25-bit 极低比特量化版本在苹果 A15 上的推理速度相比 Hy-MT1.5 的 4-bit 量化版本提升了 1.5 倍，进一步提升了实际可用性。


为了便于开发者使用，Hy-MT2 开源的模型已经在 Github 和 Huggingface 等开源社区上线，ARM、高通、Intel、沐曦、天数智芯等多个平台均支持部署。


总体看来，Hy-MT2 是一个面向真实应用场景的高质量、高效率、多能力多语翻译模型家族，在通用翻译、专业领域翻译、真实业务场景和翻译指令遵循任务上均表现出较强竞争力。


腾讯混元翻译模型坚持从社区和实际应用场景中搜集真实反馈，不断提升模型能力。同时，腾讯混元也希望通过开源和社区活动回馈社区，现在，腾讯混元也在与WMT26官方合作「视频字幕翻译比赛」（https://www2.statmt.org/wmt26/video-subtitle-translation.html），使用Hy-MT系列模型参与「通用机器翻译比赛」（https://www2.statmt.org/wmt26/translation-task.html）和「视频字幕翻译比赛」有机会获得混元特设奖励，诚邀邀大家参与，共同推动机器翻译前沿技术发展。


开源和体验链接，可访问：


l HuggingFace：https://huggingface.co/collections/tencent/hy-mt2

l Modelscope：https://modelscope.cn/collections/Tencent-Hunyuan/Hy-MT2

l Github：https://github.com/Tencent-Hunyuan/Hy-MT2

l 腾讯云：https://console.cloud.tencent.com/tokenhub/text

l 腾讯混元官网：https://aistudio.tencent.com/llm/zh?tabIndex=0

*版权所有，未经授权不得以任何形式转载及使用，违者必究。*

- 菲尔兹奖得主都看懵了：OpenAI非数学模型首次自主突破80年未解数学难题
*2026-05-21* - 虾马之后又火一个！OpenHuman用20分钟了解你的一切，存成卡帕西式知识库
*2026-05-16* - Need is all you need：AI接手Coding后，程序员最值钱的能力只剩这一项?
*2026-05-15* - 别让模型烧Token了！GitHub 20k星神作：把全网变成命令行
*2026-05-16*