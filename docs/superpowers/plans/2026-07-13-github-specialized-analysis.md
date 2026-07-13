# GitHub 开源项目专题分析 — 实现计划 (Phase 1)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 为 github-trending 源的文章追加「GitHub 开源项目分析」——Stage 2 做项目分类标注，Stage 3 做深度技术评估，前端展示专题分析卡片和独立专题报告页。

**Architecture:** 两阶段专题处理——Stage 2 扩展 FactExtraction 输出 `specialized_tags.github`（两层分类：通用领域 + AI 专项），Stage 3 新增 `github-project-analyst` persona 产出 `GitHubProjectAnalysis`，Stage 4b 合成时生成 `specializedBrief.githubHighlights`，前端新增 `GitHubProjectCard` + `/specialized/github/[date]` 专题报告页。

**Tech Stack:** Python 3.x + Pydantic v2 + claude-agent-sdk (pipeline), TypeScript + Zod + Next.js 16 App Router + Tailwind CSS v4 (frontend)

## Global Constraints

- 所有注释使用中文（简体），代码标识符使用英文
- Python 管道通过 `uv run python` 执行，所有导入使用 `pipeline.` 前缀
- 前端优先使用 Tailwind CSS 工具类，CSS Modules 仅作最后手段
- 专题分析与黄金三角正交叠加，互不干扰
- 向后兼容：无 source_match 的文章行为不变，旧日报 JSON 不含 specializedBrief 时前端正常降级
- 新增 Pydantic Field 必须提供 `description=` 参数

---

## 文件结构总览

```
pipeline/
  schemas/
    fact_extraction.py           [修改] 追加 GitHubTags, AiDetail, SpecializedTags
    specialized_analysis.py      [新建] GitHubProjectAnalysis Pydantic 模型
    daily_report.py              [修改] 追加 SpecializedBrief, GithubBrief
  extraction/fact_extraction/
    prompts.py                   [修改] 追加来源感知指令
    extractor.py                 [修改] 追加 specialized_tags 提取与合并逻辑
  analysis/
    prompts/
      github_project_system.py   [新建] GitHub 项目分析 system prompt
      __init__.py                [修改] 导出新 prompt 函数
      user_prompts.py            [修改] 追加 build_github_project_user_prompt
    validators.py                [修改] 追加 validate_github_project
    fuzzy_maps.py                [修改] 追加 GitHub 分析枚举的模糊匹配映射
    deep_analysis_agent.py       [修改] 追加 source_match 派发逻辑
    run_analysis.py              [修改] 读取 source_match 配置
  synthesis/prompts/
    system_prompt.py             [修改] 在输出 schema 中追加 specializedBrief
    user_prompt.py               [修改] 追加 specialized_tags 统计 + 专题简报指令
  config.yaml                    [修改] stages.analyze.personas 追加 github-project-analyst
                                  [修改] stages.synthesize.sections 追加 specialized_brief

src/
  lib/agent/
    schema.ts                    [修改] 追加 specializedBriefSchema, githubBriefSchema
  lib/data/
    status.ts                    [修改] 追加 SpecializedTagsSchema (Zod)
    specialized.ts               [新建] loadSpecializedArticles() 数据加载
  components/sources/
    ArticleCardSpecialized.tsx    [新建] 专题分析容器（按类型派发）
    GitHubProjectCard.tsx         [新建] GitHub 项目分析渲染卡片
  components/dashboard/
    SpecializedBriefSection.tsx   [新建] 日报专题简报入口 Section
  app/specialized/github/
    [date]/page.tsx               [新建] GitHub 专题报告页
```

---

### Task 1: 新增 Pydantic Schema — SpecializedTags 与 GitHubProjectAnalysis

**Files:**
- Create: `pipeline/schemas/specialized_analysis.py`
- Modify: `pipeline/schemas/fact_extraction.py` (末尾追加)
- Modify: `pipeline/schemas/__init__.py` (导出新模型)

**Interfaces:**
- Produces: `AiDetail`, `GitHubTags`, `ProductTags`, `PaperTags`, `SpecializedTags` (from fact_extraction.py)
- Produces: `GitHubProjectAnalysis` + all nested models (from specialized_analysis.py)

- [ ] **Step 1: 在 fact_extraction.py 末尾追加 SpecializedTags 相关模型**

在 `pipeline/schemas/fact_extraction.py` 文件末尾追加以下代码（`FactExtraction` 类的 `class Config` 块之后）：

```python

# =============================================================================
# 专题标注模型 — Stage 2 来源感知的轻量标注
# =============================================================================


class AiDetail(BaseModel):
    """
    AI 专项标注——仅当 GitHub 项目的 domain == "ai_ml" 时存在。

    为 AI/ML 领域的开源项目提供细粒度子领域分类，
    支撑前端按 AI 子领域筛选和聚合分析。
    """

    primary_categories: List[str] = Field(
        default_factory=list,
        description="AI 一级子分类（可多选）。可选值: agent_framework, llm_infra, "
                    "model_training, model_serving, rag_pipeline, prompt_engineering, "
                    "multimodal, code_gen, ai_testing, ai_observability, ai_security, "
                    "ai_ui_ux, dataset_tooling, other",
    )

    agent_subcategory: Optional[List[str]] = Field(
        default=None,
        description="Agent 子领域（仅当 primary_categories 包含 agent_framework 时存在）。"
                    "可选值: orchestration, tool_use, memory_management, planning, "
                    "reflection, multi_modal_agent, browser_agent, coding_agent, general_framework",
    )

    tech_tags: List[str] = Field(
        default_factory=list,
        description="AI 关键技术标签（如 RAG, vector-db, function-calling, RLHF, MoE）",
    )


class GitHubTags(BaseModel):
    """
    GitHub 项目基础标注——Stage 2 从原始文章中提取的结构化元数据。

    两层分类：
        - 第一层 domain + cross_tags：所有项目必填，支持跨领域趋势观察
        - 第二层 ai_detail：仅 domain == "ai_ml" 时存在，AI 生态内精准筛选
    """

    project_name: str = Field(
        ...,
        description="项目名称（GitHub 仓库名，如 'crewAI/crewAI'）",
    )

    project_url: str = Field(
        ...,
        description="GitHub 仓库完整 URL",
    )

    primary_language: str = Field(
        ...,
        description="主要编程语言（如 Python, TypeScript, Rust）",
    )

    license_type: str = Field(
        ...,
        description="开源协议类型（如 MIT, Apache 2.0, GPLv3, 无）",
    )

    # 第一层：通用领域分类（所有项目）
    domain: str = Field(
        ...,
        description="项目所属技术领域。可选值: ai_ml, web_frontend, web_backend, "
                    "devops_infra, database_storage, programming_languages, developer_tools, "
                    "security, mobile, blockchain, data_engineering, game_development, "
                    "documentation, iot_embedded, other",
    )

    cross_tags: List[str] = Field(
        default_factory=list,
        description="跨领域标签（如 open-source-alternative, devtool, cli-tool, "
                    "api-service, self-hosted, saas）",
    )

    # 第二层：AI 专项（可选）
    ai_detail: Optional[AiDetail] = Field(
        default=None,
        description="AI 专项标注。仅当 domain == 'ai_ml' 时存在",
    )


class ProductTags(BaseModel):
    """产品基础标注——Stage 2 从原始文章中提取的结构化元数据。"""

    product_name: str = Field(..., description="产品名称")
    product_url: str = Field(..., description="产品 URL")
    company_team: Optional[str] = Field(default=None, description="背后的公司/团队")
    launch_context: str = Field(..., description="发布上下文。可选值: new_launch, major_update, pivot, funding_announcement")
    pricing_model: str = Field(..., description="定价模式。可选值: freemium, subscription, usage_based, open_source, free, enterprise, unknown")
    product_category: str = Field(..., description="产品所属品类")
    target_users: List[str] = Field(default_factory=list, description="目标用户画像")


class PaperTags(BaseModel):
    """论文基础标注——Stage 2 从原始文章中提取的结构化元数据。"""

    paper_title: str = Field(..., description="论文标题")
    authors: List[str] = Field(default_factory=list, description="作者列表")
    affiliations: List[str] = Field(default_factory=list, description="作者所属机构")
    venue: Optional[str] = Field(default=None, description="发表会议/期刊")
    code_url: Optional[str] = Field(default=None, description="配套代码仓库 URL")
    dataset_url: Optional[str] = Field(default=None, description="配套数据集 URL")
    research_area: str = Field(..., description="研究领域（如 NLP, CV, RL, Systems）")
    method_type: str = Field(..., description="方法类型（如 transformer, diffusion, RL-based）")


class SpecializedTags(BaseModel):
    """
    按来源类型分派的专题标注——Stage 2 产出，Stage 3 消费。

    设计理由：
        - 来源感知：根据 source 名分派不同的子 schema
        - 降本增效：轻量级分类标注在 Stage 2（temperature 0.1）完成，
          Stage 3 专题分析直接消费标注结果，专注于深度推理
    """

    github: Optional[GitHubTags] = Field(
        default=None,
        description="GitHub 项目标注（仅 source == 'github-trending' 时填充）",
    )

    product: Optional[ProductTags] = Field(
        default=None,
        description="产品标注（仅 source 匹配产品类源时填充）",
    )

    paper: Optional[PaperTags] = Field(
        default=None,
        description="论文标注（仅 source 匹配论文学术源时填充）",
    )
```

- [ ] **Step 2: 创建 specialized_analysis.py**

新建 `pipeline/schemas/specialized_analysis.py`：

