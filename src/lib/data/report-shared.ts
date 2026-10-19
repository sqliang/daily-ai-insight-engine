// ============================================================================
// report-shared.ts — 日报摘要的共享类型与纯转换函数
//
// 从 reports.ts 抽出，供 PostgreSQL 数据层与 data/snapshot 快照读取器共用，
// 避免两个模块在回退封装时形成循环依赖。本模块不执行任何 I/O。
// ============================================================================

import type { DailyReport } from "@/lib/agent/schema";

// ---------------------------------------------------------------------------
// 日报卡片摘要类型
// ---------------------------------------------------------------------------

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

/** 各专题报告类型在特定日期的数据可用性 */
export interface SpecializedAvailability {
  github: { count: number; domains: Record<string, number> } | null;
  product: { count: number } | null;
  paper: { count: number } | null;
}

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
  /** 范围内日报总份数 */
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

// ---------------------------------------------------------------------------
// 专题报告可用性检测（DB / 快照共用，保证卡片口径一致）
// ---------------------------------------------------------------------------

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
