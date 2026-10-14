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
import { getReport, listReportDates } from "@/lib/data/reports";

// 日报数据一天只发布一两次，1 小时 ISR 足够新鲜（issue #152）
export const revalidate = 3600;

/**
 * 构建期预渲染所有已知日报日期（dynamicParams 默认开启，
 * 新发布的日期仍按需生成并按 revalidate 缓存）。
 *
 * fail-soft：CI 无 DATABASE_URL、或 Neon 挂起导致 DB 不可达时，
 * 返回空数组跳过构建期预渲染（页面降级为运行时按需 ISR），
 * 绝不让构建失败（issue #152 后续修复）。
 */
export async function generateStaticParams() {
  try {
    const dates = await listReportDates();
    return dates.map((date) => ({ date }));
  } catch {
    return [];
  }
}

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
