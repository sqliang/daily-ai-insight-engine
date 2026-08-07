---
title: A unified API for AI model routing (3 minute read)
source: https://developers.googleblog.com/a-unified-api-for-ai-model-routing/?utm_source=tldrai
author: []
published: ''
created: '2026-08-06'
manifest_dates:
- '2026-08-06'
description: TLDR AI 每日头条
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 5fa3feed9e83f3bb
source_type: news_media
tldr: Google Cloud API Gateway 在 Public Preview 中推出模型路由功能，提供轻量级无服务器入口层，接受 OpenAI 兼容请求并动态路由到
  Gemini、Claude 或 OpenAI OSS-GPT，开发者可通过 OpenAPI 3.x 规范配置路由逻辑。
objective_summary: Google Cloud 宣布其 API Gateway 在 Public Preview 阶段推出模型路由功能。该功能以轻量级、无服务器的入口层形式运行，接受
  OpenAI 兼容的请求，并将流量动态路由到 Gemini、Claude 或 OpenAI OSS-GPT 等模型。开发者通过 OpenAPI 3.x 规范中的
  x-google-api-management 扩展定义路由规则，单一路由器引用的所有后端须共享同一 Vertex 主机。API Gateway 可独立用于速率限制与
  token 追踪，也可与 Gemini Enterprise Agent Platform 配合使用。
event_type: infrastructure_update
epistemic_status: pr_statement
entities:
  companies:
  - Google Cloud
  - Anthropic
  - OpenAI
  technologies:
  - API Gateway
  - Model Routing
  - Vertex AI
  - OpenAI-compatible API
  - OpenAPI
  key_people: []
key_logic_flow:
- Google Cloud API Gateway 在 Public Preview 阶段推出模型路由功能，为开发者提供统一的 AI 模型流量入口。
- 该功能以轻量级无服务器入口层形式运行，接受 OpenAI 兼容请求，并动态路由到 Gemini、Claude 或 OpenAI OSS-GPT。
- 开发者通过 OpenAPI 3.x 规范中的 x-google-api-management 扩展配置路由逻辑，可定义多个路由器和后端。
- 单一路由器引用的所有后端必须共享同一主机（如 aiplatform.googleapis.com），路由仅在同一 Vertex 主机上切换模型与路径。
- 应用发送标准 OpenAI POST 请求后，网关会截获请求、将载荷转码为后端原生 schema，并实时完成路由。
- API Gateway 可独立用于速率限制与 token 追踪，也可与 Gemini Enterprise Agent Platform 配合使用。
object_mentions:
- object_type: product
  name: Google Cloud API Gateway
  canonical_name: Google Cloud API Gateway
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Google Cloud API Gateway 现已推出模型路由功能，该功能处于 Public Preview 阶段，为开发者提供统一的 AI 模型流量入口。
  article_id: 5fa3feed9e83f3bb
- object_type: product
  name: Model Routing
  canonical_name: API Gateway Model Routing
  url: null
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - 模型路由提供轻量级、无服务器的入口层，接受 OpenAI 兼容请求，并动态路由到 Gemini、Claude 或 OpenAI OSS-GPT 等模型。
  article_id: 5fa3feed9e83f3bb
- object_type: product
  name: Gemini Enterprise Agent Platform
  canonical_name: Gemini Enterprise Agent Platform
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - API Gateway 可独立用于速率限制和 token 追踪，也可与 Gemini Enterprise Agent Platform 无缝配合，实现严格的安全治理。
  article_id: 5fa3feed9e83f3bb
extract_result: success
impact_score:
  score: 5.5
  reason: 评分依据：这是 Google Cloud 在托管 API Gateway 上新增的模型路由能力（Public Preview），对 Google
    Cloud 生态内开发者是实用基础设施升级——可省去自建 LiteLLM 等开源代理，并借 OpenAI 兼容接口统一接入 Gemini/Claude/OSS-GPT。但限制明显：尚处公共预览阶段、单一路由器引用的所有后端必须共享同一
    Vertex 主机（无法跨云/跨供应商路由）、且 OpenRouter/LiteLLM/Portkey/Cloudflare AI Gateway 等第三方路由方案早已成熟。它改变的是
    Google Cloud 局部竞争格局（把模型代理层商品化），远未达到行业范式转移级别，故给 5.5 分。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: 同一 Vertex 主机内路由的限制与预览期稳定性，能否真正替代自建代理方案
