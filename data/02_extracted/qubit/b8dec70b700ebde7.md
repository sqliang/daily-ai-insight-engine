---
title: 写2000字提示词，不如先生成3D白模！AI视频创作进入“预演时代”
source: https://www.qbitai.com/2026/08/475476.html
author:
- '[[梦晨]]'
published: '2026-08-19'
created: '2026-08-19'
manifest_dates:
- '2026-08-19'
description: AI终于能听严格执行运镜需求
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: b8dec70b700ebde7
source_type: news_media
tldr: 量子位实测updream新上线的预演台（Previs Studio）：创作者上传场景参考图生成3D白模，排好人物走位与机位并录制预演视频，再交给Seedance、Kling等视频模型渲染，以白模空间约束解决AI视频镜头不可控的问题。
objective_summary: 2026年8月，量子位记者衡宇体验updream新上线的预演台（Previs Studio）功能并发布实测文章。该功能将影视行业成熟的Previs预演工作流搬进创作画布：先上传1-3张场景参考图生成3D白模（官方称约4-7分钟），再搭建人物与机位、绘制走位轨道并录制预演视频，最后交给Seedance、Kling、Wan、Gemini
  Veo等视频模型完成渲染。预演台定义粗粒度与细粒度两套白模用法，分别管理动作走位等动态时序信息与材质替换等风格重渲染。实测加入白模参考后，一镜到底镜头的人物运动方向、摄影机路径和停留位置均得到固定，减少了生成抽卡。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - updream
  - 量子位
  technologies:
  - Previs
  - Blockout
  - 3D白模
  - ControlNet
  - Stable Diffusion
  - Seedance
  - Kling
  - Wan
  - Gemini Veo
  - Blender
  - Maya
  - ComfyUI
  key_people:
  - 衡宇
key_logic_flow:
- AI视频生成的核心短板在于3D空间与镜头调度的可控性，症结是信息传递损耗：画面从创作者脑海转译为提示词、再经AI二次解析，两次翻译丢失大量关键信息，导致只能反复重试抽卡。
- 影视行业验证过的破局思路是白模预演：粗糙的3D白模充当视频生成的空间锚点，承载深度、遮挡、比例与可运动空间等纯粹空间时序信息，材质光影交由模型自由发挥。
- updream新上线预演台（Previs Studio）功能，把影视行业成熟的Previs预演工作流搬进创作画布，先搭白模场景、定机位、排走位、录预演视频，再交给Seedance、Kling、Wan、Gemini
  Veo等视频模型完成最终渲染。
- updream定义了粗粒度与细粒度两套白模用法：粗粒度管动作、动线、站位、运镜、切镜、光影节奏等动态时序信息，细粒度结构完整，用于材质替换、色彩调整与风格重渲染。
- 实际操作共四步：在创作画布新建预演台、上传1-3张场景参考图生成场景白模（官方称耗时约4-7分钟）、新建人物与机位并绘制走位轨道、录制白模视频导出至下游节点。
- 实测一镜到底场景时，加入白模参考后人物运动方向、摄影机移动路径与最终停留位置得到固定，相比无白模参考更接近预设运镜节奏，说明白模降低了复杂镜头的抽卡成本。
object_mentions:
- object_type: product
  name: updream 预演台 (Previs Studio)
  canonical_name: updream Previs Studio
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - updream新上线的功能预演台（Previs Studio）把影视行业成熟的Previs预演工作流搬进了创作画布。
  - 创作者先搭建3D白模场景，定好机位，排完人物走位，录制预演视频，再交给Seedance、Kling、Wan、Gemini Veo等视频模型完成最终渲染。
  - 实测操作只需四步：新建预演台、上传1-3张场景参考图生成场景白模、新建人物与机位并绘制走位轨道、录制白模视频导出至下游节点。
  article_id: b8dec70b700ebde7
- object_type: product
  name: updream
  canonical_name: updream
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 在学妹指导下，作者体验了updream新上线的预演台功能，上传户外婚礼场景参考图后，白模生成用时不足5分钟。
  - updream借助AI能力降低了建模门槛，但它不是傻瓜式一键出片工具，创作者仍需理解场景层级、机位与运动轨迹的关联。
  article_id: b8dec70b700ebde7
- object_type: project
  name: ControlNet
  canonical_name: ControlNet
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 早在Stable Diffusion时代，ControlNet就已经给出过解法，人们在生成图片前输入深度图、法线贴图或简易3D模型等空间信息来约束画面。
  article_id: b8dec70b700ebde7
