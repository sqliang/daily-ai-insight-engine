# AI 笔试题分析与策略

**Exported:** 5/7/2026 17:08:04  
**Link:** [https://gemini.google.com/app/a01a1f211955acfc](https://gemini.google.com/app/a01a1f211955acfc)

## Prompt:
我接到了一个笔试题，请帮我分析下这个题目：

AI 应用笔试题：

AI舆情分析日报系统（Daily AI Insight Engine）

一、项目背景

我们希望构建一个系统，用于：

从每日新闻信息中提取结构化洞察，并生成可读的分析报告与可视化结果

该系统将应用于：

AI行业趋势分析

舆情监测与风险预警

信息快速理解与决策辅助

二、任务目标

在本次任务中，你需要借助 AI 工具（如 Claude Code / CodeX / Gemini CLI / Cursor 等），完成一个最小可用版本（MVP）的系统。

三、数据获取（自主完成）

数据源由你自行寻找和确定，以下是一些参考方向：

表格

类型示例来源说明科技媒体TechCrunch、The Verge、机器之心、量子位行业动态报道官方渠道公司博客、GitHub Releases、arXiv技术发布信息社交媒体Twitter/X、Reddit、知乎热榜舆论讨论热点聚合平台Google News、Hacker News、Product Hunt综合信息源数据要求：

至少获取 10～20 条 与AI相关的近期新闻/信息

中英文混合更佳

数据应包含：标题、正文内容（或摘要）、来源、发布时间

提示：数据质量会影响后续分析效果，请说明你的数据源选择理由。

四、输出结果（必须完成）

你需要输出一个"AI分析日报"，包含以下三部分：

信息结构化结果（必须）

你需要设计一个结构化数据模型（Schema），对新闻进行抽取和整理。

要求：

必须说明你的 schema 设计思路（为什么这样设计字段？）

不允许仅做 summary（摘要），必须体现结构化抽取

鼓励根据你的数据源特点调整 schema

分析报告

基于结构化数据，生成一份"日报分析"，包括：

今日AI领域主要热点：Top 3-5 重要事件

重要事件深度总结：对关键事件的背景+影响分析

趋势判断：技术/应用/政策/资本方向的趋势洞察

可选：风险或机会提示：识别潜在风险或投资机会

要求：分析必须有逻辑支撑，避免空洞描述。

可视化展示

结果中需包含可视化内容，形式不限。

核心要求：能清晰传达信息，技术栈不限

五、限制条件

为了保证公平性和考察目的，请遵守：

❌ 不允许将原始数据直接"一次性丢给AI"让其生成全部结果

必须体现你的处理逻辑（如数据清洗、分批处理、结果校验等）

❌ 不允许仅调用现成产品后截图提交（如直接用某AI工具生成报告）

❌ 不允许只做简单摘要拼接

❌ 不强制要求实现爬虫，手动整理为静态数据也可以

必须体现"结构化处理 + 分析过程 + 你的设计决策"

六、时间要求

建议完成时间：1 天以内（24小时）

可合理取舍功能，优先保证核心逻辑完整

如果时间紧张，可以简化可视化，但文档必须完整

七、提交内容

请提交以下内容到一个GitHub仓库：

1\. 项目代码或脚本（不限语言/框架）

2\. 原始数据文件

说明你从哪里获取的数据

数据选择理由

3\. 输出结果示例

至少展示1份完整的"AI分析日报"结果

4\. 说明文档（必须，核心考察项）

包含：

数据源说明：来源、选择理由、数据特点

系统设计思路：整体架构、关键决策

AI使用方式：使用场景、Prompt设计、错误处理

核心流程说明：从原始数据到最终报告的完整流程

## Response:
这道笔试题非常有水平，它表面上是让你做一个“AI 总结工具”，但实际上**核心考察的是候选人的 AI 工程化落地能力、架构设计思维以及对 LLM 边界的理解**。

结合你在 Agentic Workflow 运行框架、全栈基建以及前端架构方向的深厚积累，这不仅是一个通过面试的敲门砖，更是全面展示你“全栈 Builder”产品判断力和落地速度的绝佳舞台。

以下是对这道题目的深度拆解和攻克策略：

### 一、 考官的“潜台词”与核心考察点

仔细阅读限制条件（“不允许一次性丢给AI”、“必须体现处理逻辑”、“不允许简单拼接”），考官真正在意的是：

1.  **大模型的工程化控制力（Prompt Engineering & Structured Output）：** 你是否知道如何让 LLM 稳定输出 JSON Schema？如何处理幻觉？如何控制 Token 长度？
2.  **Pipeline 设计能力（Map-Reduce / Chain 思想）：** 面对长文本和多数据源，你是否懂得先拆解（Map：单篇文章结构化抽取），后聚合（Reduce：结合多篇生成宏观趋势），而不是粗暴地塞进一个 Context 里。
3.  **数据质量的深刻认知：** “Garbage in, garbage out”。从获取数据到送入大模型前，你做了什么预处理？
4.  **业务洞察与技术审美：** 提取的字段是否真的对“舆情和趋势预警”有业务价值？最终的可视化是否符合专业、极简的现代 Tech 审美？

### 二、 MVP 架构与实施策略建议 (24小时通关指南)

为了在 24 小时内展现出资深架构师的水准，建议采用“重设计、轻爬虫、巧组装”的策略。你可以将过往在内容获取、知识沉淀和智能审核方面的自动化工具链经验直接迁移过来。

#### 1\. 数据获取层 (Data Ingestion)

*   **策略：不要在爬虫上浪费时间。** 题目允许“手动整理为静态数据”。但为了体现工程能力，建议写一个极简的脚本，通过 RSS 抓取（如 Hacker News, 机器之心 RSS, arXiv 每日更新）获取 10-20 条 JSON 数据。
*   **预处理亮点：** 拿到的网页内容往往包含大量 HTML 标签。你可以引入类似 `Readability.js` 的工具进行正文提取和降噪，只把最干净的纯文本喂给大模型。这会极大提升抽取质量，是一个非常加分的工程细节。

#### 2\. 信息结构化与 Schema 设计 (核心拿分项)

你需要定义一套严格的 JSON Schema，并强制大模型按此输出。设计时要体现出“舆情与风险预警”的业务导向。

**推荐的 Schema 结构示例：**

```
{
  "article_id": "unique_hash",
  "entities": {
    "companies": ["OpenAI", "Google"],
    "technologies": ["VLA Models", "Agentic Workflow"],
    "key_people": ["Sergey Levine"]
  },
  "event_type": "Product Launch | Research Paper | Policy | Controversy",
  "impact_score": 8, // 1-10分，体现重要性量化
  "sentiment": "Positive | Neutral | Negative",
  "structured_summary": "一句话核心事实...",
  "potential_risks": "可能导致的行业洗牌或技术伦理问题..." // 直接呼应任务目标
}
```

*   **处理逻辑设计：** 遍历 20 条新闻，**单条独立调用** LLM 进行抽取（这满足了“不一次性丢给AI”的要求），将非结构化文本转化为强结构化的 JSON 数组。

#### 3\. 分析报告生成 (Insight Generation)

有了上述的 JSON 数组，后续的分析就水到渠成了。这体现了“Human-AI Dual Engine”的理念：AI 负责繁琐的微观清洗和特征提取，人类设定宏观维度的组合逻辑。

*   **排序与筛选：** 根据 Schema 中的 `impact_score` 取 Top 5 作为“今日主要热点”。
*   **趋势聚类：** 把提取出的 `technologies` 和 `event_type` 重新丢给 LLM，让其基于这些_已经浓缩过的高质量结构化数据_，生成趋势判断和资本风向洞察。

#### 4\. 可视化与极简呈现

*   既然你不限语言和框架，可以快速起一个前端页面（比如 Next.js + Tailwind CSS），保持现代、专业和极简的高级感。
*   **可视化切入点：** \* 不用做太复杂的图表，引入 ECharts。
    *   做一个 `Sentiment` (情绪) 的环形图。
    *   做一个 `entities` 中高频词汇的词云，或者不同 `event_type` 的柱状图。
    *   配合清晰的卡片式排版展示 Top 5 深度总结。

### 三、 README 文档撰写 (决定成败的最后一公里)

很多工程师代码写得好，但文档吃亏。你的 README 必须体现出“架构师视角”。

*   **Highlight 你的设计决策：** 明确写出“为什么采用单篇抽取 + 聚合生成的两步走策略？”（答：为了突破上下文窗口限制，提高抽取精度，避免长文本的中间遗忘现象）。
*   **AI 使用规范说明：** 展示你的 Prompt 设计模式，比如使用了少样本提示（Few-Shot）来稳定输出 Schema，或者使用了某种特定的系统预设来规避模型的随意发挥。
*   **展示你对 MCP 或扩展生态的思考：** 在 Future Work (未来规划) 中，你可以顺带提一句：未来该系统可以被封装为标准化的 Model Context Protocol (MCP) Server，供其他 Agent 随时调用，完成跨平台的信息流转。这能瞬间拔高你的段位。

这个项目要在一天内完成，时间管理的优先级是：**Schema 设计与 Prompt 调优 (40%) \> 文档与架构图 (30%) \> 数据拉取与清洗 (15%) \> 前端可视化展示 (15%)**。

你打算用哪种语言/框架（比如 Python 脚本跑批处理 + React 展示，或者纯 Node.js 全栈搞定）来快速搭建这个 MVP 的主体骨架？我们可以针对你选定的技术栈进一步细化 Prompt 的实现逻辑。

## Prompt:
我打算使用 Next.js + React + Tailwindcss，在 Server 模块，我像先试用 claude-agent-sdk 来作为 Agent 核心引擎。请你先帮我设计出整个项目对应仓库的模块划分与目录设计

## Response:
这个技术栈选择非常精准。**Next.js + Tailwindcss** 能让你在几小时内糊出一个具备现代 Tech 审美、极具专业感的可视化大屏；而 **`claude-agent-sdk`** 则非常适合用来做底层的复杂推理和流程编排（尤其是处理强结构化输出和长文本上下文）。

对于一个要在 24 小时内完成的 MVP，加上你资深架构师的背景，项目的目录设计必须兼顾“快速出活”**和**“工程严谨性（高内聚、低耦合）”。

下面为你设计的目录结构，采用了轻量级的领域驱动设计（DDD）思想，将**数据流获取**、**Agent 推理**和**前端展示**进行了清晰的物理隔离。

### 核心项目结构 (Next.js App Router 模式)

```
daily-ai-insight-engine/
├── data/                       # 📂 数据存储区 (极其重要，直接满足题目提交要求)
│   ├── raw/                    # 存放原始抓取的 RSS/JSON 数据 (Raw Data)
│   └── reports/                # 存放 Agent 生成的最终日报结构化 JSON
├── scripts/                    # 📂 离线脚本区 (用于规避 Next.js API 超时)
│   └── run-pipeline.ts         # 一键执行：拉取 -> 清洗 -> Agent 抽取 -> 生成报告
├── src/
│   ├── app/                    # 📂 Next.js 前端路由与 API
│   │   ├── api/                # 后端 API (供前端读取生成的 JSON 报告)
│   │   │   └── report/route.ts 
│   │   ├── page.tsx            # 可视化大屏主页 (Dashboard)
│   │   └── layout.tsx
│   ├── components/             # 📂 前端 UI 组件
│   │   ├── charts/             # 可视化图表组件 (ECharts / Recharts 封装)
│   │   ├── report/             # 报告卡片、趋势分析展示组件
│   │   └── ui/                 # 基础原子组件 (可直接引入 shadcn/ui 提效)
│   ├── lib/                    # 📂 核心业务逻辑 (Server 端)
│   │   ├── agent/              # 🧠 Agent 核心引擎层 (claude-agent-sdk)
│   │   │   ├── index.ts        # 对外暴露的核心类 (AIInsightEngine)
│   │   │   ├── prompts.ts      # 统一管理 System Prompts 和 Few-shots
│   │   │   ├── schema.ts       # 定义并导出 Zod Schema (用于强约束输出)
│   │   │   └── tools.ts        # (可选) 如果需要 Agent 自己去调特定 API，封装在这里
│   │   ├── data/               # 📥 数据获取与预处理层
│   │   │   ├── fetcher.ts      # 负责抓取 RSS / 静态网页内容
│   │   │   └── cleaner.ts      # 核心逻辑：基于 Readability.js 等工具清洗 HTML 提取正文
│   │   └── utils/              # 通用工具函数 (Hash 生成、文件读写等)
│   └── types/                  # 📂 全局 TypeScript 类型声明
│       └── index.ts            # 业务实体类型 (Article, InsightReport, Entity)
├── .env                        # 环境变量 (CLAUDE_API_KEY 等)
├── tailwind.config.ts
├── package.json
└── README.md                   # 📝 核心交付物：架构说明与设计决策
```

* * *

### 架构设计深度解析（附面试加分话术）

为了在面试官面前展现出 senior 的工程素养，这套目录结构背后暗含了以下几个关键的架构决策，你可以在 README 中着重体现：

#### 1\. 为什么分离 `scripts/` 和 `src/app/api/`？ (解决 Serverless 超时痛点)

*   **设计考量：** 如果你将“处理 20 篇文章 -\> 单篇摘要 -\> 宏观聚合”的整个链条写在 Next.js 的 `/api/generate` 路由里，在 Vercel 等 Serverless 环境下极大概率会触发 10s 或 60s 的超时（Timeout）。
*   **MVP 最佳实践：** 采用**读写分离**。把耗时的 AI 推理 Pipeline 放在 `scripts/run-pipeline.ts` 中，通过 Node CLI 在本地或服务端后台静默运行，结果落盘到 `data/reports/`。Next.js 的前端展示和 API 仅仅负责读取（Read）静态 JSON 进行可视化渲染。这展现了你对全栈部署环境限制的深刻理解。

#### 2\. `src/lib/agent/` 的内聚设计 (控制 LLM 不确定性)

*   在使用 `claude-agent-sdk` 时，千万不要把 Prompt、Schema 定义和业务逻辑揉在一块。
*   **`schema.ts` 结合 Zod：** 这是全栈的灵魂。用 Zod 定义出严格的输出 Schema 后，一方面可以通过 SDK 强制约束 Claude 的输出结构（Tool calling 或 Structured Output），另一方面可以直接推导出 TypeScript Type（`z.infer`），让前端组件无缝消费，实现端到端的类型安全。
*   **`prompts.ts` 独立维护：** 将 Prompt 视为系统的一种“配置”或“资源”，而不是硬编码的字符串，方便后续迭代和调优。

#### 3\. `src/lib/data/cleaner.ts` (体现高质量数据认知)

*   这是很多人会忽略的拿分点。在这个文件里，你可以写一个简单的管道（Pipeline）：接收 URL/HTML -\> 剔除广告/侧边栏 -\> 提取纯文本正文 -\> 截断超长文本（控制 Token 成本）。
*   只要有了这一层，考官就能看出你具备真正的“AI 落地经验”，知道模型效果的上限由数据清洗决定。

### 下一步建议

既然底层核心选定了 `claude-agent-sdk`，我们可以优先把 `src/lib/agent/schema.ts`（数据结构）和 pipeline 的核心调度逻辑敲定下来。

你是希望我们先一起定义这个决定系统成败的 **Zod Schema**，还是先写一段 `run-pipeline.ts` 的伪代码，把“单篇抽取 -\> 全局聚合”的 Map-Reduce 骨架搭起来？

## Prompt:
请帮我写个 README.md

## Response:
这份 README.md 的设计目标是：**在考官打开仓库的第一秒，就能感受到你作为资深架构师的技术品味和工程严谨性。** 文档不仅交代了怎么把项目跑起来，更深度阐述了你的“系统设计决策”、“AI 边界控制”以及“数据流转哲学”，完美契合你所追求的极简、现代且专业的 Tech 审美。

你可以直接复制以下内容到项目的 `README.md` 文件中，只需根据实际情况微调（如补充真实的 GitHub 仓库地址）：

* * *

````
# 🧠 Daily AI Insight Engine (AI 舆情分析日报系统)

> 一个基于 Next.js 与 Claude Agent SDK 构建的自动化 AI 资讯分析与洞察系统。
> 采用“数据离线管道处理 + 前端静态渲染”的读写分离架构，致力于将每日海量碎片化新闻转化为高信噪比的结构化洞察。

## 📖 项目背景与目标

面对每日爆发式的 AI 行业资讯，单纯的新闻聚合已无法满足深度的信息理解需求。本项目旨在构建一个最小可用（MVP）的**自动化运营工具链**，通过大模型执行信息抽取、情绪分析与趋势聚类，输出具备高度结构化与商业洞察的“AI 分析日报”，辅助技术追踪、舆情监测与投资决策。

## 🏗 系统架构与核心设计决策

本项目没有采用常规的“一把梭”将所有数据丢给大模型的做法，而是基于**工程化可靠性**和**大模型上下文控制**的考量，设计了如下架构：

### 1. 读写分离架构 (Read-Write Separation)
* **Write (离线分析管道):** 在 `scripts/` 目录下通过 Node.js 运行离线 Pipeline。彻底规避 Vercel 等 Serverless 部署环境下的 API 请求超时限制，同时方便后续接入定时任务（Cron Job）。
* **Read (前端可视化):** Next.js App Router 仅负责读取生成的本地静态 JSON 报告进行可视化渲染，保证页面加载的极致速度与稳定性。

### 2. Map-Reduce 抽取分析流
应对长文本幻觉和信息遗漏，采用两段式处理：
* **Map 阶段（微观结构化）:** 遍历原始数据，对**单篇文章**独立调用 LLM，强制将其提纯为严格包含实体、情绪、影响力的 JSON 结构。
* **Reduce 阶段（宏观聚类）:** 汇总所有单篇的结构化数据（剔除了大量冗余文本，极大降低 Token 消耗），让 LLM 站在全局视角生成 Top 事件总结与趋势预判。

---

## 🛠 核心处理流程 (Pipeline)

系统的工作流定义在 `scripts/run-pipeline.ts` 中，包含四大核心步骤：

1. **数据获取 (Ingestion):** 通过轻量级脚本从预设数据源拉取最新资讯。
2. **数据清洗 (Cleaning):** 去除 HTML 标签、广告等噪音，仅保留核心正文，提升 LLM 输入信噪比。
3. **结构化抽取 (Extraction):** 依托 `claude-agent-sdk`，将清洗后的文本转化为预定义的 TypeScript / Zod Schema（实体、分类、情绪得分）。
4. **洞察生成 (Synthesis):** 基于高维度的结构化集合，生成最终的趋势洞察报告并落盘为 `reports/daily.json`。

---

## 📊 数据源说明与选择决策

* **数据来源：** * Hacker News / Product Hunt (API/RSS)：捕获最新的开发者社区讨论与独立产品发布。
  * arXiv AI 分类 (RSS)：追踪核心前沿论文与技术突破。
  * TechCrunch (网页抓取)：获取资本动向与大厂商业决策。
* **数据特点：** 中英文混合，覆盖学术界、开源社区与商业界。
* **选择理由：** 此组合能够构建完整的行业视角。学术突破（arXiv）往往领先商业落地（TechCrunch）数月，而社区讨论（HN）能最快反映技术实施的阻力与开发者情绪。综合数据源使得最终的“风险与机会提示”更具立体逻辑支撑。

---

## 🤖 AI 应用与工程化约束

为了保证输出的绝对稳定，本项目在 AI 层的工程实践包括：

1. **强类型约束 (Structured Output):** 使用 `Zod` 定义 Schema，结合 `claude-agent-sdk` 的 Tool Calling 机制，强制模型按照精确的 JSON 格式输出，杜绝“自由发挥”导致的解析崩溃。
2. **Prompt 设计 (Prompt Engineering):**
   * **角色设定:** 设定为资深 AI 行业分析师，具备敏锐的商业与技术嗅觉。
   * **Few-Shot:** 在 Prompt 中注入 1-2 个标准输出示例，极大地提高了分类（如 `event_type`）和打分（`impact_score`）的准确性。
3. **容错机制 (Error Handling):**
   单篇文章抽取失败（如接口超时、格式错误）会被 Catch 并记录日志，跳过该条目，保障整体 Pipeline 运行不会中断。

---

## 🚀 快速启动

### 前置要求
* Node.js (>= 18.x)
* pnpm 或 npm
* Anthropic API Key (Claude)

### 环境配置
```bash
git clone [https://github.com/yourusername/daily-ai-insight-engine.git](https://github.com/yourusername/daily-ai-insight-engine.git)
cd daily-ai-insight-engine
pnpm install

# 复制环境变量文件并填入你的 CLAUDE_API_KEY
cp .env.example .env
````

### 1\. 运行分析管道 (生成报告)

_该步骤需要调用 API 消耗 Token，运行时间约 1-3 分钟。_

```
npx tsx scripts/run-pipeline.ts
```

_执行成功后，结果将保存在 `data/reports/` 目录下。_

### 2\. 启动前端可视化服务

```
pnpm dev
```

打开浏览器访问 
[http://localhost:3000](https://www.google.com/search?q=http://localhost:3000)
，查看自动生成的 AI 洞察大屏。

* * *

🔮 扩展演进 (Future Work)
---------------------

本 MVP 验证了核心逻辑，未来计划的演进方向：

*   **MCP (Model Context Protocol) 接入:** 将该数据分析引擎封装为标准的 MCP Server，使得其他个人 Agent 工作流可以随时跨域调用每日分析数据。
*   **Human-in-the-loop:** 在离线管道与发布之间，增加人工快速 Review 和干预的界面，进一步提升报告的专业精准度。

```

### 给你的额外建议：

1. **项目亮点暗示：** 这个文档的设计完美展现了你在全栈架构上的成熟度。特别是“读写分离”和“MCP 接入”的提及，能够直接对齐那些招募高阶 AI 应用架构师职位的技术要求。
2. **实际操作提示：** 在提交代码前，记得在根目录建一个假的 `.env.example` 文件（里面只写 `CLAUDE_API_KEY=your_key_here`），这是极具专业感的小细节。
```

## Prompt:
我要建仓库，请给出一个仓库描述

## Response:
为 GitHub 仓库设置一个精准、专业的 Description（简介）和 Topics（标签），能让面试官在看代码前就迅速 get 到这个项目的技术含金量和业务定位。

针对你这种具备资深架构视角的项目，我为你准备了三个不同侧重点的简短描述，你可以根据个人喜好挑选：

### 选项一：极简极客风（推荐，最符合高阶开发者审美）

> 🚀 An automated pipeline transforming fragmented AI news into structured insights and visual reports, powered by Next.js & Claude Agent SDK. _(中译：一个自动化的数据管道，基于 Next.js 与 Claude Agent SDK，将碎片化的 AI 资讯转化为结构化洞察与可视化报告。)_

### 选项二：技术架构风（强调工程设计，适合直接秀肌肉）

> 🧠 Daily AI Insight Engine: A Map-Reduce style AI agent workflow for extracting structured schema and trends from daily tech news. Built with Next.js and TailwindCSS. _(中译：AI 每日洞察引擎：一个 Map-Reduce 风格的 AI Agent 工作流，用于从每日科技新闻中抽取结构化 Schema 与趋势。基于 Next.js 和 TailwindCSS 构建。)_

### 选项三：业务落地风（强调价值与产品 sense）

> 📊 自动化 AI 舆情分析日报系统：基于大模型构建“数据清洗-结构化抽取-宏观聚类”管道，提供 AI 行业趋势判断与风险预警的可视化大屏。

* * *

### 🏷️ 建议填写的 GitHub Topics (Tags)

将这些标签加在仓库右侧的 About 区域，能让仓库显得非常专业且容易被检索： `nextjs` `claude-agent` `llm-pipeline` `agentic-workflow` `structured-output` `data-visualization` `typescript`

直接把**选项一**复制到 GitHub Repo 的 Description 栏，再配上这些 Tags，整个仓库的“门面”就非常高级了。需要我开始帮你构思 `scripts/run-pipeline.ts` 的 Map-Reduce 核心代码骨架吗？



---
Powered by [Gemini Exporter](https://www.ai-chat-exporter.com)