---
title: Why Google’s AI can’t spell Google (or anything else)
source: https://techcrunch.com/2026/05/27/why-googles-ai-cant-spell-google-or-anything-else/
author:
- '[[Amanda Silberling]]'
published: '2026-05-28'
created: '2026-05-28'
description: Google is embarrassing itself, again.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 5e8c5bd85baeaf02
source_type: news_media
tldr: Google AI Overview因token架构缺陷无法正确拼写单词，连"Google"都拼错，研究人员认为该问题难以根除。
objective_summary: 2026年5月，Google搜索中集成的新版AI Overview再次出现严重拼写错误，无法正确统计单词中的字母数量或拼写单词。Google向TechCrunch承认LLM在单词内计数字母是一个已知挑战，并表示正在修复。AI研究员Matthew
  Guzdial解释了根本原因：LLM基于token而非
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Google
  - TechCrunch
  - The Onion
  - Reddit
  - University of Alberta
  technologies:
  - LLM
  - Transformer
  - tokenization
  - AI Overview
  - generative AI
  key_people:
  - Matthew Guzdial
key_logic_flow:
- Google在2026年5月将其旗舰搜索引擎全面转向以AI Overview为核心，但新版AI Overview出现基础性拼写错误，例如无法正确计数单词中的字母数量、将"Trump"拼为"t-r-p-u-m"
- 这并非Google首次在AI Overview上出问题——第一版曾引用The Onion和Reddit的讽刺帖文，建议用户吃石头、在披萨上涂胶水
- Google向TechCrunch发表声明承认该问题，称"单词内计数字母是LLM的已知挑战，正在修复此特定问题"
- AI研究员Matthew Guzdial解释了根本技术原因：LLM基于Transformer架构将文字切分为token进行数值编码，模型不知道'T'、'H'、'E'这些单个字母的存在
- 研究人员对能否彻底解决LLM的拼写问题持悲观态度，认为基于token的架构从根本上限制了模型对字母级别的理解能力
impact_score:
  score: 5.5
  reason: Google 搜索是日活数十亿的旗舰产品，AI Overview 在基础拼写任务上系统性失败，直接动摇了用户对 Google AI-first
    搜索战略的信任，并可能延缓企业级 AI 应用的采纳节奏。但评分不更高的原因是：token 架构无法理解字符级操作这一局限在学术界早已是共识，事件本身并未揭示新的技术问题，更多是产品部署决策失误的暴露——将一个已知存在根本性缺陷的系统推向十亿级用户前台。
sentiment: negative
developer_sentiment:
  tone: skeptical
  primary_focus: 明知 token 架构存在字符级理解的根本缺陷，仍将 AI Overview 强行推为搜索引擎核心——产品决策与工程现实的严重脱节
hype_assessment:
  level: low
  reason: 文章引用 Google 官方声明和阿尔伯塔大学研究员的原话，从 Transformer tokenization 编码机制层面解释了拼写错误的根因，未使用'颠覆''革命性'等
    PR 话术，且明确传达了研究者对问题可解性的悲观态度，整体报道偏技术务实而非炒作。
information_entropy: medium
domain_disruption:
  technical_innovation: 无新突破。事件反而印证了 Transformer token-based 架构在字符级粒度任务上的固有天花板——模型将文本编码为
    token 的数值表示后，完全丢失了单个字母'T'、'H'、'E'的存在信息。这一局限自 Transformer 诞生以来一直存在，Google 的失败只是将其暴露在最大规模的消费级场景中。
  business_model: Google 将 AI Overview 作为其 29 年历史搜索引擎的新核心界面，本质上是将广告驱动的搜索商业模式押注在生成式
    AI 的可靠性上。拼写错误暴露的系统性缺陷意味着：若无法根治，Google 面临两种不利选择——回退到传统搜索链接模式（承认 AI 战略受挫），或继续容忍
    AI 输出不可靠（侵蚀用户信任与广告主信心）。这对所有试图将 LLM 嵌入核心产品的企业都是一个警示案例。
engineering_complexity: production_ready
compound_value:
  score: 5.5
  reason: 该事件揭示的不是一个可修复的bug，而是Transformer token化架构的根属性缺陷——LLM无法理解字母级别信息，且研究者对此持悲观态度。这一结构性弱点具有长期复利意义：1）它将成为谷歌AI搜索全面转型的持续性摩擦源，每次拼写错误都在侵蚀用户信任；2）它为替代架构（字符感知模型、神经符号AI、混合检索方案）创造了持续的资本叙事和需求锚点；3）但它并非新发现，业界对'strawberry问题'已有多年认知，市场已部分定价这一局限。综合来看，该事件作为行业信号的长期价值高于其短期新闻价值，故给5.5分。
