---
name: issue-breakdown
description: >
  自动化需求拆解与 Issue 生成。将需求描述、问题汇总、用户想法拆解为独立的结构化 Issues，
  每个 Issue 生成 .md 文件并默认同步到 GitHub。
  触发场景：需求拆解、问题拆解、issue 拆分、需求分析、任务分解、创建 issues、
  breakdown requirement、decompose task、create GitHub issues from requirements。
---

# 需求拆解与 Issue 生成

## The Job

收到用户输入（需求描述、问题汇总、想法）后，完成以下步骤：

1. **澄清问题** — 提 3-5 个字母选项式问题确认理解
2. **拆解** — 将输入分解为独立 issues，每个 issue 分配四维标签
3. **写入文件** — 每个 issue 生成独立 `.md` 到 `docs/issues/`
4. **同步 GitHub** — 默认通过 `gh issue create` 创建（用户明确拒绝时才跳过）
5. **汇总输出** — 列出所有 issue 文件路径和 GitHub URL

**重要：只拆解和记录，不要开始实现。不要修改任何源代码。**

## Step 1: 澄清问题

收到用户输入后，在拆解之前先提 3-5 个问题确认理解。聚焦四个领域：

- **问题/目标** — 到底要解决什么？
- **范围/边界** — 明确不做什么？
- **技术约束** — 有什么限制？
- **优先级/复杂度** — 紧急程度和投入估算

### 问题格式

使用字母选项格式，让用户可以用 `1A, 2C, 3B` 的紧凑形式一次性回答：

```
确认几个关键点：

1. 这个需求的核心目标是什么？
   A. <选项A>
   B. <选项B>
   C. <选项C>
   D. 其他: [请说明]

2. 明确不做什么？
   A. <选项A>
   B. <选项B>
```

### 用户跳过澄清时

如果用户回复"直接拆解"或跳过问题，填写合理默认值，在 issue 中标注 `[Assumption]`，让不确定性可见。

## Step 2: 拆解原则

将输入分解为独立 issues 时遵循：

- **每个 issue 可独立交付** — 完成一个 issue 的改动可以独立测试和部署，不依赖其他 issue 必须先完成
- **粒度适中** — 每个 issue 的 Scope 控制在 1-5 个文件或 1-3 个功能点，避免 God Issue
- **拆解维度** — 按功能模块、技术层次（前端/后端/数据）、数据流阶段（采集→处理→展示）拆分
- **顺序标注** — 如果确实有依赖关系，在 `Dependencies / Risks` 段中明确标注 `[Blocked by #00X]`
- **超过 10 个时提示** — 拆出太多时提醒用户是否需要合并或分批

## Step 3: Issue 标题格式

**每个 issue 标题必须包含四维标签前缀：**

```
[优先级][复杂度][类型][范围] 英文祈使句描述
```

### 四个标签位

| 位置 | 维度 | 可选值 |
|------|------|--------|
| `[P0-P3]` | 优先级 | `P0`(紧急/阻塞) `P1`(高) `P2`(中) `P3`(低) |
| `[S-XL]` | 复杂度 | `S`(<1天) `M`(1-3天) `L`(3-5天) `XL`(>5天) |
| `[类型]` | 工作性质 | `feat` `fix` `chore` `docs` `refactor` `perf` `security` `enhancement` |
| `[范围]` | 影响域 | `frontend` `backend` `pipeline` `infra` `data` `fullstack` |

### 标题示例

```
[P0][XL][feat][fullstack] Migrate authentication from JWT to OAuth 2.0
[P1][M][feat][frontend] Add pagination to search endpoint
[P1][L][fix][backend] Resolve race condition in article dedup worker
[P2][S][chore][infra] Upgrade Node.js runner to v24
[P2][M][perf][frontend] Memoize dashboard chart components
[P3][S][docs][fullstack] Add JSDoc to all exported React components
```

### 标题规则

- 描述用祈使句现在时（add / fix / upgrade），不用过去式
- 首字母小写
- 不用句号结尾
- 控制在约 72 字符以内（含标签前缀）

## Step 4: Issue 正文

使用 `references/issue-template.md` 中的 7 段模板。核心要求：

- **Problem** — 说清为什么重要，谁受影响，影响多大
- **Scope** — 列出具体改什么，涉及哪些文件
- **Acceptance Criteria** — 每项必须 observable / testable / verifiable；禁止 "work correctly"
- **Approach** — 方案一目了然时省略，需要设计决策时保留
- **Testing Strategy** — 无需特殊测试时省略
- **Dependencies / Risks** — 无依赖时省略
- **Out of Scope** — 边界清晰时省略

