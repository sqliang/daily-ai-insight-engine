// ============================================================================
// reports.ts — 日报数据访问层（PostgreSQL 主数据源 + 快照回退）
//
// 提供日报列表和按日期读取的能力，供 /dashboard（卡片列表）、
// /dashboard/[date]（可视化仪表盘）、/report/[date]（Markdown 全文）消费。
//
// 正常读取 PostgreSQL daily_reports 表；只有 DB 抛错时才通过 withDbFallback
// 读取 data/snapshot（本地优先、远程 data-snapshot 分支兜底）。DB 返回
// null / 空数组表示数据不存在，不触发快照回退。
// ============================================================================

import { cache } from "react";
import { and, desc, eq, gte, inArray, lte } from "drizzle-orm";

import { dailyReportSchema, type DailyReport } from "@/lib/agent/schema";
import {
  detectSpecializedAvailability,
  type ListReportsPagination,
  type ListReportsResult,
  type ReportSummary,
  type SpecializedAvailability,
} from "@/lib/data/report-shared";
import { withDbFallback } from "@/lib/data/snapshot/fallback";
import {
  getReport as getReportFromSnapshot,
  getReportMarkdown as getReportMarkdownFromSnapshot,
  listReportDates as listReportDatesFromSnapshot,
  listReports as listReportsFromSnapshot,
} from "@/lib/data/snapshot/reports";
import type { DateRange } from "@/lib/data/types";
import { getDb } from "@/lib/db/client";
import { dailyReports } from "@/lib/db/schema";
import { paginate } from "@/lib/utils/pagination";

// 保持既有对外导入路径不变，共享类型与纯函数由 report-shared 提供
export { detectSpecializedAvailability };
export type {
  ListReportsPagination,
  ListReportsResult,
  ReportSummary,
  SpecializedAvailability,
};

// ============================================================================
// 数据读取
// ============================================================================

/** 从 daily_reports 表列出全部日报日期（仅 date 列，不搬运 JSONB） */
async function listReportDatesFromDb(): Promise<string[]> {
  const db = getDb();
  const rows = await db
    .select({ date: dailyReports.date })
    .from(dailyReports)
    .orderBy(desc(dailyReports.date));
  return rows.map((r) => r.date);
}

/**
 * 列出全部日报日期（YYYY-MM-DD，降序）。
 *
 * 供各 [date] 动态段页面的 generateStaticParams 使用。DB 抛错时自动回退
 * 到快照 index.json，因此构建期 DB 挂起也能预渲染真实日期；只有快照也
 * 不可用才向调用方抛错。React cache() 保留请求内去重。
 */
export const listReportDates = cache(
  withDbFallback(listReportDatesFromDb, listReportDatesFromSnapshot),
);

/** 从 PostgreSQL 查询日报列表（两阶段：日期过滤分页 → 当前页 JSONB） */
async function listReportsFromDb(
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
 * 查询日报日期列表（按日期范围过滤 + 降序排序）。
 *
 * 保持两阶段实现与 ReportSummary 结构；DB 抛错时回退到快照，
 * DB 返回空列表时不回退。
 */
export const listReports = withDbFallback(
  listReportsFromDb,
  listReportsFromSnapshot,
);

/** 从 daily_reports 表读取指定日期的完整日报 */
async function getReportFromDb(date: string): Promise<DailyReport | null> {
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
 * 读取指定日期的完整日报数据。
 * React cache() 保留请求内去重（generateMetadata 与页面组件共享结果）；
 * 只有 DB 抛错才回退快照，DB 返回 null（该日期无报告）时不回退。
 */
export const getReport = cache(
  withDbFallback(getReportFromDb, getReportFromSnapshot),
);

/** 从 daily_reports 表读取 Markdown；为空时经 getReport 降级为 JSON → Markdown */
async function getReportMarkdownFromDb(date: string): Promise<string | null> {
  const db = getDb();
  const rows = await db
    .select({ reportMd: dailyReports.reportMd })
    .from(dailyReports)
    .where(eq(dailyReports.date, date))
    .limit(1);

  // 优先返回入库的 .md 全文（publish 时已剥离 YAML frontmatter）
  const md = rows[0]?.reportMd;
  if (md) return md;

  // JSON → Markdown 降级；getReport 自身保留请求级缓存与快照回退
  const report = await getReport(date);
  if (!report) return null;

  const { generateMarkdown } = await import("@/lib/report/generate-markdown");
  return generateMarkdown(report);
}

/**
 * 读取指定日期的日报 Markdown 全文。
 * .md 优先，缺失时 JSON → Markdown；DB 抛错时回退快照，
 * React cache() 保留请求内去重。
 */
export const getReportMarkdown = cache(
  withDbFallback(getReportMarkdownFromDb, getReportMarkdownFromSnapshot),
);
