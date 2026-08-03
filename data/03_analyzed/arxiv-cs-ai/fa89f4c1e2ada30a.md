---
title: Atmospheric Diffusion-Guided Spatio-Temporal Transformer for Nuclear Radiation
  Forecasting
source: https://arxiv.org/abs/2607.24774
author:
- '[[Tengfei Lyu, Jindong Han, Hao Liu]]'
published: '2026-07-29'
created: '2026-07-29'
manifest_dates:
- '2026-07-29'
description: 'arXiv:2607.24774v1 Announce Type: new Abstract: Nuclear radiation, the
  energy released during atomic decay, poses persistent risks to public health and
  the environment, and concerns have only grown since the Fukushima accident and the
  recent commencement of treated-water discharge. Modern monitoring networks now record
  radiation levels and accompanying weather conditions at thousands of stations, opening
  the door to nationwide forecasting that can inform emergency response, agricultural
  advisories, and routine public-safety decisions. However, turning this abundance
  of monitoring data into reliable forecasts is difficult for three reasons. First,
  the time series at each station are highly non-stationary, shaped by radioactive
  decay, weather variability, and irregular human interventions. Second, monitoring
  stations are severely unevenly distributed in space. Roughly 78% of Japan''s stations
  sit in less than 6% of the country, clustered near Fukushima, which breaks the assumptions
  of standard graph-based models. Third, radiation co-evolves with heterogeneous context
  such as wind, temperature, and humidity through atmospheric transport processes
  that purely data-driven models struggle to capture from observations alone. In this
  study, we introduce NRFormer+, a spatio-temporal Transformer for nationwide nuclear
  radiation forecasting. NRFormer+ couples non-stationary temporal attention and density-adaptive
  spatial attention with a new atmospheric diffusion module that estimates how meteorology
  drives radiation dispersion and injects this physical signal into the network as
  an architectural prior. NRFormer+ delivers state-of-the-art accuracy on both datasets
  across all 13 baselines, reducing sudden-change MAE by up to 19.1% over the strongest
  baseline at comparable inference latency. Our code and datasets are publicly available
  at https://github.com/tfeilyu/NRFormer_Plus.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: fa89f4c1e2ada30a
source_type: academic_paper
tldr: 一篇 arXiv 论文提出 NRFormer+，一种用于全国核辐射预测的时空 Transformer。它融合非平稳时间注意力、密度自适应空间注意力与大气扩散物理模块，在全部
  13 个基线上于两个数据集取得最优精度，突发变化 MAE 最高降低 19.1%。
objective_summary: 这篇 arXiv 预印本针对福岛事故及处理后废水排放引发的核辐射持续风险，提出 NRFormer+ 时空 Transformer
  用于全国尺度核辐射预测。该方法应对三大难题：站点时间序列高度非平稳、约 78% 的日本监测站集中在不到 6% 国土面积的福岛周边、以及辐射随风温湿度等气象过程扩散难以被纯数据驱动模型捕获。模型将非平稳时间注意力、密度自适应空间注意力与新增的大气扩散物理先验相结合，在两个数据集上全部
  13 个基线的对比中取得最优精度，突发变化 MAE 相对最强基线最高降低 19.1% 且推理延迟相当。论文代码与数据集已通过 arXiv 页面公开提供。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - arXiv
  technologies:
  - NRFormer+
  - Spatio-Temporal Transformer
  - Atmospheric Diffusion Module
  - Density-Adaptive Spatial Attention
  key_people: []
