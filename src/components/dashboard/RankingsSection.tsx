import { HorizontalBarChart, type BarDatum } from "@/components/charts/HorizontalBarChart";
import type { DailyReport } from "@/lib/agent/schema";

type RankingsSectionProps = {
  visualizationData: DailyReport["visualizationData"];
};

const entityTypeColors: Record<string, string> = {
  company: "oklch(0.55 0.13 200)",
  technology: "oklch(0.60 0.16 85)",
  product: "oklch(0.45 0.16 340)",
  person: "oklch(0.48 0.02 260)",
  region: "oklch(0.50 0.06 140)",
};

export function RankingsSection({ visualizationData }: RankingsSectionProps) {
  const impactBars: BarDatum[] = visualizationData.impactRanking.slice(0, 8).map((item) => ({
    label: item.title.length > 24 ? item.title.slice(0, 22) + "…" : item.title,
    value: item.score,
  }));

  const entityBars: BarDatum[] = visualizationData.entityFrequency.slice(0, 10).map((item) => ({
    label: item.entity,
    value: item.count,
    color: entityTypeColors[item.type] ?? "oklch(0.48 0.02 260)",
  }));

  return (
    <section className="mt-6 grid gap-5 lg:grid-cols-2">
      <div className="rounded-xl border border-line bg-panel p-5 shadow-sm">
        <h2 className="text-base font-semibold">影响力排名</h2>
        <HorizontalBarChart data={impactBars} tone="cool" />
      </div>
      <div className="rounded-xl border border-line bg-panel p-5 shadow-sm">
        <h2 className="text-base font-semibold">高频实体</h2>
        <HorizontalBarChart data={entityBars} tone="accent" />
      </div>
    </section>
  );
}
