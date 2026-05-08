---
name: markdown-frontmatter-engine
description: 当用户要求为 Markdown 文件添加、修改或提取 frontmatter（属性、元数据、YAML 头），或要求补充 tags、aliases、标题、分类等字段时，必须使用此 skill。它由 schema/ 目录动态驱动——在 schema/ 下新增一个 .md 文件即可支持新的字段类型，全程无需修改 skill 本身。支持对单个文件或目录批量处理。
compatibility: Python 3，python-dotenv（可选，无此依赖时回退到手动解析 .env）
---

# Markdown Frontmatter Engine

深度分析指定 Markdown 文件的内容，结合 `schema/` 目录下预设的动态字段定义，为其提取并更新符合规范的 Frontmatter 元数据。

## 字段来源
`schema/` 目录下的 `.md` 文件对应 frontmatter 字段，文件名即字段名，数字前缀控制输出优先级。

## 工作流

### 前置准备

**步骤 0 — 扫描确认**：
```bash
python3 ./scripts/batch_ops.py scan "笔记目录" --json
```
向用户确认处理范围（有多少文件、多少已有 frontmatter），避免范围不符预期。

**步骤 1 — 读取格式规范**：
读取 `FORMAT.md`，掌握输出格式要求（字段间空一行、2 空格缩进）。

**步骤 2 — 确定字段范围（优先级：对话指定 > .env 配置 > 全量）**：

先用 `--list` 快速枚举 schema 中有哪些可用字段：
```bash
python3 ./scripts/batch_ops.py schema "./schema" --list
```

然后按以下顺序决定本次处理的字段范围：

1. **对话指定**（最高优先）：用户在对话中明确说"只要 title 和 tags"，用对话指定的字段
2. **.env 配置**（对话未指定时）：读取 skill 根目录的 `.env`，若有 `SCHEMA_FIELDS=xxx` 配置则使用：
   ```bash
   python3 ./scripts/batch_ops.py env-fields "./"
   # 输出字段名: title,tags,domain
   # 或输出 (全量) 表示无配置
   ```
   **此步骤不可跳过**。即使后续 `write`/`write-multi` 命令会自动读取 `.env`，此步骤的作用是在写入前让 AI 明确知道本次处理的字段范围，避免分析多余的字段。
3. **全量**：对话未指定且 `.env` 无配置时，读取 schema 目录下所有 `.md` 文件

若对话指定或 `.env` 中的字段在 schema 里找不到，输出警告并只处理已知字段：
```bash
# 若含未知字段，输出: 警告: 以下字段不在 schema 目录中: unknown_field
```

**步骤 3 — 加载选定字段的规则（一次性，缓存）**：
根据步骤 2 的结果决定加载范围：
- **全量**：读取 schema 目录下所有 `.md` 文件
- **部分字段**：只读取用户选定字段对应的 schema 文件

```bash
# 全量模式（步骤 2 未指定字段时）
python3 ./scripts/batch_ops.py schema "./schema"
# -> 返回: [1] title, [2] aliases, [3] tags, [4] source, [5] domain

# 部分字段模式（步骤 2 已指定字段时，直接读取对应文件即可）
# 不需要额外命令，缓存 --fields 过滤后的文件列表，按需读取
```

**步骤 4 — 确定操作范围**：
- 单个文件：`python3 ./scripts/batch_ops.py read "文件路径"`
- 目录：扫描结果即范围
- 文件列表：直接处理

### 批量处理（对操作范围内的每个 .md 文件）

**a. 读取解析**：读取文件内容，解析已有 frontmatter，**只保留不在本次更新范围内的历史字段**。

**b. 语义提取（只处理选定的字段）**：直接使用步骤 3 缓存的 schema 规则（不再读文件），**仅对用户指定或全量模式下的字段进行提取**，未选字段保持原样不动。

**c. 格式化**：按 `FORMAT.md` 规范组装 frontmatter（字段顺序由 schema 文件名数字前缀决定）。

### 收尾写入（一次性批量写入，不逐文件操作）

所有文件分析完毕后，将结果构造为 JSON 数组，用 `write-multi` 一次性写入：

```bash
python3 ./scripts/batch_ops.py write-multi "笔记目录" updates.json --schema-dir "./schema"
```

JSON 格式：
```json
[
  {"path": "file1.md", "title": "...", "tags": ["tutorial", "python"], "aliases": [], "source": "blog", "domain": "Technology"},
  {"path": "file2.md", "title": "...", "tags": ["thought"], "aliases": [], "source": "note", "domain": "Personal"}
]
```

如需单独写入单个文件，使用多字段模式：
```bash
python3 ./scripts/batch_ops.py write "note.md" --json '{"title": "...", "domain": "Technology"}'
```

## 异常处理

**b 步（读规则）**：若 schema 文件解析失败，记录并跳过该字段，继续处理其他字段。

**c 步（语义提取）**：若根据 Schema 规则无法从正文中推断出明确值，保持该字段为空或使用 Schema 中指定的默认值，**禁止随意编造**。

**d 步（写入）**：若写入失败，在报告中标记该文件并说明原因，继续处理其他文件，最后汇总报告。

## 收尾报告

向用户输出执行报告：成功更新的文件数、跳过的文件数、失败文件及原因。

## 脚本工具说明

- **`python3 ./scripts/batch_ops.py scan <dir> [--json]`**：扫描目录下的 .md 文件，`--json` 输出机器可读格式
- **`python3 ./scripts/batch_ops.py read <file_path>`**：读取文件内容和已有 frontmatter
- **`python3 ./scripts/batch_ops.py write <file_path> [--json <json>] [field value]`**：写入字段，`--json` 接受多字段 JSON
- **`python3 ./scripts/batch_ops.py write-multi <dir> <json_path> [--schema-dir <path>]`**：批量写入，`--schema-dir` 提供字段顺序
- **`python3 ./scripts/batch_ops.py schema <schema_dir>`**：扫描字段定义，支持两个轻量枚举选项：
  - `--list`：只列字段名和优先级（不读文件），用于快速了解有哪些可用字段
  - `--fields X,Y`：只返回指定字段的条目（不读文件），用于字段选择时验证和过滤；未知字段会输出警告
- **`python3 ./scripts/batch_ops.py env-fields <skill_root>`**：读取 skill 根目录的 `.env` 中的 `SCHEMA_FIELDS` 配置，输出字段名逗号分隔字符串；无配置时输出 `(全量)`

## 规模化处理

处理超过 50 个文件时，建议分批处理并向用户实时报告进度（如"已处理 25/100 个"），避免单次操作超时。
