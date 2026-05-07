import type { DailyReport } from "@/lib/agent/schema";

type DeepDivesSectionProps = {
  deepDives: DailyReport["deepDives"];
};

const borderAccents = [
  "border-l-accent",
  "border-l-warm",
  "border-l-cool",
  "border-l-positive",
];

export function DeepDivesSection({ deepDives }: DeepDivesSectionProps) {
  return (
    <section className="mt-6 rounded-xl border border-line bg-panel p-5 shadow-sm">
      <h2 className="text-lg font-semibold">关键事件深度总结</h2>
      <div className="mt-5 grid gap-5 lg:grid-cols-3">
        {deepDives.map((item, i) => (
          <article
            key={item.title}
            className={`rounded-lg border border-l-2 ${borderAccents[i] ?? "border-l-accent"} bg-surface p-4 transition-all hover:-translate-y-0.5 hover:shadow-md`}
          >
            <h3 className="text-base font-semibold leading-7">{item.title}</h3>

            <div className="mt-4">
              <span className="text-[11px] font-semibold uppercase tracking-wider text-accent">
                背景
              </span>
              <p className="mt-1 text-sm leading-7 text-muted">{item.background}</p>
            </div>

            <div className="mt-4">
              <span className="text-[11px] font-semibold uppercase tracking-wider text-warm">
                影响
              </span>
              <p className="mt-1 text-sm leading-7 text-muted">{item.impact}</p>
            </div>

            <div className="mt-4">
              <span className="text-[11px] font-semibold uppercase tracking-wider text-cool">
                后续关注
              </span>
              <p className="mt-1 text-sm leading-7 text-muted">{item.watchNext}</p>
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}
