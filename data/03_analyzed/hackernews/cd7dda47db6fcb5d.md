---
title: H.R. 6028 would fundamentally change the U.S. Copyright Office
source: https://www.eff.org/deeplinks/2026/06/congress-just-rushed-through-disastrous-copyright-office-overhaul
author:
- '[[Cider9986]]'
published: '2026-06-11'
created: '2026-06-13'
description: 'Article URL: https://www.eff.org/deeplinks/2026/06/congress-just-rushed-through-disastrous-copyright-office-overhaul
  Comments URL: https://news.ycombinator.com/item?id=48484496 Points: 212 # Comments:
  66'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: cd7dda47db6fcb5d
source_type: community_discussion
tldr: 美众议院通过H.R. 6028法案，重组版权局并削弱国会图书馆监督权，遭EFF反对
objective_summary: 美国众议院以口头表决通过H.R. 6028法案，取消国会图书馆对版权局的监督权，将版权局局长改为总统任命、参议院确认的职位，并将DMCA第1201条规则制定权转移至版权局局长。EFF批评该法案使版权局更政治化且未经听证会快速通过，呼吁参议院否决。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - EFF
  - Library of Congress
  - U.S. Copyright Office
  - U.S. House of Representatives
  - U.S. Senate
  technologies:
  - AI
  - DMCA
  key_people: []
key_logic_flow:
- 美国众议院以口头表决方式通过了H.R. 6028法案，该法案表面上是技术性机构重组，实则大幅改变美国版权局的结构。
- 法案取消国会图书馆对版权局的监督职能，将版权局局长改为由总统任命、参议院确认的政治任命职位。
- 法案将DMCA第1201条规则制定权从国会图书馆馆长移交给版权局局长，进一步集中权力于版权局内部。
- EFF指出该法案未经任何听证会或实质性审议即被快速推进，缺乏必要的公众监督和辩论。
- EFF批评版权局此前在AI合理使用报告和SOPA等议题上已偏向大型娱乐产业利益，新法案将使其更加政治化。
- EFF呼吁参议院否决该法案，认为版权机构应服务公共利益，而非总统行政部门或行业游说者。
impact_score:
  score: 6.5
  reason: 该法案从根本上重组美国版权局，将局长改为总统任命制并削弱国会图书馆监督权。对AI行业而言，版权局此前在AI合理使用报告上已偏向保守立场（偏向私有许可市场而非用户权利），新法案将进一步政治化该机构，使AI训练数据的合理使用判定更易受娱乐产业游说影响，可能加速出台对AI公司不利的版权政策。DMCA第1201条规则制定权移交也直接影响AI安全研究。虽非范式转移，但该结构性变化将长期塑造AI版权监管环境，重要性被市场低估。
sentiment: negative
developer_sentiment:
  tone: skeptical
  primary_focus: 版权局政治化将损害AI合理使用和训练数据的法律确定性
hype_assessment:
  level: low
  reason: 本文为EFF的政策分析文章，核心内容为已通过众议院的真实法案（H.R. 6028），无任何技术或产品炒作词汇。文章基于具体立法条款、历史先例（SOPA、AI报告）和程序瑕疵（未经听证会）进行事实性批评，没有使用'颠覆''革命性'等PR用语。
information_entropy: high
domain_disruption:
  technical_innovation: 无（纯政策/立法事件，非技术突破）
  business_model: 版权局政治化将改变AI行业的版权合规风险格局：局长改为总统政治任命后，AI训练数据的合理使用边界将更受行政当局和娱乐产业游说影响，不确定性增加。AI公司可能需要投入更多资源用于版权合规和游说，小型创业公司面临更高法律风险，可能加速行业整合。
engineering_complexity: conceptual
compound_value:
  score: 2.5
  reason: H.R. 6028 本质是一次版权监管架构的政治化重组，并非技术或商业模式创新，不具备价值复利效应。从 VC 视角评估：（1）该法案将版权局局长改为总统任命+参议院确认的政治职位，使版权政策更易受大型娱乐产业游说资本影响；（2）将
    DMCA 第 1201 条规则制定权从国会图书馆集中至版权局内部，削弱了以公共利益为使命的制衡力量；（3）对 AI 行业的核心冲击在于训练数据的合理使用（fair
    use）问题——版权局此前在 AI 报告中已倾向私人许可模式而非用户权利，新架构将加剧这一偏向，增加 AI 公司的合规风险和政策不确定性。该法案尚未通过参议院，最终落地存变数，但即便通过也是在存量利益格局上的权力再分配，不产生增量价值，因此评分低位。
