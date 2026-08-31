// ============================================================================
// client.ts — Drizzle 数据库客户端（postgres.js 驱动）
//
// 惰性初始化：模块加载不建立连接，首次查询时才读取 DATABASE_URL 建连。
// 这样 build 阶段（force-dynamic 页面不会真正执行查询）无需数据库可达。
// postgres.js 单一驱动同时覆盖本地 Docker PG 与 Neon（-pooler + sslmode）。
//
// 消费方：src/lib/data/ 下各数据访问模块（reports / manifests /
// structured-data / specialized）。
// ============================================================================

import { drizzle, type PostgresJsDatabase } from "drizzle-orm/postgres-js";
import postgres from "postgres";

import * as schema from "./schema";

// ---------------------------------------------------------------------------
// 惰性单例
// ---------------------------------------------------------------------------

let _db: PostgresJsDatabase<typeof schema> | null = null;

/**
 * 获取 Drizzle 客户端（进程级单例）。
 *
 * 首次调用时读取 process.env.DATABASE_URL 建立连接池；
 * 未配置时抛出带指引的错误（数据层调用方应视为运行时故障）。
 *
 * 返回：
 *   PostgresJsDatabase 实例（schema 感知）
 *
 * 异常：
 *   Error: DATABASE_URL 未配置
 */
export function getDb(): PostgresJsDatabase<typeof schema> {
  if (_db) return _db;

  const url = process.env.DATABASE_URL;
  if (!url) {
    throw new Error(
      "DATABASE_URL 未配置：本地开发请在 .env 中指向 docker compose 的 PostgreSQL，" +
        "生产环境在 Vercel 环境变量中配置 Neon 连接串",
    );
  }

  // prepare: false — 兼容 Neon pooler（pgBouncer 事务模式不支持 prepared statements）
  const client = postgres(url, { prepare: false });
  _db = drizzle(client, { schema });
  return _db;
}
