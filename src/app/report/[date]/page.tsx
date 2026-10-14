// ============================================================================
// report/[date]/page.tsx — 指定日期的日报 Markdown 全文
//
// 顶部复用 ReportHeader（与 /dashboard/[date] 同系深色 Banner），提供导航、
// 标题元数据及跳转看板入口；正文由 MarkdownRenderer 渲染长文。
// 优先读取 .md，降级为 JSON → Markdown 转换。
// ============================================================================

import { notFound } from "next/navigation";
import type { Metadata } from "next";

import { PageShell } from "@/components/layout/PageShell";
import { ReportHeader } from "@/components/dashboard/ReportHeader";
import { MarkdownRenderer } from "@/components/report/MarkdownRenderer";
import { DataUnavailable } from "@/components/ui/DataUnavailable";
import { getReport, getReportMarkdown, listReportDates } from "@/lib/data/reports";

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
 * 设计理由同 dashboard/[date]：页面组件内 await 后 notFound() 只能返回
 * 200 假 404；generateMetadata 在渲染前执行，此处才能返回真正的 404。
 * getReport 已被 React cache() 包装，与页面组件同请求共享结果，无额外
 * DB 查询。DB 不可达（抛错）时不误判 404，返回通用标题，降级提示由
 * 页面组件层负责。
 */
export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const { date } = await params;
  let report: Awaited<ReturnType<typeof getReport>>;
  try {
    report = await getReport(date);
  } catch {
    return {
      title: `AI 情报日报 ${date} - Daily AI Insight Engine`,
      description: `${date} AI 舆情分析日报完整报告`,
    };
  }
  if (!report) notFound();
  return {
    title: `AI 情报日报 ${date} - Daily AI Insight Engine`,
    description: `${date} AI 舆情分析日报完整报告`,
  };
}

export default async function ReportByDatePage({ params }: PageProps) {
  const { date } = await params;

  // 运行时 fail-soft：DB 不可达时渲染降级提示页（issue #152）；
  // 正常返回 null（该日期无报告/无 Markdown）仍走 404，语义不变
  let report: Awaited<ReturnType<typeof getReport>>;
  let markdown: Awaited<ReturnType<typeof getReportMarkdown>> = null;
  try {
    report = await getReport(date);
    if (report) {
      markdown = await getReportMarkdown(date);
    }
  } catch {
    return (
      <PageShell>
        <DataUnavailable />
      </PageShell>
    );
  }

  if (!report) {
    notFound();
  }

  if (!markdown) {
    notFound();
  }

  return (
    <PageShell>
      <ReportHeader
        report={report}
        backHref="/dashboard"
        backLabel="返回日报列表"
        actionHref={`/dashboard/${date}`}
        actionLabel="查看可视化仪表盘"
        showExecutiveSummary={false}
      />

      <div className="mt-8 w-full">
        <MarkdownRenderer content={markdown} maxWidthClass="" />
      </div>
    </PageShell>
  );
}
