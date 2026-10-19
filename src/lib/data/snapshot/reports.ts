// ============================================================================
// snapshot/reports.ts — 从 data/snapshot 读取日报数据
//
// 函数签名与返回结构对齐 src/lib/data/reports.ts 的 DB 版本，由
// withDbFallback 在 DB 抛错时调用。列表查询保持"两阶段"口径：先用
// index.json 的日期过滤/分页，再只读取当前页命中的日报 JSON。
// ============================================================================

import { dailyReportSchema, type DailyReport } from "@/lib/agent/schema";
import {
  detectSpecializedAvailability,
  type ListReportsPagination,
  type ListReportsResult,
  type ReportSummary,
} from "@/lib/data/report-shared";
import type { DateRange } from "@/lib/data/types";
import { paginate } from "@/lib/utils/pagination";
import {
  assertSnapshotAvailable,
  getSnapshotIndex,
  readSnapshotFile,
  readSnapshotJson,
} from "./client";

/** 读取单日日报 JSON；文件缺失时先确认快照整体是否可用，区分空数据与故障 */
async function readReportJson(date: string): Promise<unknown> {
  const raw = await readSnapshotJson(`reports/daily-report-${date}.json`);
  if (raw === null) {
    await assertSnapshotAvailable();
  }
  return raw;
}

/**
 * 列出快照中的全部日报日期（来自 index.json，已为降序）。
 * 索引不可用时抛出，避免把"快照故障"误报成"没有日报"。
 */
export async function listReportDates(): Promise<string[]> {
  const index = await getSnapshotIndex();
  if (!index) {
    throw new Error("本地与远程数据快照均不可用");
  }
  return index.report_dates;
}

/**
 * 查询快照日报列表（日期范围过滤 + 分页）。
 *
 * 与 DB 版一致：只解析当前页日期的报告；单份报告损坏时跳过该行，
 * totalCount / oldestDate / latestDate 仍按 index 中的日期集合计算。
 */
export async function listReports(
  dateRange?: DateRange,
  pagination?: ListReportsPagination,
): Promise<ListReportsResult> {
  let dates = await listReportDates();
  if (dateRange?.from) {
    dates = dates.filter((date) => date >= dateRange.from!);
  }
  if (dateRange?.to) {
    dates = dates.filter((date) => date <= dateRange.to!);
  }

  const paged = paginate(
    dates,
    pagination?.page ?? 1,
    pagination?.pageSize ?? Math.max(dates.length, 1),
  );
  const rawReports = await Promise.all(paged.items.map(readReportJson));

  const summaries: ReportSummary[] = [];
  for (const [index, raw] of rawReports.entries()) {
    if (raw === null || raw === undefined) continue;
    try {
      const report = dailyReportSchema.parse(raw);
      summaries.push({
        date: paged.items[index],
        reportTitle: report.reportTitle,
        executiveSummary: report.executiveSummary,
        totalArticles: report.dataSourceSummary.totalArticles,
        sourceCount: report.dataSourceSummary.sources.length,
        languages: report.dataSourceSummary.languages,
        specialized: detectSpecializedAvailability(report),
      });
    } catch {
      // 与 DB 版一致：跳过解析失败的行，不影响同页其他日报
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

/** 读取指定日期的完整日报；日期不存在或报告校验失败时返回 null */
export async function getReport(date: string): Promise<DailyReport | null> {
  const raw = await readReportJson(date);
  if (raw === null || raw === undefined) return null;
  try {
    return dailyReportSchema.parse(raw);
  } catch {
    return null;
  }
}

/**
 * 读取指定日期日报的原始 JSON payload（供专题页兼容新旧字段）。
 * 与 DB 版 loadReportPayload 一样不做 Zod 校验。
 */
export async function getReportPayload(
  date: string,
): Promise<Record<string, unknown> | null> {
  const raw = await readReportJson(date);
  if (!raw || typeof raw !== "object" || Array.isArray(raw)) return null;
  return raw as Record<string, unknown>;
}

/**
 * 读取日报 Markdown 全文；.md 缺失时回退为 JSON → Markdown 转换，
 * 与 DB 版的降级顺序一致。
 */
export async function getReportMarkdown(date: string): Promise<string | null> {
  const markdown = await readSnapshotFile(`reports/daily-report-${date}.md`);
  if (markdown === null) {
    await assertSnapshotAvailable();
  }
  if (markdown) return markdown;

  const report = await getReport(date);
  if (!report) return null;
  const { generateMarkdown } = await import("@/lib/report/generate-markdown");
  return generateMarkdown(report);
}
