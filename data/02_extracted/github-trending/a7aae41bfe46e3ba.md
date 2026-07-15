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
tldr: Apache Maven 是基于 POM 的软件项目管理和构建工具。
objective_summary: Apache Maven 是一个软件项目管理和理解工具，基于项目对象模型（POM）概念，用于管理项目的构建、报告和文档。构建需要
  Java 17+ 和 Maven 3.9.0+，采用 Apache License 2.0 许可证。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Apache Software Foundation
  technologies:
  - Maven
  - POM (Project Object Model)
  key_people: []
key_logic_flow:
- Apache Maven 是一个软件项目管理和理解工具，核心概念是项目对象模型（POM）。
- Maven 可以从统一的信息中心管理项目的构建、报告和文档生命周期。
- 构建 Maven 需要 Java 17+ 环境和 Maven 3.9.0 或更高版本的引导。
- 该项目采用 Apache License 2.0 开源许可证。
- 用户可通过 Maven Issue Tracker 提交 bug 报告，通过邮件列表参与开发讨论。
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