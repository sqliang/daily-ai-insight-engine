"use client";

// ============================================================================
// Pagination.tsx — 通用分页组件
//
// 客户端组件，通过 URL searchParams 驱动翻页（与 DateFilterBar、排序开关
// 同一模式）：保留当前全部查询参数，仅改写 page；page=1 时删除该参数以
// 保持 URL 干净。适用于所有服务端切片分页的列表页：
//   - /sources/[name] 文章列表（anchorId="article-list"）
//   - /dashboard 日报卡片列表（anchorId="report-list"）
// 设计理由：项目无 API 层，页面为 force-dynamic 服务端组件，翻页状态放在
// URL 中可分享、可后退，且与日期筛选、排序参数正交组合。
// ============================================================================

import { useRouter, useSearchParams } from "next/navigation";
import { useCallback } from "react";

// ---------------------------------------------------------------------------
// Props
// ---------------------------------------------------------------------------

type PaginationProps = {
  /** 当前页码（1-based，数据层已 clamp） */
  currentPage: number;
  /** 总页数；<= 1 时组件不渲染 */
  totalPages: number;
  /** 切片前的总条数，用于 "共 n 条" 展示 */
  totalItems: number;
  /**
   * 翻页后滚动定位的锚点元素 id（通常是列表容器）。
   * 缺省时保持滚动位置不变（scroll: false）。
   */
  anchorId?: string;
};

// ---------------------------------------------------------------------------
// 页码窗口算法
// ---------------------------------------------------------------------------

/** 页码窗口项：数字为可点击页码，"ellipsis" 为省略号占位 */
type PageWindowItem = number | "ellipsis";

/**
 * 计算页码窗口：总页数 <= 7 时全量展示；否则展示
 * `1 … c-1 c c+1 … N`（首尾页 + 当前页邻域），省略号折叠中段。
 */
function buildPageWindow(current: number, total: number): PageWindowItem[] {
  if (total <= 7) {
    return Array.from({ length: total }, (_, i) => i + 1);
  }
  const candidates = [1, current - 1, current, current + 1, total].filter(
    (p) => p >= 1 && p <= total,
  );
  const unique = [...new Set(candidates)].sort((a, b) => a - b);
  const items: PageWindowItem[] = [];
  let prev = 0;
  for (const p of unique) {
    if (p - prev > 1) items.push("ellipsis");
    items.push(p);
    prev = p;
  }
  return items;
}

// ---------------------------------------------------------------------------
// Pagination
// ---------------------------------------------------------------------------

/**
 * 通用分页条：上一页 / 页码窗口 / 下一页 + "第 x / y 页 · 共 n 条"。
 *
 * 翻页通过 router.push 改写 URL 的 page 参数完成，服务端重新渲染并返回
 * 对应页切片；传入 anchorId 时翻页后平滑滚动回列表顶部。
 */
export function Pagination({
  currentPage,
  totalPages,
  totalItems,
  anchorId,
}: PaginationProps) {
  const router = useRouter();
  const searchParams = useSearchParams();

  const goToPage = useCallback(
    (page: number) => {
      const params = new URLSearchParams(searchParams.toString());
      // page=1 为默认态，从 URL 中移除以保持链接干净
      if (page <= 1) {
        params.delete("page");
      } else {
        params.set("page", String(page));
      }
      const qs = params.toString();
      // scroll: false —— 滚动交由 anchorId 定位处理，避免先跳页面顶部再跳列表的闪烁
      router.push(qs ? `?${qs}` : window.location.pathname, { scroll: false });
      if (anchorId) {
        document
          .getElementById(anchorId)
          ?.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    },
    [searchParams, router, anchorId],
  );

  if (totalPages <= 1) return null;

  const windowItems = buildPageWindow(currentPage, totalPages);
  const isFirst = currentPage <= 1;
  const isLast = currentPage >= totalPages;

  const pageButtonClass = (active: boolean) =>
    `inline-flex h-8 min-w-8 items-center justify-center rounded-lg px-2 text-[12px] font-semibold tabular-nums transition-all duration-200 ${
      active
        ? "bg-accent text-white shadow-sm"
        : "border border-line bg-panel text-muted hover:border-muted hover:text-foreground"
    }`;

  const navButtonClass = (disabled: boolean) =>
    `inline-flex h-8 items-center gap-1 rounded-lg px-3 text-[12px] font-semibold transition-all duration-200 ${
      disabled
        ? "cursor-not-allowed border border-line bg-panel/50 text-muted/40"
        : "border border-line bg-panel text-muted hover:border-muted hover:text-foreground"
    }`;

  return (
    <nav
      aria-label="分页"
      className="mt-8 flex flex-wrap items-center justify-between gap-x-4 gap-y-3 border-t border-line pt-5"
    >
      {/* 左侧：位置与总量信息 */}
      <p className="text-[12px] text-muted/70 tabular-nums">
        第 <span className="font-semibold text-foreground">{currentPage}</span>
        {" / "}
        {totalPages} 页
        <span className="mx-1.5 text-muted/30">·</span>共 {totalItems} 条
      </p>

      {/* 右侧：翻页控件 */}
      <div className="flex items-center gap-1.5">
        <button
          type="button"
          onClick={() => goToPage(currentPage - 1)}
          disabled={isFirst}
          aria-label="上一页"
          className={navButtonClass(isFirst)}
        >
          <svg
            width="12"
            height="12"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            aria-hidden="true"
          >
            <polyline points="15 18 9 12 15 6" />
          </svg>
          上一页
        </button>

        {windowItems.map((item, idx) =>
          item === "ellipsis" ? (
            <span
              key={`ellipsis-${idx}`}
              className="inline-flex h-8 min-w-6 items-center justify-center text-[12px] text-muted/40"
              aria-hidden="true"
            >
              …
            </span>
          ) : (
            <button
              key={item}
              type="button"
              onClick={() => goToPage(item)}
              aria-label={`第 ${item} 页`}
              aria-current={item === currentPage ? "page" : undefined}
              className={pageButtonClass(item === currentPage)}
            >
              {item}
            </button>
          ),
        )}

        <button
          type="button"
          onClick={() => goToPage(currentPage + 1)}
          disabled={isLast}
          aria-label="下一页"
          className={navButtonClass(isLast)}
        >
          下一页
          <svg
            width="12"
            height="12"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            aria-hidden="true"
          >
            <polyline points="9 18 15 12 9 6" />
          </svg>
        </button>
      </div>
    </nav>
  );
}
