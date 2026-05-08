import { DonutChart, type DonutDatum } from "@/components/charts/DonutChart";
import { eventTypeLabels, sentimentLabels } from "@/lib/report/labels";
import type { DailyReport } from "@/lib/agent/schema";

type DistributionSectionProps = {
  visualizationData: DailyReport["visualizationData"];
};

const eventTypeColors: Record<string, string> = {
  infrastructure_update: "oklch(0.55 0.13 200)",
  framework_tools: "oklch(0.62 0.16 170)",
  capital_movement: "oklch(0.45 0.16 340)",
  application_landing: "oklch(0.60 0.16 85)",
  policy_and_safety: "oklch(0.50 0.20 20)",
};

const sentimentColors: Record<string, string> = {
  positive: "oklch(0.55 0.16 150)",
  neutral: "oklch(0.55 0.02 260)",
  negative: "oklch(0.50 0.20 20)",
  mixed: "oklch(0.65 0.18 90)",
};

function toDonutData(
  items: { label: string; count: number }[],
  labelMap: Record<string, string>,
  colorMap: Record<string, string>,
): DonutDatum[] {
  return items.map((item) => ({
    name: labelMap[item.label] ?? item.label,
    value: item.count,
    color: colorMap[item.label] ?? "oklch(0.55 0.02 260)",
  }));
}

function summarizeEventTypes(
  items: { label: string; count: number }[],
  labelMap: Record<string, string>,
) {
  const sorted = [...items].sort((a, b) => b.count - a.count);
  const top = sorted.slice(0, 2);
  const rest = sorted.slice(2);
  const restTotal = rest.reduce((s, i) => s + i.count, 0);
  const lines: string[] = [];

  if (top.length > 0) {
    const topNames = top.map((t) => `「${labelMap[t.label] ?? t.label}」`).join("、");
    lines.push(`${topNames} 占比最高，合计 ${top.reduce((s, t) => s + t.count, 0)} 条`);
  }
  if (rest.length > 0 && restTotal > 0) {
    const restNames = rest.slice(0, 2).map((r) => `「${labelMap[r.label] ?? r.label}」`).join("、");
    lines.push(`其余如 ${restNames} 等 ${rest.length} 类共 ${restTotal} 条，反映多元议题并行`);
  }

  return lines;
}

function summarizeSentiment(items: { label: string; count: number }[], total: number) {
  const sorted = [...items].sort((a, b) => b.count - a.count);
  const top = sorted[0];
  const lines: string[] = [];

  if (!top) return lines;

  const pct = Math.round((top.count / total) * 100);

  if (top.label === "neutral" || top.label === "mixed") {
    lines.push(`整体基调偏「${sentimentLabels[top.label]}」，${top.label === "neutral" ? "媒体以事实报道为主，情绪化表达较少" : "正面与负面信息交织，各方观点存在分歧"}`);
  } else if (top.label === "positive") {
    lines.push(`整体基调偏「正向」（${pct}%），行业利好信号集中，市场信心较强`);
  } else if (top.label === "negative") {
    lines.push(`整体基调偏「负向」（${pct}%），需关注风险事件对行业信心的冲击`);
  }

  const hasNegative = items.some((i) => i.label === "negative" && i.count > 0);
  if (hasNegative && top.label !== "negative") {
    lines.push(`存在少量负向信号，需持续跟踪是否发酵`);
  }

  return lines;
}

export function DistributionSection({ visualizationData }: DistributionSectionProps) {
  const total = visualizationData.eventTypeDistribution.reduce((s, i) => s + i.count, 0);
  const eventDonut = toDonutData(
    visualizationData.eventTypeDistribution,
    eventTypeLabels,
    eventTypeColors,
  );
  const sentimentDonut = toDonutData(
    visualizationData.sentimentDistribution,
    sentimentLabels,
    sentimentColors,
  );

  const eventSummary = summarizeEventTypes(
    visualizationData.eventTypeDistribution,
    eventTypeLabels,
  );
  const sentimentSummary = summarizeSentiment(
    visualizationData.sentimentDistribution,
    total,
  );

  return (
    <div className="grid gap-5 lg:grid-cols-2">
      <section className="rounded-xl border border-line bg-panel p-5 shadow-sm">
        <h2 className="text-base font-semibold">事件类型分布</h2>
        <DonutChart data={eventDonut} centerLabel={`总计 ${total}`} />
        {eventSummary.length > 0 && (
          <div className="mt-4 space-y-1.5 border-t border-line pt-4 text-sm leading-7 text-muted">
            {eventSummary.map((line, i) => (
              <p key={i}>{line}</p>
            ))}
          </div>
        )}
      </section>
      <section className="rounded-xl border border-line bg-panel p-5 shadow-sm">
        <h2 className="text-base font-semibold">情绪分布</h2>
        <DonutChart data={sentimentDonut} centerLabel={`总计 ${total}`} />
        {sentimentSummary.length > 0 && (
          <div className="mt-4 space-y-1.5 border-t border-line pt-4 text-sm leading-7 text-muted">
            {sentimentSummary.map((line, i) => (
              <p key={i}>{line}</p>
            ))}
          </div>
        )}
      </section>
    </div>
  );
}
