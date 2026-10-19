// ============================================================================
// snapshot/manifests.ts — 从 data/snapshot/manifests 读取 URL 清单
//
// manifests/{source}.json 是该源全部历史 manifest 的数组，按 date 降序
// （首元素最新）。读取结果与 sources/manifests.ts 的 DB 版本保持一致。
// ============================================================================

import { z } from "zod";

import { manifestSchema } from "@/lib/data/sources/types";
import {
  assertSnapshotAvailable,
  getSnapshotIndex,
  readSnapshotJson,
} from "./client";

type Manifest = z.infer<typeof manifestSchema>;

/** 读取单个 source 的 manifest 数组；文件缺失且索引可用时按正常空数据返回 [] */
async function loadManifestFile(sourceName: string): Promise<Manifest[]> {
  const raw = await readSnapshotJson(`manifests/${sourceName}.json`);
  if (raw === null) {
    await assertSnapshotAvailable();
    return [];
  }
  if (!Array.isArray(raw)) return [];

  const result: Manifest[] = [];
  for (const item of raw) {
    try {
      result.push(manifestSchema.parse(item));
    } catch {
      // 与 DB 版一致：跳过校验失败的 manifest，不影响其他历史记录
    }
  }
  return result;
}

/**
 * 加载快照中所有 source 的最新 manifest（每个文件的首条有效记录）。
 * 使用 Promise.all 并发读取，避免首页在远程回退时串行下载数十个文件。
 */
export async function loadManifests(): Promise<Map<string, Manifest>> {
  const index = await getSnapshotIndex();
  if (!index) {
    throw new Error("本地与远程数据快照均不可用");
  }

  const entries = await Promise.all(
    index.sources.map(async (sourceName) => {
      const manifests = await loadManifestFile(sourceName);
      return [sourceName, manifests[0]] as const;
    }),
  );

  const result = new Map<string, Manifest>();
  for (const [sourceName, manifest] of entries) {
    if (manifest) result.set(sourceName, manifest);
  }
  return result;
}

/** 加载指定 source 在快照中的全部历史 manifest（保持文件内的降序） */
export async function loadManifestsForSource(
  sourceName: string,
): Promise<Manifest[]> {
  return loadManifestFile(sourceName);
}
