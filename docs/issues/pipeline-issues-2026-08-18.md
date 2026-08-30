# 流水线问题清单（2026-08-18 跑数）

> **编写时间**: 2026-08-28 | **来源**: 跑通 08-18 日报全流程（ingest repair → extract → analyze → synthesize）过程中发现 | **目的**: 汇总遗留问题，便于后续单独排期解决

---

## 执行摘要

| # | 问题 | 严重度 | 归属阶段 | 当前状态 |
|---|------|--------|----------|----------|
| 1 | synthesize 长文生成中途 claude CLI 崩溃（SDK `exit code 1`） | **High** | Stage 4b synthesize | 复发，靠内置 3 次重试兜底 |
| 2 | `paper_assessment` 未产出 → `paperHighlights` 为 null | **Medium** | Stage 3 analyze（论文专项） | 持续存在，`/specialized/paper` 页空 |
| 3 | aggregate 校验失败丢数据（`sourceType` 缺失 / 日期非字符串） | **Medium** | Stage 4a aggregate | 持续存在，WARNING 级不阻断 |
| 4 | producthunt 每日 ingest 必现 Cloudflare 反爬 | **Low-Medium** | Stage 1b ingest | 已可自动 repair，但每日复发 |

---

## 问题 1 — synthesize 长文生成中途 SDK `exit code 1`（High）

### 现象

`synthesize` 调用 deepseek-v4-pro 生成日报时，约 6 分钟后 claude CLI 子进程崩溃退出，SDK 报错：

```
Fatal error in message reader: Command failed with exit code 1 (exit code: 1)
Agent 调用失败 (第 1/3 次): Agent SDK 调用异常: Command failed with exit code 1 — 2.0s 后重试
```

### 复发记录

- **08-17**: 第 4 次重跑才成功
- **08-18**: 第 1 次失败（11:02:55 起生成，11:09:10 崩溃），第 2 次重跑成功

### 影响

- 日报生成不稳定，每次都可能需要多次重跑（浪费 token 与时间）
- 若 `call_agent_with_retry` 的 3 次重试全失败，则当日日报无法生成
- 工作日（文章量大、prompt 更长）触发概率更高

### 疑似根因

- 非 max_tokens 问题（该透传链路已于本轮修复，`CLAUDE_CODE_MAX_OUTPUT_TOKENS=65536` 已生效，本轮未见 JSON 截断）
- 疑 deepseek Anthropic 兼容端点（`api.deepseek.com/anthropic`）对超长生成（166KB prompt + 65536 输出上限）存在时间/输出限制，导致流式中途断连
- SDK 吞掉了 claude CLI 的真实 stderr，只留 `Check stderr output for details`，根因难定位

### 建议修复方向

1. 捕获 claude CLI 子进程的 stderr（当前被 SDK 丢弃），先拿到真实报错再定位
2. 评估 deepseek 端点的实际输出上限，若远低于 65536，调低 `synthesize.max_tokens` 或换模型
3. 评估给 synthesize 分段/分块生成（先出日报骨架，再逐块补全），降低单次生成体量
4. 临时缓解：提高 `call_agent_with_retry` 重试次数

---

## 问题 2 — `paper_assessment` 未产出 → `paperHighlights` 为 null（Medium）

### 现象

08-18 日报的 `specializedBrief.paperHighlights` 为 `null`，而同日有 15 篇 arxiv-cs-ai 论文、20 篇带 paper 标签的文章。

```
specializedBrief 键: githubHighlights(5) / productHighlights(4) / paperHighlights(null) / projectInsights(6) / productInsights(6)
03_analyzed 中 08-18 带 paper_assessment 字段的文章数: 0
```

### 影响

- `/specialized/paper/2026-08-18` 页面无内容
- 论文专题洞察（研究问题 / 方法创新 / 实验严谨度 / 产业相关性）缺失

### 复发记录

- **08-20**：`specializedBrief.paperHighlights` 仍为 `null`，`03_analyzed` 中 created=08-20 的 arxiv 文章带 `paper_assessment` 字段数为 0（同日有 15 篇 arxiv-cs-ai 论文，前端 `/specialized/paper` 页会列出论文但无专题分析字段，researchArea 退化为 `unknown`）

