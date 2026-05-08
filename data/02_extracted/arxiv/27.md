---
title: 'A Regulatory Governance Framework for AI-Driven Financial Fraud Detection
  in U.S. Banking: Integrating OCC, SR 11-7, CFPB, and FinCEN Compliance Requirements
  for Model Development, Validation, and Monitoring Lifecycles'
source: https://arxiv.org/abs/2605.04076
author:
- '[[Mohammad Nasir Uddin]]'
published: '2026-05-07'
created: '2026-05-08'
description: 'arXiv:2605.04076v1 Announce Type: cross Abstract: U.S. financial institutions
  deploying AI-based fraud detection face a fragmented compliance landscape spanning
  four regulatory frameworks -- OCC Bulletin 2011-12, SR 11-7, the CFPB AI circular,
  and FinCEN BSA/SAR requirements -- with no integrated governance life cycle connecting
  these requirements to model development, validation, and monitoring practice. This
  paper presents the Regulatory Governance Framework for AI-Driven Financial Fraud
  Detection (RGF-AFFD), a three-tier governance architecture empirically anchored
  in a multi-study empirical program. Using the IEEE-CIS dataset (590,540 transactions)
  and ULB benchmark (284,807 transactions), we benchmark six architectures including
  an LSTM+XGBoost ensemble, and conduct ablation, temporal drift, SHAP interpretability,
  and BISG fairness analyses. The LSTM+XGBoost ensemble achieves ROC-AUC of 0.9289
  (F1: 0.6360) with a benefit-cost ratio of 6:1. XGBoost demonstrates the strongest
  temporal stability (delta-AUC = -0.0017 versus -0.0626 for LSTM). The RDT-FG Regulatory
  Digital Twin meta-model translates metrics into four regulator-specific health scores
  and a composite Regulatory Fitness Index for continuous compliance monitoring. The
  RGF-AFFD is the first integrated deployment blueprint to simultaneously satisfy
  OCC, SR 11-7, CFPB, and FinCEN requirements, supported by a community bank implementation
  vignette and four evidence-based policy recommendations.'
tags:
- clippings
id: cc7c3aa2cc864e8c
source_type: academic_paper
tldr: 提出美国银行业AI反欺诈监管治理框架RGF-AFFD，集成OCC、SR 11-7、CFPB与FinCEN四项合规要求
objective_summary: 该论文提出了RGF-AFFD三层治理架构，在IEEE-CIS（590,540笔交易）和ULB（284,807笔交易）数据集上基准测试了六种模型。LSTM+XGBoost集成模型达到ROC-AUC
  0.9289，效益成本比6:1。通过RDT-FG监管数字孪生元模型将指标转化为四项监管健康评分，
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - OCC
  - CFPB
  - FinCEN
  technologies:
  - LSTM
  - XGBoost
  - SHAP
  - BISG
  - RGF-AFFD
  - RDT-FG
  - IEEE-CIS
  key_people: []
key_logic_flow:
- 美国金融机构在部署AI反欺诈检测时面临OCC 2011-12公告、SR 11-7、CFPB AI通函和FinCEN BSA/SAR四项监管框架各自为政的合规困境，缺少覆盖模型全生命周期的集成治理方案。
- 论文提出RGF-AFFD三层治理架构，将监管合规要求与模型开发、验证和监控生命周期相连接，这是首个同时满足四项联邦监管框架的集成部署蓝图。
- 在IEEE-CIS（590,540笔交易）和ULB（284,807笔交易）两个数据集上对六种架构进行基准测试，LSTM+XGBoost集成模型达到ROC-AUC
  0.9289（F1分数0.6360），效益成本比6:1。
- XGBoost在时间稳定性上表现最优（delta-AUC = -0.0017），优于LSTM（delta-AUC = -0.0626）；论文还进行了消融实验、时间漂移分析、SHAP可解释性分析和BISG公平性分析。
- RDT-FG监管数字孪生元模型将模型指标转化为四个面向具体监管机构的健康评分和一个综合监管适应性指数，用于持续合规监控。
- 论文附带社区银行实施案例和四项基于证据的政策建议，为不同规模金融机构提供落地路径。
---

# Computer Science > Machine Learning

# Title:A Regulatory Governance Framework for AI-Driven Financial Fraud Detection in U.S. Banking: Integrating OCC, SR 11-7, CFPB, and FinCEN Compliance Requirements for Model Development, Validation, and Monitoring Lifecycles

View PDFAbstract:U.S. financial institutions deploying AI-based fraud detection face a fragmented compliance landscape spanning four regulatory frameworks -- OCC Bulletin 2011-12, SR 11-7, the CFPB AI circular, and FinCEN BSA/SAR requirements -- with no integrated governance life cycle connecting these requirements to model development, validation, and monitoring practice. This paper presents the Regulatory Governance Framework for AI-Driven Financial Fraud Detection (RGF-AFFD), a three-tier governance architecture empirically anchored in a multi-study empirical program. Using the IEEE-CIS dataset (590,540 transactions) and ULB benchmark (284,807 transactions), we benchmark six architectures including an LSTM+XGBoost ensemble, and conduct ablation, temporal drift, SHAP interpretability, and BISG fairness analyses. The LSTM+XGBoost ensemble achieves ROC-AUC of 0.9289 (F1: 0.6360) with a benefit-cost ratio of 6:1. XGBoost demonstrates the strongest temporal stability (delta-AUC = -0.0017 versus -0.0626 for LSTM). The RDT-FG Regulatory Digital Twin meta-model translates metrics into four regulator-specific health scores and a composite Regulatory Fitness Index for continuous compliance monitoring. The RGF-AFFD is the first integrated deployment blueprint to simultaneously satisfy OCC, SR 11-7, CFPB, and FinCEN requirements, supported by a community bank implementation vignette and four evidence-based policy recommendations.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.