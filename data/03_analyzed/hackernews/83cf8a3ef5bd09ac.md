---
title: 'Google copybara: moving code between repositories'
source: https://github.com/google/copybara
author:
- '[[reconnecting]]'
published: '2026-06-30'
created: '2026-07-01'
description: 'Article URL: https://github.com/google/copybara Comments URL: https://news.ycombinator.com/item?id=48740698
  Points: 206 # Comments: 33'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 83cf8a3ef5bd09ac
manifest_dates:
- '2026-07-01'
source_type: community_discussion
tldr: Google 开源了其内部使用的代码仓库同步工具 Copybara，该工具可在多个 Git 仓库之间转换和移动代码，采用无状态设计并将状态存储在目标仓库的提交信息标签中。
objective_summary: Google 将其内部使用的代码同步工具 Copybara 以开源形式发布在 GitHub 上。该工具用于在多个代码仓库之间转换和移动代码，支持选择一个权威仓库作为唯一事实来源，同时允许任何仓库接收外部贡献和发布版本。Copybara
  采用无状态设计，将同步状态以标签形式存储在目标仓库的提交信息中。目前该工具正式支持 Git 仓库，Mercurial 支持仍处于实验阶段，使用 Java 开发并通过
  Bazel 构建系统编译。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Google
  technologies: []
  key_people: []
key_logic_flow:
- Copybara 是 Google 内部开发并开源的代码仓库同步工具，用于在多个仓库之间转换和移动代码。
- 它要求选择一个权威仓库作为唯一事实来源，但允许非权威仓库接收贡献和发布版本。
- Copybara 采用无状态设计，将同步状态以标签形式存储在目标仓库的提交信息中，支持多用户或服务共享同一配置。
- 该工具目前正式支持 Git 仓库，Mercurial 仓库处于实验阶段，可扩展架构允许添加自定义的源和目标类型。
- Copybara 使用 Java 开发并通过 Bazel 构建系统编译，提供每周快照发布版本和 Docker 实验性支持。
- 配置以 .bara.sky 文件存储，推荐使用版本控制系统管理这些配置文件。
extract_result: success
object_mentions:
- object_type: project
  name: google/copybara
  canonical_name: google/copybara
  url: https://github.com/google/copybara
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Copybara 是 Google 内部使用的工具，用于在代码仓库之间转换和移动代码。
  - 该工具要求选择一个权威仓库作为唯一事实来源，但允许任何仓库接收外部贡献和发布版本。
  - Copybara 采用无状态设计，将同步状态以标签形式存储在目标仓库的提交信息中。
  article_id: 83cf8a3ef5bd09ac
impact_score:
  score: 3.0
  reason: Copybara 是 Google 内部长期使用的跨仓库代码同步工具，其开源版本已在 GitHub 上存在多时，并非今日首发。对于需要跨内部和公开仓库管理代码的
    AI 工程团队而言是一个实用基础设施，可简化模型代码和训练管道的多仓库同步流程，但它不涉及 AI 模型架构、训练方法或推理效率的任何创新。作为 DevOps
    工具，其行业冲击力有限，属于局部效率改进而非范式转移。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: Starlark 配置学习成本和 Java 21 + Bazel 运行环境的搭建门槛
hype_assessment:
  level: low
  reason: 文章是 GitHub 仓库的纯技术 README 文档，内容以架构说明、配置示例和构建指令为主，没有任何 PR 式夸张宣传用语（如"颠覆性"、"革命性"），信息呈现客观务实。
information_entropy: medium
domain_disruption:
  technical_innovation: 无状态的跨仓库同步设计是核心亮点——将同步状态嵌入目标仓库的提交标签中，无需额外数据库或状态服务，多用户可共享同一配置获得一致结果。这种架构思路可借鉴到
    AI 工程中的模型配置版本管理和实验代码同步场景。
  business_model: 无