hype_assessment:
  level: low
  reason: 文章以技术教程口吻写作，附完整 OpenAPI 3.x 配置示例和 curl 调用，客观交代了'所有后端须共享同一主机'的关键限制，未滥用'颠覆''革命性'等
    PR 词汇。仅结尾'停止管理代理、统一 AI 流量'略有宣传色彩，整体属于实打实的产品功能公告。
information_entropy: high
domain_disruption:
  technical_innovation: 将模型路由能力下沉到云厂商托管 API 网关平面：通过 OpenAPI 3.x 的 x-google-api-management
    扩展声明多路由器/多后端，网关实时将 OpenAI 兼容请求载荷转码为各后端原生 schema（Gemini generateContent、Claude
    rawPredict、OpenAI chat/completions）并完成动态路由。属于托管网关层的集成创新而非底层模型技术突破，且'仅限同一 Vertex
    主机内切换模型与路径'的约束使其功能面明显收窄。
  business_model: 强化 Vertex AI 作为多云模型聚合枢纽的商业定位，把'模型路由/代理'这一层商品化为云平台原生能力，可能挤压 LiteLLM、Portkey、OpenRouter
    等第三方代理厂商在 Google Cloud 客户群中的空间，同时以 OpenAI 兼容接口降低迁移门槛，引导企业 AI 流量留在 Google Cloud
    体系内统一计费与治理。
engineering_complexity: prototype
compound_value:
  score: 5.5
  reason: 模型路由/网关层已被验证为 AI 应用基础设施的必备环节，Google 的入场是对整个路由赛道价值的重大背书——企业无需自建代理即可在 Gemini/Claude/GPT
    之间动态切换，这降低了多云模型策略的工程门槛。但本事件的产品本身存在明显局限：所有后端必须共享同一 Vertex 主机（aiplatform.googleapis.com），无法跨云/跨厂商路由，本质上是平台锁定策略而非中立基础设施；且处于
    Public Preview 阶段，功能相较 OpenRouter/LiteLLM 等成熟方案无差异化优势。长期复利价值取决于 Google 能否放宽单主机约束并成为企业默认流量入口，目前估值中性偏积极，属'细分赛道基础设施、需持续验证'区间。
value_capture_layer: cloud_platform
moat_impact: creates_new_moat
key_beneficiaries:
- Google Cloud
- Anthropic
- Gemini Enterprise Agent Platform
competitive_casualty:
- OpenRouter
- LiteLLM
- Portkey
- Cloudflare AI Gateway
market_opportunities:
- 模型路由网关正从开源自建走向云厂商托管，开发者可将自建 LiteLLM/Portkey 等代理迁移到 Google Cloud 托管网关，围绕迁移咨询、配置审计与多云路由编排形成第三方服务机会
- API Gateway 内置速率限制与 token 追踪，可在其上构建多模型用量分析与成本优化工具，帮助企业应对 Gemini/Claude/GPT 混合调用的成本失控风险
- Google 将 Claude 与 OpenAI 模型纳入统一入口，降低了企业采用多模型策略的切换成本，催生面向'模型中立'企业应用的开发与集成商机
risk_matrix:
  regulatory: 跨模型路由意味着请求数据可能流向 Google、Anthropic、OpenAI 等多个提供商，需关注数据出境合规、GDPR/AI Act
    适用性以及美国出口管制对不同模型与地域可用性的限制
  technological: 当前仅 Public Preview 且功能受限，同一路由器后端必须共享同一 Vertex 主机、无法跨主机/跨云路由，灵活性低于
    LiteLLM 等开源方案；OpenAI 兼容层对高级特性（如工具调用、流式细节）的支持完整度待验证
  competitive: AWS Bedrock、Azure AI 等云厂商与 LiteLLM、Portkey、OpenRouter 等开源/独立网关均已布局同赛道，Google
    入场将加剧价格战与生态挤压，同时也强化了其 Vertex AI 生态的供应商锁定
  ethical: 自动路由可能导致用户无法明确知晓实际调用的模型，存在模型归因与结果透明度问题；请求转发至第三方模型提供商时，数据隐私边界与模型使用条款需向终端用户充分披露
  additional:
  - Public Preview 阶段定价与 SLA 尚未公布，成本结构存在不确定性
  - 对 Google Cloud 平台的供应商锁定风险，未来若改用其他云将面临迁移成本
confidence:
  impact: medium
  compound: medium
  hype: medium
