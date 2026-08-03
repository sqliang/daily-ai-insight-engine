---
name: daily-report-pipeline
description: >
  按指定日期跑通日报流水线（ingest 检查 → extract → analyze → synthesize），每个阶段先做后验检查、
  只对问题文章定点修复、门禁通过后才进入下一阶段。前置的 scout/ingest 由每日 17:30 定时任务完成，
  本技能从抓取完整性检查开始接管。全部操作严格限定 created == 指定日期的文章，不影响其他日期数据。
  触发场景：跑日报、生成某天的报告、补跑日报、跑 7 月 21 日的报告、日报流水线、
  daily report、daily pipeline、run report for a date。
---

# 指定日期日报流水线技能

输入一个日期（默认今天），按门禁流程跑通当天日报：**每阶段先检查 → 有问题定点修复 → 复检通过才进入下一阶段**。

## 核心原则

**日期隔离（最高优先级）。** 所有检查与修复只作用于 frontmatter `created == 目标日期` 的文章。严禁全量重跑、严禁 `--force` 不带 `-i` 单文件参数。唯一会被改写的共享文件是 `data/05_reports/daily-report.json`（latest 副本）和 `data/04_structured/*.json` 热数据——这是 pipeline 固有行为，属预期内。

**成本控制。** repair 全部是单文件粒度，LLM 调用只花在问题文章上。每阶段最多 2 轮修复循环，2 轮后仍不过则停止并输出遗留清单，不要无限重试。

**只跑 CLI 和技能脚本。** 不修改 `pipeline/` 任何源码。

## 脚本位置

```
.agents/skills/daily-report-pipeline/scripts/
  pipeline_gate.py     # check/repair 门禁（本文件的双份镜像见 .claude/skills/，修改后必须同步）
  backfill_arxiv.py    # arxiv manifest 缺失补建（被 repair-ingest 自动调用）
```

所有命令在项目根目录执行。`--date` 省略时用今天（`date +%F`）。

## 设计约束（三条铁律，2026-07-29 事故后确立）

> 事故回放：阶段执行裸跑 `extract`/`analyze`，`skip-existing` 把两个月历史积压一并送进 LLM（extract 519 篇、analyze 1381 篇，目标日期仅占 16 篇），8 小时烧穿 API 余额（402）。

1. **阶段执行只能走 gate 脚本的 `run-*`**：日期隔离已做进 pipeline CLI（`--target-date`），gate 在执行前还会预检熔断（范围内/待处理文件数超过 100 即拒绝，除非显式 `--allow-large`）
2. **禁止裸跑 `pipeline/run.py extract|analyze`**：CLI 在裸跑时会打印醒目警告；看到警告应停手改用 gate
3. **大批量 LLM 操作必须先预检**：gate `run-*` 内置了工作量统计；任何绕过 gate 的手工操作，必须先 `--dry-run` 确认范围

## 执行流程

### Phase 0 — 前置确认

- 确认 `data/00_manifest/*_{date}.json` 存在（scout/ingest 定时任务已跑）。若整个日期都没有 manifest，说明定时任务没跑，先告知用户，不要自行 scout。

### Phase 1 — ingest 门禁

```bash
GATE=.agents/skills/daily-report-pipeline/scripts/pipeline_gate.py
uv run python $GATE check-ingest --date <date>     # exit 0 通过；exit 1 输出 JSON 问题清单
```

- 有问题 → `uv run python $GATE repair-ingest --date <date>` → 再 check-ingest（最多 2 轮）
- repair-ingest 自动处理：状态重置 + 浏览器重抓 + Jina 兜底 + 劣化回滚；arxiv 缺 manifest 时自动调 backfill_arxiv.py 补建并 ingest；其他源缺 manifest 无法自动补救，报告给用户
- 2 轮后仍有 `still_failed` → 停止，把遗留清单交给用户决策（通常是源站持续反爬，可接受跳过）

### Phase 2 — extract 阶段

```bash
uv run python $GATE run-extract --date <date>       # 单进程 --target-date + 预检熔断（超 100 篇拒跑）
uv run python $GATE check-extract --date <date>
```

- 有问题 → `uv run python $GATE repair-extract --date <date>`（逐文件 `extract -i <文件> --force`）→ 复检（最多 2 轮）
- 检查口径：缺 02_extracted 对应文件 / `extract_result=failed` / `tldr` 与 `objective_summary` 均缺失 / 正文与上游不一致（stale）

### Phase 3 — analyze 阶段

```bash
uv run python $GATE run-analyze --date <date>       # 单进程 --target-date + 预检熔断
uv run python $GATE check-analyze --date <date>
```

- 有问题 → `uv run python $GATE repair-analyze --date <date>` → 复检（最多 2 轮）
- 检查口径：缺 03_analyzed 对应文件 / `impact_score` 或 `sentiment` 缺失 / 正文与上游不一致（stale）

### Phase 4 — synthesize

```bash
uv run python pipeline/run.py synthesize --target-date <date>
```

`--target-date` 保证 aggregate 与日报生成都只取 `created == date` 的文章。

### Phase 5 — 验证与汇报

- 确认 `data/05_reports/daily-report-<date>.json` 与 `.md` 已生成
- 汇报：各阶段检查/修复结果、遗留问题、日报路径

## 已知近似（如实告知用户）

- arxiv 补建是"公告日 + 标题关键词"口径，与正常 RSS 流程（标题+摘要）存在小幅偏差
- 持续被反爬的文章（如 openai.com）可能 2 轮修复仍失败，属外部限制，跳过即可
- 交互式页面（3D 演示、JS 地图应用等）本身无文字正文，会反复出现在 suspicious/still_failed 中（如 HN 的 3D 演示帖），属已知不可修复项，报告给用户后跳过
- 周末 arxiv/nlp-elvis 等源无 manifest 属正常空窗，脚本已内置判定不会误报
