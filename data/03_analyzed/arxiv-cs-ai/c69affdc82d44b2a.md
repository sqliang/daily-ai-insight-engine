---
title: 'Automata from Agent Traces: Failure and Next-Step Prediction'
source: https://arxiv.org/abs/2608.23670
author:
- '[[Seonglae Cho, Franklin Cardenoso Fernandez, Umar Mohammed, Zekun Wu, Kleyton
  Da Costa, Ilham Wicaksono, Adriano Koshiyama]]'
published: '2026-08-26'
created: '2026-08-26'
manifest_dates:
- '2026-08-26'
- '2026-08-27'
description: 'arXiv:2608.23670v1 Announce Type: new Abstract: LLM-based agents execute
  multi-step tasks, but their behavioral structure remains opaque: long unstructured
  traces resist the safety auditing and runtime monitoring that deployment requires.
  Existing approaches operate per-trace or success-only, so they miss the cross-run
  topology that links next-step and failure prediction. To recover that shared structure,
  we collapse an entire trace corpus into a single, compact finite-state machine (FSM)
  that serves as a structural substrate for the otherwise unpredictable behavior of
  LLM agents. Across twelve public datasets, the FSMs are compact (7-43 states), replay
  held-out data at >=0.997 fitness with near-identical topology across splits, and
  build in milliseconds. This substrate addresses both prediction goals. For next-step
  prediction, FSM-state context outperforms Agent Workflow Memory on every ground-truth-matched
  dataset. For failure prediction, per-state behavioral features reach held-out AUROC
  up to 0.94, and an online monitor ranks failing runs above passing ones from a partial
  trace, triggering early stopping well before completion. Behavioral topology thus
  appears shaped more by the deployment harness than by the LLM, providing a model-agnostic
  structural primitive for safety auditing and runtime monitoring.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: c69affdc82d44b2a
source_type: academic_paper
tldr: 论文提出将LLM代理的整个轨迹语料库压缩为单个紧凑的有限状态机（FSM），用于下一步预测与失败预测。在十二个公开数据集上，FSM仅含7-43个状态、拟合度不低于0.997，失败预测AUROC最高达0.94，并支持在线提前停止。
objective_summary: 该研究针对LLM代理多步任务行为结构不透明的问题，提出将整个轨迹语料库压缩为单个紧凑的有限状态机（FSM），作为代理行为的结构化基础。实验在十二个公开数据集上进行，FSM仅含7-43个状态，对保留数据拟合度不低于0.997，构建耗时仅毫秒级。在下一步预测上，FSM状态上下文在所有真值匹配的数据集上均优于Agent
  Workflow Memory基线；失败预测的每状态行为特征AUROC最高达0.94。在线监控器能凭部分轨迹区分失败与成功运行，在任务完成前触发提前停止，且行为拓扑更多由部署框架而非LLM本身塑造。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - FSM
  - LLM
  - Agent Workflow Memory
  key_people: []
key_logic_flow:
- LLM代理的多步任务执行行为结构不透明，长而无结构的轨迹难以支撑安全审计与运行时监控。
- 现有方法按单条轨迹或仅成功案例处理，忽略了连接下一步预测与失败预测的跨运行拓扑结构。
- 论文将整个轨迹语料库压缩为单个紧凑的有限状态机，作为代理行为预测的结构化基础。
- 在十二个公开数据集上，FSM仅含7至43个状态，对保留数据拟合度不低于0.997且拓扑跨划分几乎一致，构建仅需毫秒级。
- 在下一步预测上，FSM状态上下文在每个真值匹配的数据集上均优于Agent Workflow Memory基线方法。
- 在失败预测上，每状态行为特征AUROC最高达0.94，在线监控器能凭部分轨迹在任务完成前触发提前停止。
object_mentions:
- object_type: paper
  name: 'Automata from Agent Traces: Failure and Next-Step Prediction'
  canonical_name: Automata from Agent Traces
  url: https://arxiv.org/abs/2608.23670
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文提出将LLM代理的整个轨迹语料库压缩为单个紧凑的有限状态机，作为行为预测的结构化基础。
  - 论文在十二个公开数据集上验证，FSM仅含7至43个状态，对保留数据的拟合度不低于0.997。
  - 在线监控器能凭部分轨迹将失败运行排在通过运行之前，并在任务完成前触发提前停止。
  article_id: c69affdc82d44b2a
