---
url: https://docs.cloud.google.com/docs/migration/overview/migrate-modernize-overview/
title: Migration and modernization overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:39:40.808675+00:00
---

# Migration and modernization overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/migration/overview/migrate-modernize-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Guides ](https://docs.cloud.google.com/docs/migration/overview/migrate-modernize-overview)



Send feedback 

#  Migration and modernization overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the products, methodologies, and technical pathways available to migrate workloads to Google Cloud and to modernize applications and mainframe systems.

If you are a cloud architect, enterprise IT leader, application developer, or migration specialist, use the information on this page to evaluate your migration and modernization requirements, compare transformation patterns (such as lift and shift, containerization, AI-assisted code refactoring, and automated mainframe conversion), and choose the appropriate Google Cloud tools for your migration and modernization workloads.

Before you read this page, you should have a basic understanding of your existing on-premises or third-party cloud infrastructure, application architecture, codebase dependencies, and legacy mainframe systems.

## Choose a migration and modernization path

Choose a migration and modernization path that aligns with your source environment and technical goals.

### Workload migration

Use the following resources to migrate virtual machines, relational databases, containers, or object storage from on-premises data centers or third-party cloud providers, including AWS or Azure, to Google Cloud:

  * **Primary tools** : [Google Cloud Migration Center](https://docs.cloud.google.com/migration-center/docs/migration-center-overview), [Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0), [Database Migration Service](https://docs.cloud.google.com/database-migration/docs/overview), and [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview).
  * **Use cases** : virtual machine migration, database replatforming, unstructured data transfer, and multi-cloud workload mobility.
  * **Get started** : [Virtual machine migration](https://docs.cloud.google.com/docs/migration/scenarios/virtual-machine-migration.md).



### Application modernization

Use the following resources to refactor legacy codebases, modernize application frameworks, and transition to cloud-native microservices on Google Cloud:

  * **Primary tools** : [Google Cloud Modernization Hub](https://docs.cloud.google.com/modernize/hub/overview), [Antigravity CLI](https://antigravity.google/product/antigravity-cli), and [Antigravity](https://antigravity.google/).
  * **Use cases** : application framework upgrades, AI-assisted code refactoring, containerization for Java workloads, and serverless migration.
  * **Get started** : [Application modernization overview](https://docs.cloud.google.com/docs/migration/overview/app-modernization-overview).



### Mainframe modernization

Use the following resources to modernize legacy mainframe systems (such as COBOL, PL/I, and JCL) into cloud-native microservices on Google Cloud:

  * **Primary tools** : [Modernization Hub](https://docs.cloud.google.com/modernize/hub/overview), [Mainframe Assessment Tool (MAT)](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview), [Antigravity CLI](https://antigravity.google/product/antigravity-cli), [Mainframe Connector](https://docs.cloud.google.com/mainframe-connector/docs/overview), and [Dual Run](https://docs.cloud.google.com/mainframe-dual-run/docs/dual-run-overview).
  * **Use cases** : automated reverse engineering, business rule extraction, cloud microservice code generation, and parallel validation.
  * **Get started** : [Mainframe modernization overview](https://docs.cloud.google.com/docs/migration/overview/mainframe-modernization-overview).



## Rapid Migration and Modernization Program (RaMP)

The Rapid Migration and Modernization Program (RaMP) is a Google Cloud global program for migration and modernization initiatives. RaMP provides a prescriptive framework, resources, and tools to help you execute migrations and modernizations to Google Cloud.

For more information, see the [Rapid Migration and Modernization Program (RaMP) overview](https://docs.cloud.google.com/migration-center/docs/ramp-overview).

## Migration and modernization methodologies

When evaluating workloads during initial discovery, assign them to one of the following six standard migration strategies:

Strategy | Description | Use case | Primary tools  
---|---|---|---  
**Lift and shift** | Move applications to Google Cloud without changing architecture or code. | Rapid data center evacuation, legacy software with fixed dependencies. | Migrate to VMs  
**Replatform** | Move workloads to managed platforms with minimal code changes. | Moving on-premises relational databases to managed cloud databases or modernizing proprietary engines to AlloyDB for PostgreSQL. | Database Migration Service  
**Refactor** _(modernize)_ | Re-architect applications to use cloud features and microservices. | Decomposing monolithic applications into containers or serverless, and converting legacy mainframe code to modern target languages, such as Java or Go. | Modernization Hub, Antigravity CLI, Mainframe Assessment Tool  
**Repurchase** | Replace custom or legacy on-premises software with software as a service (SaaS) solutions. | Replacing legacy self-hosted email or customer relationship management (CRM) software with Google Workspace or SaaS partners. | Managed SaaS integrations  
**Retire** | Decommission applications or servers that are no longer needed. | Outdated test environments or redundant reporting servers. | Not applicable  
**Retain** | Keep applications in their source environment due to compliance or technical constraints. | Legacy hardware with non-migratable physical hardware dependencies. | Not applicable  
  
### Application modernization strategies

When modernizing applications, choose one of the following approaches to transform monolithic architectures and legacy runtimes into scalable, cloud-native services:

  * **Modernization assessment and Java workload containerization** : assess .NET and Java workloads by using Modernization Hub to evaluate transformation paths such as framework upgrades, and package Java workloads into Open Container Initiative (OCI)-compliant containers for deployment to Google Kubernetes Engine (GKE) or Cloud Run.
  * **Framework upgrading and code refactoring** : modernize legacy runtimes, such as from .NET Framework to .NET 10, and decompose monoliths into microservices by using Antigravity CLI and generative AI tools.
  * **Serverless transformation** : re-architect event-driven workloads, batch jobs, and REST APIs into managed serverless runtimes by using Cloud Run to reduce infrastructure management.



### Database migration strategies

When planning database migrations, choose one of the following strategies to balance data consistency requirements against acceptable application downtime:

  * **Offline migration (scheduled maintenance)** : stop writes to the source database, export the dataset, import it to Google Cloud, and redirect application connection strings. This approach is ideal for non-critical workloads or small datasets that can tolerate planned maintenance windows.
  * **Online migration (continuous replication)** : take an initial database snapshot and stream transactional updates continuously by using change data capture (CDC) until final cutover. This approach is ideal for mission-critical systems requiring minimal downtime and business continuity.



### Mainframe modernization strategies

When modernizing mainframe systems, use the following phased approach to extract business logic and validate parity while minimizing operational risk:

  1. **Reverse engineering** : use the Mainframe Assessment Tool (MAT) to extract underlying business logic, program call trees, and data schemas.
  2. **Forward engineering** : transform extracted business logic into cloud microservices in target languages, such as Java or Go, by using Antigravity CLI.
  3. **Dual Run validation** : process live production transactions in parallel across the mainframe and Google Cloud environments by using Dual Run to achieve functional parity before final cutover.



## What's next

  * [Application modernization overview](https://docs.cloud.google.com/docs/migration/overview/app-modernization-overview)
  * [Mainframe modernization overview](https://docs.cloud.google.com/docs/migration/overview/mainframe-modernization-overview)
  * [Enterprise landing zones and foundations](https://docs.cloud.google.com/docs/migration/plan/landing-zones.md)
  * [Modernization Hub documentation](https://docs.cloud.google.com/modernize/hub/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