- object_type: product
  name: Blender
  canonical_name: Blender
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Blender作为免费开源全能3D创作套件，从零上手动辄需要数月甚至更久，对追求效率的AI创作者而言难以承受这样的时间成本。
  article_id: b8dec70b700ebde7
- object_type: product
  name: Maya
  canonical_name: Autodesk Maya
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Maya作为商用影视级3D动画软件，与Blender一样从零上手通常需要数月甚至更久，传统3D工具的学习成本极高。
  article_id: b8dec70b700ebde7
- object_type: project
  name: ComfyUI
  canonical_name: ComfyUI
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 过去要达到白模效果，要么自己啃几个月Blender，要么去ComfyUI里搭一套复杂的节点工作流。
  article_id: b8dec70b700ebde7
- object_type: model
  name: Seedance
  canonical_name: Seedance
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 创作者录制完白模预演视频后，可将其作为参考素材交给Seedance、Kling、Wan、Gemini Veo等视频模型完成最终渲染。
  article_id: b8dec70b700ebde7
- object_type: model
  name: Kling
  canonical_name: Kling
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 创作者录制完白模预演视频后，可将其作为参考素材交给Seedance、Kling、Wan、Gemini Veo等视频模型完成最终渲染。
  article_id: b8dec70b700ebde7
- object_type: model
  name: Wan
  canonical_name: Wan
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 创作者录制完白模预演视频后，可将其作为参考素材交给Seedance、Kling、Wan、Gemini Veo等视频模型完成最终渲染。
  article_id: b8dec70b700ebde7
- object_type: model
  name: Gemini Veo
  canonical_name: Gemini Veo
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 创作者录制完白模预演视频后，可将其作为参考素材交给Seedance、Kling、Wan、Gemini Veo等视频模型完成最终渲染。
  article_id: b8dec70b700ebde7
extract_result: success
---

# 写2000字提示词，不如先生成3D白模！AI视频创作进入“预演时代”

AI终于能听严格执行运镜需求

衡宇 发自 凹非寺


量子位 | 公众号 QbitAI

不是我说，随着模型能力越来越强，现在各大平台上优秀的AI视频早就超过普通人玩AI的范畴了。

更多是有编导思维的**科班/专业人士利用AI下放的门槛，把自己的专业能力放大，在这些赛道一通乱杀。**

为了验证这种差距，我也用最近大火的视频模型生成了一段镜头：

身着传统武士铠甲的武士，缓步穿行于古日本木质村落街道，居于画面中心，步履沉稳。街道两旁村民或立或跪垂首行礼，氛围肃穆，地面微湿。镜头缓缓推进，整体充满历史电影的真实质感。


得到如下画面（且prompt被AI帮我润色补全过）：

模型能力本身是没问题的！

然而我科班出身、还在影视行业当牛马的学妹看了过后冷笑一声，说我**第一不懂编导思维不懂镜头衔接，第二不懂AI视频生成。**

听到无情嘲讽我即将小发雷霆，她给我看了同一个模型出来的成片，我一下就阿巴阿巴了。

这家伙脑中已经具备完整的分镜和调度逻辑，但，她说差异如此巨大，主要门外人都不知道影视行业一贯用到的白模（Blockout/Previs预演白模）。

也就是上面这个视频中上半屏的东东。

她喜不自胜给我嘚吧嘚：“**本来白模是要学建模的，现在不用费劲巴拉学了！**现在有了AI新工具，就传个场景参考图，AI很快就搞出来高还原度的3D白模场景了。”

对普通人来说，还是有上手难度，但对专业人士来说真的可以事！半！功！倍！

在她的指导下，我狠狠体验了一把**updream新上线的功能，预演台**（Previs Studio）。

它把影视行业成熟的Previs预演工作流搬进了创作画布：

创作者先搭建3D白模场景，定好机位，排完人物走位，录制预演视频，再交给Seedance、Kling、Wan、Gemini Veo等视频模型完成最终渲染。

先设计镜头，再做生成，以此解决用AI视频模型“拍什么”和“怎么拍”的控制问题。

妙啊！

# 别急着生成！先用AI给复杂镜头做白模预演

创作者怎么准确告诉模型“我要怎么拍”，依然缺少一种更贴近影视工业的方法，这显然是当下AI视频创作进入下一阶段后，需要面对的新问题。

AI视频的短板在3D空间与镜头调度的可控性——**很多人把生成翻车归罪于提示词写得不够完善，但症结其实在于信息传递损耗。**

文字能写下“镜头向前缓缓推进”“人物从画面左侧横穿”，却无法严格规定生成时的具体推进速度、人物与环境距离，以及运动收尾的构图。

创作者脑海中的画面先要转译为提示词，再交由AI二次解析，两次翻译会丢失大量关键信息。

