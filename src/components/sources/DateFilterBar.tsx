"use client";

// ============================================================================
// DateFilterBar.tsx — 文章时间范围过滤器
//
// 客户端组件，提供预设时间范围按钮，点击后通过 URL searchParams 切换过滤条件。
// 由 source detail page 渲染在 ArticleList 上方。
// ============================================================================

import { useRouter, useSearchParams } from "next/navigation";
import { useCallback } from "react";

// ---------------------------------------------------------------------------
// 预设类型
// ---------------------------------------------------------------------------

type Preset =
  | "latest"
  | "today"
  | "last3days"
  | "last7days"
  | "all";

const PRESETS: { key: Preset; label: string }[] = [
  { key: "latest", label: "最新" },
  { key: "today", label: "今天" },
  { key: "last3days", label: "最近 3 天" },
  { key: "last7days", label: "最近 7 天" },
  { key: "all", label: "全部" },
];

// ---------------------------------------------------------------------------
// 日期工具
// ---------------------------------------------------------------------------

function todayStr(): string {
  const d = new Date();
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
}

function daysAgoStr(n: number): string {
  const d = new Date();
  d.setDate(d.getDate() - n);
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
}

// ---------------------------------------------------------------------------
// DateFilterBar
// ---------------------------------------------------------------------------

export function DateFilterBar() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const currentFrom = searchParams.get("from");
  const currentTo = searchParams.get("to");

  const resolvePreset = useCallback((key: Preset) => {
    const params = new URLSearchParams(searchParams.toString());

    switch (key) {
      case "latest":
        params.delete("from");
        params.delete("to");
        break;
      case "today":
        params.set("from", todayStr());
        params.set("to", todayStr());
        break;
      case "last3days":
        params.set("from", daysAgoStr(2));
        params.set("to", todayStr());
        break;
      case "last7days":
        params.set("from", daysAgoStr(6));
        params.set("to", todayStr());
        break;
      case "all":
        params.set("from", "2000-01-01");
        params.set("to", todayStr());
        break;
    }

    const qs = params.toString();
    router.push(qs ? `?${qs}` : window.location.pathname, { scroll: false });
  }, [searchParams, router]);

  const activePreset = ((): Preset => {
    if (!currentFrom && !currentTo) return "latest";
    const today = todayStr();
    if (currentFrom === today && currentTo === today) return "today";
    if (currentFrom === daysAgoStr(2) && currentTo === today) return "last3days";
    if (currentFrom === daysAgoStr(6) && currentTo === today) return "last7days";
    if (currentFrom === "2000-01-01") return "all";
    return "latest";
  })();

  return (
    <div className="flex items-center gap-2 mb-6 pb-4 border-b border-line overflow-x-auto">
      {PRESETS.map(({ key, label }) => (
        <button
          key={key}
          type="button"
          onClick={() => resolvePreset(key)}
          className={
            `shrink-0 rounded-full px-4 py-1.5 text-[12px] font-semibold transition-all duration-200 ${
              activePreset === key
                ? "bg-accent text-white shadow-sm"
                : "bg-panel border border-line text-muted hover:text-foreground hover:border-muted"
            }`
          }
        >
          {label}
        </button>
      ))}
    </div>
  );
}
