---
title: Time series causal discovery with variable lags
source: https://arxiv.org/abs/2605.04081
author:
- '[[Bruno Petrungaro, Anthony C. Constantinou]]'
published: '2026-05-07'
created: '2026-05-08'
description: 'arXiv:2605.04081v1 Announce Type: cross Abstract: Causal Bayesian Networks
  (CBNs) are a powerful tool for reasoning under uncertainty about complex real-world
  problems. Such problems evolve over time, responding to external shocks as they
  occur. To support decision-making, CBNs require a cause-and-effect map of the variables
  under consideration, known as the network''s structure. Learning the graphical structure
  of a causal model from data remains challenging; learning it from time-series data
  is even harder because dependencies may arise at different time lags. Existing time-series
  causal discovery methods often assume a fixed lag window and do not explicitly optimise
  edge-specific lags. We propose a Tabu-based structure learning algorithm that searches
  for a time-ordered directed structure (i.e., where every edge respects time) while
  allowing edge-specific lags up to a specified maximum lag. The approach uses a decomposable
  BIC-based score with node-specific effective sample sizes and an explicit lag-length
  penalty encouraging parsimonious delay assignments while preserving efficient local
  score updates. We provide theoretical guarantees of validity and local optimality,
  and we also describe a parallel implementation for improved scalability. In simulations,
  the method recovered graph structure competitively and estimated lags accurately
  when true adjacencies were recovered. On a real-world UK COVID-19 policy dataset,
  the learnt structure was dominated by short delays while retaining a substantial
  minority of longer-lag dependencies, consistent with delayed behavioural and epidemiological
  effects.'
tags:
- clippings
id: dfc1fcd5fb7663ea
source_type: academic_paper
tldr: 提出基于Tabu搜索的变滞后时间序列因果发现算法
objective_summary: 论文提出一种Tabu搜索算法用于时间序列因果发现，允许每条边独立指定滞后时间，使用可分解BIC评分函数并包含滞后长度惩罚项。提供了理论保证与并行实现。仿真实验图结构恢复有竞争力，在英国COVID-19数据集上验证了短延迟为主、长延迟并存的结构特征。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Causal Bayesian Networks (CBNs)
  - Tabu search
  - BIC-based score
  key_people: []
key_logic_flow:
- 现有时间序列因果发现方法通常假设固定滞后窗口，无法针对每条边优化独立的滞后参数。
- 该论文提出一种基于Tabu搜索的结构学习算法，要求所有边满足时间顺序约束，并允许每条边独立指定滞后时间直至最大滞后值。
- 算法使用可分解的BIC评分函数，结合节点特异性有效样本量和显式的滞后长度惩罚项，鼓励简约的延迟分配。
- 作者提供了算法的有效性和局部最优性理论保证，并描述了并行实现方案以提升可扩展性。
- 仿真实验表明该方法在恢复图结构方面有竞争力，且在正确恢复邻接关系时能准确估计滞后时间。
- 在英国COVID-19政策数据集上，学习到的因果结构以短延迟为主，同时保留了相当数量的长滞后依赖关系。
impact_score:
  score: 4.2
  reason: 该论文提出的变滞后因果发现算法是对时间序列因果推断方法的一次有意义的增量改进，而非范式级突破。核心贡献在于允许每条边独立优化滞后参数，突破了固定滞后窗口的假设。但该方法仍处于学术验证阶段，仅在仿真数据集和一个真实COVID-19数据集上验证，尚未展示出足以改变行业格局的实证效果。对于因果推断研究社区有价值，但短期内对AI行业整体竞争格局影响有限。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 变滞后因果发现算法的理论保证与可扩展性
hype_assessment:
  level: low
  reason: 论文标题和摘要均为客观描述性语言，无'颠覆'、'革命性'等PR滥用词汇。提供了完整的理论保证（有效性证明、局部最优性证明）、并行实现方案以及仿真与真实数据验证，是实打实的学术贡献。
information_entropy: high
domain_disruption:
  technical_innovation: 提出允许每条因果关系边独立指定滞后参数（而非统一固定窗口）的Tabu搜索结构学习算法，配合带滞后长度惩罚项的可分解BIC评分函数，并给出有效性及局部最优性的理论保证，同时设计了并行实现提升可扩展性。
  business_model: 无直接商业模式影响，但可为时序决策系统（如经济政策评估、医疗干预效果分析、工业控制）提供更精确的因果结构推断工具，间接提升数据驱动的决策质量。
