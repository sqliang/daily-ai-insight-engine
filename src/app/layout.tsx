import type { Metadata } from "next";
import { NavBar } from "@/components/layout/NavBar";
import { SiteFooter } from "@/components/layout/SiteFooter";
import { BackToTop } from "@/components/layout/BackToTop";
import "./globals.css";

export const metadata: Metadata = {
  title: "Daily AI Insight Engine",
  description: "AI 舆情分析日报系统：结构化抽取、趋势分析与可视化展示。",
  icons: {
    icon: "/icon.svg",
  },
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="zh-CN">
      <body className="flex min-h-screen flex-col">
        <NavBar />
        <div className="flex-1">{children}</div>
        <SiteFooter />
        <BackToTop />
      </body>
    </html>
  );
}