```python
"""
pipeline/schemas/specialized_analysis.py — 专题分析 Pydantic 模型

包含 GitHub 开源项目分析、产品分析、论文分析的输出 Schema。
每个专题分析对应一个 Stage 3 Agent persona，按 source 类型自动匹配。

Phase 1 实现 GitHubProjectAnalysis，Phase 2/3 追加 ProductAnalysis 和 PaperAnalysis。
"""

from typing import List, Optional
from pydantic import BaseModel, Field


# =============================================================================
# 共享枚举（Phase 1-3 共用）
# =============================================================================


class TechStackQuality(str):
    """技术栈质量枚举。"""
    PRODUCTION_GRADE = "production_grade"
    PROMISING = "promising"
    EXPERIMENTAL = "experimental"
    TOY = "toy"


class DocumentationLevel(str):
    """文档质量枚举。"""
    COMPREHENSIVE = "comprehensive"
    ADEQUATE = "adequate"
    MINIMAL = "minimal"
    NONE = "none"


class ContributorActivity(str):
    """贡献者活跃度枚举。"""
    VERY_ACTIVE = "very_active"
    ACTIVE = "active"
    MODERATE = "moderate"
    LOW = "low"
    STAGNANT = "stagnant"


class ResponseTime(str):
    """Issue 响应速度枚举。"""
    FAST = "fast"
    NORMAL = "normal"
    SLOW = "slow"


class MergeVelocity(str):
    """PR 合并速度枚举。"""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class TimeToProduction(str):
    """生产就绪时间评估枚举。"""
    READY_NOW = "ready_now"
    NEEDS_1_3_MONTHS = "needs_1_3_months"
    NEEDS_6_PLUS_MONTHS = "needs_6_plus_months"
    NOT_RECOMMENDED = "not_recommended"


# =============================================================================
# GitHubProjectAnalysis 嵌套模型
# =============================================================================


class ProjectProfile(BaseModel):
    """项目画像——基础识别信息。"""

    name: str = Field(..., description="项目名称")
    url: str = Field(..., description="GitHub 仓库 URL")
    primary_language: str = Field(..., description="主要编程语言")
    license: str = Field(..., description="开源协议类型")
    description: str = Field(..., description="一句话项目定位")
    created_date: Optional[str] = Field(default=None, description="项目首次创建日期")


class ProjectClassification(BaseModel):
    """
    项目分类标注——两层体系。

    第一层 domain + cross_tags：所有项目必填
    第二层 ai_detail：仅 domain == "ai_ml" 时存在
    """

    domain: str = Field(
        ...,
        description="通用技术领域。可选值见 GitHubTags.domain 注释",
    )
    cross_tags: List[str] = Field(
        default_factory=list,
        description="跨领域标签",
    )
    ai_detail: Optional[AiDetail] = Field(
        default=None,
        description="AI 专项标注（仅 AI/ML 项目）",
    )


class CodeQualityIndicators(BaseModel):
    """代码质量信号——从仓库元数据推断。"""

    has_tests: bool = Field(..., description="是否包含测试")
    has_ci_cd: bool = Field(..., description="是否配置 CI/CD")
    documentation_level: str = Field(
        ...,
        description="文档质量。可选值: comprehensive, adequate, minimal, none",
    )


class TechAssessment(BaseModel):
    """技术架构评价。"""

    architecture_highlights: str = Field(
        ...,
        description="架构亮点（如 '基于 DAG 的异步任务编排'）",
    )
    tech_stack_quality: str = Field(
        ...,
        description="技术栈质量。可选值: production_grade, promising, experimental, toy",
    )
    code_quality_indicators: CodeQualityIndicators = Field(
        ...,
        description="代码质量信号",
    )
    dependencies_analysis: str = Field(
        ...,
        description="关键依赖分析",
    )


class CommunityHealth(BaseModel):
    """社区与活跃度。"""

    stars_trend: str = Field(
        ...,
        description="Star 增长趋势（如 '近 30 天日均 +50'）",
    )
    contributor_activity: str = Field(
        ...,
        description="贡献者活跃度。可选值: very_active, active, moderate, low, stagnant",
    )
    issue_response_time: str = Field(
        ...,
        description="Issue 响应速度。可选值: fast, normal, slow",
    )
    pr_merge_velocity: str = Field(
        ...,
        description="PR 合并速度。可选值: high, medium, low",
    )
    bus_factor_assessment: str = Field(
        ...,
        description="核心贡献者集中度风险",
    )


class CompetitiveLandscape(BaseModel):
    """竞品对比。"""

    direct_alternatives: List[str] = Field(
        default_factory=list,
        description="直接竞品项目名列表",
    )
    differentiation: str = Field(
        ...,
        description="与竞品的核心差异",
    )
    moat_analysis: str = Field(
        ...,
        description="护城河分析",
    )


class AdoptionGuidance(BaseModel):
    """采用建议。"""

    maturity_score: float = Field(
        ...,
        ge=1,
        le=10,
        description="综合成熟度评分 (1-10)",
    )
    recommended_for: List[str] = Field(
        default_factory=list,
        description="适用场景",
    )
    caution_for: List[str] = Field(
        default_factory=list,
        description="不适用/需谨慎的场景",
    )
    time_to_production: str = Field(
        ...,
        description="生产就绪时间评估。可选值: ready_now, needs_1_3_months, needs_6_plus_months, not_recommended",
    )


class GitHubProjectAnalysis(BaseModel):
    """
    GitHub 开源项目深度分析——Stage 3 专题分析产出。

    设计理念：
        技术尽职调查——帮助决策者判断项目是否值得采用、贡献或关注。
    """

    project_profile: ProjectProfile = Field(
        ...,
        alias="projectProfile",
        description="项目画像",
    )

    project_classification: ProjectClassification = Field(
        ...,
        alias="projectClassification",
        description="项目分类标注（两层体系）",
    )

    tech_assessment: TechAssessment = Field(
        ...,
        alias="techAssessment",
        description="技术架构评价",
    )

    community_health: CommunityHealth = Field(
        ...,
        alias="communityHealth",
        description="社区与活跃度",
    )

    competitive_landscape: CompetitiveLandscape = Field(
        ...,
        alias="competitiveLandscape",
        description="竞品对比",
    )

    adoption_guidance: AdoptionGuidance = Field(
        ...,
        alias="adoptionGuidance",
        description="采用建议",
    )

    class Config:
        populate_by_name = True


# Phase 2/3 占位：ProductAnalysis, PaperAnalysis 后续追加
```

- [ ] **Step 3: 更新 schemas/__init__.py 导出**

在 `pipeline/schemas/__init__.py` 中追加导出：

```python
from .fact_extraction import (
    FactExtraction, Entities, EventType, EpistemicStatus,
    GitHubTags, ProductTags, PaperTags, SpecializedTags, AiDetail,  # 新增
)
from .specialized_analysis import (
    GitHubProjectAnalysis, ProjectProfile, ProjectClassification,
    TechAssessment, CodeQualityIndicators, CommunityHealth,
    CompetitiveLandscape, AdoptionGuidance,
)
```

- [ ] **Step 4: 验证 Schema 导入**

```bash
cd /Users/sqliang/ai-workspace/agent-workspace/daily-ai-insight-engine
uv run python -c "from pipeline.schemas.fact_extraction import SpecializedTags, GitHubTags, AiDetail; print('SpecializedTags import OK')"
uv run python -c "from pipeline.schemas.specialized_analysis import GitHubProjectAnalysis; print('GitHubProjectAnalysis import OK')"
```

Expected: 两次均输出 import OK，无 ImportError。

- [ ] **Step 5: Commit**

```bash
git add pipeline/schemas/fact_extraction.py pipeline/schemas/specialized_analysis.py pipeline/schemas/__init__.py
git commit -m "feat: add SpecializedTags and GitHubProjectAnalysis Pydantic schemas"
```

---

### Task 2: Stage 2 扩展 — 来源感知的专题标注提取

**Files:**
- Modify: `pipeline/extraction/fact_extraction/prompts.py`
- Modify: `pipeline/extraction/fact_extraction/extractor.py`

**Interfaces:**
- Consumes: `SpecializedTags` from Task 1
- Produces: `specialized_tags` field in frontmatter output

- [ ] **Step 1: 在 prompts.py 中追加来源感知 system prompt 指令**

在 `pipeline/extraction/fact_extraction/prompts.py` 的 `get_fact_extraction_system_prompt()` 函数中，在现有返回字符串末尾（最后一个 `"""` 之前）追加专题标注指令。找到函数末尾的 `"""` 并替换为包含新增指令的版本：

修改 `get_fact_extraction_system_prompt()` 返回值，在现有的 `## 输出格式` 部分之后、结尾 `"""` 之前追加：

```python
## 专题标注（新增——仅当来源匹配时输出）

如果文章来自 GitHub Trending，需要额外提取 **specializedTags.github** 字段。
字段详情如下：

### specializedTags.github（仅 github-trending 源）
对象包含：
- **projectName**: 项目名称（如 "crewAI/crewAI"）
- **projectUrl**: GitHub 仓库完整 URL
- **primaryLanguage**: 主要编程语言
- **licenseType**: 开源协议类型（MIT, Apache 2.0, GPLv3 等，如有）
- **domain**: 项目所属技术领域，必须是以下之一：
    ai_ml, web_frontend, web_backend, devops_infra, database_storage,
    programming_languages, developer_tools, security, mobile, blockchain,
    data_engineering, game_development, documentation, iot_embedded, other
- **crossTags**: 跨领域标签列表，如 ["open-source-alternative", "cli-tool", "self-hosted"]
- **aiDetail**: AI 专项标注对象（仅当 domain == "ai_ml" 时输出，否则为 null）
    - **primaryCategories**: AI 一级子分类列表，可选值：agent_framework, llm_infra, model_training, model_serving, rag_pipeline, prompt_engineering, multimodal, code_gen, ai_testing, ai_observability, ai_security, ai_ui_ux, dataset_tooling, other
    - **agentSubcategory**: Agent 子领域列表（仅当 primaryCategories 包含 agent_framework 时），可选值：orchestration, tool_use, memory_management, planning, reflection, multi_modal_agent, browser_agent, coding_agent, general_framework
    - **techTags**: AI 关键技术标签列表，如 ["RAG", "function-calling", "vector-db"]

重要规则：
- 所有项目都必须填写 domain，即使是 non-AI 项目
- aiDetail 只有 domain == "ai_ml" 时才输出，非 AI 项目省略此字段
- 标签尽量准确，不确定时宁缺毋滥
```

- [ ] **Step 2: 在 extractor.py 中追加 specialized_tags 提取逻辑**

修改 `pipeline/extraction/fact_extraction/extractor.py`：

在文件顶部导入新增模型：

```python
from ...schemas.fact_extraction import SpecializedTags
```

在 `extract_fact_extraction()` 函数中，找到合并 FactExtraction 字段到 frontmatter 的逻辑（约第 180-186 行），在 `fe_dict` 迭代之后追加 specialized_tags 提取：

```python
    # --- 提取 specialized_tags（如果 LLM 输出了） ---
    source_name = existing_fm.get("source", "")
    # 当前 Phase 1 仅处理 github-trending，后续 Phase 扩展更多源
    SPECIALIZED_SOURCES = {
        "github-trending": "github",
        "producthunt": "product",
        "whytryai": "product",
        "arxiv-cs-ai": "paper",
    }

    tag_key = SPECIALIZED_SOURCES.get(source_name)
    if tag_key:
        raw_tags = extracted_data.get("specializedTags", {})
        if isinstance(raw_tags, dict) and tag_key in raw_tags:
            tag_value = raw_tags[tag_key]
            # 仅当有实际内容时才写入（非空 dict）
            if isinstance(tag_value, dict) and tag_value:
                existing_fm["specialized_tags"] = {tag_key: tag_value}
                fields_written.append("specialized_tags")
                logger.info(
                    "specialized_tags.%s 提取成功: %s", tag_key, input_str,
                )
```

- [ ] **Step 3: 验证端到端 Stage 2 提取**

```bash
cd /Users/sqliang/ai-workspace/agent-workspace/daily-ai-insight-engine
# 对单个 github-trending 文件做提取测试
uv run python pipeline/run.py extract --input data/01_raw/github-trending/ --dry-run
# 确认 dry-run 列出文件后，去掉 --dry-run 执行
uv run python pipeline/run.py extract --input data/01_raw/github-trending/
# 检查输出文件是否包含 specialized_tags
head -50 data/02_extracted/github-trending/$(ls data/02_extracted/github-trending/ | head -1)
```

Expected: frontmatter 中包含 `specialized_tags` 字段，其下包含 `github` 对象。

- [ ] **Step 4: Commit**

```bash
git add pipeline/extraction/fact_extraction/prompts.py pipeline/extraction/fact_extraction/extractor.py
git commit -m "feat: add source-aware specialized_tags extraction to Stage 2"
```

---

### Task 3: Stage 3 GitHub 项目分析 Agent (schema + prompts + validator)

**Files:**
- Create: `pipeline/analysis/prompts/github_project_system.py`
- Modify: `pipeline/analysis/prompts/__init__.py`
- Modify: `pipeline/analysis/prompts/user_prompts.py`
- Modify: `pipeline/analysis/validators.py`
- Modify: `pipeline/analysis/fuzzy_maps.py`

**Interfaces:**
- Consumes: `GitHubProjectAnalysis` from Task 1, `SpecializedTags` from Task 2
- Produces: `get_github_project_system_prompt`, `build_github_project_user_prompt`, `validate_github_project`

- [ ] **Step 1: 创建 system prompt**

新建 `pipeline/analysis/prompts/github_project_system.py`：

