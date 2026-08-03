---
title: How the words we teach English language learners changed
source: https://pudding.cool/2026/07/essential-words/
author:
- '[[c-oreills]]'
published: '2026-08-02'
created: '2026-08-03'
manifest_dates:
- '2026-08-03'
description: 'Article URL: https://pudding.cool/2026/07/essential-words/ Comments
  URL: https://news.ycombinator.com/item?id=49145590 Points: 219 # Comments: 168'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 4f7f0a562dddabdc
source_type: community_discussion
tldr: The Pudding发布数据新闻，对比1953年通用词汇表GSL（2,284词）与2023年新版通用词汇表NGSL 1.2（2,809词）：70年间628词被删、1,153词新增。词汇从山羊、面粉、苹果等具体日常事物转向抵押贷款、公司、尽管等抽象制度概念，并新增大量限定程度与确定性的副词。
objective_summary: The Pudding于2026年7月发表数据新闻《How the words we teach English language
  learners changed》，运用USAS语义标注、Brysbaert具象度评分与NLTK词性标注，对比1953年与2023年两份面向英语学习者的基础词汇表。结果显示1,656词保留、628词删除、1,153词新增，新词表覆盖率约90%而旧表约84%。词汇变化表明日常生活重心从具体物质世界转向制度与抽象系统，新增副词主要用于限定程度、频率与确定性。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - The Pudding
  - UCREL
  technologies:
  - USAS
  - NLTK
  - General Service List
  - New General Service List
  key_people:
  - Brysbaert
  - Stoeckel
key_logic_flow:
- 文章对比了1953年发布的General Service List（2,284词）与2023年发布的New General Service List 1.2（2,809词），两份词表均为英语二语学习者设计的教学工具。
- 两份词表共有1,656词保留、628词被删除、1,153词被新增，删除词多与具体物质世界相关（如山羊、面粉、伞），新增词多为抽象制度概念（如抵押贷款、公司、尽管）。
- 经UCREL语义分析系统标注后，食品农牧、物体器具等物理世界类别缩小，而政府、机构、抽象概念等类别扩大，反映日常生活从自给自足转向制度系统。
- Brysbaert具象度评分显示新词表抽象词占比上升；抽象词依赖副词来限定程度、频率与确定性，因此新增了较多副词（如absolutely、relatively、approximately）。
- 作者将全部保留、删除与新增单词连同语义标签、具象度评分和词性标注整理为公开电子表格，供读者查阅与复核分析结论。
object_mentions:
- object_type: dataset
  name: General Service List
  canonical_name: General Service List (GSL)
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 1953年发布的通用词汇表General Service List收录约2,300个英语常用词，作为英语学习者的基础教学工具，覆盖率约84%。
  article_id: 4f7f0a562dddabdc
- object_type: dataset
  name: New General Service List 1.2
  canonical_name: New General Service List (NGSL)
  url: https://www.newgeneralservicelist.com/
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 新版通用词汇表New General Service List 1.2于2023年发布，收录2,809个词条，据称覆盖超过90%的一般英语使用场景。
  article_id: 4f7f0a562dddabdc
- object_type: project
  name: UCREL Semantic Analysis System
  canonical_name: USAS
  url: https://ucrel.lancs.ac.uk/usas/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 文章使用UCREL语义分析系统USAS对两份词表的单词进行语义标注，将其归入21个主题类别以观察词汇分布的变迁。
  article_id: 4f7f0a562dddabdc
- object_type: project
  name: NLTK
  canonical_name: NLTK
  url: https://www.nltk.org/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 作者使用NLTK自然语言工具包对词汇进行词性标注，并手动修正误标词汇，以比较两份词表在词性构成上的差异。
  article_id: 4f7f0a562dddabdc
