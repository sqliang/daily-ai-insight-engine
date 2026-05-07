import { eventTypeLabels } from "@/lib/report/labels";
import type { DailyReport } from "@/lib/agent/schema";

type TopEventsSectionProps = {
  topEvents: DailyReport["topEvents"];
};

const rankCircleBg = [
  "bg-accent",
  "bg-warm",
  "bg-cool",
  "bg-positive",
  "bg-accent-dark",
];

export function TopEventsSection({ topEvents }: TopEventsSectionProps) {
  return (
    <section className="rounded-xl border border-line bg-panel p-5 shadow-sm">
      <h2 className="text-lg font-semibold">今日 Top 事件</h2>
      <div className="mt-5 divide-y divide-line">
        {topEvents.map((event, index) => (
          <article
            key={event.title}
            className="py-5 first:pt-0 last:pb-0 transition-shadow hover:shadow-sm hover:bg-surface/50 rounded-lg px-1 -mx-1"
          >
            <div className="flex flex-col gap-3 md:flex-row md:items-start md:justify-between">
              <div className="flex items-start gap-3">
                <span
                  className={`flex h-7 w-7 shrink-0 items-center justify-center rounded-full ${rankCircleBg[index] ?? "bg-accent"} text-xs font-bold text-white`}
                >
                  {index + 1}
                </span>
                <div>
                  <span className="rounded-full bg-accent-light px-2 py-0.5 text-[11px] font-medium text-accent">
                    {eventTypeLabels[event.eventType]}
                  </span>
                  <h3 className="mt-1.5 text-lg font-semibold leading-7">{event.title}</h3>
                </div>
              </div>
              <span className="shrink-0 rounded-lg border border-accent/20 bg-accent-light/40 px-2.5 py-1 text-xs font-semibold text-accent">
                Impact {event.impactScore}/10
              </span>
            </div>

            <div className="mt-1 flex items-center gap-2">
              <div className="h-1 flex-1 rounded-full bg-line">
                <div
                  className="h-1 rounded-full bg-gradient-to-r from-cool to-accent"
                  style={{ width: `${(event.impactScore / 10) * 100}%` }}
                />
              </div>
            </div>

            <p className="mt-3 text-sm leading-7 text-muted">{event.whyItMatters}</p>
            <ul className="mt-3 space-y-1.5 text-sm leading-6 text-muted">
              {event.evidence.map((item) => (
                <li key={item} className="flex items-start gap-2">
                  <span className="mt-2 h-1 w-1 shrink-0 rounded-full bg-accent" />
                  {item}
                </li>
              ))}
            </ul>
          </article>
        ))}
      </div>
    </section>
  );
}
