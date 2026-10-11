---
name: weekly-digest
description: >
  生成 GitHub Trending / Product Hunt 周度资源整理（中英文对照 Markdown + JSON）。
  封装 weekly_digest/run.py：skill 只做意图解析与编排，业务逻辑全部在 Python 层。
  触发场景：周报、这周/本周/上周的 GitHub 整理、Product Hunt 周报、
  weekly digest、生成周报、整理这周的 GitHub Trending、跨周区间汇总。
whenToUse: 用户要求生成/查看某周（或日期区间）的 GitHub Trending 或 Product Hunt 周报时
---

生成周报请按以下流程执行（`$ARGUMENTS` 为用户的原始表述，可能为空）：

## 1. 确定基准日期

先跑 `date +%Y-%m-%d`（并用 `date +%u` 拿星期几，1=周一）获取今天日期。**禁止凭记忆猜 ISO 周数**——所有周计算都交给 CLI。

## 2. 意图 → CLI 参数映射（确定性）

| 用户说法 | CLI 参数 |
|---|---|
| 缺省 / "这周" / "本周" | 不传 `--week`（默认当前周） |
| "上周" | `--week last` |
| 明确 ISO 周（"2026-W40"） | `--week 2026-W40` |
| 日期区间（"10月1日到12日"） | `--from YYYY-MM-DD --to YYYY-MM-DD`（跨年要补全年份；区间按 ISO 周展开，逐周各生成一份完整周报） |
| 只要一个源 | 追加 `--source github-trending` 或 `--source producthunt` |

区间转日期时注意：用户没说年份就用今天所在年份；区间端点触及某周任意一天就会生成该周的完整周报，这是预期行为，执行后可向用户说明实际生成了哪几周。

## 3. 周初空数据保护

今天是**周一或周二**且用户说"这周"时，先提示：本周刚开始，收录可能很少甚至没有，建议改生成上周（`--week last`）。用户坚持则照跑。

## 4. 执行

在仓库根目录运行：

```bash
uv run python weekly_digest/run.py <参数>
```

## 5. 汇报

逐周汇报（跨周时每周一段）：

- 输出文件路径（Markdown 链接形式给出，方便点击预览）
- 收录条数、中文摘要覆盖率
- 变更告知（脚本自动输出"较上次：新增 N 条 / M 条升级为中文摘要 / 首次生成"）——原样转述
- 是否为"进行中快照"（周未结束时文档头部有 ⚠️ 标注，告知用户后续运行会自动补全）

## 6. 质量建议（仅提示，不执行）

中文摘要覆盖率明显偏低（< 50%）时，提示用户：可先跑主 pipeline 的 extract 阶段（如 `uv run python pipeline/run.py extract --target-date <日期>`），再重新生成周报，未提取文章的英文降级会自动升级为中文摘要。

## 边界（明确不做）

- 不触发主 pipeline 的任何阶段（scout/ingest/extract/analyze/synthesize/publish）
- 不删改历史周报文件（周报按 ISO 周命名，重复运行同一周为幂等覆盖，属正常更新）
- 不访问数据库
- 周报是生成物：提醒用户不要手动编辑 `weekly_reports/` 下的文件，手改内容会在下次运行时丢失
