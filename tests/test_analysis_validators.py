"""
tests/test_analysis_validators.py — Stage 3 分析结果容错测试

覆盖 LLM 在批量分析中常见的结构偏差：根字段误嵌套、列表字段返回字符串、
以及字段拼写轻微错误。目标是让可恢复的格式问题不阻塞日报流水线。
"""

from pipeline.analysis.validators import (
    validate_foresight,
    validate_paper,
    validate_qualitative,
    validate_value,
)


def test_validate_qualitative_promotes_nested_root_fields():
    """impactScore/hypeAssessment 中误嵌套的根字段应被提升并通过校验。"""
    result = validate_qualitative(
        {
            "impactScore": {
                "score": 0.8,
                "reason": "low impact",
                "sentiment": "neutral",
                "developerSentiment": {"tone": "neutral", "primaryFocus": "scope"},
                "hypeAssessment": {
                    "level": "low",
                    "reason": "plain",
                    "informationEntropy": "low",
                    "domainDisruption": {"technicalInnovation": "无", "businessModel": "无"},
                    "engineeringComplexity": "production_ready",
                },
            }
        }
    )

    assert result.impact_score.score == 1.0
    assert result.sentiment.value == "neutral"
    assert result.information_entropy.value == "low"


def test_validate_qualitative_uses_hype_primary_focus_as_reason():
    """hypeAssessment 缺 reason 但有 primaryFocus 时应作为 reason 使用。"""
    result = validate_qualitative(
        {
            "impactScore": {"score": 5, "reason": "moderate"},
            "sentiment": "neutral",
            "developerSentiment": {"tone": "neutral", "primaryFocus": "focus"},
            "hypeAssessment": {"level": "medium", "primaryFocus": "packaged claim"},
            "informationEntropy": "medium",
            "domainDisruption": {"technicalInnovation": "无", "businessModel": "无"},
            "engineeringComplexity": "prototype",
        }
    )

    assert result.hype_assessment.reason == "packaged claim"


def test_validate_value_promotes_compound_value_fields():
    """compoundValue 中误嵌套的根字段应被提升并通过校验。"""
    result = validate_value(
        {
            "compoundValue": {
                "score": 4.5,
                "reason": "niche infra",
                "valueCaptureLayer": "application",
                "moatImpact": "neutral",
                "keyBeneficiaries": ["developers"],
                "competitiveCasualty": [],
            }
        }
    )

    assert result.value_capture_layer.value == "end_application"
    assert result.key_beneficiaries == ["developers"]


def test_validate_value_defaults_missing_root_fields():
    """只有 compoundValue 的低信息输出应补保守默认值而不是阻塞流水线。"""
    result = validate_value(
        {
            "compoundValue": {
                "score": 3,
                "reason": "policy-driven market split",
            }
        }
    )

    assert result.value_capture_layer.value == "agent_middleware"
    assert result.moat_impact.value == "neutral"
    assert result.key_beneficiaries == []


def test_validate_foresight_repairs_risk_matrix_typo():
    """riskMatrix.regularoty 拼写错误应被修复为 regulatory。"""
    result = validate_foresight(
        {
            "marketOpportunities": [],
            "riskMatrix": {
                "regularoty": "policy audit risk",
                "technological": "latency risk",
                "competitive": "fast followers",
                "ethical": "review burden",
            },
            "confidence": "medium",
            "actionableInsight": "watch",
        }
    )

    assert result.risk_matrix.regulatory == "policy audit risk"
    assert result.risk_matrix.additional == []


def test_validate_paper_repairs_typo_and_string_list():
    """论文分析中的 gapAdressed 拼写错误和字符串列表字段应自动修复。"""
    result = validate_paper(
        {
            "paperMetadata": {"title": "Paper", "paperUrl": "https://example.com/paper"},
            "researchProblem": {
                "coreQuestion": "How?",
                "motivation": "Need better methods",
                "significance": "practical",
                "gapAdressed": "Missing robust benchmark",
            },
            "methodology": {
                "approachSummary": "Method",
                "noveltyType": "algorithmic",
                "technicalDepth": "moderate",
            },
            "experimentalRigor": {
                "benchmarkCoverage": "standard",
                "baselineComparison": "adequate",
                "ablationQuality": "adequate",
                "reproducibilityLevel": "partially",
                "claimedImprovement": "better",
            },
            "limitationsAndHonesty": {
                "statedLimitations": "small benchmark",
                "overclaimingAssessment": "honest",
                "generalizationConcern": "unknown",
            },
            "industrialRelevance": {
                "computeRequirements": "datacenter",
                "integrationReadiness": "needs_engineering",
                "costEfficiencyAnalysis": "unclear",
            },
            "relatedWorkContext": {
                "advancementOverPrior": "incremental",
                "opensNewDirection": False,
            },
        }
    )

    assert result.research_problem.gap_addressed == "Missing robust benchmark"
    assert result.limitations_and_honesty.stated_limitations == ["small benchmark"]
