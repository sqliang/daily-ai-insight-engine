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
import { PageShell } from "@/components/layout/PageShell";
import { dailyReportSchema } from "@/lib/agent/schema";

export const dynamic = "force-dynamic";

async function getReport() {
  const filePath = join(process.cwd(), "data/05_reports/daily-report.json");
  const content = await readFile(filePath, "utf8");
  return dailyReportSchema.parse(JSON.parse(content));
}

export default async function DashboardPage() {
  const report = await getReport();

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
        <DistributionSection visualizationData={report.visualizationData} />
      </section>

      <section className="mt-6">
        <TopEventsSection topEvents={report.topEvents} />
      </section>

      <RankingsSection visualizationData={report.visualizationData} />

      <TrendInsightsSection trendInsights={report.trendInsights} />

      <DeepDivesSection deepDives={report.deepDives} />

      <section className="mt-6 grid gap-5 lg:grid-cols-2">
        <SignalList title="风险提示" items={report.riskSignals} />
        <SignalList title="机会提示" items={report.opportunitySignals} />
      </section>

      <ReportFooter selectionRationale={report.dataSourceSummary.selectionRationale} />
    </PageShell>
  );
}
