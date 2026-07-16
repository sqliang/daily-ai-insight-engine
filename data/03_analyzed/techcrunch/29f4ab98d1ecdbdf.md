---
title: Hack suggests AI music generator Suno scraped YouTube for training data
source: https://techcrunch.com/2026/07/15/hack-suggests-ai-music-generator-suno-scraped-youtube-for-training-data/
author:
- '[[Amanda Silberling]]'
published: '2026-07-15'
created: '2026-07-16'
manifest_dates:
- '2026-07-16'
description: The hacker used an employee's credentials to access source code, which
  revealed how Suno scraped decades of audio.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 29f4ab98d1ecdbdf
source_type: news_media
tldr: AI音乐生成器Suno遭供应链攻击，黑客获取员工凭证后访问了源代码，声称找到了Suno从YouTube Music、Deezer、Genius等平台抓取数十年音频数据用于AI训练的证据。Suno未告知用户此次数据泄露，并称事件已快速控制。
objective_summary: 2025年11月，AI音乐生成器Suno遭到供应链攻击，黑客通过入侵获取了员工凭证，进而访问了公司源代码。根据404 Media报道，源代码显示Suno疑似从YouTube
  Music、Deezer、Genius、库存音乐库和播客RSS抓取了数十年音频数据用于训练AI模型。Suno此前承认使用公开网络上的音乐文件训练AI，并主张合理使用原则。三大唱片公司正在起诉Suno，指控其违反DMCA故意绕过YouTube的反抓取保护措施。黑客还获取了客户邮箱、电话号码和Stripe中的部分信用卡号。Suno未通知用户此次泄露，仅称其为一次已快速控制的有限安全事件。
event_type: policy_and_safety
epistemic_status: rumor_leak
entities:
  companies:
  - Suno
  - YouTube
  - Deezer
  - Genius
  - Google
  - Stripe
  - 404 Media
  technologies: []
  key_people: []
key_logic_flow:
- Suno在2025年11月遭供应链攻击，黑客通过入侵员工凭证获取了源代码访问权限。
- 源代码显示Suno疑似从YouTube Music、Deezer、Genius、库存音乐库和播客RSS抓取了数十年音频数据用于AI训练。
- 三大唱片公司正在起诉Suno，指控其违反DMCA故意绕过YouTube的反抓取保护措施，并违反YouTube服务条款。
- 黑客还获取了客户数据，包括邮箱、电话号码和Stripe中的部分信用卡号。
- Suno未向客户通报此次数据泄露，仅声称是一次已快速控制的有限安全事件。
- 竞争对手Udio也面临类似的YouTube数据抓取指控，Google同样因版权侵权被多家出版商起诉。
object_mentions:
- object_type: product
  name: Suno
  canonical_name: Suno AI
  url: https://suno.com
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 文章以Suno被黑客攻击为核心事件展开报道。
  - 文章详细描述Suno被指控从YouTube等平台抓取音频数据用于训练AI。
  - 三大唱片公司正在起诉Suno，指控其违反DMCA。
  article_id: 29f4ab98d1ecdbdf
- object_type: product
  name: Udio
  canonical_name: Udio
  url: https://udio.com
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章提到Suno的竞争对手Udio也被指控抓取YouTube数据。
  article_id: 29f4ab98d1ecdbdf
- object_type: product
  name: 404 Media
  canonical_name: 404 Media
  url: https://www.404media.co
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 黑客向404 Media提供了入侵细节和证据。
  - 文章说明报道来源为404 Media的调查报道。
  article_id: 29f4ab98d1ecdbdf
extract_result: success
impact_score:
  score: 6.0
  reason: 该事件结合了供应链安全漏洞与AI训练数据合规两个敏感议题。Suno作为AI音乐生成领域的头部玩家，其源代码泄露直接证实了业界普遍怀疑但难以证实的音乐平台数据爬取行为，可能加速监管机构对AI训练数据来源的审查，并影响三大唱片公司正在进行的诉讼走向。客户数据泄露（含部分信用卡号）也暴露了AI初创公司在安全合规上的短板。不过该事件对AI行业整体的范式性影响有限，主要冲击集中在对AI音乐生成子领域的信任重塑和合规要求提升上，属于改变局部竞争格局的级别。
sentiment: negative
developer_sentiment:
  tone: skeptical
  primary_focus: Suno训练数据爬取行为是否构成DMCA违规，以及供应链攻击暴露的AI初创公司安全防护缺失
