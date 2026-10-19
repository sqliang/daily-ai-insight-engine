// ============================================================================
// snapshot/fallback.ts — PostgreSQL → 数据快照的统一回退封装
//
// 核心语义：只有 DB 抛错（连接失败、配额挂起等）才尝试快照；DB 正常返回
// null / 空数组表示"数据不存在"，绝不触发回退。快照也不可用时重新抛出
// 原始 DB 错误，让页面沿用既有的 DataUnavailable 降级链路。
// ============================================================================

import { markSnapshotUsed } from "./status";

/**
 * 为同签名的 DB 读取函数与快照读取函数生成带回退的读取函数。
 *
 * 快照成功返回（包括合法的空数据）时记录请求级快照状态，供 UI 角标使用；
 * 快照读取抛错时抛回原始 DB 错误，避免用二次错误掩盖真正的故障原因。
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
        markSnapshotUsed();
        return result;
      } catch {
        throw dbError;
      }
    }
  };
}
