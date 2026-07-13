"""
pipeline/analysis/fuzzy_maps.py — Stage 3 模糊枚举匹配映射表

为每个需要 AI 输出的枚举字段维护一张 宽松值 → 标准值 的映射表。
当 LLM 返回非标准枚举值（如 "bullish" 而非 "positive"）时，
validator 通过这些映射表进行模糊匹配修正。

所有映射表均为纯数据（dict[str, str]），无业务逻辑。
被 validators.py 导入使用。

映射表覆盖范围：
    - Sentiment（行业情绪）
    - DeveloperTone（开发者情绪）
    - HypeLevel（炒作指数）
    - InformationEntropy（信息熵）
    - EngineeringComplexity（工程落地复杂度）
    - ValueCaptureLayer（价值捕获层）
    - MoatImpact（护城河影响）
    - ConfidenceLevel（AI 研判置信度）
    - ActionableInsight（可执行建议）
"""

# =============================================================================
# QualitativeAssessment 维度枚举
# =============================================================================

# --- Sentiment 行业情绪 ---
SENTIMENT_FUZZY: dict[str, str] = {
    "positive": "positive",
    "optimistic": "positive",
    "bullish": "positive",
    "good": "positive",
    "negative": "negative",
    "pessimistic": "negative",
    "bearish": "negative",
    "bad": "negative",
    "neutral": "neutral",
    "balanced": "neutral",
    "mixed": "mixed",
    "uncertain": "mixed",
    "complex": "mixed",
}

# --- DeveloperTone 开发者情绪 ---
DEVELOPER_TONE_FUZZY: dict[str, str] = {
    "excited": "excited",
    "enthusiastic": "excited",
    "positive": "excited",
    "skeptical": "skeptical",
    "skeptic": "skeptical",
    "doubtful": "skeptical",
    "cautious": "skeptical",
    "frustrated": "frustrated",
    "angry": "frustrated",
    "disappointed": "frustrated",
    "upset": "frustrated",
    "neutral": "neutral",
    "balanced": "neutral",
    "indifferent": "neutral",
    "mixed": "neutral",
}

# --- HypeLevel 炒作指数 ---
HYPE_LEVEL_FUZZY: dict[str, str] = {
    "low": "low",
    "minimal": "low",
    "none": "low",
    "substantive": "low",
    "medium": "medium",
    "moderate": "medium",
    "some": "medium",
    "high": "high",
    "extreme": "high",
    "overhyped": "high",
    "pump": "high",
}

# --- InformationEntropy 信息熵 ---
ENTROPY_FUZZY: dict[str, str] = {
    "high": "high",
    "dense": "high",
    "rich": "high",
    "medium": "medium",
    "moderate": "medium",
    "average": "medium",
    "low": "low",
    "sparse": "low",
    "thin": "low",
    "repetitive": "low",
}

# --- EngineeringComplexity 工程落地复杂度 ---
ENGINEERING_COMPLEXITY_FUZZY: dict[str, str] = {
    "conceptual": "conceptual",
    "concept": "conceptual",
    "theoretical": "conceptual",
    "theory": "conceptual",
    "paper": "conceptual",
    "research": "conceptual",
    "prototype": "prototype",
    "demo": "prototype",
    "experimental": "prototype",
    "poc": "prototype",
    "proof_of_concept": "prototype",
    "production_ready": "production_ready",
    "production": "production_ready",
    "shipping": "production_ready",
    "deployed": "production_ready",
    "live": "production_ready",
    "infrastructure": "infrastructure",
    "platform": "infrastructure",
    "foundational": "infrastructure",
    "standard": "infrastructure",
}

# =============================================================================
# ValueAssessment 维度枚举
# =============================================================================

# --- ValueCaptureLayer 价值捕获层 ---
VALUE_CAPTURE_FUZZY: dict[str, str] = {
    "hardware_compute": "hardware_compute",
    "hardware": "hardware_compute",
    "compute": "hardware_compute",
    "chip": "hardware_compute",
    "gpu": "hardware_compute",
    "cloud_platform": "cloud_platform",
    "cloud": "cloud_platform",
    "platform": "cloud_platform",
    "iaas": "cloud_platform",
    "foundation_model": "foundation_model",
    "model": "foundation_model",
    "llm": "foundation_model",
    "ai_model": "foundation_model",
    "agent_middleware": "agent_middleware",
    "middleware": "agent_middleware",
    "agent": "agent_middleware",
    "tool": "agent_middleware",
    "framework": "agent_middleware",
    "end_application": "end_application",
    "application": "end_application",
    "saas": "end_application",
    "product": "end_application",
}

