---
title: How to Deploy Your First App on FastAPI Cloud
source: https://www.kdnuggets.com/how-to-deploy-your-first-app-on-fastapi-cloud
author:
- '[[Abid Ali Awan]]'
published: 2026-05-04
created: 2026-05-07
description: Learn how to build, test, deploy, and monitor your first FastAPI Cloud
  app, a simple live gold and silver dashboard.
tags:
- clippings
id: 5c0882beadc2bc6c
source_type: news_media
tldr: FastAPI Cloud 是一个面向 FastAPI 应用的托管部署平台，支持通过 CLI 一键部署。教程以实时贵金属价格仪表盘为例，展示从项目创建、本地测试到云端部署和监控的完整流程，部署体验接近
  Vercel 或 Supabase 等现代平台。
objective_summary: KDnuggets 发表了一篇 FastAPI Cloud 部署教程，作者使用 FastAPI 构建了一个实时黄金与白银价格仪表盘应用。文章详细演示了通过
  uvx 脚手架创建项目、添加 httpx 依赖、编写异步 API 端点、本地测试，以及使用 fastapi deploy 命令一键部署到 FastAPI Cloud
  的完整流程。部署完成后用户可通过 FastAPI Cloud 仪表盘查看日志和监控应用状态。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - FastAPI Cloud
  - KDnuggets
  - Gold API
  technologies:
  - FastAPI
  - httpx
  - uv
  key_people: []
key_logic_flow:
- FastAPI Cloud 是一个用于托管 FastAPI 应用的托管平台，提供基于 CLI 的一键部署体验。
- 作者使用 uvx fastapi-new 脚手架命令创建了名为 metals-live 的项目结构。
- 应用通过 httpx 异步客户端从 Gold API 获取实时金价和银价，并在 /api/prices 端点返回 JSON 数据。
- 应用主页提供一个自动每 15 秒刷新一次的 HTML 仪表盘，展示实时贵金属价格。
- 运行 fastapi deploy 命令后，CLI 引导用户完成账户连接和应用配置，自动构建并部署到 FastAPI Cloud。
- 部署完成后应用获得 public URL，用户可通过 FastAPI Cloud 仪表盘查看日志和监控运行状态。
pipeline_stage: fact_extracted
extract_result: success
object_mentions:
- object_type: product
  name: FastAPI Cloud
  canonical_name: FastAPI Cloud
  url: https://fastapicloud.com/
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - FastAPI Cloud 是一个托管部署平台，开发者可以通过 CLI 在数秒内完成应用的部署。
  - FastAPI Cloud 提供日志查看、应用监控和集成面板等功能，体验接近 Vercel 或 Supabase 等现代平台。
  - 访问目前仍通过 waitlist 逐步开放，作者在申请数月后才获得使用权限。
  article_id: 5c0882beadc2bc6c
- object_type: project
  name: metals-live
  canonical_name: metals-live
  url: null
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - metals-live 是一个使用 FastAPI 构建的实时贵金属价格仪表盘应用，作为本教程的示例项目。
  - 该应用通过 httpx 异步请求 Gold API，在 /api/prices 返回 JSON 数据，并在主页提供每 15 秒自动刷新的 HTML 界面。
  - 部署完成后应用可通过 https://metals-live.fastapicloud.dev/ 公开访问。
  article_id: 5c0882beadc2bc6c
- object_type: project
  name: FastAPI
  canonical_name: FastAPI
  url: https://fastapi.tiangolo.com/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - FastAPI 已发展为一个更广泛的生态系统，广泛应用于 AI 和机器学习项目的现代 Web 应用构建。
  - FastAPI 提供内置开发服务器和自动生成 API 文档的能力，支持本地测试和快速迭代。
  article_id: 5c0882beadc2bc6c
