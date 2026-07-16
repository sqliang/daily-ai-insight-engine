// ============================================================================
// SpecializedEntries.tsx — 日报卡片专题洞察入口组件
//
// 在 ReportCard 内部渲染轻量专题洞察入口。
// 项目/产品洞察是总洞察报告下的对象化专题分析能力，因此这里只做一行
// 高识别度的次级导航提示，不绑定 GitHub/ProductHunt 等当前数据来源细节。
// Phase 1/2 已恢复 GitHub 和 Product；Paper 仍保持关闭。
// ============================================================================

import Link from "next/link";
import type { SpecializedAvailability } from "@/lib/data/reports";

// ---------------------------------------------------------------------------
// Props
// ---------------------------------------------------------------------------

interface SpecializedEntriesProps {
  specialized: SpecializedAvailability;
  date: string;
}

// ---------------------------------------------------------------------------
// 子条目组件
// ---------------------------------------------------------------------------

interface BriefChipProps {
  label: string;
  href: string;
  tone: "accent" | "warm";
}

function BriefChip({ label, href, tone }: BriefChipProps) {
  const toneClass =
    tone === "warm"
      ? "border-warm/25 bg-warm/8 text-warm hover:border-warm/45 hover:bg-warm/12"
      : "border-accent/25 bg-accent/8 text-accent hover:border-accent/45 hover:bg-accent/12";

  return (
    <Link
      href={href}
      className={`inline-flex items-center gap-1.5 rounded-full border px-2.5 py-1 text-[12px] font-semibold transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-accent ${toneClass}`}
    >
      {label}
      <svg
        className="h-3 w-3 text-current/55"
        viewBox="0 0 16 16"
        fill="none"
        stroke="currentColor"
        strokeWidth="1.7"
        strokeLinecap="round"
        strokeLinejoin="round"
        aria-hidden="true"
      >
        <path d="M3 8h9" />
        <path d="m9 4 4 4-4 4" />
      </svg>
    </Link>
  );
}

// ---------------------------------------------------------------------------
// 主组件
// ---------------------------------------------------------------------------

/**
 * 专题洞察入口。
 *
 * 在日报卡片内用一行 chip 展示该日期可用的对象化专题洞察入口。
 * Phase 1/2 已恢复 GitHub 与 Product；Paper 仍保持关闭。
 */
export function SpecializedEntries({
  specialized,
  date,
}: SpecializedEntriesProps) {
  const chips: Array<{ label: string; href: string; tone: "accent" | "warm" }> = [];

  if (specialized.github) {
    chips.push({
      label: "项目洞察",
      href: `/specialized/github/${date}`,
      tone: "accent",
    });
  }

  if (specialized.product) {
    chips.push({
      label: "产品洞察",
      href: `/specialized/product/${date}`,
      tone: "warm",
    });
  }

  // Paper 专题入口保持关闭：仅当未来真正恢复数据和产品策略时再展示。
  if (chips.length === 0) {
    return null;
  }

  return (
    <div
      className="mt-3 flex flex-wrap items-center gap-2 text-xs"
      aria-label="专题洞察入口"
    >
      <span className="inline-flex items-center gap-1.5 pr-0.5 font-semibold text-foreground/65">
        <span
          className="h-3.5 w-0.5 rounded-full bg-gradient-to-b from-accent to-warm"
          aria-hidden="true"
        />
        专题洞察
      </span>
      <span className="h-3 w-px bg-line/80" aria-hidden="true" />
      {chips.map((chip) => (
        <BriefChip
          key={chip.href}
          label={chip.label}
          href={chip.href}
          tone={chip.tone}
        />
      ))}
    </div>
  );
}