# --- MoatImpact 护城河影响 ---
MOAT_IMPACT_FUZZY: dict[str, str] = {
    "strengthens_monopoly": "strengthens_monopoly",
    "monopoly": "strengthens_monopoly",
    "consolidation": "strengthens_monopoly",
    "winner_takes_all": "strengthens_monopoly",
    "democratizes_access": "democratizes_access",
    "democratization": "democratizes_access",
    "open": "democratizes_access",
    "accessible": "democratizes_access",
    "creates_new_moat": "creates_new_moat",
    "new_moat": "creates_new_moat",
    "differentiation": "creates_new_moat",
    "competitive_advantage": "creates_new_moat",
    "neutral": "neutral",
    "none": "neutral",
    "unchanged": "neutral",
}

# =============================================================================
# ForesightAndActionability 维度枚举
# =============================================================================

# --- ConfidenceLevel AI 研判置信度 ---
CONFIDENCE_FUZZY: dict[str, str] = {
    "high": "high",
    "confident": "high",
    "certain": "high",
    "strong": "high",
    "medium": "medium",
    "moderate": "medium",
    "uncertain": "medium",
    "low": "low",
    "speculative": "low",
    "weak": "low",
}

# --- ActionableInsight 可执行建议 ---
ACTIONABLE_INSIGHT_FUZZY: dict[str, str] = {
    "deep_dive": "deep_dive",
    "deepdive": "deep_dive",
    "research": "deep_dive",
    "study": "deep_dive",
    "read": "deep_dive",
    "monitor": "monitor",
    "watch": "monitor",
    "track": "monitor",
    "follow": "monitor",
    "strategic_invest": "strategic_invest",
    "invest": "strategic_invest",
    "build": "strategic_invest",
    "act": "strategic_invest",
    "speculative_watch": "speculative_watch",
    "speculative": "speculative_watch",
    "maybe": "speculative_watch",
    "ignore": "ignore",
    "skip": "ignore",
    "noise": "ignore",
    "pass": "ignore",
}


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


# =============================================================================
# PaperAnalysis 维度枚举
# =============================================================================

TECHNICAL_DEPTH_FUZZY: dict[str, str] = {
    "deeply_technical": "deeply_technical",
    "deep": "deeply_technical",
    "technical": "deeply_technical",
    "complex": "deeply_technical",
    "advanced": "deeply_technical",
    "heavy": "deeply_technical",
    "moderate": "moderate",
    "medium": "moderate",
    "average": "moderate",
    "normal": "moderate",
    "accessible": "accessible",
    "simple": "accessible",
    "easy": "accessible",
    "light": "accessible",
    "beginner": "accessible",
}

NOVELTY_TYPE_FUZZY: dict[str, str] = {
    "architectural": "architectural",
    "architecture": "architectural",
    "arch": "architectural",
    "new_architecture": "architectural",
    "model_design": "architectural",
    "algorithmic": "algorithmic",
    "algorithm": "algorithmic",
    "algo": "algorithmic",
    "new_algorithm": "algorithmic",
    "training_method": "training_method",
    "training": "training_method",
    "optimization": "training_method",
    "loss_function": "training_method",
    "data_centric": "data_centric",
    "data": "data_centric",
    "dataset": "data_centric",
    "data_driven": "data_centric",
    "theoretical": "theoretical",
    "theory": "theoretical",
    "proof": "theoretical",
    "analysis": "theoretical",
    "benchmark": "benchmark",
    "evaluation": "benchmark",
    "eval": "benchmark",
    "benchmarking": "benchmark",
}

SIGNIFICANCE_FUZZY: dict[str, str] = {
    "fundamental": "fundamental",
    "foundational": "fundamental",
    "breakthrough": "fundamental",
    "groundbreaking": "fundamental",
    "major": "fundamental",
    "practical": "practical",
    "applied": "practical",
    "useful": "practical",
    "engineering": "practical",
    "incremental": "incremental",
    "minor": "incremental",
    "small": "incremental",
    "improvement": "incremental",
    "iterative": "incremental",
    "niche": "niche",
    "specialized": "niche",
    "narrow": "niche",
    "specific": "niche",
    "limited": "niche",
}

