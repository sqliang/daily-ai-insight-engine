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
import { getReport, getReportMarkdown } from "@/lib/data/reports";

export const dynamic = "force-dynamic";

interface PageProps {
  params: Promise<{ date: string }>;
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const { date } = await params;
  return {
    title: `AI 情报日报 ${date} - Daily AI Insight Engine`,
    description: `${date} AI 舆情分析日报完整报告`,
  };
}

export default async function ReportByDatePage({ params }: PageProps) {
  const { date } = await params;
  const report = await getReport(date);

  if (!report) {
    notFound();
  }

  const markdown = await getReportMarkdown(date);

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
