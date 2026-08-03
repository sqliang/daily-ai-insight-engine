---
title: SpaceXAI launches Grok Voice Think Fast 2.0 on Agent Builder (2 minute read)
source: https://www.testingcatalog.com/spacexai-launches-grok-voice-think-fast-2-0-on-agent-builder/#google_vignette?utm_source=tldrai
author: []
published: ''
created: '2026-07-31'
manifest_dates:
- '2026-07-31'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: b82a85aafcf3d2ce
source_type: news_media
tldr: xAI发布新一代语音到语音模型Grok Voice Think Fast 2.0，定价每分钟0.08美元，在Artificial Analysis基准上综合得分82.9%，超越GPT-Realtime-2.1与Gemini
  3.1 Flash。该模型面向语音Agent开发者，转录准确率较前代大幅提升，8月5日起grok-voice-latest别名将自动切换至2.0。
objective_summary: xAI于2026年8月初推出语音到语音模型Grok Voice Think Fast 2.0，面向构建语音Agent的开发者，按每分钟音频0.08美元计费。在Artificial
  Analysis语音基准测试中，该模型综合得分82.9%，高于前代Think Fast 1.0的75.7%、OpenAI GPT-Realtime-2.1的79.1%及Google
  Gemini 3.1 Flash的69.5%，首次音频响应时间从1.25秒降至0.70秒。xAI称其在24种语言的短句转录准确率较Deepgram Nova 3与ElevenLabs
  Scribe v2提升1.5至2倍，在背景噪声与电话压缩场景下差距约为10倍。xAI在Starlink电话服务的A/B测试中报告了更高的销售转化与客服分流率，并宣布8月5日起grok-voice-latest别名将自动指向新模型。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - xAI
  - OpenAI
  - Google
  - Deepgram
  - ElevenLabs
  - Starlink
  - Artificial Analysis
  technologies:
  - speech-to-speech
  - reinforcement learning
  - word error rate
  key_people: []
key_logic_flow:
- xAI发布新一代语音到语音模型Grok Voice Think Fast 2.0，面向构建语音Agent的开发者，按每分钟音频0.08美元计费，且无需修改既有提示词即可在几乎所有用例中提升表现。
- 在Artificial Analysis语音基准上，2.0版综合得分82.9%，高于1.0版的75.7%，并超过GPT-Realtime-2.1的79.1%与Gemini
  3.1 Flash的69.5%，其智能体得分达到56.5%。
- 该模型采用与语音并行的推理设计，推理token用量降至前代的0.4倍，首次音频响应时间由1.25秒缩短至0.70秒，生产环境工具调用通常在智能体说完第一句话前即可执行。
- xAI报告其在24种语言短句上的转录准确率较Deepgram Nova 3与ElevenLabs Scribe v2提升1.5至2倍，在强背景噪声与电话压缩场景下差距约10倍。
- xAI在Starlink电话服务上进行的A/B测试显示更高的销售转化率与客服分流率，用以支撑模型在真实客户工作流中的可靠性主张。
- 2026年8月5日起grok-voice-latest别名将自动从grok-voice-think-fast-1.0切换至2.0，需要旧版的开发者必须在此之前固定1.0标识，其他用户无需任何操作。
object_mentions:
- object_type: model
  name: Grok Voice Think Fast 2.0
  canonical_name: Grok Voice Think Fast 2.0
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - xAI推出新一代语音到语音模型Grok Voice Think Fast 2.0，面向构建语音Agent的开发者，按每分钟音频0.08美元计费。
  - 在Artificial Analysis语音基准上，Think Fast 2.0综合得分82.9%，高于1.0版的75.7%并超过GPT-Realtime-2.1与Gemini
    3.1 Flash。
  - 2026年8月5日起grok-voice-latest别名将自动从grok-voice-think-fast-1.0切换至grok-voice-think-fast-2.0。
  article_id: b82a85aafcf3d2ce
- object_type: model
  name: Grok Voice Think Fast 1.0
  canonical_name: Grok Voice Think Fast 1.0
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Think Fast 2.0在Artificial Analysis语音基准上综合得分82.9%，高于前代Think Fast 1.0的75.7%，其智能体得分亦从52.1%升至56.5%。
  - 需要继续使用旧版的开发者必须在8月5日别名切换前固定grok-voice-think-fast-1.0标识。
  article_id: b82a85aafcf3d2ce
