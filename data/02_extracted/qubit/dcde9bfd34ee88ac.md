---
title: OceanBase发布AI数据库：以一套引擎融合湖库与多模态数据
source: https://www.qbitai.com/2026/06/439876.html
author:
- '[[量子位的朋友们]]'
published: '2026-06-29'
created: '2026-06-29'
description: 让AI真正“读懂”企业
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: dcde9bfd34ee88ac
manifest_dates:
- '2026-06-29'
- '2026-06-30'
source_type: news_media
tldr: OceanBase于2026年6月29日发布面向AI时代的湖库一体AI数据库，以一套引擎统一管理结构化、非结构化和向量数据，同步推出Lakebase、DataStudio、DataPilot三款产品，已在蚂蚁阿福、灵光等场景完成验证。
objective_summary: 2026年6月29日，OceanBase发布湖库一体的AI数据库，将数据湖、事务处理与多模态数据处理统一在同一引擎中。围绕该架构，OceanBase推出了Lakebase（底层引擎）、DataStudio（数据治理与编排）和DataPilot（企业智能入口）三款产品。相比传统多系统方案，整体TCO降低约30%-50%。该能力已在蚂蚁阿福和灵光两个AI场景完成验证，其中灵光累计生成数千万个闪应用。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - OceanBase
  - 蚂蚁集团
  technologies:
  - AI数据库
  - 湖库一体
  - 多模态数据
  - Lakebase
  - DataStudio
  - DataPilot
  key_people:
  - 杨传辉
  - 杨冰
key_logic_flow:
- OceanBase于2026年6月29日发布面向AI时代的湖库一体AI数据库，旨在帮助Agent一次获取完整业务上下文。
- OceanBase认为AI落地的真正瓶颈正在从模型转向数据，湖库一体架构可以通过统一引擎消除多系统割裂。
- OceanBase发布了三款产品：Lakebase作为底层引擎统一管理多模态数据，DataStudio负责数据治理与服务化，DataPilot作为企业业务智能入口。
- 相比传统多系统方案，OceanBase AI数据库可降低整体TCO约30%-50%。
- 该能力已在蚂蚁阿福和灵光等AI场景完成验证，其中灵光累计生成数千万个闪应用。
- OceanBase选择从数据库内核出发，将金融级事务一致性、高可用与弹性能力延伸至湖与多模态数据体系。
extract_result: success
object_mentions:
- object_type: product
  name: OceanBase AI数据库
  canonical_name: OceanBase AI数据库
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 6月29日，OceanBase发布面向AI时代的湖库一体AI数据库，提出以湖库一体为核心架构。
  - 相较传统多系统方案，OceanBase AI数据库可降低整体TCO约30%-50%。
  - 目前该能力已在蚂蚁阿福、灵光等场景完成验证，其中灵光累计生成数千万个闪应用。
  article_id: dcde9bfd34ee88ac
- object_type: product
  name: OceanBase Lakebase
  canonical_name: OceanBase Lakebase
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - OceanBase Lakebase作为底层引擎，让结构化数据、非结构化数据和向量数据在统一架构中被管理、加工、检索和调用。
  - Lakebase解决AI时代的数据底座问题，是OceanBase AI数据库的底层数据引擎。
  article_id: dcde9bfd34ee88ac
- object_type: product
  name: OceanBase DataStudio
  canonical_name: OceanBase DataStudio
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - OceanBase DataStudio运行在Lakebase之上，覆盖数据接入、加工、编排、语义建模到Agent协作等环节。
  - DataStudio把分散的数据资产转化为可调用的数据服务，解决数据治理与服务化问题。
  article_id: dcde9bfd34ee88ac
- object_type: product
  name: OceanBase DataPilot
  canonical_name: OceanBase DataPilot
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - OceanBase DataPilot作为统一的企业业务智能入口，让业务人员通过自然语言完成分析报告、数据看板和可信答案生成。
  - DataPilot解决业务人员如何直接使用数据智能的问题。
  article_id: dcde9bfd34ee88ac
---

# OceanBase发布AI数据库：以一套引擎融合湖库与多模态数据

让AI真正“读懂”企业

过去三年，大模型能力快速跃升，算力持续突破，但企业AI落地却并未迎来预期中的价值释放。越来越多行业开始形成共识：AI竞争的焦点，正在从模型转向数据。

6月29日，OceanBase发布面向AI时代的湖库一体AI数据库，提出以湖库一体为核心架构，将数据湖的开放与海量存储能力、数据库的事务处理与分析能力，以及多模态数据处理能力统一到一套强一致的数据底座上，帮助Agent（智能体）一次获取完整业务上下文，让AI真正“读懂”企业。

