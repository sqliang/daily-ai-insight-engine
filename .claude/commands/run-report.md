---
description: 检查指定日期数据 → 拟定跑数方案（含修复）→ 批准后全自动跑通日报
argument-hint: "[date]"
---

请使用 daily-report-pipeline 技能处理 `$ARGUMENTS`（缺省为今天）这一天的日报数据，按以下流程：

1. **先检查**：check-ingest 只读检查该日抓取文章数据是否有问题（manifest 缺失 / 抓取失败 / 可疑短正文），不做任何改动。
2. **制定跑数方案**：基于检查结果输出这一天数据的跑数方案，方案里包含——现状与问题清单、修复计划（repair-ingest 定点修复，≤2 轮）、各阶段执行步骤（extract → analyze → synthesize）、预期风险与遗留项。**等待用户 review 批准后再执行**。
3. **批准后全自动执行**：按技能门禁自动跑完全流程（repair → extract → analyze → synthesize → 验证），中途不再打断，每阶段 check-* 通过才进下一阶段。
4. **验证汇报**：跑完后确认 daily-report-<date>.{json,md} 生成且无截断，汇报结果与遗留项。

严格日期隔离（created == 目标日期），遵守三铁律（阶段执行只走 gate run-*，禁裸跑 extract|analyze，大批量先预检）。
