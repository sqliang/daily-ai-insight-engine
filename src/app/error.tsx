"use client";

import { useEffect } from "react";

export default function RootError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error("Root error boundary caught:", error);
  }, [error]);

  return (
    <div className="flex min-h-screen flex-col items-center justify-center px-4 text-center">
      <h1 className="text-xl font-bold text-foreground">页面发生错误</h1>
      <p className="mt-3 max-w-md text-sm leading-relaxed text-muted">
        抱歉，页面渲染时遇到了意外问题。请尝试重试，或返回首页。
      </p>
      <p className="mt-2 max-w-md rounded-md bg-muted px-3 py-1.5 font-mono text-xs text-muted">
        {error.message || "未知错误"}
      </p>
      <div className="mt-6 flex gap-3">
        <button
          onClick={reset}
          className="rounded-lg bg-accent px-4 py-2 text-sm font-medium text-white transition hover:opacity-90"
        >
          重试
        </button>
        <a
          href="/"
          className="rounded-lg border border-line px-4 py-2 text-sm font-medium text-foreground transition hover:bg-muted"
        >
          返回首页
        </a>
      </div>
    </div>
  );
}
