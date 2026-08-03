---
title: LinkedIn actually adds a ‘seems like AI slop’ button
source: https://www.theverge.com/ai-artificial-intelligence/973384/linkedin-seems-like-ai-slop-button
author:
- '[[Jay Peters]]'
published: '2026-07-30'
created: '2026-07-31'
manifest_dates:
- '2026-07-31'
description: A lot of content on LinkedIn might seem like AI slop, and now, you'll
  be able to report those posts. As part of a series of updates to reduce the volume
  of AI slop on the platform, LinkedIn is introducing an actual button that lets you
  flag a post as something that "Seems like AI [&#8230;]
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 5df6cbdbbfce999b
source_type: news_media
tldr: LinkedIn 正式推出'看起来像 AI 垃圾内容'举报按钮，用户可在帖子菜单中标记疑似 AI 生成的帖子，配合新分类器减少推荐流中的 AI 垃圾内容。此前检测显示
  41% 的长文被判定完全由 AI 生成，产品总监称 AI slop 是最高优先事项。
objective_summary: LinkedIn 推出一个举报按钮，允许用户在帖子的三点菜单中选择'看起来像 AI 垃圾内容'来标记疑似非人工撰写的帖子，点击后帖子会被隐藏并显示感谢反馈。此举是平台减少
  AI 垃圾内容的一系列更新的一部分，LinkedIn 同时上线新分类器以识别 AI 生成或低质量内容，并减少其在推荐和网络外内容中的出现。此前 AI 检测公司
  Pangram 发现 41% 的 LinkedIn 长文被判定为完全由 AI 生成。产品总监 Hari Srinivasan 表示 AI slop 是最高优先事项，公司还计划移除
  AI 润色功能并测试向用户展示他人对其帖子真实性感受的功能。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - LinkedIn
  - Pangram
  - 404Media
  - The Verge
  technologies:
  - AI slop
  - AI-generated content detection
  - content classifiers
  key_people:
  - Hari Srinivasan
key_logic_flow:
- LinkedIn 正在推出一个举报按钮，允许用户在帖子的三点菜单中选择'看起来像 AI 垃圾内容'来标记疑似 AI 生成的帖子。
- 该按钮是 LinkedIn 减少平台 AI 垃圾内容的一系列更新之一，产品总监 Hari Srinivasan 表示 AI slop 是所有人的最高优先事项。
- AI 检测公司 Pangram 发现 41% 的 LinkedIn 长文帖子被判定为完全由 AI 生成，这一数据由 404Media 报道。
- LinkedIn 同时上线新的分类器，用于识别帖子是否为 AI 垃圾内容或一般低质量内容，以减少推荐内容和网络外内容中的 AI 垃圾。
- 用户点击举报按钮后帖子会被隐藏，LinkedIn 会显示感谢反馈的信息，并利用这些反馈来调优模型和改善信息流。
- LinkedIn 正在测试向用户展示其他人认为其帖子不真实或重度使用 AI 的功能，并移除 AI 润色功能，改用只校对不改语气的功能。
object_mentions:
- object_type: product
  name: LinkedIn 'Seems like AI slop' button
  canonical_name: LinkedIn Seems like AI slop button
  url: https://www.linkedin.com
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - LinkedIn 正式推出一个举报按钮，用户可在帖子三点菜单中选择'看起来像 AI 垃圾内容'来标记疑似 AI 生成的帖子。
  - 点击该按钮后 LinkedIn 会立即隐藏该帖子，并向用户显示一条感谢其反馈的提示信息。
  article_id: 5df6cbdbbfce999b
- object_type: company
  name: Pangram
  canonical_name: Pangram
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - AI 检测公司 Pangram 发现 41% 的 LinkedIn 长文帖子被标记为完全由 AI 生成，这一数据由 404Media 报道。
  article_id: 5df6cbdbbfce999b
- object_type: product
  name: LinkedIn proofread feature
  canonical_name: LinkedIn proofread feature
  url: https://www.linkedin.com
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - LinkedIn 将移除使用 AI 来'增强'帖子的功能，并替换为一个'校对你的文字但不改变你的语气'的新功能。
  article_id: 5df6cbdbbfce999b
extract_result: success
impact_score:
  score: 5.5
  reason: 评分依据：这是主流职业社交平台首次将'AI 垃圾内容'举报直接产品化，配合 41% 长文疑似完全由 AI 生成的第三方数据，标志 AI slop
    从社区吐槽升级为平台级治理问题，对内容平台的 AI 内容审核策略有示范效应。但它本质是防御性内容治理功能，而非技术范式突破，影响范围局限于 LinkedIn
    及同类社交平台，不改变 AI 模型或行业整体走向，因此未达到 8 分以上的范式转移级别。综合评定为 5.5 分。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: AI 内容检测分类器的准确性与误报风险，以及创作者依赖 AI 辅助写作是否会被误判为'垃圾内容'