## Step 5: 输出

### 文件写入

每个 issue 写入独立文件，命名规则：

```
docs/issues/{NNN}-{优先级}-{复杂度}-{类型}-{范围}-{slug}.md
```

示例：
```
docs/issues/001-P1-M-feat-frontend-pagination.md
docs/issues/002-P1-L-fix-backend-dedup-race.md
docs/issues/003-P2-S-chore-infra-node-upgrade.md
```

先确保 `docs/issues/` 目录存在（不存在则创建）。

### 同步到 GitHub

**默认在文件写入后立即执行 `gh issue create`。** 仅在用户明确说"不用同步到 GitHub""只要本地"时才跳过。

#### 前置步骤：确保 Labels 存在

**在创建 issues 之前，先检查并创建所需 labels**，否则 `gh issue create --label` 会失败：

```bash
# 检查哪些 labels 已存在
gh label list

# 按需创建缺失的 labels（幂等操作，已存在的不会重复创建）
# Priority
gh label create "priority:critical" --color "B60205" 2>/dev/null
gh label create "priority:high" --color "D93F0B" 2>/dev/null
gh label create "priority:medium" --color "FBCA04" 2>/dev/null
gh label create "priority:low" --color "0E8A16" 2>/dev/null
# Difficulty
gh label create "difficulty:easy" --color "0E8A16" 2>/dev/null
gh label create "difficulty:medium" --color "FBCA04" 2>/dev/null
gh label create "difficulty:hard" --color "D93F0B" 2>/dev/null
gh label create "difficulty:xl" --color "B60205" 2>/dev/null
# Type
gh label create "type:feature" --color "0E8A16" 2>/dev/null
gh label create "type:bug" --color "D93F0B" 2>/dev/null
gh label create "type:chore" --color "C5DEF5" 2>/dev/null
gh label create "type:docs" --color "0075CA" 2>/dev/null
gh label create "type:refactor" --color "5319E7" 2>/dev/null
gh label create "type:perf" --color "1D76DB" 2>/dev/null
gh label create "type:security" --color "B60205" 2>/dev/null
gh label create "type:enhancement" --color "A2EEEF" 2>/dev/null
# Scope
gh label create "scope:frontend" --color "006B75" 2>/dev/null
gh label create "scope:backend" --color "BFDADC" 2>/dev/null
gh label create "scope:pipeline" --color "BFDADC" 2>/dev/null
gh label create "scope:infra" --color "D4C5F9" 2>/dev/null
gh label create "scope:data" --color "F9D0C4" 2>/dev/null
gh label create "scope:fullstack" --color "D4C5F9" 2>/dev/null
# Status
gh label create "status:ready" --color "0E8A16" 2>/dev/null
```

#### 单个 issue

```bash
gh issue create \
  --title "[P1][M][feat][frontend] Add pagination to search endpoint" \
  --label "priority:high,difficulty:medium,type:feature,scope:frontend,status:ready" \
  --body-file docs/issues/001-P1-M-feat-frontend-pagination.md
```

#### 批量创建（安全规则）

当需要一次创建多个 issues 时，**严格遵守以下规则避免重复**：

**规则 1：使用单一路径展开。** 不要用多个可能重叠的 glob pattern。
**规则 2：文件名带前缀时，一个 glob 覆盖全部即可。** 例如文件名以 `0` 开头时，`0*.md` 已匹配所有。

安全写法（推荐）：
```bash
# 方式一：单个 glob 直接展开
for f in docs/issues/0*.md; do
  # 从文件名提取标题和 labels...
  gh issue create --title "$title" --label "$labels" --body-file "$f"
done

# 方式二：ls + sort + while read（更安全，避免 glob 陷阱）
ls docs/issues/0*.md | sort | while read f; do
  # ...
done
```

**禁止的错误写法**：
```bash
# 错误！0*.md 和 01*.md 重叠，010*.md 会被处理两次
for f in docs/issues/0*.md docs/issues/01*.md docs/issues/02*.md; do
```

#### 创建后验证

全部创建完成后，用 `uniq -d` 检查是否有标题完全相同的重复 issue：
```bash
gh issue list --state open --limit 100 --json title --jq '.[].title' | sort | uniq -d
```
如果有输出，说明存在重复，用 `gh issue close <N> --reason "not planned"` 关闭重复项。

