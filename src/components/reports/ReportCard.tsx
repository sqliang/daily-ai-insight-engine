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
import { SpecializedEntries } from "./SpecializedEntries";

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
 * 左侧为日期区块，中间为标题和摘要，右侧为进入日报的箭头。
 * 用顶部光带和日期板强化卡片识别度，hover 时整体微上浮并显示阴影。
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
    <div
      className="group relative overflow-hidden rounded-2xl border border-line/70 p-0 shadow-sm transition-all duration-300 hover:-translate-y-0.5 hover:border-accent/30 hover:shadow-lg hover:shadow-accent/10"
      style={{
        background:
          "linear-gradient(135deg, color-mix(in oklch, var(--accent) 10%, var(--panel)) 0%, var(--panel) 38%, color-mix(in oklch, var(--warm) 5%, var(--panel)) 74%, color-mix(in oklch, var(--cool) 6%, var(--panel)) 100%)",
      }}
    >
      <div
        className="pointer-events-none absolute inset-x-0 top-0 h-1"
        style={{
          background:
            "linear-gradient(90deg, var(--accent), color-mix(in oklch, var(--warm) 80%, var(--accent)), var(--cool))",
        }}
      />

      <div className="relative flex flex-col gap-0 sm:flex-row">
        {/* 左侧：日期区块 */}
        <Link
          href={`/dashboard/${report.date}`}
          className="flex shrink-0 flex-row items-center gap-3 border-b border-accent/12 px-5 py-5 sm:w-36 sm:flex-col sm:items-center sm:justify-center sm:border-b-0 sm:border-r sm:px-4"
          style={{
            background:
              "linear-gradient(180deg, color-mix(in oklch, var(--accent) 12%, transparent), color-mix(in oklch, var(--accent) 4%, transparent))",
          }}
        >
          {/* 月-日 */}
          <time
            dateTime={report.date}
            className="whitespace-nowrap text-3xl font-black tracking-tight text-foreground sm:text-4xl"
          >
            {monthDay}
          </time>
          {/* 周几 + 年份 */}
          <div className="flex flex-col items-start sm:items-center">
            {weekday && (
              <span className="rounded-full bg-accent/10 px-2 py-0.5 text-xs font-bold text-accent">
                {weekday}
              </span>
            )}
            <span className="mt-1 text-[11px] font-medium text-muted/50">
              {report.date.slice(0, 4)}
            </span>
          </div>
        </Link>

        {/* 中间：标题 + 摘要 + 元数据 + 简报入口 */}
        <div className="flex min-w-0 flex-1 flex-col justify-center px-5 py-5 sm:px-6">
          {/* 宏观日报区域 — 点击跳转 /dashboard/[date] */}
          <Link href={`/dashboard/${report.date}`} className="block">
            {/* 报告标题 */}
            <h3 className="text-[17px] font-bold leading-snug text-foreground transition-colors group-hover:text-accent">
              {report.reportTitle}
            </h3>

            {/* 执行摘要（长截断） */}
            <p className="mt-2 text-sm leading-relaxed text-foreground/70 transition-colors group-hover:text-foreground/78">
              {truncated}
            </p>

            {/* 底部：文章数 + 信源数 + 语言 */}
            <div className="mt-3 flex flex-wrap items-center gap-2">
              <span className="inline-flex items-center rounded-full bg-accent/10 px-2.5 py-0.5 text-xs font-bold text-accent ring-1 ring-accent/10">
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
          </Link>

          {/* 专题洞察入口：总洞察报告下的轻量二级操作 */}
          <SpecializedEntries
            specialized={report.specialized}
            date={report.date}
          />
        </div>

        {/* 右侧：箭头指示 — 指向日报仪表盘 */}
        <Link
          href={`/dashboard/${report.date}`}
          className="flex shrink-0 items-center self-end px-5 pb-5 sm:self-stretch sm:px-5 sm:pb-0"
        >
          <span className="inline-flex h-10 w-10 items-center justify-center rounded-full border border-line/60 bg-panel/70 text-muted/35 shadow-sm transition-all duration-200 group-hover:border-accent/30 group-hover:bg-accent/8 group-hover:text-accent">
            <svg
              width="18"
              height="18"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
              className="transition-transform duration-200 group-hover:translate-x-0.5"
            >
              <path d="M5 12h14" />
              <path d="m12 5 7 7-7 7" />
            </svg>
          </span>
        </Link>
      </div>
    </div>
  );
}