- object_type: dataset
  name: Brysbaert Concreteness Ratings
  canonical_name: Brysbaert et al. (2014) Concreteness Ratings
  url: https://link.springer.com/article/10.3758/s13428-013-0403-5
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 文章引用Brysbaert等人2014年发布的具象度评分数据集，该数据集为约四万个英语词条提供1到5级的具象性评分。
  article_id: 4f7f0a562dddabdc
- object_type: dataset
  name: All Tagged Words Spreadsheet
  canonical_name: GSL/NGSL Tagged Word Spreadsheet
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 作者将两份词表中保留、删除与新增的单词连同语义标签、具象度评分和词性标注整理为公开电子表格，供读者查阅与复核。
  article_id: 4f7f0a562dddabdc
extract_result: success
impact_score:
  score: 1.5
  reason: 该事件是 The Pudding 的数据新闻可视化作品，本质是语言学/英语教育领域的历时词表对比分析，并非 AI 行业事件。虽然文中使用了 USAS
    语义标注、Brysbaert 具象度评分、NLTK 词性标注等 NLP 方法，但这些均为既有的成熟工具，文章未提出新算法、新架构，也未涉及 AI 产品发布、论文、融资或竞争格局变化。按评分标准，1-3
    分属于日常更新、小圈子自嗨范畴，该文对 AI 行业短期冲击力可忽略，故评 1.5 分。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 该文章与 AI 研发无直接关联，开发者最多关注其语料标注方法论的可复现性与公开数据集质量
hype_assessment:
  level: low
  reason: 文章是典型的数据新闻，方法论透明（明确标注 USAS、Brysbaert、NLTK 三个工具），并附公开电子表格供读者复核结论，通篇无'颠覆'、'革命性'等
    PR 滥用词汇。全文均为可验证的数据分析而非概念包装，炒作水分极低。
information_entropy: medium
domain_disruption:
  technical_innovation: 无本质技术突破。该文是将既有 NLP 工具（UCREL USAS 语义标注、Brysbaert 具象度评分、NLTK
    词性标注）应用于 1953/2023 两份英语词表的历时对比，方法论成熟且非首创，未引入新算法或新架构，真正的价值在于数据新闻的叙事视角而非技术本身。
  business_model: 无直接商业模式影响。对 AI 教育领域仅有间接参考价值：NGSL 2023 词表可作为自适应英语学习 SaaS 的词汇基准、LLM
    词汇评测集或教育产品的语料锚点，但该文本身不构成任何商业模式变革。
engineering_complexity: production_ready
compound_value:
  score: 2.5
  reason: 这是一篇数据新闻作品而非可积累的商业资产：核心交付物是公开电子表格与交互文章，无专有数据护城河，不产生直接现金流或复利效应，3-5年后不会成为行业基础设施。但其揭示的结构性趋势（日常语言从具体物质世界向抽象制度系统迁移、数据驱动的词汇表正替代主观编排的传统词表）对AI语言学习产品的课程数据策略有间接参考价值，这也是唯一的长期信号价值。综合判定为低复利事件。
value_capture_layer: end_application
moat_impact: neutral
key_beneficiaries:
- The Pudding
- UCREL
- Duolingo
- Vocabulary.com
competitive_casualty:
- 传统 ESL 教材出版商
- 依赖旧版词汇框架的课程产品
market_opportunities:
- 教育科技团队可利用NGSL 1.2公开词表与标注数据（语义类别、具象度评分、词性标注），构建面向英语学习者的个性化词汇教学与自适应测评产品，替代僵化的传统教材词表
- 数据新闻或语言研究团队可复刻该分析管线（USAS语义标注+NLTK词性标注+具象度评分），开发多语言词汇变迁追踪工具，为出版社、教育机构和语言政策制定者提供数据化决策服务
- AI口语/写作辅导产品可将具象度评分与程度/确定性副词标注纳入讲解引擎，针对不同抽象度词汇动态调整示例与解释层级，提升非母语学习者的理解效率
risk_matrix:
  regulatory: 无
  technological: 基于固定词表的传统词汇教学路线面临被LLM个性化自适应学习替代的风险；NGSL词表本身也可能随语言演变与技术变革再次过时，静态词表方法论存在技术迭代压力
  competitive: 开源数据极易被大型EdTech平台（如Duolingo、自适应学习系统等）整合吸收，独立工具与内容创业者的差异化空间受挤压，数据价值可能被巨头低成本复制
  ethical: 词表选择隐含价值判断——'essential words'向制度与抽象概念（mortgage、corporation、legislation）倾斜，反映并可能固化西方制度化生活方式的偏见；将其作为标准化教学内容可能对非西方文化背景的学习者构成隐性认知门槛
  additional:
  - 词汇变化与社会演变的因果关系需谨慎解读，数据新闻呈现的相关性不应被过度引申为教学或政策决策依据，存在误读与过度推断风险
