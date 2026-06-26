---
title: Deezer says its new feature lets fans remix songs with artist consent
source: https://techcrunch.com/2026/06/24/deezer-says-its-new-feature-lets-fans-remix-songs-with-artist-consent/
author:
- '[[Lauren Forristal]]'
published: '2026-06-24'
created: '2026-06-25'
description: Global music streaming service Deezer is taking a contrarian approach
  to AI, even as it adds a feature that lets fans remix songs.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 3d6d1a7b7d8fccd9
source_type: news_media
tldr: Deezer 推出 Remix Lab，粉丝可在艺术家授权下混音歌曲并让艺术家获得报酬
objective_summary: 2026年6月24日，Deezer 发布 Remix Lab 功能，允许粉丝在艺术家授权下通过应用内工具（调整节奏、添加混响、改变音乐类型和风格）创作混音作品。该功能最初仅在法国上线，面向
  Céline Dion 等部分法国艺术家作品开放。Deezer 强调混音版本的每次播放都会向版权方支付报酬，
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Deezer
  - YouTube
  - Spotify
  - Universal Music Group
  - Apple Music
  technologies: []
  key_people:
  - Alexis Lanternier
  - Pierre Trochu
key_logic_flow:
- Deezer 推出 Remix Lab 功能，允许粉丝在获得原艺术家和版权方同意后对歌曲进行混音创作，且混音版本的每次播放都会向艺术家支付报酬。
- Remix Lab 提供应用内混音工具（调整节奏、添加混响、改变音乐类型和风格），与 YouTube 和 Spotify 依赖 AI 进行混音的方案形成对比。
- Deezer 长期采取抵制 AI 音乐的立场，其平台主动识别并移除 AI 生成曲目，不将其纳入编辑推荐歌单。
- Remix Lab 最初仅在法国上线，面向 Céline Dion、Alain Souchon、Alonzo 等法国艺术家作品开放混音。
- Deezer 同步在 Deezer Club 举办混音竞赛，获胜作品将入选官方歌单，获胜者获得 Deezer Purple Door 活动门票及艺术家周边。
extract_result: success
impact_score:
  score: 4.0
  reason: Deezer 作为小型流媒体平台（市场份额远低于 Spotify/Apple Music），其 Remix Lab 功能在技术层面并无突破——应用内音频混音工具（调节奏、加混响、改风格）已是成熟技术。真正的亮点在于'艺术家授权
    + 每次混音播放均付费'的版权模式，这在当前 AI 混音大行其道的行业中构成一种差异化信号。但该功能目前仅在法国上线、仅限少数法国艺术家作品，且 Deezer
    用户基数有限，短期内对行业格局几乎没有冲击力。综合评分 4.0。
sentiment: positive
developer_sentiment:
  tone: skeptical
  primary_focus: 音轨混音工具的技术实现并无新意，核心看点在于授权与分账模式而非工程创新
hype_assessment:
  level: medium
  reason: 文章本身是 TechCrunch 的客观报道而非 Deezer 通稿，但 Deezer 在 PR 中刻意强化'反 AI'立场并将 Remix Lab
    包装成行业异类，存在一定程度的叙事包装。'让粉丝参与创作'和'艺术家获得报酬'是合理的价值主张，但未提供技术细节说明混音能力有何独到之处，本质上仍是常规应用内音频编辑功能的商业包装。
information_entropy: medium
domain_disruption:
  technical_innovation: 无。应用内音频混音（调整节奏、混响、风格转换）是音乐制作软件中已成熟的技术，Deezer 并未提出新的音频处理算法或架构创新。
  business_model: 艺术家授权 + 每次混音播放均向版权方付费的模式，在主流流媒体平台中较为罕见，与 YouTube/Spotify 依赖 AI 生成混音的路径形成对比。若该模式被验证可行，可能为音乐版权方提供一种新变现途径，并影响其他平台在
    AI 音乐 vs 人工创作之间的策略选择。
engineering_complexity: production_ready
compound_value:
  score: 3.5
  reason: Deezer Remix Lab 是端应用层的功能创新，核心差异化在于'艺术家授权+每次播放付费'模式，且 Deezer 借此强化了反 AI 音乐的品牌定位。但从
    VC 复利视角看，该事件商业价值有限：1) Deezer 全球市场份额不足 2%，远非行业主导者，其产品策略难以左右行业走向；2) 该功能仅限法国市场且仅面向少数法国艺人，规模化路径不清晰；3)
    混音工具技术门槛低，Spotify、YouTube 等巨头可快速跟进复制，Deezer 毫无护城河；4) 作为公开上市公司产品功能而非基础设施级创新，不具备网络效应或数据飞轮。3-5
    年后此功能大概率成为行业历史注脚，除非其授权+付费模式被广泛采纳为行业标准，但 Deezer 无力推动这一变革。