engineering_complexity: production_ready
compound_value:
  score: 3.5
  reason: Copybara 解决的是跨 Git 仓库代码同步与转换这一细分工程痛点，Google 背书带来长期维护可信度。但这不是一个 VC 可投的赛道：市场天花板极低（主要服务于需要管理私有/公开仓库映射的
    open-core 公司和大型合规企业），且作为 Apache 2.0 开源项目缺乏商业化变现路径，Google 也未将其包装为云服务创收。工具本身无网络效应或数据飞轮，切换成本中等（配置文件和
    Starlark 工作流绑定）。虽非昙花一现（已存活多年），但不具备 10x 回报的复利基础——长期价值在于降低特定场景的操作摩擦，而非创造新的价值捕获节点。
value_capture_layer: end_application
moat_impact: democratizes_access
key_beneficiaries:
- Google
- 采用 open-core 模式的公司
- 需要合规多仓库管理的大型企业
competitive_casualty:
- 自研代码同步脚本/内部工具
- 商业代码迁移与同步服务商
market_opportunities:
- 企业内部可基于 Copybara 构建标准化的多仓库代码同步管道，解决微服务架构下私库与公库之间的代码流转与合规审查问题
- 咨询和技术服务团队可围绕 Copybara 提供仓库迁移、CI/CD 集成和定制化适配器开发等增值服务，降低企业使用门槛
- 开源基础设施团队可基于 Copybara 的可扩展架构开发 GitLab、Bitbucket、SVN 等非 Git 仓库的适配器，拓展其生态覆盖范围
risk_matrix:
  regulatory: 无。Copybara 是开源代码同步工具，不涉及 AI 监管、出口管制或版权诉讼等合规领域
  technological: 仅正式支持 Git 仓库类型（Mercurial 仍为实验性），且依赖 Java 21+ 和 Bazel 构建系统，部署门槛较高；面临
    git subtree、git submodule 等原生工具的替代竞争
  competitive: 多仓库代码同步场景已有多种成熟方案（GitHub Actions 同步、GitLab 仓库镜像、Jenkins 插件、自建脚本等），Copybara
    需在复杂转换能力和企业级支持上建立差异化优势
  ethical: 无。该工具不涉及数据偏见、隐私侵犯、深度伪造或就业冲击等伦理议题
  additional:
  - Google 内部工具的开源版本可能存在长期维护不确定性，社区活跃度可能随 Google 内部优先级变化而波动
  - 学习曲线较陡：用户需掌握 Starlark DSL 和 Bazel 构建系统的使用，对非 Google 生态的团队构成入门障碍
confidence:
  impact: medium
  compound: medium
  hype: high
actionable_insight: monitor
object_insights:
- object_type: project
  name: google/copybara
  canonical_name: google/copybara
  url: https://github.com/google/copybara
  positioning: Google 开源的无状态代码仓库同步工具，支持在多个 Git 仓库间转换和移动代码，以标签形式将同步状态存储在目标仓库的提交信息中。
  technical_signal: 采用无状态架构设计，将同步状态以标签形式存储在目标仓库提交信息中，支持多用户或服务共享同一配置且结果一致。
  adoption_signal: 刚以开源形式发布在 GitHub 上，提供每周快照预编译二进制版本和 Docker 实验性支持，社区采用目前处于早期阶段。
  ecosystem_relevance: 填补了多仓库同步场景下开源工具的空缺，适合需要维护公共仓库与私有仓库同步的团队，其可扩展架构为自定义源和目标类型提供基础。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Google 内部多年验证的代码同步工具正式开源，其无状态设计和权威仓库模式为多仓库代码管理提供了成熟可复用的解决方案，值得关注其社区接受度和生态发展速度。
  risk_notes:
  - 目前仅正式支持 Git 仓库，Mercurial 和其他类型仓库仍处于实验阶段。
  - 每周快照版本未经自动测试和兼容性保证，生产环境使用需谨慎评估。
  score: 6.0
  article_ids:
  - 83cf8a3ef5bd09ac
  evidence_snippets:
  - Copybara 是 Google 内部使用的工具，用于在代码仓库之间转换和移动代码。
  - 该工具要求选择一个权威仓库作为唯一事实来源，但允许任何仓库接收外部贡献和发布版本。
  - Copybara 采用无状态设计，将同步状态以标签形式存储在目标仓库的提交信息中。
