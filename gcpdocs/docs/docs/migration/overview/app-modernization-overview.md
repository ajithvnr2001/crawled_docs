---
url: https://docs.cloud.google.com/docs/migration/overview/app-modernization-overview/
title: Application modernization overview \u00a0|\u00a0 Migration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:38:58.237366+00:00
---

# Application modernization overview  |  Migration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/migration/overview/app-modernization-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Guides ](https://docs.cloud.google.com/docs/migration/overview/migrate-modernize-overview)



Send feedback 

#  Application modernization overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an architectural overview of the strategies, tools, and pathways available to modernize legacy monolithic applications and serverless workloads into cloud-native microservices on Google Cloud.

If you are a cloud architect, application developer, or engineering lead, use the information on this page to evaluate application modernization pathways, assess container readiness for Java workloads with Google Cloud Modernization Hub, refactor codebases by using generative AI, and deploy to Google Kubernetes Engine (GKE) and Cloud Run.

Before you read this page, you should have an understanding of your existing application architectures, source code dependencies, and target runtime requirements.

## Application modernization pathways

Choose an appropriate application modernization pathway based on your source workload architecture and development goals. The following diagram illustrates three pathways for modernizing applications:

![Flowchart illustrating three modernization paths: .NET and Java modernization with Modernization Hub, AI-assisted code refactoring, and serverless Lambda-to-Cloud Run migration.](https://docs.cloud.google.com/docs/migration/images/app-modernization-pathways.svg)

Each pathway addresses a specific modernization scenario:

  * **.NET and Java workload modernization** : assesses .NET and Java workloads by using Modernization Hub to evaluate transformation paths such as framework upgrades and containerization for Java workloads.
  * **AI-assisted code refactoring** : modernizes legacy frameworks and decomposes monolithic architectures by using generative AI.
  * **Serverless migration** : converts event-driven functions into portable, containerized HTTP microservices.



## .NET and Java workload modernization

[Modernization Hub](https://docs.cloud.google.com/modernize/hub/overview) helps you assess ASP.NET, .NET Framework, and Java workloads and evaluate transformation paths such as framework upgrades and containerization for Java workloads across three phases:

  1. **Workload assessment** : analyze source archives in [Cloud Storage](https://docs.cloud.google.com/storage/docs) to evaluate codebase compatibility and modernization effort without provisioning separate compute instances.
  2. **Blocker detection** : identify OS-specific and framework blockers (such as Windows Registry calls, Windows Communication Foundation (WCF) services, Internet Information Services (IIS) dependencies, and legacy Java EE namespaces) in downloadable HTML and Markdown reports.
  3. **Transformation planning** : evaluate recommended transformation paths, including framework and dependency upgrades for .NET and Java workloads, and Linux containerization for Java workloads on [GKE](https://docs.cloud.google.com/kubernetes-engine/docs) or [Cloud Run](https://docs.cloud.google.com/run/docs).



For more information, see [Assess .NET applications](https://docs.cloud.google.com/modernize/hub/assess-dotnet), [Assess Java applications](https://docs.cloud.google.com/modernize/hub/assess-java), and [Containerized application migration](https://docs.cloud.google.com/docs/migration/scenarios/container-migration.md).

## AI-assisted code refactoring

To analyze and modernize legacy application code, such as upgrading .NET Framework 4.x or modernizing Java workloads for Linux containers, [Modernization Hub](https://docs.cloud.google.com/modernize/hub/overview), the [Antigravity CLI](https://antigravity.google/product/antigravity-cli), and [Antigravity](https://antigravity.google/) support the following workflow:

  1. **Dependency assessment** : scan source code repositories to identify unsupported APIs, tightly coupled monolithic components, and target runtime compatibility.
  2. **Code refactoring** : use [Antigravity CLI](https://antigravity.google/product/antigravity-cli) to transform legacy framework calls into modern, cross-platform equivalents.
  3. **Artifact generation** : generate multi-stage Dockerfiles and configuration files for target applications.



## Serverless migration

Migrating serverless functions from AWS Lambda to Cloud Run involves the following stages:

  1. **Runtime dependency evaluation** : identify event triggers, environment variables, and execution limits.
  2. **Execution wrapper refactoring** : use the Antigravity CLI to adapt AWS Lambda event handlers into standard HTTP stateless container handlers.
  3. **Cloud Run deployment** : package the function as a container and deploy it to [Cloud Run](https://docs.cloud.google.com/run/docs) for autoscaling with pay-per-use billing.



## Reference architectures

For in-depth architectural patterns and modernization reference guides, see the following resources in the Google Cloud Architecture Center:

  * [Migrate AWS Lambda to Cloud Run](https://docs.cloud.google.com/architecture/migrate-aws-lambda-to-cloudrun)
  * [Migrate containers to GKE](https://docs.cloud.google.com/architecture/migrating-containers-kubernetes-gke)
  * [Application development resources](https://docs.cloud.google.com/architecture/application-development)



## What's next

  * [Containerized application migration](https://docs.cloud.google.com/docs/migration/scenarios/container-migration.md)
  * [Mainframe modernization overview](https://docs.cloud.google.com/docs/migration/overview/mainframe-modernization-overview)
  * [Modernization Hub documentation](https://docs.cloud.google.com/modernize/hub/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
