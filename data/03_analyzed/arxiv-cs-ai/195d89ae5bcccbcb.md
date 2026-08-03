---
title: 'SEAGym: An Evaluation Environment for Self-Evolving LLM Agents'
source: https://arxiv.org/abs/2606.17546
author:
- '[[Congjie Zheng, Chuanyi Xue, Bin Liang, Jun Yang, Changshui Zhang]]'
published: '2026-06-17'
created: '2026-06-17'
description: 'arXiv:2606.17546v1 Announce Type: new Abstract: Self-evolving LLM-based
  agents improve mainly by changing their agent harness: the structured execution
  layer around a base model, including prompts, memory, tools, middleware, runtime
  state, and the model-tool interaction loop. Existing evaluations often reduce this
  process to isolated task scores or a single sequential curve, obscuring whether
  an update produces reusable improvement, overfits recent tasks, increases cost,
  or harms older behavior. We introduce SEAGym, an evaluation environment for measuring
  agent harness updates across training, validation, test, replay, and cost records.
  SEAGym turns Harbor-compatible benchmarks into dynamic self-evolution task sources
  with train batches, frozen update-validation, held-out ID and OOD transfer views,
  replay diagnostics, and saved snapshot and metric records. Instantiating SEAGym
  on Terminal-Bench 2.0 and HLE, we compare ACE, TF-GRPO, and AHE under a shared epoch/batch
  protocol. The results show that these evaluation views provide complementary signals
  about the evolution process: frequent updates may fail to improve held-out performance,
  useful intermediate snapshots may collapse later, and source diversity and model
  backend can affect harness reliability.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 195d89ae5bcccbcb
source_type: academic_paper
tldr: SEAGym 是一个用于评估自进化 LLM Agent 框架更新的评测环境，在 Terminal-Bench 2.0 和 HLE 上对比了 ACE、TF-GRPO
  和 AHE 三种方法，发现频繁更新可能无法提升留出性能且中间快照可能在后继更新中崩溃。
objective_summary: 研究者提出了 SEAGym，一个专为自进化 LLM Agent 设计的评测环境，用于衡量 agent harness（包括提示词、记忆、工具、中间件、运行时状态及模型-工具交互循环）的更新效果。SEAGym
  提供训练、验证、测试、回放和成本记录五个维度的评估视图，将 Harbor 兼容基准测试转化为动态自进化任务源。研究者在 Terminal-Bench 2.0 和
  HLE 上实例化 SEAGym，对比了 ACE、TF-GRPO 和 AHE 三种方法，结果表明频繁更新可能无法提升留出测试集性能，有用中间快照可能在后继更新中崩溃，且源多样性与模型后端影响框架可靠性。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - SEAGym
  - ACE
  - TF-GRPO
  - AHE
  - Terminal-Bench 2.0
  - HLE
  - Harbor
  key_people: []
key_logic_flow:
- SEAGym 是一个专门用于评估自进化 LLM Agent 的评测环境，核心关注 agent harness 层面的更新，包括提示词、记忆、工具、中间件和运行时状态。
- 现有评估方法通常将自进化过程简化为孤立任务分数或单一序列曲线，无法判断更新是否产生可复用改进、是否过拟合近期任务或是否损害旧行为。
- SEAGym 提供训练、验证、测试、回放和成本记录五个评估维度，并将 Harbor 兼容基准测试转化为动态自进化任务源。
- 研究者在 Terminal-Bench 2.0 和 HLE 两个基准上实例化 SEAGym，对比了 ACE、TF-GRPO 和 AHE 三种自进化方法在统一 epoch/batch
  协议下的表现。
- 实验结果表明频繁更新可能无法提升留出测试集性能，有用的中间快照可能在后续更新中性能衰退，且源多样性与模型后端选择会影响 agent 框架的整体可靠性。
extract_result: success
object_mentions:
- object_type: project
  name: SEAGym
  canonical_name: SEAGym
  url: https://arxiv.org/abs/2606.17546
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - SEAGym 是一个用于测量 agent harness 更新效果的评测环境，覆盖训练、验证、测试、回放和成本记录五个维度。
  - SEAGym 将 Harbor 兼容基准测试转化为动态自进化任务源，支持训练批次、冻结更新验证、留出 ID 和 OOD 迁移视图以及回放诊断。
  article_id: 195d89ae5bcccbcb
- object_type: dataset
  name: Terminal-Bench 2.0
  canonical_name: Terminal-Bench 2.0
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 研究者将 SEAGym 实例化在 Terminal-Bench 2.0 和 HLE 两个基准上，用于对比不同自进化方法的效果。
  article_id: 195d89ae5bcccbcb
- object_type: dataset
  name: HLE
  canonical_name: HLE
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 研究者将 SEAGym 实例化在 Terminal-Bench 2.0 和 HLE 两个基准上，用于对比不同自进化方法的效果。
  article_id: 195d89ae5bcccbcb
- object_type: project
  name: ACE
  canonical_name: ACE
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 研究者在统一 epoch/batch 协议下，使用 SEAGym 对比了 ACE、TF-GRPO 和 AHE 三种自进化方法的评估结果。
  article_id: 195d89ae5bcccbcb
