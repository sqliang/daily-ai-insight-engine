// ============================================================================
// src/components/reports/SpecializedReportHero.tsx — 专题详情页统一 Hero 横幅
//
// 被 /specialized/github/[date]、/specialized/product/[date] 等专题详情页消费。
// 视觉语言与 SourcesHero / DashboardHero 保持一致：深色渐变、几何装饰、
// 轻量面包屑、分区标题与玻璃态统计说明。
//
// 组件职责：
//   - 提供专题页顶部的一致性视觉入口
//   - 展示关键统计（如项目数、领域分布、覆盖信源）
//   - 通过 breadcrumb 返回对应日期的日报仪表盘
// ============================================================================

import Link from "next/link";
import type { ReactNode } from "react";

type HeroStat = {
  /** 统计项标签 */
  label: string;
  /** 统计项值 */
  value: string;
};

type SpecializedReportHeroProps = {
  /** 返回日报页的日期，用于构造 breadcrumb href */
  date: string;
  /** Hero 主标题 */
  title: string;
  /** 英文专题标签 */
  eyebrow: string;
  /** 中文摘要说明 */
  summary?: string;
  /** 右侧或底部展示的关键统计 */
  stats: HeroStat[];
  /** 额外分布标签内容 */
  children?: ReactNode;
};

/**
 * 专题详情页 Hero。
 *
 * 与洞察报告 / 数据源页面使用同一组背景、装饰和文字层级，
 * 避免专题详情页产生独立子站感。
 */
export function SpecializedReportHero({
  date,
  title,
  eyebrow,
  summary,
  stats,
  children,
}: SpecializedReportHeroProps) {
  return (
    <header className="relative overflow-hidden rounded-2xl bg-gradient-to-br from-foreground via-foreground to-accent-dark p-6 shadow-lg md:p-10">
      <svg
        className="pointer-events-none absolute inset-0 h-full w-full"
        aria-hidden="true"
        viewBox="0 0 1200 360"
        preserveAspectRatio="none"
      >
        <circle cx="1050" cy="50" r="150" fill="oklch(0.55 0.13 200 / 0.10)" />
        <circle cx="1080" cy="30" r="80" fill="oklch(0.55 0.13 200 / 0.08)" />
        <circle cx="80" cy="300" r="110" fill="oklch(0.45 0.16 340 / 0.08)" />
        <circle cx="50" cy="320" r="60" fill="oklch(0.45 0.16 340 / 0.06)" />
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
          y1="330"
          x2="380"
          y2="330"
          stroke="oklch(0.55 0.13 200 / 0.20)"
          strokeWidth="0.5"
          strokeDasharray="4 6"
        />
      </svg>

      <div className="relative">
        <Link
          href={`/dashboard/${date}`}
          className="mb-5 inline-flex items-center gap-1.5 text-[12px] font-medium text-white/50 transition-colors duration-200 hover:text-accent-light focus:outline-none focus-visible:ring-2 focus-visible:ring-accent-light"
        >
          <svg
            className="h-3.5 w-3.5"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            aria-hidden="true"
          >
            <path d="m15 18-6-6 6-6" />
          </svg>
          回到日报
        </Link>

        <div className="flex items-center gap-2.5">
          <span className="relative flex h-2.5 w-2.5">
            <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-accent opacity-60" />
            <span className="relative inline-flex h-2.5 w-2.5 rounded-full bg-accent" />
          </span>
          <p className="text-[11px] font-medium uppercase tracking-[0.25em] text-accent-light/90">
            {eyebrow}
          </p>
        </div>

        <h1 className="mt-4 text-2xl font-bold tracking-tight text-white md:text-3xl">
          专题报告<span className="text-accent-light/60"> · </span>
          <span className="bg-gradient-to-r from-accent-light via-white to-accent-light bg-clip-text text-transparent">
            {title}
          </span>
        </h1>

        {summary && (
          <p className="mt-3 max-w-7xl text-sm leading-relaxed text-white/55 md:text-[15px] md:leading-7">
            {summary}
          </p>
        )}

        <div className="mt-5 flex flex-wrap items-center gap-x-3 gap-y-1 md:mt-6">
          <span className="shrink-0 text-[11px] font-semibold uppercase tracking-wider text-white/45">
            专题规模
            <span className="mx-1.5 text-white/25">·</span>
            <span className="tabular-nums text-accent-light/90">{date}</span>
            {stats.map((stat) => (
              <span key={stat.label}>
                <span className="mx-1.5 text-white/25">·</span>
                <span className="tabular-nums text-accent-light/90">{stat.value}</span>
                {" "}{stat.label}
              </span>
            ))}
          </span>
          <div className="hidden h-px min-w-[2rem] flex-1 bg-gradient-to-r from-white/12 via-white/6 to-transparent sm:block" />
        </div>

        {children && (
          <div className="mt-4 rounded-xl border border-white/8 bg-white/[0.03] p-4 backdrop-blur md:p-5">
            {children}
          </div>
        )}
      </div>
    </header>
  );
}
