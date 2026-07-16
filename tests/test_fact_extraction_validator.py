"""
tests/test_fact_extraction_validator.py — FactExtraction 容错校验测试

覆盖 Stage 2b 对 Agent 输出的本地修复逻辑，尤其是字段别名和
snake_case 混用时的超长文本截断，避免单篇文章因格式轻微漂移阻塞整批提取。
"""

from pipeline.extraction.fact_extraction.validator import _validate_fact_extraction


def _base_payload(**overrides):
    """
    构造一份最小可用的 FactExtraction Agent 返回值。

    参数：
        overrides: 覆盖默认字段的键值对

    返回：
        dict: 可供 validator 校验的原始字典
    """
    payload = {
        "tldr": "项目发布了新的安全分析工具。",
        "objectiveSummary": "研究者披露了一个 GitHub 相关安全事件，并说明其影响范围。",
        "eventType": "policy_and_safety",
        "epistemicStatus": "verified_fact",
        "entities": {
            "companies": ["GitHub"],
            "technologies": ["security"],
            "keyPeople": [],
        },
        "keyLogicFlow": ["事件被披露", "影响范围被说明", "后续修复仍需跟进"],
    }
    payload.update(overrides)
    return payload


def test_validator_truncates_objective_summary_alias():
    """objectiveSummary 超长时应自然截断到 schema 上限内。"""
    long_summary = "这是一个用于验证长度兜底的客观摘要，" * 20

    result = _validate_fact_extraction(
        _base_payload(objectiveSummary=long_summary)
    )

    assert len(result.objective_summary) <= 500


def test_validator_truncates_objective_summary_snake_case():
    """objective_summary 超长时也应被截断，而不是绕过别名兜底。"""
    long_summary = "这是一个使用 snake_case 字段的客观摘要，" * 20
    payload = _base_payload()
    payload.pop("objectiveSummary")
    payload["objective_summary"] = long_summary

    result = _validate_fact_extraction(payload)

    assert len(result.objective_summary) <= 500


def test_validator_truncates_tldr():
    """tldr 超长时应被截断到 schema 上限（250 字符）以内。"""
    long_tldr = "安全研究者披露 GitHub 相关零日漏洞投放活动，" * 10

    result = _validate_fact_extraction(
        _base_payload(tldr=long_tldr)
    )

    assert len(result.tldr) <= 250
