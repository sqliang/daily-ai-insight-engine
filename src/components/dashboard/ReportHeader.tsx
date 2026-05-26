// ============================================================================
// ReportHeader.tsx — 单份日报的上下文 Banner（仪表盘 / 全文页共用）
//
// 展示标题、日期、生成时间与可选执行摘要；非列表页营销 Hero。
// 被 DashboardContent、report/[date]/page.tsx 消费。
// ============================================================================

import Link from "next/link";
import type { DailyReport } from "@/lib/agent/schema";
import { formatGeneratedAt } from "@/lib/utils/date";

type ReportHeaderProps = {
  report: Pick<DailyReport, "reportTitle" | "date" | "generatedAt" | "executiveSummary">;
  /** 返回链接的 href（可选，不传则不显示面包屑） */
  backHref?: string;
  /** 返回链接的文本 */
  backLabel?: string;
  /** 右上角主操作按钮链接，默认跳转 Markdown 完整报告 */
  actionHref?: string;
  /** 右上角主操作按钮文案 */
  actionLabel?: string;
  /** 是否展示执行摘要玻璃面板；全文页正文已含摘要时可关闭以避免重复 */
  showExecutiveSummary?: boolean;
};

export function ReportHeader({
  report,
  backHref,
  backLabel,
  actionHref,
  actionLabel = "完整报告",
  showExecutiveSummary = true,
}: ReportHeaderProps) {
  const primaryActionHref = actionHref ?? `/report/${report.date}`;
  return (
    <header className="relative overflow-hidden rounded-2xl bg-gradient-to-br from-foreground via-foreground to-accent-dark p-6 shadow-lg md:p-10">
      {/* Decorative geometric shapes */}
      <svg
        className="pointer-events-none absolute inset-0 h-full w-full"
        aria-hidden="true"
        viewBox="0 0 1200 400"
        preserveAspectRatio="none"
      >
        {/* Large blurred circle — top right */}
        <circle
          cx="1050"
          cy="60"
          r="180"
          fill="oklch(0.55 0.13 200 / 0.12)"
        />
        <circle
          cx="1080"
          cy="40"
          r="100"
          fill="oklch(0.55 0.13 200 / 0.10)"
        />
        {/* Medium circle — bottom left */}
        <circle
          cx="80"
          cy="340"
          r="140"
          fill="oklch(0.45 0.16 340 / 0.10)"
        />
        <circle
          cx="50"
          cy="360"
          r="80"
          fill="oklch(0.45 0.16 340 / 0.08)"
        />
        {/* Small dot grid — top left area */}
        {Array.from({ length: 6 }).flatMap((_, row) =>
          Array.from({ length: 6 }).map((_, col) => (
            <circle
              key={`${row}-${col}`}
              cx={40 + col * 24}
              cy={30 + row * 24}
              r="1.2"
              fill="oklch(1 0 0 / 0.18)"
            />
          )),
        )}
        {/* Accent line — bottom decorative */}
        <line
          x1="36"
          y1="370"
          x2="400"
          y2="370"
          stroke="oklch(0.55 0.13 200 / 0.25)"
          strokeWidth="0.5"
          strokeDasharray="4 6"
        />
      </svg>

      <div className="relative">
        {/* 面包屑导航 — 位于 banner 内部左上角，与 /sources/[name] 保持一致 */}
        {backHref && backLabel && (
          <Link
            href={backHref}
            className="mb-5 inline-flex items-center gap-1.5 text-[12px] font-medium text-white/50
                       hover:text-accent-light transition-colors duration-200"
          >
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"
              strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <polyline points="15 18 9 12 15 6" />
            </svg>
            {backLabel}
          </Link>
        )}

        {/* Brand label */}
        <div className="flex items-center gap-2.5">
          <span className="relative flex h-2.5 w-2.5">
            <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-accent opacity-60" />
            <span className="relative inline-flex h-2.5 w-2.5 rounded-full bg-accent" />
          </span>
          <p className="text-[11px] font-medium uppercase tracking-[0.25em] text-accent-light/90">
            Daily AI Insight Engine
          </p>
        </div>

        {/* Title */}
        <h1 className="mt-4 max-w-4xl bg-gradient-to-r from-white via-white to-accent-light bg-clip-text text-3xl font-bold leading-tight tracking-tight text-transparent md:text-4xl lg:text-5xl">
          {report.reportTitle}
        </h1>

        {/* Metadata row */}
        <div className="mt-5 flex flex-wrap items-center justify-between gap-3">
          <div className="flex flex-wrap items-center gap-3">
            <span className="inline-flex items-center gap-1.5 rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs font-medium text-white/70 backdrop-blur">
              <svg
                width="12"
                height="12"
                viewBox="0 0 16 16"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.5"
                className="text-accent-light"
              >
                <rect x="2" y="3" width="12" height="11" rx="2" />
                <path d="M2 7h12M5 2v3m6-3v3" strokeLinecap="round" />
              </svg>
              {report.date}
            </span>
            <span className="inline-flex items-center gap-1.5 rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs font-medium text-white/50 backdrop-blur">
              <svg
                width="12"
                height="12"
                viewBox="0 0 16 16"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.5"
              >
                <circle cx="8" cy="8" r="6.5" />
                <path d="M8 4.5V8l3 2" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
              {formatGeneratedAt(report.generatedAt)}
            </span>
          </div>
          <Link
            href={primaryActionHref}
            className="inline-flex items-center rounded-full bg-accent px-4 py-1.5 text-xs font-semibold text-white shadow-glow transition-all duration-200 hover:bg-accent-dark"
          >
            {actionLabel}
          </Link>
        </div>

        {/* Executive summary — 仪表盘预览用；全文页由 Markdown 承载 */}
        {showExecutiveSummary && (
          <div className="mt-6 rounded-xl border border-white/8 bg-white/[0.04] p-4 backdrop-blur md:p-5">
            <p className="text-sm leading-7 text-white/75 md:text-base md:leading-8">
              {report.executiveSummary}
            </p>
          </div>
        )}
      </div>
    </header>
  );
}
