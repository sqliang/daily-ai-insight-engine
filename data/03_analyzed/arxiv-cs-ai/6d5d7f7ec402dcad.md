---
title: 'TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon
  Agent Training'
source: https://arxiv.org/abs/2607.05804
author:
- '[[Yuhang Zhou, Kai Zheng, Haoling Li, Dengyun Peng, Can Xu, Jingjing Chen]]'
published: '2026-07-08'
created: '2026-07-08'
description: 'arXiv:2607.05804v1 Announce Type: new Abstract: On-policy distillation
  (OPD) trains a student policy by matching a stronger teacher on the student''s own
  trajectories, offering a promising framework for language agent training. However,
  its application to long-horizon agentic tasks remains insufficiently explored. We
  identify two key inefficiencies in vanilla agent OPD: (1) full-horizon rollouts
  often waste wall-clock resources on tail turns that provide weak and noisy KL supervision,
  and (2) trajectory-level KL objectives concentrate most of the loss on shallow tokens,
  leaving deeper decision turns under-trained once initial behaviors are aligned.
  To address these challenges, we propose TurnOPD, a turn-level budgeting strategy
  for efficient on-policy distillation of long-horizon agents. TurnOPD consists of
  two budget controllers: adaptive rollout-depth budgeting, which uses probe-based
  turn statistics to determine rollout length, and progressive turn-normalized loss
  budgeting, which gradually shifts KL weighting from token-level to turn-balanced
  supervision. Experiments on ALFWorld, WebShop, and Multi-Hop Search with task-specialized
  teacher models show that TurnOPD achieves superior validation accuracy under equal
  wall-clock training budgets and advances the accuracy--time frontier beyond vanilla
  OPD.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 6d5d7f7ec402dcad
manifest_dates:
- '2026-07-08'
source_type: academic_paper
tldr: 提出 TurnOPD，一种面向长程智能体训练的高效同策略蒸馏方法，通过回合级预算控制提升训练效率。
objective_summary: 该论文提出 TurnOPD 方法，通过自适应 rollout 深度预算和渐进式回合归一化损失预算，解决长程智能体同策略蒸馏中的低效问题。在
  ALFWorld、WebShop 和 Multi-Hop Search 任务上，TurnOPD 在同等训练时间下取得了更优的验证准确率。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - TurnOPD
  - On-Policy Distillation
  - KL divergence
  - Agent Training
  key_people: []
key_logic_flow:
- TurnOPD 识别出 vanilla 同策略蒸馏的两个低效问题：完整回合 rollout 在尾部步骤浪费资源，以及回合级 KL 损失集中在浅层 token 上导致深层决策回合训练不足。
- TurnOPD 提出自适应 rollout 深度预算控制器，基于探针回合统计数据动态决定 rollout 长度，避免尾部无效计算。
- TurnOPD 提出渐进式回合归一化损失预算控制器，将 KL 权重从 token 级逐步转向回合平衡监督。
- 在 ALFWorld、WebShop 和 Multi-Hop Search 三个长程智能体任务上，TurnOPD 在相同壁钟训练预算下超越了 vanilla OPD
  的验证准确率。
specialized_tags:
  paper:
    paperTitle: 'TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon
      Agent Training'
    authors: []
    affiliations: []
    venue: arXiv preprint
    codeUrl: null
    datasetUrl: null
    researchArea: AI
    methodType: RL-based
extract_result: success
impact_score:
  score: 4.5
  reason: TurnOPD 是对同策略蒸馏（OPD）技术的增量改进，聚焦于长程智能体训练中的效率问题。该方法通过自适应 rollout 深度预算和渐进式回合归一化损失预算两个控制器，在
    ALFWorld、WebShop 和 Multi-Hop Search 三个基准上验证了有效性。虽是扎实的学术贡献，但并非范式突破——它优化的是已有框架（OPD）的工程效率，而非提出全新训练范式。对专门从事智能体训练的研究团队有参考价值，但不会引发行业范围的格局变化。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: 长程智能体训练中同策略蒸馏的计算效率提升
hype_assessment:
  level: low
  reason: 这是 arXiv 上的一篇学术论文，语言克制、用词准确（'improve efficiency'、'advances the accuracy-time
    frontier'），没有出现'颠覆'、'革命性'等 PR 滥用词汇。论文提供了清晰的实验设置、任务定义和消融研究，属于实打实的技术贡献。
information_entropy: high
domain_disruption:
  technical_innovation: 提出自适应 rollout 深度预算控制器（基于探针回合的统计数据动态截断无效尾部 rollout）和渐进式回合归一化损失预算控制器（从
    token 级 KL 逐步过渡到回合平衡监督），两者协同解决长程智能体同策略蒸馏中计算资源浪费和深层回合训练不足的两个核心低效问题。
  business_model: 无
