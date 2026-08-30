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
impact_score:
  score: 6.0
  reason: 先看事件本质：这是AI视频创作工具的产品功能落地（updream预演台上线），并非模型层或全新理论的突破，不构成行业范式转移。但该功能精准击中了AI视频行业公认的核心短板——3D空间与镜头调度的不可控性，通过把影视工业成熟的Previs工作流AI化（参考图生成白模、免去Blender/Maya建模门槛），将ControlNet时代验证过的'空间锚点'思路延伸到了视频生成工作流层，且量子位实测验证了减少抽卡的效果。从竞争格局看，这一能力若被验证有效，很可能促使Seedance、Kling、可灵、Pika等头部视频平台跟进同类预演能力，属于会改变局部竞争态势的产品发布。综合评分为6分：高于一般产品更新（因为解决的是真痛点、有实测背书），但受限于updream非头部平台、思路为既有技术的工程化整合，短期冲击力不足以达到7分以上。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 能否真正减少复杂镜头的'抽卡'成本，获得镜头走位与3D空间的可控性
hype_assessment:
  level: medium
  reason: 识别PR话术：标题中'AI视频创作进入预演时代'是对单一功能上线的拔高包装，'预演时代'一词具有明显的概念放大成分。但判定依据同时要考虑实质：量子位做了实测（白模生成实际不到5分钟、一镜到底的运镜路径得到固定），并诚实指出了上手门槛（仍需理解场景层级、机位、运动轨迹），说明技术实质真实存在、非空壳炒作。综合看，功能本身是干货，但'时代'级别的表述属于包装，故判定为medium。
information_entropy: medium
domain_disruption:
  technical_innovation: 将影视工业Previs工作流AI化落地：上传1-3张场景参考图即可自动生成3D白模场景，免去Blender/Maya数月的建模学习成本；创新性地定义粗/细粒度两套白模抽象，把动作动线、运镜切镜等动态时序信息与材质替换、风格重渲染等静态信息解耦，实质是把ControlNet的空间锚定思路从图像生成扩展到视频生成的工作流层，用几何约束解决提示词两次翻译的信息损耗问题。
  business_model: 推动AI视频工具从'提示词抽卡'的消费级玩具向专业创作流水线演进：预演/调度类能力为面向科班创作者的高级功能打开付费空间，可能成为视频平台差异化竞争的新维度，并倒逼头部平台跟进同类工作流能力，重塑AI视频SaaS的价值分层。
engineering_complexity: production_ready
compound_value:
  score: 6.0
  reason: 预演（Previs）工作流直击AI视频生成最核心的可控性瓶颈——3D空间与镜头调度，且是影视工业验证数十年的成熟方法论，具备真实的长期复利潜力：一旦'白模空间约束'成为标准创作层，创作者的素材积累与预演思维训练将形成切换成本，控制层有望沉淀为AI视频堆栈的常驻环节，并随专业创作渗透（影视/广告/短剧）而持续放大价值。但必须冷静看待两个稀释因素：其一，Seedance/Kling/Veo等视频大模型自身3D空间理解能力快速增强后，白模这一中间表示可能被原生空间推理能力替代，存在'过渡性技术'风险；其二，预演能力极易被模型厂商或大平台内化吸收（如剪映/CapCut类产品一键集成），独立工具层的价值捕获不确定性较高。因此定性为'有潜力成为细分赛道基础设施，但需持续验证'的中位偏上区间，而非8分以上的基石级判断。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- updream
