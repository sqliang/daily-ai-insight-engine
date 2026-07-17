// ============================================================================
// pagination.ts — 服务端分页切片纯函数与页大小常量
//
// 为列表页（/sources/[name] 文章列表、/dashboard 日报卡片列表）提供统一的
// 分页切片能力。纯函数、无副作用，被数据层（sources/index.ts、reports.ts）
// 在服务端调用；分页元信息随数据传给 Pagination 组件渲染。
// 设计理由：切片逻辑集中在数据层，可同时减少 RSC 传输体积与客户端渲染量，
// 这是列表页卡顿（全量渲染数百张卡片）的根因。
// ============================================================================

/** 文章列表默认每页条数（ArticleCard 较复杂，取值保守） */
export const PAGE_SIZE_ARTICLES = 20;

/** 日报卡片列表默认每页条数 */
export const PAGE_SIZE_REPORTS = 10;

/** 分页元信息 — 随数据层返回值传给分页 UI 组件 */
export interface PaginationMeta {
  /** 当前页码（1-based，已 clamp 到合法范围） */
  page: number;
  /** 每页条数 */
  pageSize: number;
  /** 切片前的总条数 */
  totalItems: number;
  /** 总页数；空列表为 0 */
  totalPages: number;
}

/** 分页切片结果 — 当前页数据 + 分页元信息 */
export interface PaginatedResult<T> extends PaginationMeta {
  /** 当前页的数据切片 */
  items: T[];
}

/**
 * 对数组做分页切片。
 *
 * 参数：
 *   items:   完整数据数组（不会被修改）
 *   page:    目标页码（1-based）；越界时 clamp 到 [1, totalPages]
 *   pageSize: 每页条数；非法值（<1 / NaN）按 1 处理
 *
 * 返回：
 *   PaginatedResult，其中 page 为 clamp 后的实际页码；
 *   空列表返回 { items: [], page: 1, totalPages: 0, ... }
 *
 * 设计理由：
 *   clamp 而非报错 —— URL 中的 page 参数可被用户随意篡改
 *   （如 page=999）， clamp 到末页比 404 更符合浏览语义。
 */
export function paginate<T>(
  items: readonly T[],
  page: number,
  pageSize: number,
): PaginatedResult<T> {
  const size = Number.isFinite(pageSize) && pageSize >= 1 ? Math.floor(pageSize) : 1;
  const totalItems = items.length;
  const totalPages = Math.ceil(totalItems / size);
  const requested = Number.isFinite(page) && page >= 1 ? Math.floor(page) : 1;
  const safePage = totalPages === 0 ? 1 : Math.min(requested, totalPages);
  const start = (safePage - 1) * size;

  return {
    items: items.slice(start, start + size),
    page: safePage,
    pageSize: size,
    totalItems,
    totalPages,
  };
}

/**
 * 解析 URL searchParams 中的 page 参数。
 *
 * 缺省、非数字、小于 1 时一律回退到第 1 页 —— 页码是用户可篡改的
 * 外部输入，解析层兜底可以保证数据层永远收到合法值。
 */
export function parsePageParam(raw: string | undefined): number {
  if (!raw) return 1;
  const n = Number.parseInt(raw, 10);
  return Number.isFinite(n) && n >= 1 ? n : 1;
}
