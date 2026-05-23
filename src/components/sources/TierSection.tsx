import type { SourceStatus } from "@/lib/data/sources";
import type { TierMeta } from "@/lib/data/tiers";
import { TIER_COLORS } from "@/lib/data/tiers";
import { SourceCard } from "./SourceCard";

type TierSectionProps = {
  tier: string;
  meta: TierMeta | undefined;
  sources: SourceStatus[];
};

/**
 * 单层 Tier 数据源分组展示区块，包含标题栏和响应式卡片网格。
 *
 * 用于 SourcesGrid 中每个 Tier 分组。标题栏以彩色竖条 + Tier 标签 + 源数量徽章标识，
 * 内容区以 1/2/3 列响应式网格排列 SourceCard。
 */
export function TierSection({ tier, meta, sources }: TierSectionProps) {
  const color = TIER_COLORS[tier] ?? "var(--line)";

  return (
    <section className="animate-fade-up">
      {/* Section header */}
      <div className="flex items-center gap-4 mb-6">
        {/* Colored vertical bar */}
        <div
          className="h-8 w-1 shrink-0 rounded-full"
          style={{ backgroundColor: color }}
        />
        <div className="min-w-0 flex-1">
          <h2 className="text-xl font-bold text-foreground tracking-tight">
            {meta?.label ?? `Tier ${tier}`}
          </h2>
          {meta?.subtitle && (
            <p className="mt-1 text-sm text-muted line-clamp-1">
              {meta.subtitle}
            </p>
          )}
        </div>
        {/* Count badge */}
        <span
          className="inline-flex shrink-0 items-center gap-1.5 rounded-full px-3 py-1 text-[12px] font-medium whitespace-nowrap"
          style={{ backgroundColor: `${color}14`, color }}
        >
          <span className="h-1.5 w-1.5 rounded-full" style={{ backgroundColor: color }} />
          {sources.length} 个源
        </span>
      </div>

      {/* Card grid */}
      <div className="grid gap-5 md:grid-cols-2 lg:grid-cols-3">
        {sources.map((source) => (
          <SourceCard key={source.name} source={source} />
        ))}
      </div>
    </section>
  );
}