- ByteDance (Seedance)
- Kuaishou (Kling)
- Alibaba (Wan)
- Google (Gemini Veo)
competitive_casualty:
- ComfyUI 空间控制节点工作流
- 传统 Previs 预演服务商
- 缺乏控制层的纯提示词视频平台
- 面向简单白模场景的 Blender/Maya 建模需求
market_opportunities:
- 创业者可为影视、短剧、广告等垂直行业开发'AI白模预演+成片渲染'的一体化工作流工具，将原本需要数月学习门槛的Previz预演能力下放到普通创作者，降低前期分镜与预演成本
- AI视频创作工具应将'空间约束'类能力（白模/深度图/相机路径/走位轨道）作为核心差异化卖点集成到创作画布中，以解决复杂镜头不可控这一行业痛点，从而黏住具备编导思维的专业用户
- 预演白模、运镜模板与走位轨道可作为可复用的数字资产沉淀，建议探索预演资产库与模板交易平台的商业化机会，类似于3D行业的素材市场
risk_matrix:
  regulatory: 版权与内容标识风险：上传场景参考图生成白模可能涉及第三方版权素材的未授权使用，商业用途需完成图像确权；AI视频生成内容在国内面临深度伪造防范与生成内容标识（如AIGC水印）等监管要求
  technological: 技术替代风险：若Seedance、Kling、Wan等视频模型后续原生支持相机路径与空间布局控制（如相机token、运动轨迹条件输入），白模预演作为外部空间锚点的中间方案可能被逐步边缘化，成为过渡性技术路线
  competitive: 竞争格局风险：可灵、即梦、Runway等视频模型厂商很可能将预演/相机控制能力原生内建进官方创作台，updream这类第三方预演工具的生态位易被巨头挤压；ComfyUI开源社区也可能出现成本更低的替代工作流
  ethical: 伦理与就业冲击：白模预演大幅降低分镜与预演门槛，可能冲击影视前期工种（Previz艺术家、分镜师、初级建模师）的就业结构；参考图生成白模及模型训练涉及未授权数据与个人肖像权益风险
  additional:
  - 产品留存风险：updream官方强调其并非'傻瓜式'一键出片工具，用户仍需理解场景层级、机位与运动轨迹关联，叠加白模生成需等待4-7分钟，非专业用户上手门槛较高，可能造成'叫好不叫座'
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: updream 预演台 (Previs Studio)
  canonical_name: updream Previs Studio
  url: null
  positioning: updream新上线的预演台功能，将影视工业成熟的Previs白模预演工作流搬入创作画布，以3D白模作为空间锚点约束AI视频生成，解决镜头不可控问题。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 影视行业科班创作者
  - 专业编导与摄影师
  - 追求复杂镜头控制的AI视频创作者
  product_signal: 实测四步完成预演：新建预演台、上传参考图生成白模、新建人物机位绘制走位轨道、录制导出至下游节点，加入白模后一镜到底镜头被固定。
  market_signal: 针对AI视频生成3D空间与镜头调度不可控的核心痛点，将影视行业成熟工作流产品化，降低建模门槛，属于AI视频工具链的差异化增量。
  differentiation: 相比自己啃Blender/Maya数月或搭ComfyUI复杂节点工作流，预演台以AI生成3D白模大幅降低门槛，且不是傻瓜式一键出片，保留专业调度能力。
  watch_reason: AI视频生成已进入专业编导能力放大阶段，镜头与空间可控性是下一阶段核心竞争点。updream将影视工业Previs工作流产品化，白模约束方案有跨模型通用潜力，其粗/细粒度白模分层设计与实测减少抽卡的效果值得持续跟踪验证。
  risk_notes:
  - 白模生成仍需要4-7分钟，且预演台不是傻瓜式工具，创作者需理解场景层级、机位与运动轨迹关联，上手门槛高于普通文生视频工具。
  - 复杂叙事镜头仍需提前拆解分镜，白模约束对极端复杂场景的适用性和生成稳定性有待更多实测验证。
  score: 9.0
  article_ids:
  - b8dec70b700ebde7
  evidence_snippets:
  - updream新上线的功能预演台（Previs Studio）把影视行业成熟的Previs预演工作流搬进了创作画布。
  - 创作者先搭建3D白模场景，定好机位，排完人物走位，录制预演视频，再交给Seedance、Kling、Wan、Gemini Veo等视频模型完成最终渲染。
  - 实测操作只需四步：新建预演台、上传1-3张场景参考图生成场景白模、新建人物与机位并绘制走位轨道、录制白模视频导出至下游节点。
