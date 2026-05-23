"use client";

// ============================================================================
// SourcesGrid.tsx — 数据源按 Tier 分组的网格布局
//
// 被 Sources 页面（src/app/page.tsx）消费。按 tier 字段将 SourceStatus[]
// 分组后委托 TierSection 渲染各组，使用 useMemo 优化分组计算，空分组自动跳过。
// ============================================================================

import { useMemo } from "react";
import type { SourceStatus } from "@/lib/data/sources";
import type { TierMeta } from "@/lib/data/tiers";
import { TierSection } from "./TierSection";

type SourcesGridProps = {
  sources: SourceStatus[];
  tiersMeta: Record<string, TierMeta>;
};

/**
 * 数据源网格布局，按 Tier（A/B/C）分组后委托 TierSection 渲染各组。
 *
 * Sources 页面的主内容区。使用 useMemo 按 tier 分组，空分组自动跳过。
 */
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
