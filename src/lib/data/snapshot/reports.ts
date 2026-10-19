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
  getSnapshotIndex,
  readSnapshotFile,
  readSnapshotJson,
  SnapshotReadError,
} from "./client";

/**
 * 读取单日日报 JSON。
 *
 * 合法 null 仅限"索引中不存在该日期且文件确认不存在"。若 index.report_dates
 * 已包含日期而 JSON 缺失，说明快照不完整，必须抛错而不是误报 404/空页。
 */
async function readReportJson(date: string): Promise<unknown> {
  const raw = await readSnapshotJson(`reports/daily-report-${date}.json`);
  if (raw !== null) return raw;

  const index = await getSnapshotIndex();
  if (!index) {
    throw new SnapshotReadError("本地与远程数据快照均不可用");
  }
  if (!index.report_dates.includes(date)) return null;
  throw new SnapshotReadError(`索引包含 ${date}，但日报 JSON 确认缺失`);
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
 * 与 DB 版一致：只解析当前页日期的报告；JSON 缺失/传输失败会抛错，
 * 仅 schema 校验失败的单行才跳过。totalCount 与 oldest/latest 日期
 * 仍按 index 中的日期集合计算。
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
    // index 只应包含带 JSON 的日期；分页命中却读不到 JSON 是快照故障，
    // 不能静默跳过造成"有总数、无卡片"的空页（Markdown-only 不入 index）
    if (raw === null || raw === undefined) {
      throw new SnapshotReadError(`分页日报 JSON 读取失败：${paged.items[index]}`);
    }
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
 * 剥离 Markdown 开头的 YAML frontmatter（首行 --- 到第二个 ---）。
 * 与 pipeline/publish/publishers.py 的 strip_frontmatter 等价：
 * 无 frontmatter 或缺少闭合标记时原样返回。
 */
function stripFrontmatter(text: string): string {
  const lines = text.split(/(?<=\n)/);
  if (!lines.length || lines[0].trim() !== "---") return text;
  for (let i = 1; i < lines.length; i++) {
    if (lines[i].trim() === "---") {
      return lines.slice(i + 1).join("").replace(/^\n+/, "");
    }
  }
  return text;
}

/**
 * 读取日报 Markdown 全文；.md 缺失时回退为 JSON → Markdown 转换。
 * 快照 .md 含 YAML frontmatter，返回前按 publish 入库口径剥离，
 * 保证 /report/[date] 的 DB 与快照渲染一致。
 */
export async function getReportMarkdown(date: string): Promise<string | null> {
  const markdown = await readSnapshotFile(`reports/daily-report-${date}.md`);
  if (markdown) return stripFrontmatter(markdown);

  const report = await getReport(date);
  if (!report) return null;
  const { generateMarkdown } = await import("@/lib/report/generate-markdown");
  return generateMarkdown(report);
}