confidence:
  impact: medium
  compound: medium
  hype: high
actionable_insight: monitor
object_insights:
- object_type: project
  name: UCREL Semantic Analysis System
  canonical_name: USAS
  url: https://ucrel.lancs.ac.uk/usas/
  positioning: USAS是兰卡斯特大学UCREL团队开发的语义标注系统，可将词汇自动归入21个主题语义类别，广泛用于语料库语言学研究。
  technical_signal: USAS通过固定语义分类体系将词汇自动归入21个主题类别，文章据此量化对比两份词表的语义分布变迁。
  adoption_signal: 文章将USAS称为常用语言学研究工具并直接采用其完成全词表标注，反映其在语料语义分析领域已有成熟应用基础。
  ecosystem_relevance: USAS由兰卡斯特大学UCREL维护，是语料库语言学工具链的组成部分，常与语义标注、语料检索等研究流程配合使用。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: USAS作为成熟的语义标注基础设施，被The Pudding用于跨70年的公众词汇变迁分析，证明其能够支撑面向大众的数据新闻研究；值得持续观察其语义类别体系能否跟上语言演变并保持分析价值。
  risk_notes:
  - USAS的21个固定语义类别可能难以覆盖新兴词汇与跨领域用法，自动归类结果需要结合人工复核才能保证准确。
  score: 5.0
  article_ids:
  - 4f7f0a562dddabdc
  evidence_snippets:
  - 文章使用UCREL语义分析系统USAS对两份词表的单词进行语义标注，将其归入21个主题类别以观察词汇分布的变迁。
- object_type: project
  name: NLTK
  canonical_name: NLTK
  url: https://www.nltk.org/
  positioning: NLTK是Python生态中历史悠久的自然语言处理工具包，提供词性标注、分词与语料处理等基础能力，广泛用于教学与文本分析。
  technical_signal: 文章使用NLTK对两份词表全部词汇进行词性标注，并人工修正误标项，以比较词表在词性构成上的差异。
  adoption_signal: NLTK被The Pudding数据新闻选用完成实际语料分析，显示其在学术与公众传播场景中都被作为默认NLP工具。
  ecosystem_relevance: NLTK是Python自然语言处理生态的基础组件，与语料库构建、词表分析等流程协同，长期服务于语言学教学与研究。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: NLTK凭借稳定的API与丰富的内置语料长期占据Python教学NLP的主流位置，本次被数据新闻用于词表对比也印证其易用性；在深度学习工具冲击下，其角色演变值得持续跟踪。
  risk_notes:
  - NLTK词性标注准确率有限，文中需手动修正误标词汇，面对复杂或口语化文本时可靠性与效率存在短板。
  score: 5.0
  article_ids:
  - 4f7f0a562dddabdc
  evidence_snippets:
  - 作者使用NLTK自然语言工具包对词汇进行词性标注，并手动修正误标词汇，以比较两份词表在词性构成上的差异。
---

Look through the words scattered around this page. Every one of them is among the most commonly used words in the English language.

They come from a 2023 list of about 2,800 words, shown to cover over 90% of general English use, intended for people learning the language.

