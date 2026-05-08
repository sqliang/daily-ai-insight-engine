# Markdown Frontmatter Engine

为 Markdown 文件批量提取和更新 frontmatter 元数据，由 AI 语义分析驱动，字段规则完全由 `schema/` 目录定义，无需修改核心代码即可扩展新字段。

---

## 目录结构

```
markdown-frontmatter-engine/
├── SKILL.md          # Skill 定义（Claude 读取的工作流说明）
├── FORMAT.md         # Frontmatter 输出格式规范
├── scripts/
│   └── batch_ops.py  # 文件读写引擎（Python 3，无需依赖）
└── schema/           # 字段定义目录（一个文件 = 一个字段）
    ├── 01.title.md
    ├── 02.aliases.md
    ├── 03.tags.md
    ├── 04.source.md
    └── 05.domain.md
```

---

## 快速开始

### 用户角度：如何触发

当你说这些话时，Claude 会自动使用此 skill：

- "帮我分析 `/xxx/notes/` 下的笔记，补全 frontmatter"
- "给这篇 Markdown 添加 tags 和标题"
- "更新这个文件夹里所有笔记的属性"
- "为这些文件提取 domain 和 source"

### 运行前提

- Python 3
- 无需安装任何依赖（纯标准库）

---

## 工作原理

```
用户请求
    │
    ▼
扫描目录 → 读取 schema/ 所有字段定义（一次性缓存）
    │
    ▼
对每个 .md 文件：
    读取正文内容
    AI 按 schema 规则推断元数据
    收集结果
    │
    ▼
一次性批量写入（write-multi）
```

**核心设计**：字段规则定义在 `schema/` 目录下，新增字段只需添加文件，无需改代码。

---

## 脚本命令参考

```bash
# 扫描目录，查看有哪些 .md 文件
python3 scripts/batch_ops.py scan "笔记目录"
python3 scripts/batch_ops.py scan "笔记目录" --json   # 机器可读格式

# 读取单个文件的内容和现有 frontmatter
python3 scripts/batch_ops.py read "note.md"

# 写入字段（单字段模式）
python3 scripts/batch_ops.py write "note.md" title "Agent 前沿解读"

# 写入字段（多字段模式，推荐）
python3 scripts/batch_ops.py write "note.md" --json '{"title": "...", "domain": "Technology"}'

# 批量写入（处理完所有文件后一次性写入）
python3 scripts/batch_ops.py write-multi "笔记目录" updates.json --schema-dir "./schema"

# 查看当前所有字段定义及优先级
python3 scripts/batch_ops.py schema "./schema"
```

---

## 扩展字段指南

### 新增一个字段

只需两步：

**第一步**：在 `schema/` 下创建一个 `.md` 文件，文件名格式为 `[优先级].字段名.md`。

例如，想新增一个 `status` 字段（表示笔记状态：draft / published），想排在 `source` 之后：

```
# 当前顺序（schema/ 下的文件）
01.title.md
02.aliases.md
03.tags.md
04.source.md   ← 在这之后
05.domain.md

# 重命名 source 以腾出位置
mv 04.source.md 04.status.md
mv 05.domain.md 06.domain.md

# 最终顺序
01.title.md
02.aliases.md
03.tags.md
04.status.md   ← 新字段
05.source.md
06.domain.md
```

**第二步**：在 `schema/04.status.md` 中编写提取规则，参考下方"字段定义规范"。

### 字段定义规范

每个 schema 文件的结构：

```markdown
# 字段名

- 类型：`string | string[] | boolean | ...`
- 说明：描述这个字段的用途

## 提取规则

1. 规则描述...
2. 规则描述...
```

**示例**（参考 `schema/03.tags.md`）：

```markdown
# status

- 类型：`'draft' | 'published' | 'archived'`
- 说明：笔记的发布状态

## 提取规则

1. **强制枚举**：值必须为上述三者之一，不可自行生造。
2. 若正文包含"草稿"或未完成的占位符 → `draft`
3. 若正文有明显发布痕迹（如 URL、署名）→ `published`
4. 其他情况默认 → `draft`
```

### 扩展字段（不想指定顺序）

如果新字段不需要固定顺序，放在最后即可：

```
# 直接创建文件，不加数字前缀
schema/my-custom-field.md

# 它会自动排在所有数字前缀字段之后，按字母顺序
```

---

## Frontmatter 格式规范（FORMAT.md）

所有输出的 frontmatter 严格遵循以下格式：

```yaml
---
title: Agent 前沿解读

aliases:
  - RAG
  - 检索增强生成

tags:
  - tutorial
  - ai

source: blog

domain: Technology
---

<正文内容>
```

**规则**：
- 字段与字段之间空一行
- 列表项缩进 2 空格
- `---` 闭合后空一行再接正文

---

## 维护指南

### 修改现有字段的提取规则

直接在对应的 schema 文件中编辑即可。例如想让 `domain` 字段增加一个新的顶层分类，直接编辑 `schema/05.domain.md`。

### 调整字段输出顺序

通过重命名 schema 文件的数字前缀来调整。例如想把 `tags` 排到 `aliases` 之前：

```bash
mv 02.aliases.md 03.aliases.md
mv 03.tags.md 02.tags.md
```

### 字段合并行为

`tags` 和 `aliases` 是**合并模式**字段：多次写入时，新值会追加到旧值中并去重。其他字段为**覆盖模式**。

---

## 测试验证

修改后建议运行以下测试：

```bash
cd skills/markdown-frontmatter-engine

# 1. 验证 schema 扫描顺序正确
python3 scripts/batch_ops.py schema ./schema

# 2. 验证 parse + build 往返一致性
python3 - << 'EOF'
import sys; sys.path.insert(0, './scripts')
from batch_ops import build_frontmatter, parse_frontmatter

# 无 frontmatter 文件
fm, body = parse_frontmatter("正文内容")
assert fm == {}, f"Expected {{}}, got {fm}"
print("PASS: no-frontmatter file handled")

# 有 frontmatter 文件
content = "---\ntitle: Test\n\naliases:\n  - A\n  - B\n---\n正文"
fm, body = parse_frontmatter(content)
assert fm['aliases'] == ['A', 'B'], f"Expected [A,B], got {fm['aliases']}"
print("PASS: list field parsed correctly")

# 3. 验证字段顺序
order = __import__('batch_ops').get_field_order('./schema')
assert order == ['title', 'aliases', 'tags', 'source', 'domain'], f"Wrong order: {order}"
print("PASS: field order correct")

print("\n所有测试通过！")
EOF
```