key_logic_flow:
- 研究背景是福岛事故与处理后废水排放加剧了核辐射对公共健康和环境的持续风险，现代监测网络已在数千个站点记录辐射水平及伴随气象数据，为全国尺度预测提供基础。
- 作者归纳出三大技术挑战：各站点时间序列高度非平稳、监测站空间分布严重不均（约 78% 的站点聚集在不到 6% 国土面积的福岛附近）、辐射通过大气输运与风温湿度等异质气象背景协同演化。
- 论文提出 NRFormer+，将非平稳时间注意力与密度自适应空间注意力耦合，并新增大气扩散模块估算气象对辐射扩散的驱动作用，以架构先验形式注入网络。
- 实验在两个数据集上对比全部 13 个基线，NRFormer+ 取得最优精度，突发变化 MAE 相比最强基线最高降低 19.1%，且推理延迟相当。
- 论文声明其代码与数据集已公开提供，便于复现和后续研究。
object_mentions:
- object_type: model
  name: NRFormer+
  canonical_name: NRFormer+
  url: https://arxiv.org/abs/2607.24774
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - NRFormer+ 是一种面向全国核辐射预测的时空 Transformer，将非平稳时间注意力与密度自适应空间注意力相结合，并新增大气扩散模块估算气象对辐射扩散的驱动作用。
  - NRFormer+ 在全部 13 个基线上于两个数据集取得最优精度，突发变化 MAE 相比最强基线最高降低 19.1%，且推理延迟相当。
  article_id: fa89f4c1e2ada30a
- object_type: paper
  name: Atmospheric Diffusion-Guided Spatio-Temporal Transformer for Nuclear Radiation
    Forecasting
  canonical_name: Atmospheric Diffusion-Guided Spatio-Temporal Transformer for Nuclear
    Radiation Forecasting
  url: https://arxiv.org/abs/2607.24774
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文针对福岛事故后核辐射监测数据高度非平稳、监测站空间分布不均等问题，提出 NRFormer+ 模型用于全国核辐射预测。
  - 论文声明其代码与数据集已通过 arXiv 页面公开提供，支持后续复现与研究。
  article_id: fa89f4c1e2ada30a
extract_result: success
impact_score:
  score: 2.5
  reason: 该论文是核辐射预测这一垂直领域的方法学改进，将非平稳时间注意力、密度自适应空间注意力与大气扩散物理先验耦合，属于'领域内 SOTA'而非范式级创新。其对主流
    AI 生态几乎无短期冲击，影响范围局限在辐射监测、时空序列预测等小圈子；不过物理先验以架构注入的建模思路对相邻时空预测方向有一定参考价值，且实验结果具体可复现，故给出中等偏低评分。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: 大气扩散物理先验注入时空 Transformer 的方法能否迁移到空气污染、气象预报等相邻时空预测场景
hype_assessment:
  level: low
  reason: 论文为 arXiv 预印本，宣称在全部 13 个基线上取得最优、突发变化 MAE 最高降低 19.1%，并公开代码与数据集以供复现。表述克制、无'颠覆/革命性'等
    PR 滥用词汇，实验结果具体且可证伪，属于实打实的学术干货，水分较低。
information_entropy: medium
domain_disruption:
  technical_innovation: 针对监测站空间分布极端不均（约 78% 站点集中在不到 6% 国土面积的福岛周边）导致标准图模型假设失效的问题，提出密度自适应空间注意力；并将大气扩散物理过程以架构先验形式注入
    Transformer，使气象驱动辐射输运的信号可被网络显式建模，弥补纯数据驱动模型在物理机制捕捉上的短板。
  business_model: 纯学术论文，暂无直接商业模式。潜在商业化路径为核安全与环境监测平台、应急响应辅助决策系统及农业安全预警体系，对福岛后日本的辐射监测网络具备落地价值；同一套'物理先验+时空注意力'框架亦可复用到空气污染扩散、气象要素预报等相近的时空预测场景。
engineering_complexity: prototype
compound_value:
  score: 3.0
  reason: 该事件是 arXiv 学术方法创新而非商业化产品。核辐射预测属于高度垂直的公共安全领域，市场规模极小，采购主体为政府监管机构，缺乏商业变现路径、网络效应与数据飞轮，难以形成长期复利资产。NRFormer+
    的技术创新（非平稳时间注意力、密度自适应空间注意力、大气扩散物理先验注入）对通用时空预测领域有一定迁移价值，且代码与数据集开源有助于沉淀为该细分赛道的标准基线；但需持续迭代验证并在更多场景复用才能放大价值。当前判定为细分学术贡献，3-5
    年后大概率不会成为行业基石，故给予 3 分。
