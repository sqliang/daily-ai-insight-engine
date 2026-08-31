// ============================================================================
// reports.ts — 日报数据访问层
//
// 提供日报列表和按日期读取的能力，供 /dashboard（卡片列表）、
// /dashboard/[date]（可视化仪表盘）、/report/[date]（Markdown 全文）消费。
//
// 数据源：PostgreSQL daily_reports 表（由 pipeline Stage 5 publish 写入）。
// ============================================================================

import { and, desc, eq, gte, inArray, lte } from "drizzle-orm";

import { dailyReportSchema, type DailyReport } from "@/lib/agent/schema";
import type { DateRange } from "@/lib/data/types";
import { getDb } from "@/lib/db/client";
import { dailyReports } from "@/lib/db/schema";
import { paginate } from "@/lib/utils/pagination";

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
 * 查询日报日期列表（按日期范围过滤 + 降序排序）。
 *
 * 两阶段实现（性能考虑）：
 *   1. 仅查 date 列做范围过滤与排序 —— 不搬运 JSONB，
 *      totalCount 与 oldest/latest 日期都在这一阶段得出
 *   2. 只对当前页 slice 命中的日期取整行 JSONB + Zod parse
 * 全量范围（"全部"预设）下，旧文件实现需解析目录内每一个日报 JSON
 * （44+ 个、共数 MB）才能渲染卡片列表，是 /dashboard 卡顿的根因之一。
 *
 * 参数：
 *   dateRange:  可选日期范围过滤
 *   pagination: 可选分页参数；缺省时返回范围内全部日报
 */
export async function listReports(
  dateRange?: DateRange,
  pagination?: ListReportsPagination,
): Promise<ListReportsResult> {
  const db = getDb();

  // ---- 阶段 1：date 列级过滤与排序（不搬运 JSONB） ----
  const conditions = [];
  if (dateRange?.from) conditions.push(gte(dailyReports.date, dateRange.from));
  if (dateRange?.to) conditions.push(lte(dailyReports.date, dateRange.to));

  const dateRows = await db
    .select({ date: dailyReports.date })
    .from(dailyReports)
    .where(conditions.length > 0 ? and(...conditions) : undefined)
    .orderBy(desc(dailyReports.date));
  const dates = dateRows.map((r) => r.date);

  // ---- 阶段 2：仅取当前页 slice 命中的行 ----
  // 未传分页参数时以 totalCount 为页大小，退化为全量返回（兼容旧行为）
  const paged = paginate(
    dates,
    pagination?.page ?? 1,
    pagination?.pageSize ?? Math.max(dates.length, 1),
  );

  const reportRows = paged.items.length
    ? await db
        .select({ date: dailyReports.date, report: dailyReports.report })
        .from(dailyReports)
        .where(inArray(dailyReports.date, paged.items))
    : [];
  // inArray 不保证返回顺序，按 date 建索引后按分页顺序重组
  const byDate = new Map(reportRows.map((r) => [r.date, r.report]));

  const summaries: ReportSummary[] = [];
  for (const date of paged.items) {
    const raw = byDate.get(date);
    if (raw === undefined) continue;
    try {
      const report = dailyReportSchema.parse(raw);
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
      // 跳过解析失败的行（数据损坏或格式不兼容）
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
  const db = getDb();
  const rows = await db
    .select({ report: dailyReports.report })
    .from(dailyReports)
    .where(eq(dailyReports.date, date))
    .limit(1);

  const raw = rows[0]?.report;
  if (raw === undefined) return null;

  try {
    return dailyReportSchema.parse(raw);
  } catch {
    return null;
  }
}

/**
 * 读取指定日期的日报 Markdown 全文。
 *
 * 优先读取 daily_reports.report_md（管道 Stage 4b 产出、publish 入库），
 * 为空时降级为 report JSON → generateMarkdown() 转换。
 *
 * 参数：
 *   date: 日报日期，格式 YYYY-MM-DD
 *
 * 返回：
 *   Markdown 字符串或 null（该日期无报告）
 */
export async function getReportMarkdown(date: string): Promise<string | null> {
  const db = getDb();
  const rows = await db
    .select({ reportMd: dailyReports.reportMd })
    .from(dailyReports)
    .where(eq(dailyReports.date, date))
    .limit(1);

  // 优先返回入库的 .md 全文（publish 时已剥离 YAML frontmatter）
  const md = rows[0]?.reportMd;
  if (md) return md;

  // JSON → Markdown 降级
  const report = await getReport(date);
  if (!report) return null;

  const { generateMarkdown } = await import("@/lib/report/generate-markdown");
  return generateMarkdown(report);
}