This 2023 list is an update of an earlier one, made in 1953, which identified about 2,300 words as the essential vocabulary to everyday life at the time.

Between the two lists, 70 years apart, about 600 words were dropped, and over 1,100 were added. The rest remained as is.

Some of the changes make immediate sense: Telegraph dropped out; computer was added, along with website and blog. Tobacco was replaced by cigarette. Motherhood became mom, and dad was added too, though *fatherhood* was never on the list to begin with. The world changed and vocabulary surely followed.

But also: apple didn’t make the new list. Neither did fork, soap, umbrella or leaf, for example. It’s not that these things vanished from everyday life, but many hands-on words became less central to the core vocabulary. Dog stayed; goat and donkey didn’t. Bread stayed; breadmaking ingredients—flour and wheat—dropped. Cook is on the new list. Boil, bake, and fry are not.

And many of the words that were added, such as mortgage, corporation, appropriate, analysis, fairly, and despite, don’t look anything like the ones that were discarded. In fact, they are mostly abstract concepts that don’t look like anything at all.

# From Goat to Despite

How the Words We Teach English Language Learners Changed, and What That Says About Us

These “essential vocabulary” lists are called the General Service List (1953) and the New General Service List (2013, revised in 2023).

They were designed as teaching tools for people learning English as a second language, built from real-world usage data and extensively tested. The aim was a vocabulary list with as few words and as much coverage of everyday English usage. That coverage is high, over 90% for the 2023 list1 and about 84% for the 1953 list.2 To account for that much of the language, they had to track a significant portion of whatever people were actually reading and saying. A word earned its place by appearing often enough, across enough contexts, to be hard to avoid for the average person in an English-speaking society. Open the word lists panel on the right to browse through all the entries in both lists.

While these were practical tools, built to capture which words people need most, the answer also doubles as a snapshot of ordinary life, 70 years apart: what people were expected to engage with, and had to deal with, in their daily lives.

Treating the lists as an indirect record of day-to-day life, I went through the differences between them from a few angles: what the words were about, how tangible were they, and to which parts of speech they belonged.

## The Expanding World

I started by using a common linguistics research tool3 that sorted all of the words by meaning. It assigned each word to one of 21 subject categories, based on typical usage: Food and Farming, the Body and the Self, Government and Public, Language and Communication, and so on. Together, they suggested what kind of world each list was built for.

Data source: all words run through the UCREL Semantic Analysis System (USAS).

The categories that shrank are mostly those that have to do with the immediate, physical world, while the gains are those furthest from it.

To better see this, the categories can be oriented spatially. Some categories describe you: your body and emotions. Some describe what’s immediately around you: food, objects, and the natural world. Others name systems you participate in: government, institutions, society, and culture. And some have no location at all: abstract concepts, reasoning, and processes. When we look at the data grouped by *physical scope,* the pattern of change seems to point in a specific direction.

## Data source: all words run through the UCREL Semantic Analysis System (USAS), then grouped into five umbrella-term domains. Expand to view the full category breakdown.

**The Self:**Emotion | The Body and the Individual**Local/Immediate:**Substances, Materials, Objects and Equipment | Food and Farming | Life and Living Things | Architecture, Housing and the Home | World and Environment**Institutional:**Money and Commerce in Industry | Government and Public | Education | Science and Technology**Social/Communicative:**Social Actions, States, and Processes | Movement, Location, Travel and Transport | Language and Communication | Entertainment, Sports and Games | Arts and Crafts**Universal/Abstract:**General and Abstract Terms | Psychological Actions, States and Processes | Numbers and Measurement | Names and Grammar | Time

In hindsight, the shift makes sense. By 1957, four years after the original list was published, white-collar workers outnumbered blue-collar for the first time in US history. And by 2000, fewer than one in four workers did manual labor. The stuff people encountered in their daily lives, what they needed to talk about, and the systems they had to navigate all changed.

