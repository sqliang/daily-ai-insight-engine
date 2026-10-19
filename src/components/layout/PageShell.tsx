// ============================================================================
// PageShell.tsx — 页面统一内容容器
//
// 提供最大宽度与响应式内边距，并集中挂载 SnapshotNotice：只有当前请求
// 的数据层实际回退到快照时才显示角标，各页面无需分别接入。
// ============================================================================

import type { ReactNode } from "react";

import { SnapshotNotice } from "./SnapshotNotice";

type PageShellProps = {
  children: ReactNode;
};

/** 页面统一内容容器；快照角标位于正文顶部，不改变既有布局宽度 */
export function PageShell({ children }: PageShellProps) {
  return (
    <main className="mx-auto max-w-7xl px-4 py-6 sm:px-6 md:px-8 md:py-8">
      <SnapshotNotice />
      {children}
    </main>
  );
}