- object_type: product
  name: updream
  canonical_name: updream
  url: null
  positioning: updream是上线预演台（Previs Studio）功能的AI视频创作平台，通过AI生成3D白模降低建模门槛，让创作者先设计镜头再生成视频。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 有编导思维的科班或专业人士
  - AI视频专业创作者
  product_signal: 平台将白模预演能力内嵌于创作画布，支持场景白模生成、人物机位搭建、走位轨道绘制与预演视频导出，并衔接自有其他功能视频模型。
  market_signal: updream借助AI能力降低建模门槛，但定位并非傻瓜式一键出片工具，面向有编导思维的专业创作者，与市面通用文生视频工具形成区隔。
  differentiation: 与Blender、Maya等传统3D工具相比，updream以参考图即可生成高还原度3D白模场景，大幅压缩从零上手的数月学习成本。
  watch_reason: updream以预演台切入AI视频可控性这一核心痛点，将影视工业方法论产品化，且与Seedance、Kling等主流模型生态互通，代表AI视频工具从生成走向调度的方向，值得持续跟踪其用户反馈与功能演进。
  risk_notes:
  - 预演台实测上手仍有一定门槛，创作者需理解场景层级、机位与运动轨迹关联，普通用户可能难以直接受益。
  - 文章为单一媒体实测，缺乏长期用户反馈与规模化验证数据，产品成熟度仍需观察。
  score: 8.0
  article_ids:
  - b8dec70b700ebde7
  evidence_snippets:
  - 在学妹指导下，作者体验了updream新上线的预演台功能，上传户外婚礼场景参考图后，白模生成用时不足5分钟。
  - updream借助AI能力降低了建模门槛，但它不是傻瓜式一键出片工具，创作者仍需理解场景层级、机位与运动轨迹的关联。
- object_type: project
  name: ControlNet
  canonical_name: ControlNet
  url: https://github.com/lllyasviel/ControlNet
  positioning: ControlNet是Stable Diffusion时代的空间控制方案，通过在生成图片前输入深度图、法线贴图或简易3D模型等空间信息来约束画面，解决画面失控问题。
  technical_signal: ControlNet通过输入深度图、法线贴图或简易3D模型等空间信息约束生成画面，即使火柴人级输入也能稳定约束人物姿态与透视关系。
  adoption_signal: 该思路在Stable Diffusion时代被广泛用于解决画面失控问题，随后被迁移到视频生成领域，成为白模约束方案的技术源头。
  ecosystem_relevance: ControlNet提出的空间信息约束生成范式为后续视频生成的白模预演方案奠定基础，updream预演台等新工具可视作其在视频领域的延续。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: ControlNet代表了以空间锚点约束生成的方法论起点，其思路正在视频生成领域被预演台等产品重新激活，追踪其影响可判断AI视频可控性技术路线的演进方向。
  risk_notes:
  - ControlNet仅为文中提及的历史参考方案，文章未提供其当前维护状态或视频领域直接应用的最新信息，持续跟踪价值有限。
  score: 4.0
  article_ids:
  - b8dec70b700ebde7
  evidence_snippets:
  - 早在Stable Diffusion时代，ControlNet就已经给出过解法，人们在生成图片前输入深度图、法线贴图或简易3D模型等空间信息来约束画面。
