---
title: A survey detection channel overrides the pixels in an astronomical foundation
  model, and biases tomographic mean redshifts
source: https://arxiv.org/abs/2608.23626
author:
- '[[Ihor Kendiukhov]]'
published: '2026-08-26'
created: '2026-08-26'
manifest_dates:
- '2026-08-26'
- '2026-08-27'
description: 'arXiv:2608.23626v1 Announce Type: new Abstract: Foundation models for
  astronomy are trained on survey pixels together with the catalogue products derived
  from those pixels. Those catalogues are incomplete at a measurable rate, and a model
  trained on both inherits that incompleteness as a systematic. We audit AION-1, a
  39-modality transformer trained on more than 200 million objects, using causal interventions
  on its inputs. Holding the image tokens byte-identical and editing only the survey
  segmentation map changes every quantity the model reports -- flux, size, ellipticity,
  redshift -- by 110-4400 times a matched placebo. The mechanism is detection gating,
  presence at the field centre (r = 0.47), not the light the mask encloses (r = 0.30);
  across 322 real blends the model ignores how the pipeline partitioned the light
  (R = -0.006). Nor is the preference specific to that channel: contradicted catalogue
  photometry leaves the model nine times worse than supplying no metadata at all.
  The Legacy Survey pipeline leaves 3.68% of targets with no segment covering their
  position. Propagating that rate, with a miss represented by the fields the pipeline
  actually returns, shifts tomographic mean redshifts by a median 0.71 times the LSST
  DESC requirement over 40 assignments and exceeds it in 12; observed positional errors
  take the worst bin to 8.3 times. Drawing the misses by their measured magnitude
  dependence rather than uniformly does not change it. Spectroscopy removes the effect,
  withholding the detection channel removes it at no measurable cost, and the effect
  grows with model scale. Two further limits lie in the tokeniser: its image codec
  resolves 28 effective states on source patches against 934 for the spectrum codec,
  and the redshift readout is quantisation-limited. Sparse dictionaries are unreliable
  causal handles: across 15, recovery spans 26-75% and moves up to 18 points on the
  seed alone.'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: 3fcba86f0c2cae9d
---

# Computer Science > Artificial Intelligence

# Title:A survey detection channel overrides the pixels in an astronomical foundation model, and biases tomographic mean redshifts

View PDF HTML (experimental)Abstract:Foundation models for astronomy are trained on survey pixels together with the catalogue products derived from those pixels. Those catalogues are incomplete at a measurable rate, and a model trained on both inherits that incompleteness as a systematic. We audit AION-1, a 39-modality transformer trained on more than 200 million objects, using causal interventions on its inputs.

Holding the image tokens byte-identical and editing only the survey segmentation map changes every quantity the model reports -- flux, size, ellipticity, redshift -- by 110-4400 times a matched placebo. The mechanism is detection gating, presence at the field centre (r = 0.47), not the light the mask encloses (r = 0.30); across 322 real blends the model ignores how the pipeline partitioned the light (R = -0.006). Nor is the preference specific to that channel: contradicted catalogue photometry leaves the model nine times worse than supplying no metadata at all.

The Legacy Survey pipeline leaves 3.68% of targets with no segment covering their position. Propagating that rate, with a miss represented by the fields the pipeline actually returns, shifts tomographic mean redshifts by a median 0.71 times the LSST DESC requirement over 40 assignments and exceeds it in 12; observed positional errors take the worst bin to 8.3 times. Drawing the misses by their measured magnitude dependence rather than uniformly does not change it. Spectroscopy removes the effect, withholding the detection channel removes it at no measurable cost, and the effect grows with model scale.

Two further limits lie in the tokeniser: its image codec resolves 28 effective states on source patches against 934 for the spectrum codec, and the redshift readout is quantisation-limited. Sparse dictionaries are unreliable causal handles: across 15, recovery spans 26-75% and moves up to 18 points on the seed alone.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.