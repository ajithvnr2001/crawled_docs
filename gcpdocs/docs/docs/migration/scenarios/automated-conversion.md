---
url: https://docs.cloud.google.com/docs/migration/scenarios/automated-conversion/
title: Automated mainframe code conversion \u00a0|\u00a0 Migration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:36:46.461313+00:00
---

# Automated mainframe code conversion  |  Migration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/migration/scenarios/automated-conversion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Guides ](https://docs.cloud.google.com/docs/migration/overview/migrate-modernize-overview)



Send feedback 

#  Automated mainframe code conversion Stay organized with collections  Save and categorize content based on your preferences. 

This page provides architectural guidance and operational workflows for automating mainframe code generation and validating functional parity on Google Cloud.

If you are a cloud architect, application developer, or migration engineer, use the information on this page to synthesize extracted technical metadata into modern microservices in target languages, such as Java or Go, by using the Antigravity CLI, and validate production parity with Dual Run before cutover.

Before you read this page, you should have completed legacy code analysis, extracted your business rules, and defined your target architecture specifications.

## Automated code generation workflow

AI-assisted code generation combines four core inputs—extracted business logic from the [Mainframe Assessment Tool](https://docs.cloud.google.com/mainframe-assessment-tool/docs), technical schema metadata, product requirements documents (PRDs), and target architecture templates—to produce microservice implementations, as shown in the following diagram:

![Architecture diagram showing the four core inputs combining into the
AI-assisted code generation
workflow.](https://docs.cloud.google.com/docs/migration/images/automated-code-gen-workflow.svg)

## Parallel validation with Dual Run

To reduce the risk of cutovers, Dual Run validates parallel transactions by using the following components:

  * **Interceptor proxy** : captures incoming HTTP, 3270, Socket, or MQ requests on the legacy mainframe and forwards live payloads to [Pub/Sub](https://docs.cloud.google.com/pubsub/docs).
  * **Dualizer replay engine** : replays captured online transactions against the modernized secondary system running on Google Cloud.
  * **Data comparator** : automatically compares responses and database state between the legacy mainframe and Google Cloud instances in real time.
  * **Parity dashboard** : tracks functional parity metrics in [BigQuery](https://docs.cloud.google.com/bigquery/docs) dashboards to support switchover decisions.



## What's next

  * [Mainframe workload lift and shift](https://docs.cloud.google.com/docs/migration/scenarios/mainframe-lift-shift)
  * [Dual Run documentation](https://docs.cloud.google.com/mainframe-dual-run/docs)
  * [Mainframe Assessment Tool documentation](https://docs.cloud.google.com/mainframe-assessment-tool/docs)
  * [Mainframe Connector documentation](https://docs.cloud.google.com/mainframe-connector/docs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