value_capture_layer: foundation_model
moat_impact: strengthens_monopoly
key_beneficiaries:
- Disney
- Warner Bros. Discovery
- Sony Music
- Recording Industry Association of America (RIAA)
- Motion Picture Association (MPA)
competitive_casualty:
- 小型 AI 初创公司
- 开源 AI 社区
- 学术研究机构
- 安全研究人员
market_opportunities:
- AI企业与版权律师可提前布局对DMCA第1201条规则制定权移交后的合规策略，为涉及安全研究、模型逆向分析等场景准备法律应对方案
- 版权局政治化后，专注于AI合理使用辩护和著作权争议解决的第三方咨询机构将迎来需求增长
- 关注参议院审议进程，若法案未通过则说明公众监督力量有效，利好AI开源社区和合理使用倡导组织的维权协作产品
risk_matrix:
  regulatory: H.R. 6028将版权局局长改为总统任命/参议院确认的政治职位，并集中DMCA第1201条规则制定权于版权局内部，可能导致AI训练数据的合理使用空间被进一步压缩，版权局的AI合理使用报告已表现出偏向大型内容产业利益而非用户权利的倾向
  technological: DMCA第1201条规则制定权的集中可能限制安全研究、模型逆向工程、数字修复等AI相关技术活动的合法性，不利于AI安全社区的技术透明度建设
  competitive: 大型娱乐产业（内容版权方）将获得更强的政策游说杠杆，可能通过版权局施压AI公司，加剧AI训练数据获取成本，形成对中小AI企业的准入壁垒
  ethical: 国会图书馆的监督职能被削弱，原知识获取与公共利益的制衡机制弱化，可能影响学术研究、教育机构和文化保护项目对受版权保护材料的合理使用权利
  additional: []
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: monitor
---

In a voice vote earlier this week, the House of Representatives passed H.R. 6028, the “Legislative Branch Agencies Clarification Act.” The legislation is presented as a technical reorganization of some government agencies, but it’s much more than that.

H.R. 6028 would fundamentally change the U.S. Copyright Office, and not in a good way. The bill removes the Library of Congress’ current supervisory role over the Copyright Office, transfers several powers directly to the Register of Copyrights, and makes the Register a presidential appointee, confirmed by the Senate.

These changes would make an office that’s already hugely influential in copyright and tech policy much more political. EFF first explained why that’s a terrible idea when it came up nearly a decade ago. This bill, like the older one, weakens the few public-interest checks and balances that do exist. We hope the Senate promptly rejects this bill.

**The Copyright Office Doesn’t Need More Politics—Or More Power**

The Copyright Office's main responsibilities are administrative and advisory. It registers copyrights, maintains records, grows the Library of Congress’s collections, and provides expertise to Congress on copyright law. But over the past two decades, the Office has also become increasingly influential in copyright policy debates that affect free expression, libraries, educators, competition—and everyday internet users. Unfortunately, it has not been a neutral advocate. The office’s recent report on the role of AI severely bungled the issue of fair use, prioritizing private licensing market “solutions” over user rights.

Going further back, the Copyright Office supported one of the most infamous anti-internet proposals of all time—the Stop Online Piracy Act (SOPA), a disastrous internet censorship proposal that sparked one of the largest online protests in history. The Office has repeatedly advanced positions that favored large entertainment-industry interests over the public interest.

The Office also plays a major role in the Digital Millennium Copyright Act (DMCA) Section 1201 rulemaking process, which determines when the public may lawfully bypass digital locks for activities such as security research, repair, preservation, or accessibility. EFF has used this process repeatedly to mitigate some of the worst harms of the DMCA. H.R. 6028 would move rulemaking authority over 1201 from the Librarian of Congress to the Register of Copyrights, further consolidating power within the Copyright Office itself.

The bill also makes the Register of Copyrights a presidential appointee confirmed by the Senate. Each administration will be pressured to pick nominees aligned with their own policy preferences, and the powerful copyright owning industries will invest even more heavily in lobbying to get their way, and influence the selection. This position should be focused on administrative ability and actual expertise, not lobbying and politics.

**The Copyright Office Should Stay Connected To The Library of Congress**

H.R. 6028 would do more than change who appoints the Register of Copyrights. It would sever the Copyright Office from Library of Congress supervision and transfer many Librarian powers directly to the Register.

The supervisory relationship exists for good reason, as the nation’s libraries have pointed out for years. The Library, while far from perfect, at least has the mission of preserving and providing access to knowledge. That *should* be an important public-interest counterweight in copyright debates. Congress has not explained how weakening the ties between the Library and the Copyright Office would serve the public better, or even seriously inquired about it.

**This Bill Was Rushed Through**

Back in March, EFF joined Public Knowledge, the Center for Democracy and Technology, library organizations and tech groups, urging Congress *not* to fast-track this legislation. We told them changes to the Copyright Office will have major consequences for the “speech rights, educational opportunities, and creative freedoms of all Americans.”

Yet Congress moved forward without any hearings on the bill, and without meaningful examination. H.R. 6028 creates a years-long separation of the Copyright Office from the Library of Congress, transfers significant legal authority, and restructures the appointment process for the nation’s top copyright official. Changes like that deserve hearings, debate, and public scrutiny. H.R. 6028 got none of that.

**The Senate Should Stop This Bill**

Copyright law exists to serve the public and “promote the progress” of science and learning. The institutions that administer copyright law should do the same.

H.R. 6028 would move the Copyright Office further away from that goal. Congress should be strengthening public-interest oversight of copyright policymaking, not looking for ways to concentrate more authority in a single presidentially appointed official.

The Senate should reject H.R. 6028. The Copyright Office should serve the public—not presidential administrations, and not industry lobbyists.