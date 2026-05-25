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