hype_assessment:
  level: low
  reason: 该报道源自404 Media的调查报道，以黑客提供的源代码截图作为证据支撑，属于事实性新闻报道而非企业PR宣传。文中援引了正在进行的三大唱片公司诉讼、DMCA法律条款、YouTube服务条款等具体法律依据，措辞严谨，没有使用'颠覆性''革命性'等PR滥用词汇，可信度较高。
information_entropy: medium
domain_disruption:
  technical_innovation: 无。本次事件是一次供应链攻击引发的源代码泄露，本身不构成技术突破。但泄露的代码可能揭示了Suno大规模音频爬取的技术架构实现，对业界了解AI音乐生成公司的数据收集工程实践有一定参考价值。
  business_model: 若唱片公司在诉讼中胜诉，将严重冲击AI音乐生成公司依赖'合理使用'条款爬取公开音乐数据的商业模式基础，迫使整个行业转向授权数据来源或自研合成数据方案。同时，此次安全事件暴露的数据保护缺失可能使用户对AI音乐平台产生信任危机。
engineering_complexity: production_ready
compound_value:
  score: 2.5
  reason: Suno 的核心商业模式建立在抓取大规模音频数据训练 AI 模型上，此次供应链攻击曝光了其训练数据来源（YouTube Music、Deezer、Genius
    等）的系统性合规风险，叠加三大唱片公司的 DMCA 诉讼和客户数据泄露未告知的监管风险，使其面临法律、声誉和运营三重危机。从 VC 视角看：第一，法律风险极高——如果法院认定故意绕过
    YouTube 反爬措施构成 DMCA 违法，Suno 可能面临巨额赔偿甚至被强制删除训练数据，商业模式根基动摇；第二，数据泄露未告知客户暴露了安全治理和企业道德的严重缺陷，可能导致用户流失和监管罚款；第三，竞争格局恶化——竞争对手
    Udio 同样面临类似指控，但 Suno 作为行业领先者承受了主要火力。长期复利价值极低，存活概率显著下降，除非能快速达成庭外和解并获得授权，否则 3-5
    年内大概率不复存在或被迫转型。
value_capture_layer: end_application
moat_impact: creates_new_moat
key_beneficiaries:
- 三大唱片公司（索尼音乐、环球音乐、华纳音乐）
- YouTube/Google
- 已获得合法授权的音乐 AI 公司
competitive_casualty:
- Suno
- Udio
- 其他依赖未授权数据训练的 AI 音乐生成创业公司
market_opportunities:
- AI训练数据溯源与合规审计工具——随着唱片公司起诉Suno等案件增多，市场需要能够自动扫描模型训练数据来源并生成合规报告的技术方案
- 面向AI公司的供应链安全检测服务——Suno因供应链攻击导致源码泄露，针对AI初创企业的员工凭证管理、第三方依赖审计和入侵检测产品存在明确需求
- 正版授权AI音乐生成解决方案——与音乐版权方合作获取合法授权数据训练的AI音乐工具，可作为市场差异化竞争点切入企业级音频创作场景
risk_matrix:
  regulatory: 三大唱片公司正在起诉Suno违反DMCA故意绕过YouTube反抓取保护，黑客窃取的信用卡号涉及GDPR/CCPA等数据保护法规的合规义务，Suno未通知用户泄露事件可能面临监管处罚
  technological: 供应链攻击暴露了AI公司源代码托管与员工凭证管理的薄弱环节，源码泄露披露的数据抓取手法（YouTube/Deezer/Genius）可能导致反爬措施全面升级，增加未来AI数据采集的技术成本
  competitive: 音乐版权行业联合对AI生成音乐展开法律围剿，Suno和Udio均面临类似诉讼可能拖垮初创企业；Google母公司同样面临版权诉讼，行业生态存在系统性收紧风险
  ethical: 客户邮箱、电话号码和信用卡号遭泄露且公司未主动通知用户，存在严重的隐私保护失责；未标注来源的版权数据用于模型训练涉及对原创作者的权益侵害
  additional:
  - 供应链攻击传播链不明确，黑客可能进一步利用窃取的凭证渗透上下游合作伙伴系统
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: Suno
  canonical_name: Suno AI
  url: https://suno.com
  positioning: AI音乐生成器，用户通过文本提示和歌词生成完整音乐作品
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI音乐创作者
  - 音乐制作人
  - 内容创作者
  - 普通用户探索音乐生成
  product_signal: 支持文本到音乐生成，但源代码泄露显示其训练数据依赖从YouTube Music、Deezer、Genius等平台大规模抓取，数据合规性存疑
  market_signal: 2025年11月遭供应链攻击，黑客获取源代码并发现大规模数据抓取证据；三大唱片公司正在起诉Suno违反DMCA故意绕过YouTube反抓取保护；客户邮箱、电话、部分信用卡号在泄露中被获取，公司未通知用户
  differentiation: 生成式AI音乐领域的标志性产品之一，但训练数据合法性争议相比竞争对手更为突出，面临直接的法律诉讼
  watch_reason: 供应链攻击暴露了Suno的训练数据来源和内部架构，版权诉讼结果可能为AI音乐行业确立数据合规的先例；数据泄露未通知用户带来隐私监管风险，值得持续跟踪诉讼进展和产品应对策略
  risk_notes:
  - 三大唱片公司DMCA诉讼可能导致业务模式被迫调整
  - 数据泄露未通知用户存在GDPR/CCPA等隐私法规合规风险
  - 训练数据来源合法性受质疑，合理使用辩护尚未获法院认可
  - 源代码暴露可能带来后续安全攻击面
  score: 8.0
  article_ids:
  - 29f4ab98d1ecdbdf
  evidence_snippets:
  - 文章以Suno被黑客攻击为核心事件展开报道。
  - 文章详细描述Suno被指控从YouTube等平台抓取音频数据用于训练AI。
  - 三大唱片公司正在起诉Suno，指控其违反DMCA。
  - 黑客获取了客户数据包括邮箱、电话号码和Stripe中的部分信用卡号。
  - Suno未向客户通报此次数据泄露。
