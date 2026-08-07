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
pipeline_stage: ingested
id: 5fa3feed9e83f3bb
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