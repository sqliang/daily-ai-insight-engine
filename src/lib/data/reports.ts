// ============================================================================
// reports.ts — 日报数据访问层
//
// 提供日报列表扫描和按日期读取的能力，供 /dashboard（卡片列表）、
// /dashboard/[date]（可视化仪表盘）、/report/[date]（Markdown 全文）消费。
//
// 文件命名约定：daily-report-{YYYY-MM-DD}.json / .md
// daily-report.json / .md 为最新版（管道 Stage 4b 写入），不在列表中返回。
// ============================================================================

import { readFile, readdir } from "node:fs/promises";
import { join } from "node:path";

import { dailyReportSchema, type DailyReport } from "@/lib/agent/schema";
import type { DateRange } from "@/lib/data/types";

// 日报文件命名前缀，用于识别和解析文件名中的日期
const REPORT_PREFIX = "daily-report-";
const REPORT_SUFFIX = ".json";

// ============================================================================
// 类型定义
// ============================================================================

/** 日报卡片摘要 — 仅包含列表页卡片展示所需的字段 */
export interface ReportSummary {
  date: string;
  reportTitle: string;
  executiveSummary: string;
  totalArticles: number;
  /** 覆盖的信源数量 */
  sourceCount: number;
  /** 覆盖的语言种类 */
  languages: string[];
  /** 当日专题报告可用性（Phase 1: GitHub, Phase 2: Product/Paper） */
  specialized: SpecializedAvailability;
}

// ============================================================================
// 专题报告可用性
// ============================================================================

/** 各专题报告类型在特定日期的数据可用性 */
export interface SpecializedAvailability {
  github: { count: number; domains: Record<string, number> } | null;
  product: { count: number } | null;
  paper: { count: number } | null;
}

/**
 * 检测指定日期是否有 GitHub 专题数据。
 *
 * 扫描 data/04_structured/github-trending.json（热数据），
 * 按 created 日期分组，检查是否存在带 specialized_tags.github 的文章。
 */
// ============================================================================
// 数据读取
// ============================================================================

/**
 * 扫描 data/05_reports/ 目录，列出所有历史日报摘要。
 *
 * 仅匹配 daily-report-{YYYY-MM-DD}.json 格式的文件，
 * 排除 daily-report.json（最新版管道输出）。
 *
 * 返回按 date 降序排列的摘要列表。
 */
export async function listReports(dateRange?: DateRange): Promise<ReportSummary[]> {
  const reportsDir = join(process.cwd(), "data/05_reports");
  let entries: string[];

  try {
    entries = await readdir(reportsDir);
  } catch {
    return []; // 目录不存在，返回空列表
  }

  const summaries: ReportSummary[] = [];

  for (const filename of entries) {
    // 仅匹配 daily-report-YYYY-MM-DD.json，排除 daily-report.json
    if (!filename.startsWith(REPORT_PREFIX) || !filename.endsWith(REPORT_SUFFIX)) {
      continue;
    }

    const date = filename.slice(
      REPORT_PREFIX.length,
      filename.length - REPORT_SUFFIX.length,
    );
    // 日期格式校验：YYYY-MM-DD
    if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) {
      continue;
    }

    // 日期范围过滤
    if (dateRange) {
      if (dateRange.from && date < dateRange.from) continue;
      if (dateRange.to && date > dateRange.to) continue;
    }

    try {
      const raw = await readFile(join(reportsDir, filename), "utf8");
      const report = dailyReportSchema.parse(JSON.parse(raw));
      // 从日报 JSON 的 specializedBrief 提取专题可用性
      const sb = report.specializedBrief;
      summaries.push({
        date,
        reportTitle: report.reportTitle,
        executiveSummary: report.executiveSummary,
        totalArticles: report.dataSourceSummary.totalArticles,
        sourceCount: report.dataSourceSummary.sources.length,
        languages: report.dataSourceSummary.languages,
        specialized: {
          github: sb?.githubHighlights?.articleCount
            ? {
                count: sb.githubHighlights.articleCount,
                domains: sb.githubHighlights.domainDistribution || {},
              }
            : null,
          product: null,
          paper: sb?.paperHighlights?.articleCount
            ? { count: sb.paperHighlights.articleCount }
            : null,
        },
      });
    } catch {
      // 跳过解析失败的文件（数据损坏或格式不兼容）
    }
  }

  // 按日期降序排列（最新在前）
  summaries.sort((a, b) => b.date.localeCompare(a.date));
  return summaries;
}

/**
 * 读取指定日期的完整日报数据。
 *
 * 参数：
 *   date: 日报日期，格式 YYYY-MM-DD
 *
 * 返回：
 *   DailyReport 或 null（该日期无报告或解析失败）
 */
export async function getReport(date: string): Promise<DailyReport | null> {
  const filePath = join(
    process.cwd(),
    "data/05_reports",
    `daily-report-${date}.json`,
  );

  try {
    const raw = await readFile(filePath, "utf8");
    return dailyReportSchema.parse(JSON.parse(raw));
  } catch {
    return null;
  }
}

/**
 * 读取指定日期的日报 Markdown 全文。
 *
 * 优先读取 daily-report-{date}.md（管道直接产出），
 * 不存在时降级为 JSON → generateMarkdown() 转换。
 *
 * 参数：
 *   date: 日报日期，格式 YYYY-MM-DD
 *
 * 返回：
 *   Markdown 字符串或 null（该日期无任何报告文件）
 */
export async function getReportMarkdown(date: string): Promise<string | null> {
  const reportsDir = join(process.cwd(), "data/05_reports");
  const mdPath = join(reportsDir, `daily-report-${date}.md`);

  // 优先读取 .md 文件
  try {
    const raw = await readFile(mdPath, "utf8");
    // 去除 YAML frontmatter（--- ... ---）
    return raw.replace(/^---[\s\S]*?---\n*/, "").trimStart();
  } catch {
    // .md 不存在，降级为 JSON 转换
  }

  // JSON → Markdown 降级
  const report = await getReport(date);
  if (!report) return null;

  const { generateMarkdown } = await import("@/lib/report/generate-markdown");
  return generateMarkdown(report)
    .replace(/^---[\s\S]*?---\n*/, "")
    .trimStart();
}