### 疑似根因

- Stage 3 论文专项分析（产出 `paper_assessment` 字段）未对 arxiv 论文生效，或触发条件有缺陷
- `check-analyze` 门禁只校验 `impact_score` / `sentiment`，不覆盖 `paper_assessment`，因此门禁未拦截该缺口

### 建议修复方向

1. 排查 `pipeline/analysis/` 论文专项分析的触发条件（哪些源/标签会走 paper_assessment），确认 arxiv-cs-ai 是否被正确路由
2. 门禁 `check-analyze` 补充 `paper_assessment` 缺失的判定（对判定为论文的文章）
3. 修复后回归：用 `--target-date` 重跑某日 analyze，确认论文文章产出 paper_assessment

---

## 问题 3 — aggregate 校验失败丢数据（Medium）

### 现象

synthesize 的 aggregate 阶段大量 WARNING（`DailyAIInsight 校验失败 [base_info]`），两类：

1. **`sourceType` 缺失**（`01_raw/tldrai/*.md`、`01_raw/whytryai/*.md`）：这些文章停留在 raw 阶段、从未 extract，BaseInfo 缺 `sourceType` 字段，校验失败
2. **日期非字符串**（`03_analyzed/tldrai/*.md`）：`published`/`created` 被解析为 `datetime.date` 而非 string，报 `string_type` 错误（如 `input: datetime.date(2026, 5, 6)`）

### 影响

- 校验失败的文章在 aggregate 时被跳过，不进 per-source JSON / all_articles.json
- 与「多阶段 aggregate」设计意图冲突：设计上 raw 文章应作为 `scout` 状态出现在 JSON 中，但 `sourceType` 缺失导致其校验失败被丢弃
- 日期非字符串是历史数据遗留（`created: 2026-05-07` 未加引号，YAML 解析为 date 对象）

### 疑似根因

- 前端 frontmatter 写入时日期字段未强制字符串（引号），旧数据存在未加引号的日期
- aggregate 对「未 extract 的 raw 文章」无容错：BaseInfo 校验要求 `sourceType`，但 raw 阶段本就无此字段

### 建议修复方向

1. 排查 frontmatter 日期序列化，确保 `published`/`created` 始终写为带引号字符串
2. 评估 aggregate 对 raw 未 extract 文章的容错策略（按 scout 状态放行，而非因缺 `sourceType` 丢弃），或显式过滤并降级日志噪音
3. 一次性数据清洗：批量修复 `03_analyzed/tldrai` 中日期为 date 对象的旧文件

---

## 问题 4 — producthunt 每日 ingest 必现 Cloudflare 反爬（Low-Medium）

### 现象

08-18 ingest 有 5 篇 producthunt 抓取失败（Cloudflare 反爬，正文仅 ~100 字描述片段，`extraction_status: failed`），需 `repair-ingest` 兜底。

### 现状

- `PRODUCTHUNT_API_TOKEN` 已配置，`repair-ingest` 走官方 API 绕过 Cloudflare，5 篇已全部修复
- 但**每日定时 ingest 阶段**仍会先撞 Cloudflare，事后再 repair，多一轮往返

### 影响

- 每天 producthunt 都需要 repair 兜底，增加跑数步骤与延迟

### 建议修复方向

1. ingest 阶段对 producthunt 源直接走官方 API（PRODUCTHUNT_API_TOKEN），绕过浏览器/Jina 反爬链，从源头避免失败
2. 若保留现状，则把 repair-ingest 纳入每日定时任务，自动兜底

---

## 备注

- 以上 4 项均为**数据/流水线层面**问题，与前端渲染无关；问题 1/3 已在 CLAUDE.md 或历史 run 中有先例，属复发项。
- 排序按影响面：问题 1 直接影响日报产出稳定性，建议优先；问题 2 影响论文专题页完整性；问题 3/4 为数据质量与采集兜底，可后置。
