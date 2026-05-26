---
title: You can now remix other people’s YouTube Shorts with AI
source: https://www.theverge.com/tech/934704/google-gemini-omni-youtub-shorts-remix-ai
author:
- '[[Terrence O’Brien]]'
published: '2026-05-20'
created: '2026-05-21'
description: Google announced a new YouTube Shorts Remix feature that lets users restyle
  clips or even insert themselves into other people's videos using Gemini Omni. Now,
  at the bottom of a YouTube Short, when you click the remix icon, you'll see an option
  to "reimagine" it. Here, you can prompt Gemini to turn a video into [&#8230;]
tags:
- clippings
extraction_status: success
id: decb0744cbe9f9e8
source_type: news_media
tldr: Google 为 YouTube Shorts 推出基于 Gemini Omni 的 AI 重混功能，用户可提示词转换视频风格或修改内容。
objective_summary: Google 于 2026 年 5 月宣布 YouTube Shorts 新 Remix 功能，集成 Gemini Omni
  模型。用户点击 Shorts 底部 remix 图标后选择"reimagine"选项，通过自然语言提示词可将视频转换为像素艺术、动漫、恐怖片等风格，
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Google
  - YouTube
  technologies:
  - Gemini Omni
  - digital watermarking
  key_people: []
key_logic_flow:
- Google 宣布 YouTube Shorts 新增 Remix 功能，底层集成 Gemini Omni 多模态 AI 模型
- 用户在任意 Shorts 底部点击 remix 图标后，出现"reimagine"选项，可通过自然语言提示词驱动 AI 对视频进行风格转换
- 支持的风格转换包括像素艺术、动漫、伪纪录片恐怖片等，同时也支持内容级别的修改（放大头部、插入背景演员、更换服装等）
- 用户还可通过该功能将自身形象插入到他人的 Shorts 视频中
- 创作者拥有控制权：可在上传时选择关闭 AI 重混功能，防止他人操纵自己的视频内容
- 所有通过 Gemini Omni 重混生成的视频均强制添加数字水印（digital watermark），并自动链接回原始视频以保障来源可追溯
pipeline_stage: fact_extracted
impact_score:
  score: 6.5
  reason: Google 将 Gemini Omni 多模态 AI 视频编辑能力部署到 YouTube Shorts（全球最大短视频平台之一），属于重要产品发布。该功能让数亿用户通过自然语言提示词即可进行视频风格转换和内容修改，大幅降低了
    AI 视频编辑门槛。创作者控制权和强制数字水印的设计体现了一定的部署成熟度。但本质上这是已有 AI 视频技术（风格迁移、内容编辑）的大规模产品化落地，而非底层模型能力或训练范式的根本性突破，因此评分在
    6-7 区间。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: 数字水印的鲁棒性与 AI 生成内容的溯源可靠性——水印能否抵抗裁剪、压缩等二次处理，以及是否能真正防止深度伪造滥用
hype_assessment:
  level: medium
  reason: Google 使用 'reimagine' 等营销化命名包装功能，但报道来自 The Verge 相对克制，且功能有明确的产品形态（remix
    入口、提示词交互、风格选项）、创作者控制开关和数字水印等具体落地细节，非纯概念炒作。存在一定包装但核心是真实产品发布。
information_entropy: medium
domain_disruption:
  technical_innovation: Gemini Omni 多模态模型在 YouTube 超大规模消费级视频平台上的产品化部署能力——包括实时视频理解、风格迁移推理和内容级编辑的端到端管线，以及数字水印+溯源链接的双重内容真实性保障体系
  business_model: 重塑 UGC 短视频的二次创作范式：AI 重混将视频编辑门槛从专业工具降低到自然语言交互，可能催生新的内容创作行为和病毒传播模式，同时创作者控制权机制在开放创作与保护原创之间建立了新的平台治理平衡，直接影响
    YouTube 与 TikTok 在短视频赛道的竞争格局
engineering_complexity: production_ready
compound_value:
  score: 7.0
  reason: 该功能本质上是 Google 将自研基础模型能力向超级应用分发的经典打法。长期复利体现在三个层面：（1）数据飞轮——每一次 AI 重混都在为 Google
    的视频生成模型贡献高质量多模态训练数据，这种规模化、低成本的标注数据采集机制是竞争对手难以复制的壁垒；（2）平台锁定——Remix 功能通过「数字水印 +
    自动链接回原始视频」构建了闭环归因体系，创作者内容被重混得越多，其原始视频曝光越多，形成正向激励，进一步加固 YouTube 的创作者生态护城河；（3）广告库存扩张——AI
    驱动的 UGC 重混降低了内容生产门槛，理论上可指数级扩张 Shorts 的内容供给，直接转化为更多广告位和用户时长。但扣分项在于：AI 视频风格转换本身并非不可逾越的技术壁垒，TikTok/Meta
    等竞品有能力在 6-12 个月内跟进类似功能，因此该事件的长期独特性存疑。综合来看，这是一次典型的「巨头用 AI 加固现有城池」而非「创造新大陆」的事件，评分
    7.0。
value_capture_layer: end_application
moat_impact: strengthens_monopoly
key_beneficiaries:
- Google
- Alphabet
- YouTube 头部创作者
competitive_casualty:
- TikTok
- Meta (Instagram Reels)
- Runway
- Pika
- AI 视频编辑初创公司
market_opportunities:
- 数字水印与内容溯源赛道迎来实质性需求爆发：Google 强制要求所有 AI 重混视频添加水印并链接回原始视频，这将推动 YouTube 生态内外的第三方水印验证、版权归属追踪和内容真实性审核工具的市场需求，创业者可围绕「AI
  生成内容的可验证溯源」构建 SaaS 或 API 服务
- AI 视频风格迁移工具向 C 端下沉的创业窗口打开：Gemini Omni 的多模态能力通过 Shorts 触及数十亿用户，验证了「自然语言驱动的视频重混」的
  PMF，建议关注面向 TikTok、Instagram Reels 等竞品平台的类似工具开发机会，或针对特定垂直领域（如电商产品视频一键换装、教育视频风格适配）的微调方案
- 创作者经济进入「AI 协同创作」新范式：该功能允许用户将自身形象插入他人视频，意味着个人 IP 的跨内容流动成为可能，创作者和 MCN 机构应提前布局「AI 分身」授权管理模式，探索基于
  AI 形象授权的新的变现路径
risk_matrix:
  regulatory: 该功能涉及对他人视频内容的实质性修改（包括人物外观、场景元素），在欧盟 AI Act 下可能触发「深度伪造」相关的高风险分类披露义务；在美国则面临各州不同步的肖像权法和深度伪造立法的合规碎片化风险；此外，用户将自身形象插入他人视频的行为涉及双向隐私同意问题，可能引发
    GDPR/CCPA 下的数据主体权利纠纷
  technological: 数字水印技术在面对截图、录屏、二次压缩等攻击时鲁棒性存疑，若水印被轻易绕过将导致溯源机制形同虚设，进而引发信任危机；同时，开源多模态模型（如
    Qwen-VL 系列）正在快速缩小差距，若竞品平台基于开源方案实现类似功能且无平台锁定，YouTube 的先发优势窗口可能比预期更短
  competitive: TikTok 和 Instagram Reels 大概率将在短期内跟进类似功能——TikTok 已有 Symphony AI 套件基础，Meta
    有 Movie Gen 模型储备，AI 视频重混的「功能均质化竞争」即将展开；对于中小型视频平台而言，无法自研多模态模型的玩家将被进一步边缘化，行业集中度可能加速提升
  ethical: 最突出的风险在于非自愿内容操纵——尽管创作者可关闭重混功能，但该选项默认开启（opt-out 而非 opt-in），大量不熟悉隐私设置的用户可能在不知情的情况下其视频被篡改；儿童视频（Google
    官方也特别提及）若被恶意风格化为恐怖片或不当内容，社会影响极为恶劣；此外，该功能可能被滥用于政治人物的视频操纵，为虚假信息传播提供新的低成本途径
  additional:
  - 平台责任边界模糊风险：当用户利用 AI 重混功能生成侵权或诽谤内容时，YouTube 作为工具提供方和 Gemini 作为模型提供方之间的责任划分尚不明确，可能引发集体诉讼
  - 创作者出走风险：头部创作者若认为 AI 重混稀释了原创内容的独特性和价值，可能减少在 YouTube 的投入或转向对 AI 更保守的平台
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: strategic_invest
---

Google announced a new YouTube Shorts Remix feature that lets users restyle clips or even insert themselves into other people’s videos using Gemini Omni. Now, at the bottom of a YouTube Short, when you click the remix icon, you’ll see an option to “reimagine” it. Here, you can prompt Gemini to turn a video into pixel art, an anime, or a found-footage horror film. But, beyond that, you can also alter the contents by, say, inflating heads, inserting background actors, dressing people in pirate costumes, or even putting yourself in the clip.

# You can now remix other people’s YouTube Shorts with AI

Gemini Omni can turn video into anime or put giant heads on people.

Gemini Omni can turn video into anime or put giant heads on people.

Creators can enable or disable the ability to reimagine videos. So, if you upload a short of your kids and would prefer (for obvious and understandable reasons) that people not be able to manipulate it, you can turn off remixing. Google also says that shorts remixed through Omni will have a digital watermark and link back to the original video.

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.