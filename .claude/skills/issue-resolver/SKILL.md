---
name: issue-resolver
description: >
  以单个 GitHub Issue 为输入，深度分析代码库后制定解决方案，自我评估后决定自动实现或仅评论。
  自动实现时按 git-workflow 规范完成分支→改代码→提交→PR→Issue评论的完整闭环。
  触发场景：解决 issue、分析 issue、制定解决方案、resolve issue、fix issue、implement issue、
  分析这个 issue、帮我解决 #XX、#XX 怎么修、改一下 #XX。
---

# Issue 解决方案制定与自主实现

## The Job

以单个 Issue 为输入，完成 6 步全流程。根据自我评估结果分两支：

**自动实现分支（简单/安全的改动）**：
分析 → 方案 → 自我评估 ✅ → 分支 → 改代码 → 提交 → PR → Issue评论（含PR链接）

**仅评论分支（复杂/高风险的改动）**：
分析 → 方案 → 自我评估 ❌ → Issue评论（含完整方案 + 人工处理建议）

**理念**：简单改动无需来回确认，用户打开 Issue → 读结论评论 → 点 PR 链接 review。复杂改动在 Issue 中留下完整方案和上下文，等待人工介入。

## Step 1: 获取 Issue 内容

根据用户输入的方式获取 issue 内容：

- **GitHub #号**（如 `#10`）：`gh issue view <N> --json title,body` 拉取
- **GitHub URL**（如 `https://github.com/.../issues/10`）：提取 #号后用 `gh`
- **本地 .md 文件**（如 `docs/issues/001-....md`）：直接 Read
- **用户直接粘贴** issue 摘要：以此为输入

提取以下关键信息：
- 标题（确认四维标签：[P?][S/M/L/XL][type][scope]）
- Problem（问题描述，谁受影响，影响多大）
- Scope（涉及文件列表）
- Acceptance Criteria
- 相关代码片段（issue 中已列出的）

## Step 2: 深度分析代码库

**这是最关键的步骤。必须亲自读代码验证根因，不能仅凭 issue 描述推断。**

### 2.1 阅读 Scope 中的所有文件

按 Scope 中列出的文件路径，逐个 Read 相关源文件。理解：
- 当前代码逻辑
- 数据流方向
- 和其他模块的交互

### 2.2 搜索引用方

用 `grep` 搜索关键函数名、类名、组件名，确认：
- 哪些地方调用了相关代码
- 修改会影响哪些下游
- 是否有类似的问题在其他文件中存在

```bash
grep -rn "函数名\|组件名" --include="*.py" --include="*.tsx" --include="*.ts"
```

### 2.3 确认根因

在 issue 描述的基础上，通过代码审查确认问题的真实根因。如果发现 issue 描述有误（Scope 不准确、根因判断错误），在方案中纠正。

## Step 3: 制定方案

按 `references/solution-template.md` 模板输出结构化解决方案，包括：
- 根因分析（基于代码证据）
- 涉及文件 + 具体改动（改动前后对比）
- 验证步骤（可执行的命令）
- 风险与回滚
- 影响范围

输出方案后，**不要等待用户确认**，直接进入 Step 4 自我评估。

## Step 4: 自我评估与决策

读取 `references/complexity-criteria.md`，按清单逐项自评。

### 评估流程

1. 对照「自动实现条件」逐项检查，确认是否 **全部满足**
2. 对照「仅评论条件」逐项检查，确认是否有 **任意一条命中**
3. 如果处于灰色地带 → **倾向 defer 给人工**

### 决策输出

在终端输出评估结论：

```
## 自我评估

| 条件 | 判定 | 说明 |
|------|------|------|
| 文件数 ≤ 5 | ✅/❌ | N 个文件 |
| 无需 DB 迁移 | ✅/❌ | — |
| 不改变 API 契约 | ✅/❌ | — |
| 不涉及 auth/安全 | ✅/❌ | — |
| 优先级 P1-P3 | ✅/❌ | 标签显示 P? |
| 增量/简单替换 | ✅/❌ | — |
| 级联影响 ≤ 3 | ✅/❌ | grep 确认 N 个下游 |
| 无新增依赖 | ✅/❌ | — |

**决策**: 自动实现 / 仅评论
**原因**: （一句话总结）
```

## Step 5: 自动实现（仅当 Step 4 评估通过）

按 git-workflow 规范完成完整交付流程。

### 5.1 创建分支

**必须严格按以下 5 步执行，不可跳过任何一步。**

#### 分支命名

| Issue 类型 | 分支前缀 |
|-----------|---------|
| feat / enhancement | `feature/` |
| fix | `fix/` |
| chore / docs / refactor / perf | `chore/` |

分支名从 issue 标题提取关键词，kebab-case：`fix/dedup-uncertain-key`、`feat/error-boundaries`。

#### Step 1: Stash 未提交改动（如有）

```bash
git stash push -u -m "WIP: <brief description>"
```

`-u` 确保新创建但未跟踪的文件也被暂存。**如果工作区已是干净状态（git status 无任何改动），跳过此步。**

#### Step 2: 同步基分支（必须执行，不可跳过）

