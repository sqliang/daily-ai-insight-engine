// ============================================================================
// 区块三：深度研判与量化分析 (Deep Analysis & Scoring)
// [核心价值]：利用 AI 的推理能力，对事件进行多维度的"价值审判"。
// 三维度平铺于 DailyAIInsight，Phase 2 并行处理后汇总聚合。
// ============================================================================

// ============================================================================
// 3.1 定性研判 (Qualitative Assessment)
// 回答："这是什么事件，当下有多重要？"
// ============================================================================
export interface QualitativeAssessment {
    /**
     * 短期行业冲击力 (1-3 个月)
     * - 1-3分：日常更新，小圈子自嗨
     * - 4-7分：重要产品发布或高额融资，改变局部竞争格局
     * - 8-10分：行业范式转移（如 ChatGPT 发布、Transformer 论文发表）
     * - 日报 Top 5 榜单的核心排序指标
     */
    impactScore: {
        score: number;
        /** 强制 CoT：先给出评分依据，再给出评分 */
        reason: string;
    };

    /**
     * 行业情绪倾向
     * - positive：利好 AI 行业（如技术突破、开源发布、政策松绑）
     * - negative：利空 AI 行业（如安全事故、监管收紧、关键人才流失）
     * - neutral：中性信息（如例行财报、人事变动）
     * - mixed：影响复杂/多空交织（如大厂开源挤压小厂但利好生态）
     * - 与 impactScore 正交：高冲击力可以是坏消息，低冲击力可以是好消息
     */
    sentiment: 'positive' | 'negative' | 'neutral' | 'mixed';

    /**
     * 开发者 / 核心圈情绪反应。
     * - 标注什么：用脚投票的开发者群体的真实反馈，而非大众媒体的表层叙事。
     * - 为什么用：开发者情绪是技术落地阻力/推力的最前置指标——大众觉得牛逼，但开发者可能觉得 API 太贵或协议流氓。
     * - 与 sentiment 的区分：sentiment 判断事件对行业的客观影响方向，developerSentiment 捕捉核心圈的主观情绪温度。
     */
    developerSentiment: {
        tone: 'excited' | 'skeptical' | 'frustrated' | 'neutral';
        /** 开发者关注或争议的焦点（如"API 定价"、"开源协议"、"性能水分"） */
        primaryFocus: string;
    };

    /**
     * 炒作指数/水分预警
     * - low：实打实的干货
     * - medium：存在一定包装
     * - high：严重的概念炒作，大屏上将打上红色预警标签
     */
    hypeAssessment: {
        level: 'low' | 'medium' | 'high';
        /** 强制 CoT：识别"颠覆"、"革命性"等 PR 滥用词汇，给出判定依据 */
        reason: string;
    };

    /**
     * 信息熵 / 干货浓度。
     * - high：高密度新知（开创性理念、颠覆性架构、独家爆料），值得逐字精读。
     * - medium：常规迭代（版本更新、功能补齐、行业研报），可快速扫读。
     * - low：炒作冷饭（重复解读、情绪宣泄、无实质内容），可跳过。
     * - 与 hypeAssessment 正交：低水分文章也可能是旧闻重发（低熵），高水分文章也可能有真实突破（高熵）。
     */
    informationEntropy: 'high' | 'medium' | 'low';

    /**
     * 领域破局点解析：强制跨域思考，将技术"硬实力"与商业"软实力"解耦分析。
     * - 即使是纯商业新闻，也需反推其背后的技术驱动力
     * - 即使是纯学术论文，也需推演其潜在的商业化路径
     */
    domainDisruption: {
        /** 技术架构或工程实现的本质突破。若是纯商业新闻，简述其背后的技术驱动力；若确实无关则填"无" */
        technicalInnovation: string;
        /** 对商业模式或 SaaS 生态的重塑力。若是纯学术论文，推演其潜在商业化路径；若确实无关则填"无" */
        businessModel: string;
    };

    /**
     * 工程落地复杂度 / 技术成熟度。
     * - conceptual：概念验证阶段（白皮书、博客设想）。
     * - prototype：实验室原型 / 论文代码（跑通了，但不可靠）。
     * - production_ready：生产级可用（SLA 有保障，可直接接入业务）。
     * - infrastructure：泛用型基建（已成为行业标准，如 Transformer、Kubernetes）。
     * - 为什么用：防忽悠机制。矫正市场对短期技术落地速度的盲目乐观。
     */
    engineeringComplexity: 'conceptual' | 'prototype' | 'production_ready' | 'infrastructure';
}

