---
title: hasaneyldrm/exercises-dataset
source: https://github.com/hasaneyldrm/exercises-dataset
author: []
published: ''
created: '2026-07-14'
description: '1,324-exercise fitness dataset — animation GIFs, 180×180 thumbnails,
  muscle-group & equipment data, and step-by-step instructions in 6 languages. The
  exercise data layer behind the LogPress app. 💪 Exercises Dataset A comprehensive,
  ready-to-use fitness exercise dataset with 1,324 exercises — each with an animation
  GIF, 180×180 thumbnail image, category, body-part, equipment, target and muscle-group
  data, and step-by-step instructions in 9 languages (English, Spanish, Italian, Turkish,
  Russian, Chinese, Hindi, Polish, Korean). 📱 Powers the LogPress app — an AI-assisted
  workout tracker; this dataset is its exercise data layer. Building your own fitness
  app? Drop it straight into your backend. 📦 Data Source This repository provides:
  1,324 exercises with category, body-part, equipment, target and muscle-group data
  an animation GIF + 180×180 thumbnail for every exercise (media © Gym visual — see
  License) step-by-step instructions in 9 languages (🇬🇧 English, 🇪🇸 Spanish, 🇮🇹 Italian,
  🇹🇷 Turkish, 🇷🇺 Russian, 🇨🇳 Chinese, 🇮🇳 Hindi, 🇵🇱 Polish, 🇰🇷 Korean) the interactive
  browser (index.html) and developer setup guide (setup.html) 📋 Table of Contents
  Data Source Overview Interactive Browser & Developer Setup File Structure Statistics
  Data Schema Sample Exercises Usage Examples License & Use 🔍 Overview This dataset
  is a curated collection of 1,324 fitness exercises for educational and research
  purposes. It covers a wide range of muscle groups, equipment types, and exercise
  categories — making it ideal for: Building fitness or workout planning applications
  Machine learning projects involving exercise recognition or recommendation Health
  and wellness research Educational demonstrations and prototypes Each exercise entry
  contains: Field Description Unique ID Numeric identifier (e.g. "0001") Name Full
  descriptive exercise name Category Primary muscle group targeted Target Specific
  target muscle Muscle Group Supporting / synergist muscles Equipment Equipment required
  (or body weight for bodyweight) Instructions Step-by-step instructions for each
  exercise Available Languages 🇬🇧 English · 🇪🇸 Spanish · 🇮🇹 Italian · 🇹🇷 Turkish ·
  🇷🇺 Russian · 🇨🇳 Chinese · 🇮🇳 Hindi · 🇵🇱 Polish · 🇰🇷 Korean Media 180×180 thumbnail
  (image) + animation GIF (gif_url) per exercise — media © Gym visual, see License
  🖥️ Interactive Browser & Developer Setup This repository includes two ready-to-use
  HTML tools — no server required, just open in a browser. Note: the browser displays
  each exercise''s 180×180 thumbnail and animation GIF alongside its metadata and
  instructions. index.html — Exercise Browser A fully client-side exercise explorer
  with: Live search across all 1,324 exercises Filter by category, equipment, and
  target muscle Infinite scroll grid Click any card to see full details and instructions
  in English, Spanish, Italian, Turkish, Russian, Chinese, Hindi, Polish, or Korean
  setup.html — Developer Setup Guide A step-by-step guide for integrating the dataset
  into your own application: Database Setup — CREATE TABLE SQL for SQL Server, PostgreSQL,
  MySQL, and SQLite. Generate a ready-to-run .sql file with all 1,324 INSERT statements,
  built entirely in your browser. API Integration — Copy-paste client code in JavaScript,
  Python, C#, Java, PHP, Go, and cURL showing how to call your backend API. Enter
  your base URL and all examples update live. Ask Your LLM — A structured prompt (choose
  your framework + database) that you can paste into ChatGPT, Claude, or Gemini to
  generate a complete, production-ready REST API in one shot. Supports Express.js,
  FastAPI, ASP.NET Core, Spring Boot, Laravel, and Gin. 📂 File Structure exercises-dataset/
  ├── data/ │ ├── exercises.json # Full dataset — 1,324 exercise records (JSON array)
  │ └── exercises.schema.json # JSON Schema (2020-12) describing every record ├──
  images/ # 1,324 × 180×180 thumbnails (© Gym visual) ├── videos/ # 1,324 × 180×180
  animation GIFs (© Gym visual) ├── index.html # Interactive exercise browser (client-side,
  no server needed) ├── setup.html # Developer setup guide (DB import + API integration)
  ├── NOTICE.md # Media attribution & license terms └── README.md Key Files data/exercises.json
  — The primary data file. A JSON array of 1,324 exercise objects with all metadata.
  image / gif_url point to the local 180×180 assets, and each record carries an attribution
  field; media_id holds the original media reference id. data/exercises.schema.json
  — A JSON Schema (Draft 2020-12) that formally describes every field, its type and
  constraints. Use it to validate the dataset or your own additions with any standard
  JSON Schema validator. images/, videos/ — 180×180 thumbnails and animation GIFs
  (© Gym visual, used with permission). index.html — Standalone exercise browser.
  Open directly in any modern browser. setup.html — Developer guide for DB setup,
  API integration, and LLM-assisted backend generation. LICENSE, NOTICE.md — MIT (code/data)
  + the Gym visual media terms. 📊 Statistics Metric Count Total Exercises 1,324 Instruction
  Languages 9 Exercises by Body Part Body Part Exercise Count Upper Arms 292 Upper
  Legs 227 Back 203 Waist 169 Chest 163 Shoulders 143 Lower Legs 59 Lower Arms 37
  Cardio 29 Neck 2 Exercises by Equipment Equipment Exercise Count Body Weight 325
  Dumbbell 294 Cable 157 Barbell 154 Leverage Machine 81 Band 54 Smith Machine 48
  Kettlebell 41 Weighted 36 Stability Ball 28 EZ Barbell 23 Other 83 Note: ~25% of
  exercises require no equipment at all — great for at-home workout applications.
  🗂️ Data Schema Each record in data/exercises.json follows this structure. A machine-readable
  JSON Schema is also provided for validation. Field Type Description id string Unique
  numeric identifier (e.g. "0001") name string Full exercise name (e.g. "3/4 Sit-up")
  category string Body part category (e.g. "upper arms", "chest", "back") body_part
  string Same as category — body part targeted equipment string Required equipment
  (e.g. "dumbbell", "body weight") instructions.en string Full step-by-step instructions
  in English instructions.es string Full step-by-step instructions in Spanish instructions.it
  string Full step-by-step instructions in Italian instructions.tr string Full step-by-step
  instructions in Turkish instructions.ru string Full step-by-step instructions in
  Russian instructions.zh string Full step-by-step instructions in Chinese instructions.hi
  string Full step-by-step instructions in Hindi instructions.pl string Full step-by-step
  instructions in Polish instructions.ko string Full step-by-step instructions in
  Korean instruction_steps.<lang> array[string] Same instructions split into an ordered
  array of steps, per language (en, es, it, tr, ru, zh, hi, pl, ko) muscle_group string
  Primary synergist muscle group secondary_muscles array[string] Additional muscles
  involved target string Primary target muscle (e.g. "biceps", "pectoralis major")
  media_id string Original media reference id (e.g. "2gPfomN") image string Path to
  the 180×180 thumbnail (e.g. "images/0001-2gPfomN.jpg") gif_url string Path to the
  180×180 animation GIF (e.g. "videos/0001-2gPfomN.gif") attribution string Media
  copyright notice — "© Gym visual — https://gymvisual.com/" created_at string ISO
  8601 timestamp of record creation Sample Record { "id": "0001", "name": "3/4 sit-up",
  "category": "waist", "body_part": "waist", "equipment": "body weight", "instructions":
  { "en": "Lie flat on your back with your knees bent and feet flat on the ground.
  Place your hands behind your head with your elbows pointing outwards. Engaging your
  abs, slowly lift your upper body off the ground, curling forward until your torso
  is at a 45-degree angle. Pause for a moment at the top, then slowly lower your upper
  body back down to the starting position. Repeat for the desired number of repetitions.",
  "es": "Túmbate sobre tu espalda con las rodillas flexionadas y los pies apoyados
  en el suelo. ...", "it": "Sdraiati sulla schiena con le ginocchia piegate e i piedi
  appoggiati a terra. ...", "tr": "Sırt üstü yatın, dizlerinizi bükün ve ayaklarınızı
  yere düz koyun. ...", "ru": "Лягте на спину, согните колени и поставьте ступни на
  землю. ...", "zh": "平躺，膝盖弯曲，双脚平放在地上。...", "hi": "अपने घुटनों को मोड़कर और पैरों
  को ज़मीन पर सपाट रखते हुए अपनी पीठ के बल लेट जाएँ।...", "pl": "Połóż się płasko
  na plecach, ugnij kolana i oprzyj stopy płasko na pod ...", "ko": "등을 바닥에 누워 무릎을
  구부리고 발을 바닥에 붙입니다. ..." }, "muscle_group": "hip flexors", "secondary_muscles": ["hip
  flexors", "lower back"], "target": "abs", "media_id": "2gPfomN", "image": "images/0001-2gPfomN.jpg",
  "gif_url": "videos/0001-2gPfomN.gif", "attribution": "© Gym visual — https://gymvisual.com/",
  "created_at": "2026-03-18T12:31:32.854798+00:00" } 🎬 Sample Exercises Each example
  ships a 180×180 thumbnail (image) and animation GIF (gif_url), © Gym visual. 1 —
  Barbell Bench Press · Chest Equipment: Barbell · Target: Pectorals · Secondary:
  Triceps, Shoulders · Media ID: EIeI8Vf The Barbell Bench Press is the cornerstone
  of chest training and one of the "Big Three" powerlifting movements. Lying flat
  on a bench, you lower a loaded barbell to your chest and press it back up explosively.
  It simultaneously recruits the pectorals, triceps, and anterior deltoids, making
  it the single most effective exercise for upper body pushing strength and chest
  mass development. Key cues: Retract and depress your scapulae before unracking.
  Keep your feet flat on the floor, arch your lower back naturally, and maintain a
  shoulder-width grip. Lower the bar under control to mid-chest and drive up through
  the heels. 2 — Barbell Deadlift · Upper Legs / Back Equipment: Barbell · Target:
  Glutes · Secondary: Hamstrings, Lower Back · Media ID: ila4NZS The Barbell Deadlift
  is widely regarded as the ultimate full-body strength exercise. It engages virtually
  every major muscle in the posterior chain — glutes, hamstrings, and lower back —
  while also demanding significant contribution from the upper back, traps, and grip.
  Proper spinal alignment and bracing technique are critical for both performance
  and safety. Key cues: Set up with the bar over your mid-foot. Hinge at the hips,
  grip just outside your legs, brace your core hard, and keep the bar in contact with
  your shins throughout the lift. Drive the floor away, lock out at the top by squeezing
  glutes and extending hips fully. 3 — Barbell Full Squat · Upper Legs Equipment:
  Barbell · Target: Glutes · Secondary: Quadriceps, Hamstrings, Calves, Core · Media
  ID: qXTaZnJ Often called "the king of all exercises," the Barbell Full Squat demands
  coordinated strength across the entire lower body and core. Breaking parallel maximizes
  glute and hamstring activation compared to partial squats. It is the foundation
  of nearly every strength and hypertrophy program. Key cues: Bar on upper traps (high
  bar) or rear deltoids (low bar). Brace your core before descent, push knees out
  in line with toes, sit into your hips, and descend until your thighs pass parallel
  to the floor. Drive through the whole foot to stand. 4 — Dumbbell Biceps Curl ·
  Upper Arms Equipment: Dumbbell · Target: Biceps · Secondary: Forearms · Media ID:
  NbVPDMW The Dumbbell Biceps Curl is the most recognized isolation exercise for the
  arms. Training each side independently helps identify and correct strength imbalances
  between limbs. The supinated (palms-up) grip maximizes biceps contraction at the
  top of the movement. Key cues: Stand tall with elbows pinned to your sides. Supinate
  your wrists as you curl up, squeeze at the top, and lower under control without
  swinging. Avoid using momentum from the shoulders or lower back. 5 — Pull-up · Back
  Equipment: Body Weight · Target: Lats · Secondary: Biceps, Forearms · Media ID:
  lBDjFxJ The Pull-up is the gold standard bodyweight exercise for upper body pulling
  strength. It primarily develops the latissimus dorsi — creating the coveted V-taper
  — while heavily involving the biceps, rear deltoids, and core stabilizers. It scales
  from beginner (band-assisted) to advanced (weighted). Key cues: Dead hang from an
  overhand grip, shoulder-width or slightly wider. Initiate with your lats by depressing
  your shoulder blades, then pull your chest toward the bar. Lower fully between reps
  to maintain range of motion. 6 — Dumbbell Lateral Raise · Shoulders Equipment: Dumbbell
  · Target: Delts · Secondary: Traps · Media ID: DsgkuIt The Dumbbell Lateral Raise
  is the go-to isolation exercise for building shoulder width. It directly targets
  the lateral (middle) head of the deltoid, which is responsible for the broad-shouldered
  look. Controlled tempo and strict form matter far more than load. Key cues: Stand
  with a slight bend in your elbows throughout. Raise the dumbbells out to the sides
  until your arms are parallel to the floor — no higher. Lead with your elbows, not
  your wrists. Lower slowly under control to maximize time under tension. 🚀 Usage
  Examples Python — Load and Filter import json with open("data/exercises.json", "r",
  encoding="utf-8") as f: exercises = json.load(f) print(f"Total exercises loaded:
  {len(exercises)}") # Filter by category chest_exercises = [ex for ex in exercises
  if ex["category"] == "chest"] print(f"Chest exercises: {len(chest_exercises)}")
  # -> Chest exercises: 163 # Filter by equipment bodyweight = [ex for ex in exercises
  if ex["equipment"] == "body weight"] print(f"Bodyweight exercises: {len(bodyweight)}")
  # -> Bodyweight exercises: 325 # Get all unique categories categories = sorted({ex["category"]
  for ex in exercises}) print("Categories:", categories) # Access multilingual instructions
  ex = exercises[0] print(ex["instructions"]["en"]) # English print(ex["instructions"]["es"])
  # Spanish print(ex["instructions"]["it"]) # Italian print(ex["instructions"]["tr"])
  # Turkish print(ex["instructions"]["ru"]) # Russian print(ex["instructions"]["zh"])
  # Chinese print(ex["instructions"]["hi"]) # Hindi Python — Load with Pandas import
  json import pandas as pd with open("data/exercises.json", "r", encoding="utf-8")
  as f: data = json.load(f) df = pd.DataFrame(data) # Top categories by exercise count
  print(df["category"].value_counts().head(10)) # All barbell exercises targeting
  upper legs barbell_quads = df[(df["equipment"] == "barbell") & (df["category"] ==
  "upper legs")] print(barbell_quads[["name", "target", "equipment"]]) JavaScript
  / Node.js const exercises = require("./data/exercises.json"); console.log(`Total
  exercises: ${exercises.length}`); // Bodyweight exercises only const bodyweight
  = exercises.filter(ex => ex.equipment === "body weight"); console.log(`Bodyweight
  exercises: ${bodyweight.length}`); // -> Bodyweight exercises: 325 // Group exercises
  by category const byCategory = exercises.reduce((acc, ex) => { acc[ex.category]
  = (acc[ex.category] || []); acc[ex.category].push(ex); return acc; }, {}); // Access
  multilingual instructions const ex = exercises[0]; console.log(ex.instructions.en);
  // English console.log(ex.instructions.es); // Spanish console.log(ex.instructions.it);
  // Italian console.log(ex.instructions.tr); // Turkish console.log(ex.instructions.ru);
  // Russian console.log(ex.instructions.zh); // Chinese console.log(ex.instructions.hi);
  // Hindi console.log(ex.instructions.pl); // Polish console.log(ex.instructions.ko);
  // Korean TypeScript — Type-safe Usage interface Exercise { id: string; name: string;
  category: string; body_part: string; equipment: string; instructions: { en: string;
  es: string; it: string; tr: string; ru: string; zh: string; hi: string; pl: string;
  ko: string; }; muscle_group: string; secondary_muscles: string[]; target: string;
  media_id: string | null; image: string | null; gif_url: string | null; attribution:
  string; created_at: string; } import exercises from "./data/exercises.json"; const
  data = exercises as Exercise[]; const randomWorkout: Exercise[] = data.slice(0,
  6); console.log("First 6 exercises:", randomWorkout.map(e => e.name)); 📄 License
  & Use This repository is a developer setup wizard and structured exercise dataset
  — exercise metadata, multilingual instruction translations, and 180×180 exercise
  media. Code, tooling, dataset structure, and instruction text are released under
  the MIT License. Exercise media (images & GIFs) is © Gym visual and redistributed
  here with permission, at 180×180 resolution — see NOTICE.md and the media exception
  in LICENSE. Keep the © Gym visual — https://gymvisual.com/ attribution intact. Reuse
  is governed by Gym visual''s Terms & Conditions; obtain your own license there before
  reusing the media. This repository does not claim ownership of the underlying exercise
  content or media.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: afba96f60b5ba9cc