BASELINE_COMPARISON_FUZZY: dict[str, str] = {
    "comprehensive": "comprehensive",
    "complete": "comprehensive",
    "extensive": "comprehensive",
    "thorough": "comprehensive",
    "adequate": "adequate",
    "sufficient": "adequate",
    "enough": "adequate",
    "reasonable": "adequate",
    "decent": "adequate",
    "selective": "selective",
    "selected": "selective",
    "cherry_picked": "selective",
    "partial": "selective",
    "weak": "weak",
    "poor": "weak",
    "insufficient": "weak",
    "lacking": "weak",
    "minimal": "weak",
}

ABLATION_QUALITY_FUZZY: dict[str, str] = {
    "thorough": "thorough",
    "complete": "thorough",
    "comprehensive": "thorough",
    "detailed": "thorough",
    "extensive": "thorough",
    "adequate": "adequate",
    "sufficient": "adequate",
    "enough": "adequate",
    "reasonable": "adequate",
    "decent": "adequate",
    "minimal": "minimal",
    "basic": "minimal",
    "simple": "minimal",
    "limited": "minimal",
    "absent": "absent",
    "none": "absent",
    "missing": "absent",
    "no_ablation": "absent",
}

REPRODUCIBILITY_FUZZY: dict[str, str] = {
    "fully_reproducible": "fully_reproducible",
    "fully": "fully_reproducible",
    "reproducible": "fully_reproducible",
    "complete": "fully_reproducible",
    "open_source": "fully_reproducible",
    "mostly_reproducible": "mostly_reproducible",
    "mostly": "mostly_reproducible",
    "largely": "mostly_reproducible",
    "partially": "partially",
    "partial": "partially",
    "somewhat": "partially",
    "not_reproducible": "not_reproducible",
    "not": "not_reproducible",
    "irreproducible": "not_reproducible",
    "closed": "not_reproducible",
}

OVERCLAIMING_FUZZY: dict[str, str] = {
    "honest": "honest",
    "accurate": "honest",
    "fair": "honest",
    "balanced": "honest",
    "modest": "honest",
    "mild_overclaim": "mild_overclaim",
    "mild": "mild_overclaim",
    "slight": "mild_overclaim",
    "minor_overclaim": "mild_overclaim",
    "some_overclaim": "mild_overclaim",
    "significant_overclaim": "significant_overclaim",
    "significant": "significant_overclaim",
    "major": "significant_overclaim",
    "overclaim": "significant_overclaim",
    "exaggerated": "significant_overclaim",
    "hype": "significant_overclaim",
}

COMPUTE_REQUIREMENTS_FUZZY: dict[str, str] = {
    "commodity": "commodity",
    "consumer": "commodity",
    "laptop": "commodity",
    "desktop": "commodity",
    "single_gpu": "commodity",
    "cheap": "commodity",
    "datacenter": "datacenter",
    "cluster": "datacenter",
    "multi_gpu": "datacenter",
    "server": "datacenter",
    "cloud": "datacenter",
    "supercomputer": "supercomputer",
    "hpc": "supercomputer",
    "large_scale": "supercomputer",
    "thousands_of_gpus": "supercomputer",
    "prohibitive": "prohibitive",
    "impossible": "prohibitive",
    "unaffordable": "prohibitive",
    "extreme": "prohibitive",
    "not_feasible": "prohibitive",
}

INTEGRATION_READINESS_FUZZY: dict[str, str] = {
    "ready_to_integrate": "ready_to_integrate",
    "ready": "ready_to_integrate",
    "production_ready": "ready_to_integrate",
    "deployable": "ready_to_integrate",
    "now": "ready_to_integrate",
    "needs_engineering": "needs_engineering",
    "engineering_required": "needs_engineering",
    "needs_work": "needs_engineering",
    "needs_optimization": "needs_engineering",
    "soon": "needs_engineering",
    "needs_research": "needs_research",
    "research_required": "needs_research",
    "needs_exploration": "needs_research",
    "experimental": "needs_research",
    "distant": "distant",
    "far": "distant",
    "unknown": "distant",
    "unclear": "distant",
    "long_term": "distant",
}
