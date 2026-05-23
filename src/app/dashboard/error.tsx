"use client";

import { useEffect } from "react";

export default function DashboardError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error("Dashboard error boundary caught:", error);
  }, [error]);

  return (
    <main className="mx-auto max-w-7xl px-4 py-6 sm:px-6 md:px-8 md:py-8">
      <div className="rounded-xl border border-line bg-panel p-8 text-center shadow-sm">
        <h2 className="text-lg font-bold text-foreground">仪表板渲染失败</h2>
        <p className="mt-3 max-w-md mx-auto text-sm leading-relaxed text-muted">
          日报数据可能不完整或格式异常，导致仪表板组件渲染失败。请确认数据文件
          <code className="mx-1 rounded bg-muted px-1.5 py-0.5 font-mono text-xs">
            data/05_reports/daily-report.json
          </code>
          结构完整，或重新运行数据管道。
        </p>
        <p className="mt-2 font-mono text-xs text-muted">
          {error.message}
        </p>
        <div className="mt-6 flex justify-center gap-3">
          <button
            onClick={reset}
            className="rounded-lg bg-accent px-4 py-2 text-sm font-medium text-white transition hover:opacity-90"
          >
            重试
          </button>
          <a
            href="/report"
            className="rounded-lg border border-line px-4 py-2 text-sm font-medium text-foreground transition hover:bg-muted"
          >
            查看文字报告
          </a>
        </div>
      </div>
    </main>
  );
}
