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
pipeline_stage: ingested
id: afba96f60b5ba9cc
manifest_dates:
- '2026-07-01'
- '2026-07-02'
- '2026-07-03'
- '2026-07-14'
- '2026-07-15'
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