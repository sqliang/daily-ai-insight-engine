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
import { paginate } from "@/lib/utils/pagination";

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
  /** 当日专题报告可用性 */
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
 * 从日报数据中提取各专题报告的可用性。
 *
 * 项目与产品洞察优先读取新 projectInsights/productInsights。
 * 历史报告没有新字段时，回退到 githubHighlights/productHighlights。
 *
 * 参数：
 *    report: 已解析的 DailyReport
 *
 * 返回：
 *    SpecializedAvailability 对象
 */
export function detectSpecializedAvailability(
  report: DailyReport,
): SpecializedAvailability {
  const projectInsights = report.specializedBrief?.projectInsights;
  const gh = report.specializedBrief?.githubHighlights;
  const github = projectInsights
    ? {
        count: projectInsights.items.length,
        domains: projectInsights.distribution,
      }
    : gh
    ? {
        count: gh.articleCount,
        domains: gh.domainDistribution,
      }
    : null;

  const productInsights = report.specializedBrief?.productInsights;
  const ph = report.specializedBrief?.productHighlights;
  const product = productInsights
    ? {
        count: productInsights.items.length,
      }
    : ph
    ? {
        count: ph.articleCount,
      }
    : null;

  return {
    github,
    product,
    // 论文洞察暂不恢复
    paper: null,
  };
}

// ============================================================================
// 数据读取
// ============================================================================

/** listReports 的分页参数；缺省时返回范围内全部日报（兼容旧行为） */
export interface ListReportsPagination {
  /** 目标页码（1-based），越界由 paginate() clamp */
  page?: number;
  /** 每页条数 */
  pageSize?: number;
}

/** listReports 返回值：当前页卡片摘要 + 分页与日期跨度元信息 */
export interface ListReportsResult {
  /** 当前页的日报摘要（按日期降序） */
  reports: ReportSummary[];
  /** 范围内日报总份数（文件名计数，无需解析 JSON） */
  totalCount: number;
  /** 当前页码（clamp 后） */
  page: number;
  /** 每页条数 */
  pageSize: number;
  /** 总页数 */
  totalPages: number;
  /** 范围内最早日报日期（无日报时为 null） */
  oldestDate: string | null;
  /** 范围内最新日报日期（无日报时为 null） */
  latestDate: string | null;
}

/**
 * 扫描 data/05_reports/ 目录，分页列出历史日报摘要。
 *
 * 两阶段实现（性能考虑）：
 *   1. 仅根据文件名做格式校验 + 日期范围过滤 + 降序排序 —— 零 JSON 解析，
 *      totalCount 与 oldest/latest 日期都在这一阶段得出
 *   2. 只对当前页 slice 命中的文件做 read + Zod parse
 * 全量范围（"全部"预设）下，旧实现需解析目录内每一个日报 JSON（44+ 个、
 * 共数 MB）才能渲染卡片列表，是 /dashboard 卡顿的根因之一。
 *
 * 仅匹配 daily-report-{YYYY-MM-DD}.json 格式的文件，
 * 排除 daily-report.json（最新版管道输出）。
 *
 * 参数：
 *   dateRange:  可选日期范围过滤
 *   pagination: 可选分页参数；缺省时返回范围内全部日报
 */
export async function listReports(
  dateRange?: DateRange,
  pagination?: ListReportsPagination,
): Promise<ListReportsResult> {
  const reportsDir = join(process.cwd(), "data/05_reports");
  let entries: string[];

  try {
    entries = await readdir(reportsDir);
  } catch {
    entries = []; // 目录不存在，按空列表处理
  }

  // ---- 阶段 1：文件名级别的过滤与排序（零 JSON 解析） ----
  const dates: string[] = [];
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

    dates.push(date);
  }

  // 按日期降序排列（最新在前）
  dates.sort((a, b) => b.localeCompare(a));

  // ---- 阶段 2：仅解析当前页 slice 命中的文件 ----
  // 未传分页参数时以 totalCount 为页大小，退化为全量返回（兼容旧行为）
  const paged = paginate(
    dates,
    pagination?.page ?? 1,
    pagination?.pageSize ?? Math.max(dates.length, 1),
  );

  const summaries: ReportSummary[] = [];
  for (const date of paged.items) {
    try {
      const raw = await readFile(
        join(reportsDir, `${REPORT_PREFIX}${date}${REPORT_SUFFIX}`),
        "utf8",
      );
      const report = dailyReportSchema.parse(JSON.parse(raw));
      summaries.push({
        date,
        reportTitle: report.reportTitle,
        executiveSummary: report.executiveSummary,
        totalArticles: report.dataSourceSummary.totalArticles,
        sourceCount: report.dataSourceSummary.sources.length,
        languages: report.dataSourceSummary.languages,
        specialized: detectSpecializedAvailability(report),
      });
    } catch {
      // 跳过解析失败的文件（数据损坏或格式不兼容）
    }
  }

  return {
    reports: summaries,
    totalCount: dates.length,
    page: paged.page,
    pageSize: paged.pageSize,
    totalPages: paged.totalPages,
    oldestDate: dates[dates.length - 1] ?? null,
    latestDate: dates[0] ?? null,
  };
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
