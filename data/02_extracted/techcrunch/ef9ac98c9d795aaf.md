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
tldr: 前特斯拉Optimus技术负责人Jay Li创办的机器人手部公司Proception，与特斯拉的商业机密诉讼达成和解，同时宣布完成1100万美元种子轮融资并开始交付首批高灵巧度机器人手。
objective_summary: 2026年6月29日，Proception创始人Jay Li宣布与特斯拉就商业机密诉讼达成和解，特斯拉已于当月早些时候撤诉。同日，Proception宣布完成1100万美元种子轮融资，由First
  Round Capital领投，Y Combinator和BoxGroup参投，并开始向研究机构和机器人公司交付首批高灵巧度机器人手，同时开放更广泛订单。Li认为远程操作员训练方法存在触觉反馈缺失和机器人数量受限的缺陷，Proception的数据收集方式有望更快解决灵巧操作难题。
event_type: capital_movement
epistemic_status: verified_fact
entities:
  companies:
  - Tesla
  - Proception
  - First Round Capital
  - Y Combinator
  - BoxGroup
  technologies: []
  key_people:
  - Jay Li
  - Elon Musk
  - Kevin Lynch
key_logic_flow:
- 前特斯拉Optimus人形机器人项目技术负责人Jay Li创办了机器人手部公司Proception，被特斯拉起诉窃取商业机密。
- 经过数月法律交锋，Proception与特斯拉达成和解，特斯拉于2026年6月初撤诉。
- Proception宣布完成1100万美元种子轮融资，由First Round Capital领投，Y Combinator和BoxGroup参投。
- Proception开始向研究人员和机器人公司交付首批高灵巧度机器人手，并开放更广泛订单。
- Li认为当前行业普遍使用的远程操作员训练方法存在缺陷——操作员无法接收触觉反馈且受限于可用机器人数量。
- Proception的目标是成为机器人的手部供应商，让其他公司无需自行投入资源研发灵巧操作技术。
extract_result: success
object_mentions:
- object_type: company
  name: Proception
  canonical_name: Proception
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Proception由前特斯拉Optimus技术负责人Jay Li创办，被特斯拉起诉窃取商业机密后达成和解。
  - Proception宣布完成1100万美元种子轮融资，由First Round Capital领投，Y Combinator和BoxGroup参投。
  - Proception开始向研究人员和机器人公司交付首批高灵巧度机器人手，并开放更广泛订单。
  article_id: ef9ac98c9d795aaf
- object_type: product
  name: Proception high-dexterity robotic hand
  canonical_name: Proception高灵巧度机器人手
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Proception开始向研究人员和机器人公司交付首批高灵巧度机器人手，并开放更广泛订单。
  - 公司目标是成为其他公司的手部供应商，让对方无需自行研发灵巧操作技术。
  article_id: ef9ac98c9d795aaf
- object_type: project
  name: Tesla Optimus
  canonical_name: Tesla Optimus
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Jay Li曾是Tesla Optimus人形机器人项目的技术负责人，这是其被起诉的背景。
  - Elon Musk曾表示机器人手部是尚未解决的最大工程问题之一，Optimus机器人可能数年内进入工厂工作。
  article_id: ef9ac98c9d795aaf
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