- object_type: product
  name: Blender
  canonical_name: Blender
  url: https://www.blender.org/
  positioning: Blender是免费开源的全能3D创作套件，支持建模、动画、渲染等完整流程，但传统3D工具学习成本极高，从零上手需数月甚至更久。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 3D建模与动画从业者
  - 传统3D内容创作者
  product_signal: Blender作为免费开源全能3D创作套件，功能全面但上手门槛高，对追求效率的AI创作者而言难以承受数月学习时间成本。
  market_signal: 文章将Blender定位为传统3D工具高门槛的代表，与AI预演台形成对比，凸显AI降低建模门槛的市场机会。
  differentiation: 与updream预演台等AI工具相比，Blender从零上手需数月甚至更久，专业能力强大但效率导向的AI创作者难以直接使用。
  watch_reason: Blender作为开源3D工具的标杆，其与AI工作流（如预演台）的关系变化值得关注，但本文仅将其作为传统高门槛工具的对比参照，跟踪优先级不高。
  risk_notes:
  - 文章仅以对比视角提及Blender，未提供其AI集成、社区生态或最新动态信息，缺乏独立跟踪的事实基础。
  score: 3.0
  article_ids:
  - b8dec70b700ebde7
  evidence_snippets:
  - Blender作为免费开源全能3D创作套件，从零上手动辄需要数月甚至更久，对追求效率的AI创作者而言难以承受这样的时间成本。
- object_type: product
  name: Maya
  canonical_name: Autodesk Maya
  url: https://www.autodesk.com/products/maya
  positioning: Maya是商用影视级3D动画软件，常用于影视工业制作流程，但与传统3D工具一样从零上手通常需要数月甚至更久，学习成本极高。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 影视动画从业者
  - 视觉特效与动画师
  product_signal: Maya作为商用影视级3D动画软件，功能专业且被影视行业广泛使用，但其从零上手需数月甚至更久，对AI创作者门槛过高。
  market_signal: 文章将Maya作为传统影视级3D工具的代表，与AI预演台形成对比，说明专业级运镜能力正在被AI工具下放。
  differentiation: 相比Maya等商用影视级软件，updream预演台以参考图生成3D白模，无需数月学习即可获得专业级镜头调度能力，形成显著体验差异。
  watch_reason: Maya作为影视级3D工具标杆，其专业运镜能力正在被AI预演台等新工具所替代的趋势值得观察，但本文仅将其作为对比参照，缺乏独立跟踪的事实基础。
  risk_notes:
  - 文章仅以对比视角提及Maya，未提供其AI集成或最新功能信息，证据有限，独立跟踪价值较低。
  score: 3.0
  article_ids:
  - b8dec70b700ebde7
  evidence_snippets:
  - Maya作为商用影视级3D动画软件，与Blender一样从零上手通常需要数月甚至更久，传统3D工具的学习成本极高。
- object_type: project
  name: ComfyUI
  canonical_name: ComfyUI
  url: https://github.com/comfyanonymous/ComfyUI
  positioning: ComfyUI是节点式AI图像生成工作流工具，过去要达到白模效果需在其中搭建复杂的节点工作流，是专业用户实现精细控制的手段之一。
  technical_signal: ComfyUI以节点式工作流实现精细控制，过去用户需在其中搭建复杂节点体系才能达到白模效果，门槛较高。
  adoption_signal: 文章将其作为过去实现白模效果的两条路径之一（另一为学习Blender），说明其在专业AI创作者中具备一定采用基础。
  ecosystem_relevance: ComfyUI与ControlNet等空间控制方案同属AI生成精细控制生态，updream预演台等产品化方案可能分流其部分复杂工作流需求。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: ComfyUI是AI图像生成控制工作流的重要载体，updream预演台等白模方案若持续产品化，可能改变专业用户对其复杂节点工作流的依赖，值得观察。
  risk_notes:
  - 文章仅以一句提及ComfyUI，未提供其版本更新、生态现状或与预演台的直接对比信息，独立跟踪依据有限。
  score: 3.0
  article_ids:
  - b8dec70b700ebde7
  evidence_snippets:
  - 过去要达到白模效果，要么自己啃几个月Blender，要么去ComfyUI里搭一套复杂的节点工作流。
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