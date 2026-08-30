---
title: harveyai/harvey-labs
source: https://github.com/harveyai/harvey-labs
author: []
published: ''
created: '2026-08-10'
manifest_dates:
- '2026-08-10'
- '2026-08-12'
description: 'A benchmark built to evaluate and improve agent capabilities for supporting
  legal work. Legal Agent Benchmark (LAB): An open-source benchmark for evaluating
  agents on real legal work. Harvey LAB is an open-source project aimed at benchmarking
  LLM agents'' abilities to perform legal work in realistic environments. LAB consists
  of two parts: a dataset of tasks containing agent instructions, documents, and rubrics
  as well as an execution harness for running and evaluating agents against those
  tasks. LAB is an ongoing project and we expect to consistently add to and refine
  the task set and execution harness. Read the announcement post: Introducing Harvey''s
  Legal Agent Benchmark Getting Started Start with the full walkthrough in docs/tutorial.md
  — it takes one realistic M&A data-room assignment end to end: setup, task inspection,
  agent run, scoring, report review, and comparison dashboards. Additional Documentation
  Guide Description Architecture Task model, harness, tools, adapters, reports, and
  sweeps Evaluation Methodology All-pass rubric scoring and LLM judge behavior Contributing
  Add tasks, model adapters, evaluation improvements, and docs Citation If you use
  Harvey LAB in your research, please cite it as: @misc{harveylab2026, title = {Harvey
  LAB: The Legal Agent Benchmark}, author = {{Harvey AI}}, year = {2026}, version
  = {v1.0}, url = {https://github.com/harveyai/harvey-labs/tree/v1.0}, note = {Announcement:
  \url{https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark}} }'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: b1dcbece28dae08b
source_type: community_discussion
tldr: Harvey AI 发布开源基准 Harvey LAB，用于在真实法律工作环境中评估 LLM 智能体的法律工作能力，由任务数据集与执行框架两部分构成，目前仍在持续迭代。
objective_summary: Harvey AI 于 2026 年发布开源项目 Harvey LAB（Legal Agent Benchmark），其目标是在真实法律工作场景中评估
  LLM 智能体的能力。LAB 由两部分组成：一是包含智能体指令、文档与评分量规的任务数据集，二是用于运行和评估智能体的执行框架。项目提供 M&A 数据室任务的端到端演练文档，采用全通过量规评分与
  LLM 评判员评估方法，并给出 v1.0 版本引用格式。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Harvey AI
  technologies:
  - LLM
  - LLM agents
  - LLM-as-judge
  - Legal Agent Benchmark (LAB)
  key_people: []
key_logic_flow:
- Harvey AI 发布开源项目 Harvey LAB，用于在真实法律工作环境中评估 LLM 智能体的法律工作能力。
- LAB 由两部分构成：一个包含智能体指令、文档与评分量规的任务数据集，以及一个用于运行和评估智能体的执行框架。
- 项目文档提供 M&A 数据室任务的端到端演练，涵盖环境搭建、任务检查、智能体运行、评分、报告审阅与对比仪表盘。
- LAB 的评估方法采用全通过量规评分与 LLM 评判员行为，架构涉及任务模型、工具、适配器、报告与 sweeps。
- 该项目仍处于持续开发阶段，官方计划不断补充和优化任务集与执行框架，并已提供 v1.0 版本的学术引用格式。
object_mentions:
- object_type: project
  name: harveyai/harvey-labs
  canonical_name: Harvey LAB (Legal Agent Benchmark)
  url: https://github.com/harveyai/harvey-labs
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Harvey LAB 是 Harvey AI 发布的开源项目，用于在真实法律工作环境中评估 LLM 智能体的法律工作能力。
  - LAB 由两部分组成：一个包含智能体指令、文档与评分量规的任务数据集，以及一个用于运行和评估智能体的执行框架。
  - LAB 提供 M&A 数据室任务的端到端演练文档，并采用全通过量规评分与 LLM 评判员行为进行评测。
  - Harvey LAB 仍在持续开发中，官方计划不断补充任务集与执行框架，并已发布 v1.0 版本及对应引用格式。
  article_id: b1dcbece28dae08b
