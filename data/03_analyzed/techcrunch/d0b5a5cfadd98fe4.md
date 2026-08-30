---
title: Barret Zoph, the Thinking Machines co-founder ousted before joining OpenAI,
  is now at Google
source: https://techcrunch.com/2026/08/27/barret-zoph-the-thinking-machines-co-founder-who-defected-to-openai-is-now-at-google/
author:
- '[[Lucas Ropek]]'
published: '2026-08-27'
created: '2026-08-28'
manifest_dates:
- '2026-08-28'
description: Zoph, who co-founded Thinking Machines Lab alongside Mira Murati and
  also served as the startup's CTO, led a brief stint at OpenAI and is now at Google.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: d0b5a5cfadd98fe4
source_type: news_media
tldr: Thinking Machines 联合创始人 Barret Zoph 在被解雇后重返 OpenAI，仅任职五个月又离职，现已加入 Google 出任研究副总裁。Google
  发言人表示期待他将强化学习与后训练专长带给 Gemini，文章同时指出 OpenAI 过去八个月流失大量关键高管。
objective_summary: Barret Zoph 曾在 OpenAI 工作两年，于 2024 年 10 月离职，并与此前已离开的 Mira Murati
  共同创立 AI 初创公司 Thinking Machines。2026 年 1 月，他与另一位联合创始人 Luke Metz 离开 Thinking Machines
  重返 OpenAI，事后披露其系被解雇。Zoph 在 OpenAI 负责 AI 企业销售，仅任职五个月后于 6 月离职，现已出任 Google 研究副总裁。Google
  发言人确认了这一任命，并表示期待他将强化学习与后训练专长带给 Gemini。
event_type: capital_movement
epistemic_status: verified_fact
entities:
  companies:
  - Google
  - OpenAI
  - Thinking Machines
  technologies:
  - Gemini
  - RL
  - post-training
  key_people:
  - Barret Zoph
  - Mira Murati
  - Luke Metz
key_logic_flow:
- Barret Zoph 曾在 OpenAI 工作两年，于 2024 年 10 月离职，并与 Mira Murati 共同创立 AI 初创公司 Thinking
  Machines。
- 2026 年 1 月，Zoph 与另一位联合创始人 Luke Metz 离开 Thinking Machines 重返 OpenAI，事后披露他系被解雇。
- Zoph 在 OpenAI 负责 AI 企业销售，仅任职五个月后于 2026 年 6 月再次离职。
- Zoph 现已加入 Google 出任研究副总裁，Google 发言人表示期待他将强化学习与后训练专长带给 Gemini。
- 文章指出 AI 行业高管流动率高，OpenAI 过去八个月流失大量关键员工，包括 COO 与一位顶级数据中心高管。
object_mentions:
- object_type: company
  name: Thinking Machines
  canonical_name: Thinking Machines
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Barret Zoph 在 OpenAI 工作两年后，于 2024 年 10 月离职，并与 Mira Murati 共同创立 AI 初创公司 Thinking
    Machines。
  - 2026 年 1 月，Zoph 与另一位联合创始人 Luke Metz 离开 Thinking Machines 重返 OpenAI，事后披露他系被解雇。
  article_id: d0b5a5cfadd98fe4
- object_type: product
  name: Gemini
  canonical_name: Gemini
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Google 发言人向《华尔街日报》表示，期待 Barret 回归 Google，并将他的强化学习与后训练专长带给 Gemini。
  article_id: d0b5a5cfadd98fe4
extract_result: success
impact_score:
  score: 4.5
  reason: 该事件属于头部 AI 公司之间的核心人才流动：Barret Zoph 是 RLHF 早期方法论（Deep RL from Human Preferences、InstructGPT
    系列）的贡献者之一，其加盟对 Google Gemini 的后训练与偏好对齐能力是明确补强；同时事件再次暴露 OpenAI 在冲刺 IPO 前夜连续流失 COO、数据中心高管及企业销售负责人的组织动荡，属于资本市场与行业舆论关注的负面信号。但本质仍是一次单一高管任命，不构成技术范式转移或产品级冲击，对短期行业竞争格局的影响是边际性的，不会立即改变用户可感知的模型能力。综合评定
    4.5 分。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: OpenAI 高管持续流失背后的组织稳定性隐患，以及 Zoph 的 RL 后训练专长能否在 Gemini 训练管线上真正落地
hype_assessment:
  level: low
  reason: 报道为 TechCrunch 的事实性人事新闻，全篇是对已证实事件的客观陈述，未出现"颠覆""革命性""改变一切"等 PR 滥用词汇，也无概念包装或前瞻性夸大；唯一带倾向性的表述是对
    OpenAI 高管流失现象的观察，属于合理推断而非炒作话术。因此判定为低炒作。
information_entropy: medium
domain_disruption:
  technical_innovation: 事件本身无直接技术突破，潜在技术驱动力在于 Zoph 在 RLHF/后训练方向的深厚积累——他加盟后可能强化 Gemini
    的偏好对齐、推理优化与在线强化学习能力，属于研究组织层面的补强而非新技术发布。
  business_model: 人才争夺折射出大模型军备竞赛正从预训练算力规模转向后训练工程化：OpenAI 在 IPO 前夜八个月内连续流失企业销售负责人（Zoph
    仅任职五个月）、COO 与数据中心高管，显示其商业化组织稳定性承压；Google 通过引入后训练人才补齐 Gemini 短板，体现头部厂商以人才投资换取模型代差竞争力的商业逻辑。
