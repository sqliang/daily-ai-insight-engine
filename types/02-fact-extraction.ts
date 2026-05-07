// ============================================================================
// 区块二：事实提炼与浓缩 (Fact Extraction)
// [核心价值]：滤除修辞、情绪和废话，将非结构化长文本压缩为高密度的客观事实。
// ============================================================================
export interface FactExtraction {
    /**
     * 极简一句话总结 (TLDR)
     * - 类型：字符串（限制 80 字以内）
     * - 定义与语义：剔除所有修饰语，只讲核心事实。这是列表页的最强锚点。
     * - 与 objectiveSummary 的区分：tldr 是扫描单位（列表页），objectiveSummary 是阅读单位（详情页）。
     */
    tldr: string;

    /**
     * 极简客观事实 (objectiveSummary)
     * - 类型：字符串 (限制 150 字以内)
     * - 定义与语义：剥离一切主观形容词，只用最冷峻的语言描述 5W1H（谁、什么时候、做了什么、结果如何）。
     * - 为什么用：对抗信息过载的"第一道防线"。很多科技新闻标题党泛滥，这个字段要求 AI 扮演无情的"事实提取器"，让阅读者一眼看透事件本质。
     */
    objectiveSummary: string;

    // eventType (核心事件分类)
    // infrastructure_update (基建演进：如新模型发布、芯片算力更新)
    // framework_tools (框架与工具：如新的 Agent 框架、开发者工具开源)
    // capital_movement (资本动向：如巨额融资、并购、财报)
    // application_landing (应用落地：具体的 ToB/ToC AI 产品发布)
    // policy_and_safety (政策与安全：监管、版权诉讼、安全事故)
    // 定义与语义：将复杂的现实事件进行降维，强制归入最核心的宏观赛道。
    // 背后的思维维度：这是构建宏观趋势大屏（如饼图、柱状图）的基石。通过这个字段，系统可以统计出“本周资本是在投基建还是在投应用”，从而敏锐捕捉行业周期的切换。
    eventType: 'infrastructure_update' | 'framework_tools' | 'capital_movement' | 'application_landing' | 'policy_and_safety';

    /**
     * 认识论状态：这条信息的声明本质是什么？
     * - verified_fact：已验证事实（如 GitHub 正式开源、财报发布、产品上线）。
     * - pr_statement：公关声明（官方发声但包含包装话术，尚未交付的"期货"）。
     * - theoretical_claim：理论主张（如 arXiv 论文 Benchmark，尚未经工业界验证）。
     * - rumor_leak：坊间传闻或灰度泄露（如媒体爆料、匿名信源）。
     * - 为什么用：物理隔离"确凿事实"与"期货大饼"，聚合时赋予不同可信度权重。rumor 即使 impactScore 高也应降权。
     */
    epistemicStatus: 'verified_fact' | 'pr_statement' | 'theoretical_claim' | 'rumor_leak';

    // entities (核心实体拓扑)
    // 定义与语义：提取事件中涉及的具象化节点，分为三个子阵列：
    // companies: 涉及的核心企业或机构（如 OpenAI, 斯坦福大学）。
    // technologies: 涉及的核心 AI 技术名词（如 VLA, RAG, MCP, RLHF）。
    // key_people: 核心关键人物（如 Sergey Levine, Sam Altman）。
    // 背后的思维维度：“从孤立事件走向关系图谱”。这是构建词云和知识图谱的底层数据。如果 technologies 中连续三天高频出现 "MCP"，系统就能自动在日报中标记其为“爆发趋势词”。
    entities: {
        companies: string[];
        technologies: string[];
        key_people: string[];
    };

    /**
     * 核心逻辑脉络/关键事实清单 (keyLogicFlow)
     * - 类型：字符串数组 (3-6 条)
     * - 定义与语义：文章骨架的 X 光片。如果是技术文章，提取其架构创新的步骤；如果是商业新闻，提取其融资背后的对赌协议或战略意图。
     * - 为什么用："结构化思维还原"。将线性的长文本还原为树状或步骤状的逻辑块，满足高阶读者"跳读式理解"的需求，不仅知其然，更知其所以然。
     */
    keyLogicFlow: string[];
}
