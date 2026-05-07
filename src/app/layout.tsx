import type { Metadata } from "next";
import { NavBar } from "@/components/layout/NavBar";
import "./globals.css";

export const metadata: Metadata = {
  title: "Daily AI Insight Engine",
  description: "AI 舆情分析日报系统：结构化抽取、趋势分析与可视化展示。",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="zh-CN">
      <body className="min-h-screen flex flex-col">
        <NavBar />
        {children}
      </body>
    </html>
  );
}