- object_type: model
  name: GPT-Realtime-2.1
  canonical_name: OpenAI GPT-Realtime-2.1
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 在Artificial Analysis语音基准上，GPT-Realtime-2.1综合得分为79.1%，低于Think Fast 2.0的82.9%，仅在对话基准上以95.7%略高于后者的95.1%。
  article_id: b82a85aafcf3d2ce
- object_type: model
  name: Gemini 3.1 Flash
  canonical_name: Google Gemini 3.1 Flash
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 在Artificial Analysis语音基准上，Gemini 3.1 Flash综合得分为69.5%，智能体得分为37.7%，均低于Think Fast
    2.0的82.9%与56.5%。
  article_id: b82a85aafcf3d2ce
- object_type: product
  name: Deepgram Nova 3
  canonical_name: Deepgram Nova 3
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - xAI称Think Fast 2.0在24种语言短句上的转录准确率较Deepgram Nova 3提升1.5至2倍，衡量指标采用词错误率。
  article_id: b82a85aafcf3d2ce
- object_type: product
  name: ElevenLabs Scribe v2
  canonical_name: ElevenLabs Scribe v2
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - xAI称Think Fast 2.0在24种语言短句上的转录准确率较ElevenLabs Scribe v2提升1.5至2倍，强噪声与电话压缩场景下差距约10倍。
  article_id: b82a85aafcf3d2ce
extract_result: success
impact_score:
  score: 7.5
  reason: 该发布直接改写了实时语音 Agent 市场的竞争格局：在第三方基准（Artificial Analysis）上综合得分 82.9%，同时超越 OpenAI
    GPT-Realtime-2.1（79.1%）与 Google Gemini 3.1 Flash（69.5%），且 0.70 秒首字音频延迟与 0.08 美元/分钟的定价在质量-成本-延迟三角上形成综合冲击，属于足以改变局部竞争格局的重要产品发布。但它是现有语音到语音赛道的迭代领先，而非
    ChatGPT 或 Transformer 论文级别的范式转移，因此未给到 8 分以上。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 基准分数领先与 0.70 秒首字延迟是否在真实生产环境中可复现，以及 0.08 美元/分钟定价下语音 Agent 的成本结构重构
hype_assessment:
  level: medium
  reason: 文章混用了两类证据：第三方基准（Artificial Analysis 综合分 82.9%）可信度较高，但 24 语言转录准确率提升 1.5-2
    倍、强噪声下约 10 倍差距、Starlink A/B 测试转化率提升等均为厂商自报数据且缺乏独立复现，需谨慎对待。同时'无需修改提示词即可在几乎所有用例中提升表现''生产环境工具调用在智能体说完第一句话前执行'等表述带有明显的
    PR 包装色彩。核心基准与定价数据基本可靠，故判定为中等水分。
information_entropy: high
domain_disruption:
  technical_innovation: 语音与推理并行执行（reason in parallel with speech）的架构设计将推理 token 用量降至前代
    0.4 倍，在不牺牲延迟的前提下支撑更复杂查询；叠加强化学习驱动的句长压缩与减少冗余对话，使首字音频延迟从 1.25 秒降至 0.70 秒，并在 agentic
    得分上拉开与竞品差距——这是语音到语音模型在延迟-智能权衡上的实质工程突破。
  business_model: 以 0.08 美元/分钟的低价锚定实时语音 API 调用成本，可能带动整个语音 Agent 定价体系下探，对 Deepgram、ElevenLabs
    等专用语音供应商形成正面冲击；配合 grok-voice-latest 别名平滑升级策略（8 月 5 日自动切换、无需改提示词）大幅降低开发者迁移摩擦，加速语音
    Agent 从试点走向规模化商用。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: 评估逻辑：这不是单点产品发布，而是对'实时语音 Agent 基础设施'这一层的定价与性能重置。三方面支撑复利判断——(1) 价格锚点：$0.08/分钟对标或优于
    GPT-Realtime-2.1 与 Gemini 3.1 Flash，直接把实时语音 Agent 的边际成本拉低，加速整个品类的开发者采用，而开发者一旦用
    grok-voice-latest 建产品就会形成迁移成本和生态粘性；(2) 架构代差：'推理与语音并行'将首次音频响应从 1.25s 压到 0.70s、推理
    token 降至前代 0.4 倍，这属于可累积的工程资产，而非一次性营销参数，后续迭代可继续在此架构上叠加；(3) 数据飞轮：Starlink 电话业务的真实
    A/B 测试场景让 xAI 拥有别家没有的真实对话/电话噪声数据回流，强化转录与工具调用的短板，形成'模型更强→部署更多→数据更多'的正循环。扣分项：语音到语音是
    OpenAI/Google/Deepgram/ElevenLabs 混战的高竞争赛道，领先窗口通常以季度计，且 xAI 的语音能力高度绑定其自有分发（X/Starlink），对第三方开发者的生态控制力尚需验证。综合判定处于'细分赛道基础设施候选'区间的上沿，但距
    8 分以上的确定性基石仍有距离。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- xAI
