// ============================================================================
// dashboard/page.tsx — 日报卡片列表页
//
// 顶部 DashboardHero 阐述洞察产出与内化价值，下方为全宽横向卡片，
// 每张卡片展示日期、标题、摘要、
// 文章数、信源数、语言覆盖等关键信息。
// 点击卡片跳转到 /dashboard/[date] 可视化仪表盘。
// ============================================================================

import { PageShell } from "@/components/layout/PageShell";
import { DashboardHero } from "@/components/dashboard/DashboardHero";
import { ReportCard } from "@/components/reports/ReportCard";
import { listReports } from "@/lib/data/reports";

export const dynamic = "force-dynamic";

export default async function DashboardPage() {
  const reports = await listReports();

  // 空状态：尚无任何日报数据
  if (reports.length === 0) {
    return (
      <PageShell>
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
            日报文件尚未生成，请先运行数据管道（scout → ingest → extract → analyze
            → synthesize）以产出当日 AI 情报日报。
          </p>
        </div>
      </PageShell>
    );
  }

  const totalArticles = reports.reduce((sum, r) => sum + r.totalArticles, 0);
  // listReports 按日期降序：首项最新，末项最早
  const latestDate = reports[0]?.date ?? null;
  const oldestDate = reports[reports.length - 1]?.date ?? null;

  return (
    <PageShell>
      <DashboardHero
        reportCount={reports.length}
        totalArticles={totalArticles}
        oldestDate={oldestDate}
        latestDate={latestDate}
      />

      {/* ====== 卡片列表：全宽横向，垂直排列 ====== */}
      <div className="mt-8 flex flex-col gap-4">
        {reports.map((report) => (
          <ReportCard key={report.date} report={report} />
        ))}
      </div>
    </PageShell>
  );
}