engineering_complexity: production_ready
compound_value:
  score: 4.5
  reason: 单起高管人事变动本身不具备基础设施属性，但该事件是稀缺人才资本向 Google Gemini 集聚的明确信号。RL/后训练是当前前沿模型竞争中最稀缺、最难以外包复制的关键能力层，顶尖研究者沉淀到
    Gemini 会转化为模型迭代优势，具有跨版本复利效应。然而价值兑现高度依赖 Zoph 在 Google 的实际产出——此前他在 OpenAI 被安排在 AI
    企业销售岗仅五个月即离职，存在角色错配与管理风险，且单一人事变动的不确定性大，需持续验证其对 Gemini 后训练能力的实际贡献。
value_capture_layer: foundation_model
moat_impact: strengthens_monopoly
key_beneficiaries:
- Google
- Google DeepMind
competitive_casualty:
- OpenAI
- Thinking Machines
market_opportunities:
- 建议关注高端 AI 人才流动催生的专业猎头与薪酬/期权咨询机会，头部实验室高管轮换频繁，垂直化的 AI 人才中介服务存在市场缺口
- Google 明确将强化学习与后训练作为 Gemini 差异化重点，可关注面向中小团队的 RL 后训练工具链、评估与训练即服务（Training-as-a-Service）的创业方向
- OpenAI 高管持续流失削弱企业客户长期信心，企业侧对多模型编排与供应商多元化（避免单一实验室绑定）的需求可能上升
risk_matrix:
  regulatory: 高管频繁跨司流动可能引发商业秘密与非竞争条款争议，但目前事件暂无直接监管风险，需关注美国 AI 人才竞业限制诉讼的演进趋势
  technological: Zoph 的 RL 与后训练专长加入 Google 将强化 Gemini 模型迭代能力，对依赖 OpenAI 技术路线的第三方生态构成技术替代压力
  competitive: Google 持续加码 Gemini 并吸纳顶尖 RL 人才，基础模型头部竞争加剧；OpenAI 八个月关键高管流失削弱其组织执行力与客户信心，可能影响其
    IPO 叙事
  ethical: 顶尖人才向少数巨头集中加剧行业资源垄断与创新同质化；频繁人才流动伴随隐性知识迁移，埋下知识产权与保密义务争议隐患
  additional:
  - OpenAI 高管离职潮暴露其公司治理与组织稳定性风险，可能波及其企业客户续约与 IPO 进程
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: monitor
object_insights:
- object_type: product
  name: Gemini
  canonical_name: Gemini
  url: null
  positioning: Gemini 是 Google 的旗舰 AI 模型系列，覆盖多模态推理与生成场景，正通过引入强化学习与后训练专家强化模型优化能力。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users: []
  product_signal: Google 确认将 Barret Zoph 的强化学习与后训练专长投入 Gemini，显示该产品正加码模型后训练环节的能力建设。
  market_signal: AI 行业高管流动加剧，OpenAI 持续流失关键人才，Google 借此吸纳研究高管，或改变大模型厂商间的人才与技术竞争格局。
  differentiation: Zoph 兼具 OpenAI 训练研究与 Thinking Machines 创业经验，其加入或为 Gemini 在后训练与强化学习路线上构建差异化优势。
  watch_reason: Gemini 作为 Google 对抗 OpenAI 与 Anthropic 的核心产品，其通过引进强化学习与后训练领军人物来加固技术栈的动向，反映大模型竞争重心正向后训练迁移，值得持续跟踪其能力演进与人才布局。
  risk_notes:
  - 文章未披露 Zoph 在 Gemini 的具体职责与权限范围，其实际技术影响力仍待观察。
  - AI 行业高管流动率高，Zoph 此前在 OpenAI 任职仅五个月，其岗位稳定性构成不确定性。
  score: 5.0
  article_ids:
  - d0b5a5cfadd98fe4
  evidence_snippets:
  - Google 发言人向《华尔街日报》表示，期待 Barret 回归 Google，并将他的强化学习与后训练专长带给 Gemini。
---

The game of musical chairs for AI executives continues. Barret Zoph, a co-founder of the AI startup Thinking Machines who left the company earlier this year to rejoin OpenAI, has found yet another job.

Zoph spent two years at OpenAI and left in October 2024 to co-found Thinking Machines with Mira Murati, who had left the AI lab the month prior. In January, Zoph and another Thinking Machines co-founder, Luke Metz, quite dramatically departed from the startup to return to OpenAI. It was later revealed that Zoph had been fired.

His return didn’t quite stick. Zoph spent only five months at OpenAI, where he was tasked with heading AI enterprise sales. He left the company in June. And now we know where he landed.

Zoph has taken a position as vice president of research at Google (which happens to be another company where he previously worked). “We look forward to Barret returning to Google and bringing his RL and post-training expertise to Gemini,” a Google spokesperson told the Wall Street Journal.

TechCrunch reached out to OpenAI and Google for more information.

It’s not always easy to divine why tech executives seem to be spending less time in their roles. The turnover rate in the AI industry is high, and it’s been especially high at OpenAI — a company that, despite readying itself for an IPO and being one of the most powerful presences in the tech world, has lost a lot of critical staff over the last eight months. The turnover of high-level executives — from the departure of its COO to the recent loss of one of its top data center execs — has left onlookers scratching their heads.

*This story has been updated to include the fact that Zoph was fired from Thinking Machines. *