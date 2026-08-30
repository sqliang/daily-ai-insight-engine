---
title: Daybreak models are now available on AWS
source: https://openai.com/index/daybreak-models-are-now-available-on-aws
author: []
published: Tue, 11 Aug 2026 10:00:00 GMT
created: '2026-08-12'
manifest_dates:
- '2026-08-12'
- '2026-08-13'
- '2026-08-14'
description: OpenAI and AWS are making Daybreak cybersecurity capabilities available
  through Amazon Bedrock to support enterprise security workflows.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 5d3aff0aba5d0b8a
source_type: tech_blog
tldr: OpenAI 宣布其网络安全模型产品 Daybreak（含 Blue 与 Red 两个访问层级）正式上线 Amazon Bedrock，企业可在现有 AWS
  环境中调用前沿网络防御与漏洞研究能力。
objective_summary: OpenAI 于 2026 年发布公告，将 Daybreak 网络安全模型能力通过 Amazon Bedrock 向符合条件的企业客户提供。Daybreak
  Blue 面向授权防御性安全工作，提供包括 GPT-5.6 Sol 在内的前沿通用模型；Daybreak Red 面向授权漏洞研究、漏洞利用验证和安全测试，提供专门训练的网络安全模型。客户获批加入
  Daybreak Access 后，可通过 Amazon Bedrock 控制台或 Responses API 的 bedrock-mantle 端点访问这些模型。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - OpenAI
  - Amazon Web Services
  technologies:
  - Daybreak
  - Daybreak Blue
  - Daybreak Red
  - GPT-5.6 Sol
  - Amazon Bedrock
  - Responses API
  - bedrock-mantle endpoint
  key_people: []
key_logic_flow:
- OpenAI 此前已将前沿模型与 Codex 引入 AWS，本次进一步把 Daybreak 能力通过 Amazon Bedrock 提供给企业客户。
- Daybreak Access 包含 Blue 与 Red 两个访问层级，分别服务于授权防御性安全工作和授权进攻性安全研究。
- Daybreak Blue 提供 GPT-5.6 Sol 等前沿通用模型，并配备针对防御性安全工作的安全护栏。
- Daybreak Red 提供专门训练的网络安全模型，支持漏洞研究、利用验证、安全测试、利用复现与缓解方案开发。
- 符合条件的企业客户在获批加入 Daybreak Access 后，可通过 Amazon Bedrock 控制台或 Responses API 的 bedrock-mantle
  端点调用模型。
- 该合作旨在让企业利用现有 AWS 的安全、治理与运维流程，将前沿 AI 网络安全能力投入生产。
object_mentions:
- object_type: product
  name: Daybreak
  canonical_name: OpenAI Daybreak
  url: https://openai.com/index/daybreak-models-are-now-available-on-aws
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - OpenAI 宣布 Daybreak 能力现可通过 Amazon Bedrock 提供，Blue 与 Red 两个访问层级均已在 AWS 上线。
  - Daybreak 模型用于加速漏洞研究、检测工程、事件响应、利用复现与缓解方案开发等复杂安全流程。
  - 企业客户获批加入 Daybreak Access 后，可通过 Amazon Bedrock 控制台或 Responses API 的 bedrock-mantle
    端点访问模型。
  article_id: 5d3aff0aba5d0b8a
- object_type: product
  name: Daybreak Access
  canonical_name: OpenAI Daybreak Access
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Daybreak Red 与 Daybreak Blue 均要求客户先注册并获批加入 Daybreak Access。
  - 通过 Daybreak Access，防御方可以在其现有 AWS 环境中使用 OpenAI 的前沿网络模型。
  - Daybreak Access 设有两个访问层级：Blue 面向防御性安全工作，Red 面向授权漏洞研究与利用验证。
  article_id: 5d3aff0aba5d0b8a