- object_type: product
  name: FastAPI CLI
  canonical_name: FastAPI CLI
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - FastAPI CLI 提供 fastapi dev 命令用于本地开发服务器启动，以及 fastapi deploy 命令用于一键部署到 FastAPI Cloud。
  - fastapi deploy 命令会在部署过程中引导用户完成账户连接、应用名称和团队配置等设置。
  article_id: 5c0882beadc2bc6c
---

## \# Introduction

**[FastAPI](https://fastapi.tiangolo.com/)** has grown far beyond being just a simple Python library for serving APIs. It has become a broader ecosystem that many developers rely on to build modern web applications, especially for AI and machine learning projects. One of the reasons FastAPI became so popular is its speed, simplicity, and developer-friendly design.

  
Image from [FastAPI Cloud](https://fastapicloud.com/)

  

Now, with **[FastAPI Cloud](https://fastapicloud.com/)**, the deployment experience is becoming much easier too. Instead of spending time configuring servers and deployment pipelines, you can deploy an application in seconds using the FastAPI Cloud command-line interface (CLI). The setup feels straightforward, lightweight, and much closer to the smooth experience developers expect from modern managed platforms.

At the time of writing, access is still rolling out through a waitlist. I applied a couple of months ago and recently got access, so I wanted to put together a simple guide based on my experience. In this tutorial, I will walk through the basic setup process and show how to deploy a small FastAPI app in just a few steps.

## \# Creating the Project

In this tutorial, you will build a simple live metals dashboard using FastAPI. The app will fetch gold and silver prices from an API, return the data in JSON format, and display the values in the browser using a small HTML interface.

Before you begin, make sure you have:

- **[uv](https://docs.astral.sh/uv/)** installed for project scaffolding, or a recent supported Python version.
- A FastAPI Cloud account.

To get started, create a new FastAPI project with the official setup command:

```
uvx fastapi-new metals-live
cd metals-live
```

Within a few seconds, FastAPI will generate the project structure and install the required dependencies for you.

![FastAPI project structure after scaffolding](https://www.kdnuggets.com/wp-content/uploads/awan_deploy_first_app_fastapi_cloud_8.png)  
Image by Author

  

Next, activate the virtual environment inside the project directory.

On Linux/macOS:

```
source .venv/bin/activate
```

On Windows PowerShell:

```
.venv\Scripts\Activate.ps1
```

## \# Adding httpx

Next, install the packages the app will need. We will use **[httpx](https://www.python-httpx.org/)** to fetch live gold and silver prices from the API, and we will also make sure the standard FastAPI extras are installed so the app runs and deploys smoothly without missing dependencies.

```
uv add httpx "fastapi[standard]"
```

This command adds `httpx` for making outbound API requests and installs the standard FastAPI dependencies commonly needed for development and deployment.

## \# Replacing the Default App

Now it is time to replace the default FastAPI app with the version you will actually deploy.

This is what the default project structure looks like:

![Default FastAPI project structure](https://www.kdnuggets.com/wp-content/uploads/awan_deploy_first_app_fastapi_cloud_6.png)  
Image by Author

  

Open `main.py` and replace its contents with the custom code shown below. This version does two things: it fetches live gold and silver prices from the Gold API, and it serves a simple browser dashboard that refreshes automatically every 15 seconds.

Paste this into `main.py`:

```
import httpx
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI(title="Live Gold & Silver Prices")

GOLD_API_BASE = "https://api.gold-api.com"

async def fetch_price(symbol: str):
    url = f"{GOLD_API_BASE}/price/{symbol}"

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=502, detail=f"Failed to fetch {symbol} price")

    data = response.json()

    return {
        "symbol": data.get("symbol", symbol),
        "name": data.get("name", symbol),
        "price": data.get("price"),
        "currency": data.get("currency", "USD"),
        "updatedAt": data.get("updatedAt") or data.get("timestamp"),
    }

@app.get("/api/prices")
async def get_prices():
    gold = await fetch_price("XAU")
    silver = await fetch_price("XAG")
    return {
        "gold": gold,
        "silver": silver,
    }

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!doctype html>
    <html>
    <head>
      <meta charset="utf-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <title>Live Gold & Silver Prices</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          background: #0f1115;
          color: #ffffff;
          margin: 0;
          padding: 40px 20px;
        }
        .container {
          max-width: 900px;
          margin: 0 auto;
        }
        h1 {
          margin-bottom: 8px;
        }
        p {
          color: #b9c0cc;
        }
        .grid {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
          gap: 20px;
          margin-top: 30px;
        }
        .card {
          background: #171a21;
          border: 1px solid #2a2f3a;
          border-radius: 16px;
          padding: 24px;
        }
        .label {
          font-size: 14px;
          color: #9aa4b2;
          margin-bottom: 10px;
        }
        .price {
          font-size: 36px;
          font-weight: bold;
          margin-bottom: 8px;
        }
        .meta {
          font-size: 14px;
          color: #c6ced9;
        }
        .footer {
          margin-top: 24px;
          font-size: 13px;
          color: #8c97a8;
        }
      </style>
    </head>
    <body>
      <div class="container">
        <h1>Live Gold & Silver Prices</h1>
        <p>Prices refresh automatically every 15 seconds.</p>

        <div class="grid">
          <div class="card">
            <div class="label">Gold</div>
            <div class="price" id="gold-price">Loading...</div>
            <div class="meta" id="gold-meta"></div>
          </div>

          <div class="card">
            <div class="label">Silver</div>
            <div class="price" id="silver-price">Loading...</div>
            <div class="meta" id="silver-meta"></div>
          </div>
        </div>

        <div class="footer" id="updated"></div>
      </div>

      <script>
        async function loadPrices() {
          try {
            const res = await fetch('/api/prices');
            const data = await res.json();

            const gold = data.gold;
            const silver = data.silver;

            document.getElementById('gold-price').textContent =
              \`${gold.price ?? 'N/A'} ${gold.currency ?? ''}\`;

            document.getElementById('silver-price').textContent =
              \`${silver.price ?? 'N/A'} ${silver.currency ?? ''}\`;

            document.getElementById('gold-meta').textContent =
              gold.symbol || 'XAU';

            document.getElementById('silver-meta').textContent =
              silver.symbol || 'XAG';

            const updated = gold.updatedAt || silver.updatedAt;
            document.getElementById('updated').textContent =
              updated
                ? \`Last updated: ${new Date(updated).toLocaleString()}\`
                : 'Last updated: Unknown';
          } catch (err) {
            document.getElementById('gold-price').textContent = 'Error';
            document.getElementById('silver-price').textContent = 'Error';
            document.getElementById('gold-meta').textContent = '';
            document.getElementById('silver-meta').textContent = '';
            document.getElementById('updated').textContent = 'Could not load live prices.';
          }
        }

        loadPrices();
        setInterval(loadPrices, 15000);
      </script>
    </body>
    </html>
    """
```

What this code does:

- Creates a FastAPI app.
- Fetches live gold and silver prices from the API.
- Returns the data through `/api/prices`.
- Serves a simple HTML dashboard at `/`.
- Refreshes the displayed prices every 15 seconds.

## \# Testing Locally

Before deploying, it is a good idea to run the app locally and make sure everything works as expected. FastAPI makes this easy with its built-in development server.

Start the app with:

```
fastapi dev main.py
```

Once the server starts, FastAPI will generate a local URL for your app and a docs URL for testing the endpoints.

![FastAPI development server running in terminal](https://www.kdnuggets.com/wp-content/uploads/awan_deploy_first_app_fastapi_cloud_2.png)  
Image by Author

  

Open your browser and go to:

```
http://127.0.0.1:8000
```

You should see your live dashboard showing gold and silver prices. The values will refresh automatically every 15 seconds.

![Live metals dashboard showing gold and silver prices](https://www.kdnuggets.com/wp-content/uploads/awan_deploy_first_app_fastapi_cloud_1.png)  
Image by Author

  

You can also test the JSON endpoint directly at:

```
http://127.0.0.1:8000/api/prices
```

This is especially useful if you want to inspect the raw response or later connect the data to another frontend or application.

![Raw JSON response from the /api/prices endpoint](https://www.kdnuggets.com/wp-content/uploads/awan_deploy_first_app_fastapi_cloud_10.png)  
Image by Author

  

## \# Deploying to FastAPI Cloud

Once the app works locally, you are ready to deploy it to FastAPI Cloud. The deployment flow is very simple and starts with a single command.

Run:

```
fastapi deploy
```

The CLI will guide you through connecting your FastAPI Cloud account and completing the setup. During onboarding, you may be asked a few short questions, such as your team name, app name, and deployment settings.

![FastAPI Cloud CLI onboarding prompts](https://www.kdnuggets.com/wp-content/uploads/awan_deploy_first_app_fastapi_cloud_13.png)  
Image by Author

  

Once that is done, FastAPI Cloud will build and deploy your app for you.

![FastAPI Cloud build and deployment in progress](https://www.kdnuggets.com/wp-content/uploads/awan_deploy_first_app_fastapi_cloud_4.png)  
Image by Author

  

After the deployment finishes, you will get a live public URL for your app — for example:

![FastAPI Cloud deployment complete with live URL](https://www.kdnuggets.com/wp-content/uploads/awan_deploy_first_app_fastapi_cloud_7.png)  
Image by Author

  

```
https://metals-live.fastapicloud.dev/
```

FastAPI Cloud also gives you interactive API docs at:

```
https://metals-live.fastapicloud.dev/docs
```

![FastAPI Cloud interactive API docs page](https://www.kdnuggets.com/wp-content/uploads/awan_deploy_first_app_fastapi_cloud_11.png)  
Image by Author

  

This is useful because you can test your API directly from the browser, without needing any extra tools.

![Testing the API endpoint from the FastAPI Cloud docs interface](https://www.kdnuggets.com/wp-content/uploads/awan_deploy_first_app_fastapi_cloud_12.png)  
Image by Author

  

## \# Monitoring the App

After deployment, you can use the FastAPI Cloud dashboard to monitor your app and check its logs.

To view the logs:

- Open the FastAPI Cloud dashboard.
- Go to **Apps**.
- Select your app.
- Open **Logs**.

This is useful for checking whether your app is running correctly, spotting API errors, and debugging issues after deployment.

![FastAPI Cloud dashboard showing app logs](https://www.kdnuggets.com/wp-content/uploads/awan_deploy_first_app_fastapi_cloud_3.png)  
Image by Author

  

FastAPI Cloud also starts to feel closer to platforms like **[Supabase](https://supabase.com/)** or **[Vercel](https://vercel.com/)**, with managed hosting, quick CLI-based deployment, and extra integrations you can connect to your app as you grow it.

![FastAPI Cloud dashboard integrations panel](https://www.kdnuggets.com/wp-content/uploads/awan_deploy_first_app_fastapi_cloud_9.png)  
Image by Author

  

## \# Wrapping Up

FastAPI Cloud makes it easy to take a small FastAPI app from local development to a live deployment. In this guide, we built a simple live metals dashboard, tested it locally, deployed it with one command, and checked logs after launch.

For a first deployment, the workflow is straightforward and a good introduction to the FastAPI Cloud experience.  

****[Abid Ali Awan](https://abid.work/)**** ([@1abidaliawan](https://www.linkedin.com/in/1abidaliawan)) is a certified data scientist professional who loves building machine learning models. Currently, he is focusing on content creation and writing technical blogs on machine learning and data science technologies. Abid holds a Master's degree in technology management and a bachelor's degree in telecommunication engineering. His vision is to build an AI product using a graph neural network for students struggling with mental illness.