manifest_dates:
- '2026-07-01'
- '2026-07-02'
- '2026-07-03'
- '2026-07-14'
- '2026-07-15'
source_type: community_discussion
tldr: hasaneyldrm 在 GitHub 上发布了包含 1,324 个健身动作的完整数据集，含动画 GIF 和 9 种语言说明。
objective_summary: 开发者 hasaneyldrm 在 GitHub 发布了 exercises-dataset 项目，包含 1,324 个健身动作的结构化数据，每个动作配有
  180×180 缩略图与动画 GIF，以及 9 种语言（英、西、意、土、俄、中、印地、波、韩）的分步说明。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - Gym visual
  technologies: []
  key_people:
  - hasaneyldrm
key_logic_flow:
- hasaneyldrm 在 GitHub 上发布了 exercises-dataset 项目，提供 1,324 个健身动作的结构化数据集。
- 每个动作包含分类、身体部位、所需器材、目标肌群、次要肌群等元数据字段。
- 所有动作均配有 180×180 缩略图（images/）和动画 GIF（videos/），媒体版权归 Gym visual。
- 分步说明支持 9 种语言（含中文），以字符串和数组两种格式提供。
- 项目附带客户端交互浏览器（index.html）和开发者集成指南（setup.html），支持多种数据库 SQL 脚本和编程语言的 API 示例。
- 数据以 JSON 格式提供，附带 JSON Schema（2020-12 Draft）用于验证，代码与数据采用 MIT 协议。
specialized_tags:
  github:
    projectName: hasaneyldrm/exercises-dataset
    projectUrl: https://github.com/hasaneyldrm/exercises-dataset
    primaryLanguage: JavaScript
    licenseType: MIT
    domain: data_engineering
    crossTags:
    - dataset
    - fitness
    - multi-language
    aiDetail: null
