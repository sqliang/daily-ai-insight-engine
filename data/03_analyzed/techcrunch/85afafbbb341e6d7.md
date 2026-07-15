---
title: Midjourney wants Hollywood studios to reveal the details of their AI usage
source: https://techcrunch.com/2026/07/04/midjourney-wants-hollywood-studios-to-reveal-the-details-of-their-ai-usage/
author:
- '[[Anthony Ha]]'
published: '2026-07-04'
created: '2026-07-05'
description: As part of an ongoing legal dispute with three Hollywood studios, Midjourney
  is seeking to compel those studios to reveal how they use AI themselves.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 85afafbbb341e6d7
manifest_dates:
- '2026-07-05'
- '2026-07-06'
source_type: news_media
tldr: Midjourney要求好莱坞工作室披露AI使用细节，以证明用版权内容训练AI是行业惯例。
objective_summary: 在迪士尼、环球和华纳兄弟起诉Midjourney侵犯版权后，Midjourney向法院申请要求这些工作室披露其内部使用生成式AI的全部情况，包括用于故事板和内容构思的AI模型及提示词，以证明未授权使用版权内容训练AI属于行业惯例。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - Midjourney
  - Disney
  - Universal
  - Warner Bros.
  technologies:
  - generative AI
  - image-generation models
  key_people:
  - David Singer
key_logic_flow:
- 迪士尼和环球去年起诉Midjourney侵犯版权，称其图像生成模型可创建受版权保护的角色形象（如巴特·辛普森和达斯·维达），随后华纳兄弟也提起类似诉讼。
- 法官此前裁定工作室需提供生成式AI使用信息，但仅限于面向消费者的视频和图片，而非内部使用。
- Midjourney申请推翻该限制，认为工作室可以借此筛选对其有利的文件，而隐瞒能支持Midjourney抗辩的证据。
- Midjourney声称若工作室内部也在开发图像生成AI用于故事板或内容构思，则证明未授权使用版权内容训练AI是行业惯例。
- Midjourney还要求工作室披露在Midjourney上使用的所有提示词及输出结果，而非仅限涉嫌侵权的内容。
- 工作室首席律师David Singer称Midjourney的请求属于"钓鱼式取证"，并强调工作室无意阻止AI技术发展，只是要求停止未经授权复制其影视作品和角色。
extract_result: success
impact_score:
  score: 5.5
  reason: 这是AI版权诉讼中的一次策略性法律交锋，Midjourney试图通过反制性证据开示要求来构建'行业惯例'抗辩。案件本身涉及AI训练数据的合法性边界这一核心行业命题，但本次事件仅属于取证阶段的程序性动作，尚未触及实质判决或创造判例。对AI行业的短期冲击有限，主要影响在法律合规策略层面，不会立刻改变技术格局或竞争态势。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: AI训练数据的合理使用原则在司法实践中的适用边界
hype_assessment:
  level: low
  reason: 文章是对真实法律诉讼进展的客观新闻报道，未使用'颠覆'、'革命性'等PR夸大词汇。Midjourney的'行业惯例'论证是一个具体的法律抗辩策略，而非技术突破声明。事件本身是已提交的法庭文件，事实基础扎实，不存在概念炒作空间。
information_entropy: medium
domain_disruption:
  technical_innovation: 无
  business_model: 如果法院采纳Midjourney的'行业惯例'论证逻辑，将建立'自身也在使用AI的公司不能完全禁止他人使用版权数据训练AI'的先例，可能削弱版权所有者对训练数据的排他性主张，从而降低AI公司获取训练数据的法律风险和合规成本，重塑AI训练数据的合规生态。
engineering_complexity: production_ready
compound_value:
  score: 4.5
  reason: 这是一项诉讼程序中的法律动议，本身不是技术或产品交付，不具备持续的复利积累效应。其长期价值完全取决于法院是否采纳Midjourney的'行业惯例'抗辩逻辑。若采纳，将为AI使用未授权版权内容训练模型确立关键判例先例，从根本上降低所有基础模型公司的数据合规风险，影响全行业训练数据范式。但此案处于早期取证阶段，从动议到最终裁决路径漫长且高度不确定（可能经历多年上诉），且法官有较大裁量权。评分4.5反映了'高影响力但极强路径依赖和不确定性'的折中判断——一旦利好结果落地则是行业分水岭，但当前节点距离实质结论还很远。
