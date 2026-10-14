# [P0][L][perf][fullstack] Reduce Neon DB egress to restore site availability

> 诊断日期：2026-10-14 · 现象：线上站点完全无法打开，Neon 控制台提示
> "You've used all of your monthly network transfer allowance for this project"

## 诊断报告（给非技术读者的版本）

### 发生了什么？

网站打不开不是代码崩溃，而是**数据库被 Neon 平台"停机"了**：

1. 我们用的是 Neon 免费套餐，每个项目每月只有 **5 GB 数据库出站流量**额度
   （出站 = 数据库发给网站服务器的数据；写入不算）。
2. 10 月账单周期内这 5 GB 被用完了。Neon 官方规则是：免费套餐流量耗尽后
   **数据库计算实例直接挂起**，直到下个计费周期重置或升级套餐
   （[Neon plans 文档](https://neon.com/docs/introduction/plans)：
   "when you run out of CU-hours or public network transfer, your compute is
   suspended until the next billing period or until you upgrade"）。
3. 我们网站所有页面都要实时查数据库，数据库一挂，全站瘫痪。

**数据没有丢失，也不用抢救**——下个计费周期会自动恢复，升级套餐可立即恢复。

### 为什么 5 GB 这么快就用完了？（根因）

额度是平台的，但**烧流量的方式是我们自己代码的问题**。三个叠加因素：

**因素 1：查得太多 —— 列表页把整列大 JSON 全捞出来**

`articles` 表每行有一个 `payload` JSONB 字段（约 10 KB/行，全表约 8000 行 ≈ 90 MB）。
文章列表页（`/sources/[name]`）的查询（`src/lib/data/sources/structured-data.ts:43-46`）：

- 默认时间范围是"全部历史"（2000-01-01 起）
- SQL 没有 `LIMIT`，把该源**全部历史文章**的完整 payload 一次性拉回
- 分页是在 Node.js 内存里做的（`src/lib/utils/pagination.ts:51-70` 的 `paginate()`），
  数据库流量一分不少；**每翻一页、每切一次排序都重新全量拉一遍**

实测单次访问大源的出站流量：hackernews ≈ 20 MB、github-trending ≈ 14 MB、
arxiv ≈ 13 MB、36kr ≈ 12 MB。

**因素 2：文章详情页的"兜底"查询**

`src/lib/data/sources/index.ts:92-95, 420-433`：打开一篇文章详情时，先在 14 天窗口内
全量加载该源数据找这篇文章；找不到（文章早于 14 天）就改用 **1970-9999 全量范围
再加载一遍**——等于为了取一行数据，把整个 source 的文章全拉了一次（又一次 ~20 MB）。
而 `articles.id` 本来就是主键，可以直接精确查单行。

**因素 3：全站零缓存**

全部 8 个页面都是 `export const dynamic = "force-dynamic"`，全仓库没有
`revalidate` / `unstable_cache` / React `cache()`。意味着**每一次访问、每一次刷新、
每一次搜索引擎爬虫抓取都真实打到数据库**。而日报数据一天只更新一次，
完全可以用缓存承接绝大部分访问。

**粗算**：每天只要有约 10 次大 source 列表页浏览（含翻页）≈ 200 MB+/天 ≈ 6 GB/月，
仅凭因素 1+2 就足以耗尽 5 GB 免费额度。

### 可以排除的嫌疑

- 每日 publish 写入 ~25 MB：**不计入流量**（Neon 只计出站 egress，写入是入站）
- 数据库客户端连接方式：正常，无轮询、无重复建连放大
- 平台故障：不是，是额度规则按设计生效

## Problem

网站因 Neon 免费套餐 5 GB/月出站流量耗尽被平台挂起，全站不可用。
根因是前端数据层三个设计缺陷：列表页无 SQL 分页且整列拉取大 JSONB、
文章详情页用全量加载代替主键查询、全站 force-dynamic 零缓存。
即使升级套餐恢复服务，不改代码流量仍会以 $0.10/GB 持续计费。

## Scope

- 修改 `src/lib/data/sources/structured-data.ts`
  - `loadStructuredData()` 支持 SQL 级 `LIMIT/OFFSET` 分页 + 按 `impact_score` 排序下推
  - 列表场景只 select 标量列（id/title/url/tldr/impact_score/sentiment/created 等），不拉整列 `payload`
- 修改 `src/lib/data/sources/index.ts`
  - `getSourceArticleDetail()` 改为按主键 `id` 精确查单行，删除 14 天窗口 + 全量 fallback 的全量加载逻辑
- 修改 `src/app/**/page.tsx`（8 个页面）
  - `export const dynamic = "force-dynamic"` → `export const revalidate = 3600`
- 修改 `src/lib/data/sources/manifests.ts`
  - `loadManifests()` 加 React `cache()` 做请求内去重

## Approach

性价比排序：SQL 分页 + 列裁剪（单次 20 MB → KB 级）是根治；详情页主键查询
消除重复全量加载；revalidate 缓存让 Vercel 边缘承接重复访问。
三者正交，可一次做完。备选方案"回退为读本地 JSON/构建期静态生成"改动面更大，
且与 PostgreSQL 解耦架构相悖，不采用。

## Acceptance Criteria

- [ ] `/sources/[name]` 任意源、任意页码、任意排序下页面正常渲染，且单次请求的 SQL 带 `LIMIT/OFFSET`（不整列拉 `payload` 到内存分页）
- [ ] 打开任意历史文章详情页（含早于 14 天的文章）正常渲染，且只产生按主键的单行查询
- [ ] 8 个页面无 `force-dynamic`，均为 `revalidate = 3600`；`pnpm build` 输出中页面标记为静态/ISR 而非动态
- [ ] `loadManifests()` 在同一请求内多次调用只执行一次 DB 查询
- [ ] `pnpm typecheck`、`pnpm lint`、`pnpm build` 全部通过
- [ ] 修复后估算月出站流量 < 100 MB（远低于 5 GB 免费额度）

## Testing Strategy

- `pnpm dev` 本地连接数据库，逐一访问首页、大源列表页（hackernews/arxiv 翻 3 页 + 切排序）、历史文章详情页、dashboard 列表/详情、report 页、3 个 specialized 页，确认渲染正常
- `pnpm build` 检查页面渲染模式标记
- 部署后观察 Neon 控制台 Data Transfer 指标增速

## Dependencies / Risks

- **本站恢复不依赖本修复**：额度下个计费周期自动重置，或升级 Neon Launch 套餐（500 GB/月）立即恢复；本修复防止再次耗尽
- 风险：SQL 分页改动涉及列表页排序/总数统计逻辑，需回归验证翻页与排序交互
- 回滚方案：`git revert` 修复提交后重新部署即可

## Out of Scope

- 不升级/降级 Neon 套餐（运维决策，由用户自行在 Neon 控制台操作）
- 不改动 pipeline 写入侧（publish 为入站流量，不计费）
- 不重构 `payload` JSONB 的表结构（如拆列）——列裁剪已足够把流量降到 KB 级