extract_result: success
impact_score:
  score: 6.0
  reason: 评分依据：Harvey 是法律 AI 领域估值最高的头部厂商，其开源基准有望成为该垂直领域的事实评估标准（类似 SWE-bench 之于软件工程），填补了法律
    agent 缺乏真实场景公开基准的空白，可能在 6-12 个月内被同行、学术圈与企业采购方引用；但影响范围局限于法律垂直领域，不改变通用 AI 评估范式，且当前无公开榜单数据验证其公允性与横向可比性。综合评估属于'改变局部竞争格局'级别，远未达到行业范式转移规模，故给
    6.0 分。
sentiment: positive
developer_sentiment:
  tone: skeptical
  primary_focus: 基准是否偏向 Harvey 自家模型（自我服务偏见）以及 LLM-as-judge 全通过量规的评分可靠性
hype_assessment:
  level: low
  reason: 判定依据：原文措辞克制，使用 'open-source benchmark'、'ongoing project' 等平实表述，未出现'颠覆'、'革命性'等
    PR 滥用词汇；项目提供可运行的执行框架、端到端教程与 v1.0 学术引用格式，属可验证的干货。仅有的包装点在于 Harvey 借此树立法律 AI 思想领袖形象，但不构成概念炒作。
information_entropy: medium
domain_disruption:
  technical_innovation: 将真实法律工作场景（M&A 数据室）抽象为包含指令、文档与量规的可执行任务集，并配套 agent 执行框架与'全通过量规
    + LLM 评判员'评分流程，是法律 agent 评估基础设施的重要补白；但属于评估方法论层面的工程化贡献，而非底层模型或架构的突破性创新。
  business_model: Harvey 通过开源基准抢占法律 AI 评估标准制定权，若 LAB 被业界采纳，可形成'以我之基准衡量全行业'的先发优势，并成为企业采购/选型法律
    AI 产品时的参考标准，客观上构建生态影响力与潜在锁定效应。
engineering_complexity: production_ready
compound_value:
  score: 6.5
  reason: Harvey LAB 的战略本质是抢占'法律 AI 智能体评测标准'这一基础设施层，逻辑类似 SWE-bench 之于编程智能体、MMLU 之于通用模型：一旦成为法律垂类的默认基准，就形成'任务集越丰富→采用者越多→反馈迭代越强→任务集更丰富'的复利飞轮，且制定者掌握评测话语权与结果数据资产，3-5
    年内有概率成为该赛道的行业标尺。但必须审慎看待三重风险：其一，Harvey 本身是最大的法律 AI 应用厂商，'运动员兼裁判'的身份存在明显利益冲突，Casetext/Spellbook/Luminance
    等直接竞对可能拒绝采信或另立标准，这会阻断其成为行业统一基准的路径，使其退化为单厂商营销工具；其二，全通过量规 + LLM-as-judge 在高度专业的法律任务上的评测可靠性尚需实证，法律结果对错误零容忍，评测体系自身就可能被证伪；其三，项目仍处
    v1.0 迭代早期，尚未形成 SWE-bench 级别的社区网络效应与第三方生态。综合判断：具备细分赛道基础设施的潜力，但需持续观察 2-3 个版本迭代质量与竞对采纳率，故给
    6.5 分。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Harvey AI
