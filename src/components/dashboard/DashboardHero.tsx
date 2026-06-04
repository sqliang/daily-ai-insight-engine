// ============================================================================
// DashboardHero.tsx — 日报列表页顶部 Hero 横幅
//
// 阐述流水线产出侧价值：结构化洞察报告、可读可学的交付形态。
// 与 SourcesHero（信源输入）形成首尾呼应，被 dashboard/page.tsx 消费。
// ============================================================================

export type DashboardHeroProps = {
  /** 历史日报份数 */
  reportCount: number;
  /** 累计解读文章篇数 */
  totalArticles: number;
  /** 最早日报日期（YYYY-MM-DD） */
  oldestDate: string | null;
  /** 最新日报日期（YYYY-MM-DD） */
  latestDate: string | null;
};

/**
 * 日报列表页 Hero：说明洞察产出理念，并以分区标题展示归档规模。
 */
export function DashboardHero({
  reportCount,
  totalArticles,
  oldestDate,
  latestDate,
}: DashboardHeroProps) {
  const dateRangeLabel =
    oldestDate && latestDate
      ? oldestDate === latestDate
        ? oldestDate
        : `${oldestDate} — ${latestDate}`
      : null;

  return (
    <header className="relative overflow-hidden rounded-2xl bg-gradient-to-br from-foreground via-foreground to-accent-dark p-6 shadow-lg md:p-10">
      {/* 装饰性几何形状 — 与 SourcesHero 保持同一视觉语言 */}
      <svg
        className="pointer-events-none absolute inset-0 h-full w-full"
        aria-hidden="true"
        viewBox="0 0 1200 320"
        preserveAspectRatio="none"
      >
        <circle cx="1050" cy="50" r="150" fill="oklch(0.55 0.13 200 / 0.10)" />
        <circle cx="1080" cy="30" r="80" fill="oklch(0.55 0.13 200 / 0.08)" />
        <circle cx="80" cy="270" r="110" fill="oklch(0.45 0.16 340 / 0.08)" />
        <circle cx="50" cy="290" r="60" fill="oklch(0.45 0.16 340 / 0.06)" />
        {Array.from({ length: 5 }).flatMap((_, row) =>
          Array.from({ length: 5 }).map((_, col) => (
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
          x1="30"
          y1="300"
          x2="380"
          y2="300"
          stroke="oklch(0.55 0.13 200 / 0.20)"
          strokeWidth="0.5"
          strokeDasharray="4 6"
        />
      </svg>

      <div className="relative">
        {/* 品牌标签 */}
        <div className="flex items-center gap-2.5">
          <span className="relative flex h-2.5 w-2.5">
            <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-accent opacity-60" />
            <span className="relative inline-flex h-2.5 w-2.5 rounded-full bg-accent" />
          </span>
          <p className="text-[11px] font-medium uppercase tracking-[0.25em] text-accent-light/90">
            Daily AI Insight Engine
          </p>
        </div>

        {/* 主标题 */}
        <h1 className="mt-4 text-2xl font-bold tracking-tight text-white md:text-3xl">
          洞察报告<span className="text-accent-light/60"> · </span>
          <span className="bg-gradient-to-r from-accent-light via-white to-accent-light bg-clip-text text-transparent">
            历史归档
          </span>
        </h1>

        {/* 价值阐述：流水线产出 → 读者吸收 */}
        <div className="mt-2.5 space-y-2 text-pretty md:space-y-2.5">
          <p className="text-sm leading-relaxed text-white/55 md:text-[15px] md:leading-7">
            上游信源经采集、提炼与多维解读后，由主编 Agent 综合为{" "}
            <span className="font-medium text-white/85">结构化洞察报告</span>
            ——不是链接堆砌，而是可直接吸收的判断与脉络。
          </p>
          <p className="text-sm leading-relaxed text-white/55 md:text-[15px] md:leading-7">
            每份日报提供执行摘要、关键事件与风险信号，并配套{" "}
            <span className="text-accent-light/90">交互式看板</span>
            与{" "}
            <span className="text-accent-light/90">Markdown 全文</span>
            ；既可速览当日要点，也能深读复盘、沉淀认知。
          </p>
          <p className="mt-0.5 border-l-2 border-accent-light/60 py-0.5 pl-3.5 text-[15px] font-semibold leading-snug md:pl-4 md:text-base md:leading-relaxed">
            <span className="bg-gradient-to-r from-accent-light via-white to-accent-light bg-clip-text text-transparent">
              少花时间筛信息，多花时间理解与学习
            </span>
          </p>
        </div>

        {/* 归档规模 — 数字集中展示，避免与正文重复 */}
        <div
          className="mt-5 flex flex-wrap items-center gap-x-3 gap-y-1 md:mt-6"
          role="separator"
          aria-label={`归档规模 ${reportCount} 份日报，覆盖 ${totalArticles} 篇文章`}
        >
          <span className="shrink-0 text-[11px] font-semibold uppercase tracking-wider text-white/45">
            归档规模
            <span className="mx-1.5 text-white/25">·</span>
            <span className="tabular-nums text-accent-light/90">{reportCount}</span>
            {" "}份日报
            <span className="mx-1.5 text-white/25">·</span>
            <span className="tabular-nums text-accent-light/90">{totalArticles}</span>
            {" "}篇解读
            {dateRangeLabel && (
              <>
                <span className="mx-1.5 text-white/25">·</span>
                <span className="tabular-nums font-normal normal-case tracking-normal text-white/40">
                  {dateRangeLabel}
                </span>
              </>
            )}
          </span>
          <div className="hidden h-px min-w-[2rem] flex-1 bg-gradient-to-r from-white/12 via-white/6 to-transparent sm:block" />
        </div>

        {/* 单份日报交付物说明 */}
        <div className="mt-4 rounded-xl border border-white/8 bg-white/[0.03] p-4 backdrop-blur md:p-5">
          <p className="text-[11px] font-semibold uppercase tracking-wider text-white/40">
            每份日报包含
          </p>
          <div className="mt-3 grid gap-3 text-[12px] leading-relaxed text-white/50 sm:grid-cols-3">
            <div className="flex items-start gap-2.5">
              <svg
                width="14"
                height="14"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
                className="mt-0.5 shrink-0 text-accent-light/60"
              >
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
                <polyline points="14 2 14 8 20 8" />
                <line x1="16" y1="13" x2="8" y2="13" />
                <line x1="16" y1="17" x2="8" y2="17" />
              </svg>
              <span>主编综述 — 执行摘要串联当日最重要变化与判断</span>
            </div>
            <div className="flex items-start gap-2.5">
              <svg
                width="14"
                height="14"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
                className="mt-0.5 shrink-0 text-accent-light/60"
              >
                <path d="M12 20V10" />
                <path d="M18 20V4" />
                <path d="M6 20v-4" />
              </svg>
              <span>交互看板 — KPI、事件分布、趋势与机会/风险信号</span>
            </div>
            <div className="flex items-start gap-2.5">
              <svg
                width="14"
                height="14"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
                className="mt-0.5 shrink-0 text-accent-light/60"
              >
                <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />
                <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
              </svg>
              <span>完整报告 — Markdown 全文，支持深读与按需检索</span>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}