- Starlink
- Vapi
- Retell AI
competitive_casualty:
- Deepgram
- ElevenLabs
- OpenAI
- Google
market_opportunities:
- 语音 Agent 开发者可利用 Think Fast 2.0 低至 0.70 秒的首音频延迟与并行推理设计，构建实时客服、销售外呼等高转化场景产品，借助“工具调用在智能体说完第一句话前即可执行”的特性提升用户留存与转化率
- 该模型在强背景噪声与电话压缩场景下相对 Deepgram Nova 3、ElevenLabs Scribe v2 约 10 倍的转录准确率优势，为呼叫中心质检、电话客服、嘈杂环境语音输入等垂直场景提供了差异化选择，创业者可围绕电话音频场景开发专用解决方案
- 0.08 美元/分钟的低定价与无需修改提示词的兼容性，为现有语音 Agent 服务商创造了从 OpenAI Realtime 等方案迁移以降低推理成本的窗口期，第三方基准对比工具与迁移评估服务存在市场空间
risk_matrix:
  regulatory: 语音 AI 涉及通话录音、用户知情同意与数据留存等隐私合规要求；若该模型被用于自动外呼营销或冒充客服的诈骗场景，将面临电信监管与消费者保护法规（如
    GDPR、CCPA）的追责风险；xAI 训练数据来源及跨境数据流动亦可能触发出口管制与数据本地化审查
  technological: 语音到语音模型迭代极快（1.0 到 2.0 间隔很短），8 月 5 日 grok-voice-latest 别名将自动切换至 2.0
    属破坏性变更，未提前固定 1.0 标识的开发者可能遭遇生产环境行为漂移；同时 OpenAI GPT-Realtime-2.1、Gemini 3.1 Flash
    正在快速追赶，基准领先优势未必持久
  competitive: xAI 以 0.08 美元/分钟的激进定价切入语音 Agent 市场，可能引发价格战并挤压 Deepgram、ElevenLabs 等专注转录与语音合成厂商的利润空间；开发者面临平台锁定风险，OpenAI
    与 Google 生态可能以捆绑折扣或模型能力升级进行反击
  ethical: 高质量语音合成与实时语音 Agent 可能被滥用为深度伪造、自动诈骗电话与冒充客服的犯罪工具；24 种语言的转录准确率存在差异，可能对非英语语言用户造成服务质量偏见；客服与话务等岗位面临被自动化替代的就业冲击
  additional:
  - 官方宣称的基准优势与 Starlink 电话服务 A/B 测试结果均出自 xAI 集团内部（Starlink 属同一控制人体系），缺乏第三方独立复现验证，存在营销溢价与实证不足的风险
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: Deepgram Nova 3
  canonical_name: Deepgram Nova 3
  url: null
  positioning: Deepgram Nova 3 是面向实时语音转写的专业转录模型，服务语音 Agent 与客服场景，在本次对比中被视为转录准确率的行业基准之一。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 语音 Agent 开发者
  - 客服中心与电话语音场景
  - 多语言转录应用团队
  product_signal: 该模型被作为转录准确率对比基线，xAI 宣称 Think Fast 2.0 在 24 种语言短句上准确率高出其 1.5 至 2
    倍，衡量指标为词错误率。
  market_signal: 被头部语音模型厂商主动作为对标对象，说明其在语音转录细分市场仍具代表性地位。
  differentiation: 与端到端语音到语音模型不同，Nova 3 专注纯转录环节，以低词错误率与多语言覆盖为卖点。
  watch_reason: 作为 xAI 官方对标的两大转录基线之一，Nova 3 的基准分数直接影响 Grok Voice 2.0 转录优势主张的可信度与市场说服力，值得持续跟踪其后续基准更新、产品迭代以及厂商在语音转录赛道的竞争回应。
  risk_notes:
  - 对比数据由 xAI 单方报告，非独立第三方评测，准确性需独立验证。
  - 文章仅在短句与特定噪声场景下对比，未覆盖长音频与多方言等复杂场景。
  score: 4.0
  article_ids:
  - b82a85aafcf3d2ce
  evidence_snippets:
  - xAI称Think Fast 2.0在24种语言短句上的转录准确率较Deepgram Nova 3提升1.5至2倍，衡量指标采用词错误率。