extract_result: success
impact_score:
  score: 3.0
  reason: 该事件是一个健身动作数据集的发布，虽然数据集结构完整（1,324个动作、9种语言、JSON Schema验证），但其核心价值是面向健身应用开发者的数据资源，而非AI技术创新。对AI行业的竞争格局没有直接影响，属于细分领域的基础设施建设。唯一与AI行业的交叉点在于可作为运动识别/推荐等ML项目的训练数据，但项目本身未提供任何模型或算法创新。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 可直接用于健身应用后端的结构化数据集，含多语言说明和动画GIF
hype_assessment:
  level: low
  reason: 项目README描述客观平实，以结构化表格列出字段和数据统计，没有使用'颠覆'、'革命性'等PR滥用词汇。带有交互式浏览器和开发者集成指南，属于实用型工具发布而非概念炒作。媒体版权声明清晰（©
    Gym visual），数据协议明确（MIT），无过度承诺。
information_entropy: medium
domain_disruption:
  technical_innovation: 无——这是一个结构化数据集的发布，而非技术创新。数据以标准JSON格式组织，附带JSON Schema（2020-12
    Draft）用于验证，属于成熟工程实践。
  business_model: 对健身/健康类SaaS应用的开发成本有边际影响——开发者可以直接复用该数据集作为运动库的后端数据层，节省数据采集和整理的成本，但不足以重塑商业模式。
