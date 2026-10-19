// ============================================================================
// snapshot/client.ts — data/snapshot 快照的本地 / 远程读取客户端
//
// 读取顺序：本地 data/snapshot/<relPath> → 远程 data-snapshot 分支。
// 结果严格区分：
//   - 确认不存在：本地 ENOENT 且远程 404 → 返回 null（合法空数据）
//   - 传输/解析失败：网络错误、非 404 HTTP 错误、JSON 损坏等 → 抛出
//     SnapshotReadError（由 withDbFallback 转回原始 DB 错误）
// 本地 JSON 损坏时也会尝试远程副本，避免坏文件遮蔽可用远程数据。
//
// DATA_SNAPSHOT_BASE_URL 可覆盖远程基址（主要用于验证与私有镜像）。
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
  /** 快照包含的日报日期（仅带 JSON 的日报），降序 */
  report_dates: z.array(z.string()).default([]),
  /** 快照包含的 source 名称，字母序 */
  sources: z.array(z.string()).default([]),
});

export type SnapshotIndex = z.infer<typeof snapshotIndexSchema>;

/** 快照传输或内容解析失败；与"文件确认不存在"严格区分 */
export class SnapshotReadError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "SnapshotReadError";
  }
}

/** 检查 ASCII 控制字符，避免把它们写入文件路径或远程 URL */
function hasControlCharacter(value: string): boolean {
  for (const char of value) {
    const code = char.charCodeAt(0);
    if (code <= 0x1f || code === 0x7f) return true;
  }
  return false;
}

/**
 * 严格校验快照相对路径，防止路径穿越与 URL 注入。
 * 拒绝反斜杠、查询/片段分隔符、控制字符、绝对路径和 .. 点段。
 * 同时直接拒绝 %：快照路径均为静态生成，无需百分号编码，可阻止
 * %2e%2e、.%2e 经 WHATWG URL 规范化后变成点段的绕过方式。
 */
function normalizeRelativePath(relPath: string): string {
  if (
    !relPath ||
    relPath.includes("\\") ||
    relPath.includes("?") ||
    relPath.includes("#") ||
    relPath.includes("%") ||
    hasControlCharacter(relPath) ||
    path.posix.isAbsolute(relPath) ||
    path.win32.isAbsolute(relPath) ||
    relPath.split("/").some((segment) => segment === "..")
  ) {
    throw new SnapshotReadError(`非法快照路径：${relPath}`);
  }
  return path.posix.normalize(relPath);
}

/** 远程基址统一保留末尾斜杠，避免拼接时丢失分支目录 */
function getRemoteBaseUrl(): string {
  const base = process.env.DATA_SNAPSHOT_BASE_URL ?? DEFAULT_SNAPSHOT_BASE_URL;
  return base.endsWith("/") ? base : `${base}/`;
}

function isEnoent(error: unknown): boolean {
  return (
    typeof error === "object" &&
    error !== null &&
    "code" in error &&
    error.code === "ENOENT"
  );
}

/**
 * 读取远程文本；仅 404 返回 null 表示远端确认不存在。
 * 网络错误、非 404 HTTP 错误与响应读取失败均抛出 SnapshotReadError。
 */
async function readRemoteText(relPath: string): Promise<string | null> {
  let response: Response;
  try {
    response = await fetch(`${getRemoteBaseUrl()}${relPath}`, {
      next: { revalidate: 3600 },
    });
  } catch {
    throw new SnapshotReadError(`远程快照网络读取失败：${relPath}`);
  }

  if (response.status === 404) return null;
  if (!response.ok) {
    throw new SnapshotReadError(
      `远程快照 HTTP ${response.status}：${relPath}`,
    );
  }
  try {
    return await response.text();
  } catch {
    throw new SnapshotReadError(`远程快照响应读取失败：${relPath}`);
  }
}

/**
 * 读取快照中的单个文本文件。
 *
 * 返回 null 的唯一条件是本地 ENOENT 且远程 404；其他本地/远程组合故障
 * 均抛出 SnapshotReadError，避免把传输失败误报为合法空数据。
 */
export async function readSnapshotFile(
  relPath: string,
): Promise<string | null> {
  const normalized = normalizeRelativePath(relPath);
  let localError: unknown;

  try {
    return await readFile(path.join(SNAPSHOT_LOCAL_ROOT, normalized), "utf8");
  } catch (error) {
    localError = error;
  }

  const remoteText = await readRemoteText(normalized);
  if (remoteText !== null) return remoteText;
  if (isEnoent(localError)) return null;

  throw new SnapshotReadError(
    `本地快照读取失败且远程文件不存在：${normalized}`,
  );
}

/**
 * 读取并解析快照 JSON 文件。
 *
 * 本地 JSON 损坏时继续尝试远程副本；只有本地 ENOENT + 远程 404 才返回
 * null。本地损坏且远程 404、远程 JSON 损坏、网络/HTTP 失败均抛错。
 */
export async function readSnapshotJson(relPath: string): Promise<unknown> {
  const normalized = normalizeRelativePath(relPath);
  let localError: unknown;

  try {
    const localText = await readFile(
      path.join(SNAPSHOT_LOCAL_ROOT, normalized),
      "utf8",
    );
    try {
      return JSON.parse(localText) as unknown;
    } catch (error) {
      localError = error;
    }
  } catch (error) {
    localError = error;
  }

  const remoteText = await readRemoteText(normalized);
  if (remoteText !== null) {
    try {
      return JSON.parse(remoteText) as unknown;
    } catch {
      throw new SnapshotReadError(`远程快照 JSON 解析失败：${normalized}`);
    }
  }
  if (isEnoent(localError)) return null;

  throw new SnapshotReadError(
    `本地快照 JSON 解析失败且远程文件不可用：${normalized}`,
  );
}

/**
 * 读取快照索引。React cache() 保证同一请求只读取一次。
 *
 * index.json 确认不存在时返回 null；传输失败、JSON 损坏或结构不符合
 * 契约均抛错，不能再把故障索引误判为"空快照"。
 */
export const getSnapshotIndex = cache(
  async (): Promise<SnapshotIndex | null> => {
    const raw = await readSnapshotJson("index.json");
    if (raw === null) return null;
    try {
      return snapshotIndexSchema.parse(raw);
    } catch {
      throw new SnapshotReadError("快照 index.json 结构不符合契约");
    }
  },
);

/** 快照整体可用性判据：索引确认不存在时抛出 SnapshotReadError */
export async function assertSnapshotAvailable(): Promise<void> {
  const index = await getSnapshotIndex();
  if (!index) {
    throw new SnapshotReadError("本地与远程数据快照均不可用");
  }
}
