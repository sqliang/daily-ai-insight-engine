---
title: Robot hand company settles Tesla trade secret suit and announces $11M raise
source: https://techcrunch.com/2026/06/29/robot-hand-company-settles-tesla-trade-secret-suit-and-announces-11m-raise/
author:
- '[[Sean O''Kane]]'
published: '2026-06-29'
created: '2026-06-30'
description: 'The startup, Proception, is taking a unique approach to collecting training
  data to tackle one of the hardest problems in robotics: hands.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ef9ac98c9d795aaf
manifest_dates:
- '2026-06-30'
source_type: news_media
tldr: Proception 与特斯拉达成和解并完成 1100 万美元种子轮融资，专注高灵巧度机器人手研发
objective_summary: 前特斯拉 Optimus 技术负责人 Jay Li 创办的 Proception 与特斯拉就商业机密诉讼达成和解。该公司同期宣布完成
  1100 万美元种子轮融资，由 First Round Capital 领投，Y Combinator 和 BoxGroup 参投，
event_type: capital_movement
epistemic_status: verified_fact
entities:
  companies:
  - Proception
  - Tesla
  - First Round Capital
  - Y Combinator
  - BoxGroup
  - Northwestern University
  technologies: []
  key_people:
  - Jay Li
  - Elon Musk
  - Kevin Lynch
key_logic_flow:
- 前特斯拉 Optimus 项目技术负责人 Jay Li 被前雇主指控窃取商业机密以创办 Proception，双方经过数月法律交锋后于本月达成和解，特斯拉撤销诉讼。
- Proception 宣布完成 1100 万美元种子轮融资，由 First Round Capital 领投，Y Combinator 和 BoxGroup 参投。
- Proception 已开始向研究机构和机器人公司交付首批高灵巧度机械手，并开放更大规模订单，目标是成为其他机器人公司的手部供应商。
- Jay Li 认为当前机器人手部训练主要依赖遥操作方式，但该方式存在遥操作者无法获得触觉反馈且受限于可用机器人数量两大缺陷，Proception 采用不同的数据采集方法以加速研发。
extract_result: success
impact_score:
  score: 4.5
  reason: 该事件是机器人灵巧手细分领域的一家早期创业公司的融资和诉讼和解新闻，涉及金额仅1100万美元种子轮。虽然灵巧操作是具身智能领域的公认难题，且特斯拉和解消除了该公司的重大法律障碍，但Proception目前仍处于早期发货阶段，尚未证明其技术路线的规模化可行性。该事件对整体AI/机器人行业的影响有限，属于细分赛道的局部进展，不足以改变行业竞争格局。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: Proception的灵巧手实际性能指标和数据采集方法与主流遥操作路线的对比
hype_assessment:
  level: low
  reason: 文章是TechCrunch的客观报道，没有使用'颠覆性'、'革命性'等夸张用语。创始人坦承被特斯拉起诉是'压力测试'，且引用了第三方专家（西北大学Kevin
    Lynch）关于灵巧手仍需十年才能达到人类水平的保守估计，形成了合理的叙事平衡。融资额和交付规模也都在合理范围内，无明显概念炒作。
information_entropy: medium
domain_disruption:
  technical_innovation: Proception提出了不同于主流遥操作路线的数据采集方法，创始人指出遥操作存在两大缺陷：操作者无法获得触觉反馈、受限于可用机器人数量。但文章未披露其替代方案的具体技术细节，缺乏可评估的技术创新内容。灵巧手硬件本身的高自由度设计是实现类人操作的前提，但这属于行业内已有共识的技术方向。
  business_model: Proception定位为其他机器人公司的手部供应商，采用垂直模块化供应策略而非整机竞争。这种'机器人的机器人供应商'模式若成功，可降低整个行业进入灵巧操作领域的硬件门槛，形成类似'Intel
    Inside'的平台化效应，让下游机器人公司专注躯干、导航和上层AI，而将手部难题外包。
engineering_complexity: prototype
compound_value:
  score: 6.5
  reason: Proception 定位为机器人行业的'手部供应商'，是典型的 picks-and-shovels 商业模式。中长期复利逻辑有三层：1）行业贝塔红利——无论哪家机器人公司最终胜出，只要行业增长、人手级灵巧操作成为刚需，Proception
    作为上游组件商都能受益；2）硬件迭代飞轮——出货量积累带来制造工艺改进和成本下降，形成对后发者的先发优势；3）数据护城河——手部部署越多，采集的灵巧操作数据越多，可反哺下一代硬件设计和控制算法。但需保持谨慎：灵巧操作是业界公认最难的技术问题之一（西北大学预计仍需十年），种子轮
    1100 万美元在硬件赛道中偏小，且面临 Tesla Optimus、Figure 等垂直整合巨头的自研替代风险。评分 6.5 反映'细分赛道基础设施潜力存在，但技术和商业化风险仍高，需持续验证'。