- object_type: product
  name: ElevenLabs Scribe v2
  canonical_name: ElevenLabs Scribe v2
  url: null
  positioning: ElevenLabs Scribe v2 是 ElevenLabs 面向多语言与噪声场景推出的语音转录产品，常与 Deepgram Nova
    并列成为行业转录基准。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 语音转录开发者
  - 字幕与多语言本地化团队
  - 电话与客服语音分析场景
  product_signal: xAI 宣称 Think Fast 2.0 在 24 种语言短句转录准确率上较其提升 1.5 至 2 倍，强噪声与电话压缩场景差距约
    10 倍。
  market_signal: 作为 ElevenLabs 语音产品线在转录领域的代表，被竞争对手主动对标，显示其在语音生态中的竞争分量。
  differentiation: 以多语言转录准确率和抗噪声能力为核心竞争力，是语音合成之外 ElevenLabs 布局转录赛道的关键产品。
  watch_reason: 该模型被 xAI 单独点名对比，尤其提出强噪声与电话压缩场景约 10 倍的转录差距主张，这一判断若被验证将直接影响 Scribe 的竞争定位，值得关注
    ElevenLabs 的正式回应及 Scribe 系列后续版本升级。
  risk_notes:
  - xAI 的 1.5 至 2 倍与约 10 倍差距均为其单方宣称，缺乏第三方独立复测。
  - 对比集中在短句场景，未充分覆盖长音频、方言与口音等实际生产条件。
  score: 4.0
  article_ids:
  - b82a85aafcf3d2ce
  evidence_snippets:
  - xAI称Think Fast 2.0在24种语言短句上的转录准确率较ElevenLabs Scribe v2提升1.5至2倍，强噪声与电话压缩场景下差距约10倍。
---

xAI has introduced Grok Voice Think Fast 2.0, its next-generation speech-to-speech model, with gains in intelligence, transcription accuracy, conversational behavior, and tool use. The model is aimed at developers building voice agents and costs $0.08 per minute of audio. xAI expects it to raise performance across almost all use cases without changes to existing prompts.

On Artificial Analysis’ speech-to-speech benchmark, Think Fast 2.0 scored 82.9% overall, up from 75.7% for version 1.0 and ahead of GPT-Realtime-2.1 at 79.1% and Gemini 3.1 Flash at 69.5%. Its agentic score reached 56.5%, compared with 52.1% for its predecessor, 45.7% for GPT-Realtime-2.1, and 37.7% for Gemini 3.1 Flash. Time to first audio fell from 1.25 seconds to 0.70 seconds. The model’s 95.1% conversational benchmark score was just below GPT-Realtime-2.1 at 95.7%.

Transcription is another major focus. In xAI’s evaluation of thousands of short phrases across 24 languages, the company reported accuracy improvements of 1.5 to 2.0 times versus Deepgram Nova 3 and ElevenLabs Scribe v2, and 1.4 times versus Think Fast 1.0. xAI says the gap is roughly 10× under substantial background noise and telephony compression. The comparison uses the word error rate, with lower scores preferred.

Think Fast 2.0 reasons in parallel with speech, a design intended to preserve latency while handling more complex queries. Median relative reasoning-token use fell to 0.4 times, using the predecessor’s 1.0 times as a baseline. xAI says this lets production tool calls usually execute before the agent finishes its first sentence. Reinforcement learning also pushed the model toward shorter sentences, one question at a time, and less fluff while guiding users through complex workflows.

For SpaceXAI, this release is a push to make Grok Voice more dependable in real customer workflows. An A/B test on Starlink’s phone service produced higher sales conversion and support containment rates, according to the company. On August 5, 2026, the grok-voice-latest alias will automatically move from grok-voice-think-fast-1.0 to grok-voice-think-fast-2.0. Developers who want the prior model must pin the 1.0 identifier before the switch; everyone else needs to take no action.