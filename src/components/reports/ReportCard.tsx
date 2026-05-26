// ============================================================================
// ReportCard.tsx — 日报卡片组件
//
// 在 /dashboard 日报列表中使用，以横向全宽卡片展示单份日报的关键信息：
// 日期、周几、标题、执行摘要（长截断）、文章数、信源数、语言覆盖。
// 点击后跳转到 /dashboard/[date] 可视化仪表盘。
// ============================================================================

"use client";

import Link from "next/link";

import type { ReportSummary } from "@/lib/data/reports";

/** 执行摘要截断长度（字符数）— 横向布局可展示更多文字 */
const SUMMARY_TRUNCATE = 200;

/** 将 YYYY-MM-DD 日期转换为中文周几 */
function weekdayLabel(dateStr: string): string {
  const weekdays = ["周日", "周一", "周二", "周三", "周四", "周五", "周六"];
  const d = new Date(dateStr + "T00:00:00");
  if (isNaN(d.getTime())) return "";
  return weekdays[d.getDay()];
}

/**
 * 日报横向卡片 — 全宽展示单份日报摘要。
 *
 * 左侧为日期区块，中间为标题和摘要，右侧为统计数据。
 * hover 时整体微上浮并显示阴影。
 */
export function ReportCard({ report }: { report: ReportSummary }) {
  const truncated =
    report.executiveSummary.length > SUMMARY_TRUNCATE
      ? report.executiveSummary.slice(0, SUMMARY_TRUNCATE) + "…"
      : report.executiveSummary;

  const weekday = weekdayLabel(report.date);
  // 从日期中提取月日部分（如 "05-26"）
  const monthDay = report.date.slice(5);

  return (
    <Link
      href={`/dashboard/${report.date}`}
      className="group flex flex-col gap-4 rounded-xl border border-line/50 bg-card p-6 transition-all duration-200 hover:-translate-y-0.5 hover:border-line hover:shadow-lg hover:shadow-accent/5 sm:flex-row sm:gap-6"
    >
      {/* 左侧：日期区块 */}
      <div className="flex shrink-0 flex-row items-center gap-3 sm:w-28 sm:flex-col sm:items-center sm:justify-center sm:border-r sm:border-line/30 sm:pr-4">
        {/* 月-日 */}
        <time
          dateTime={report.date}
          className="text-2xl font-bold tracking-tight text-foreground sm:text-3xl"
        >
          {monthDay}
        </time>
        {/* 周几 + 年份 */}
        <div className="flex flex-col items-start sm:items-center">
          {weekday && (
            <span className="text-xs font-medium text-accent">{weekday}</span>
          )}
          <span className="text-[11px] text-muted/50">{report.date.slice(0, 4)}</span>
        </div>
      </div>

      {/* 中间：标题 + 摘要 + 元数据 */}
      <div className="flex min-w-0 flex-1 flex-col justify-center">
        {/* 报告标题 */}
        <h3 className="text-[16px] font-semibold leading-snug text-foreground group-hover:text-accent transition-colors">
          {report.reportTitle}
        </h3>

        {/* 执行摘要（长截断） */}
        <p className="mt-2 text-sm leading-relaxed text-muted/75">
          {truncated}
        </p>

        {/* 底部：文章数 + 信源数 + 语言 */}
        <div className="mt-3 flex flex-wrap items-center gap-2">
          <span className="inline-flex items-center rounded-full bg-accent/10 px-2.5 py-0.5 text-xs font-medium text-accent">
            {report.totalArticles} 篇文章
          </span>
          <span className="inline-flex items-center gap-1 text-xs text-muted/50">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
              <path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z" />
              <line x1="4" y1="22" x2="4" y2="15" />
            </svg>
            {report.sourceCount} 个信源
          </span>
          {report.languages.length > 0 && (
            <span className="inline-flex items-center gap-1 text-xs text-muted/50">
              <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
                <circle cx="12" cy="12" r="10" />
                <line x1="2" y1="12" x2="22" y2="12" />
                <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
              </svg>
              {report.languages.join(" / ")}
            </span>
          )}
        </div>
      </div>

      {/* 右侧：箭头指示 */}
      <div className="flex shrink-0 items-center self-end sm:self-center">
        <svg
          width="18"
          height="18"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
          className="text-muted/30 transition-all duration-200 group-hover:translate-x-1 group-hover:text-accent"
        >
          <path d="M5 12h14" />
          <path d="m12 5 7 7-7 7" />
        </svg>
      </div>
    </Link>
  );
}
