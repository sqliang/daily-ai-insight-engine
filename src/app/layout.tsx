import type { Metadata } from "next";
import "./globals.css";

// ============================================================================
// layout.tsx — Next.js App Router 根布局
//
// 所有页面的外层容器。在此处设置：
//   - HTML lang 属性（zh-CN，面向中文用户）
//   - 全局 metadata（页面标题 & 描述，用于 SEO 和社交分享）
//   - 全局样式导入（globals.css → Tailwind + 设计 Token）
//
// 本文件在整个应用的生命周期中只渲染一次（服务端组件）。
// ============================================================================

export const metadata: Metadata = {
  title: "Daily AI Insight Engine",
  description: "AI 舆情分析日报系统：结构化抽取、趋势分析与可视化展示。",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="zh-CN">
      <body>{children}</body>
    </html>
  );
}