hype_assessment:
  level: low
  reason: 判定依据：文章描述的是已上线、可实际点击验证的功能（The Verge 记者亲自测试了按钮），不存在'颠覆'、'革命性'等 PR 滥用词汇；41%
    的 AI 生成比例来自独立第三方公司 Pangram（经 404Media 报道），而非 LinkedIn 官方宣传口径；产品总监表态克制（'我们很重视这件事'）。整体属于实打实的产品更新，水分极低。
information_entropy: high
domain_disruption:
  technical_innovation: 将'用户显式举报信号 + 自动内容分类器 + 推荐模型反馈调优'组合成闭环的 AI 内容治理体系，并配套产品策略（下架
    AI 润色功能、改为保留用户语气的校对功能、测试向作者展示他人对其内容真实性的感知），属于平台级内容治理工程实践。技术上并非底层检测算法突破，创新点在于把人类反馈信号与分类器协同用于信息流治理。
  business_model: 平台把'内容真实性'正式纳入生态治理规则，直接压缩依赖 AI 批量生成帖子换取曝光的增长黑客式营销空间，可能推动职业内容创作者回归真实表达；同时
    LinkedIn 主动收缩自身 AI 增强功能，释放了'AI 辅助需以保真为前提'的产品信号，间接影响面向社交平台的 AI 写作工具生态的合规边界。
engineering_complexity: production_ready
compound_value:
  score: 6.0
  reason: 事件本质是平台层为'生成式 AI 内容泛滥'构建信任基础设施，这是随 LLM 生成成本趋近于零而持续放大的结构性矛盾，具备长期复利属性：41%
    长文被判定完全由 AI 生成这一数据表明问题已具系统性，LinkedIn 的举报按钮、分类器与反馈闭环构成了一个不断积累训练数据的真实性治理飞轮，未来 3-5
    年内容真实性校验几乎确定会从'可选项'变为所有内容平台的基础设施。但需要谨慎的是：检测技术本质是攻防军备竞赛，生成模型的迭代速度快于检测器，单一平台的功能级方案复利效应有限；真正的长期价值沉淀在'社交图谱+用户反馈数据+真实性标签'的组合中，而非检测算法本身。因此给出中性偏上的
    6 分——问题确定性高，但具体执行层的技术护城河需要持续验证，尚无证据表明 LinkedIn 的分类器具备跨平台迁移的通用壁垒。
value_capture_layer: end_application
moat_impact: strengthens_monopoly
key_beneficiaries:
- LinkedIn
- Microsoft
- Originality.ai
- GPTZero
- Pangram
competitive_casualty:
- AI 内容农场
- 依赖 AI 批量生产长文的营销机构
- 生成式 AI 灌水工具
- 缺乏审核资源的小型新社交平台
market_opportunities:
- 创业者可基于 AI 内容真实性检测赛道，开发面向创作者与品牌方的'内容人味检测'工具，在发布前评估内容被判定为 AI 生成的风险，并给出保留个人风格的改写建议
- 建议关注面向企业社媒运营的'AI 辅助但保留真人感'内容生产工作流，将 AI 用于资料检索、事实核查与校对，但把语气和观点表达留给真人，降低被平台标记为 AI
  slop 的运营风险