engineering_complexity: prototype
compound_value:
  score: 4.5
  reason: 该论文提出变滞后时间序列因果发现算法，解决了传统方法固定滞后窗口无法优化边级别延迟的核心痛点。从VC视角看：这是一项有扎实理论贡献的方法论创新，价值捕获路径需通过集成到成熟因果发现框架（如DoWhy、TETRAD、CausalNex）来实现，而非独立商业化。其可分解BIC评分和滞后惩罚项设计具备工程友好性，但论文仍处于仿真验证和单一真实数据集验证阶段，大规模工业级鲁棒性尚未证明。中长期复利潜力取决于：(1)能否被主流因果推断工具链吸收为标准模块；(2)是否有团队围绕此构建更完整的因果AutoML产品。当前对流行病学、经济学等领域的应用价值明确，但不足以自成基础设施，处于4-7分的中间偏下位置，需持续关注后续工程化和生态建设进展。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Microsoft Research (DoWhy/pywhy-ecosystem)
- causaLens
- 因果推断学术社区
- 流行病学与公共卫生政策研究机构
- 时间序列分析开源生态（如TETRAD、pcalg）
competitive_casualty:
- 固定滞后窗口假设的传统因果发现方法
- 仅依赖相关性或Granger因果检验的简化分析工具
- 不支持变量特定滞后优化的时间序列分析软件
market_opportunities:
- 政府公共卫生与政策评估部门可利用变滞后因果发现算法，分析政策干预（如封锁措施、疫苗接种）对疫情指标的延迟效应，提升循证决策精度
- 量化投资与宏观对冲基金可探索将该算法集成到因子归因系统，自动发现不同经济变量间差异化滞后的因果传导关系，优化预测模型
- 工业预测性维护与供应链优化领域，可基于该算法从传感器时间序列中识别设备故障信号与操作变量之间延迟时间不一的因果链路
risk_matrix:
  regulatory: 无直接监管风险，但若应用于金融投资决策或医疗健康等强监管领域，需要额外验证方法的鲁棒性和可解释性
  technological: Tabu搜索在大规模变量图结构学习场景下可能面临可扩展性瓶颈；基于深度学习的端到端因果发现方法（如DAG-GNN、IMC等）可能在未来提供竞争性替代方案
  competitive: 时间序列因果发现领域已有PCMCI、基于VAR的结构学习、Granger因果检验等成熟方法，该算法需要与这些已有工具竞争用户采纳和生态支持
  ethical: 若模型假设（如马尔可夫性、无隐变量混淆）在实际数据中不成立，推断出的因果结构可能产生误导，影响政策或商业决策的质量
  additional: []
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: monitor
---

# Computer Science > Machine Learning

# Title:Time series causal discovery with variable lags

View PDF HTML (experimental)Abstract:Causal Bayesian Networks (CBNs) are a powerful tool for reasoning under uncertainty about complex real-world problems. Such problems evolve over time, responding to external shocks as they occur. To support decision-making, CBNs require a cause-and-effect map of the variables under consideration, known as the network's structure. Learning the graphical structure of a causal model from data remains challenging; learning it from time-series data is even harder because dependencies may arise at different time lags. Existing time-series causal discovery methods often assume a fixed lag window and do not explicitly optimise edge-specific lags. We propose a Tabu-based structure learning algorithm that searches for a time-ordered directed structure (i.e., where every edge respects time) while allowing edge-specific lags up to a specified maximum lag. The approach uses a decomposable BIC-based score with node-specific effective sample sizes and an explicit lag-length penalty encouraging parsimonious delay assignments while preserving efficient local score updates. We provide theoretical guarantees of validity and local optimality, and we also describe a parallel implementation for improved scalability. In simulations, the method recovered graph structure competitively and estimated lags accurately when true adjacencies were recovered. On a real-world UK COVID-19 policy dataset, the learnt structure was dominated by short delays while retaining a substantial minority of longer-lag dependencies, consistent with delayed behavioural and epidemiological effects.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.