---
title: 'Adjudicated Captioning: Multi-Agent Alignment Scoring and Consensus-Distilled
  Beam Arbitration for Strict Zero-Shot Image Captioning'
source: https://arxiv.org/abs/2607.28986
author:
- '[[Duy Tran Thanh, Thien-Phuc Doan, Long Nguyen-Vu, Ngo Tan Vu Khanh]]'
published: '2026-08-04'
created: '2026-08-04'
manifest_dates:
- '2026-08-04'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: d70e5fdfc1a69c1e
---

# Computer Science > Computer Vision and Pattern Recognition

# Title:Adjudicated Captioning: Multi-Agent Alignment Scoring and Consensus-Distilled Beam Arbitration for Strict Zero-Shot Image Captioning

View PDF HTML (experimental)Abstract:Zero-shot image captioning (ZIC) describes images without paired image-caption supervision during captioner training, relying on text-only corpora and frozen pretrained image-text scorers. Existing retrieval-augmented methods score image-text alignment once, at retrieval, then commit the captioner's autoregressive beam under language-model probability alone, leaving the decoder without further visual grounding feedback. Progress has stalled, with no method improving on the strict-regime best since 2024.

We propose Adjudicated Captioning, an inference-time multi-agent framework that restores grounding feedback at multiple checkpoints over an unchanged IFCap captioner. First, we install a stronger frozen Retrieval Encoder at the input. Second, between retrieval and decoding we insert a frozen Cross-Attention Verifier that re-ranks the top-9 retrievals to top-5. Third, at the output beam we attach a learned Reranker pairing TriFuse, a multilayer perceptron, with MemAttend, a memory-attended transformer, the pipeline's only learned components; both are trained self-supervised by Borda-consensus distillation across the three frozen scorers, using no paired image-caption labels and no reference captions.

Under the inductive headline protocol, with rerankers fit on the disjoint COCO Karpathy validation beam and applied frozen to test, the framework reaches CIDEr 117.6 and SPICE 21.9 on COCO Karpathy, up from 108.0 and 20.3 for IFCap, a +9.6 CIDEr gain, and +7.7 above NES, the strongest synthetic-image-augmented method at 109.9, without retraining the captioner. A training-free fixed-fusion baseline reaches 115.8 CIDEr, so +7.8 of the +9.6 gain comes from the non-learned architectural intervention and the remaining +1.8 from the learned rerankers. The same recipe transfers off-COCO without captioner retraining: +8.1 CIDEr on Flickr30k Karpathy and +5.7 on NoCaps overall.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.