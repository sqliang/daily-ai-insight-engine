---
title: apache/maven
source: https://github.com/apache/maven
author: []
published: ''
created: '2026-07-04'
description: 'Apache Maven coreApache Maven master = 4.1.x 4.0.x: 3.10.x: 3.9.x: Apache
  Maven is a software project management and comprehension tool. Based on the concept
  of a project object model (POM), Maven can manage a project''s build, reporting
  and documentation from a central piece of information. If you think you have found
  a bug, please file an issue in the Maven Issue Tracker. Documentation More information
  can be found on Apache Maven Homepage. Questions related to the usage of Maven should
  be posted on the Maven User List. Where can I get the latest release? You can download
  the release source from our download page. Contributing If you are interested in
  the development of Maven, please consult the documentation first and afterward you
  are welcome to join the developers mailing list to ask questions or discuss new
  ideas/features/bugs etc. Take a look into the contribution guidelines. License This
  code is under the Apache License, Version 2.0, January 2004. See the NOTICE file
  for required notices and attributions. Donations Do you like Apache Maven? Then
  donate back to the ASF to support the development. Quick Build If you want to bootstrap
  Maven, you''ll need: Java 17+ Maven 3.9.0 or later Run Maven, specifying a location
  into which the completed Maven distro should be installed:mvn -DdistributionTargetDir="$HOME/app/maven/apache-maven-4.1.x-SNAPSHOT"
  clean package'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: a7aae41bfe46e3ba
manifest_dates:
- '2026-07-04'
source_type: community_discussion
tldr: Apache Maven 是一个基于项目对象模型（POM）的软件项目管理和理解工具，可从统一信息中心管理构建、报告和文档。该项目托管在 GitHub 上，使用
  Apache License 2.0 协议。
objective_summary: Apache Software Foundation 维护的开源项目 Apache Maven，是一款基于项目对象模型（POM）概念的软件项目管理和理解工具。Maven
  能够从统一的信息中心管理项目的构建、报告和文档。该项目托管在 GitHub 上，代码采用 Apache License 2.0 协议授权。构建 Maven 需要
  Java 17 以上版本和 Maven 3.9.0 以上版本。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Apache Software Foundation
  technologies:
  - Maven
  - POM
  - Java
  key_people: []
key_logic_flow:
- Apache Maven 是一款基于项目对象模型（POM）概念的软件项目管理和理解工具。
- Maven 可以从统一的信息中心管理项目的构建、报告和文档。
- 构建 Maven 需要 Java 17 或以上版本以及 Maven 3.9.0 或以上版本。
- Maven 的源代码使用 Apache License 2.0 协议进行授权。
- 用户可以通过 `mvn -DdistributionTargetDir=... clean package` 命令编译生成 Maven 发行版。
- 项目托管在 GitHub 上，用户可以通过 Issue Tracker 提交 bug 报告。
specialized_tags:
  github:
    projectName: apache/maven
    projectUrl: https://github.com/apache/maven
    primaryLanguage: Java
    licenseType: Apache 2.0
    domain: developer_tools
    crossTags:
    - build-automation
    - project-management
    - java
extract_result: success
object_mentions:
- object_type: project
  name: apache/maven
  canonical_name: apache/maven
  url: https://github.com/apache/maven
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Apache Maven 是一款基于项目对象模型（POM）概念的软件项目管理和理解工具。
  - Maven 可以从统一的信息中心管理项目的构建、报告和文档。
  - 构建 Maven 需要 Java 17 或以上版本以及 Maven 3.9.0 或以上版本。
  article_id: a7aae41bfe46e3ba
---

Apache Maven is a software project management and comprehension tool. Based on the concept of a project object model (POM), Maven can manage a project's build, reporting and documentation from a central piece of information.

If you think you have found a bug, please file an issue in the Maven Issue Tracker.

More information can be found on Apache Maven Homepage. Questions related to the usage of Maven should be posted on the Maven User List.

You can download the release source from our download page.

If you are interested in the development of Maven, please consult the documentation first and afterward you are welcome to join the developers mailing list to ask questions or discuss new ideas/features/bugs etc.

Take a look into the contribution guidelines.

This code is under the Apache License, Version 2.0, January 2004.

See the `NOTICE`

file for required notices and attributions.

Do you like Apache Maven? Then donate back to the ASF to support the development.

If you want to bootstrap Maven, you'll need:

- Java 17+
- Maven 3.9.0 or later
- Run Maven, specifying a location into which the completed Maven distro should be installed:
`mvn -DdistributionTargetDir="$HOME/app/maven/apache-maven-4.1.x-SNAPSHOT" clean package`