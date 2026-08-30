---
title: CFD-Guided Detection of Concept Drift in Multimodal Physiologic Signals
source: https://arxiv.org/abs/2608.07759
author:
- '[[Farouk Ganiyu Adewumi, Timothy Oladunni, Rochak Ghimire, Kosisochukwu Ogbuanya,
  Sanaa Reeves, Sandy Akoy]]'
published: '2026-08-12'
created: '2026-08-12'
manifest_dates:
- '2026-08-12'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: a9ffe55ffe02f51d
---

# Electrical Engineering and Systems Science > Signal Processing

# Title:CFD-Guided Detection of Concept Drift in Multimodal Physiologic Signals

View PDF HTML (experimental)Abstract:Cardiovascular AI models can classify clean elec- trocardiogram (ECG) signals, but real wearable signals change because of motion, breathing, posture, sensor contact, and true clinical deterioration. This paper asks when a model should keep its prediction, change it, or flag uncertainty. We propose a physiologic stability framework, called PECS, that compares changes inside the model with measurable changes in the signal. ECG is treated as the main cardiac signal, photoplethysmography (PPG) adds pulse and vascular information, and respiration is used only when ECG and PPG disagree. We test the framework on PTB-XL at pilot and full scales and on synchronized BIDMC and MIMIC waveform cohorts. The PTB-XL pilot and full- scale analyses selected different domain pairs, and the strongest cross-modal pair also changed across BIDMC and MIMIC, showing that adding every available signal is not always the best choice. PECS outperformed the evaluated drift-detection baseline implementations, reaching drift classification accuracy (DCA) of 0.8786 on expanded BIDMC and 0.9560 on MIMIC. The MIMIC results also showed that respiration can help during disagreement cases, but it should be used selectively rather than as an automatic override. Overall, the results support PECS as a candidate monitoring framework for wearable cardiovascular AI while highlighting the need for scale-aware domain selection and interpretable trust routing

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.