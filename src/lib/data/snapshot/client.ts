// ============================================================================
// snapshot/client.ts — data/snapshot 快照的本地 / 远程读取客户端
//
// 快照由 pipeline 的 `snapshot` 命令生成，目录契约与 GitHub data-snapshot
// orphan 分支一致。读取顺序固定为：
//   本地 data/snapshot/<relPath> → 远程 raw.githubusercontent.com 分支文件。
// 本地文件不存在、远程 404、网络失败均返回 null，不向页面抛传输层异常。
//
// DATA_SNAPSHOT_BASE_URL 可覆盖远程基址（主要用于验证与私有镜像），
// 缺省使用项目公开的 data-snapshot 分支。
// ============================================================================

import { readFile } from "node:fs/promises";
import path from "node:path";

import { cache } from "react";
import { z } from "zod";

const DEFAULT_SNAPSHOT_BASE_URL =
  "https://raw.githubusercontent.com/sqliang/daily-ai-insight-engine/data-snapshot/";

const SNAPSHOT_LOCAL_ROOT = path.join(process.cwd(), "data", "snapshot");

const snapshotIndexSchema = z.object({
  /** 快照生成时间（ISO8601），用于页面离线数据角标 */
  generated_at: z.string(),
  /** 快照包含的日报日期，降序 */
  report_dates: z.array(z.string()).default([]),
  /** 快照包含的 source 名称，字母序 */
  sources: z.array(z.string()).default([]),
});

export type SnapshotIndex = z.infer<typeof snapshotIndexSchema>;

/** 规范化 relPath，拒绝越出快照目录的路径（所有调用方均使用内部固定路径） */
function normalizeRelativePath(relPath: string): string | null {
  if (!relPath || path.isAbsolute(relPath)) return null;
  const normalized = path.posix.normalize(relPath);
  if (normalized === ".." || normalized.startsWith("../")) return null;
  return normalized;
}

/** 远程基址统一保留末尾斜杠，避免拼接时丢失分支目录 */
function getRemoteBaseUrl(): string {
  const base = process.env.DATA_SNAPSHOT_BASE_URL ?? DEFAULT_SNAPSHOT_BASE_URL;
  return base.endsWith("/") ? base : `${base}/`;
}

/**
 * 读取快照中的单个文本文件。
 *
 * 优先读取本地文件；本地读取失败后访问远程 raw 分支。远程响应通过
 * Next.js fetch 缓存 1 小时，避免同一次构建/多个页面重复下载相同文件。
 *
 * 返回：
 *   文件文本；本地与远程均不可用时返回 null（不抛出 404/网络错误）
 */
export async function readSnapshotFile(
  relPath: string,
): Promise<string | null> {
  const normalized = normalizeRelativePath(relPath);
  if (!normalized) return null;

  try {
    return await readFile(path.join(SNAPSHOT_LOCAL_ROOT, normalized), "utf8");
  } catch {
    // 本地快照未生成或文件不存在时继续尝试远程分支
  }

  try {
    const response = await fetch(`${getRemoteBaseUrl()}${normalized}`, {
      next: { revalidate: 3600 },
    });
    if (!response.ok) return null;
    return await response.text();
  } catch {
    return null;
  }
}

/**
 * 读取并解析快照 JSON 文件。
 *
 * 返回：
 *   解析后的 JSON 值；文件不可用或 JSON 损坏时返回 null
 */
export async function readSnapshotJson(relPath: string): Promise<unknown> {
  const text = await readSnapshotFile(relPath);
  if (text === null) return null;
  try {
    return JSON.parse(text) as unknown;
  } catch {
    return null;
  }
}

/**
 * 读取快照索引。React cache() 保证同一请求只读取一次。
 *
 * index.json 同时承担"快照整体是否可用"的判据：具体文件缺失但索引可读时，
 * 视为正常的空数据/热窗口缺失；索引也不可用时才认定快照整体不可用。
 */
export const getSnapshotIndex = cache(
  async (): Promise<SnapshotIndex | null> => {
    const raw = await readSnapshotJson("index.json");
    try {
      return snapshotIndexSchema.parse(raw);
    } catch {
      return null;
    }
  },
);

/**
 * 确认快照整体可用；索引不可读时抛出，供 withDbFallback 判定是否继续
 * 向页面传播原始 DB 错误。具体文件缺失不应调用本函数以外的额外报错逻辑。
 */
export async function assertSnapshotAvailable(): Promise<void> {
  const index = await getSnapshotIndex();
  if (!index) {
    throw new Error("本地与远程数据快照均不可用");
  }
}