- object_type: paper
  name: Agent Workflow Memory
  canonical_name: Agent Workflow Memory
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 在下一步预测任务中，FSM状态上下文在每个真值匹配的数据集上均优于Agent Workflow Memory这一基线方法。
  article_id: c69affdc82d44b2a
extract_result: success
impact_score:
  score: 5.5
  reason: 评分依据：论文直击 LLM agent 在生产部署中最痛的可观测性/安全性问题，提出用单个紧凑 FSM 压缩整个轨迹语料库，作为模型无关的监控原语。技术扎实度较高——12
    个公开数据集、与 Agent Workflow Memory 基线的逐项对比、保留数据拟合度≥0.997、失败预测 AUROC 达 0.94，且工程成本极低（毫秒级构建、仅
    7-43 个状态），因此对 agent 可观测性、安全审计和提前停止机制的设计有直接参考价值，短期内有望被 agent 平台研发团队和可观测性工具关注。但它属于渐进式方法论贡献：不改变
    agent 能力本身，没有新训练范式或新模型，不构成行业范式转移，短期冲击范围主要局限于学术圈与 agent 基础设施研发者，普通开发者感知有限。综合评分为
    5.5。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: FSM 轨迹压缩能否跨框架复现并落地为生产级 agent 监控与提前停止机制
hype_assessment:
  level: low
  reason: 判定依据：全文措辞克制，未出现'颠覆''革命性'等 PR 滥用词汇；主张均有实证支撑——12 个公开数据集、保留数据拟合度与跨划分拓扑一致性、与既有基线
    Agent Workflow Memory 的系统对比、AUROC 等量化指标齐全，方法描述可复现，属于实打实的学术干货。唯一需要保留的是'行为拓扑由部署框架而非
    LLM 本身塑造'这一较强论断，其普适性有待跨框架/跨模型的独立复现验证，但不足以推高炒作判定。
information_entropy: high
domain_disruption:
  technical_innovation: 核心创新是把 LLM 代理长而无结构的轨迹语料库整体压缩为单个紧凑确定性 FSM，提取跨运行共享的行为拓扑结构，首次将'下一步预测'与'失败预测'统一到同一结构化基板上，并揭示行为拓扑主要由部署框架（harness）而非底层
    LLM 塑造，为不透明 agent 行为提供模型无关的结构化表示与在线提前停止能力。
  business_model: 该方法构建成本极低（毫秒级）、压缩率极高（7-43 状态），天然适合嵌入 agent 可观测性/安全监控类产品，可作为'代理运行时监控、失败早期预警、上线前安全审计'等
    SaaS 或开源工具的核心算法；对 agent 编排框架、AI 网关及 APM 类可观测性厂商有直接集成价值，可能催生轻量级 agent 行为审计的新品类。
engineering_complexity: prototype
compound_value:
  score: 5.5
  reason: 从资本视角看，该研究切入的是 AI Agent 规模化部署中最关键也最缺位的环节——行为可观测性与安全审计（即'Agent 时代的 APM'）。其复利潜质来自三点：第一，将任意
    LLM 代理的整段轨迹语料压缩为 7-43 个状态的紧凑 FSM，构建仅毫秒级，意味着监控边际成本趋近于零，天然适合规模化接入；第二，研究发现行为拓扑主要由部署框架（harness）而非底层
    LLM 决定，即模型无关，不绑定单一模型厂商，具备跨代模型复用的长期价值；第三，一个结构同时支撑下一步预测与失败预测（AUROC 最高 0.94）并支持在线提前停止，直击企业级
    Agent 落地最刚性的风险合规需求。若该技术被主流 Agent 可观测性/安全平台采纳为底层标准，有机会沉淀为细分赛道基础设施。但当前仍属学术理论验证阶段（theoretical_claim），尚无真实生产环境的多任务鲁棒性验证；且该能力很可能被
    LangChain、OpenAI、Anthropic 等框架/平台直接内置吸收，独立商业化的空间存在被压缩风险。综合评分为 5.5——具备成为基础设施的潜质，但需持续验证产品化路径。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Langfuse
