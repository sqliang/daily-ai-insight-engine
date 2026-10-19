// ============================================================================
// snapshot/fallback.ts — PostgreSQL → 数据快照的统一回退封装
//
// 核心语义：只有 DB 抛错（连接失败、配额挂起等）才尝试快照；DB 正常返回
// null / 空数组表示"数据不存在"，绝不触发回退。快照也不可用时重新抛出
// 原始 DB 错误，让页面沿用既有的 DataUnavailable 降级链路。
// ============================================================================

import { markSnapshotUsed } from "./status";

/** 仅真正拿到快照数据时才显示角标；合法 null/空集合不标记为已使用 */
function hasSnapshotData(result: unknown): boolean {
  if (result === null || result === undefined) return false;
  if (Array.isArray(result)) return result.length > 0;
  if (result instanceof Map) return result.size > 0;
  if (typeof result === "string") return result.length > 0;
  return true;
}

/**
 * 为同签名的 DB 读取函数与快照读取函数生成带回退的读取函数。
 *
 * 快照读取抛错时抛回原始 DB 错误（且不记录角标状态），避免用二次错误
 * 掩盖真正的故障原因；只有快照实际返回数据时才记录请求级快照状态。
 */
export function withDbFallback<Args extends unknown[], Result>(
  dbReader: (...args: Args) => Promise<Result>,
  snapshotReader: (...args: Args) => Promise<Result>,
): (...args: Args) => Promise<Result> {
  return async (...args: Args): Promise<Result> => {
    try {
      return await dbReader(...args);
    } catch (dbError) {
      try {
        const result = await snapshotReader(...args);
        if (hasSnapshotData(result)) {
          markSnapshotUsed();
        }
        return result;
      } catch {
        throw dbError;
      }
    }
  };
}