The vocabulary lists, built from the language of their respective eras, tracked those changes. The shifts reflect a life that moved further from its own making: less tied to tools, animals, food, and the body; more tied to national or global institutions, categories, systems, and ideas.

The new vocabulary—mortgage, legislation, perspective, involvement, improvement, assumption, evaluation—are words you can’t weigh, point to, or hold in your hand. These words shape your life, but they do it without occupying physical space.

## Harder to Picture

To better understand whether there was a shift in vocabulary describing the physical world, I compared each word to a database that rates its tangibility on a scale of 1 to 5 (called a “concreteness rating4”). A rating of 5 means you can experience the word directly with your senses, while a rating of 1 means you can’t.

Kernel density estimation, bandwidth 0.08 · Data source: Brysbaert et al. (2014)

This shift matters because abstract and concrete words are processed by our brains in different ways. When you read axe, your brain doesn’t just decode letters, it reaches for something: an image, a weight, or a gesture. The word activates both a verbal label and a sensory trace. Psychologists call this dual coding:5 Concrete words travel through two channels, verbal and sensory; abstract words travel through one. Two channels mean two retrieval pathways, which is why concrete words are “stickier,” easier to hold in a line of thought and faster to recall. Abstract words, on the other hand, are purely verbal, and have to be understood through language alone.

To put it another way: Concrete words are easier for us to process because they are bundled with a web of associations, tactile experiences, and memories that anchor their meaning. Here’s a more detailed view of the shift away from concrete language:

Data source: Brysbaert Concreteness ratings for 40 thousand generally known English word lemmas. The dataset provided 99.8% coverage of the words in both lists. 6 words not in the dataset are not included in this chart: *as, dialog, english, gaiety, madden, old-fashioned.*

While concrete words have sensory grounding to carry their meaning, abstract words rely on other parts of speech to specify, soften, or sharpen what they mean. That help tends to come from one particular corner of the language: adverbs.

## How Much, How Often, How Certain

The 2023 list contains more words overall (2,809 vs. 2,284). All changes mentioned in the text reflect each category's share of its list, not raw counts. Data source: NLTK (Natural Language Toolkit), with manual correction of mislabeled words.

Axe doesn’t need an adverb to modify it; you know what it is. But acceptable, relevant, and adequate come with conditions, qualifications, and degrees that need to be spelled out. Adverbs do precisely that: language to calibrate language.

Look through all the adverbs that were added:

Most of the adverbs specify degree, frequency, certainty, and extent. Some hedge (somewhat, partly, relatively, possibly, approximately). Others assert (absolutely, definitely, entirely, exactly, precisely). They're all doing the same kind of work: Take a statement and tell you how much of it is true, how often, and how certain. It’s as if the world now requires you to be more precise about everything.

## Further

Bread survived both lists. Flour, wheat, harvest and bake didn’t. The word for what sustains us remained essential, while the words for how we’d make it weren’t. That might be the most honest summary of what happened.

The world that made the 2023 list is more regulated, more connected, and in many ways more capable than the one behind the 1953 list. It’s a world further than our kitchen or home, reaching across economies, institutions, and democracies.

Today's vocabulary reflects a life that isn’t self-contained, but rather more systemic. It’s not so much about what’s within arm’s reach, but more about the larger world we navigate through. That sort of long-distance connection requires a particular kind of language: expansive, abstract, and precise. And language, it turns out, can’t help itself. It keeps track.

## Methods & Notes

I compared two prominent vocabulary lists for English learners: the General Service List (GSL, 1953; 2,284 words) and the New General Service List (NGSL 1.2, 2023; 2,809 words). I labeled words appearing on both lists as “remained” (1,656), words only on the 1953 list as “removed” (628), and words only on the 2023 list as “added” (1,153).

The GSL words came from the Simple English Wiktionary GSL. The NGSL words came from the official NGSL 1.2 file (“alphabetized and lemmatized for research”).
The NGSL uses lemmas (one entry per word family); the GSL sometimes lists inflected forms as separate headwords. These lists track word forms deemed worth teaching based on frequency and usefulness, not abstract concepts. For example, the word *being* is on the GSL as its own headword and was not included in the NGSL, But this doesn’t mean the concept of existence left the language. In the NGSL it falls under *be*, which is on both lists.