value_capture_layer: foundation_model
moat_impact: democratizes_access
key_beneficiaries:
- Anthropic
- OpenAI
- Perplexity AI
- 神经符号AI初创公司
- AI可观测性与测试工具厂商
competitive_casualty:
- Google
- 依赖AI Overview类功能的搜索引擎
- 高精度文本生成场景的LLM部署方
market_opportunities:
- AI输出后处理与拼写校验层的创业机会：鉴于LLM在token级别存在根本性拼写缺陷且短期内难以根除，可开发轻量级拼写/计数校验中间件，作为LLM输出管道的最后一道闸门，面向搜索引擎、客服机器人等对准确性要求高的场景提供服务
- 字符级（character-level）或混合架构模型的研发窗口：当前Transformer token化架构的局限性已被Google事件充分暴露，具备差异化架构（如字节级建模、符号推理与神经网络混合系统）的AI公司可借此获得资本市场和客户关注，建议关注该方向的论文和初创公司
- AI搜索可靠性评测工具的创业方向：Google AI Overview连续两次重大翻车暴露出AI搜索引擎缺乏系统性可靠性评测，可开发面向AI搜索产品的自动化评测平台，覆盖事实准确性、拼写正确性、来源可信度等维度，为企业采购或监管合规提供第三方认证服务
risk_matrix:
  regulatory: 欧盟《AI法案》可能将搜索引擎集成的生成式AI归类为高风险应用（涉及信息检索与公共知识获取），Google AI Overview的反复出错可能加速监管机构对AI搜索的合规审查；此外，搜索结果中出现错误拼写和虚假信息可能触发各国消费者保护法和反虚假信息法规的调查
  technological: Transformer的token化架构从根本上限制了对字母级别的理解能力，研究人员对能否彻底解决持悲观态度，这意味着当前主流LLM架构在精确文字处理场景存在天花板；若Google无法有效修复，可能引发行业对纯token架构的信任危机，加速替代架构（如字节级语言模型、检索增强生成结合规则引擎）的研发竞赛
  competitive: Google将AI Overview作为29年旗舰搜索产品的核心进行押注，连续两次重大翻车直接动摇用户对其搜索可靠性的信任，为Perplexity、OpenAI（ChatGPT
    Search）、Microsoft Copilot等竞争对手创造了差异化窗口；若拼写等基础问题长期无法解决，Google搜索的市场份额可能受到实质性侵蚀
  ethical: AI Overview的错误输出并非仅限于娱乐性拼写错误——第一版曾引用讽刺网站建议用户吃石头、在披萨上涂胶水，新版则在搜索'd disregard'时返回AI对话残片而非词典定义，这些错误可能对缺乏判断力的用户造成实际伤害；同时，Google作为全球最大搜索引擎在AI输出中传播错误信息，构成系统性的信息生态风险
  additional:
  - 品牌声誉风险：Google搜索是其核心收入来源，AI Overview的反复失败已形成负面舆论惯性，修复成本高昂且每轮修复周期都在持续消耗用户信任
  - 广告商业模型风险：若用户因AI Overview不可靠而减少搜索使用或转向竞品，将直接影响Google的搜索广告收入基本盘
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
---

How many Ps are in Google? According to Google, there are two.

There’s also is also “exactly 1 ‘r’ in the word ‘poop’,” Google’s AI Overview says, as well as two ‘d’s in the word journalism, yet spelled it: j-o-u-r-n-a-d-i-s-m. Google did at least identify that there is one P in the last name of the U.S. president, but spelled it as t-r-p-u-m.

You didn’t need to be a prophet to predict that Google’s AI-forward Search overhaul was going to go over poorly. We’ve done this before. The first time Google added AI Overviews to Search, the feature ended up citing satirical posts from The Onion and Reddit, advising people to eat rocks and put glue on their pizza.

This time around, as Google doubles down on its commitment to make generative AI the centerpiece of its 29-year-old flagship product, it’s not surprising to see it stumble.

“Counting within words has been a known challenge for LLMs, and we’re working to fix this particular issue,” Google told TechCrunch in an emailed statement.

These basic spelling errors may seem familiar. LLMs, the kind of artificial intelligence that powers chatbots and other text-generators, are not built to understand spelling. It’s been a running joke for years that whenever a company unveils a new AI model, you should ask it how many ‘r’s are in the word strawberry. These AI models — which can code an app in seconds, or solve problems that have stumped mathematicians for decades — are about as good as a kindergartener at spelling.

Google’s AI overview woes reach beyond silly spelling mistakes though. Google already patched an issue from last week in which searching the word “disregard” would yield what looked like a dictionary definition of the word, only the definition was shown as, “Understood. Let me know whenever you have a new prompt or question!” But these spelling errors have remained amusing because they’re so difficult to quash.

As researchers have previously explained when we’ve asked about these spelling conundrums, AI doesn’t perceive sentences as units of language made up of words and letters. Many LLMs are built on transformers models, which break down text into tokens, which can be full words, syllables, or letters, depending on the model. Instead of “reading” like a human would, the AI converts the text into numerical representations of itself, which are then contextualized to help the AI come up with a logical response.

“LLMs are based on this transformer architecture, which notably is not actually reading text. What happens when you input a prompt is that it’s translated into an encoding,” Matthew Guzdial, an AI researcher and assistant professor at the University of Alberta, told TechCrunch. “When it sees the word ‘the,’ it has this one encoding of what ‘the’ means, but it does not know about ‘T,’ ‘H,’ ‘E.’”

The token-based architecture that powers LLMs like Google’s AI overview is inherently limiting, and researchers haven’t been optimistic that they can solve the spelling problem.