value_capture_layer: end_application
moat_impact: democratizes_access
key_beneficiaries:
- 日本原子力规制委员会
- 辐射环境监测网络运营方
- 福岛退役与废水处理项目运营方
- 时空预测开源研究社区
competitive_casualty:
- 传统图神经网络时空预测模型
- 纯数据驱动时序预测方案（LSTM/TCN 类）
- 依赖私有数据与闭源模型的辐射预测服务商
market_opportunities:
- 创业者可将密度自适应空间注意力与大气扩散物理先验注入的方法迁移至空气污染、海洋环境、核电站周边监测等站点分布不均的环境预测领域，开发垂直时空预测服务
- 核电站运营方与辐射安全监管机构可评估引入此类时空 Transformer 作为应急响应与核废水排放影响评估的辅助决策工具
- 论文公开的代码与数据集为团队提供了低成本复现与二次开发的基础，可用于构建辐射预测对比基准或嵌入现有环境监测平台
risk_matrix:
  regulatory: 核辐射监测数据在多数国家属敏感监管领域，数据获取、跨境使用与模型部署均可能受核安全法规和数据合规条款约束，落地前需完成合规审查
  technological: 该研究为 arXiv 预印本，尚待同行评审验证；纯数据驱动结合物理先验的可迁移性与长期泛化能力未经充分检验，且可能被更大规模的天气/气候基础模型（如
    GraphCast、盘古气象）快速覆盖
  competitive: 时空预测领域巨头密集（Google DeepMind、华为、英伟达等），通用基础模型向环境预测赛道延伸可能挤压专用小模型的生态空间，NRFormer+
    的护城河有限
  ethical: 辐射预测的误差可能引发公众恐慌或安全懈怠，将其用于公共安全与农业决策需建立严格的不确定性披露机制；监测站空间分布不均可能放大预测偏差，加剧地域间风险评估的不平等
  additional:
  - 核辐射相关数据的敏感性可能牵涉信息发布安全与地缘政治层面的争议，公开部署需谨慎
confidence:
  impact: medium
  compound: low
  hype: low
actionable_insight: monitor
---

# Computer Science > Artificial Intelligence

# Title:Atmospheric Diffusion-Guided Spatio-Temporal Transformer for Nuclear Radiation Forecasting

View PDF HTML (experimental)Abstract:Nuclear radiation, the energy released during atomic decay, poses persistent risks to public health and the environment, and concerns have only grown since the Fukushima accident and the recent commencement of treated-water discharge. Modern monitoring networks now record radiation levels and accompanying weather conditions at thousands of stations, opening the door to nationwide forecasting that can inform emergency response, agricultural advisories, and routine public-safety decisions. However, turning this abundance of monitoring data into reliable forecasts is difficult for three reasons. First, the time series at each station are highly non-stationary, shaped by radioactive decay, weather variability, and irregular human interventions. Second, monitoring stations are severely unevenly distributed in space. Roughly 78% of Japan's stations sit in less than 6% of the country, clustered near Fukushima, which breaks the assumptions of standard graph-based models. Third, radiation co-evolves with heterogeneous context such as wind, temperature, and humidity through atmospheric transport processes that purely data-driven models struggle to capture from observations alone. In this study, we introduce NRFormer+, a spatio-temporal Transformer for nationwide nuclear radiation forecasting. NRFormer+ couples non-stationary temporal attention and density-adaptive spatial attention with a new atmospheric diffusion module that estimates how meteorology drives radiation dispersion and injects this physical signal into the network as an architectural prior. NRFormer+ delivers state-of-the-art accuracy on both datasets across all 13 baselines, reducing sudden-change MAE by up to 19.1% over the strongest baseline at comparable inference latency. Our code and datasets are publicly available at this https URL.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.