value_capture_layer: hardware_compute
moat_impact: democratizes_access
key_beneficiaries:
- Proception
- First Round Capital
- Figure AI
- Agility Robotics
- 1X Technologies
competitive_casualty:
- Tesla (Optimus项目)
- Shadow Robot Company
- 垂直整合型人形机器人公司
- 传统工业机器人厂商(FANUC/ABB)
market_opportunities:
- 机器人灵巧手独立供应商模式已验证商业模式，创业者可关注机器人核心部件（灵巧手、触觉传感器、关节模组）的模块化供应机会，抓住人形机器人产业链分工红利
- Proception 的非纯遥操作数据采集方法为机器人训练开辟新思路，建议机器人训练平台企业和具身智能公司探索融合多种数据源（触觉反馈、自主探索等）的训练方案
- 投资者可关注机器人灵巧操作赛道中具备差异化技术路径（非纯遥操作、多模态数据融合）的早期项目，该细分领域存在被巨头忽视的结构性机会
risk_matrix:
  regulatory: 特斯拉商业机密诉讼虽已和解，但和解条款可能包含技术使用范围限制或竞业约束，影响 Proception 后续技术演进方向；先进机器人硬件出口管制政策可能限制其海外市场拓展
  technological: 高灵巧度机器人手被学界和业界公认为'十年难题'，Proception 宣称能大幅缩短这一周期但缺乏公开技术验证，存在技术承诺过度、交付不及预期的风险；其差异化数据采集方法尚未被同行复现或认可
  competitive: 特斯拉 Optimus 项目自研手部形成直接竞争，Shadow Robot 等老牌灵巧手公司已有多年的产品积累，中国供应链企业可能以更低成本快速跟进，导致价格竞争和利润空间挤压
  ethical: 高灵巧度机器人手是推动人形机器人进入制造业的关键瓶颈，一旦突破将加速制造业岗位替代，引发就业冲击与社会公平讨论
  additional:
  - 关键人物风险：创始人 Jay Li 是核心技术灵魂，团队依赖度过高；规模化量产能力尚未验证，从实验室原型到批量交付存在巨大制造鸿沟；1100 万美元种子轮资金有限，面对长期技术攻坚可能面临资金耗尽风险
confidence:
  impact: medium
  compound: medium
  hype: medium
actionable_insight: monitor
---

Jay Li doesn’t recommend getting sued by Tesla if you’re trying to get a startup off the ground. But he does think his company, Proception, might be better off for having endured the experience.

“I think it’s kind of like a resilience test, or pressure test,” he told TechCrunch in an exclusive interview. “People say that what doesn’t kill you makes you stronger, right?”

Li, who was a technical lead on Tesla’s Optimus humanoid robot program, was accused by his former employer last year of absconding with trade secrets to start Proception. But after months of trading legal blows, he finally reached a settlement with Tesla, which dismissed the lawsuit earlier this month. (Tesla did not respond to a request for comment.)

Now Li is free to tackle what he thinks is an even harder problem: making robot hands work like a human’s.

To help do that, Proception announced Monday that it has raised an $11 million seed round led by First Round Capital, with contributions from Y Combinator and early-stage fund BoxGroup.

Proception also announced Monday that it is shipping the first batch of its “high-dexterity robotic hand” to “researchers and robotics companies,” while opening up to wider orders. The goal, Li said, is to become the top hand supplier to other companies that don’t want to spend the time or resources developing what’s known in the industry as “dexterous manipulation.”

While there’s been an avalanche of money and attention rushing into the world of robotics, Li believes not enough of that has gone to making robotic hands truly mimic a human’s hands.

One of the loudest voices talking about this challenge has actually been his old boss, Tesla CEO Elon Musk, who has said robot hands are one of the biggest engineering problems yet to be solved.

While Musk has maintained that Optimus robots could start working in factories in a matter of years, the consensus view is that making robotic hands equivalent to a human’s is still many years away. Kevin Lynch, the director of Northwestern University’s Center for Robotics and Biosystems, told the Wall Street Journal last year that his team believes it will be a decade until they are “functional and useful and able to do some of the things that humans do.”

Li thinks Proception can do it much faster, in large part because of how they’re collecting data.

Most companies training humanoid robots right now are using teleoperators to train their systems. A human wearing a virtual-reality headset is able to see what a robot sees and manipulate what’s in front of that robot, then the robot can learn from the commands given by the human.

A big drawback to this approach, according to Li, is that the teleoperator is not receiving feedback from the objects the robot is touching. This approach is also limited to the number of robots a company has available at any given moment, Li said.