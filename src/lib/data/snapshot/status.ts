// ============================================================================
// snapshot/status.ts — 请求作用域的快照使用状态
//
// withDbFallback 成功从快照取数后调用 markSnapshotUsed()；PageShell 中的
// SnapshotNotice 再读取同一请求的状态，决定是否显示离线数据角标。
// React cache() 返回的对象在同一请求内共享，因此无需引入全局可变变量。
// ============================================================================

import { cache } from "react";

import { getSnapshotIndex } from "./client";

export interface SnapshotRequestStatus {
  /** 本次请求是否有任意数据读取成功回退到快照 */
  used: boolean;
  /** 快照生成时间；索引不可读时为 null */
  generatedAt: string | null;
}

const getRequestStatus = cache((): SnapshotRequestStatus => ({
  used: false,
  generatedAt: null,
}));

/** 标记当前请求已使用快照数据（仅由 withDbFallback 在回退成功后调用） */
export function markSnapshotUsed(): void {
  getRequestStatus().used = true;
}

/**
 * 获取当前请求的快照状态；首次需要角标时补充读取 index.json 的
 * generated_at。索引读取本身有请求级缓存，不会造成重复网络请求。
 *
 * 注意：本函数不能用 React cache() 缓存“读取结果”。首页 loading.tsx 也
 * 使用 PageShell，可能在数据加载前读到 used=false；若缓存该中间结果，
 * 正文回退成功后就无法再显示角标。这里只缓存可变的请求状态对象。
 */
export async function getSnapshotStatus(): Promise<SnapshotRequestStatus> {
  const state = getRequestStatus();
  if (!state.used) {
    return { used: false, generatedAt: null };
  }
  if (!state.generatedAt) {
    const index = await getSnapshotIndex();
    state.generatedAt = index?.generated_at ?? null;
  }
  return { ...state };
}
