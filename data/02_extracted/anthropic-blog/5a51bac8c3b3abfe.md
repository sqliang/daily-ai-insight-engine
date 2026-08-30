---
title: Frontier Model Security
source: https://www.anthropic.com/news/frontier-model-security
author: []
published: '2026-08-26'
created: '2026-08-27'
manifest_dates:
- '2026-08-27'
- '2026-08-28'
- '2026-08-29'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 5a51bac8c3b3abfe
source_type: tech_blog
tldr: Anthropic 发布《Frontier model security》文章，提出以「两人控制」多方授权机制保障前沿 AI 模型的安全开发、训练与部署，并建议政府将前沿
  AI 行业视为关键基础设施，先从自愿合规逐步过渡到强制监管。
objective_summary: Anthropic 于官网发布《Frontier model security》一文，分享其保障前沿 AI 模型安全开发的具体步骤，并面向行业与政府提出网络安全最佳实践建议。文章主张所有前沿模型系统必须采用「两人控制」的多方授权设计，确保没有任何个人对生产关键环境拥有持久访问权限。Anthropic
  建议政府与前沿 AI 实验室短期内保护先进模型、模型权重及支撑研究，并将前沿 AI 行业视为类似「关键基础设施」的领域开展公私合作，必要时通过政府采购或监管权力强制合规。
event_type: policy_and_safety
epistemic_status: pr_statement
entities:
  companies:
  - Anthropic
  technologies:
  - frontier model
  - two-party control
  - multi-party authorization to AI-critical infrastructure design
  key_people: []
key_logic_flow:
- 前沿 AI 模型的发展可能颠覆国家内部及国家之间的经济与安全格局，因此前沿 AI 研究和模型必须以远超普通商业技术的安全标准加以保护，防止被窃取或滥用。
- Anthropic 认为保护先进 AI 系统必须采用「两人控制」机制，并将其应用于开发、训练、托管和部署前沿 AI 模型的全部系统。
- 该机制体现为系统设计中没有任何个人对生产关键环境拥有持久访问权限，任何访问都须向同事申请限时授权并提供业务理由。
- 短期内政府和前沿 AI 实验室需保护先进模型、模型权重及其相关研究，并将前沿 AI 行业视为类似「关键基础设施」的领域开展公私合作。
- 相关安全措施可先以自愿安排形式推行，但必要时政府可运用采购或监管权力强制要求合规。
object_mentions: []
extract_result: success
---

# Frontier model security

As the capabilities of frontier artificial intelligence models continue to increase rapidly, ensuring the security of these systems has become a critical priority. In our previous posts, we’ve focused on Anthropic’s approach to safety, and Claude’s capabilities and applications. In this post, we are sharing some of the steps we are taking to ensure our models are developed securely. We hope to advance public discussion about how all labs can deploy top models securely, as well as share recommendations for government regulatory approaches that encourage adoption of strong cybersecurity practices. Below we discuss some of our recommendations for cybersecurity best practices, which Anthropic itself is in the process of implementing.

## Summary

Future advanced AI models have the potential to upend economic and national security affairs within and among nation-states. Given the strategic nature of this technology, frontier AI research and models must be secured to levels far exceeding standard practices for other commercial technologies in order to protect them from theft or misuse.

In the near term, governments and frontier AI labs must be ready to protect advanced models and model weights, and the research that feeds into them. This should include measures such as the development of robust best practices widely diffused among industry, as well as treating the advanced AI sector as something akin to “critical infrastructure” in terms of the level of public-private partnership in securing these models and the companies developing them.

Many of these measures can begin as voluntary arrangements, but in time it may be appropriate to use government procurement or regulatory powers to mandate compliance.

## Cybersecurity Best Practices

We believe “two-party control” is necessary to secure advanced AI systems. Two-party control is already used in a range of domains; for example, two people with two keys are needed to open the most secure vaults, and multi-party review patterns have been applied in manufacturing (GMP, ISO 9001), food (FSMA PCQI, ISO 22000), medical (ISO 13485) and finance tech (SOX).

- This pattern should be applied to all systems involved in the development, training, hosting, and deployment of frontier AI models.
- This pattern is already in widespread use within major tech companies to defend against the most advanced threat actors and mitigate insider risk.
- It is manifested as a system design where no person has persistent access to production-critical environments, and they must ask a coworker for time-limited access with a business justification for that request.
- Even emerging AI labs, without large enterprise resources, can implement these controls.


We call this **multi-party authorization to AI-critical infrastructure design**. This is a leading security requirement that depends on the gamut of cybersecurity best practices to implement correctly.