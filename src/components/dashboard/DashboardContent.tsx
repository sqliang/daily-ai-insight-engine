// ============================================================================
// DashboardContent.tsx — 日报可视化仪表盘内容组件
//
// 将仪表盘的完整布局（ReportHeader + KPI + 图表 + 事件 + 信号 + Footer）
// 提取为独立组件，接收 DailyReport 数据作为 props。
// 被 /dashboard/[date]/page.tsx 等服务端组件调用，保持纯展示逻辑。
// ============================================================================

import type { DailyReport } from "@/lib/agent/schema";

import { DeepDivesSection } from "@/components/dashboard/DeepDivesSection";
import { DistributionSection } from "@/components/dashboard/DistributionSection";
import { KPISection } from "@/components/dashboard/KPISection";
import { RankingsSection } from "@/components/dashboard/RankingsSection";
import { ReportFooter } from "@/components/dashboard/ReportFooter";
import { ReportHeader } from "@/components/dashboard/ReportHeader";
import { SignalList } from "@/components/dashboard/SignalList";
import { TopEventsSection } from "@/components/dashboard/TopEventsSection";
import { TrendInsightsSection } from "@/components/dashboard/TrendInsightsSection";
import { SpecializedBriefSection } from "@/components/dashboard/SpecializedBriefSection";
import { ErrorBoundary } from "@/components/charts/ErrorBoundary";

interface DashboardContentProps {
  report: DailyReport;
  /** 返回链接的 href（可选，不传则不显示面包屑） */
  backHref?: string;
  /** 返回链接的文本 */
  backLabel?: string;
}

/**
 * 日报可视化仪表盘完整内容。
 *
 * 包含日报的所有可视化区块：头部（含可选面包屑）、KPI、分布图、热门事件、排名、
 * 趋势洞察、深度分析、风险/机会信号、页脚。
 * 页面层负责数据获取，本组件仅负责布局和渲染。
 */
export function DashboardContent({ report, backHref, backLabel }: DashboardContentProps) {
  return (
    <>
      <ReportHeader
        report={{
          reportTitle: report.reportTitle,
          date: report.date,
          generatedAt: report.generatedAt,
          executiveSummary: report.executiveSummary,
        }}
        backHref={backHref}
        backLabel={backLabel}
      />

      <KPISection dataSourceSummary={report.dataSourceSummary} />

      <section className="mt-6">
        <ErrorBoundary sectionName="分布图">
          <DistributionSection visualizationData={report.visualizationData} />
        </ErrorBoundary>
      </section>

      <section className="mt-6">
        <ErrorBoundary sectionName="热门事件">
          <TopEventsSection topEvents={report.topEvents} />
        </ErrorBoundary>
      </section>

      <ErrorBoundary sectionName="排名">
        <RankingsSection visualizationData={report.visualizationData} />
      </ErrorBoundary>

      <ErrorBoundary sectionName="趋势洞察">
        <TrendInsightsSection trendInsights={report.trendInsights} />
      </ErrorBoundary>

      <ErrorBoundary sectionName="深度分析">
        <DeepDivesSection deepDives={report.deepDives} />
      </ErrorBoundary>

      {/* 专题洞察入口 */}
      <SpecializedBriefSection
        data={report.specializedBrief}
        date={report.date}
      />

      <section className="mt-6 grid gap-5 lg:grid-cols-2">
        <ErrorBoundary sectionName="风险提示">
          <SignalList title="风险提示" items={report.riskSignals} />
        </ErrorBoundary>
        <ErrorBoundary sectionName="机会提示">
          <SignalList title="机会提示" items={report.opportunitySignals} />
        </ErrorBoundary>
      </section>

      <ReportFooter selectionRationale={report.dataSourceSummary.selectionRationale} />
    </>
  );
}
