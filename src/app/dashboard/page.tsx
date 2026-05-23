import { readFile } from "node:fs/promises";
import { join } from "node:path";

import { DeepDivesSection } from "@/components/dashboard/DeepDivesSection";
import { DistributionSection } from "@/components/dashboard/DistributionSection";
import { KPISection } from "@/components/dashboard/KPISection";
import { RankingsSection } from "@/components/dashboard/RankingsSection";
import { ReportFooter } from "@/components/dashboard/ReportFooter";
import { ReportHeader } from "@/components/dashboard/ReportHeader";
import { SignalList } from "@/components/dashboard/SignalList";
import { TopEventsSection } from "@/components/dashboard/TopEventsSection";
import { TrendInsightsSection } from "@/components/dashboard/TrendInsightsSection";
import { ErrorBoundary } from "@/components/charts/ErrorBoundary";
import { PageShell } from "@/components/layout/PageShell";
import { dailyReportSchema } from "@/lib/agent/schema";

export const dynamic = "force-dynamic";

async function getReport() {
  try {
    const filePath = join(process.cwd(), "data/05_reports/daily-report.json");
    const content = await readFile(filePath, "utf8");
    return dailyReportSchema.parse(JSON.parse(content));
  } catch {
    return null;
  }
}

export default async function DashboardPage() {
  const report = await getReport();

  if (!report) {
    return (
      <PageShell>
        <div className="flex flex-col items-center justify-center py-32 text-center">
          <svg
            width="48" height="48" viewBox="0 0 24 24" fill="none"
            stroke="var(--muted)" strokeWidth="1.2" strokeLinecap="round" strokeLinejoin="round"
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
            日报文件尚未生成，请先运行数据管道（scout → ingest → extract → analyze →
            synthesize）以产出当日 AI 情报日报。
          </p>
        </div>
      </PageShell>
    );
  }

  return (
    <PageShell>
      <ReportHeader
        report={{
          reportTitle: report.reportTitle,
          date: report.date,
          generatedAt: report.generatedAt,
          executiveSummary: report.executiveSummary,
        }}
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

      <section className="mt-6 grid gap-5 lg:grid-cols-2">
        <ErrorBoundary sectionName="风险提示">
          <SignalList title="风险提示" items={report.riskSignals} />
        </ErrorBoundary>
        <ErrorBoundary sectionName="机会提示">
          <SignalList title="机会提示" items={report.opportunitySignals} />
        </ErrorBoundary>
      </section>

      <ReportFooter selectionRationale={report.dataSourceSummary.selectionRationale} />
    </PageShell>
  );
}
