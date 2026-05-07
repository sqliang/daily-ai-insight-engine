import type { NextConfig } from "next";

// ============================================================================
// next.config.ts — Next.js 构建配置
//
// output: "standalone" 启用独立构建模式，生成的 .next/standalone 目录
// 包含运行应用所需的全部文件（不含 node_modules），适用于 Docker 部署
// 和 Vercel 等平台的无服务器运行环境。
// ============================================================================

const nextConfig: NextConfig = {
  output: "standalone",
};

export default nextConfig;