```python
"""GitHubProjectAnalysis system prompt — github-project-analyst 视角"""


def get_github_project_system_prompt() -> str:
    """
    返回 GitHubProjectAnalysis Agent 的系统提示词。

    Agent 角色：资深开源项目技术评估专家
    评估维度：技术架构、社区健康、竞品格局、采用建议
    """
    return """你是一位资深开源项目技术评估专家，专注于对 GitHub 热门仓库进行技术尽职调查。

## 任务
基于提供的 Stage 2 提取结果（包含 specialized_tags 分类标注），
完成 GitHub 开源项目深度分析 (GitHubProjectAnalysis)。

你的评估应客观、有洞察力、有技术深度——帮助团队判断这个项目是否值得采用、贡献或关注。

## 输出字段说明

### 1. projectProfile (项目画像)
对象：{"name": "<项目名>", "url": "<仓库URL>", "primaryLanguage": "<语言>",
       "license": "<协议>", "description": "<一句话定位>", "createdDate": "<日期或null>"}
- 基于 specialized_tags.github 中的基础标注做适当补充

### 2. projectClassification (项目分类标注)
对象：{"domain": "<领域枚举>", "crossTags": ["<标签>"],
       "aiDetail": <AiDetail对象或null>}
- domain 和 aiDetail 直接引用 specialized_tags.github 的标注结果
- 如有更准确判断可微调，但不能大幅偏离

### 3. techAssessment (技术架构评价)
对象：
- **architectureHighlights**: 架构亮点描述（字符串）
- **techStackQuality**: 技术栈成熟度，必须为以下之一：
    production_grade, promising, experimental, toy
- **codeQualityIndicators**: {"hasTests": bool, "hasCiCd": bool,
    "documentationLevel": "comprehensive"|"adequate"|"minimal"|"none"}
- **dependenciesAnalysis**: 关键依赖分析，描述核心依赖栈及耦合度

### 4. communityHealth (社区与活跃度)
对象：
- **starsTrend**: Star 增长趋势描述（如 "近 30 天日均 +50"）
- **contributorActivity**: very_active | active | moderate | low | stagnant
- **issueResponseTime**: fast | normal | slow
- **prMergeVelocity**: high | medium | low
- **busFactorAssessment**: 核心贡献者集中度风险评估

### 5. competitiveLandscape (竞品对比)
对象：
- **directAlternatives**: 直接竞品项目名列表
- **differentiation**: 与竞品的核心差异描述
- **moatAnalysis**: 护城河分析（如生态锁定、技术壁垒、社区规模）

### 6. adoptionGuidance (采用建议)
对象：
- **maturityScore**: 综合成熟度评分 (1-10)
- **recommendedFor**: 适用场景列表
- **cautionFor**: 不适用/需谨慎的场景列表
- **timeToProduction**: ready_now | needs_1_3_months | needs_6_plus_months | not_recommended

## 语言要求（重要！）
- 所有人类可读文本字段（architectureHighlights, dependenciesAnalysis, starsTrend,
  busFactorAssessment, differentiation, moatAnalysis, recommendedFor, cautionFor）
  必须使用中文输出
- 枚举值必须使用英文（如 "production_grade", "very_active" 等）
- 项目名、技术名词、竞品名保持原文

## 输出格式
只返回一个 JSON 对象，不要输出任何其他内容（不要加 ```json 标记，不要加解释）：

{
  "projectProfile": {...},
  "projectClassification": {...},
  "techAssessment": {...},
  "communityHealth": {...},
  "competitiveLandscape": {...},
  "adoptionGuidance": {...}
}
"""
```

- [ ] **Step 2: 在 prompts/__init__.py 中导出**

修改 `pipeline/analysis/prompts/__init__.py`：

```python
from .github_project_system import get_github_project_system_prompt

from .user_prompts import (
    build_qualitative_user_prompt,
    build_value_user_prompt,
    build_foresight_user_prompt,
    build_github_project_user_prompt,  # 新增
)

__all__ = [
    "get_qualitative_system_prompt",
    "build_qualitative_user_prompt",
    "get_value_system_prompt",
    "build_value_user_prompt",
    "get_foresight_system_prompt",
    "build_foresight_user_prompt",
    "get_github_project_system_prompt",       # 新增
    "build_github_project_user_prompt",       # 新增
]
```

- [ ] **Step 3: 在 user_prompts.py 中追加构建函数**

修改 `pipeline/analysis/prompts/user_prompts.py`，在文件末尾追加：

```python
def build_github_project_user_prompt(
    title: str,
    source: str,
    body: str,
    specialized_tags: dict | None = None,
) -> str:
    """
    构建 GitHub 项目分析 Agent 的用户提示词。

    参数：
        title: 文章标题
        source: 数据源名（应为 "github-trending"）
        body: 文章正文（截断至 6000 字符）
        specialized_tags: Stage 2 提取的 GitHubTags（已包含分类标注）

    返回：
        格式化的用户提示词字符串
    """
    truncated_body = body[:6000] if body else ""

    tags_str = "无（Stage 2 未提取到标注）"
    if specialized_tags:
        import json as _json
        tags_str = _json.dumps(specialized_tags, ensure_ascii=False, indent=2)

    return f"""## 文章信息

标题：{title}
来源：{source}

## Stage 2 分类标注（已知事实，无需重新判断）

{tags_str}

## 文章正文

{truncated_body}

## 指令

