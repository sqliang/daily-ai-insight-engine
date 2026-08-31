// ============================================================================
// drizzle.config.ts — drizzle-kit 迁移配置
//
// 依据 src/lib/db/schema.ts 生成 SQL 迁移文件到 drizzle/ 目录，
// 并可通过 `pnpm drizzle-kit migrate` 应用到 DATABASE_URL 指向的库。
// ============================================================================

import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  schema: "./src/lib/db/schema.ts",
  out: "./drizzle",
  dbCredentials: {
    url: process.env.DATABASE_URL ?? "",
  },
});
