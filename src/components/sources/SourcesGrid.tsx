import type { SourceStatus } from "@/lib/data/sources";
import { SourceCard } from "./SourceCard";

const tierConfig: Record<string, { label: string; color: string }> = {
  A: { label: "Core Sources", color: "var(--accent)" },
  B: { label: "Community & Developer", color: "var(--warm)" },
  C: { label: "News & Media", color: "var(--cool)" },
};

type SourcesGridProps = {
  sources: SourceStatus[];
};

export function SourcesGrid({ sources }: SourcesGridProps) {
  const grouped = new Map<string, SourceStatus[]>();
  for (const s of sources) {
    const list = grouped.get(s.tier) ?? [];
    list.push(s);
    grouped.set(s.tier, list);
  }

  return (
    <div className="space-y-8">
      {["A", "B", "C"].map((tier) => {
        const items = grouped.get(tier);
        if (!items || items.length === 0) return null;

        const cfg = tierConfig[tier] ?? { label: tier, color: "var(--line)" };

        return (
          <section key={tier}>
            {/* Tier header */}
            <div className="flex items-center gap-3 mb-4">
              <div
                className="h-2 w-2 rounded-full shrink-0"
                style={{ backgroundColor: cfg.color }}
              />
              <h2 className="text-[13px] font-semibold uppercase tracking-wider text-muted">
                {cfg.label}
                <span className="ml-2 font-normal normal-case text-muted/50">
                  ({items.length} sources)
                </span>
              </h2>
            </div>

            {/* Card grid */}
            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
              {items.map((source) => (
                <SourceCard key={source.name} source={source} />
              ))}
            </div>
          </section>
        );
      })}
    </div>
  );
}
