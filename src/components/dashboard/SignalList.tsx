import { severityLabels } from "@/lib/report/labels";
import type { DailyReport } from "@/lib/agent/schema";

type SignalListProps = {
  title: string;
  items: DailyReport["riskSignals"];
};

const severityStyle = {
  low: {
    pill: "bg-slate-100 text-slate-600",
    bar: "bg-slate-300",
    tint: "",
  },
  medium: {
    pill: "bg-warm-light text-warm",
    bar: "bg-warm",
    tint: "bg-warm-light/20",
  },
  high: {
    pill: "bg-cool-light text-cool",
    bar: "bg-cool",
    tint: "bg-cool-light/20",
  },
};

const severityWidth = {
  low: "w-1/4",
  medium: "w-3/5",
  high: "w-full",
};

export function SignalList({ title, items }: SignalListProps) {
  const isRisk = title.includes("风险");

  return (
    <section className="rounded-xl border border-line bg-panel p-5 shadow-sm">
      <div className="flex items-center gap-2">
        <span className="flex h-7 w-7 items-center justify-center rounded-lg bg-accent-light text-accent text-sm">
          {isRisk ? "!" : "?"}
        </span>
        <h2 className="text-base font-semibold">{title}</h2>
      </div>
      <div className="mt-4 space-y-3">
        {items.map((item) => {
          const style = severityStyle[item.severity];
          return (
            <article
              key={`${item.signal}-${item.rationale}`}
              className={`rounded-lg border border-line p-4 first:border-t ${style.tint}`}
            >
              <div className="flex items-start justify-between gap-3">
                <h3 className="text-sm font-semibold leading-6">{item.signal}</h3>
                <span className={`shrink-0 rounded-full px-2.5 py-0.5 text-xs font-medium ${style.pill}`}>
                  {severityLabels[item.severity]}
                </span>
              </div>
              <div className="mt-2 h-1 w-full rounded-full bg-line">
                <div className={`h-1 rounded-full ${style.bar} ${severityWidth[item.severity]}`} />
              </div>
              <p className="mt-2 text-sm leading-6 text-muted">{item.rationale}</p>
            </article>
          );
        })}
      </div>
    </section>
  );
}