engineering_complexity: prototype
compound_value:
  score: 5.5
  reason: TurnOPD 切中了一个真实且日益重要的痛点——长程智能体训练的计算效率瓶颈。自适应 rollout 深度预算和渐进式回合归一化损失预算这两个机制，在技术逻辑上是扎实的增量创新，且实验覆盖了
    ALFWorld、WebShop、Multi-Hop Search 三个典型长程任务场景。但从 VC 视角看，这篇论文的本质是学术优化技巧，而非平台级或产品级突破：它需要在主流训练框架（如
    RLHF/DPO 工具链、开源 RL 库）中获得实质性集成才能产生规模效应。当前缺乏生产环境的实证数据（仅在 benchmark 上验证），商业化路径不清晰，是否会被大实验室内部更成熟的蒸馏系统（如
    Anthropic 的 Constitutions 方法、Google 的 PAX 生态）采纳仍是未知数。长期复利潜力存在，但处于需持续验证的阶段，评分中性偏正面。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Anthropic
- Google DeepMind
- OpenAI
- LangChain
- Hugging Face
competitive_casualty:
- 依赖完整 rollout 蒸馏的传统 RL agent 训练平台
- 训练效率低下的 AI agent 初创公司
market_opportunities:
- 专注于长程智能体训练的企业可采用 TurnOPD 方法降低同策略蒸馏的计算成本，在相同训练预算下获得更高准确率的智能体模型
- AI Infra 和训练平台团队可参考自适应 rollout 深度控制器的思路，为强化学习训练框架加入动态回合截断功能，提升训练资源利用率
- 面向 Web 自动化、客服对话等长程决策场景的创业公司，可基于 TurnOPD 的思路优化微调 pipeline，缩短模型迭代周期
risk_matrix:
  regulatory: 无直接监管风险，但该技术若被用于训练具有自动执行能力的智能体（如 Web 自动化），可能触发各国对自主 AI 代理的监管审查
  technological: 该方法高度依赖教师模型的质量，且仅在特定长程基准（ALFWorld、WebShop）上验证，跨领域泛化性尚未被充分证明；若有更高效的蒸馏方法出现，TurnOPD
    可能被快速取代
  competitive: 头部 AI 实验室（如 OpenAI、Google DeepMind、Anthropic）均在探索智能体训练优化，可能推出更系统化的训练框架挤压该方法的独立应用空间
  ethical: 提升长程智能体训练效率可能加速自主智能体的规模化部署，若缺乏安全对齐，可能带来不可控的自动决策风险；但同时也有助于在更少计算资源下实现更好的对齐训练，兼具双面性
  additional:
  - 该方法需要针对每个任务调整探针回合的超参数，工程化落地的复杂度可能高于预期
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: monitor
paper_metadata:
  title: 'TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon
    Agent Training'
  authors: []
  affiliations: []
  venue: arXiv preprint
  paper_url: https://arxiv.org/abs/2607.05804
  code_url: null
  dataset_url: null
research_problem:
  core_question: 如何通过引入回合级别的预算感知机制，解决基于策略的蒸馏（OPD）在长周期智能体训练中面临的尾部回合计算浪费和深层决策回合训练不足的问题？
  motivation: 基于策略的蒸馏（OPD）通过让学生模型在自己的轨迹上匹配更强的教师模型，是一种有前景的语言智能体训练框架。但现有 OPD 在长周期（多轮交互）智能体任务中表现出两大关键低效：一是完整周期
    rollout 的尾部回合通常提供弱且有噪声的 KL 监督信号，造成计算资源的浪费；二是轨迹级别的 KL 目标将大部分损失集中在浅层 token 上，一旦初始行为对齐，深层决策回合便难以获得充分的训练信号。这两个问题严重制约了
    OPD 在长周期智能体训练中的效率与效果。
  significance: practical
  gap_addressed: 现有 OPD 方法在长周期智能体任务中缺乏对回合级训练效率的系统性关注——既没有对低价值尾部回合进行计算预算的优化控制，也没有对回合间的损失分配不均衡问题进行处理，导致训练资源浪费且深层决策回合训练不足。
methodology:
  approach_summary: TurnOPD 提出了一种回合级预算策略（turn-level budgeting strategy），旨在提高长周期智能体基于策略蒸馏（OPD）的训练效率。该方法由两个互补的预算控制器组成：(1)
    自适应 rollout 深度预算（adaptive rollout-depth budgeting），通过探针回合（probe-based turn）的统计信息动态决定每个轨迹的
    rollout 长度，在尾部回合 KL 监督信号变弱时提前截断，避免资源浪费；(2) 渐进式回合归一化损失预算（progressive turn-normalized
    loss budgeting），在训练过程中逐步将 KL 损失的加权策略从 token 级别转向回合级别的平衡监督，确保深层决策回合也能获得足够的梯度信号。两个控制器协同工作，在保持蒸馏质量的同时显著提升训练的计算效率。
  novelty_type: algorithmic
  key_innovations:
  - 提出自适应 rollout 深度预算机制，通过探针回合统计动态决定 rollout 截断点，避免在低信息量的尾部回合上浪费计算资源
  - 提出渐进式回合归一化损失预算机制，从 token 级 KL 损失逐步过渡到回合平衡的 KL 损失，解决深层决策回合训练不足问题
  inspiration_sources:
  - 基于策略的蒸馏（OPD）框架
  - 课程学习与渐进式训练策略
  - 长周期智能体任务中的稀疏监督与信用分配研究
  - 自适应计算与提前退出机制
  technical_depth: moderate