---

*A tool for transforming and moving code between repositories.*

Copybara is a tool used internally at Google. It transforms and moves code between repositories.

Often, source code needs to exist in multiple repositories, and Copybara allows you to transform and move source code between these repositories. A common case is a project that involves maintaining a confidential repository and a public repository in sync.

Copybara requires you to choose one of the repositories to be the authoritative repository, so that there is always one source of truth. However, the tool allows contributions to any repository, and any repository can be used to cut a release.

The most common use case involves repetitive movement of code from one repository to another. Copybara can also be used for moving code once to a new repository.

Examples uses of Copybara include:

-
Importing sections of code from a confidential repository to a public repository.

-
Importing code from a public repository to a confidential repository.

-
Importing a change from a non-authoritative repository into the authoritative repository. When a change is made in the non-authoritative repository (for example, a contributor in the public repository), Copybara transforms and moves that change into the appropriate place in the authoritative repository. Any merge conflicts are dealt with in the same way as an out-of-date change within the authoritative repository.


One of the main features of Copybara is that it is stateless, or more specifically, that it stores the state in the destination repository (As a label in the commit message). This allows several users (or a service) to use Copybara for the same config/repositories and get the same result.

Currently, the only supported type of repository is Git. Copybara is also able to read from Mercurial repositories, but the feature is still experimental. The extensible architecture allows adding bespoke origins and destinations for almost any use case. Official support for other repositories types will be added in the future.

```
core.workflow(
name = "default",
origin = git.github_origin(
url = "https://github.com/google/copybara.git",
ref = "master",
),
destination = git.destination(
url = "file:///tmp/foo",
),
# Copy everything but don't remove a README_INTERNAL.txt file if it exists.
destination_files = glob(["third_party/copybara/**"], exclude = ["README_INTERNAL.txt"]),
authoring = authoring.pass_thru("Default email <default@default.com>"),
transformations = [
core.replace(
before = "//third_party/bazel/bashunit",
after = "//another/path:bashunit",
paths = glob(["**/BUILD"])),
core.move("", "third_party/copybara")
],
)
```

Run:

```
$ (mkdir /tmp/foo ; cd /tmp/foo ; git init --bare)
$ copybara copy.bara.sky
```

The easiest way to start is with weekly "snapshot" releases, that include pre-built a binary. Note that these are released automatically without any manual testing, version compatibility or correctness guarantees.

Choose a release from https://github.com/google/copybara/releases.

To use an unreleased version of copybara, so you need to compile from HEAD. In order to do that, you need to do the following:

- Install JDK 11.
- Install Bazel.
- Clone the copybara source locally:
`git clone https://github.com/google/copybara.git`


- Build:
`bazel build //java/com/google/copybara`

`bazel build //java/com/google/copybara:copybara_deploy.jar`

to create an executable uberjar.

- Tests:
`bazel test //...`

if you want to ensure you are not using a broken version. Note that certain tests require the underlying tool to be installed(e.g. Mercurial, Quilt, etc.). It is fine to skip those tests if your Pull Request is unrelated to those modules (And our CI will run all the tests anyway).

These packages can be installed using the appropriate package manager for your system.

If you use Intellij and the Bazel plugin, use this project configuration:

```
directories:
copybara/integration
java/com/google/copybara
javatests/com/google/copybara
third_party
targets:
//copybara/integration/...
//java/com/google/copybara/...
//javatests/com/google/copybara/...
//third_party/...
```


Note: configuration files can be stored in any place, even in a local folder. We recommend using a VCS (like git) to store them; treat them as source code.

If using a weekly snapshot release, install Copybara as follows:

- Copybara ships with class files with version 65.0, so it must be run with Java Runtime 21 or greater. Add to your
`.bazelrc`