engineering_complexity: production_ready
compound_value:
  score: 4.0
  reason: 这是一个高质量的结构化健身动作数据集，1,324 条记录覆盖全身肌群，附带动画 GIF、9 语言说明、JSON Schema 和数据库脚本，MIT
    协议开源。其价值在于作为 Fitness 领域的标准化参照数据集，可嵌入任何健身应用后端，节省大量数据采集和整理成本。但静态数据缺乏网络效应和持续迭代机制，媒体版权归
    Gym visual 而非项目方，且 MIT 协议限制了直接变现能力。长期看，它可能成为类似 ImageNet 的行业基准数据集，但架构上不具备平台级复利效应——这是一份优质的开源数据资产，而非可规模化捕获价值的商业模式。评分
    4.0，属于细分赛道的高质量基础设施但缺复合增长引擎。
value_capture_layer: end_application
moat_impact: democratizes_access
key_beneficiaries:
- LogPress
- 独立健身应用开发者
- ML 健身动作识别研究者
- Gym visual
competitive_casualty:
- 商业健身数据集销售商
- 自建动作数据标注管线的健身初创公司
- Keep 等需要视觉数据的健身平台
market_opportunities:
- 健身类App和Web应用开发者可直接集成该1,324个动作的结构化数据集，快速构建训练动作库功能，大幅降低内容采集成本
- 基于该数据集的多语言分步说明和元数据字段，可开发AI驱动的个性化训练计划推荐系统或动作识别模型
- 创业团队可围绕该开源数据集构建垂直健身SaaS产品，如AI健身教练、企业健康管理平台等
risk_matrix:
  regulatory: 媒体文件（动画GIF和缩略图）版权归Gym visual所有，遵循单独的NOTICE.md许可条款而非MIT协议，若未正确署名可能面临版权纠纷
  technological: 无——数据集以标准化JSON格式提供，附带JSON Schema验证，技术风险较低
  competitive: 健身数据集开源社区门槛较低，后续可能出现规模更大（例如10,000+动作）或覆盖更广（如瑜伽、普拉提）的竞品数据集，侵蚀该项目的差异化价值
  ethical: 数据集本身风险较低，但若用于AI教练类产品需注意动作安全性建议的准确性，避免因错误或不当的动作指导导致用户受伤
  additional:
  - 数据集依赖的Gym visual媒体资产可能因版权方商业策略变更而撤回授权或限制使用
  - 数据集仅包含静态说明和GIF动画，缺乏3D姿态数据或视频动作捕捉数据，在高级AI训练场景中存在数据形态局限
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: monitor
---