actionable_insight: monitor
object_insights:
- object_type: product
  name: Google Cloud API Gateway
  canonical_name: Google Cloud API Gateway
  url: null
  positioning: Google Cloud 提供的轻量级无服务器 API 入口层，在 Public Preview 阶段新增统一 AI 模型路由能力，接受
    OpenAI 兼容请求并将其分发到多个模型后端。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - AI 应用开发者
  - 企业平台工程团队
  - 需要统一多模型接入的运维团队
  product_signal: 以无服务器入口层接受 OpenAI 兼容请求，可动态路由到 Gemini、Claude 与 OpenAI OSS-GPT，并独立提供速率限制与
    token 追踪能力。
  market_signal: 以官方云服务身份切入统一的 AI 模型路由市场，与自建开源代理及第三方网关形成直接竞争。
  differentiation: 通过 OpenAPI 3.x 的 x-google-api-management 扩展声明路由规则，开发者无需维护代理基础设施即可统一
    AI 流量入口。
  watch_reason: Google Cloud 将模型路由内建到官方 API Gateway，标志云厂商正从单一模型提供商向统一 AI 流量入口演进；其
    OpenAI 兼容接口与多模型路由策略可能重塑企业 AI 网关选型格局，值得持续跟踪其 Public Preview 转 GA 的进展。
  risk_notes:
  - 该功能目前处于 Public Preview 阶段，路由能力与稳定性尚未经过大规模生产环境验证。
  - 单一路由器引用的所有后端必须共享同一 Vertex 主机，跨主机路由场景受到限制。
  score: 7.0
  article_ids:
  - 5fa3feed9e83f3bb
  evidence_snippets:
  - Google Cloud API Gateway 现已推出模型路由功能，该功能处于 Public Preview 阶段，为开发者提供统一的 AI 模型流量入口。
- object_type: product
  name: Model Routing
  canonical_name: API Gateway Model Routing
  url: null
  positioning: Google Cloud API Gateway 中新增的模型路由能力，以轻量级无服务器入口层接受 OpenAI 兼容请求，并将流量动态路由到
    Gemini、Claude 或 OpenAI OSS-GPT 等模型。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 构建多模型 AI 应用的开发者
  - 希望避免硬编码模型端点的平台团队
  product_signal: 支持通过 OpenAPI 3.x 规范的 x-google-api-management 扩展定义多个路由器与后端，网关实时截获请求并转码为后端原生
    schema。
  market_signal: 模型路由正在成为云平台的基础能力，降低开发者自建和维护开源 AI 代理的运维成本与复杂度。
  differentiation: 路由仅在同一 Vertex 主机上切换模型与路径，可与 Gemini Enterprise Agent Platform 无缝配合形成治理到路由的完整链路。
  watch_reason: 模型路由以声明式 OpenAPI 配置取代手写代理逻辑，代表云厂商统一 AI 流量入口的产品化方向；其动态转码与多模型切换能力可降低企业多供应商接入成本，值得持续关注后续能力扩展与生产化进度。
  risk_notes:
  - 路由仅支持在同一 Vertex 主机上切换模型与路径，无法跨不同主机路由，灵活性有限。
  - 该功能尚处 Public Preview，依赖 Google Cloud 生态，存在厂商锁定风险。
  score: 7.0
  article_ids:
  - 5fa3feed9e83f3bb
  evidence_snippets:
  - 模型路由提供轻量级、无服务器的入口层，接受 OpenAI 兼容请求，并动态路由到 Gemini、Claude 或 OpenAI OSS-GPT 等模型。
- object_type: product
  name: Gemini Enterprise Agent Platform
  canonical_name: Gemini Enterprise Agent Platform
  url: null
  positioning: Google Cloud 面向企业场景的 AI Agent 平台，可与 API Gateway 配合，将 Agent 出口流量经安全治理后交由网关完成动态模型路由。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 企业级 AI Agent 平台团队
  - 有严格安全治理需求的大型组织
  product_signal: 支持将 Agent 的出口流量通过 Agent Gateway 进行严格安全治理，再传递给 API Gateway 处理动态路由，实现企业级管控链路。
  market_signal: null
  differentiation: 与 API Gateway 模型路由能力原生集成，形成从 Agent 安全治理到多模型路由的端到端企业方案。
  watch_reason: 作为 Google Cloud 企业级 Agent 平台，其与 API Gateway 的配合方式展示了云厂商将 Agent 治理与模型路由整合为一站式链路的产品方向，值得跟踪其在企业市场的落地进展。
  risk_notes:
  - 文章对 Gemini Enterprise Agent Platform 的描述较为简略，其独立能力与市场成熟度尚需更多证据支撑。
  - 该平台与 API Gateway 的集成仍处早期，端到端方案的实际生产效果有待验证。
  score: 5.0
  article_ids:
  - 5fa3feed9e83f3bb
  evidence_snippets:
  - API Gateway 可独立用于速率限制和 token 追踪，也可与 Gemini Enterprise Agent Platform 无缝配合，实现严格的安全治理。
