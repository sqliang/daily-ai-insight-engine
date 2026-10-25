# Comment conventions（注释规范完整示例）

> 何时读我：在 `pipeline/`（Python）、`src/`（TypeScript/TSX）或 YAML 配置文件中写代码/改代码前必读。根文件 CLAUDE.md 中有 6 条一行式规则摘要，本文是完整示例与细则。

All comments use **Chinese** (Simplified). Code identifiers (variable names, function names, type names) remain English. Comments explain **why** and **how** — design rationale, architectural decisions, data flow direction, and edge cases. Don't write comments that just restate what the code says.

## Python (`pipeline/`)

```python
"""
pipeline/module_name.py — 模块用途简述

说明本模块在管道中的位置（Stage N）、负责什么、被哪些模块消费。
包含：关键设计决策、数据流转方向、异常处理策略。
"""

# ---------------------------------------------------------------------------
# 逻辑分区标题
# ---------------------------------------------------------------------------

def public_function(param: str) -> dict:
    """
    函数用途。

    参数：
        param: 参数说明（含约束条件）

    返回：
        dict: 返回值说明

    异常：
        ValueError: 在什么情况下抛出

    设计理由：
        为什么这样做而不是另一种方式（如涉及非显而易见的取舍）
    """
    ...

class SomeModel(BaseModel):
    """类的用途和设计意图。"""

    field_name: str = Field(
        ...,
        description="字段含义。说明该字段的消费方和用途。",
    )
```

- **每个 `.py` 文件**开头必须有模块级 docstring
- **每个函数**（包括 `_private`）必须有 docstring
- **每个 Pydantic model 和 class** 必须有 docstring
- **每个 Pydantic Field** 必须提供 `description=` 参数
- 用 `# ---` 分隔线划分文件内的逻辑分区
- 行内注释用 `#` 仅在逻辑非显而易见时使用

## TypeScript / TSX (`src/`)

```tsx
// ============================================================================
// component-or-module.tsx — 文件用途简述
//
// 说明本文件的职责、被哪些页面/模块消费、数据流向。
// 涉及非显而易见的决策时解释设计理由。
// ============================================================================

// ---------------------------------------------------------------------------
// 逻辑分区标题
// ---------------------------------------------------------------------------

/**
 * 组件或函数的用途。
 *
 * 描述该组件的职责、使用场景、以及关键的交互行为。
 * 当 props 含义不是一目了然时，说明其作用。
 */
export function MyComponent({ items, onSelect }: Props) {
  // 非显而易见的逻辑需要行内注释说明原因
  const threshold = items.length > 10 ? 0.5 : 0.8;

  return ( ... );
}
```

- **每个 `.ts` / `.tsx` 文件**开头必须有 banner 注释块（`// ====` 分隔），说明文件职责和消费方
- **每个 export 的组件和函数**必须有 JSDoc（`/** ... */`）描述其用途
- 组件 JSDoc 需说明使用场景，props 含义不直观时需额外说明
- 用 `// ---` 分隔线划分文件内的逻辑分区
- 行内注释用 `//` 仅在逻辑非显而易见时使用（为什么取这个阈值、为什么做这个判断）

## YAML 配置文件

```yaml
# ---------------------------------------------------------------------------
# 配置区块标题 — 说明该区块控制什么功能
# ---------------------------------------------------------------------------

# 字段含义说明，尤其是值含义不直观时
key: value  # 行内注释说明该值的特殊含义或选择理由
```

- 每个逻辑区块用 `# ---` 分隔注释标注
- 每个配置项应有行内或上方注释说明含义
- 布尔开关和枚举值必须注释说明每个值的含义