- LangSmith
- Arize AI
- OpenAI
- Anthropic
competitive_casualty:
- 传统 RPA 厂商（UiPath、Automation Anywhere）
- 模型锁定的闭源 Agent 监控方案
- Agent Workflow Memory 类基线方法
market_opportunities:
- 可基于FSM轨迹压缩技术开发LLM代理运行时监控与提前停止工具，帮助企业拦截注定失败的Agent任务、降低算力与token成本，这是当前可观测性工具尚未充分覆盖的场景
- 建议关注Agent安全审计赛道：将轨迹压缩为紧凑FSM作为行为结构化基座，构建跨框架的失败预测与合规审计产品，切入LangSmith、Langfuse、AgentOps等现有可观测性厂商的能力盲区
- 论文揭示'行为拓扑更多由部署框架而非LLM本身塑造'，可将其转化为代理框架选型与提示词/工具编排优化的评估指标，为工程团队提供模型无关的调试诊断工具
risk_matrix:
  regulatory: 该技术本身合规风险较低，甚至有助于满足欧盟AI法案等监管对高风险AI系统可审计性、运行时监控的要求；但应用时若将含用户交互的轨迹数据压缩进FSM用于监控，需注意轨迹中可能隐含个人数据，须评估GDPR等数据保护法的合规性
  technological: 该结论基于arXiv预印本，认识论状态为theoretical_claim，尚未经独立复现与生产环境验证；FSM对保留数据0.997的高拟合度可能依赖特定轨迹形态，代理框架升级或任务分布漂移可能导致状态机拓扑失效，且存在被更强序列模型或在线学习方法替代的风险
  competitive: Agent可观测性赛道竞争激烈，LangSmith、Langfuse、AgentOps等既有厂商可能快速将类似轨迹压缩或状态聚类能力内建到产品中，挤压独立创业团队的差异化空间；论文若仅发表不开源也会削弱技术壁垒
  ethical: 将用户代理轨迹压缩并用于行为监控可能涉及数据隐私与知情同意问题；失败预测AUROC在不同任务类型间可能不均衡，存在对特定代理行为系统性误判的风险；行为拓扑揭示的框架差异信息亦可能被用于规避或反向攻击安全监控
  additional:
  - 该技术依赖高质量标注轨迹语料，数据标注成本与噪声可能限制落地效果
  - 论文未披露与主流代理框架（如LangChain、Claude Code）的工程集成细节，实际适配成本与在线监控延迟开销未知
confidence:
  impact: medium
  compound: medium
  hype: medium
actionable_insight: deep_dive
---

# Computer Science > Artificial Intelligence

# Title:Automata from Agent Traces: Failure and Next-Step Prediction

View PDF HTML (experimental)Abstract:LLM-based agents execute multi-step tasks, but their behavioral structure remains opaque: long unstructured traces resist the safety auditing and runtime monitoring that deployment requires. Existing approaches operate per-trace or success-only, so they miss the cross-run topology that links next-step and failure prediction. To recover that shared structure, we collapse an entire trace corpus into a single, compact finite-state machine (FSM) that serves as a structural substrate for the otherwise unpredictable behavior of LLM agents. Across twelve public datasets, the FSMs are compact (7-43 states), replay held-out data at >=0.997 fitness with near-identical topology across splits, and build in milliseconds. This substrate addresses both prediction goals. For next-step prediction, FSM-state context outperforms Agent Workflow Memory on every ground-truth-matched dataset. For failure prediction, per-state behavioral features reach held-out AUROC up to 0.94, and an online monitor ranks failing runs above passing ones from a partial trace, triggering early stopping well before completion. Behavioral topology thus appears shaped more by the deployment harness than by the LLM, providing a model-agnostic structural primitive for safety auditing and runtime monitoring.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.