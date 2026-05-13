"use client";

import { useMemo } from "react";
import type { SourceStatus } from "@/lib/data/sources";
import type { TierMeta } from "@/lib/data/tiers";
import { TierSection } from "./TierSection";

type SourcesGridProps = {
  sources: SourceStatus[];
  tiersMeta: Record<string, TierMeta>;
};

export function SourcesGrid({ sources, tiersMeta }: SourcesGridProps) {
  const grouped = useMemo(() => {
    const map = new Map<string, SourceStatus[]>();
    for (const s of sources) {
      const list = map.get(s.tier) ?? [];
      list.push(s);
      map.set(s.tier, list);
    }
    return map;
  }, [sources]);

  return (
    <div className="mt-10 space-y-10">
      {["A", "B", "C"].map((tier) => {
        const items = grouped.get(tier);
        if (!items || items.length === 0) return null;

        return (
          <TierSection
            key={tier}
            tier={tier}
            meta={tiersMeta[tier]}
            sources={items}
          />
        );
      })}
    </div>
  );
}
