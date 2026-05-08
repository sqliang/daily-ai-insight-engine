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