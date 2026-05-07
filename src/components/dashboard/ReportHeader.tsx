// ============================================================================
// ReportHeader.tsx — 报告页头组件
//
// 职责：渲染日报首屏的页头区域，包含以下信息：
//   - 产品标签（Daily AI Insight Engine）
//   - 报告标题（动态生成，如"2025年5月7日 AI 日报"）
//   - 报告日期和生成时间
//   - 执行摘要（executive summary）
//
// 设计决策：
//   - 作为独立组件，便于页头样式/结构的单独维护
//   - 日期格式化使用 toLocaleString("zh-CN") 确保中文区域习惯
//   - 执行摘要独占一行，字体颜色为 muted，与主标题形成层级对比
// ============================================================================

import type { DailyReport } from "@/lib/agent/schema";

type ReportHeaderProps = {
  report: Pick<DailyReport, "reportTitle" | "date" | "generatedAt" | "executiveSummary">;
};

export function ReportHeader({ report }: ReportHeaderProps) {
  return (
    <header className="border-b border-line pb-6">
      <div className="flex flex-col gap-4 md:flex-row md:items-end md:justify-between">
        <div>
          <p className="text-sm font-medium text-signal">Daily AI Insight Engine</p>
          <h1 className="mt-2 max-w-4xl text-3xl font-semibold tracking-normal md:text-5xl">
            {report.reportTitle}
          </h1>
        </div>
        <div className="text-sm leading-6 text-muted md:text-right">
          <p>报告日期：{report.date}</p>
          <p>生成时间：{new Date(report.generatedAt).toLocaleString("zh-CN")}</p>
        </div>
      </div>
      <p className="mt-5 max-w-5xl text-base leading-8 text-muted">{report.executiveSummary}</p>
    </header>
  );
}