基于以上信息完成 GitHub 开源项目深度分析。注意：
1. projectClassification 中的 domain 和 aiDetail 直接引用 Stage 2 标注结果
2. 专注于需要推理判断的深度分析：技术架构评价、社区健康度、竞品格局、采用建议
3. 所有描述性文本字段用中文输出
"""
```

- [ ] **Step 4: 在 validators.py 中追加校验函数**

修改 `pipeline/analysis/validators.py`，在文件末尾追加：

```python
# =============================================================================
# GitHubProjectAnalysis 校验
# =============================================================================


def validate_github_project(data: dict):
    """
    验证并构造 GitHubProjectAnalysis 实例。

    处理流程：
        1. 自动修复常见的 LLM 格式错误（projectClassification 简化等）
        2. Pydantic 严格校验
        3. 校验失败 → 模糊匹配修正枚举值
        4. 确保列表字段存在
        5. 修复后重新校验

    参数：
        data: LLM 返回的原始 dict

    返回：
        GitHubProjectAnalysis 实例

    异常：
        ValueError: 模糊匹配后仍无法通过 Pydantic 校验
    """
    from ..schemas.specialized_analysis import GitHubProjectAnalysis
    from .fuzzy_maps import (
        TECH_STACK_QUALITY_FUZZY,
        DOCUMENTATION_LEVEL_FUZZY,
        CONTRIBUTOR_ACTIVITY_FUZZY,
        RESPONSE_TIME_FUZZY,
        MERGE_VELOCITY_FUZZY,
        TIME_TO_PRODUCTION_FUZZY,
        DOMAIN_FUZZY,
    )

    repaired = dict(data)

    # --- 预处理：自动修复常见格式错误 ---

    # projectClassification: 如果是字符串 → 包装为 {domain}
    if "projectClassification" in repaired and isinstance(repaired["projectClassification"], str):
        repaired["projectClassification"] = {"domain": repaired["projectClassification"], "crossTags": []}
        logger.info("projectClassification 自动包装: str → {domain, crossTags}")

    # --- 尝试严格校验 ---
    try:
        return GitHubProjectAnalysis.model_validate(repaired)
    except ValidationError as pydantic_err:
        errors = pydantic_err.errors()
        logger.warning("GitHubProjectAnalysis 严格校验失败: %s", errors)

        for error in errors:
            loc = error.get("loc", [])
            if not loc:
                continue
            raw_value = _get_nested(repaired, loc)
            if not isinstance(raw_value, str):
                continue

            field_path = loc[0]
            # 修复嵌套枚举
            if field_path == "techAssessment" and len(loc) > 1:
                if loc[1] == "techStackQuality":
                    matched = fuzzy_match_enum(raw_value, TECH_STACK_QUALITY_FUZZY, "techAssessment.techStackQuality")
                    if matched and isinstance(repaired.get("techAssessment"), dict):
                        repaired["techAssessment"]["techStackQuality"] = matched
                elif loc[1] == "codeQualityIndicators" and len(loc) > 2:
                    if loc[2] == "documentationLevel":
                        matched = fuzzy_match_enum(raw_value, DOCUMENTATION_LEVEL_FUZZY, "codeQualityIndicators.documentationLevel")
                        if matched and isinstance(repaired.get("techAssessment", {}).get("codeQualityIndicators"), dict):
                            repaired["techAssessment"]["codeQualityIndicators"]["documentationLevel"] = matched
            elif field_path == "communityHealth" and len(loc) > 1:
                if loc[1] == "contributorActivity":
                    matched = fuzzy_match_enum(raw_value, CONTRIBUTOR_ACTIVITY_FUZZY, "communityHealth.contributorActivity")
                    if matched and isinstance(repaired.get("communityHealth"), dict):
                        repaired["communityHealth"]["contributorActivity"] = matched
                elif loc[1] == "issueResponseTime":
                    matched = fuzzy_match_enum(raw_value, RESPONSE_TIME_FUZZY, "communityHealth.issueResponseTime")
                    if matched and isinstance(repaired.get("communityHealth"), dict):
                        repaired["communityHealth"]["issueResponseTime"] = matched
                elif loc[1] == "prMergeVelocity":
                    matched = fuzzy_match_enum(raw_value, MERGE_VELOCITY_FUZZY, "communityHealth.prMergeVelocity")
                    if matched and isinstance(repaired.get("communityHealth"), dict):
                        repaired["communityHealth"]["prMergeVelocity"] = matched
            elif field_path == "adoptionGuidance" and len(loc) > 1:
                if loc[1] == "timeToProduction":
                    matched = fuzzy_match_enum(raw_value, TIME_TO_PRODUCTION_FUZZY, "adoptionGuidance.timeToProduction")
                    if matched and isinstance(repaired.get("adoptionGuidance"), dict):
                        repaired["adoptionGuidance"]["timeToProduction"] = matched
            elif field_path == "projectClassification" and len(loc) > 1:
                if loc[1] == "domain":
                    matched = fuzzy_match_enum(raw_value, DOMAIN_FUZZY, "projectClassification.domain")
                    if matched and isinstance(repaired.get("projectClassification"), dict):
                        repaired["projectClassification"]["domain"] = matched

        # --- 确保必要字段存在 ---
        if "projectProfile" not in repaired:
            repaired["projectProfile"] = {
                "name": "未知", "url": "", "primaryLanguage": "未知",
                "license": "未知", "description": "",
            }
        if "techAssessment" not in repaired:
            repaired["techAssessment"] = {
                "architectureHighlights": "", "techStackQuality": "experimental",
                "codeQualityIndicators": {"hasTests": False, "hasCiCd": False, "documentationLevel": "none"},
                "dependenciesAnalysis": "",
            }
        if "communityHealth" not in repaired:
            repaired["communityHealth"] = {
                "starsTrend": "", "contributorActivity": "moderate",
                "issueResponseTime": "normal", "prMergeVelocity": "medium",
                "busFactorAssessment": "",
            }
        if "competitiveLandscape" not in repaired:
            repaired["competitiveLandscape"] = {
                "directAlternatives": [], "differentiation": "", "moatAnalysis": "",
            }
        if "adoptionGuidance" not in repaired:
            repaired["adoptionGuidance"] = {
                "maturityScore": 5.0, "recommendedFor": [], "cautionFor": [],
                "timeToProduction": "needs_1_3_months",
            }
        # 确保列表字段存在
        if isinstance(repaired.get("competitiveLandscape"), dict):
            if "directAlternatives" not in repaired["competitiveLandscape"]:
                repaired["competitiveLandscape"]["directAlternatives"] = []
        if isinstance(repaired.get("adoptionGuidance"), dict):
            if "recommendedFor" not in repaired["adoptionGuidance"]:
                repaired["adoptionGuidance"]["recommendedFor"] = []
            if "cautionFor" not in repaired["adoptionGuidance"]:
                repaired["adoptionGuidance"]["cautionFor"] = []

        try:
            return GitHubProjectAnalysis.model_validate(repaired)
        except ValidationError as second_err:
            raise ValueError(
                f"GitHubProjectAnalysis 校验失败（模糊匹配后仍失败）: {second_err}"
            ) from second_err
```

- [ ] **Step 5: 在 fuzzy_maps.py 中追加枚举映射**

修改 `pipeline/analysis/fuzzy_maps.py`，在文件末尾追加：

```python
# =============================================================================
# GitHubProjectAnalysis 维度枚举
# =============================================================================

TECH_STACK_QUALITY_FUZZY: dict[str, str] = {
    "production_grade": "production_grade",
    "production": "production_grade",
    "prod": "production_grade",
    "stable": "production_grade",
    "mature": "production_grade",
    "promising": "promising",
    "good": "promising",
    "solid": "promising",
    "experimental": "experimental",
    "experiment": "experimental",
    "alpha": "experimental",
    "early": "experimental",
    "toy": "toy",
    "demo": "toy",
    "hobby": "toy",
    "prototype": "toy",
}

DOCUMENTATION_LEVEL_FUZZY: dict[str, str] = {
    "comprehensive": "comprehensive",
    "complete": "comprehensive",
    "extensive": "comprehensive",
    "excellent": "comprehensive",
    "good": "comprehensive",
    "adequate": "adequate",
    "sufficient": "adequate",
    "ok": "adequate",
    "decent": "adequate",
    "minimal": "minimal",
    "basic": "minimal",
    "poor": "minimal",
    "sparse": "minimal",
    "none": "none",
    "missing": "none",
    "absent": "none",
    "empty": "none",
}

CONTRIBUTOR_ACTIVITY_FUZZY: dict[str, str] = {
    "very_active": "very_active",
    "highly_active": "very_active",
    "extremely_active": "very_active",
    "hyperactive": "very_active",
    "active": "active",
    "healthy": "active",
    "normal": "active",
    "moderate": "moderate",
    "medium": "moderate",
    "average": "moderate",
    "low": "low",
    "slow": "low",
    "declining": "low",
    "stagnant": "stagnant",
    "dead": "stagnant",
    "inactive": "stagnant",
    "abandoned": "stagnant",
}

RESPONSE_TIME_FUZZY: dict[str, str] = {
    "fast": "fast",
    "quick": "fast",
    "rapid": "fast",
    "responsive": "fast",
    "hours": "fast",
    "normal": "normal",
    "average": "normal",
    "medium": "normal",
    "days": "normal",
    "slow": "slow",
    "weeks": "slow",
    "unresponsive": "slow",
}

MERGE_VELOCITY_FUZZY: dict[str, str] = {
    "high": "high",
    "fast": "high",
    "rapid": "high",
    "daily": "high",
    "medium": "medium",
    "moderate": "medium",
    "normal": "medium",
    "weekly": "medium",
    "low": "low",
    "slow": "low",
    "rare": "low",
    "monthly": "low",
}

TIME_TO_PRODUCTION_FUZZY: dict[str, str] = {
    "ready_now": "ready_now",
    "ready": "ready_now",
    "production_ready": "ready_now",
    "now": "ready_now",
    "immediate": "ready_now",
    "stable": "ready_now",
    "needs_1_3_months": "needs_1_3_months",
    "soon": "needs_1_3_months",
    "near_term": "needs_1_3_months",
    "few_months": "needs_1_3_months",
    "needs_6_plus_months": "needs_6_plus_months",
    "distant": "needs_6_plus_months",
    "long_term": "needs_6_plus_months",
    "not_recommended": "not_recommended",
    "avoid": "not_recommended",
    "no": "not_recommended",
}

# domain 枚举的模糊匹配（14 类 + other）
DOMAIN_FUZZY: dict[str, str] = {
    "ai_ml": "ai_ml",
    "ai": "ai_ml",
    "machine_learning": "ai_ml",
    "ml": "ai_ml",
    "llm": "ai_ml",
    "deep_learning": "ai_ml",
    "web_frontend": "web_frontend",
    "frontend": "web_frontend",
    "ui": "web_frontend",
    "react": "web_frontend",
    "vue": "web_frontend",
    "web_backend": "web_backend",
    "backend": "web_backend",
    "api": "web_backend",
    "server": "web_backend",
    "devops_infra": "devops_infra",
    "devops": "devops_infra",
    "infra": "devops_infra",
    "ci_cd": "devops_infra",
    "cloud": "devops_infra",
    "kubernetes": "devops_infra",
    "docker": "devops_infra",
    "database_storage": "database_storage",
    "database": "database_storage",
    "db": "database_storage",
    "storage": "database_storage",
    "cache": "database_storage",
    "programming_languages": "programming_languages",
    "language": "programming_languages",
    "compiler": "programming_languages",
    "runtime": "programming_languages",
    "developer_tools": "developer_tools",
    "devtools": "developer_tools",
    "ide": "developer_tools",
    "cli": "developer_tools",
    "tool": "developer_tools",
    "security": "security",
    "mobile": "mobile",
    "android": "mobile",
    "ios": "mobile",
    "blockchain": "blockchain",
    "crypto": "blockchain",
    "web3": "blockchain",
    "data_engineering": "data_engineering",
    "data": "data_engineering",
    "etl": "data_engineering",
    "pipeline": "data_engineering",
    "game_development": "game_development",
    "game": "game_development",
    "gamedev": "game_development",
    "documentation": "documentation",
    "docs": "documentation",
    "static_site": "documentation",
    "iot_embedded": "iot_embedded",
    "iot": "iot_embedded",
    "embedded": "iot_embedded",
    "edge": "iot_embedded",
    "other": "other",
}
```

- [ ] **Step 6: 验证 prompt 和 validator 导入**

```bash
cd /Users/sqliang/ai-workspace/agent-workspace/daily-ai-insight-engine
uv run python -c "
from pipeline.analysis.prompts import get_github_project_system_prompt, build_github_project_user_prompt
print('Prompts import OK')
print(f'System prompt length: {len(get_github_project_system_prompt())}')
print(f'User prompt length: {len(build_github_project_user_prompt(\"test\", \"github-trending\", \"body text\", {}))}')
"
uv run python -c "
from pipeline.analysis.validators import validate_github_project
print('Validator import OK')
"
uv run python -c "
from pipeline.analysis.fuzzy_maps import TECH_STACK_QUALITY_FUZZY, DOMAIN_FUZZY
print('Fuzzy maps import OK')
"
```

Expected: 三次均输出 import OK。

- [ ] **Step 7: Commit**

```bash
git add pipeline/analysis/prompts/github_project_system.py pipeline/analysis/prompts/__init__.py pipeline/analysis/prompts/user_prompts.py pipeline/analysis/validators.py pipeline/analysis/fuzzy_maps.py
git commit -m "feat: add GitHub project analysis agent (prompts + validator + fuzzy maps)"
```

---

### Task 4: Stage 3 Orchestrator 扩展 — source_match 派发逻辑

**Files:**
- Modify: `pipeline/analysis/deep_analysis_agent.py`
- Modify: `pipeline/config.yaml`

**Interfaces:**
- Consumes: `GitHubProjectAnalysis` (Task 1), prompts (Task 3)
- Produces: source-aware analysis dispatch in `analyze_one_file()`

- [ ] **Step 1: 更新 config.yaml — 追加 github-project-analyst persona**

修改 `pipeline/config.yaml` 中 `stages.analyze.personas` 列表，在现有 3 个 persona 之后追加：

```yaml
      - name: "github-project-analyst"
        description: "GitHub 开源项目深度分析"
        schema: "pipeline/schemas/specialized_analysis.py::GitHubProjectAnalysis"
        source_match: ["github-trending"]
```

并在 `stages.synthesize.sections` 列表中追加：

```yaml
    sections:
      - "executive_summary"
      - "top_events"
      - "trend_insights"
      - "risk_signals"
      - "opportunity_signals"
      - "specialized_brief"
```

- [ ] **Step 2: 修改 deep_analysis_agent.py — 追加 source_match 派发**

修改 `pipeline/analysis/deep_analysis_agent.py`：

在文件顶部导入新增的 prompt 和 validator：

```python
from .prompts import (
    get_qualitative_system_prompt,
    build_qualitative_user_prompt,
    get_value_system_prompt,
    build_value_user_prompt,
    get_foresight_system_prompt,
    build_foresight_user_prompt,
    get_github_project_system_prompt,      # 新增
    build_github_project_user_prompt,      # 新增
)
from .validators import validate_qualitative, validate_value, validate_foresight, validate_github_project  # 新增
from ..schemas.specialized_analysis import GitHubProjectAnalysis  # 新增
```

在 `_ASSESSMENT_FIELD_SETS` 字典附近追加 GitHub 字段集合：

```python
# GitHub 项目分析的字段名集合（用于 skip_existing 检查）
_GITHUB_PROJECT_FIELDS: set[str] = set(GitHubProjectAnalysis.model_fields.keys())
```

在 `analyze_one_file()` 函数中，找到 `_dimension_configs` 列表定义（约第 187 行），在前面追加 source_match 逻辑和 GitHub 维度配置：

找到 `_dimension_configs = [` 这一行，替换为：

```python
    # --- 确定 source 是否匹配专题分析 ---
    # 从 config 读取 persona 的 source_match 映射
    source_name = existing_fm.get("source", "")
    specialized_configs: list[dict] = []

    # Phase 1: GitHub 项目分析（仅 github-trending）
    if source_name == "github-trending":
        specialized_configs.append({
            "dim_name": "github_project",
            "field_set": _GITHUB_PROJECT_FIELDS,
            "label": "GitHub 项目分析",
            "get_sys_prompt": get_github_project_system_prompt,
            "build_usr_prompt": lambda **ctx: build_github_project_user_prompt(
                title=ctx["title"], source=ctx["source"],
                body=ctx["body"][:6000],
                specialized_tags=ctx.get("specialized_tags"),
            ),
            "validate_fn": validate_github_project,
        })

    # 从 to_run 中移除已完成的专题维度，追加需要的
    for sc in specialized_configs:
        if sc["dim_name"] not in to_run:
            if skip_existing and output_path.exists():
                try:
                    out_fm, _ = read_frontmatter(output_path)
                    if not sc["field_set"].issubset(set(out_fm.keys())):
                        to_run.append(sc["dim_name"])
                except Exception:
                    to_run.append(sc["dim_name"])
            else:
                to_run.append(sc["dim_name"])
```

在 `_dimension_configs` 列表之后追加 specialized_configs 对应的执行任务构建：

在 `tasks` 列表构建之前（约第 215 行），追加：

```python
    # 构建 specialized 维度的任务配置映射
    _specialized_map = {sc["dim_name"]: sc for sc in specialized_configs}

    # 扩展 _dimension_configs 的查找逻辑，让 tasks 构建也能找到 specialized 维度
    _all_configs = dict(_dimension_configs)
    for sc in specialized_configs:
        _all_configs[sc["dim_name"]] = (
            sc["dim_name"], sc["get_sys_prompt"], sc["build_usr_prompt"], sc["validate_fn"]
        )
```

修改 tasks 构建逻辑，使其能处理 specialized 维度：

找到 `tasks = [` 这行，将原来只从 `_dimension_configs` 查找的逻辑改为同时查找 `_all_configs`：

```python
    tasks = [
        _run_assessment(dim, get_sys, build_usr, vfn)
        for dim, get_sys, build_usr, vfn in [
            _all_configs[dim] for dim in to_run if dim in _all_configs
        ]
    ]
```

- [ ] **Step 3: 验证 orchestrator 派发逻辑**

```bash
cd /Users/sqliang/ai-workspace/agent-workspace/daily-ai-insight-engine
# 确保 github-trending 源有已提取的文件
ls data/02_extracted/github-trending/ | head -3
# Dry-run 分析
uv run python pipeline/run.py analyze --input data/02_extracted/github-trending/ --dry-run
```

Expected: dry-run 列出 github-trending 文件，并在输出中显示 "维度: qualitative, value, foresight, github_project"。

- [ ] **Step 4: Commit**

```bash
git add pipeline/analysis/deep_analysis_agent.py pipeline/config.yaml
git commit -m "feat: add source_match dispatch for GitHub project analysis in Stage 3"
```

---

### Task 5: Stage 4b 日报合成 — specialized_brief

**Files:**
- Modify: `pipeline/schemas/daily_report.py`
- Modify: `pipeline/synthesis/prompts/system_prompt.py`
- Modify: `pipeline/synthesis/prompts/user_prompt.py`
- Modify: `pipeline/synthesis/editor_in_chief_agent.py`

**Interfaces:**
- Consumes: `specialized_tags` + `GitHubProjectAnalysis` fields from all_articles.json
- Produces: `specializedBrief` in DailyReport JSON

- [ ] **Step 1: 在 daily_report.py 中追加 SpecializedBrief 模型**

在 `pipeline/schemas/daily_report.py` 文件末尾追加：

```python

# =============================================================================
# 专题简报 — Stage 4b 日报中的轻量专题摘要
# =============================================================================


class GithubBrief(BaseModel):
    """GitHub 项目专题简报——日报中的轻量摘要。"""

    summary: str = Field(
        ...,
        description="一句话总结今日 GitHub Trending 项目趋势（中文）",
    )

    top_projects: List[str] = Field(
        default_factory=list,
        description="值得关注的项目名列表（Top 3-5）",
    )

    domain_distribution: dict = Field(
        default_factory=dict,
        description="通用领域分布（如 {'ai_ml': 3, 'devops_infra': 2}）",
    )

    ai_category_distribution: Optional[dict] = Field(
        default=None,
        description="AI 子领域分布（仅当有 AI 项目时，如 {'agent_framework': 2}）",
    )

    article_count: int = Field(
        ...,
        description="当日 github-trending 文章总数",
    )


class ProductBrief(BaseModel):
    """产品专题简报——Phase 2 实现。"""

    summary: str = ""
    notable_products: List[str] = []
    article_count: int = 0


class PaperBrief(BaseModel):
    """论文专题简报——Phase 2 实现。"""

    summary: str = ""
    key_papers: List[str] = []
    research_areas: List[str] = []
    article_count: int = 0


class SpecializedBrief(BaseModel):
    """
    日报中的专题简报——轻量摘要 + 入口引导。

    每个子块仅在当天有匹配文章时存在。
    """

    github_highlights: Optional[GithubBrief] = Field(
        default=None,
        alias="githubHighlights",
        description="今日 GitHub 项目亮点（仅当有 github-trending 文章时）",
    )

    product_highlights: Optional[ProductBrief] = Field(
        default=None,
        alias="productHighlights",
        description="今日产品亮点（仅当有产品类文章时）",
    )

    paper_highlights: Optional[PaperBrief] = Field(
        default=None,
        alias="paperHighlights",
        description="今日论文亮点（仅当有论文类文章时）",
    )

    class Config:
        populate_by_name = True
```

在 `DailyReport` 类中追加字段（在文件中的 `DailyReport` 定义里，最后一个字段之后）：

```python
    specialized_brief: Optional[SpecializedBrief] = Field(
        default=None,
        alias="specializedBrief",
        description="专题简报——轻量摘要 + 入口引导。仅当有专题文章时存在。",
    )
```

- [ ] **Step 2: 修改 synthesis system_prompt**

修改 `pipeline/synthesis/prompts/system_prompt.py`，在输出 Schema 描述中追加 `specializedBrief` 指令。

找到 system prompt 中描述输出 JSON structure 的部分，在 `opportunitySignals` 之后追加：

```python
### 7. specializedBrief (专题简报——可选)
仅当今日有 github-trending / producthunt / arxiv 文章时输出对应的子块。
每种子块最多出现一次。

- **githubHighlights** (可选): GitHub 项目亮点
  - **summary**: 一句话总结今日 GitHub Trending 趋势
  - **topProjects**: 值得关注的项目名列表 (Top 3-5)
  - **domainDistribution**: 领域分布 dict (如 {"ai_ml": 3, "devops_infra": 2})
  - **aiCategoryDistribution**: AI 子领域分布 (可选，仅当有 AI 项目时)
  - **articleCount**: 今日项目数量

- **productHighlights** (可选): 产品亮点 — Phase 2
- **paperHighlights** (可选): 论文亮点 — Phase 2
```

同时在规则部分追加一条（在现有 9/11 条规则之后）：

```python
10. **specializedBrief 生成规则**：
    - 仅当当日有匹配来源的文章时才生成对应的子块
    - summary 应从 specialized_tags 的统计分布中提炼趋势判断
    - topProjects 按项目影响力（Star 趋势 + 社区活跃度）筛选
    - 不需要深入每篇文章的细节，保持轻量
```

- [ ] **Step 3: 修改 synthesis user_prompt**

修改 `pipeline/synthesis/prompts/user_prompt.py`，在 `_compute_statistics()` 函数中追加 specialized_tags 统计：

在 `_compute_statistics()` 函数末尾、`return` 语句之前追加：

```python
    # --- 专题标注统计 (Phase 1: GitHub) ---
    github_domains: Counter = Counter()
    github_ai_cats: Counter = Counter()
    github_count = 0

    for a in articles:
        spec_tags = a.get("specialized_tags", {})
        if isinstance(spec_tags, dict):
            gh = spec_tags.get("github")
            if isinstance(gh, dict):
                github_count += 1
                domain = gh.get("domain", "other")
                github_domains[domain] += 1

                ai_detail = gh.get("aiDetail") or gh.get("ai_detail")
                if isinstance(ai_detail, dict):
                    for cat in ai_detail.get("primaryCategories", []) or []:
                        github_ai_cats[cat] += 1
```

在返回的 `stats_dict` 中追加：

```python
        "specialized_stats": {
            "github": {
                "count": github_count,
                "domain_distribution": dict(github_domains),
                "ai_category_distribution": dict(github_ai_cats) if github_ai_cats else None,
            },
        },
```

在 `build_user_prompt()` 函数中，找到格式化统计摘要的部分，追加专题统计展示：

```python
    # 专题标注统计
    spec_stats = stats.get("specialized_stats", {})
    gh_stats = spec_stats.get("github", {})
    if gh_stats.get("count", 0) > 0:
        prompt_parts.append("## 专题标注统计")
        prompt_parts.append(f"### GitHub Trending ({gh_stats['count']} 个项目)")
        prompt_parts.append(f"  领域分布: {_format_distribution(gh_stats.get('domain_distribution', {}))}")
        if gh_stats.get("ai_category_distribution"):
            prompt_parts.append(f"  AI 子领域分布: {_format_distribution(gh_stats['ai_category_distribution'])}")
```

- [ ] **Step 4: 修改 editor_in_chief_agent.py——在 validate 之后处理 specializedBrief**

在 `editor_in_chief_agent.py` 的 `_enrich_evidence_sources()` 调用之后，`_apply_cjk_spacing()` 之后追加对 `specializedBrief` 的 CJK 间距处理（现有的 `_apply_cjk_spacing` 已经是递归的，自动覆盖 `specializedBrief` 内的所有文本字段——无需额外代码）。

验证：`_apply_cjk_spacing()` 的实现已经是递归遍历所有 dict 和 list，所以 `specializedBrief` 中的文本字段会自动被处理。

- [ ] **Step 5: 验证 synthesize 端到端**

```bash
cd /Users/sqliang/ai-workspace/agent-workspace/daily-ai-insight-engine
# Dry run 验证 prompt 构造正确
uv run python pipeline/run.py synthesize --dry-run
# 如果有当日 github-trending 数据，执行合成
uv run python pipeline/run.py synthesize
# 检查输出
python3 -c "
import json
report = json.load(open('data/05_reports/daily-report.json'))
sb = report.get('specializedBrief')
if sb:
    gh = sb.get('githubHighlights')
    if gh:
        print(f'GitHub highlights: {gh.get(\"summary\", \"N/A\")}')
        print(f'Top projects: {gh.get(\"topProjects\", [])}')
        print(f'Domain distribution: {gh.get(\"domainDistribution\", {})}')
    else:
        print('No github highlights in specializedBrief')
else:
    print('No specializedBrief in report (may be expected if no github-trending articles today)')
"
```

- [ ] **Step 6: Commit**

```bash
git add pipeline/schemas/daily_report.py pipeline/synthesis/prompts/system_prompt.py pipeline/synthesis/prompts/user_prompt.py pipeline/synthesis/editor_in_chief_agent.py
git commit -m "feat: add specialized_brief to Stage 4b daily report synthesis"
```

---

### Task 6: Frontend TypeScript Schema 扩展

**Files:**
- Modify: `src/lib/agent/schema.ts`
- Modify: `src/lib/data/status.ts`
- Create: `src/lib/data/specialized.ts`

**Interfaces:**
- Consumes: `dailyReportSchema` daily-report.json structure
- Produces: `specializedBriefSchema`, `specializedTagsSchema`, `loadSpecializedArticles()`

- [ ] **Step 1: 在 schema.ts 中追加 specializedBrief Zod schema**

修改 `src/lib/agent/schema.ts`，在现有 Zod schema 定义之后追加：

```typescript
// ============================================================================
// 专题简报 Schema — Stage 4b 日报中的轻量专题摘要
// ============================================================================

const githubBriefSchema = z.object({
  summary: z.string(),
  topProjects: z.array(z.string()),
  domainDistribution: z.record(z.string(), z.number()),
  aiCategoryDistribution: z.record(z.string(), z.number()).nullable().optional(),
  articleCount: z.number().int().positive(),
});

const productBriefSchema = z.object({
  summary: z.string(),
  notableProducts: z.array(z.string()),
  articleCount: z.number().int().nonnegative(),
});

const paperBriefSchema = z.object({
  summary: z.string(),
  keyPapers: z.array(z.string()),
  researchAreas: z.array(z.string()),
  articleCount: z.number().int().nonnegative(),
});

const specializedBriefSchema = z.object({
  githubHighlights: githubBriefSchema.nullable().optional(),
  productHighlights: productBriefSchema.nullable().optional(),
  paperHighlights: paperBriefSchema.nullable().optional(),
});
```

在 `dailyReportSchema` 中追加字段（在现有最后一个字段 `visualizationData` 之后）：

```typescript
  specializedBrief: specializedBriefSchema.optional(),
```

- [ ] **Step 2: 在 status.ts 中追加 specializedTagsSchema**

修改 `src/lib/data/status.ts`，在 `structuredArticleSchema` 的 `.passthrough()` 之前追加 `specializedTags` 的宽松 schema（pass-through 已存在，会自动放行新字段；仅追加显式 schema 以便有类型提示时使用）：

```typescript
// ============================================================================
// 专题标注 Schema — 按来源类型分派
// ============================================================================

const aiDetailSchema = z.object({
  primaryCategories: z.array(z.string()).optional(),
  agentSubcategory: z.array(z.string()).nullable().optional(),
  techTags: z.array(z.string()).optional(),
}).passthrough();

const githubTagsSchema = z.object({
  projectName: z.string(),
  projectUrl: z.string(),
  primaryLanguage: z.string(),
  licenseType: z.string(),
  domain: z.string(),
  crossTags: z.array(z.string()).optional(),
  aiDetail: aiDetailSchema.nullable().optional(),
}).passthrough();

const specializedTagsSchema = z.object({
  github: githubTagsSchema.nullable().optional(),
  product: z.any().nullable().optional(),
  paper: z.any().nullable().optional(),
}).passthrough();

// 追加到 structuredArticleSchema（作为 optional 字段）
// structuredArticleSchema 已有 .passthrough()，新字段自动通过。
// 显式添加类型以支持 TypeScript 推导：
export type SpecializedTags = z.infer<typeof specializedTagsSchema>;
export type GitHubTags = z.infer<typeof githubTagsSchema>;
export type AiDetail = z.infer<typeof aiDetailSchema>;
```

- [ ] **Step 3: 创建 specialized.ts 数据加载模块**

新建 `src/lib/data/specialized.ts`：

```typescript
// ============================================================================
// src/lib/data/specialized.ts — 专题分析数据加载
//
// 从 all_articles.json 或 per-source JSON 中加载、
// 过滤、聚合专题分析相关的文章数据。
// ============================================================================

import { readJsonFile } from './files';
import type { StructuredArticle } from './status';

// ---------------------------------------------------------------------------
// 类型定义
// ---------------------------------------------------------------------------

/** GitHub 专题报告中的项目条目 */
export interface GithubProjectEntry {
  articleId: string;
  title: string;
  url: string;
  projectName: string;
  projectUrl: string;
  primaryLanguage: string;
  licenseType: string;
  domain: string;
  crossTags: string[];
  aiDetail?: {
    primaryCategories: string[];
    agentSubcategory?: string[] | null;
    techTags: string[];
  } | null;
  // Stage 3 分析结果（可能尚未运行）
  techAssessment?: {
    techStackQuality: string;
    architectureHighlights: string;
    maturityScore?: number;
  };
  communityHealth?: {
    contributorActivity: string;
    starsTrend: string;
  };
  adoptionGuidance?: {
    recommendedFor: string[];
    cautionFor: string[];
    timeToProduction: string;
  };
}

// ---------------------------------------------------------------------------
// 数据加载
// ---------------------------------------------------------------------------

/**
 * 加载指定日期的 GitHub 专题文章。
 *
 * 从 all_articles.json 中筛选 source_dir == "github-trending" 的文章，
 * 提取 specialized_tags.github（Stage 2 标注）和 Stage 3 分析字段。
 */
export async function loadGithubArticles(
  date: string,
): Promise<GithubProjectEntry[]> {
  const allArticlesPath = `data/04_structured/all_articles.json`;
  // 如果 all_articles 的 lookback_days 不匹配，回退读取 archive
  try {
    const data = await readJsonFile(allArticlesPath);
    const articles = (data.articles || []) as StructuredArticle[];

    return articles
      .filter((a: any) => a.source_dir === 'github-trending')
      .map((a: any) => {
        const gh = a.specialized_tags?.github || {};

        return {
          articleId: a.id || '',
          title: a.title || '',
          url: a.url || '',
          projectName: gh.project_name || gh.projectName || '',
          projectUrl: gh.project_url || gh.projectUrl || '',
          primaryLanguage: gh.primary_language || gh.primaryLanguage || '',
          licenseType: gh.license_type || gh.licenseType || '',
          domain: gh.domain || 'other',
          crossTags: gh.cross_tags || gh.crossTags || [],
          aiDetail: gh.ai_detail || gh.aiDetail || null,
          techAssessment: {
            techStackQuality: a.tech_assessment?.tech_stack_quality || '',
            architectureHighlights: a.tech_assessment?.architecture_highlights || '',
          },
          communityHealth: {
            contributorActivity: a.community_health?.contributor_activity || '',
            starsTrend: a.community_health?.stars_trend || '',
          },
          adoptionGuidance: {
            recommendedFor: a.adoption_guidance?.recommended_for || [],
            cautionFor: a.adoption_guidance?.caution_for || [],
            timeToProduction: a.adoption_guidance?.time_to_production || '',
          },
        };
      });
  } catch {
    return [];
  }
}

/**
 * 计算领域分布统计。
 */
export function computeDomainDistribution(
  projects: GithubProjectEntry[],
): Record<string, number> {
  const dist: Record<string, number> = {};
  for (const p of projects) {
    dist[p.domain] = (dist[p.domain] || 0) + 1;
  }
  return dist;
}

/**
 * 计算 AI 子领域分布统计。
 */
export function computeAiCategoryDistribution(
  projects: GithubProjectEntry[],
): Record<string, number> {
  const dist: Record<string, number> = {};
  for (const p of projects) {
    if (p.aiDetail?.primaryCategories) {
      for (const cat of p.aiDetail.primaryCategories) {
        dist[cat] = (dist[cat] || 0) + 1;
      }
    }
  }
  return dist;
}
```

- [ ] **Step 4: 验证 TypeScript 类型安全**

```bash
cd /Users/sqliang/ai-workspace/agent-workspace/daily-ai-insight-engine
pnpm typecheck
```

Expected: 无类型错误。

- [ ] **Step 5: Commit**

```bash
git add src/lib/agent/schema.ts src/lib/data/status.ts src/lib/data/specialized.ts
git commit -m "feat: add TypeScript schemas and data loader for specialized analysis"
```

---

### Task 7: Frontend GitHubProjectCard 组件

**Files:**
- Create: `src/components/sources/GitHubProjectCard.tsx`
- Create: `src/components/sources/ArticleCardSpecialized.tsx`

**Interfaces:**
- Consumes: `StructuredArticle` enriched article data
- Produces: Visual analysis card rendered inside expanded ArticleCard

- [ ] **Step 1: 创建 GitHubProjectCard 组件**

新建 `src/components/sources/GitHubProjectCard.tsx`：

```tsx
// ============================================================================
// GitHubProjectCard.tsx — GitHub 开源项目分析卡片
//
// 在 Source Detail 页面中，展示单篇文章的 GitHub 项目深度分析。
// 作为 ArticleCardSpecialized 的子卡片渲染。
// ============================================================================

import type { GitHubTags, AiDetail } from '@/lib/data/status';

// ---------------------------------------------------------------------------
// 领域颜色映射 (14 domains + other)
// ---------------------------------------------------------------------------
const DOMAIN_COLORS: Record<string, { bg: string; text: string }> = {
  ai_ml: { bg: 'bg-purple-100 dark:bg-purple-900/30', text: 'text-purple-700 dark:text-purple-300' },
  web_frontend: { bg: 'bg-blue-100 dark:bg-blue-900/30', text: 'text-blue-700 dark:text-blue-300' },
  web_backend: { bg: 'bg-green-100 dark:bg-green-900/30', text: 'text-green-700 dark:text-green-300' },
  devops_infra: { bg: 'bg-orange-100 dark:bg-orange-900/30', text: 'text-orange-700 dark:text-orange-300' },
  database_storage: { bg: 'bg-cyan-100 dark:bg-cyan-900/30', text: 'text-cyan-700 dark:text-cyan-300' },
  programming_languages: { bg: 'bg-red-100 dark:bg-red-900/30', text: 'text-red-700 dark:text-red-300' },
  developer_tools: { bg: 'bg-indigo-100 dark:bg-indigo-900/30', text: 'text-indigo-700 dark:text-indigo-300' },
  security: { bg: 'bg-rose-100 dark:bg-rose-900/30', text: 'text-rose-700 dark:text-rose-300' },
  mobile: { bg: 'bg-emerald-100 dark:bg-emerald-900/30', text: 'text-emerald-700 dark:text-emerald-300' },
  blockchain: { bg: 'bg-amber-100 dark:bg-amber-900/30', text: 'text-amber-700 dark:text-amber-300' },
  data_engineering: { bg: 'bg-teal-100 dark:bg-teal-900/30', text: 'text-teal-700 dark:text-teal-300' },
  game_development: { bg: 'bg-pink-100 dark:bg-pink-900/30', text: 'text-pink-700 dark:text-pink-300' },
  documentation: { bg: 'bg-gray-100 dark:bg-gray-800', text: 'text-gray-700 dark:text-gray-300' },
  iot_embedded: { bg: 'bg-lime-100 dark:bg-lime-900/30', text: 'text-lime-700 dark:text-lime-300' },
  other: { bg: 'bg-gray-100 dark:bg-gray-800', text: 'text-gray-600 dark:text-gray-400' },
};

const DOMAIN_LABELS: Record<string, string> = {
  ai_ml: 'AI/ML',
  web_frontend: 'Web 前端',
  web_backend: 'Web 后端',
  devops_infra: 'DevOps/基础设施',
  database_storage: '数据库/存储',
  programming_languages: '编程语言',
  developer_tools: '开发者工具',
  security: '安全',
  mobile: '移动端',
  blockchain: '区块链',
  data_engineering: '数据工程',
  game_development: '游戏开发',
  documentation: '文档/知识库',
  iot_embedded: 'IoT/嵌入式',
  other: '其他',
};

// ---------------------------------------------------------------------------
// Props
// ---------------------------------------------------------------------------

interface GitHubProjectCardProps {
  /** Stage 2 specialized_tags.github */
  tags: GitHubTags;
  /** Stage 3 分析结果（可能未运行） */
  analysis?: Record<string, any>;
}

// ---------------------------------------------------------------------------
// 子组件
// ---------------------------------------------------------------------------

function DomainPill({ domain }: { domain: string }) {
  const colors = DOMAIN_COLORS[domain] || DOMAIN_COLORS.other;
  const label = DOMAIN_LABELS[domain] || domain;
  return (
    <span
      className={`inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium ${colors.bg} ${colors.text}`}
    >
      {label}
    </span>
  );
}

function AiCategoryPills({ aiDetail }: { aiDetail: AiDetail }) {
  return (
    <div className="flex flex-wrap gap-1 mt-1">
      {aiDetail.primaryCategories?.map((cat) => (
        <span
          key={cat}
          className="inline-flex items-center rounded-full bg-purple-100 dark:bg-purple-900/20 px-2 py-0.5 text-xs font-medium text-purple-700 dark:text-purple-300"
        >
          {cat.replace(/_/g, ' ')}
        </span>
      ))}
      {aiDetail.agentSubcategory?.map((sub) => (
        <span
          key={sub}
          className="inline-flex items-center rounded-full bg-pink-100 dark:bg-pink-900/20 px-2 py-0.5 text-xs font-medium text-pink-700 dark:text-pink-300 border border-pink-200 dark:border-pink-800"
        >
          agent: {sub.replace(/_/g, ' ')}
        </span>
      ))}
    </div>
  );
}

function MaturityBadge({ score }: { score?: number }) {
  if (!score) return null;
  const color =
    score >= 7
      ? 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-300'
      : score >= 4
        ? 'bg-yellow-100 text-yellow-700 dark:bg-yellow-900/30 dark:text-yellow-300'
        : 'bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-300';
  return (
    <span className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-mono font-bold ${color}`}>
      {score.toFixed(1)}
    </span>
  );
}

// ---------------------------------------------------------------------------
// 主组件
// ---------------------------------------------------------------------------

export function GitHubProjectCard({ tags, analysis }: GitHubProjectCardProps) {
  const colors = DOMAIN_COLORS[tags.domain] || DOMAIN_COLORS.other;

  return (
    <div className="rounded-lg border border-gray-200 dark:border-gray-700 overflow-hidden">
      {/* 卡片标题栏 */}
      <div className="px-4 py-3 bg-gray-50 dark:bg-gray-800/50 border-b border-gray-200 dark:border-gray-700">
        <div className="flex items-center gap-2">
          <svg className="w-5 h-5 text-gray-700 dark:text-gray-300" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
          </svg>
          <span className="text-sm font-semibold text-gray-800 dark:text-gray-200">
            GitHub 项目分析
          </span>
          {analysis?.adoption_guidance?.maturity_score && (
            <MaturityBadge score={analysis.adoption_guidance.maturity_score} />
          )}
        </div>
      </div>

      {/* 卡片正文 */}
      <div className="p-4 space-y-3">
        {/* 项目画像 + 分类标签 */}
        <div>
          <div className="flex items-center gap-2 flex-wrap">
            <span className="text-base font-semibold text-gray-900 dark:text-gray-100">
              {tags.project_name}
            </span>
            <DomainPill domain={tags.domain} />
            {tags.primary_language && (
              <span className="text-xs text-gray-500 dark:text-gray-400 font-mono">
                {tags.primary_language}
              </span>
            )}
            {tags.license_type && (
              <span className="text-xs text-gray-400 dark:text-gray-500">
                {tags.license_type}
              </span>
            )}
          </div>

          {/* AI 子标签 */}
          {tags.aiDetail && <AiCategoryPills aiDetail={tags.aiDetail} />}

          {/* 跨领域标签 */}
          {tags.cross_tags?.length > 0 && (
            <div className="flex flex-wrap gap-1 mt-1">
              {tags.cross_tags.map((tag) => (
                <span
                  key={tag}
                  className="inline-flex items-center rounded-full bg-gray-100 dark:bg-gray-800 px-2 py-0.5 text-xs text-gray-600 dark:text-gray-400"
                >
                  {tag}
                </span>
              ))}
            </div>
          )}
        </div>

        {/* 技术评价（如果 Stage 3 已运行） */}
        {analysis?.tech_assessment && (
          <div className="rounded-md bg-gray-50 dark:bg-gray-800/30 p-3">
            <div className="flex items-center gap-2 text-xs text-gray-500 dark:text-gray-400 mb-1">
              <span className="font-medium">技术评价</span>
              <span className="text-gray-400">·</span>
              <span>{analysis.tech_assessment.tech_stack_quality}</span>
              {analysis.tech_assessment.code_quality_indicators?.has_tests && (
                <>
                  <span className="text-gray-400">·</span>
                  <span className="text-green-600 dark:text-green-400">有测试</span>
                </>
              )}
              {analysis.tech_assessment.code_quality_indicators?.has_ci_cd && (
                <>
                  <span className="text-gray-400">·</span>
                  <span className="text-green-600 dark:text-green-400">CI/CD</span>
                </>
              )}
            </div>
            {analysis.tech_assessment.architecture_highlights && (
              <p className="text-sm text-gray-700 dark:text-gray-300">
                {analysis.tech_assessment.architecture_highlights}
              </p>
            )}
          </div>
        )}

        {/* 社区健康度 + 采用建议 */}
        {(analysis?.community_health || analysis?.adoption_guidance) && (
          <div className="grid grid-cols-2 gap-3">
            {analysis?.community_health && (
              <div className="rounded-md bg-gray-50 dark:bg-gray-800/30 p-3">
                <div className="text-xs font-medium text-gray-500 dark:text-gray-400 mb-1">
                  社区活跃度
                </div>
                <div className="text-sm text-gray-700 dark:text-gray-300 space-y-1">
                  <div>贡献者: {analysis.community_health.contributor_activity}</div>
                  {analysis.community_health.stars_trend && (
                    <div>趋势: {analysis.community_health.stars_trend}</div>
                  )}
                </div>
              </div>
            )}
            {analysis?.adoption_guidance && (
              <div className="rounded-md bg-gray-50 dark:bg-gray-800/30 p-3">
                <div className="text-xs font-medium text-gray-500 dark:text-gray-400 mb-1">
                  采用建议
                </div>
                <div className="text-sm text-gray-700 dark:text-gray-300">
                  <div>状态: {analysis.adoption_guidance.time_to_production}</div>
                  {analysis.adoption_guidance.recommended_for?.length > 0 && (
                    <div className="text-green-700 dark:text-green-400">
                      ✓ {analysis.adoption_guidance.recommended_for.slice(0, 2).join(', ')}
                    </div>
                  )}
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
```

- [ ] **Step 2: 创建 ArticleCardSpecialized 容器组件**

新建 `src/components/sources/ArticleCardSpecialized.tsx`：

```tsx
// ============================================================================
// ArticleCardSpecialized.tsx — 专题分析容器
//
// 按文章来源类型派发对应的专题分析卡片。
// 在 ArticleCard 展开态中，渲染于黄金三角分析下方。
// ============================================================================

import { GitHubProjectCard } from './GitHubProjectCard';
import type { GitHubTags } from '@/lib/data/status';

interface ArticleCardSpecializedProps {
  source: string;
  enriched: Record<string, any> | null;
}

export function ArticleCardSpecialized({ source, enriched }: ArticleCardSpecializedProps) {
  if (!enriched) return null;

  const specializedTags = enriched.specialized_tags;

  // Phase 1: GitHub — 检查是否有 GitHub 标注
  if (source === 'github-trending' && specializedTags?.github) {
    const githubTags = specializedTags.github as GitHubTags;

    // 提取 Stage 3 GitHub 分析字段（snake_case → 适配）
    const analysis = {
      project_profile: enriched.project_profile,
      project_classification: enriched.project_classification,
      tech_assessment: enriched.tech_assessment,
      community_health: enriched.community_health,
      competitive_landscape: enriched.competitive_landscape,
      adoption_guidance: enriched.adoption_guidance,
    };

    return (
      <div className="mt-4">
        <div className="flex items-center gap-2 mb-3">
          <div className="h-px flex-1 bg-gradient-to-r from-transparent via-purple-300 dark:via-purple-700 to-transparent" />
          <span className="text-xs font-medium text-purple-600 dark:text-purple-400 uppercase tracking-wider">
            专题分析
          </span>
          <div className="h-px flex-1 bg-gradient-to-r from-transparent via-purple-300 dark:via-purple-700 to-transparent" />
        </div>
        <GitHubProjectCard tags={githubTags} analysis={analysis} />
      </div>
    );
  }

  // Phase 2: Product — 待实现
  // if (['producthunt', 'whytryai'].includes(source) && specializedTags?.product) { ... }

  // Phase 3: Paper — 待实现
  // if (source === 'arxiv-cs-ai' && specializedTags?.paper) { ... }

  return null;
}
```

- [ ] **Step 3: 在 ArticleCard 中集成 ArticleCardSpecialized**

修改 `src/components/sources/ArticleCard.tsx`，在展开态中黄金三角分析（`ArticleCardAnalysis`）之后追加专题分析渲染。

找到渲染 `ArticleCardAnalysis` 的位置，在其 JSX 闭合标签之后追加：

```tsx
        {/* 专题分析（按来源类型匹配） */}
        <ArticleCardSpecialized
          source={article.source}
          enriched={article.enriched}
        />
```

并在文件顶部追加导入：

```tsx
import { ArticleCardSpecialized } from './ArticleCardSpecialized';
```

- [ ] **Step 4: 验证前端组件构建**

```bash
cd /Users/sqliang/ai-workspace/agent-workspace/daily-ai-insight-engine
pnpm typecheck
pnpm build
```

Expected: 构建成功，无 TypeScript 错误。

- [ ] **Step 5: Commit**

```bash
git add src/components/sources/GitHubProjectCard.tsx src/components/sources/ArticleCardSpecialized.tsx src/components/sources/ArticleCard.tsx
git commit -m "feat: add GitHubProjectCard and ArticleCardSpecialized components"
```

---

### Task 8: Frontend 专题报告页 + Dashboard 入口

**Files:**
- Create: `src/app/specialized/github/[date]/page.tsx`
- Modify: `src/components/dashboard/DashboardContent.tsx`
- Create: `src/components/dashboard/SpecializedBriefSection.tsx`

**Interfaces:**
- Consumes: `loadGithubArticles()` from Task 6, `DailyReport.specializedBrief` from Task 5
- Produces: `/specialized/github/[date]` route, Dashboard specialized section

- [ ] **Step 1: 创建 GitHub 专题报告页**

新建 `src/app/specialized/github/[date]/page.tsx`：

```tsx
// ============================================================================
// /specialized/github/[date] — GitHub 开源项目专题报告页
//
// 展示指定日期的 GitHub Trending 项目分析结果。
// 支持按领域和 AI 子领域筛选。
// ============================================================================

import { notFound } from 'next/navigation';
import Link from 'next/link';
import {
  loadGithubArticles,
  computeDomainDistribution,
  computeAiCategoryDistribution,
} from '@/lib/data/specialized';
import type { GithubProjectEntry } from '@/lib/data/specialized';
import { PageShell } from '@/components/layout/PageShell';
import { DOMAIN_LABELS, DOMAIN_COLORS } from '@/components/sources/GitHubProjectCard';

// 直接导入上面的常量（或者改为从 GitHubProjectCard 导出）
const DOMAIN_LIST = [
  'ai_ml', 'web_frontend', 'web_backend', 'devops_infra', 'database_storage',
  'programming_languages', 'developer_tools', 'security', 'mobile', 'blockchain',
  'data_engineering', 'game_development', 'documentation', 'iot_embedded', 'other',
];

export const dynamic = 'force-dynamic';

interface Props {
  params: Promise<{ date: string }>;
  searchParams: Promise<{ domain?: string }>;
}

export default async function GithubSpecializedPage({ params, searchParams }: Props) {
  const { date } = await params;
  const { domain: filterDomain } = await searchParams;

  const projects = await loadGithubArticles(date);

  if (projects.length === 0) {
    return (
      <PageShell>
        <div className="py-20 text-center">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-4">
            {date} GitHub 项目专题报告
          </h1>
          <p className="text-gray-500 dark:text-gray-400">
            当日没有 GitHub Trending 数据。
          </p>
          <Link href="/dashboard" className="text-blue-600 hover:underline mt-4 inline-block">
            ← 回到日报列表
          </Link>
        </div>
      </PageShell>
    );
  }

  // 筛选
  const filtered = filterDomain
    ? projects.filter((p) => p.domain === filterDomain)
    : projects;

  const domainDist = computeDomainDistribution(projects);
  const aiCatDist = computeAiCategoryDistribution(projects);

  return (
    <PageShell>
      {/* Hero Banner */}
      <div className="mb-8 p-6 rounded-xl bg-gradient-to-br from-purple-50 to-indigo-50 dark:from-purple-950/30 dark:to-indigo-950/30 border border-purple-200 dark:border-purple-800">
        <Link
          href={`/dashboard/${date}`}
          className="text-sm text-purple-600 dark:text-purple-400 hover:underline mb-2 inline-block"
        >
          ← 回到日报
        </Link>
        <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mt-2">
          {date} GitHub 开源项目专题报告
        </h1>
        <p className="text-gray-600 dark:text-gray-400 mt-1">
          共 {projects.length} 个项目 · {Object.keys(domainDist).length} 个领域
        </p>

        {/* 领域分布条 */}
        <div className="mt-4 flex flex-wrap gap-1">
          {DOMAIN_LIST.filter((d) => domainDist[d]).map((d) => {
            const colors = DOMAIN_COLORS[d] || DOMAIN_COLORS.other;
            const label = DOMAIN_LABELS[d] || d;
            const count = domainDist[d];
            const isActive = filterDomain === d;
            return (
              <Link
                key={d}
                href={isActive ? `/specialized/github/${date}` : `?domain=${d}`}
                className={`inline-flex items-center gap-1 rounded-full px-2.5 py-1 text-xs font-medium transition-colors ${
                  isActive
                    ? 'ring-2 ring-purple-400 ' + colors.bg + ' ' + colors.text
                    : colors.bg + ' ' + colors.text + ' hover:opacity-80'
                }`}
              >
                {label} ({count})
              </Link>
            );
          })}
        </div>

        {/* AI 子领域分布（条件显示） */}
        {Object.keys(aiCatDist).length > 0 && (
          <div className="mt-2 flex flex-wrap gap-1">
            <span className="text-xs text-gray-400 mr-1">AI 子领域:</span>
            {Object.entries(aiCatDist).sort((a, b) => b[1] - a[1]).map(([cat, count]) => (
              <span
                key={cat}
                className="inline-flex items-center rounded-full bg-purple-100 dark:bg-purple-900/30 px-2 py-0.5 text-xs text-purple-700 dark:text-purple-300"
              >
                {cat.replace(/_/g, ' ')} ({count})
              </span>
            ))}
          </div>
        )}
      </div>

      {/* 项目列表 */}
      <div className="space-y-4">
        {filtered.map((project) => (
          <ProjectCard key={project.articleId} project={project} date={date} />
        ))}
      </div>

      {filtered.length === 0 && (
        <p className="text-center text-gray-500 py-12">该领域下暂无项目。</p>
      )}
    </PageShell>
  );
}

// ---------------------------------------------------------------------------
// 项目卡片子组件
// ---------------------------------------------------------------------------

function ProjectCard({ project, date }: { project: GithubProjectEntry; date: string }) {
  const colors = DOMAIN_COLORS[project.domain] || DOMAIN_COLORS.other;
  const domainLabel = DOMAIN_LABELS[project.domain] || project.domain;

  // 检查是否有 Stage 3 分析数据
  const hasAnalysis = !!project.techAssessment?.techStackQuality;

  return (
    <Link
      href={`/sources/github-trending`}
      className="block rounded-lg border border-gray-200 dark:border-gray-700 p-4 hover:border-purple-300 dark:hover:border-purple-700 transition-colors"
    >
      <div className="flex items-start justify-between gap-4">
        <div className="min-w-0 flex-1">
          {/* 项目名 + 领域标签 */}
          <div className="flex items-center gap-2 flex-wrap mb-1">
            <h3 className="text-base font-semibold text-gray-900 dark:text-gray-100 truncate">
              {project.projectName || project.title}
            </h3>
            <span
              className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${colors.bg} ${colors.text}`}
            >
              {domainLabel}
            </span>
          </div>

          {/* 元信息 */}
          <div className="flex items-center gap-3 text-xs text-gray-500 dark:text-gray-400">
            {project.primaryLanguage && (
              <span className="font-mono">{project.primaryLanguage}</span>
            )}
            {project.licenseType && <span>{project.licenseType}</span>}
          </div>

          {/* 技术评价摘要 */}
          {hasAnalysis && (
            <div className="mt-2 flex items-center gap-3 text-sm">
              {project.techAssessment?.techStackQuality && (
                <span className="text-gray-700 dark:text-gray-300">
                  技术栈: {project.techAssessment.techStackQuality}
                </span>
              )}
              {project.communityHealth?.contributorActivity && (
                <span className="text-gray-500 dark:text-gray-400">
                  社区: {project.communityHealth.contributorActivity}
                </span>
              )}
              {project.adoptionGuidance?.timeToProduction && (
                <span className="text-gray-500 dark:text-gray-400">
                  投产: {project.adoptionGuidance.timeToProduction}
                </span>
              )}
            </div>
          )}

          {/* 采用建议 */}
          {project.adoptionGuidance?.recommendedFor?.length > 0 && (
            <div className="mt-2 flex flex-wrap gap-1">
              {project.adoptionGuidance.recommendedFor.slice(0, 3).map((rec) => (
                <span
                  key={rec}
                  className="inline-flex items-center rounded bg-green-50 dark:bg-green-900/20 px-2 py-0.5 text-xs text-green-700 dark:text-green-400"
                >
                  ✓ {rec}
                </span>
              ))}
            </div>
          )}
        </div>

        {/* 箭头指示 */}
        <svg className="w-5 h-5 text-gray-400 flex-shrink-0 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
        </svg>
      </div>
    </Link>
  );
}
```

- [ ] **Step 2: 将 DOMAIN_COLORS 和 DOMAIN_LABELS 从 GitHubProjectCard 导出**

修改 `src/components/sources/GitHubProjectCard.tsx`，在 `const DOMAIN_COLORS` 和 `const DOMAIN_LABELS` 前加 `export`：

```tsx
export const DOMAIN_COLORS: Record<string, { bg: string; text: string }> = {
export const DOMAIN_LABELS: Record<string, string> = {
```

同时将 `DOMAIN_LIST` 也导出：

```tsx
export const DOMAIN_LIST = [
```

- [ ] **Step 3: 创建 SpecializedBriefSection 组件**

新建 `src/components/dashboard/SpecializedBriefSection.tsx`：

```tsx
// ============================================================================
// SpecializedBriefSection.tsx — 日报专题简报入口 Section
//
// 从 dailyReport.specializedBrief 读取可选子块，
// 渲染为入口卡片，点击进入专题报告详情页。
// ============================================================================

import Link from 'next/link';

interface GithubHighlights {
  summary: string;
  topProjects: string[];
  domainDistribution: Record<string, number>;
  aiCategoryDistribution?: Record<string, number> | null;
  articleCount: number;
}

interface SpecializedBrief {
  githubHighlights?: GithubHighlights | null;
  productHighlights?: any;
  paperHighlights?: any;
}

interface SpecializedBriefSectionProps {
  data: SpecializedBrief | null | undefined;
  date: string;
}

export function SpecializedBriefSection({ data, date }: SpecializedBriefSectionProps) {
  if (!data) return null;

  const hasContent = data.githubHighlights || data.productHighlights || data.paperHighlights;
  if (!hasContent) return null;

  return (
    <section className="mt-8">
      <h2 className="text-xl font-bold text-gray-900 dark:text-gray-100 mb-4">
        专题洞察
      </h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {data.githubHighlights && (
          <GithubBriefCard data={data.githubHighlights} date={date} />
        )}
        {data.productHighlights && (
          <BriefCardPlaceholder
            icon="📦"
            title="产品扫描"
            summary={data.productHighlights.summary}
            count={data.productHighlights.articleCount}
          />
        )}
        {data.paperHighlights && (
          <BriefCardPlaceholder
            icon="📄"
            title="论文速递"
            summary={data.paperHighlights.summary}
            count={data.paperHighlights.articleCount}
          />
        )}
      </div>
    </section>
  );
}

function GithubBriefCard({ data, date }: { data: GithubHighlights; date: string }) {
  return (
    <Link
      href={`/specialized/github/${date}`}
      className="block rounded-xl border border-purple-200 dark:border-purple-800 bg-gradient-to-br from-purple-50 to-indigo-50 dark:from-purple-950/20 dark:to-indigo-950/20 p-5 hover:shadow-md hover:border-purple-300 dark:hover:border-purple-700 transition-all group"
    >
      <div className="flex items-center gap-2 mb-2">
        <span className="text-2xl">🐙</span>
        <h3 className="text-lg font-semibold text-gray-900 dark:text-gray-100">
          GitHub 开源项目
        </h3>
        <span className="ml-auto inline-flex items-center rounded-full bg-purple-100 dark:bg-purple-900/30 px-2 py-0.5 text-xs font-medium text-purple-700 dark:text-purple-300">
          {data.articleCount} 个项目
        </span>
      </div>

      <p className="text-sm text-gray-600 dark:text-gray-400 mb-3 line-clamp-2">
        {data.summary}
      </p>

      {/* Top 项目列表 */}
      {data.topProjects?.length > 0 && (
        <div className="space-y-1 mb-3">
          {data.topProjects.slice(0, 3).map((name, i) => (
            <div key={name} className="flex items-center gap-2 text-sm text-gray-700 dark:text-gray-300">
              <span className="text-purple-400 text-xs font-mono">{i + 1}.</span>
              <span className="truncate">{name}</span>
            </div>
          ))}
        </div>
      )}

      {/* 领域分布预览 */}
      {data.domainDistribution && Object.keys(data.domainDistribution).length > 0 && (
        <div className="flex flex-wrap gap-1">
          {Object.entries(data.domainDistribution)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 4)
            .map(([domain, count]) => (
              <span
                key={domain}
                className="inline-flex items-center rounded-full bg-white/60 dark:bg-gray-800/60 px-2 py-0.5 text-xs text-gray-600 dark:text-gray-400"
              >
                {domain} ×{count}
              </span>
            ))}
          {Object.keys(data.domainDistribution).length > 4 && (
            <span className="text-xs text-gray-400">
              +{Object.keys(data.domainDistribution).length - 4}
            </span>
          )}
        </div>
      )}

      <div className="mt-3 flex items-center text-sm text-purple-600 dark:text-purple-400 group-hover:underline">
        查看完整报告
        <svg className="w-4 h-4 ml-1 group-hover:translate-x-0.5 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
        </svg>
      </div>
    </Link>
  );
}

function BriefCardPlaceholder({
  icon, title, summary, count,
}: {
  icon: string; title: string; summary: string; count: number;
}) {
  return (
    <div className="block rounded-xl border border-gray-200 dark:border-gray-700 bg-gray-50 dark:bg-gray-800/20 p-5 opacity-60">
      <div className="flex items-center gap-2 mb-2">
        <span className="text-2xl">{icon}</span>
        <h3 className="text-lg font-semibold text-gray-900 dark:text-gray-100">{title}</h3>
        <span className="ml-auto text-xs text-gray-500">{count} 项</span>
      </div>
      <p className="text-sm text-gray-600 dark:text-gray-400 line-clamp-2">{summary}</p>
      <p className="text-xs text-gray-400 mt-3">专题报告即将上线</p>
    </div>
  );
}
```

- [ ] **Step 4: 在 DashboardContent 中集成 SpecializedBriefSection**

修改 `src/components/dashboard/DashboardContent.tsx`：

在 `DeepDivesSection` 渲染之后、`SignalList` 渲染之前，插入：

```tsx
        {/* 专题洞察入口 */}
        <SpecializedBriefSection
          data={report.specializedBrief}
          date={report.date}
        />
```

并在文件顶部导入：

```tsx
import { SpecializedBriefSection } from './SpecializedBriefSection';
```

- [ ] **Step 5: 验证前端构建和路由**

```bash
cd /Users/sqliang/ai-workspace/agent-workspace/daily-ai-insight-engine
pnpm typecheck
pnpm build
```

Expected: 构建成功。Next.js 自动识别 `src/app/specialized/github/[date]/page.tsx` 为新路由。

- [ ] **Step 6: Commit**

```bash
git add src/app/specialized/ src/components/dashboard/SpecializedBriefSection.tsx src/components/dashboard/DashboardContent.tsx src/components/sources/GitHubProjectCard.tsx
git commit -m "feat: add GitHub specialized report page and dashboard entry section"
```

---

### Task 9: 端到端验证

**Files:** (none — verification only)

- [ ] **Step 1: 全管线 Python 验证**

```bash
cd /Users/sqliang/ai-workspace/agent-workspace/daily-ai-insight-engine

# 1. Schema 导入验证
uv run python -c "
from pipeline.schemas.fact_extraction import SpecializedTags, GitHubTags, AiDetail
from pipeline.schemas.specialized_analysis import GitHubProjectAnalysis
from pipeline.schemas.daily_report import DailyReport, SpecializedBrief, GithubBrief
print('All schemas imported successfully')
"

# 2. Stage 2 提取验证（用 github-trending 文件）
uv run python pipeline/run.py extract --input data/02_extracted/github-trending/ --force
# 检查输出 frontmatter 是否包含 specialized_tags
head -60 data/02_extracted/github-trending/$(ls data/02_extracted/github-trending/ | head -1)

# 3. Stage 3 分析验证
uv run python pipeline/run.py analyze --input data/02_extracted/github-trending/ --force
# 检查输出 frontmatter 是否包含 GitHub 分析字段
head -80 data/03_analyzed/github-trending/$(ls data/03_analyzed/github-trending/ | head -1)

# 4. Stage 4a 聚合验证
uv run python pipeline/run.py aggregate --lookback-days 0
python3 -c "
import json
data = json.load(open('data/04_structured/all_articles.json'))
gh = [a for a in data['articles'] if a.get('source_dir') == 'github-trending']
print(f'GitHub articles in all_articles.json: {len(gh)}')
if gh:
    print('Sample keys:', list(gh[0].keys())[:20])
"

# 5. Stage 4b 合成验证（dry-run 先）
uv run python pipeline/run.py synthesize --dry-run
uv run python pipeline/run.py synthesize
python3 -c "
import json
report = json.load(open('data/05_reports/daily-report.json'))
sb = report.get('specializedBrief')
print('specializedBrief present:', sb is not None)
if sb and sb.get('githubHighlights'):
    print('githubHighlights:', json.dumps(sb['githubHighlights'], ensure_ascii=False, indent=2)[:500])
"
```

- [ ] **Step 2: 前端验证**

```bash
cd /Users/sqliang/ai-workspace/agent-workspace/daily-ai-insight-engine
pnpm dev
```

在浏览器中验证：
1. 访问 `http://localhost:3000/sources/github-trending` → 展开文章 → 确认底部出现「专题分析」分隔线 + GitHub 项目分析卡片
2. 访问 `http://localhost:3000/dashboard/2026-07-13` → 确认 Deep Dives 下方出现「专题洞察」Section + GitHub 项目入口卡片
3. 点击 GitHub 入口卡片 → 确认跳转到 `/specialized/github/2026-07-13`，页面渲染项目列表和领域筛选
4. 访问旧日报 `http://localhost:3000/dashboard/2026-07-12` → 确认无 `specializedBrief` 时正常降级（不显示专题洞察 Section）

- [ ] **Step 3: TypeScript 最终检查**

```bash
pnpm typecheck && pnpm lint
```

Expected: 零错误，零警告。

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "feat(phase-1): complete GitHub specialized analysis pipeline + frontend"
```

---

## Phase 2/3 Preview

Phase 1 完成后，Phase 2 (Paper) 和 Phase 3 (Product) 遵循相同模式：

| Phase | Stage 2 标注 | Stage 3 分析 | 前端 |
|-------|-------------|-------------|------|
| Paper | `PaperTags` (已在 Task 1 定义) | `PaperAnalysis` schema + paper-analyst persona | `PaperCard` + `/specialized/paper/[date]` |
| Product | `ProductTags` (已在 Task 1 定义) | `ProductAnalysis` schema + product-analyst persona | `ProductCard` + `/specialized/product/[date]` |

每 Phase 约 5 个 task（schema → stage 2 → stage 3 → stage 4b → frontend），可复用 Phase 1 的全部基础设施（SpecializedTags 容器、Stage 3 派发逻辑、SpecializedBriefSection）。