#### Labels 映射表（标题标签 → GitHub Label）

| 标题标签 | GitHub Label |
|---------|-------------|
| P0 / P1 / P2 / P3 | `priority:critical` / `priority:high` / `priority:medium` / `priority:low` |
| S / M / L / XL | `difficulty:easy` / `difficulty:medium` / `difficulty:hard` / `difficulty:xl` |
| feat / fix / chore / docs / refactor / perf / security / enhancement | `type:feature` / `type:bug` / `type:chore` / `type:docs` / `type:refactor` / `type:perf` / `type:security` / `type:enhancement` |
| frontend / backend / pipeline / infra / data / fullstack | `scope:frontend` / `scope:backend` / `scope:pipeline` / `scope:infra` / `scope:data` / `scope:fullstack` |
| (始终) | `status:ready` |

### 汇总输出

全部 issues 创建完毕后，打印汇总表格：

```
| # | Issue | 文件 | GitHub |
|---|-------|------|--------|
| 001 | [P1][M][feat][frontend] Add pagination | docs/issues/001-...md | https://github.com/.../issues/1 |
| 002 | [P1][L][fix][backend] Fix dedup race | docs/issues/002-...md | https://github.com/.../issues/2 |
```

## Edge Cases

| 场景 | 处理方式 |
|------|---------|
| 用户输入很模糊 | 追问一次；仍模糊则推断合理默认值并标注 `[Assumption]` |
| `docs/issues/` 不存在 | 自动创建 |
| 用户说"不用同步到 GitHub""只要本地" | 只生成本地 `.md`，跳过 `gh` |
| 拆出的 issue 超过 10 个 | 提示用户数量较多，建议按优先级分批次实施 |
| 用户要求修改某个 issue | 更新对应 `.md` 文件，用 `gh issue edit` 同步标题和正文 |
| GitHub repo 未设 remote 或无权限 | 用 `gh repo view` 检测，失败时告知用户并降级为仅本地 |
| Labels 在 GitHub repo 中不存在 | 先执行 `gh label create` 创建所有需要的 labels，再创建 issues（见 Step 5 前置步骤） |
| 批量创建后发现重复 issue | 用 `gh issue list \| sort \| uniq -d` 检测，用 `gh issue close <N> --reason "not planned"` 关闭重复项 |

## Example

### 输入

> 我们 dashboard 页面的 KPI 卡片数字显示有延迟，首次加载时总是显示 0 然后跳变，体验很差。另外 TopEventsSection 的列表有时候事件标题重复。还有我想给报告页加一个导出 PDF 的功能。

### 澄清

```
确认几个关键点：

1. PDF 导出的样式要求？
   A. 保持网页样式，直接打印导出
   B. 需要专门的 PDF 排版，包含报告封面和页眉页脚
   C. 暂无特殊要求，能导出即可

2. 这些问题有明确的优先级差异吗？
   A. KPI 动画问题最紧急，先修；PDF 导出排后面
   B. 三个问题都希望尽快处理

3. PDF 导出是在前端生成还是后端生成？
   A. 前端（浏览器端）生成
   B. 后端（Node.js 服务端）生成
   C. 没有偏好，推荐最优方案
```

### 拆解结果

**Issue 1**: `[P1][S][fix][frontend] Fix KPI card initial zero flash`
**Issue 2**: `[P2][S][fix][frontend] Deduplicate TopEventsSection titles`
**Issue 3**: `[P2][M][feat][frontend] Add PDF export to report page`

## Self-Audit Checklist

保存每个 issue 前，确认以下各项：

- [ ] 标题是否包含 `[P?][S/M/L/XL][type][scope]` 四维标签？
- [ ] 每个 issue 是否为独立可交付的工作单元？
- [ ] Problem 是否说清了为什么重要、谁受影响？
- [ ] Scope 是否具体到文件或组件级别？
- [ ] 每个 AC 是否 observable/testable/verifiable？（无 "work correctly"）
- [ ] 可选段在不需要时是否已省略？
- [ ] 文件命名是否遵循 `{NNN}-{P}-{复杂度}-{type}-{scope}-{slug}.md`？
- [ ] Labels 是否按映射表正确设置？
- [ ] 批量创建前：GitHub repo 的 labels 是否已就绪？（`gh label list` 预检）
- [ ] 批量创建后：是否有重复 issue？（`gh issue list | sort | uniq -d` 检查）
