---
url: https://docs.cloud.google.com/docs/migration/scenarios/mainframe-refactor/
title: Mainframe application refactoring \u00a0|\u00a0 Migration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:39:50.848055+00:00
---

# Mainframe application refactoring  |  Migration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/migration/scenarios/mainframe-refactor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Guides ](https://docs.cloud.google.com/docs/migration/overview/migrate-modernize-overview)



Send feedback 

#  Mainframe application refactoring Stay organized with collections  Save and categorize content based on your preferences. 

This page provides architectural guidance and forward-engineering methodologies for refactoring monolithic legacy mainframe applications into modular cloud-native microservices on Google Cloud.

If you are a cloud architect, application developer, or engineering lead, use the information on this page to transform procedural mainframe code, such as COBOL or PL/I, into modern codebases, such as Java or Go, generate microservices by using generative AI, and deploy to Google Kubernetes Engine (GKE) or Cloud Run.

Before you read this page, you should have completed an initial mainframe codebase assessment and extracted your application's core business rules.

## Refactoring lifecycle

Refactoring uses AI-assisted forward engineering to convert extracted business logic into maintainable microservices through the following phases:

  1. **Extract business logic** : use the [Mainframe Assessment Tool](https://docs.cloud.google.com/mainframe-assessment-tool/docs) to extract validated business rules and control flows from the original source code.
  2. **Generate requirements** : transform assessment outputs into structured product requirements documents (PRDs) by using the [Antigravity CLI](https://antigravity.google/product/antigravity-cli). Export [dependency graphs and assessment results](https://docs.cloud.google.com/mainframe-assessment-tool/docs/export-results) into the Antigravity CLI to generate equivalent target language microservice contracts.
  3. **Refactor target databases** : re-architect VSAM flat files or DB2 schemas into modern relational and distributed data models on [Spanner](https://docs.cloud.google.com/spanner/docs) or [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs).



## What's next

  * [Automated mainframe code conversion](https://docs.cloud.google.com/docs/migration/scenarios/automated-conversion)
  * [Mainframe workload lift and shift](https://docs.cloud.google.com/docs/migration/scenarios/mainframe-lift-shift)
  * [Mainframe Assessment Tool documentation](https://docs.cloud.google.com/mainframe-assessment-tool/docs)
  * [Dual Run documentation](https://docs.cloud.google.com/mainframe-dual-run/docs)
  * [Mainframe Connector documentation](https://docs.cloud.google.com/mainframe-connector/docs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
