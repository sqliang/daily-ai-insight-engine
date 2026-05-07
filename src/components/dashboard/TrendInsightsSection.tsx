import { RadarChart, type RadarDimension } from "@/components/charts/RadarChart";
import type { DailyReport } from "@/lib/agent/schema";

type TrendInsightsSectionProps = {
  trendInsights: DailyReport["trendInsights"];
};

const dimensionMeta: Record<string, { label: string; icon: string; border: string }> = {
  technology: { label: "技术", icon: "T", border: "border-l-accent" },
  application: { label: "应用", icon: "A", border: "border-l-warm" },
  policy: { label: "政策", icon: "P", border: "border-l-cool" },
  capital: { label: "资本", icon: "C", border: "border-l-positive" },
};

function toRadarData(insights: DailyReport["trendInsights"]): RadarDimension[] {
  return insights.map((t) => ({
    dimension: dimensionMeta[t.dimension]?.label ?? t.dimension,
    value: Math.min(t.supportingSignals.length, 5),
  }));
}

export function TrendInsightsSection({ trendInsights }: TrendInsightsSectionProps) {
  const radarData = toRadarData(trendInsights);

  return (
    <section className="mt-6 rounded-xl border border-line bg-panel p-5 shadow-sm">
      <h2 className="text-lg font-semibold">趋势判断</h2>

      <div className="mt-4 mb-2 flex justify-center">
        <RadarChart data={radarData} height={280} />
      </div>

      <div className="mt-2 grid gap-4 md:grid-cols-2">
        {trendInsights.map((trend) => {
          const meta = dimensionMeta[trend.dimension] ?? {
            label: trend.dimension,
            icon: "?",
            border: "border-l-line",
          };
          return (
            <article
              key={trend.dimension}
              className={`rounded-lg border border-line border-l-2 ${meta.border} bg-surface p-4 transition-shadow hover:shadow-sm`}
            >
              <div className="flex items-center gap-2 mb-2">
                <span className="flex h-5 w-5 items-center justify-center rounded-full bg-accent-light text-[10px] font-bold text-accent">
                  {meta.icon}
                </span>
                <p className="text-xs font-medium uppercase tracking-wider text-muted">
                  {meta.label}
                </p>
              </div>
              <h3 className="text-base font-semibold leading-7">{trend.judgment}</h3>
              <ul className="mt-3 space-y-1.5">
                {trend.supportingSignals.map((s, i) => (
                  <li key={i} className="flex items-start gap-2 text-sm leading-6 text-muted">
                    <span className="mt-2 h-1 w-1 shrink-0 rounded-full bg-accent" />
                    {s}
                  </li>
                ))}
              </ul>
            </article>
          );
        })}
      </div>
    </section>
  );
}