**A comprehensive, ready-to-use fitness exercise dataset with 1,324 exercises — each with an animation GIF, 180×180 thumbnail image, category, body-part, equipment, target and muscle-group data, and step-by-step instructions in 9 languages (English, Spanish, Italian, Turkish, Russian, Chinese, Hindi, Polish, Korean).**


📱 Powers the LogPress app— an AI-assisted workout tracker; this dataset is its exercise data layer. Building your own fitness app? Drop it straight into your backend.

**This repository provides:**

- 1,324 exercises with category, body-part, equipment, target and muscle-group data
- an animation GIF + 180×180 thumbnail for every exercise (media © Gym visual — see License)
- step-by-step instructions in 9 languages (🇬🇧 English, 🇪🇸 Spanish, 🇮🇹 Italian, 🇹🇷 Turkish, 🇷🇺 Russian, 🇨🇳 Chinese, 🇮🇳 Hindi, 🇵🇱 Polish, 🇰🇷 Korean)
- the interactive browser (
`index.html`

) and developer setup guide (`setup.html`

)

- Data Source
- Overview
- Interactive Browser & Developer Setup
- File Structure
- Statistics
- Data Schema
- Sample Exercises
- Usage Examples
- License & Use

This dataset is a curated collection of **1,324 fitness exercises** for educational and research purposes. It covers a wide range of muscle groups, equipment types, and exercise categories — making it ideal for:

- Building fitness or workout planning applications
- Machine learning projects involving exercise recognition or recommendation
- Health and wellness research
- Educational demonstrations and prototypes

Each exercise entry contains:

| Field | Description |
|---|---|
| Unique ID | Numeric identifier (e.g. `"0001"` ) |
| Name | Full descriptive exercise name |
| Category | Primary muscle group targeted |
| Target | Specific target muscle |
| Muscle Group | Supporting / synergist muscles |
| Equipment | Equipment required (or `body weight` for bodyweight) |
| Instructions | Step-by-step instructions for each exercise |
| Available Languages | 🇬🇧 English · 🇪🇸 Spanish · 🇮🇹 Italian · 🇹🇷 Turkish · 🇷🇺 Russian · 🇨🇳 Chinese · 🇮🇳 Hindi · 🇵🇱 Polish · 🇰🇷 Korean |
| Media | 180×180 thumbnail (`image` ) + animation GIF (`gif_url` ) per exercise — media © Gym visual, see License |