```bash
git checkout main
git fetch origin main
git pull --rebase origin main
```

**即使工作区干净也必须执行。** 跳过的风险：新分支基于过期的 main，后续 PR 可能包含已在 main 上修复的冲突，或缺失 main 上新增的依赖。

#### Step 3: 创建新分支

```bash
git checkout -b <prefix>/<slug>
```

#### Step 4: 恢复 stash（仅当 Step 1 有 stash 时）

```bash
git stash pop
```

如果有冲突，手动解决后执行 `git add <resolved-files> && git stash drop`。

#### Step 5: 验证工作区（必须执行，不可跳过）

```bash
git status
```

确认工作区只包含与当前 issue 相关的文件。意外出现的修改文件用 `git restore <unwanted-file>` 还原。上一步 stash pop 可能带出 lint 工具修改或其他 session 的残留改动。

### 5.2 执行代码修改

按 Step 3 方案中的具体改动逐个修改文件。**注意**：

- 遵循项目 CLAUDE.md 的注释规范和代码风格
- 不添加方案中未列出的改动
- 修改完成后运行 `git status` 确认只改动了预期文件

### 5.3 提交

按 git-workflow Section 2 的 Conventional Commits 格式：

```bash
git add <file1> <file2> ...   # 逐个精确添加
git commit -m "$(cat <<'EOF'
<type>(<scope>): <description>

<body>

Refs #<N>
EOF
)"
```

### 5.4 推送到远程并创建 PR

```bash
git push --set-upstream origin <branch-name>
gh pr create \
  --title "<type>(<scope>): <description>" \
  --body "$(cat <<'EOF'
## Summary
<改动总结>

## Test plan
- [ ] pnpm typecheck
- [ ] pnpm build
EOF
)"
```

### 5.5 记录 PR URL

记下 `gh pr create` 输出的 PR URL，用于 Step 6 的 Issue 评论。

## Step 6: 发布 Issue 结论评论

读取 `references/comment-templates.md`，根据 Step 4 的决策选择对应模板：

- **自动实现** → 模板 A：《AI 自主实现报告》（含自我评估、改动总结、PR 链接）
- **仅评论** → 模板 B：《解决方案》（嵌入完整方案 + 人工处理原因）

### 发布命令

```bash
cat > /tmp/issue-<N>-conclusion.md << 'EOF'
<评论正文>
EOF

gh issue comment <N> --body-file /tmp/issue-<N>-conclusion.md
```

### 发布后

- **自动实现**：告知用户 → Issue URL + PR URL，提醒 review 代码后合并
- **仅评论**：告知用户 → Issue URL，提醒查看方案并决定下一步

### 发布失败时的降级处理

如果 `gh issue comment` 失败，将完整评论正文直接输出，让用户手动粘贴到 GitHub。

## Edge Cases

| 场景 | 处理方式 |
|------|---------|
| Issue 描述的 Scope 不准确 | 分析后纠正，在根因分析中说明实况 |
| 问题不在代码层面（配置/环境/第三方服务） | 明确说明非代码问题，给出运维/配置建议；标记为「仅评论」 |
| 需要跨多个 issue 一起解决 | 标注依赖关系，建议解决顺序；标记为「仅评论」（级联影响大） |
| Issue 为 P0 紧急问题 | 标记为「仅评论」，额外标注修复时间窗口和风险等级，建议最小改动方案 |
| 需要新增第三方依赖 | 标记为「仅评论」，说明新增依赖的理由和影响评估 |
| 已过时（代码已变更） | 告知用户代码状态已变化，issue 可能需要更新或关闭 |
| gh 命令失败（无权限、网络等） | 告知用户失败原因，输出完整内容供手动操作 |
| 自动实现中途失败 | 回滚改动，在 Issue 评论中说明失败原因，附上方案供人工处理 |
| 自我评估处于灰色地带 | **倾向 defer**，标记为「仅评论」，在评论中详细说明模糊点和建议 |

## Self-Audit Checklist

发布前逐项确认：

- [ ] 是否亲自读了 Scope 中列出的所有文件？
- [ ] 是否搜索了关键函数/组件的所有引用方（grep）？
- [ ] 根因分析是否基于代码证据（引用了具体文件:行号）？
- [ ] 方案是否具体到文件路径和修改方式，有无改动前后对比？
- [ ] 验证步骤是否可执行（具体命令或页面路径）？
- [ ] 是否标注了影响范围（直接 + 间接）和风险？
- [ ] 是否已按 complexity-criteria.md 逐项完成自我评估？
- [ ] 若自动实现：建分支是否完整执行了 5 步流程（stash→sync main→branch→pop→status）？
- [ ] 若自动实现：typecheck 和 build 是否已通过？
- [ ] 是否已将结论评论发布到 GitHub Issue？

## 与其他 Skill 的配合

- 配合 `issue-breakdown`：issue-breakdown 负责拆解需求为 issues，issue-resolver 负责逐个解决
- 配合 `code-health-check`：code-health-check 发现的问题可拆解为 issues，再由 issue-resolver 制定方案
- 配合 `git-workflow`：自动实现时引用其分支命名、提交规范、PR 创建流程
