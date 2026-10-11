# weekly_digest — 周度资源整理

独立于主 pipeline 的周报生成器：按 ISO 自然周（周一~周日）汇总 `data/` 下指定信源的文章，生成中英文对照的 Markdown 周报，供周末翻阅。**纯本地模板拼接，零 LLM 调用。**

日常使用中一般通过 `weekly-digest` skill 以自然语言触发（"生成这周的周报"），本目录的 CLI 也可独立使用。

## 用法

```bash
uv run python weekly_digest/run.py                              # github-trending + producthunt × 本 ISO 周
uv run python weekly_digest/run.py --week last                  # 上一 ISO 周（别名 current/last）
uv run python weekly_digest/run.py --week 2026-W40              # 指定历史周
uv run python weekly_digest/run.py --from 2026-10-01 --to 2026-10-12  # 跨周区间：按 ISO 周展开，逐周各生成一份
uv run python weekly_digest/run.py --source github-trending     # 只跑单源
uv run python weekly_digest/run.py --output-dir /tmp/x          # 覆盖输出目录
```

`--week` 与 `--from/--to` 互斥；`--from` 与 `--to` 必须成对。区间端点触及某周任意一天即生成该周的完整周报（周报语义以完整 ISO 周为单位，区间只是"选周"方式）。

## 输出

```
weekly_reports/
  github-trending/2026-W41.md    # 中文摘要 + 英文原文对照，按日期倒序分组，含上榜天数
  github-trending/2026-W41.json  # WeeklyDigest 结构化数据（预留给未来 web 站点）
  producthunt/2026-W41.md
  producthunt/2026-W41.json
```

## 更新语义（重要）

- 周报是 `data/` 的**纯函数**：重复运行同一周为**幂等全量重生成**——不丢数据（`data/` 只增不减），且补跑 extract 后的文章会自动从英文降级升级为中文摘要
- 每次运行会与上次生成的 JSON 对比，输出变更告知：`较上次：新增 N 条 / M 条升级为中文摘要`（首次运行输出"首次生成"）
- 周未结束时生成的文档头部标注 **⚠️ 进行中快照**，后续运行自动补全
- **请勿手动编辑 `weekly_reports/` 下的文件**——手改内容会在下次运行时丢失

## 数据规则

- 扫描 `data/02_extracted/{source}/` 优先，`data/01_raw/{source}/` 补齐，按文章 ID 去重
- 按 frontmatter `created` 过滤是否落在周窗口内
- 中文摘要取 Stage 2 的 `tldr`；未执行 extraction 的文章降级展示英文 `description` 原文（标注"未提取"）
- GitHub Trending 用 `manifest_dates` 统计本周上榜天数；Product Hunt 展示原始发布日期
