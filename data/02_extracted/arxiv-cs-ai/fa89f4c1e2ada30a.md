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