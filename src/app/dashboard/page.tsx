// ============================================================================
// dashboard/page.tsx — 日报卡片列表页
//
// 顶部 DashboardHero 阐述洞察产出与内化价值，中间 DateFilterBar 时间过滤，
// 下方为全宽横向卡片，每张卡片展示日期、标题、摘要、
// 文章数、信源数、语言覆盖等关键信息。
// 点击卡片跳转到 /dashboard/[date] 可视化仪表盘。
// ============================================================================

import { PageShell } from "@/components/layout/PageShell";
import { DashboardHero } from "@/components/dashboard/DashboardHero";
import { ReportCard } from "@/components/reports/ReportCard";
import { DateFilterBar } from "@/components/sources/DateFilterBar";
import { Pagination } from "@/components/ui/Pagination";
import { listReports } from "@/lib/data/reports";
import type { DateRange } from "@/lib/data/types";
import { PAGE_SIZE_REPORTS, parsePageParam } from "@/lib/utils/pagination";

export const dynamic = "force-dynamic";

// ---------------------------------------------------------------------------
// Search params
// ---------------------------------------------------------------------------

interface DashboardSearchParams {
  from?: string;
  to?: string;
  preset?: string;
  page?: string;
}

// ---------------------------------------------------------------------------
// 默认日期范围（近 15 天）
// ---------------------------------------------------------------------------

function defaultDateRange(): DateRange {
  const to = new Date().toISOString().slice(0, 10);
  const from = new Date(Date.now() - 14 * 86400000).toISOString().slice(0, 10);
  return { from, to };
}

// ---------------------------------------------------------------------------
// Page
// ---------------------------------------------------------------------------

export default async function DashboardPage({
  searchParams,
}: {
  searchParams: Promise<DashboardSearchParams>;
}) {
  const sp = await searchParams;

  // 日期范围：from/to 优先 → preset=latest 无限定 → 默认半个月
  let dateRange: DateRange | undefined;
  if (sp.from || sp.to) {
    dateRange = { from: sp.from, to: sp.to };
  } else if (sp.preset !== "latest") {
    dateRange = defaultDateRange();
  }
  // preset=latest → dateRange=undefined，显示全部

  // 服务端分页：仅解析当前页命中的日报 JSON，避免全量 parse 导致卡顿
  const { reports, totalCount, page, totalPages, oldestDate, latestDate } =
    await listReports(dateRange, {
      page: parsePageParam(sp.page),
      pageSize: PAGE_SIZE_REPORTS,
    });

  // 空状态：尚无任何日报数据
  if (reports.length === 0) {
    return (
      <PageShell>
        <div className="mt-6">
          <DateFilterBar />
        </div>
        <div className="flex flex-col items-center justify-center py-32 text-center">
          <svg
            width="48"
            height="48"
            viewBox="0 0 24 24"
            fill="none"
            stroke="var(--muted)"
            strokeWidth="1.2"
            strokeLinecap="round"
            strokeLinejoin="round"
            className="mb-5"
          >
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
            <polyline points="14 2 14 8 20 8" />
            <line x1="16" y1="13" x2="8" y2="13" />
            <line x1="16" y1="17" x2="8" y2="17" />
            <polyline points="10 9 9 9 8 9" />
          </svg>
          <h2 className="text-lg font-bold text-foreground">暂无日报数据</h2>
          <p className="mt-2 max-w-md text-sm leading-relaxed text-muted">
            当前筛选范围内暂无日报，请调整时间范围或运行数据管道。
          </p>
        </div>
      </PageShell>
    );
  }

  return (
    <PageShell>
      <DashboardHero
        reportCount={totalCount}
        oldestDate={oldestDate}
        latestDate={latestDate}
      />

      <div className="mt-6">
        <DateFilterBar />
      </div>

      {/* ====== 卡片列表：全宽横向，垂直排列 ====== */}
      <div id="report-list" className="mt-6 flex scroll-mt-20 flex-col gap-4">
        {reports.map((report) => (
          <ReportCard key={report.date} report={report} />
        ))}
      </div>

      <Pagination
        currentPage={page}
        totalPages={totalPages}
        totalItems={totalCount}
        anchorId="report-list"
      />
    </PageShell>
  );
}
