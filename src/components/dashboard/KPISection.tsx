import { MetricCard } from "@/components/dashboard/MetricCard";
import type { DailyReport } from "@/lib/agent/schema";

type KPISectionProps = {
  dataSourceSummary: DailyReport["dataSourceSummary"];
};

export function KPISection({ dataSourceSummary }: KPISectionProps) {
  return (
    <section className="mt-6 grid gap-4 md:grid-cols-3">
      <MetricCard
        label="样本量"
        value={dataSourceSummary.totalArticles}
        helper="逐篇 Map 抽取后再 Reduce 聚合"
        accent="accent"
        icon={
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5">
            <path d="M2 3h4l2 2h6v7H2V3z" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        }
      />
      <MetricCard
        label="信源数"
        value={dataSourceSummary.sources.length}
        helper={dataSourceSummary.sources.slice(0, 4).join(" / ")}
        accent="warm"
        icon={
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5">
            <circle cx="8" cy="8" r="6" />
            <ellipse cx="8" cy="8" rx="3" ry="6" />
            <path d="M2 8h12" />
          </svg>
        }
      />
      <MetricCard
        label="语言覆盖"
        value={dataSourceSummary.languages.join(" + ")}
        helper="混合中英文信源，兼顾全球与本土语境"
        accent="cool"
        icon={
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5">
            <path d="M2 5h12M5 2v3m6-3v3M3 8h10v5a1 1 0 01-1 1H4a1 1 0 01-1-1V8z" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        }
      />
    </section>
  );
}