This repository includes two ready-to-use HTML tools — no server required, just open in a browser.


Note:the browser displays each exercise's 180×180 thumbnail and animation GIF alongside its metadata and instructions.

A fully client-side exercise explorer with:

- Live search across all 1,324 exercises
- Filter by category, equipment, and target muscle
- Infinite scroll grid
- Click any card to see full details and instructions in English, Spanish, Italian, Turkish, Russian, Chinese, Hindi, Polish, or Korean

A step-by-step guide for integrating the dataset into your own application:

**Database Setup**—`CREATE TABLE`

SQL for SQL Server, PostgreSQL, MySQL, and SQLite. Generate a ready-to-run`.sql`

file with all 1,324 INSERT statements, built entirely in your browser.**API Integration**— Copy-paste client code in**JavaScript, Python, C#, Java, PHP, Go, and cURL**showing how to call your backend API. Enter your base URL and all examples update live.**Ask Your LLM**— A structured prompt (choose your framework + database) that you can paste into ChatGPT, Claude, or Gemini to generate a complete, production-ready REST API in one shot. Supports Express.js, FastAPI, ASP.NET Core, Spring Boot, Laravel, and Gin.

```
exercises-dataset/
├── data/
│ ├── exercises.json # Full dataset — 1,324 exercise records (JSON array)
│ └── exercises.schema.json # JSON Schema (2020-12) describing every record
├── images/ # 1,324 × 180×180 thumbnails (© Gym visual)
├── videos/ # 1,324 × 180×180 animation GIFs (© Gym visual)
├── index.html # Interactive exercise browser (client-side, no server needed)
├── setup.html # Developer setup guide (DB import + API integration)
├── NOTICE.md # Media attribution & license terms
└── README.md
```


— The primary data file. A JSON array of 1,324 exercise objects with all metadata.`data/exercises.json`

`image`

/`gif_url`

point to the local 180×180 assets, and each record carries an`attribution`

field;`media_id`

holds the original media reference id.— A JSON Schema (Draft 2020-12) that formally describes every field, its type and constraints. Use it to validate the dataset or your own additions with any standard JSON Schema validator.`data/exercises.schema.json`

— 180×180 thumbnails and animation GIFs (© Gym visual, used with permission).`images/`

,`videos/`

— Standalone exercise browser. Open directly in any modern browser.`index.html`

— Developer guide for DB setup, API integration, and LLM-assisted backend generation.`setup.html`

— MIT (code/data) + the Gym visual media terms.`LICENSE`

,`NOTICE.md`


| Metric | Count |
|---|---|
| Total Exercises | 1,324 |
| Instruction Languages | 9 |

| Body Part | Exercise Count |
|---|---|
| Upper Arms | 292 |
| Upper Legs | 227 |
| Back | 203 |
| Waist | 169 |
| Chest | 163 |
| Shoulders | 143 |
| Lower Legs | 59 |
| Lower Arms | 37 |
| Cardio | 29 |
| Neck | 2 |

| Equipment | Exercise Count |
|---|---|
| Body Weight | 325 |
| Dumbbell | 294 |
| Cable | 157 |
| Barbell | 154 |
| Leverage Machine | 81 |
| Band | 54 |
| Smith Machine | 48 |
| Kettlebell | 41 |
| Weighted | 36 |
| Stability Ball | 28 |
| EZ Barbell | 23 |
| Other | 83 |


Note:~25% of exercises require no equipment at all — great for at-home workout applications.

Each record in `data/exercises.json`

follows this structure. A machine-readable JSON Schema is also provided for validation.

| Field | Type | Description |
|---|---|---|
`id` |
`string` |
Unique numeric identifier (e.g. `"0001"` ) |
`name` |
`string` |
Full exercise name (e.g. `"3/4 Sit-up"` ) |
`category` |
`string` |
Body part category (e.g. `"upper arms"` , `"chest"` , `"back"` ) |
`body_part` |
`string` |
Same as `category` — body part targeted |
`equipment` |
`string` |
Required equipment (e.g. `"dumbbell"` , `"body weight"` ) |
`instructions.en` |
`string` |
Full step-by-step instructions in English |
`instructions.es` |
`string` |
Full step-by-step instructions in Spanish |
`instructions.it` |
`string` |
Full step-by-step instructions in Italian |
`instructions.tr` |
`string` |
Full step-by-step instructions in Turkish |
`instructions.ru` |
`string` |
Full step-by-step instructions in Russian |
`instructions.zh` |
`string` |
Full step-by-step instructions in Chinese |
`instructions.hi` |
`string` |
Full step-by-step instructions in Hindi |
`instructions.pl` |
`string` |
Full step-by-step instructions in Polish |
`instructions.ko` |
`string` |
Full step-by-step instructions in Korean |
`instruction_steps.<lang>` |
`array[string]` |
Same instructions split into an ordered array of steps, per language (`en` , `es` , `it` , `tr` , `ru` , `zh` , `hi` , `pl` , `ko` ) |
`muscle_group` |
`string` |
Primary synergist muscle group |
`secondary_muscles` |
`array[string]` |
Additional muscles involved |
`target` |
`string` |
Primary target muscle (e.g. `"biceps"` , `"pectoralis major"` ) |
`media_id` |
`string` |
Original media reference id (e.g. `"2gPfomN"` ) |
`image` |
`string` |
Path to the 180×180 thumbnail (e.g. `"images/0001-2gPfomN.jpg"` ) |
`gif_url` |
`string` |
Path to the 180×180 animation GIF (e.g. `"videos/0001-2gPfomN.gif"` ) |
`attribution` |
`string` |
Media copyright notice — `"© Gym visual — https://gymvisual.com/"` |
`created_at` |
`string` |
ISO 8601 timestamp of record creation |