- object_type: product
  name: Daybreak Blue
  canonical_name: OpenAI Daybreak Blue
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Daybreak Blue 提供访问前沿通用模型的权限，包括 GPT-5.6 Sol，并配备面向授权防御性安全工作的安全护栏。
  - 该层级已在 AWS 上线，面向需要开展防御性安全工作的授权客户。
  - 与 Red 层级不同，Blue 侧重通用模型能力在防御场景中的安全使用。
  article_id: 5d3aff0aba5d0b8a
- object_type: product
  name: Daybreak Red
  canonical_name: OpenAI Daybreak Red
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Daybreak Red 提供访问专门训练的网络安全模型的权限，用于授权漏洞研究、利用验证与安全测试。
  - 该层级支持复杂工作流，包括利用复现与缓解方案开发。
  - Daybreak Red 与 Daybreak Blue 一样，需要客户先加入 Daybreak Access 才能使用。
  article_id: 5d3aff0aba5d0b8a
- object_type: model
  name: GPT-5.6 Sol
  canonical_name: GPT-5.6 Sol
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Daybreak Blue 提供的前沿通用模型中明确包含 GPT-5.6 Sol。
  - GPT-5.6 Sol 作为 Daybreak Blue 可访问的模型之一，配备面向授权防御性安全工作的安全护栏。
  - OpenAI 未在文中进一步披露 GPT-5.6 Sol 的技术细节或训练数据。
  article_id: 5d3aff0aba5d0b8a
- object_type: product
  name: Amazon Bedrock
  canonical_name: Amazon Bedrock
  url: https://aws.amazon.com/bedrock/
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - OpenAI 选择通过 Amazon Bedrock 向符合条件的企业客户提供 Daybreak 能力。
  - 客户可在其已用于构建、保护和运行软件的 AWS 环境中使用 Daybreak。
  - 获批客户可通过 Amazon Bedrock 控制台访问 Daybreak Red 与 Daybreak Blue。
  article_id: 5d3aff0aba5d0b8a
- object_type: product
  name: Responses API
  canonical_name: OpenAI Responses API
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 获批客户除 Bedrock 控制台外，还可通过 Responses API 的 bedrock-mantle 端点访问 Daybreak 模型。
  - 该 API 路径为客户提供了一种程序化调用 Daybreak 能力的方式。
  - 文中未详细说明 Responses API 在此场景下的完整功能或定价。
  article_id: 5d3aff0aba5d0b8a
extract_result: success
---

Earlier this year, OpenAI frontier models and Codex became generally available on AWS, giving enterprises a new path to bring advanced AI into production. Today, we’re sharing the next step in our work with AWS: making Daybreak capabilities available through Amazon Bedrock.

With Daybreak Access, defenders can use frontier cyber models within their existing AWS environments. Daybreak Blue and Daybreak Red access levels are both available in AWS:

**Daybreak Blue**provides access to frontier general-purpose models, including GPT‑5.6 Sol, with safeguards tailored to authorized defensive security work.**Daybreak Red**provides access to our purpose-trained cybersecurity models for authorized vulnerability research, exploit validation, and security testing.

These models help accelerate vulnerability research, detection engineering, and incident response, from initial discovery through a validated fix. They also support complex workflows such as exploit reproduction and mitigation development.

For enterprises, adopting specialized cybersecurity capabilities requires more than model performance. It also requires security review, governance, procurement, access controls, and an operating model teams can support.

Through Amazon Bedrock, eligible customers can use Daybreak, including Daybreak Red and Daybreak Blue, within the AWS environments where they already build, secure, and operate software. This gives security teams a clearer path to apply frontier AI through familiar AWS security, governance, and operational workflows.

Together, OpenAI and AWS are helping more organizations put advanced cybersecurity capabilities to work in production.

Daybreak Red and Daybreak Blue require enrollment in Daybreak Access. Once approved, you can access the model through the Amazon Bedrock console or the Responses API using the bedrock-mantle endpoint. To learn more, see the documentation.(opens in a new window)