- object_type: project
  name: TF-GRPO
  canonical_name: TF-GRPO
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 研究者在统一 epoch/batch 协议下，使用 SEAGym 对比了 ACE、TF-GRPO 和 AHE 三种自进化方法的评估结果。
  article_id: 195d89ae5bcccbcb
- object_type: project
  name: AHE
  canonical_name: AHE
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 研究者在统一 epoch/batch 协议下，使用 SEAGym 对比了 ACE、TF-GRPO 和 AHE 三种自进化方法的评估结果。
  article_id: 195d89ae5bcccbcb
- object_type: project
  name: Harbor
  canonical_name: Harbor
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - SEAGym 将 Harbor 兼容的基准测试转化为动态自进化任务源，以支持训练批次和冻结更新验证等功能。
  article_id: 195d89ae5bcccbcb
impact_score:
  score: 6.0
  reason: SEAGym 填补了自进化 LLM 代理评估方法论的一个重要空白——将原先碎片化的单曲线/单分数评价提升为包含训练、验证、测试、回放和成本记录的多维度框架。对于当前火热的自进化代理研究领域，标准化评估基础设施是刚需。然而，这是一篇方法论/基准论文，而非架构突破或产品发布，影响力集中在学术研究圈，短期难以辐射到应用层开发者。评分依据：虽然领域内需求明确，但受众较窄，不足以改变整体竞争格局。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 自进化代理评估标准化——多维度度量能否被社区采纳并替代现有的单曲线评价
hype_assessment:
  level: low
  reason: 论文没有使用任何 PR 软性词汇（如"革命性"、"突破"），实验设计透明，且诚实报告了负面发现——频繁更新未必提升保留集性能、中间快照可能后续失效，这种包含"失败的信号"的学术风格恰恰是低炒作的有力证据。
information_entropy: high
domain_disruption:
  technical_innovation: 提出将自进化代理框架的更新过程分解为训练批次、冻结验证、ID/OOD 迁移视图、回放诊断和快照记录五个评估维度，能够检测到单曲线评价无法捕捉的过拟合、成本回归和行为退化现象。将
    Harbor 兼容基准转化为动态自进化任务源的工程设计思路也具有可复用价值。
  business_model: 无
engineering_complexity: prototype
compound_value:
  score: 4.5
  reason: SEAGym 切入了一个真实且快速增长的痛点——自进化 LLM 代理框架的评估缺乏系统性方法论。现有评估要么简化为孤立任务分数，要么用单条序列曲线掩盖有害更新和过拟合，SEAGym
    首次提供训练/验证/测试/回放/成本五维评估框架，并揭示了重要的反直觉结论（频繁更新未必提升保留性能、中间快照可能失效）。从 VC 视角看，评估基础设施在
    AI 生态中有长期价值，但 SEAGym 是学术开源原型（非商业产品），其长期复利取决于能否被社区采纳为事实标准。AI 评估标准迭代极快（GLUE→SuperGLUE→BIG-Bench→…），单一学术框架的护城河薄弱，且
    monetization 路径不清晰。核心研究洞察有持久参考价值，但工具本身的 3-5 年生命周期风险较高。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- ACE 项目
- TF-GRPO 项目
- AHE 项目
- Anthropic
- OpenAI
- Google DeepMind
competitive_casualty:
- 传统静态 Agent Benchmark（如单任务评分体系）
- 闭源评估平台
- 缺乏系统回放机制的 Agent 框架
market_opportunities:
- 自进化LLM代理的评估基础设施存在市场空白，可基于SEAGym的框架思路开发面向企业的代理行为审计与回归测试SaaS平台，覆盖训练验证、回放诊断、成本追踪等维度
- 发现'频繁更新未必提升保留集性能'和'中间快照可能后续失效'，为AI工程团队提供了代理更新策略的设计依据——建议建立快照版本管理、自动回滚和持续回归验证的工程实践
- 研究者和第三方评测机构可基于SEAGym的多维度评估协议（ID/OOD迁移、回放诊断），推出针对自进化代理鲁棒性的行业基准评测服务
risk_matrix:
  regulatory: 无
  technological: 自进化代理存在快照失效（useful intermediate snapshots may collapse later）和频繁更新无效的系统性风险，生产环境中若缺乏版本回滚机制和持续验证流程，可能导致代理行为不可逆退化
  competitive: 无
  ethical: 自进化代理的行为随时间漂移可能引发不可预测输出，部署后若缺乏持续监控和人工审核机制，在敏感场景（如医疗建议、金融决策）中可能产生合规与安全风险
  additional: []
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: SEAGym
  canonical_name: SEAGym
  url: https://arxiv.org/abs/2606.17546
  positioning: SEAGym 是一个专为自进化 LLM Agent 设计的评测环境，专注于衡量 agent harness（提示词、记忆、工具、中间件、运行时状态）层面的更新效果。
  technical_signal: SEAGym 提供训练、验证、测试、回放和成本记录五个评估维度，将 Harbor 兼容基准测试转化为动态自进化任务源。
  adoption_signal: 研究者在 Terminal-Bench 2.0 和 HLE 上实例化 SEAGym，使用统一 epoch/batch 协议对比了
    ACE、TF-GRPO 和 AHE 三种方法的评估效果。
  ecosystem_relevance: SEAGym 填补了自进化 Agent 评测空白，解决了现有评估无法判断更新是否产生可复用改进或损害旧行为的问题。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: SEAGym 提出的多维度评估框架为自进化 LLM Agent 研究提供了标准化评测手段。实验发现频繁更新未必提升留出性能、有用中间快照可能衰退等结论，对
    Agent 自进化方向具有重要指导意义。
  risk_notes:
  - SEAGym 仅基于 Terminal-Bench 2.0 和 HLE 两个基准验证，在更广泛场景下的适用性尚待检验。
  - SEAGym 作为评测工具本身不提供自进化方法及基线，其长期价值依赖于社区采用和贡献程度。
  score: 7.0
  article_ids:
  - 195d89ae5bcccbcb
  evidence_snippets:
  - SEAGym 是一个用于测量 agent harness 更新效果的评测环境，覆盖训练、验证、测试、回放和成本记录五个维度。
  - SEAGym 将 Harbor 兼容基准测试转化为动态自进化任务源，支持训练批次、冻结更新验证、留出 ID 和 OOD 迁移视图以及回放诊断。