```
{
"id": "0001",
"name": "3/4 sit-up",
"category": "waist",
"body_part": "waist",
"equipment": "body weight",
"instructions": {
"en": "Lie flat on your back with your knees bent and feet flat on the ground. Place your hands behind your head with your elbows pointing outwards. Engaging your abs, slowly lift your upper body off the ground, curling forward until your torso is at a 45-degree angle. Pause for a moment at the top, then slowly lower your upper body back down to the starting position. Repeat for the desired number of repetitions.",
"es": "Túmbate sobre tu espalda con las rodillas flexionadas y los pies apoyados en el suelo. ...",
"it": "Sdraiati sulla schiena con le ginocchia piegate e i piedi appoggiati a terra. ...",
"tr": "Sırt üstü yatın, dizlerinizi bükün ve ayaklarınızı yere düz koyun. ...",
"ru": "Лягте на спину, согните колени и поставьте ступни на землю. ...",
"zh": "平躺，膝盖弯曲，双脚平放在地上。...",
"hi": "अपने घुटनों को मोड़कर और पैरों को ज़मीन पर सपाट रखते हुए अपनी पीठ के बल लेट जाएँ।...",
"pl": "Połóż się płasko na plecach, ugnij kolana i oprzyj stopy płasko na pod ...",
"ko": "등을 바닥에 누워 무릎을 구부리고 발을 바닥에 붙입니다. ..."
},
"muscle_group": "hip flexors",
"secondary_muscles": ["hip flexors", "lower back"],
"target": "abs",
"media_id": "2gPfomN",
"image": "images/0001-2gPfomN.jpg",
"gif_url": "videos/0001-2gPfomN.gif",
"attribution": "© Gym visual — https://gymvisual.com/",
"created_at": "2026-03-18T12:31:32.854798+00:00"
}
```

Each example ships a 180×180 thumbnail (

`image`

) and animation GIF (`gif_url`

), © Gym visual.


Equipment:Barbell ·Target:Pectorals ·Secondary:Triceps, Shoulders ·Media ID:`EIeI8Vf`


The Barbell Bench Press is the cornerstone of chest training and one of the "Big Three" powerlifting movements. Lying flat on a bench, you lower a loaded barbell to your chest and press it back up explosively. It simultaneously recruits the pectorals, triceps, and anterior deltoids, making it the single most effective exercise for upper body pushing strength and chest mass development.

**Key cues:** Retract and depress your scapulae before unracking. Keep your feet flat on the floor, arch your lower back naturally, and maintain a shoulder-width grip. Lower the bar under control to mid-chest and drive up through the heels.


Equipment:Barbell ·Target:Glutes ·Secondary:Hamstrings, Lower Back ·Media ID:`ila4NZS`


The Barbell Deadlift is widely regarded as the ultimate full-body strength exercise. It engages virtually every major muscle in the posterior chain — glutes, hamstrings, and lower back — while also demanding significant contribution from the upper back, traps, and grip. Proper spinal alignment and bracing technique are critical for both performance and safety.

**Key cues:** Set up with the bar over your mid-foot. Hinge at the hips, grip just outside your legs, brace your core hard, and keep the bar in contact with your shins throughout the lift. Drive the floor away, lock out at the top by squeezing glutes and extending hips fully.


Equipment:Barbell ·Target:Glutes ·Secondary:Quadriceps, Hamstrings, Calves, Core ·Media ID:`qXTaZnJ`


Often called "the king of all exercises," the Barbell Full Squat demands coordinated strength across the entire lower body and core. Breaking parallel maximizes glute and hamstring activation compared to partial squats. It is the foundation of nearly every strength and hypertrophy program.

**Key cues:** Bar on upper traps (high bar) or rear deltoids (low bar). Brace your core before descent, push knees out in line with toes, sit into your hips, and descend until your thighs pass parallel to the floor. Drive through the whole foot to stand.


Equipment:Dumbbell ·Target:Biceps ·Secondary:Forearms ·Media ID:`NbVPDMW`


The Dumbbell Biceps Curl is the most recognized isolation exercise for the arms. Training each side independently helps identify and correct strength imbalances between limbs. The supinated (palms-up) grip maximizes biceps contraction at the top of the movement.

