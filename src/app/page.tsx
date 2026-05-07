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

async function getReport() {
  const filePath = join(process.cwd(), "data/04_reports/daily-report.json");
  const content = await readFile(filePath, "utf8");
  return dailyReportSchema.parse(JSON.parse(content));
}

export default async function Home() {
  const report = await getReport();

  return (
    <PageShell>
      {/* ====== 页头区：标题 + 元信息 + 执行摘要 ====== */}
      <ReportHeader
        report={{
          reportTitle: report.reportTitle,
          date: report.date,
          generatedAt: report.generatedAt,
          executiveSummary: report.executiveSummary,
        }}
      />

      {/* ====== KPI 指标卡片区 ====== */}
      <KPISection dataSourceSummary={report.dataSourceSummary} />

      {/* ====== 分布图区：事件类型 + 情绪分布（双 Donut 并排） ====== */}
      <section className="mt-6">
        <DistributionSection visualizationData={report.visualizationData} />
      </section>

      {/* ====== Top 事件区（全宽） ====== */}
      <section className="mt-6">
        <TopEventsSection topEvents={report.topEvents} />
      </section>

      {/* ====== 影响力排名 + 高频实体（双栏） ====== */}
      <RankingsSection visualizationData={report.visualizationData} />

      {/* ====== 趋势判断区：雷达图 + 四维卡片 ====== */}
      <TrendInsightsSection trendInsights={report.trendInsights} />

      {/* ====== 深度分析区 ====== */}
      <DeepDivesSection deepDives={report.deepDives} />

      {/* ====== 风险 & 机会信号区 ====== */}
      <section className="mt-6 grid gap-5 lg:grid-cols-2">
        <SignalList title="风险提示" items={report.riskSignals} />
        <SignalList title="机会提示" items={report.opportunitySignals} />
      </section>

      {/* ====== 页脚 ====== */}
      <ReportFooter selectionRationale={report.dataSourceSummary.selectionRationale} />
    </PageShell>
  );
}