value_capture_layer: foundation_model
moat_impact: democratizes_access
key_beneficiaries:
- Midjourney
- Stability AI
- OpenAI
- Anthropic
- Google DeepMind
competitive_casualty:
- Disney
- Universal
- Warner Bros.
- Getty Images
- Shutterstock
market_opportunities:
- AI训练数据合规审计服务将迎来爆发式增长，企业需要专业机构评估其训练数据来源的版权风险并建立合规流程
- 影视娱乐行业AI使用治理工具存在蓝海机会，可开发覆盖提示词管理、输出溯源、版权检查的一站式企业AI治理平台
- 版权清晰的授权训练数据集市场价值将被重估，创业者可构建经授权的影视/创意内容数据集并以此作为差异化优势
risk_matrix:
  regulatory: 该案可能成为美国AI训练数据合理使用边界的标志性判例，若Midjourney败诉将引发行业级合规地震，全球各国（尤其是欧盟AI Act、中国生成式AI管理办法）可能加速出台训练数据版权合规细则
  technological: 若法院最终裁定未授权使用版权内容训练AI不构成合理使用，几乎所有基于大规模互联网爬取数据训练的生成式图像模型将面临技术路线颠覆——要么重新训练要么获得授权
  competitive: 好莱坞工作室一边起诉侵权一边内部自研AI工具的双重标准一旦被证据证实，将严重削弱其诉讼道德立场，但同时也揭示出大型内容方正在从被侵权者转型为AI竞赛参与者，形成新的竞争格局
  ethical: 该案本质是创作者权益保护与AI技术发展之间的根本冲突，裁判结果将深刻影响数字时代创作生态——过度倾向AI可能打击原创动力，过度限制可能扼杀技术创新
  additional:
  - 诉讼取证阶段的拉锯战可能导致案件拖延数年，期间行业处于高不确定性状态，投资决策面临法律风险溢价
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
---

As part of an ongoing legal dispute with three Hollywood studios, AI startup Midjourney is seeking to compel those studios to reveal how they use AI themselves.

Disney and Universal sued Midjourney for alleged copyright infringement last year, noting that the startup’s image-generation models could create images of characters, such as Bart Simpson and Darth Vader, who are owned by the studios. A few months later, Warner Bros. sued Midjourney as well.

The startup argues that training its AI models on images of copyrighted characters is permitted under fair use.

The current dispute revolves around the documentation the studios will need to produce during the discovery process. A judge previously ruled that the studios would indeed have to provide information about their generative AI usage – but only when it led to “consumer-facing” videos and images.

In its latest filing, Midjourney seeks to overturn that limitation, arguing that it “unfairly” allows the studios “to cherry-pick only those documents they believe support their market harm claims while depriving Midjourney of documents that would support its defenses.”

Midjourney goes on to claim that the “documents [the studios] are withholding are precisely those that would reveal whether, behind closed doors, they are doing exactly what they are suing Midjourney for doing.”

For example, the startup says that if the studios are developing image-generating AI models “for internal use in storyboarding or ideating content for film or TV, that evidence would equally demonstrate that it is an industry custom, even among the studios themselves, to download and train AI on unlicensed copyrighted content.”

In the filing, the startup also argues that the studios should reveal all the prompts they used in Midjourney, as well as the resulting outputs, not just the prompts that produced the allegedly infringing images.

The studios’ lead attorney David Singer previously claimed Midjourney was seeking this documentation as part of a “fishing expedition.”

He also said the studios “do not seek to stop AI technology or even shut down Midjourney’s business,” but rather “simply want Midjourney to stop copying their movies and TV shows and to stop distributing, publicly displaying, publicly performing, and creating derivative works that include copies of [their] famous characters without authorization.”