value_capture_layer: end_application
moat_impact: neutral
key_beneficiaries:
- Deezer
competitive_casualty:
- AI 音乐创作平台
- AI 混音工具
market_opportunities:
- 可借鉴 Deezer 的授权+付费混音模式，在视频、播客等内容平台构建类似的二次创作授权与版税分账基础设施
- AI 音乐检测与合规工具赛道机会扩大——随着混音内容增加，识别未授权 AI 生成/混音音乐的工具需求将持续上升
- 围绕艺术家版权许可管理的 SaaS 服务平台存在空白，可帮助版权方在 AI 时代实现授权自动化与实时版税追踪
risk_matrix:
  regulatory: Deezer 的授权混音模式虽主动合规，但若推广至全球，不同司法管辖区对衍生作品版税分配的法律差异可能带来合规复杂性；同时该模式隐含对
    AI 混音的批判立场，可能触发欧盟 AI Act 关于生成式 AI 在创意产业应用的讨论
  technological: Deezer 采用非 AI 的应用内工具进行混音（调整节奏、混响、风格变换），若 YouTube 和 Spotify 的 AI 混音技术在质量和体验上大幅领先，Deezer
    可能在用户创作自由度上处于竞争劣势
  competitive: YouTube（AI 混音）、Spotify（与 UMG 合作 AI 翻唱/混音）等巨头资金与用户规模远超 Deezer，且 Deezer
    初期仅限法国市场、少数艺人，如不能快速规模化则面临生态挤压
  ethical: 该功能主动规避了 AI 混音常见的版权侵权与艺术家报酬缺失问题，具有正面伦理示范效应；但若未来扩大至更多艺术家，需警惕「授权」机制在操作层面是否真正充分知情、防止权利滥用
  additional: []
confidence:
  impact: medium
  compound: low
  hype: medium
actionable_insight: speculative_watch
---

Global music streaming service Deezer announced on Wednesday the launch of its new feature, “Remix Lab,” which allows fans to creatively remix songs with the consent of the original artists and rights holders. Plus, the company says artists actually get paid for every stream of these remixed tracks.

The new Remix Lab feature can be found in the app on select artists’ pages. Unlike competing services that rely on AI for remixes, Deezer implements in-app tools to create remixes, such as adjusting tempo and adding reverb, or “more elaborate transformations such as changes to musical genre and style,” head of product Pierre Trochu explains in today’s blog post.

In comparison, YouTube lets creators remix tracks using AI tools, and Spotify has recently teamed up with Universal Music Group for AI-generated covers and remixes. However, some argue that this approach brings more AI music to these platforms, which could overshadow human artists, making it more challenging for them to gain traction.

Deezer has taken a strong stance against AI for some time and recently introduced a new tool that analyzes playlists from streaming services such as Spotify and Apple Music to detect AI-generated tracks. The platform is also recognized as one of the few streaming services that actively removes AI tracks from its recommendations and omits them from editorial playlists.

“This remix tool perfectly embodies our vision of offering a product that enriches the listening experience for fans, by allowing them to participate in the creative process and create a deeper connection with their favorite music, directly in the Deezer app,” CEO Alexis Lanternier said in a statement. “True to our DNA, these features are made possible with full participation of the artists, fully respecting rights, and maximizing earnings for each track.”

While Remix Lab is initially available in France (with vague plans to roll it out to other countries eventually), this feature is notable in the streaming industry because it runs so contrary to the AI-generated direction that most of them are going. Should it prove popular with music fans and artists, it could be a signal that the AI invasion on streaming services isn’t the only future the music industry could pursue.

It could also become an example for other services of how artists can be compensated for their work as fans enjoy remixes. Currently, users are able to remix tracks from select French artists, such as Céline Dion, Alain Souchon, Alonzo, Ronisia, Mosimann, Tiakola, and Zaho.

Additionally, users can sign up for contests hosted in the Deezer Club, where winners will be announced in early September. Winning remixes will be featured in a dedicated Deezer playlist, and each winner will also receive two tickets to a Deezer Purple Door event, along with exclusive merchandise from the respective artist.