围绕这一能力，OceanBase AI数据库 同步形成覆盖数据引擎、数据治理与业务入口的产品体系，包括Lakebase、DataStudio、DataPilot等，并已在蚂蚁阿福、灵光等AI场景完成业务验证。

业内普遍认为，随着Agent成为数据库新的使用者，数据库正从“记录事实”走向“参与决策”，AI数据库也因此成为AI时代新的基础设施形态。

（图说：OceanBase发布湖库一体的AI数据库）

**AI落地瓶颈在数据，“湖库一体”成为最佳路径**

过去，大模型解决的是“会不会思考”的问题；今天，真正的瓶颈变成了“是否理解业务”。模型能力在快速收敛，业务差异正在向数据层转移。

随着Agent进入系统执行层、企业数据走向多模态化，传统多系统协同的架构越来越难以满足AI对“统一上下文”的要求。AI正在改变数据的管理范式，Agent进入生产带来的“规模、上下文和进化”等三个关键挑战愈发显著，把AI对数据库的影响拆解来看，数据形态、数据流动、数据交互都在变，但数据库本身的一致性、扩展性、可靠性、实时性这四条底线不可退让。

真正需要被重写的是架构，必须被坚守的是底线——指向的正是湖库一体：让多模态数据在统一引擎中被管理、计算与服务，从架构层消除多系统割裂。

（图说： OceanBase 发布面向AI时代的全新产品体系）

围绕湖库一体，OceanBase 打造了AI时代的全新产品体系：

OceanBase Lakebase作为底层引擎，让结构化数据、非结构化数据和向量数据在统一架构中被管理、加工、检索和调用，解决AI时代的数据底座问题；

OceanBase DataStudio运行在Lakebase之上，覆盖数据接入、加工、编排、语义建模到Agent协作等环节，把分散的数据资产转化为可调用的数据服务，解决数据治理与服务化问题；

OceanBase DataPilot则作为统一的企业业务智能入口，让业务人员通过自然语言完成分析报告、数据看板和可信答案生成，解决业务人员如何直接使用数据智能的问题。

据介绍，相较传统多系统方案，OceanBase AI数据库可降低整体TCO（Total Cost of Ownership，总体拥有成本）约30%-50%。目前该能力已在蚂蚁阿福、灵光等场景完成验证，其中灵光累计生成数千万个“闪应用”，验证了湖库一体架构在千万级Agent场景下的可行性。

OceanBase CTO杨传辉表示：“真正的一体化，必须发生在架构层。湖库一体不是数据库和数据湖的简单拼接，而是在同一套引擎中统一管理多模态数据，打通在线与离线处理。”

**重新定义AI数据库，国产厂商迎来新的窗口期**

AI数据库正在成为全球基础软件的新赛道，但技术路径尚未收敛：有的从数据湖延展能力边界，有的强化搜索与语义理解能力，也有厂商从数据库内核出发，尝试重构整体数据体系。

差异的本质，不在组件选择，而在对“AI如何使用数据”的不同理解。在这一轮变化中，AI数据库不再是传统数据库的能力扩展，而是在重新定义数据如何被AI组织、调用与决策。

（图说： OceanBase再造AI时代的湖库一体数据库）

OceanBase选择从数据库内核出发，将长期在金融核心系统中验证的事务一致性、高可用与弹性能力，延伸至湖与多模态数据体系之上，使其具备统一支撑AI负载的能力——这是从底层出发的重构，而非在旧架构上的叠加修补。

公开资料显示，OceanBase是中国自主研发的数据库，起源于2010年“双十一”场景。十五年来，它经历了金融行业最严苛的锤炼——已服务超400家金融机构，连续二年位居中国分布式数据库本地部署市场第一，也是迄今唯一同时登顶TPC-C和TPC-H两项国际权威测试的数据库，业务覆盖全球多个国家和地区。

这套在金融级场景中锤炼出的能力——数据不出错、系统不中断、故障毫秒恢复——正是AI时代的刚需。将其从“库”延伸到“湖”，是OceanBase站在十五年地基之上的自然一步，也使其具备了参与AI数据库范式重构竞争的基础。

长期以来，基础软件的标准主要由国际厂商定义，而AI数据库正进入一个规则尚未固化的阶段。这意味着竞争不再只是追赶已有体系，而是参与新体系的形成过程。

OceanBase CEO杨冰表示：“我们有机会从‘跟随者’走向‘共同定义者’，参与AI数据库范式的形成。这既是中国的机遇，也是OceanBase的机遇。”

*本文由蚂蚁OceanBase提供，量子位获授权转载，观点归原作者所有。

*版权所有，未经授权不得以任何形式转载及使用，违者必究。*