# [P1][S][fix][frontend] Fix article detail 404 for articles outside default 14-day window

## Problem

文章详情页对所有"创建时间早于近 14 天"的文章返回 404,即使用户是从列表页正常点击进入的。

**复现路径**:
1. 打开 https://daily-ai-insight-engine.vercel.app/sources/arxiv-cs-ai (列表默认时间筛选为"全部")
2. 翻页到较早的文章(如 page=18,2026-08-31 的文章)
3. 点击进入详情 → **404 This page could not be found**

实测案例:`/sources/arxiv-cs-ai/articles/ae709a916c274f9e?page=18`(文章 `ae709a916c274f9e`,created=2026-08-31)。已确认该文章**在 articles 表中存在**(id / source_dir / created 均匹配),404 不是数据缺失,而是查询逻辑问题。

**影响范围**:所有 created 早于近 14 天的文章详情页都会 404。随着 6~7 月历史数据恢复入库(articles 表现有 7500+ 篇、横跨 5 个月),受影响链接占比超过 90%,信源页的历史文章浏览功能基本不可用。

## 根因分析

**列表页与详情页的默认时间范围不一致**:

- 列表页(`src/app/sources/[name]/page.tsx`):无筛选参数时默认"全部"(commit `7b93d858` 引入),所以 page=18 能正常显示 8 月的文章
- 详情页(`src/app/sources/[name]/articles/[articleId]/page.tsx` 的 `resolveDateRange()`):无 `preset`/`from`/`to` 参数时**默认回退到近 14 天**(`fromDate.setDate(today - 14)`)
- 详情查询 `getSourceArticleDetail()`(`src/lib/data/sources/index.ts:381`)把 dateRange 传给 `getSourceDetailEnriched()`,文章列表被裁剪到近 14 天后再 `findIndex` 匹配 articleId → 窗口外的文章匹配失败 → `notFound()`

**放大因素**:文章卡片链接(`buildArticleDetailHref`)只透传 `page` 等参数,未把列表页当前生效的时间范围(或其"全部"语义)带给详情页,导致详情页总是走自己的 14 天默认值。

## Scope

- `src/lib/data/sources/index.ts` — `getSourceArticleDetail()`:文章本体定位不再受 dateRange 约束(用全量/宽窗口文章集查找),dateRange 仅用于上一篇/下一篇邻导航上下文
- `src/app/sources/[name]/articles/[articleId]/page.tsx` — 配合调整(如 resolveDateRange 的用途收窄)
- 涉及文件预计 1-2 个,改动集中在数据查询层

## Acceptance Criteria

- [ ] 直接访问 `https://daily-ai-insight-engine.vercel.app/sources/arxiv-cs-ai/articles/ae709a916c274f9e`(无任何 query 参数)返回 200,展示文章详情
- [ ] 从列表页任意日期筛选(全部 / 近 7 天 / 自定义范围)点击进入任意文章详情,均不 404
- [ ] 文章不存在(伪造 id)时仍正确返回 404
- [ ] 详情页的"上一篇 / 下一篇"导航在带日期筛选进入时仍按筛选上下文排序工作
- [ ] `pnpm typecheck && pnpm lint && pnpm build` 通过

## Approach

推荐方案:解耦"文章定位"与"导航上下文"。`getSourceArticleDetail()` 内部先用**不带 dateRange** 的文章集定位目标文章(找到才继续,找不到才 404),再用 dateRange 过滤后的列表计算 previousArticle / nextArticle。这样直接访问、分享链接、搜索引擎抓取的详情 URL 对任何已入库文章都可达,dateRange 退化为纯导航上下文。

[Assumption] 默认时间筛选语义(列表"全部" vs 详情"近 14 天")以列表页为准,详情页不再自行设默认窗口——因为详情页的核心职责是展示单篇文章,而不是列表过滤。

## Testing Strategy

- 本地 `pnpm dev` + 本地/Neon 数据库,直接访问若干 created 早于 14 天的文章详情 URL 验证 200
- 构造不存在的 articleId 验证仍 404
- 部署后回归实测报告中的 URL
