---
title: 'Joint Treatment Effect Estimation from Incomplete Healthcare Data: Temporal
  Causal Normalizing Flows with LLM-driven Evolutionary MNAR Imputation'
source: https://arxiv.org/abs/2605.05125
author:
- '[[Olivia Jullian Parra, Sara Zoccheddu, David Catalan Cerezo, Tom Forzy, Franziska
  Ulrich, William Sutcliffe, Jakob Martin Burgstaller, Oliver Senn, Patrick Owen,
  Nicola Serra]]'
published: '2026-05-07'
created: '2026-05-08'
description: 'arXiv:2605.05125v1 Announce Type: cross Abstract: Target trial emulation
  (TTE) enables causal questions to be studied with observational data when randomized
  controlled trials (RCTs) are infeasible. Yet treatment-effect methods often address
  causal estimation, missingness, and temporal structure separately, limiting their
  robustness in electronic health records (EHRs), where time-varying confounding and
  missing-not-at-random (MNAR) biomarkers can reach 50%--80%. We propose a two-stage
  pipeline for treatment effect estimation from incomplete longitudinal EHRs. First,
  CausalFlow-T, a directed acyclic graph (DAG)-constrained normalizing flow with long
  short-term memory (LSTM)-encoded patient history, performs exact invertible counterfactual
  inference, avoiding approximation errors from variational inference and separating
  confounding through explicit causal structure. Ablations on four synthetic and one
  semi-synthetic benchmark with known counterfactuals show that DAG constraints and
  exact inference address distinct failure modes: neither compensates for the other.
  Second, because CausalFlow-T requires completed inputs, we introduce an LLM-driven
  evolutionary imputer that proposes executable imputation operators rather than individual
  entries, and evaluate it with three large language model (LLM) backends, including
  two open-source models. Across 30%--80% MNAR missingness, this imputer achieves
  the best pooled rank over biomarker and causal metrics, leading in point-wise accuracy
  and temporal extrapolation while preserving average treatment effect (ATE) recovery
  as statistical baselines degrade. On Swiss primary-care EHRs from adults with type
  2 diabetes initiating a GLP-1 receptor agonist or SGLT-2 inhibitor, the pipeline
  estimates a per-protocol weight-loss difference of -0.98 kg [95% CI -1.01, -0.96]
  favoring GLP-1 receptor agonists, consistent with randomized evidence and obtained
  from realistically incomplete real-world EHRs.'
tags:
- clippings
id: 87c5ed94ea4eb6fe
source_type: academic_paper
tldr: 提出CausalFlow-T与LLM进化插补的两阶段框架，从不完整EHR数据估计治疗效果
objective_summary: 该论文提出两阶段治疗效应估计管道：CausalFlow-T使用DAG约束归一化流与LSTM编码患者病史，进行精确可逆反事实推断；LLM驱动的进化插补器生成可执行插补算子处理MNAR缺失数据。在四个合成基准和一个半合成基准上验证，并在瑞士2型糖尿病成人患者真实EHR数据上估计出GLP-1受体激动剂相比
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - CausalFlow-T
  - normalizing flow
  - DAG-constrained
  - LSTM
  - LLM
  - MNAR
  - ATE
  - counterfactual inference
  - target trial emulation
  key_people: []
key_logic_flow:
- 现有治疗方法效果评估方法在因果估计、缺失值处理和时序结构上彼此分离，在电子健康记录中鲁棒性不足，尤其是MNAR类型缺失率可达50%-80%。
- 提出CausalFlow-T方法：基于有向无环图约束的归一化流，结合LSTM编码的患者历史，实现精确可逆的反事实推断，避免变分推断的近似误差。
- 为解决CausalFlow-T需要完整输入的问题，提出LLM驱动的进化插补器，生成可执行的插补算子而非单个数值条目，并使用三个LLM后端（含两个开源模型）进行评估。
- 在四个合成基准和一个半合成基准上的消融实验表明，DAG约束和精确推断分别处理不同的失效模式，二者不可相互替代。
- 在30%-80%的MNAR缺失率下，该插补器在生物标志物和因果指标上取得最佳综合排名，在均值治疗效果恢复上随统计基线退化仍保持领先。
- 在瑞士2型糖尿病成人患者真实EHR数据上应用目标试验仿真，GLP-1受体激动剂相比SGLT-2抑制剂的按方案减重差异估计为-0.98kg，与随机对照试验证据一致。
impact_score:
  score: 5.5
  reason: 该论文提出了一套完整的端到端因果效应估计管道，将DAG约束归一化流与LLM驱动插补有机结合，在真实EHR数据上验证了与RCT一致的结论。但整体属于方法论增量创新，而非范式级突破；短期影响限于因果推断与医疗AI交叉领域的研究社区，不会广泛出圈。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 精确反事实推断与LLM驱动缺失值插补的创新集成，以及在高缺失率真实医疗数据上的验证
hype_assessment:
  level: low
  reason: 论文使用学术论文标准语言，未出现'颠覆'、'革命性'等夸大词汇。消融实验设计严谨，区分了DAG约束与精确推断各自处理不同的失效模式，并在四个合成+一个半合成基准上进行了系统验证，结论保守且可靠。