生成前，我们无从判断模型接收了哪些指令，也无从得知到底会生成什么画面。

能咋办？只能一遍遍重试抽卡。

而**白模参考是文娱影视业内验证过的破局思路。**

白模承担的是纯粹的空间与时序信息。

粗糙的3D白模充当视频生成的空间锚点，模型能精准理解分镜中的深度、遮挡、比例和可运动空间，这些概念很难单纯通过提示词描述清楚。

**早在Stable Diffusion时代，ControlNet就已经给出过解法。**

当时为解决画面失控，人们会在生成图片前输入深度图、法线贴图或简易3D模型等空间信息，哪怕只是火柴人，也能稳定约束人物姿态与透视关系。

这一思路随后也被**迁移到视频生成领域。**

白模只输出空间约束，材质、光影交由模型自由发挥，但空间结构不允许漂移错乱。

即便没有色彩纹理，它也能指引模型组织画面，大幅降低人物走位、场景透视崩坏的概率。

可建模技能向来门槛颇高，**传统3D工具学习成本极高，Blender**（免费开源全能3D创作套件）**、Maya**（商用影视级3D动画软件）**从零上手动辄数月甚至更久**，对于追求效率的AI创作者，难以承受这样的时间成本。

updream预演台，干的就是把这套原本需要建模经验和专业软件支撑的门槛打下来。

它把过去需要Blender或Maya才能做的事，狠狠用AI降低了门槛。

官方把白模控制定义为高级能力，专门出台了对应的提示词规范，区分粗粒度、细粒度两套白模用法。

两种白模分工如下：

**粗粒度白模**：管动作、动线、站位、运镜、切镜、光影节奏这些动态时序信息，不需要精致外观，只用几何体把“怎么动”讲清楚，人物外貌、场景材质交给别的参考图去定义。**细粒度白模**：本身结构完整，更多用来做材质替换、色彩调整、人物与场景风格重渲染。

超大字号提醒！

updream借助AI能力降低了建模门槛，但它不是个“傻瓜式”一键出片工具。

创作者要弄懂场景层级、机位、运动轨迹的关联，复杂叙事镜头依旧需要提前拆解分镜，最终才能产出专业级调度。

# updream预演台，究竟改变了多少？

好，虽然我刚才拉响了小白预警，但实际操作下来，这套流程的手感是很顺的（毕竟有学妹从旁指导）。

为了验证预演台的效果，我分别测试了几类AI视频中较难控制的镜头。

从步骤上来说，只需要总共四步。

**首先，打开updream，在创作画布内右键点击空白处，新建预演台。**

**第二步，点击“生成空间”或“创建场景”，然后上传1-3张场景参考图。**

上传参考图的目的是生成场景白模，人物需要搭建完场景之后添加。

体验的时候，我找了一张户外婚礼场景的图丢给预演台。

我发起任务是当天18:49分，白模生成出来是18:53分，**拢共也没用上5分钟。**

我的场景确实比较简单啦，但官方教程里面也表示这一环节耗时大约为4-7分钟。

生成的白模拖动移动、放大缩小都可以，360度旋转或导航也没问题。

过去要达到下图这个效果，要么自己老老实实啃几个月Blender，要么去ComfyUI里搭一套复杂的节点工作流。

白模生成好后，可以新建人物、机位等。

这里，人物运动片段还能选择全局动作和局部动作。

有了你满意的场景、人物、机位，绘制人物走位和轨道过后，点击右上角录制，即可将白模视频导出至画布的下游节点。

导出前，我恨不得架它八个机位……

接下来就已经可以剪辑录下来的白模预演视频，把它作为参考素材，送到updream的其他功能的视频模型里去生成。

为了验证它到底能不能减少抽卡，学妹指导我实测了三个最容易乱成一锅粥的复杂场景。

**第一个，一镜到底。**

输入了个极简风prompt：

户外婚礼现场，一个穿着旗袍的女性走到座位区的倒数第三排落座。


一镜到底很考验连续运动过程中，空间、人和环境的关系对照关系和变化。

如果只用图片和参考图，不用白模，旗袍妹子走着走着户外草坪的背景就容易突然变异。

加入白模参考后，我们规定了旗袍妹子的前进路线：

可以看到，人物运动方向、摄影机移动路径以及最终停留位置都得到了很好的固定：

相比没有白模参考的生成结果，这次输出更接近我们脑子里预设的运镜节奏。

**第二个，多机位切换。**

核心考验AI能不能理解同一个空间里，不同镜头之间的连续关系。

AI很容易把每个镜头理解成新的生成任务。

于是可能出现：