---

When building AI applications, developers need the freedom to route traffic to the best model for the job without hardcoding endpoints or managing open-source proxies. Google Cloud API Gateway now offers model routing in Public Preview to solve this. It provides a lightweight, serverless ingress layer that accepts OpenAI-compatible requests and dynamically routes them to Gemini, Claude, or OpenAI OSS-GPT.

API Gateway can be used standalone for simple rate limiting and token tracking, or paired seamlessly with the Gemini Enterprise Agent Platform. For example, you can route your agent's egress through Agent Gateway for strict security governance, and then pass the request to API Gateway to handle dynamic routing to Google-hosted LLMs. Here is a step-by-step guide on how to configure your routing logic.

Setting up your model routing logic takes just a few steps:

`x-google-api-management`

extension block.```
openapi: 3.0.4
info:
title: OpenAPI 3.x spec using Model Routing
description: Using Model Routing in an OAS 3.x spec
version: 1.0.0
x-google-api-management:
backends:
gemini-35-flashlite:
address: >-
https://aiplatform.googleapis.com/v1/projects/YOUR_PROJECT_ID/locations/global/publishers/google/models/gemini-3.5-flash-lite:generateContent
deadline: 60.0
pathTranslation: CONSTANT_ADDRESS
anthropic-claude-opus-47:
address: >-
https://aiplatform.googleapis.com/v1/projects/YOUR_PROJECT_ID/locations/global/publishers/anthropic/models/claude-opus-4-7:rawPredict
deadline: 60.0
pathTranslation: CONSTANT_ADDRESS
openai-gpt-oss-120b:
address: >-
https://aiplatform.googleapis.com/v1/projects/YOUR_PROJECT_ID/locations/global/endpoints/openapi/chat/completions
deadline: 60.0
pathTranslation: CONSTANT_ADDRESS
ai:
models:
routing:
routers:
# Router 1: route between Gemini (default) and Claude.
gemini-claude-router:
defaultModel:
backend: gemini-35-flashlite
targetModel: google/gemini-3.5-flash-lite
rules:
- model: "claude-opus-4-7"
backend: anthropic-claude-opus-47
targetModel: anthropic/claude-opus-4-7
# Router 2: route between OpenAI GPT (default) and Gemini.
openai-gemini-router:
defaultModel:
backend: openai-gpt-oss-120b
targetModel: openai/gpt-oss-120b-maas
rules:
- model: "gemini-3.5-flash-lite"
backend: gemini-35-flashlite
targetModel: google/gemini-3.5-flash-lite
servers:
- url: "https://my-gateway-url.com"
paths:
/v1/chat/gemini-claude:
post:
summary: "Endpoint:defaults to Gemini & Claude as an option."
operationId: "chatGeminiClaude"
x-google-model-router: gemini-claude-router
responses:
'200':
description: "OK"
/v1/chat/openai-gemini:
post:
summary: "Endpoint:defaults to OpenAI & Gemini as an option."
operationId: "chatOpenAIGemini"
x-google-model-router: openai-gemini-router
responses:
'200':
description: "OK"
```


**Note:** All backends referenced by a single router must share the same host (for example, aiplatform.googleapis.com). Routing selects a different model and path on that shared Vertex host — it does not route across different hosts.

2.** Deploy the Gateway:** Deploy your updated API config so the Gateway is active and ready to process traffic.

3. **Send standard requests:** Your application simply sends a standard OpenAI `POST /v1/chat/gemini-claude`

or `POST /v1/chat/openai-gemini`

request. The Gateway intercepts it, transcodes the payload to the native schema of the backend, and routes it on the fly. As an example (use appropriate values for `$API_KEY`

and `my-gateway-url.com`

) :

```
curl -X POST "https://my-gateway-url.com/v1/chat/gemini-claude" \
-H "content-type: application/json" \
-H "x-api-key: $API_KEY" \
-d '{
"model": "claude-opus-4-7",
"messages": [
{"role": "user", "content": "Introduce yourself in 5 words"}
]
}'
```


Model routing is now available in Public Preview for API Gateway. To stop managing proxies and start unifying your AI traffic, check out our documentation to deploy your first model router today.