experimental_rigor:
  benchmark_coverage: 在三个代表性长周期智能体基准上进行了评估：ALFWorld（具身交互任务）、WebShop（网页购物智能体）和 Multi-Hop
    Search（多跳信息检索），覆盖了具身推理、电子商务和知识检索三类不同的长期决策场景
  baseline_comparison: adequate
  ablation_quality: adequate
  reproducibility_level: partially
  claimed_improvement: 在相同 wall-clock 训练预算下取得更优的验证准确率，推进了精度-时间（accuracy-time）训练前沿面，超越了
    vanilla OPD
limitations_and_honesty:
  stated_limitations:
  - 评估仅覆盖 ALFWorld、WebShop 和 Multi-Hop Search 三类任务，对更广泛场景的适用性尚需验证
  - 需配合任务专用教师模型（task-specialized teacher），教师模型的质量直接影响学生蒸馏效果
  reviewer_concerns:
  - 探针回合策略引入的额外计算开销是否已被公允纳入效率对比，是否存在探针频率的 trade-off
  - 两个预算控制器引入的新超参数（探针触发时机、损失转换进度等）的敏感性分析和调参成本
  - 仅与 vanilla OPD 对比，缺乏与其他训练策略（如课程学习、优先级采样、混合训练）的横向比较
  - 回合归一化损失可能在极端长尾任务中导致早期回合噪声放大，影响训练稳定性
  overclaiming_assessment: honest
  generalization_concern: 方法在三个基准任务上表现良好，但这些任务的回合结构相对规整（有明确的终止状态和回合边界）。对于回合边界模糊、奖励极度稀疏或需要自由形式交互的真实世界智能体任务（如软件工程、科学研究、开放式对话），两个预算控制器的适应性和效果尚待验证。
industrial_relevance:
  applicable_domains:
  - 大语言模型驱动的长周期智能体训练与部署
  - 知识蒸馏与模型压缩
  - 自动化工作流与 RPA 智能体
  - 多轮对话系统与客服机器人
  - 网页自动化与信息检索智能体
  compute_requirements: commodity
  integration_readiness: needs_engineering
  cost_efficiency_analysis: TurnOPD 的核心价值在于提升训练效率而非增加算力需求。通过减少无效尾部 rollout 的计算开销和优化损失分配，在相同
    GPU 预算下可以训练出性能更优的智能体模型，或加速训练迭代周期。对于已使用 OPD 框架训练长周期智能体的团队，集成两个预算控制器的工程成本相对可控，边际收益显著。该方法不依赖特殊硬件，适合在现有训练基础设施上部署。
related_work_context:
  closest_prior_works:
  - On-Policy Distillation (OPD) — 基于策略的蒸馏框架
  - Imitation Learning / Behavioral Cloning for Language Agents
  - 长周期智能体中的稀疏奖励与信用分配方法
  - 知识蒸馏中的损失加权与课程学习策略
  advancement_over_prior: 相比 vanilla OPD，TurnOPD 首次系统性地识别并解决了长周期智能体蒸馏中的两个回合级效率瓶颈——尾部计算浪费和回合间损失失衡。自适应
    rollout 深度预算和渐进式回合归一化损失预算两个机制形成互补，在不改变 OPD 核心蒸馏逻辑的前提下显著提升了训练效率，是 OPD 在长周期场景下的实用化改进。
  opens_new_direction: false
  potential_follow_ups:
  - 将回合级预算策略扩展到离线蒸馏或多教师蒸馏框架
  - 探索更高效的探针机制（如基于不确定性或熵的指标）以减少额外开销
  - 将 TurnOPD 与课程学习、自适应计算图等技术结合形成更完整的训练策略
  - 在更复杂的真实世界智能体任务（如 SWE-bench、AgentBench 等）上进行大规模验证
  - 研究回合归一化损失的收敛理论性质及与训练稳定性的关系
---

# Computer Science > Artificial Intelligence

# Title:TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon Agent Training

View PDFAbstract:On-policy distillation (OPD) trains a student policy by matching a stronger teacher on the student's own trajectories, offering a promising framework for language agent training. However, its application to long-horizon agentic tasks remains insufficiently explored. We identify two key inefficiencies in vanilla agent OPD: (1) full-horizon rollouts often waste wall-clock resources on tail turns that provide weak and noisy KL supervision, and (2) trajectory-level KL objectives concentrate most of the loss on shallow tokens, leaving deeper decision turns under-trained once initial behaviors are aligned. To address these challenges, we propose TurnOPD, a turn-level budgeting strategy for efficient on-policy distillation of long-horizon agents. TurnOPD consists of two budget controllers: adaptive rollout-depth budgeting, which uses probe-based turn statistics to determine rollout length, and progressive turn-normalized loss budgeting, which gradually shifts KL weighting from token-level to turn-balanced supervision. Experiments on ALFWorld, WebShop, and Multi-Hop Search with task-specialized teacher models show that TurnOPD achieves superior validation accuracy under equal wall-clock training budgets and advances the accuracy--time frontier beyond vanilla OPD.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.