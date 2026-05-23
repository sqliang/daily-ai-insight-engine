// ============================================================================
// SourcesHero.tsx — Sources 页面顶部 Hero 横幅
//
// 展示数据源全景概览：总数量、最近更新日期、三层 Tier 概览卡片（黄金三角），
// 以及数据筛选策略说明（关键词过滤 + 时效窗口 + 配额去重）。
// 被 Sources 页面（src/app/page.tsx）消费。
// ============================================================================

import type { TierMeta } from "@/lib/data/tiers";
import { TIER_COLORS } from "@/lib/data/tiers";

type SourcesHeroProps = {
  tiersMeta: Record<string, TierMeta>;
  totalSources: number;
  latestDate: string | null;
  tierSourceCounts: Record<string, number>;
};

/**
 * Sources 页面顶部 Hero 横幅，展示数据源全景概览。
 *
 * 包含总数据源数量、最近更新日期、三层 Tier 概览卡片（学术/产品/商业）
 * 以及数据筛选策略说明（关键词过滤+时效窗口+配额去重）。
 */
export function SourcesHero({
  tiersMeta,
  totalSources,
  latestDate,
  tierSourceCounts,
}: SourcesHeroProps) {
  return (
    <header className="relative overflow-hidden rounded-2xl bg-gradient-to-br from-foreground via-foreground to-accent-dark p-6 shadow-lg md:p-10">
      {/* Decorative SVG shapes */}
      <svg
        className="pointer-events-none absolute inset-0 h-full w-full"
        aria-hidden="true"
        viewBox="0 0 1200 400"
        preserveAspectRatio="none"
      >
        <circle cx="1050" cy="50" r="160" fill="oklch(0.55 0.13 200 / 0.10)" />
        <circle cx="1080" cy="30" r="90" fill="oklch(0.55 0.13 200 / 0.08)" />
        <circle cx="80" cy="350" r="120" fill="oklch(0.45 0.16 340 / 0.08)" />
        <circle cx="50" cy="370" r="70" fill="oklch(0.45 0.16 340 / 0.06)" />
        <circle cx="600" cy="380" r="100" fill="oklch(0.60 0.16 85 / 0.05)" />
        {Array.from({ length: 6 }).flatMap((_, row) =>
          Array.from({ length: 6 }).map((_, col) => (
            <circle
              key={`${row}-${col}`}
              cx={30 + col * 22}
              cy={20 + row * 22}
              r="1"
              fill="oklch(1 0 0 / 0.15)"
            />
          )),
        )}
        <line
          x1="30" y1="385" x2="400" y2="385"
          stroke="oklch(0.55 0.13 200 / 0.20)"
          strokeWidth="0.5"
          strokeDasharray="4 6"
        />
      </svg>

      <div className="relative">
        {/* Label */}
        <p className="text-[11px] font-semibold uppercase tracking-widest text-accent-light/80">
          Source Intelligence
        </p>

        {/* Title */}
        <h1 className="mt-3 text-2xl font-bold tracking-tight text-white md:text-3xl">
          数据源全景<span className="text-accent-light/60"> · </span>
          <span className="bg-gradient-to-r from-accent-light via-white to-accent-light bg-clip-text text-transparent">
            黄金三角
          </span>
        </h1>

        {/* Subtitle */}
        <p className="mt-2.5 max-w-full text-sm leading-relaxed text-white/55 md:text-[15px]">
          {totalSources} 个精选 AI 数据源，按学术/技术 → 产品/开发者 → 商业/资本三层分类，通过关键词过滤、时效窗口与配额控制，每日输出高信噪比的 AI 信息情报。
        </p>

        {/* Stats pills */}
        <div className="mt-5 flex flex-wrap items-center gap-2">
          <span className="inline-flex items-center gap-1.5 rounded-full border border-white/10 bg-white/5 px-3 py-1 text-[11px] font-medium text-white/70 backdrop-blur">
            <span className="h-1.5 w-1.5 rounded-full bg-accent" />
            {totalSources} 个数据源
          </span>
          {latestDate && (
            <span className="inline-flex items-center gap-1.5 rounded-full border border-white/10 bg-white/5 px-3 py-1 text-[11px] font-medium text-white/50 backdrop-blur">
              <svg width="11" height="11" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5">
                <circle cx="8" cy="8" r="6.5" />
                <path d="M8 4.5V8l3 2" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
              {latestDate}
            </span>
          )}
        </div>

        {/* Golden Triangle vertex cards */}
        <div className="mt-6 grid gap-4 sm:grid-cols-3">
          {(["A", "B", "C"] as const).map((tier) => {
            const meta = tiersMeta[tier];
            const color = TIER_COLORS[tier];
            const tierLetter = tier;

            return (
              <div
                key={tier}
                className="rounded-xl border border-white/8 bg-white/[0.03] p-4 backdrop-blur md:p-5"
              >
                {/* Tier color dot + letter */}
                <div className="flex items-center gap-3">
                  <span
                    className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full text-[13px] font-bold text-white"
                    style={{ backgroundColor: color }}
                  >
                    {tierLetter}
                  </span>
                  <div>
                    <p className="text-[15px] font-bold text-white">
                      {meta?.label ?? `Tier ${tierLetter}`}
                    </p>
                    <p className="text-[11px] text-white/40">
                      {(tierSourceCounts[tier] ?? 0)} 个源
                    </p>
                  </div>
                </div>
                <p className="mt-3 text-[12px] leading-relaxed text-white/50">
                  {meta?.subtitle ?? ""}
                </p>
              </div>
            );
          })}
        </div>

        {/* Filter strategy summary */}
        <div className="mt-5 rounded-xl border border-white/8 bg-white/[0.03] p-4 backdrop-blur md:p-5">
          <p className="text-[11px] font-semibold uppercase tracking-wider text-white/40">
            数据筛选策略
          </p>
          <div className="mt-3 grid gap-3 text-[12px] leading-relaxed text-white/50 sm:grid-cols-3">
            <div className="flex items-start gap-2.5">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="mt-0.5 shrink-0 text-accent-light/60">
                <polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3" />
              </svg>
              <span>关键词过滤 — 每个源配置专属关键词白名单，仅保留高度相关的 AI 技术内容</span>
            </div>
            <div className="flex items-start gap-2.5">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="mt-0.5 shrink-0 text-accent-light/60">
                <circle cx="12" cy="12" r="10" />
                <polyline points="12 6 12 12 16 14" />
              </svg>
              <span>时效窗口 — 48-72 小时抓取窗口，确保信息新鲜度，过时内容自动淘汰</span>
            </div>
            <div className="flex items-start gap-2.5">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="mt-0.5 shrink-0 text-accent-light/60">
                <path d="M12 20V10" />
                <path d="M18 20V4" />
                <path d="M6 20v-4" />
              </svg>
              <span>配额与去重 — 每 Tier 上限 5 篇 / 总计 15 篇，按 impact 评分择优保留</span>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}