- object_type: product
  name: Udio
  canonical_name: Udio
  url: https://udio.com
  positioning: AI音乐生成器，Suno的直接竞争对手
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI音乐创作者
  - 音乐制作人
  product_signal: 与Suno类似提供AI音乐生成能力，也被指控从YouTube抓取训练数据
  market_signal: 被指控抓取YouTube数据，面临与Suno相似的版权争议，但未提及具体诉讼进展
  differentiation: Suno的主要竞品，二者面临相同的训练数据合规性质疑，行业整体监管风险同步上升
  watch_reason: 与Suno面临相同的数据抓取指控，版权诉讼若对Suno不利将直接连锁影响Udio的业务合法性
  risk_notes:
  - 面临与Suno类似的数据抓取和版权指控，风险高度关联
  - 行业监管收紧可能影响整体AI音乐赛道
  score: 5.0
  article_ids:
  - 29f4ab98d1ecdbdf
  evidence_snippets:
  - 文章提到Suno的竞争对手Udio也被指控抓取YouTube数据。
- object_type: product
  name: 404 Media
  canonical_name: 404 Media
  url: https://www.404media.co
  positioning: 专注科技行业的深度调查新闻媒体
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 科技行业从业者
  - 调查研究人员
  - 关注AI与数字权利议题的读者
  product_signal: 深度调查报道能力，在此次事件中作为独家曝光渠道，黑客主动向其提供入侵细节和源代码证据
  market_signal: 作为Suno黑客事件的独家报道渠道，展示了其在科技调查新闻领域的影响力和信源获取能力
  differentiation: 与主流科技媒体不同，404 Media专注于深度调查和黑客/安全事件的独家报道，在此次事件中证明了其作为安全事件信息枢纽的价值
  watch_reason: 作为安全事件的独家报道来源，404 Media在AI行业安全事件的信息分发中扮演越来越重要的角色
  risk_notes: []
  score: 4.0
  article_ids:
  - 29f4ab98d1ecdbdf
  evidence_snippets:
  - 黑客向404 Media提供了入侵细节和证据。
  - 文章说明报道来源为404 Media的调查报道。
---

The AI music generator Suno was hacked, according to a report from 404 Media.

The hacker told the publication that they used a supply chain attack in November to access an employee’s credentials, allowing them to then access source code showing how Suno allegedly scraped decades of audio from YouTube Music, Deezer, Genius, stock music libraries, and podcast RSS feeds.

Suno previously admitted that it trains its AI on “publicly available music files” on the open internet, arguing that it can train on copyrighted material under the fair use doctrine, a subjective carve-out of copyright law. But according to the major record labels actively suing Suno, it is illegal under the Digital Millennium Copyright Act (DMCA) to deliberately circumvent YouTube’s protections against data scraping; it also violates YouTube’s terms of service.

Udio, a competitor to Suno, has also been accused of scraping YouTube data. Google, the parent company of YouTube, faces similar allegations of copyright infringement from a variety of major book publishers.

The hacker reportedly accessed customer data including customer emails, phone numbers, and partial credit card numbers in Stripe.

Suno did not notify customers about the November 2025 breach and claims that this was a “limited security incident that was quickly contained.”