file:`run --java_runtime_version=remotejdk_21`

- Use
`http_jar`

to download the release artifact.- In WORKSPACE:
`load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_jar")`

- In MODULE.bazel:
`http_jar = use_repo_rule("@bazel_tools//tools/build_defs/repo:http.bzl", "http_jar")`


- In WORKSPACE:
- In WORKSPACE or MODULE.bazel, fill in the
`[version]`

placeholder:http_jar( name = "com_github_google_copybara", # Fill in from https://github.com/google/copybara/releases/download/[version]/copybara_deploy.jar.sha256 # sha256 = "", urls = ["https://github.com/google/copybara/releases/download/[version]/copybara_deploy.jar"], )

- In any BUILD file (perhaps
`/tools/BUILD.bazel`

) declare the`java_binary`

:load("@rules_java//java:java_binary.bzl", "java_binary") java_binary( name = "copybara", main_class = "com.google.copybara.Main", runtime_deps = ["@com_github_google_copybara//jar"], )

- Use that target with
`bazel run`

, for example`bazel run //tools:copybara -- migrate copy.bara.sky`


There are convenience macros defined for all of Copybara's dependencies. Add the
following code to your `WORKSPACE`

file, replacing `{{ sha256sum }}`

and
`{{ commit }}`

as necessary.

```
http_archive(
name = "com_github_google_copybara",
sha256 = "{{ sha256sum }}",
strip_prefix = "copybara-{{ commit }}",
url = "https://github.com/google/copybara/archive/{{ commit }}.zip",
)
load("@com_github_google_copybara//:repositories.bzl", "copybara_repositories")
copybara_repositories()
load("@com_github_google_copybara//:repositories.maven.bzl", "copybara_maven_repositories")
copybara_maven_repositories()
load("@com_github_google_copybara//:repositories.go.bzl", "copybara_go_repositories")
copybara_go_repositories()
```

You can then build and run the Copybara tool from within your workspace:

`bazel run @com_github_google_copybara//java/com/google/copybara -- <args...>`

*NOTE: Docker use is currently experimental, and we encourage feedback or contributions.*

You can build copybara using Docker like so

`docker build --rm -t copybara .`

Once this has finished building, you can run the image like so from the root of the code you are trying to use Copybara on:

`docker run -it -v "$(pwd)":/usr/src/app copybara help`

In addition to passing cmd args to the container, you can also set the following environment variables as an alternative:

`COPYBARA_SUBCOMMAND=migrate`

- allows you to change the command run, defaults to
`migrate`


- allows you to change the command run, defaults to
`COPYBARA_CONFIG=copy.bara.sky`

- allows you to specify a path to a config file, defaults to root
`copy.bara.sky`


- allows you to specify a path to a config file, defaults to root
`COPYBARA_WORKFLOW=default`

- allows you to specify the workflow to run, defaults to
`default`


- allows you to specify the workflow to run, defaults to
`COPYBARA_SOURCEREF=''`

- allows you to specify the sourceref, defaults to none

`COPYBARA_OPTIONS=''`

- allows you to specify options for copybara, defaults to none


```
docker run \
-e COPYBARA_SUBCOMMAND='validate' \
-e COPYBARA_CONFIG='other.config.sky' \
-v "$(pwd)":/usr/src/app \
-it copybara
```

There are a number of ways by which to share your git config and ssh credentials with the Docker container, an example is below:

```
docker run \
-v ~/.gitconfig:/root/.gitconfig:ro \
-v ~/.ssh:/root/.ssh \
-v ${SSH_AUTH_SOCK}:${SSH_AUTH_SOCK} -e SSH_AUTH_SOCK
-v "$(pwd)":/usr/src/app \
-it copybara
```

We are still working on the documentation. Here are some resources:

If you have any questions about how Copybara works, please contact us at our mailing list.

-
If you want to see the test errors in Bazel, instead of having to

`cat`

the logs, add this line to your`~/.bazelrc`

:`test --test_output=streamed`