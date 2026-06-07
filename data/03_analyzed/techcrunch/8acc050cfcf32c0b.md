---
title: NSA said to be readying Anthropic’s Mythos for use in cyber operations
source: https://techcrunch.com/2026/06/05/nsa-said-to-be-readying-anthropics-mythos-for-use-in-cyber-operations/
author:
- '[[Zack Whittaker]]'
published: '2026-06-05'
created: '2026-06-07'
description: The U.S. eavesdropping agency is reportedly preparing Anthropic's Mythos
  for use in cyberattacks, despite a federal ban on using the AI model maker.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 8acc050cfcf32c0b
source_type: news_media
tldr: 外媒称Anthropic向NSA派驻工程师协助使用其网络安全AI模型Mythos
objective_summary: Financial Times援引匿名消息称，Anthropic已向美国国家安全局派驻约6名工程师，协助其将前沿网络安全AI模型Mythos用于情报收集和网络攻击行动。此前Axios在4月报道NSA已在Mythos被联邦禁用的情况下使用该模型。
event_type: application_landing
epistemic_status: rumor_leak
entities:
  companies:
  - Anthropic
  - National Security Agency
  - Financial Times
  - Axios
  - Department of Defense
  technologies:
  - Mythos
  key_people: []
key_logic_flow:
- Financial Times援引匿名消息称，Anthropic已向美国国家安全局派驻约6名工程师，协助其使用Mythos模型进行网络情报收集和攻击行动。
- 目前尚不清楚这些工程师或Mythos模型是否已被积极用于NSA的黑客行动中。
- Axios在4月曾报道NSA已在使用Mythos，尽管该模型因联邦禁令被禁止使用。
- 美国国防部将Anthropic列为供应链风险，原因是Anthropic拒绝让政府将其模型用于大规模国内监控和自主武器系统。
- 各国政府正争相获取Mythos的访问权限，而Anthropic出于对其网络安全能力被滥用的担忧，已限制该模型的访问。
- NSA发言人拒绝对该报道置评，Anthropic也未回应置评请求。
impact_score:
  score: 6.5
  reason: 该事件标志着前沿AI安全模型首次被曝直接嵌入国家级情报与进攻性网络操作能力体系，对AI安全治理格局有重要信号意义。但事件尚处于匿名信源传闻阶段，缺乏官方确认或具体技术细节，且对AI行业生态（模型训练、API定价、开发者工具等）无直接冲击，因此评分为中等偏上而非颠覆级。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: AI网络安全模型的军事化应用与Anthropic安全立场的矛盾
hype_assessment:
  level: low
  reason: 报道来自Financial Times和Axios的匿名消息源，属于严肃新闻调查而非PR通稿。文本中未出现'颠覆''革命性'等夸大措辞，主要陈述事实性派驻安排和背景矛盾，无明显包装炒作。
information_entropy: medium
domain_disruption:
  technical_innovation: 核心创新不在模型技术本身，而在于前沿AI网络安全模型从学术/防御场景延伸到国家级进攻性网络操作的实际部署，标志着AI攻防能力在国家级对抗场景中的工程化落地。
  business_model: Anthropic 派出驻场工程师协助情报机构使用其模型，形成了'AI模型授权+驻场专业服务'的新型政府合作模式。各国政府争相获取Mythos访问权限，可能催生'国家级AI能力授权'这一独立商业赛道。
engineering_complexity: production_ready
compound_value:
  score: 8.5
  reason: 此事件标志着Anthropic从企业市场向国家级安全基础设施的关键跃迁。政府合同的特性是续约率高、合同周期长（通常3-5年起步）、议价能力弱（价格弹性低），一旦深度嵌入NSA的网安作战流程，将形成极强的数据飞轮——Mythos从真实国家级网络攻防中获得的反馈数据可反向提升模型能力，进一步拉大与竞品的差距。此外，国家安全领域的合规壁垒（安全审查、供应链认证）本身就是护城河，一旦建立很难被竞争者短期突破。最大的风险变量是Anthropic与DoD之间因伦理立场（拒绝用于大规模监控和自主武器）导致的供应链风险定性，这意味着政府收入可能伴随政策摇摆。但整体而言，国家级网络安全基础设施的复利效应极强，3-5年后若Mythos成为美国网安行动的标配，其价值难以被替代。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- Palantir
- 美国国防承包商生态系统
competitive_casualty:
- 传统网络安全厂商（CrowdStrike、Palo Alto Networks）
- 未获政府安全认证的AI基础模型厂商
- 开源网络安全AI方案
market_opportunities:
- 国防与情报部门的AI网络安全能力成为高增长赛道，安全合规型AI模型定制服务商可瞄准军工和政府客户
- AI模型供应链合规审计与安全评估服务需求激增，尤其是针对前沿模型在敏感场景下的滥用风险管控
- 政府级AI安全沙箱与访问控制基础设施存在市场空白，可开发支持细粒度权限管理和审计追踪的企业级AI部署平台
risk_matrix:
  regulatory: 联邦禁令被实质性绕过，Anthropic面临违反国防部供应链风险规定的法律追责风险；美国对前沿AI模型的出口管制和国内使用法规可能加速出台
  technological: Mythos的网络安全能力（漏洞发现、自动化攻击）若在NSA大规模部署，模型能力可能被对手方逆向推理或泄露，Anthropic的技术护城河面临扩散风险
  competitive: 其他AI Labs（OpenAI、Google DeepMind）可能被迫跟进与国防部门的合作，引发AI安全承诺的"竞次"效应；开源网络安全模型可能因政府自建能力而获得更多资源倾斜
  ethical: Anthropic此前以"不参与大规模监控和自主武器"为原则拒绝政府合作，如今转向协助NSA网络攻击，严重损害其AI安全品牌公信力；模型用于网络攻击可能间接造成平民基础设施受损的伦理困境
  additional:
  - 人才流失风险：Anthropic内部因安全/伦理路线分歧可能导致核心研究人员离职
  - 地缘政治风险：他国政府可能以此为理由加速自身AI军事化部署，引发全球AI军备竞赛升级
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
---

Anthropic has deployed around half-a-dozen engineers to the National Security Agency to help its spies use the company’s frontier cybersecurity AI model, Mythos, Financial Times reported, citing anonymous sources.

The engineers are reportedly tasked with helping the intelligence agency use Mythos for certain applications, the report said. However, it’s unclear if the engineers or Mythos are being actively used in the agency’s hacking operations.

The NSA is tasked with collecting intelligence from wiretaps, undersea cables, corporate partnerships, and other clandestine means, as well as conducting offensive cyberattacks on foreign adversaries.

FT’s report adds to earlier news from Axios, which reported in April that the NSA was using Mythos despite a federal ban on using Anthropic’s technology. That ban followed a decision by the Department of Defense to designate Anthropic a “supply-chain risk” in retaliation for not allowing the government to use its models for mass domestic surveillance and autonomous weapons.

The latest report comes as governments are scrambling to gain access to Mythos, which Anthropic claims it had to limit access to, fearing its cybersecurity capabilities could be exploited to discover security flaws and carry out hacks.

When reached by TechCrunch, a spokesperson for the NSA declined to confirm or deny the reporting. Anthropic did not respond to a request for comment.