// ============================================================================
// 3.2 价值与格局评估 (Value & Moat Assessment)
// 回答："长期价值沉淀在哪里，竞争格局如何重塑？"
// ============================================================================
export interface ValueAssessment {
    /**
     * 长期复利价值 (3-5 年)
     * - 1-3分：昙花一现，无长期积累效应
     * - 4-7分：有潜力成为细分赛道基础设施，但需持续验证
     * - 8-10分：极强复利效应，3-5 年后大概率仍是行业基石
     * - 设计理念：引入"价值投资"思维，打捞当前不显山露水但具备底层创新的事件
     */
    compoundValue: {
        score: number;
        /** 强制 CoT：拒绝拍脑袋打分 */
        reason: string;
    };

    /**
     * 价值捕获层：此次事件的红利最终沉淀在科技栈的哪一层？
     */
    valueCaptureLayer: 'hardware_compute' | 'cloud_platform' | 'foundation_model' | 'agent_middleware' | 'end_application';

    /**
     * 护城河影响：事件对行业竞争格局的重塑
     */
    moatImpact: 'strengthens_monopoly' | 'democratizes_access' | 'creates_new_moat' | 'neutral';

    /**
     * 关键受益方：此次事件中可能获益的具体公司或项目
     * 注意：与 EcosystemTopology 中的 protagonist/allies（事件直接参与方）不同，
     * 此字段聚焦中长期价值流动的最终受益者
     */
    keyBeneficiaries: string[];

    /**
     * 竞争波及方 / 受损者。
     * - 标注什么：因该事件护城河受损的实体或细分赛道（如大厂发布免费原生功能，导致套壳 SaaS 丧失生存空间）。
     * - 为什么用：风险预警的关键指标。识别受益方只能看到机会，识别受损方才能看到风险的全貌。
     * - 与 keyBeneficiaries 互补：一个看赢家，一个看输家，二者共同描绘事件的格局重塑力。
     */
    competitiveCasualty: string[];
}

// ============================================================================
// 3.3 前瞻预测与行动转化 (Foresight & Actionability)
// 回答："有什么风险，我该做什么？"
// [核心价值]：从"理解过去"转向"指导未来"，输出具有实操意义的指南。
// ============================================================================
export interface ForesightAndActionability {
    /**
     * 赛道机会与落地启发
     * - 基于该事件推演的 1-3 个具体商业变现、产品迭代或个人技能提升方向
     * - 例："长文本法律合同审查 SaaS 赛道迎来爆发"，而非泛泛的"去训练大模型"
     */
    marketOpportunities: string[];

    /**
     * 风险矩阵：强制 AI 从四个维度审视潜在下行风险。
     * - 结构化维度确保不遗漏，additional 作为自由补充的安全阀。
     * - 监管与伦理拆分：regulatory 聚焦合规与法律风险，ethical 聚焦数据伦理与社会影响。
     */
    riskMatrix: {
        /** 监管与合规风险（如 AI Act、出口管制、版权诉讼） */
        regulatory: string;
        /** 技术替代风险（如架构过时、论文撤回、开源替代） */
        technological: string;
        /** 竞争格局风险（如巨头入场、价格战、生态挤压） */
        competitive: string;
        /** 数据伦理与社会影响（如偏见歧视、深度伪造、数据投毒、隐私侵犯、就业冲击） */
        ethical: string;
        /** 补充风险：非上述四类的额外风险（可选，为空数组表示无额外风险） */
        additional: string[];
    };

    /**
     * AI 研判置信度：标记 LLM 对自身判断的确定程度，避免"所有结论同样可信"的错觉
     */
    confidence: {
        /** 短期冲击力判断的置信度 */
        impact: 'high' | 'medium' | 'low';
        /** 长期复利判断的置信度（通常低于短期） */
        compound: 'high' | 'medium' | 'low';
        /** 炒作判定的置信度 */
        hype: 'high' | 'medium' | 'low';
    };

    /**
     * 可执行建议：分析做完后，读者应该做什么
     * - deep_dive：值得深入阅读原文
     * - monitor：持续跟踪后续进展
     * - strategic_invest：具备战略投资/研究方向价值
     * - speculative_watch：投机性关注，不确定性高
     * - ignore：噪音，可跳过
     *
     * 注意：此字段为分类标签，具体战略陈述见 EndgameStrategy.strategicTakeaway
     */
    actionableInsight: 'deep_dive' | 'monitor' | 'strategic_invest' | 'speculative_watch' | 'ignore';
}

// ============================================================================
// 以下按时间维度拆分为三个独立接口，在 DailyAIInsight 中平铺使用
// ============================================================================