- object_type: project
  name: ACE
  canonical_name: ACE
  url: null
  positioning: ACE 是一种在 SEAGym 统一框架下接受评估并与 TF-GRPO、AHE 对比的自进化 LLM Agent 方法。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: ACE 作为 SEAGym 评测框架下的对比方法之一，其在统一 epoch/batch 协议下的表现结果为自进化 Agent 方法研究提供了参考基准。
  risk_notes:
  - 当前仅知 ACE 被纳入 SEAGym 的对比评估，缺乏对其方法细节和独立性能的公开信息。
  score: 3.0
  article_ids:
  - 195d89ae5bcccbcb
  evidence_snippets:
  - 研究者在统一 epoch/batch 协议下，使用 SEAGym 对比了 ACE、TF-GRPO 和 AHE 三种自进化方法的评估结果。
- object_type: project
  name: TF-GRPO
  canonical_name: TF-GRPO
  url: null
  positioning: TF-GRPO 是一种在 SEAGym 统一框架下接受评估并与 ACE、AHE 对比的自进化 LLM Agent 方法。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: TF-GRPO 作为 SEAGym 评测框架下的对比方法之一，其在统一 epoch/batch 协议下的表现结果为自进化 Agent
    方法研究提供了参考基准。
  risk_notes:
  - 当前仅知 TF-GRPO 被纳入 SEAGym 的对比评估，缺乏对其方法细节和独立性能的公开信息。
  score: 3.0
  article_ids:
  - 195d89ae5bcccbcb
  evidence_snippets:
  - 研究者在统一 epoch/batch 协议下，使用 SEAGym 对比了 ACE、TF-GRPO 和 AHE 三种自进化方法的评估结果。
- object_type: project
  name: AHE
  canonical_name: AHE
  url: null
  positioning: AHE 是一种在 SEAGym 统一框架下接受评估并与 ACE、TF-GRPO 对比的自进化 LLM Agent 方法。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: AHE 作为 SEAGym 评测框架下的对比方法之一，其在统一 epoch/batch 协议下的表现结果为自进化 Agent 方法研究提供了参考基准。
  risk_notes:
  - 当前仅知 AHE 被纳入 SEAGym 的对比评估，缺乏对其方法细节和独立性能的公开信息。
  score: 3.0
  article_ids:
  - 195d89ae5bcccbcb
  evidence_snippets:
  - 研究者在统一 epoch/batch 协议下，使用 SEAGym 对比了 ACE、TF-GRPO 和 AHE 三种自进化方法的评估结果。
---

# Computer Science > Artificial Intelligence

# Title:SEAGym: An Evaluation Environment for Self-Evolving LLM Agents

View PDF HTML (experimental)Abstract:Self-evolving LLM-based agents improve mainly by changing their agent harness: the structured execution layer around a base model, including prompts, memory, tools, middleware, runtime state, and the model-tool interaction loop. Existing evaluations often reduce this process to isolated task scores or a single sequential curve, obscuring whether an update produces reusable improvement, overfits recent tasks, increases cost, or harms older behavior. We introduce SEAGym, an evaluation environment for measuring agent harness updates across training, validation, test, replay, and cost records. SEAGym turns Harbor-compatible benchmarks into dynamic self-evolution task sources with train batches, frozen update-validation, held-out ID and OOD transfer views, replay diagnostics, and saved snapshot and metric records. Instantiating SEAGym on Terminal-Bench 2.0 and HLE, we compare ACE, TF-GRPO, and AHE under a shared epoch/batch protocol. The results show that these evaluation views provide complementary signals about the evolution process: frequent updates may fail to improve held-out performance, useful intermediate snapshots may collapse later, and source diversity and model backend can affect harness reliability.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.