information_entropy: high
domain_disruption:
  technical_innovation: 提出CausalFlow-T，利用DAG约束归一化流实现精确可逆反事实推断，避免变分推断的近似误差；同时首创LLM驱动的进化插补器，生成可执行插补算子而非单值填充，在30%-80%
    MNAR缺失率下保持因果估计一致性。
  business_model: 目标试验仿真（TTE）的可靠性提升可降低药物疗效评估对昂贵随机对照试验的依赖，加速真实世界证据（RWE）在监管决策和临床指南中的应用，具有显著的成本效益优势。
engineering_complexity: prototype
compound_value:
  score: 5.5
  reason: 该论文提出的 CausalFlow-T + LLM 进化插补框架在方法论上有明显创新：首次将 DAG 约束归一化流与 LLM 驱动的可执行插补算子相结合，解决
    EHR 中 50%-80% MNAR 缺失率下的治疗效应估计问题。长期复利价值在于（1）真实世界证据（RWE）监管接受度持续提升，此类因果推断基础设施需求刚性增长；（2）LLM
    生成可执行算子而非简单插值的思路可能推广至其他科学领域。但扣分原因：（1）纯学术论文，无公司实体和产品化路径，技术转移风险高；（2）验证仅限一个瑞士 T2D
    真实数据集，泛化性待验证；（3）归一化流+LSTM 架构在快速迭代的 LLM 时代面临被更简单端到端方案替代的风险。整体看是细分领域的重要基础设施潜力，但距离可投资产品还有
    2-3 年差距。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- 诺华 (Novartis)
- 罗氏 (Roche)
- IQVIA
- FDA/CDER 真实世界证据办公室
- Flatiron Health
competitive_casualty:
- 传统 CRO 统计服务商
- SAS 医疗分析业务
- 传统多重插补（MI）软件厂商
market_opportunities:
- 制药公司与CRO可采用该两阶段管线进行真实世界证据生成和目标试验仿真，降低对昂贵随机对照试验的依赖，加速药物上市后疗效评估与监管申报
- 电子健康记录系统供应商可将LLM驱动的进化插补器集成到数据管道中，解决50%-80%的MNAR缺失率问题，大幅提升下游分析和临床决策支持的数据质量
- 医疗AI创业公司可基于该框架构建因果推断即服务平台，为医院和保险公司提供从非完整真实世界数据中估计治疗效果的SaaS工具
risk_matrix:
  regulatory: 医疗AI法规风险：若该管道用于辅助临床决策或药物评估，可能面临FDA/EMA的医疗器械软件（SaMD）监管框架审查，需额外临床试验验证；同时涉及敏感患者数据处理，需确保GDPR/HIPAA合规
  technological: LLM生成的插补算子质量高度依赖后端模型能力，开源模型效果可能不稳定性，且在不同疾病领域和医疗系统的泛化性尚未充分验证；归一化流在高维生物标志物空间的可扩展性是潜在瓶颈
  competitive: 因果推断领域已有DoWhy、CausalNex等成熟框架以及科技巨头的医疗AI平台（如Google DeepMind、Microsoft
    Nuance），该方法的差异化优势（MNAR处理+精确推断）需快速产品化以避免被生态挤压
  ethical: 有向无环图的结构若被错误设定，可能导致治疗效果估计系统性偏差，进而影响临床治疗决策；真实EHR数据中的隐私风险和数据投毒问题不容忽视，需建立严格的数据治理机制
  additional: []
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: monitor
---

# Computer Science > Machine Learning

# Title:Joint Treatment Effect Estimation from Incomplete Healthcare Data: Temporal Causal Normalizing Flows with LLM-driven Evolutionary MNAR Imputation

View PDF HTML (experimental)Abstract:Target trial emulation (TTE) enables causal questions to be studied with observational data when randomized controlled trials (RCTs) are infeasible. Yet treatment-effect methods often address causal estimation, missingness, and temporal structure separately, limiting their robustness in electronic health records (EHRs), where time-varying confounding and missing-not-at-random (MNAR) biomarkers can reach 50%--80%. We propose a two-stage pipeline for treatment effect estimation from incomplete longitudinal EHRs. First, CausalFlow-T, a directed acyclic graph (DAG)-constrained normalizing flow with long short-term memory (LSTM)-encoded patient history, performs exact invertible counterfactual inference, avoiding approximation errors from variational inference and separating confounding through explicit causal structure. Ablations on four synthetic and one semi-synthetic benchmark with known counterfactuals show that DAG constraints and exact inference address distinct failure modes: neither compensates for the other. Second, because CausalFlow-T requires completed inputs, we introduce an LLM-driven evolutionary imputer that proposes executable imputation operators rather than individual entries, and evaluate it with three large language model (LLM) backends, including two open-source models. Across 30%--80% MNAR missingness, this imputer achieves the best pooled rank over biomarker and causal metrics, leading in point-wise accuracy and temporal extrapolation while preserving average treatment effect (ATE) recovery as statistical baselines degrade. On Swiss primary-care EHRs from adults with type 2 diabetes initiating a GLP-1 receptor agonist or SGLT-2 inhibitor, the pipeline estimates a per-protocol weight-loss difference of -0.98 kg [95% CI -1.01, -0.96] favoring GLP-1 receptor agonists, consistent with randomized evidence and obtained from realistically incomplete real-world EHRs.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.