- 个人可将'人机协作写作'作为可沉淀的技能：用 AI 完成信息整理与初稿框架，注入个人经历、观点与独特叙事，形成难以被分类器误判且更有传播力的原创表达
risk_matrix:
  regulatory: LinkedIn 的'AI slop'分类与举报机制可能引发内容审核透明度与误判争议；欧盟 DSA 等法规要求平台披露审核逻辑并提供申诉渠道，若分类器存在语言或文化偏见，还可能面临歧视性算法质询，但当前无直接诉讼风险
  technological: AI 检测分类器本质上存在误报/漏报，且与生成式 AI 形成对抗性军备竞赛（改写工具可规避检测）；未来若大模型内置水印或内容凭证（如
    C2PA）成为标准，独立检测技术可能被替代
  competitive: X、Meta、Reddit 等主流平台可能跟进类似'低质/AI 内容'治理功能，使检测能力成为平台标配；LinkedIn 自带分类器也将挤压
    Pangram 等独立 AI 检测初创公司的市场空间
  ethical: 分类误报可能误伤真实创作者的劳动成果，引发'AI 羞辱'与创作寒蝉效应；对非英语内容与不同写作风格的检测偏差可能放大不平等；平台收集并展示其他用户对帖子真实性的主观反馈，可能给作者带来隐私泄露与心理压力
  additional:
  - 用户可能利用举报按钮对竞争对手或意见不合者进行规模化恶意标记（brigading），污染反馈信号与推荐算法
  - 平台对'AI slop'的定义本身高度主观，治理标准缺乏透明共识，可能引发用户对内容审查边界的信任危机
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: monitor
object_insights:
- object_type: product
  name: LinkedIn 'Seems like AI slop' button
  canonical_name: LinkedIn Seems like AI slop button
  url: https://www.linkedin.com
  positioning: LinkedIn 面向平台用户推出的内容治理功能，通过帖子三点菜单中的'看起来像 AI 垃圾内容'按钮，让用户标记疑似 AI 生成的帖子以净化推荐信息流。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - LinkedIn 平台内容消费者
  - 职场内容创作者
  product_signal: 平台同步上线新分类器识别 AI 垃圾或低质量内容，用户举报后帖子即时隐藏，反馈被用于调优模型与改善信息流。
  market_signal: AI 检测机构 Pangram 发现 41% 的 LinkedIn 长文被判定完全由 AI 生成，产品总监称 AI slop 是所有人的最高优先事项，反映治理需求迫切。
  differentiation: 区别于纯算法过滤，该功能引入用户主动标记的众包机制，与分类器协同治理 AI 垃圾内容，强调社区参与反馈闭环。
  watch_reason: 该按钮是 LinkedIn 系统性治理 AI 垃圾内容的标志性动作，其与众包反馈、新分类器的联动机制将影响信息流真实度，可作为观察主流平台如何应对
    AI 生成内容泛滥的重要指标，值得持续跟踪其上线范围与治理效果。
  risk_notes:
  - 用户标记高度依赖主观判断，真实人工内容可能被误报为 AI 生成，需观察误判率与申诉机制。
  - 新分类器与举报机制的治理效果短期难以量化，41% 的 AI 长文占比说明问题规模较大，成效有待验证。
  score: 7.0
  article_ids:
  - 5df6cbdbbfce999b
  evidence_snippets:
  - LinkedIn 正式推出一个举报按钮，用户可在帖子三点菜单中选择'看起来像 AI 垃圾内容'来标记疑似 AI 生成的帖子。
  - 点击该按钮后 LinkedIn 会立即隐藏该帖子，并向用户显示一条感谢其反馈的提示信息。
- object_type: product
  name: LinkedIn proofread feature
  canonical_name: LinkedIn proofread feature
  url: https://www.linkedin.com
  positioning: LinkedIn 正在调整的 AI 写作辅助功能，将移除使用 AI'增强'帖子的能力，改为只校对文字、不改变用户语气的新功能。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - LinkedIn 内容创作者
  - 使用 AI 写作辅助的职场用户
  product_signal: 该功能从 AI'增强'写作改为只校对而不改变语气，体现 LinkedIn 对 AI 写作辅助产品方向的克制化调整。
  market_signal: 在 AI 写作工具普遍强调增强能力的大背景下，LinkedIn 反其道转向保守校对，反映平台对 AI 生成内容的反制趋势。
  differentiation: 与常见的一键润色增强型 AI 写作工具不同，该功能刻意限制 AI 介入程度，以保留创作者个人语气为核心卖点。
  watch_reason: 该功能与举报按钮同属 LinkedIn 治理 AI 垃圾内容的系列举措，其从增强写作向保留人声校对的转向，可作为观察 AI 写作工具产品方向变化的信号。
  risk_notes:
  - 仅提及替换计划，新校对功能的具体能力边界与上线时间尚不明确，存在方向调整的不确定性。
  - 移除 AI 增强功能可能削弱部分创作者依赖的写作辅助能力，新校对功能的价值需要用户验证。
  score: 5.0
  article_ids:
  - 5df6cbdbbfce999b
  evidence_snippets:
  - LinkedIn 将移除使用 AI 来'增强'帖子的功能，并替换为一个'校对你的文字但不改变你的语气'的新功能。
---

A lot of content on LinkedIn might seem like AI slop, and now, you’ll be able to report those posts. As part of a series of updates to reduce the volume of AI slop on the platform, LinkedIn is introducing an actual button that lets you flag a post as something that “Seems like AI slop.”

# LinkedIn actually adds a ‘seems like AI slop’ button

You can now report posts that don’t feel human-written.

You can now report posts that don’t feel human-written.

The new feature is part of a broader push to reduce the volume of apparent AI slop on the platform. AI detector Pangram recently found that 41 percent of longform LinkedIn posts were flagged as being completely generated by AI, as reported by *404Media*.

“AI slop is a top priority for all of us,” chief product officer Hari Srinivasan says in a post. “We really care about this.” In addition to the button to report a post as seemingly being AI-generated, LinkedIn is also ramping up new classifiers to identify “if a post is AI-slop or generally low-quality content,” which will “reduce the amount of AI slop you might see in suggested content and content from outside your network.”

I’m currently seeing the new report button in the three-dots menu on posts. When I click it, LinkedIn hides the post and shows a message thanking me for my feedback.

The new button will help LinkedIn “tune our models and make better feeds,” Srinivasan says. The company is also testing a way to show people that other users feel their posts come across as inauthentic or that they include heavy use of AI.

In addition, LinkedIn is removing a feature that used AI to “enhance” a post and will replace it with a “feature that proofreads your words, but does not change your voice,” according to Srinivasan.

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.