- Anthropic
- OpenAI
competitive_casualty:
- Casetext（Thomson Reuters CoCounsel）
- Spellbook
- Luminance
- 传统法律科技平台（Relativity、iManage）
market_opportunities:
- 法律科技创业团队可基于 Harvey LAB 开源基准搭建自家法律 AI 产品的评测体系，用真实 M&A 数据室任务量化智能体能力，作为产品差异化宣传与律所采购论证的核心素材
- 该'任务数据集 + 执行框架'的开源基准模式可复制到医疗合规、金融尽调等高价值垂直领域，抢先建立行业评测标准不仅能掌握生态话语权，还能衍生出基准定制与评测咨询服务
- 律所与公司法务部门可参照 LAB 的评估方法论（全通过量规 + LLM 评判员）建立第三方法律 AI 工具的准入与验收流程，系统性降低选型与采购风险
risk_matrix:
  regulatory: 法律工作属强监管领域，基准任务若涉及真实法律文档可能触发律师保密义务与数据隐私合规问题；欧盟 AI Act 等法规可能将法律 AI 评估视为高风险场景，且基准结果的营销化使用可能引发误导性宣传的监管审查
  technological: LLM-as-judge 评估方法存在评判员偏差与自我偏好等已知缺陷，且 v1.0 基准仍处早期迭代、任务集覆盖有限，随 LLM
    能力快速提升可能饱和失效；开源基准还面临被针对性过拟合刷榜的技术风险
  competitive: Harvey AI 既是法律 AI 参赛者又是基准裁判，其主导的开源基准可能被竞争对手质疑为自我偏好设计；LegalBench 等既有基准与后续新玩家的同类基准将形成标准之争，可能挤压本基准的行业采用率
  ethical: 法律文档高度敏感，任务集构建存在隐私与保密伦理风险；自动化评估法律工作可能加剧律所初级岗位被替代的就业冲击，且自动化评分对法律服务质量与公平正义的评判存在失真风险
  additional:
  - 开源基准的长期演进依赖厂商持续投入，存在项目停滞或标准被弃用的可持续性风险
  - 若律所过度采信基准结论作为采购与质量依据，可能引发法律职业责任及'算法辅助决策'责任归属争议
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: harveyai/harvey-labs
  canonical_name: Harvey LAB (Legal Agent Benchmark)
  url: https://github.com/harveyai/harvey-labs
  positioning: Harvey LAB 是 Harvey AI 发布的开源法律智能体基准，面向真实法律工作环境评估 LLM 智能体的能力，由任务数据集与执行框架两部分构成。
  technical_signal: 项目采用全通过量规评分与 LLM 评判员评估方法，架构涵盖任务模型、工具、适配器、报告与 sweeps，并提供 M&A 数据室端到端演练文档。
  adoption_signal: 项目已发布 v1.0 版本并提供学术引用格式，表明基准具备对外引用基础，但官方称仍在持续补充任务集与执行框架。
  ecosystem_relevance: Harvey AI 作为法律 AI 头部厂商开源评测基准，为法律智能体评测提供标准化任务集与执行框架，有望推动行业评测方法趋同。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Harvey LAB 由法律 AI 头部厂商 Harvey AI 开源，切入真实法律工作场景的 LLM 智能体评测空白，其任务集与执行框架可能成为行业能力对比的参照标准，且项目仍在持续迭代，值得跟踪任务集扩展与评测方法演进。
  risk_notes:
  - 项目仍处于持续开发阶段，任务集覆盖的司法场景有限，当前评测结论可能尚不具备广泛普适性。
  - 评测依赖 LLM 评判员进行全通过量规评分，评判偏差与结果可复现性存在不确定性。
  - 基准由 Harvey AI 主导维护，任务设计与评分标准可能带有其自身产品取向，第三方中立性有待观察。
  score: 7.0
  article_ids:
  - b1dcbece28dae08b
  evidence_snippets:
  - Harvey LAB 是 Harvey AI 发布的开源项目，用于在真实法律工作环境中评估 LLM 智能体的法律工作能力。
  - LAB 由两部分组成：一个包含智能体指令、文档与评分量规的任务数据集，以及一个用于运行和评估智能体的执行框架。
  - LAB 提供 M&A 数据室任务的端到端演练文档，并采用全通过量规评分与 LLM 评判员行为进行评测。
  - Harvey LAB 仍在持续开发中，官方计划不断补充任务集与执行框架，并已发布 v1.0 版本及对应引用格式。
---

**Legal Agent Benchmark (LAB): An open-source benchmark for evaluating agents on real legal work.**

Harvey LAB is an open-source project aimed at benchmarking LLM agents' abilities to perform legal work in realistic environments.

LAB consists of two parts: a dataset of *tasks* containing agent instructions, documents, and rubrics as well as an *execution harness* for running and evaluating agents against those tasks.

LAB is an ongoing project and we expect to consistently add to and refine the task set and execution harness.

Read the announcement post: Introducing Harvey's Legal Agent Benchmark

Start with the full walkthrough in **docs/tutorial.md** — it takes one realistic M&A data-room assignment end to end: setup, task inspection, agent run, scoring, report review, and comparison dashboards.

| Guide | Description |
|---|---|
| Architecture | Task model, harness, tools, adapters, reports, and sweeps |
| Evaluation Methodology | All-pass rubric scoring and LLM judge behavior |
| Contributing | Add tasks, model adapters, evaluation improvements, and docs |

If you use Harvey LAB in your research, please cite it as:

```
@misc{harveylab2026,
title = {Harvey LAB: The Legal Agent Benchmark},
author = {{Harvey AI}},
year = {2026},
version = {v1.0},
url = {https://github.com/harveyai/harvey-labs/tree/v1.0},
note = {Announcement: \url{https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark}}
}
```