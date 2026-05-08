import { join } from "node:path";
import {
  dailyReportSchema,
  rawArticleListSchema,
  structuredInsightListSchema,
} from "@/lib/agent/schema";
import { readJsonFile } from "@/lib/data/files";

// ============================================================================
// validate-report.ts — 数据完整性验证脚本
//
// 用法：pnpm validate
//
// 功能：对流水线产出的三个 JSON 文件逐一执行 Zod Schema 校验。
// 任意一个文件的 Schema 不匹配（字段缺失、类型错误、约束违反）
// 都会立即抛错，exit code ≠ 0。
//
// 适用于：
//   - CI 流水线中的数据完整性检查
//   - 手动修改 articles.json 或报告后的回归验证
//   - 结构化洞察和日报格式的一键自检
// ============================================================================

async function main() {
  await readJsonFile(join(process.cwd(), "data/01_raw/articles.json"), rawArticleListSchema);
  await readJsonFile(
    join(process.cwd(), "data/02_processed/structured-insights.json"),
    structuredInsightListSchema,
  );
  await readJsonFile(join(process.cwd(), "data/05_reports/daily-report.json"), dailyReportSchema);
  console.log("All data files passed Zod validation.");
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
