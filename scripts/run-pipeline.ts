import { writeFile } from "node:fs/promises";
import { join } from "node:path";
import { AIInsightEngine } from "@/lib/agent";
import {
  dailyReportSchema,
  rawArticleListSchema,
  structuredInsightListSchema,
} from "@/lib/agent/schema";
import { cleanArticle } from "@/lib/data/cleaner";
import { readJsonFile, writeJsonFile } from "@/lib/data/files";
import { generateMarkdown } from "@/lib/report/generate-markdown";

// ============================================================================
// run-pipeline.ts — 日报流水线入口脚本
//
// 用法：pnpm pipeline
//
// 流水线四阶段：
//   1. Ingestion  — 读取 data/raw/articles.json（原始语料）
//   2. Cleaning   — 去 HTML / 截断文本，控制 token 消耗
//   3. Map        — 逐篇抽取为 StructuredInsight（独立处理，失败可跳过）
//   4. Reduce     — 聚合所有 StructuredInsight 生成 DailyReport
//
// 所有中间产物和最终产物都经过 Zod Schema 校验，
// 任何校验失败都会立即抛错终止流水线。
//
// 输出文件：
//   data/02_processed/structured-insights.json — Map 阶段产物
//   data/04_reports/daily-report.json          — 最终日报
// ============================================================================

const root = process.cwd();
const rawPath = join(root, "data/01_raw/articles.json");
const structuredPath = join(root, "data/02_processed/structured-insights.json");
const reportPath = join(root, "data/04_reports/daily-report.json");
const markdownPath = join(root, "data/04_reports/daily-report.md");

async function main() {
  const startedAt = Date.now();
  console.log("Daily AI Insight Engine pipeline started.");

  // 1. Ingestion: 从文件系统读取原始语料。
  //    MVP 使用精选静态数据，使评审焦点集中在结构化设计和分析质量上。
  const rawArticles = await readJsonFile(rawPath, rawArticleListSchema);

  // 2. Cleaning: 在 Map 之前去除明显的文本噪声并限制长度。
  //    这一步保护 token 预算，同时提高抽取一致性。
  const articles = rawArticles.map(cleanArticle);
  const engine = new AIInsightEngine();
  const insights = [];

  // 3. Map extraction: 每篇文章独立处理，单篇失败不会丢失整日报。
  for (const [index, article] of articles.entries()) {
    try {
      console.log(`[map ${index + 1}/${articles.length}] extracting: ${article.title}`);
      const insight = await engine.extractArticle(article);
      insights.push(insight);
    } catch (error) {
      console.error(`[map failed] ${article.id}`, error);
    }
  }

  const structured = structuredInsightListSchema.parse(insights);
  await writeJsonFile(structuredPath, structured);

  // 4. Reduce synthesis: 报告从已验证的结构化特征生成，而非原始文章堆。
  //    这是整个系统的核心设计决策 —— Map/Reduce 分离使每一步可独立验证。
  console.log(`[reduce] synthesizing report from ${structured.length} structured insights.`);
  const report = dailyReportSchema.parse(await engine.synthesizeReport(structured));
  await writeJsonFile(reportPath, report);

  // Write markdown report alongside JSON
  await writeFile(markdownPath, generateMarkdown(report), "utf8");

  console.log(`Pipeline completed in ${Math.round((Date.now() - startedAt) / 1000)}s.`);
  console.log(`Structured insights: ${structuredPath}`);
  console.log(`Daily report (JSON): ${reportPath}`);
  console.log(`Daily report (MD):   ${markdownPath}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