## Why treat the lists as a portrait of everyday English?

Both lists were built for teaching, but external research suggests each covers a large share of everyday language use. About 84% of general English for the GSL and about 90% for the NGSL, depending on the text and how words are counted. I did not re-run those corpus analyses myself. I take the published materials as given and rely on coverage figures from the list authors and from follow-up studies (including an independent check on American English by Stoeckel, 2019 – see footnotes). That’s why the differences between the lists felt worth examining as more than a curriculum update, with the caveat that neither list is a neutral census of culture.

## Where can I find the data?

All tagged words: remained, removed, and added, with semantic tags, concreteness ratings, and part-of-speech labels are in this public spreadsheet. You can also browse the word lists in the word-list panel on the right side of this page.

## How did I sort words by meaning?

Each word was tagged with the UCREL Semantic Analysis System (USAS), using the 21 top-level categories. USAS also assigns much finer sub-categories (there are hundreds), but I stayed at the top level so the charts could show broad shifts without splitting the words into overly granular bins.

I chose not to correct mislabels. For example, *hammer, nail,* and *wax* are all tagged “General and Abstract Terms”, but in USAS’s finer tags, they read as actions (“to hammer,” “to nail,” “to wax”), not objects. Out of context, many of these words go multiple ways, and it didn’t feel right to override that case by case; USAS is an established linguistic framework, and swapping in my own judgment would mix two different standards.

For the second chart, I grouped USAS’s 21 categories into five “scope” domains (self, local, institutional, social, abstract). That grouping is my editorial choice, not part of USAS. It came from noticing a spatial quality to the trends seen across the 21 categories.

## How did I measure concreteness?

Concreteness ratings come from Brysbaert et al. (2014). I used these as-is. Six words weren’t in the database and were left out of the concreteness charts: *as, dialog, english, gaiety, madden,* and *old-fashioned.*

## How did I tag parts of speech?

Parts of speech were tagged with NLTK, simplified to five categories. Here I did intervene, but only when a word was clearly mislabeled (132 words, 3.8% of the list; mostly adjectives mislabeled as nouns). When a word can act as more than one part of speech depending on context, I left the tag as-is and deferred to NLTK as the established framework, using the primary, most common label. Here I also used an LLM strictly to help flag potential errors in NLTK’s output.

## What are the limitations?

Both lists rank words by frequency, then apply learner-focused curation. Michael West’s 1953 list especially reflects period pedagogy. He favored general-purpose vocabulary over emotional or highly specific words, not just whatever appeared most often (Therova, 2020, summarizing West, 1953, pp. ix–x). Some of what looks like “1950s life” may also be how mid-century ESL teaching filtered the language. I still treat the lists as a portrait of everyday English because both cover a large share of running text and speech that goes well beyond the classroom.

## Footnotes

- On NGSL’s ~90% coverage: Browne, Culligan & Phillips, NGSL project. See also: A New General Service List: The Better Mousetrap We’ve Been Looking for?, Browne (2014); and An Examination of the New General Service List, Stoeckel (2019). ⏎
- On GSL’s ~84% coverage:
*A general service list of English words with semantic frequencies,*West (1953); The New General Service List: A core vocabulary for EFL students and teachers, Cambridge ELT (2018). ⏎ - UCREL: Semantic Analysis System (USAS). ⏎
- Concreteness ratings for 40 thousand generally known English word lemmas, Brysbaert, M., Warriner, A. B., & Kuperman, V. (2014). Behavior Research Methods, 46, 904–911. ⏎
- Why are pictures easier to recall than words? Paivio, A., Rogers, T.B. & Smythe, P.C. Psychon Sci 11, 137–138 (1968). ⏎