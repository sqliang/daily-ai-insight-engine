// ============================================================================
// dashboard/[date]/page.tsx — 指定日期的日报可视化仪表盘
//
// 根据 URL 中的 date 参数（YYYY-MM-DD）读取对应日报 JSON，
// 渲染完整的可视化仪表盘（KPI、图表、事件、信号等）。
// 面包屑导航和 "完整报告" 按钮均在 banner 内部，与 /sources/[name] 保持一致。
// ============================================================================

import { notFound } from "next/navigation";

import { PageShell } from "@/components/layout/PageShell";
import { DashboardContent } from "@/components/dashboard/DashboardContent";
import { getReport } from "@/lib/data/reports";

export const dynamic = "force-dynamic";

interface PageProps {
  params: Promise<{ date: string }>;
}

export default async function DashboardByDatePage({ params }: PageProps) {
  const { date } = await params;
  const report = await getReport(date);

  // 该日期无报告 → 404
  if (!report) {
    notFound();
  }

  return (
    <PageShell>
      <DashboardContent
        report={report}
        backHref="/dashboard"
        backLabel="返回日报列表"
      />
    </PageShell>
  );
}
