// ============================================================================
// dashboard/[date]/page.tsx — 指定日期的日报可视化仪表盘
//
// 根据 URL 中的 date 参数（YYYY-MM-DD）读取对应日报 JSON，
// 渲染完整的可视化仪表盘（KPI、图表、事件、信号等）。
// 面包屑导航和 "完整报告" 按钮均在 banner 内部，与 /sources/[name] 保持一致。
// ============================================================================

import { notFound } from "next/navigation";
import type { Metadata } from "next";

import { PageShell } from "@/components/layout/PageShell";
import { DashboardContent } from "@/components/dashboard/DashboardContent";
import { DataUnavailable } from "@/components/ui/DataUnavailable";
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

/**
 * 生成页面元数据，并在流式渲染开始前做日报存在性检查。
 *
 * 设计理由：页面组件内 await 数据后再 notFound() 时，HTTP 状态码已被
 * 固定为 200（"假 404"，会被搜索引擎误收录）。generateMetadata 在页面
 * 渲染前执行，此处 notFound() 才能返回真正的 404 状态码。
 *
 * getReport 已被 React cache() 包装，与页面组件在同请求内共享结果，
 * 本检查不产生额外 DB 查询。
 *
 * 与 DB 不可达的交互：抛错时只返回通用标题、不做 notFound（数据可能
 * 只是暂时拿不到，不能误判 404），降级提示由页面组件层负责渲染。
 */
export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const { date } = await params;
  let report: Awaited<ReturnType<typeof getReport>>;
  try {
    report = await getReport(date);
  } catch {
    return { title: `日报看板 ${date} - Daily AI Insight Engine` };
  }
  if (!report) notFound();
  return { title: `日报看板 ${date} - Daily AI Insight Engine` };
}

export default async function DashboardByDatePage({ params }: PageProps) {
  const { date } = await params;

  // 运行时 fail-soft：DB 不可达时渲染降级提示页（issue #152）；
  // 注意与"该日期无报告"区分 —— 后者是正常返回 null，仍走 404
  let report: Awaited<ReturnType<typeof getReport>>;
  try {
    report = await getReport(date);
  } catch {
    return (
      <PageShell>
        <DataUnavailable />
      </PageShell>
    );
  }

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
