// ============================================================================
// sources/config.ts — Pipeline YAML 配置文件读取
//
// 封装 pipeline/config.yaml 和 pipeline/tiers.yaml 的读取和解析逻辑。
// 提供 getSourceConfigs()（获取已启用的 source 配置列表）和
// getTiersMeta()（获取 tier 元数据）两个纯数据读取函数。
// ============================================================================

import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { parse as parseYaml } from "yaml";
import type { SourceConfig } from "./types";
import type { TierMeta } from "@/lib/data/tiers";

// ---------------------------------------------------------------------------
// 配置文件路径常量
// ---------------------------------------------------------------------------

const CONFIG_PATH = join(process.cwd(), "pipeline/config.yaml");
const TIERS_PATH = join(process.cwd(), "pipeline/tiers.yaml");

// ---------------------------------------------------------------------------
// 配置读取函数
// ---------------------------------------------------------------------------

/**
 * 读取 pipeline/config.yaml 并返回所有已启用的 source 配置。
 *
 * 过滤掉 enabled: false 的 source，仅返回活跃源。
 */
export async function getSourceConfigs(): Promise<SourceConfig[]> {
  const raw = await readFile(CONFIG_PATH, "utf8");
  const config = parseYaml(raw);
  const sources: unknown[] = config?.sources ?? [];
  return sources
    .filter(
      (s): s is SourceConfig =>
        typeof s === "object" &&
        s !== null &&
        "enabled" in s &&
        (s as SourceConfig).enabled === true,
    )
    .map((s) => s as SourceConfig);
}

/**
 * 读取 pipeline/tiers.yaml 并返回所有 tier 的元数据。
 *
 * 返回的 key 为 tier 标识（"A"/"B"/"C"），value 包含 label/subtitle/rationale。
 */
export async function getTiersMeta(): Promise<Record<string, TierMeta>> {
  const raw = await readFile(TIERS_PATH, "utf8");
  const tiers = parseYaml(raw);
  return (tiers ?? {}) as Record<string, TierMeta>;
}
