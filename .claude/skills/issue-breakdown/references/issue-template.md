# Issue Body Template

Use this template when creating a GitHub issue via `gh issue create`.

```markdown
## Problem
<!-- 问题是什么？为什么重要？ -->
<!-- 如何触发的？谁受影响？影响多大？ -->
<!-- 用 2-4 句话描述清楚背景和动机 -->

## Scope
<!-- 需要改什么？涉及哪些文件/组件/系统？ -->
<!-- 列出具体变更项，尽量精确到文件路径 -->
- 

## Approach
<!-- 解决思路是什么？考虑过哪些替代方案？为什么选这个？ -->
<!-- 实现方案一目了然时可省略本段 -->

## Acceptance Criteria
<!-- 完成标准 — 所有框必须打勾才算 Done -->
<!-- 每项必须 observable / testable / verifiable -->
<!-- 禁止：❌ "work correctly"  ❌ "good UX"  ❌ "excellent performance" -->
- [ ] 

## Testing Strategy
<!-- 如何验证？哪些回归场景需要覆盖？ -->
<!-- 无需特殊测试时可省略本段 -->

## Dependencies / Risks
<!-- 依赖什么前置条件？有什么风险？回滚方案？ -->
<!-- 无依赖/风险时可省略本段 -->

## Out of Scope
<!-- 明确不做什么，防止范围膨胀 -->
<!-- 边界清晰时可省略本段 -->
```

## Examples

### Example 1: Bug Fix

```markdown
## Problem
Dashboard KPI 卡片首次渲染时数字显示为 0，约 800ms 后跳变到正确值。
MetricCard 组件使用 requestAnimationFrame 做计数动画，但动画从 0 开始
且无初始值设置。用户感知为闪烁（flash of zero），影响数据信任感。

## Scope
- 修改 src/components/dashboard/MetricCard.tsx 动画逻辑
  - 动画起始值改为最终值的 90%（减少视觉跳跃距离）
  - 或先显示 `--` placeholder，动画完成后再显示数字

## Approach
两种方案：
A. 动画起始值设为最终值的 90% — 改动最小，但仍可感知跳跃
B. SSR 预计算最终值，客户端渲染时直接显示 — 彻底消除动画，但丢失动效

选 A：平衡视觉体验和实现复杂度，配合 `duration: 600ms` 的快动画减少可见跳变。

## Acceptance Criteria
- [ ] 页面首次加载时，KPI 数字在 600ms 内从接近最终值过渡到精确值
- [ ] 无 "0 → 最终值" 的大幅跳动
- [ ] value prop 变化时，动画重新执行
- [ ] 组件卸载时 requestAnimationFrame 被取消（控制台无 "on unmounted component" 警告）

## Testing Strategy
- 浏览器中反复刷新 /dashboard 页面 10 次，确认无 0 值闪现
- 使用 React DevTools Profiler 确认组件卸载时无残留动画帧
- 修改 value prop 模拟数据更新，确认动画重新触发
```

### Example 2: Feature

```markdown
## Problem
用户需要将每日 AI 洞察报告以 PDF 格式分享给未使用平台的管理层。
当前报告仅支持网页浏览，离线分享和存档不方便。

## Scope
- 新增 src/components/report/ExportPDFButton.tsx（导出按钮组件）
- 新增 src/lib/report/generate-pdf.ts（PDF 生成逻辑，基于 html2canvas + jsPDF）
- 在 src/app/report/page.tsx 中集成导出按钮
- 安装 html2canvas 和 jspdf 依赖

## Approach
使用 html2canvas 截取报告内容为图片，再用 jsPDF 嵌入 PDF。
备选方案 @react-pdf/renderer 需要声明式组件重写，成本过高。
选择 html2canvas + jsPDF：兼容现有 react-markdown 渲染内容，无需重写。

## Acceptance Criteria
- [ ] 报告页右上角显示"导出 PDF"按钮
- [ ] 点击按钮后 3 秒内生成并下载 PDF 文件（文件名：AI洞察报告-YYYY-MM-DD.pdf）
- [ ] PDF 包含报告标题、日期、执行摘要、所有 chart 图表、正文内容
- [ ] 中文内容渲染正常（无乱码）
- [ ] 移动端按钮隐藏（屏幕宽度 < 768px 时不可见）

## Testing Strategy
- 在 Chrome/Firefox/Safari 中分别测试 PDF 导出
- 验证导出的 PDF 在 Preview.app 和 Adobe Reader 中打开正常
- 使用不同日期报告数据验证内容完整性

## Out of Scope
- 不包含邮件自动发送 PDF 功能（后续独立需求）
- 不导出 dashboard 交互图表为动态 SVG（PDF 中为静态截图）
```

### Example 3: Chore

```markdown
## Problem
当前 tsconfig.json target 为 ES2018，缺少 Array.flatMap、Object.fromEntries、
Promise.allSettled 等现代 API 的原生支持。代码中已在使用这些 API，
依赖 Next.js/swc 的 downlevel 编译，增加不必要的编译开销。

## Scope
- 修改 tsconfig.json: target 从 "ES2018" → "ES2022"

## Acceptance Criteria
- [ ] `pnpm typecheck` 通过，无新增类型错误
- [ ] `pnpm build` 成功，构建产物大小无显著增长（±5%）
- [ ] CI 中的 lint/typecheck/build 全部通过

## Dependencies / Risks
- 确认 Vercel 部署环境的 Node.js 版本支持 ES2022（当前 v24，已验证支持）
- 回滚方案：恢复 target 为 ES2018 并重新部署
```
