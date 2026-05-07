/**
 * AI 舆情分析日报系统核心认知模型 (Daily AI Insight Schema)
 * * 本模型摒弃了传统 RSS 的"表面事实罗列"，采用"领域驱动设计 (DDD)"与"价值投资视角"。
 * 旨在通过大模型将非结构化的嘈杂新闻，降维解构为：信息论状态、生态博弈、技术基元与商业护城河。
 * 它是构建自动化 AI 行业雷达、前端可视化大屏以及后续多 Agent 协同调度的核心数据契约。
 */

import type { BaseInfo } from './01-base-info';
import type { FactExtraction } from './02-fact-extraction';
import type { QualitativeAssessment, ValueAssessment, ForesightAndActionability } from './03-deep-analysis';

// ============================================================================
// 顶层结构：DailyAIInsight
// 设计流程：
//   Phase 1 → 提取 baseInfo + factExtraction（基础元信息 + 事实浓缩）
//   Phase 2 → 并行深度分析，三维度平铺（定性研判 / 价值评估 / 前瞻行动），汇总聚合
// ============================================================================
export interface DailyAIInsight {
    // ============================================================================
    // Phase 1：基础元信息 (Base Information)
    // ============================================================================
    baseInfo: BaseInfo;
    // ============================================================================
    // Phase 1：事实提炼与浓缩 (Fact Extraction)
    // ============================================================================
    factExtraction: FactExtraction;

    // ============================================================================
    // Phase 2：深度分析 —— 三组字段平铺，并行处理
    // ============================================================================
    /** 定性研判：当下 —— 事件本身是什么，有多重要？ */
    qualitativeAssessment: QualitativeAssessment;
    /** 价值评估：中长期 —— 价值流向哪里，格局如何重塑？ */
    valueAssessment: ValueAssessment;
    /** 前瞻行动：未来 —— 有什么风险，该做什么？ */
    foresightAndActionability: ForesightAndActionability;
}

