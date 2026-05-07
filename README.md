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
