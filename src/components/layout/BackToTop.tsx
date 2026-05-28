"use client";

// ============================================================================
// BackToTop.tsx — 回到顶部浮动按钮
//
// 页面滚动超过 300px 后淡入，固定在右下角。点击平滑滚动回顶部。
// 滚动恢复后自动淡出。挂载于 RootLayout，全站可用。
// ============================================================================

import { useEffect, useState, useCallback } from "react";

const THRESHOLD = 300;

export function BackToTop() {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    let ticking = false;

    const onScroll = () => {
      if (!ticking) {
        requestAnimationFrame(() => {
          setVisible(window.scrollY > THRESHOLD);
          ticking = false;
        });
        ticking = true;
      }
    };

    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  const scrollToTop = useCallback(() => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  }, []);

  return (
    <button
      type="button"
      aria-label="回到顶部"
      onClick={scrollToTop}
      className={`fixed bottom-6 right-6 z-50 flex h-10 w-10 items-center justify-center rounded-full border border-line bg-background/80 shadow-md backdrop-blur transition-all duration-300 hover:shadow-lg hover:border-accent-light/40 hover:bg-surface ${
        visible
          ? "pointer-events-auto translate-y-0 opacity-100"
          : "pointer-events-none translate-y-4 opacity-0"
      }`}
      tabIndex={visible ? 0 : -1}
    >
      <svg
        width="18"
        height="18"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
        className="text-accent transition-transform duration-200 group-hover:scale-110"
      >
        <polyline points="18 15 12 9 6 15" />
      </svg>
    </button>
  );
}
