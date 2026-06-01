// ============================================================================
// SourcesHero.tsx — Sources 页面顶部 Hero 横幅
//
// 展示数据源全景概览：产品价值说明、三层 Tier 概览卡片（黄金三角）、
// 以及数据筛选策略说明。总数仅在分区标题与 Tier 卡片中展示，避免重复。
// 被 Sources 页面（src/app/page.tsx）消费。
// ============================================================================

import type { TierMeta } from "@/lib/data/tiers";
import { TIER_COLORS } from "@/lib/data/tiers";

type SourcesHeroProps = {
  tiersMeta: Record<string, TierMeta>;
  totalSources: number;
  tierSourceCounts: Record<string, number>;
};

/**
 * Sources 页面顶部 Hero 横幅，展示数据源全景概览。
 *
 * 包含产品价值说明、三层 Tier 概览卡片（学术/产品/商业），
 * 以及数据筛选策略说明（关键词过滤+时效窗口+配额去重）。
 */
export function SourcesHero({
  tiersMeta,
  totalSources,
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

        {/* Subtitle — 两段正文 + 独立价值主张，避免单行过长 */}
        <div className="mt-2.5 space-y-2 text-pretty md:space-y-2.5">
          <p className="text-sm leading-relaxed text-white/55 md:text-[15px] md:leading-7">
            聚合多个中英文精选优质信息数据源，通过{" "}
            <span className="font-medium text-white/85">黄金三角</span>
            {" "}串联技术前沿、产品动态与商业信号。
          </p>
          <p className="text-sm leading-relaxed text-white/55 md:text-[15px] md:leading-7">
            经采集、提炼与多维解读，把高噪资讯沉淀为{" "}
            <span className="font-medium text-white/85">带摘要与评分的结构化内容</span>
            ；既可{" "}
            <span className="text-accent-light/90">速览日报脉络</span>
            ，也能{" "}
            <span className="text-accent-light/90">单篇深读、按需回溯</span>
            。
          </p>
          <p className="mt-0.5 border-l-2 border-accent-light/60 py-0.5 pl-3.5 text-[15px] font-semibold leading-snug md:pl-4 md:text-base md:leading-relaxed">
            <span className="bg-gradient-to-r from-accent-light via-white to-accent-light bg-clip-text text-transparent">
              少花时间筛信息，多花时间理解与学习
            </span>
          </p>
        </div>

        {/* 分区标题：总数只在此处与 Tier 卡片联动展示 */}
        <div
          className="mt-5 flex items-center gap-3 md:mt-6"
          role="separator"
          aria-label={`黄金三角分层，共 ${totalSources} 路信源`}
        >
          <span className="shrink-0 text-[11px] font-semibold uppercase tracking-wider text-white/45">
            黄金三角
            <span className="mx-1.5 text-white/25">·</span>
            <span className="tabular-nums text-accent-light/90">{totalSources}</span>
            {" "}路信源
          </span>
          <div className="h-px min-w-0 flex-1 bg-gradient-to-r from-white/12 via-white/6 to-transparent" />
        </div>

        {/* Golden Triangle vertex cards */}
        <div className="mt-4 grid gap-4 sm:grid-cols-3">
          {(["A", "B", "C"] as const).map((tier) => {
            const meta = tiersMeta[tier];
            const color = TIER_COLORS[tier];
            const tierLetter = tier;

            return (
              <a
                key={tier}
                href={`#tier-${tier.toLowerCase()}`}
                className="block rounded-xl border border-white/8 bg-white/[0.03] p-4 backdrop-blur transition hover:border-white/15 hover:bg-white/[0.06] md:p-5"
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
              </a>
            );
          })}
        </div>

        {/* Filter strategy summary */}
        {/* <div className="mt-5 rounded-xl border border-white/8 bg-white/[0.03] p-4 backdrop-blur md:p-5">
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
        </div> */}
      </div>
    </header>
  );
}