**Key cues:** Stand tall with elbows pinned to your sides. Supinate your wrists as you curl up, squeeze at the top, and lower under control without swinging. Avoid using momentum from the shoulders or lower back.


Equipment:Body Weight ·Target:Lats ·Secondary:Biceps, Forearms ·Media ID:`lBDjFxJ`


The Pull-up is the gold standard bodyweight exercise for upper body pulling strength. It primarily develops the latissimus dorsi — creating the coveted V-taper — while heavily involving the biceps, rear deltoids, and core stabilizers. It scales from beginner (band-assisted) to advanced (weighted).

**Key cues:** Dead hang from an overhand grip, shoulder-width or slightly wider. Initiate with your lats by depressing your shoulder blades, then pull your chest toward the bar. Lower fully between reps to maintain range of motion.


Equipment:Dumbbell ·Target:Delts ·Secondary:Traps ·Media ID:`DsgkuIt`


The Dumbbell Lateral Raise is the go-to isolation exercise for building shoulder width. It directly targets the lateral (middle) head of the deltoid, which is responsible for the broad-shouldered look. Controlled tempo and strict form matter far more than load.

**Key cues:** Stand with a slight bend in your elbows throughout. Raise the dumbbells out to the sides until your arms are parallel to the floor — no higher. Lead with your elbows, not your wrists. Lower slowly under control to maximize time under tension.

```
import json
with open("data/exercises.json", "r", encoding="utf-8") as f:
exercises = json.load(f)
print(f"Total exercises loaded: {len(exercises)}")
# Filter by category
chest_exercises = [ex for ex in exercises if ex["category"] == "chest"]
print(f"Chest exercises: {len(chest_exercises)}")
# -> Chest exercises: 163
# Filter by equipment
bodyweight = [ex for ex in exercises if ex["equipment"] == "body weight"]
print(f"Bodyweight exercises: {len(bodyweight)}")
# -> Bodyweight exercises: 325
# Get all unique categories
categories = sorted({ex["category"] for ex in exercises})
print("Categories:", categories)
# Access multilingual instructions
ex = exercises[0]
print(ex["instructions"]["en"]) # English
print(ex["instructions"]["es"]) # Spanish
print(ex["instructions"]["it"]) # Italian
print(ex["instructions"]["tr"]) # Turkish
print(ex["instructions"]["ru"]) # Russian
print(ex["instructions"]["zh"]) # Chinese
print(ex["instructions"]["hi"]) # Hindi
```

```
import json
import pandas as pd
with open("data/exercises.json", "r", encoding="utf-8") as f:
data = json.load(f)
df = pd.DataFrame(data)
# Top categories by exercise count
print(df["category"].value_counts().head(10))
# All barbell exercises targeting upper legs
barbell_quads = df[(df["equipment"] == "barbell") & (df["category"] == "upper legs")]
print(barbell_quads[["name", "target", "equipment"]])
```

```
const exercises = require("./data/exercises.json");
console.log(`Total exercises: ${exercises.length}`);
// Bodyweight exercises only
const bodyweight = exercises.filter(ex => ex.equipment === "body weight");
console.log(`Bodyweight exercises: ${bodyweight.length}`);
// -> Bodyweight exercises: 325
// Group exercises by category
const byCategory = exercises.reduce((acc, ex) => {
acc[ex.category] = (acc[ex.category] || []);
acc[ex.category].push(ex);
return acc;
}, {});
// Access multilingual instructions
const ex = exercises[0];
console.log(ex.instructions.en); // English
console.log(ex.instructions.es); // Spanish
console.log(ex.instructions.it); // Italian
console.log(ex.instructions.tr); // Turkish
console.log(ex.instructions.ru); // Russian
console.log(ex.instructions.zh); // Chinese
console.log(ex.instructions.hi); // Hindi
console.log(ex.instructions.pl); // Polish
console.log(ex.instructions.ko); // Korean
```

```
interface Exercise {
id: string;
name: string;
category: string;
body_part: string;
equipment: string;
instructions: {
en: string;
es: string;
it: string;
tr: string;
ru: string;
zh: string;
hi: string;
pl: string;
ko: string;
};
muscle_group: string;
secondary_muscles: string[];
target: string;
media_id: string | null;
image: string | null;
gif_url: string | null;
attribution: string;
created_at: string;
}
import exercises from "./data/exercises.json";
const data = exercises as Exercise[];
const randomWorkout: Exercise[] = data.slice(0, 6);
console.log("First 6 exercises:", randomWorkout.map(e => e.name));
```

This repository is a **developer setup wizard and structured exercise dataset** — exercise metadata, multilingual instruction translations, and 180×180 exercise media.

**Code, tooling, dataset structure, and instruction text**are released under the MIT License.**Exercise media (images & GIFs) is © Gym visual**and redistributed here**with permission**, at 180×180 resolution — see`NOTICE.md`

and the media exception in`LICENSE`

. Keep the`© Gym visual — https://gymvisual.com/`

attribution intact. Reuse is governed by Gym visual's Terms & Conditions; obtain your own license there before reusing the media.- This repository does
**not**claim ownership of the underlying exercise content or media.