---
url: https://docs.cloud.google.com/docs/migration/overview/mainframe-modernization-overview/
title: Mainframe modernization overview \u00a0|\u00a0 Migration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:39:29.061475+00:00
---

# Mainframe modernization overview  |  Migration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/migration/overview/mainframe-modernization-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Guides ](https://docs.cloud.google.com/docs/migration/overview/migrate-modernize-overview)



Send feedback 

#  Mainframe modernization overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the tools, strategies, and structured workflows for modernizing legacy mainframe workloads on Google Cloud.

If you are an enterprise cloud architect, mainframe engineer, or migration specialist, use the information on this page to evaluate mainframe assessment tools, modernize mainframe data, generate cloud-native services by using AI-assisted tooling, and validate functional parity before cutover.

Before you read this page, you should have an inventory of your mainframe applications (such as COBOL, PL/I, JCL, and DB2/VSAM datasets) and an understanding of your target cloud architecture goals.

## Choose a mainframe modernization pathway

Use the following table to choose a modernization strategy and the recommended Google Cloud tools based on your source workload and modernization goals:

Modernization pathway | Source workload | Recommended tools | Target services | Scenario guide  
---|---|---|---|---  
**AI-assisted application refactoring** | Monolithic COBOL, PL/I, and CICS applications |  [Google Cloud Modernization Hub](https://docs.cloud.google.com/modernize/hub/overview), [Mainframe Assessment Tool](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview), [Antigravity CLI](https://antigravity.google/product/antigravity-cli) |  [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs), [Cloud Run](https://docs.cloud.google.com/run/docs), [Spanner](https://docs.cloud.google.com/spanner/docs), or [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs) |  [Mainframe application refactoring](https://docs.cloud.google.com/docs/migration/scenarios/mainframe-refactor)  
**Automated code conversion and validation** | Extracted business rules and legacy procedural codebases |  [Antigravity CLI](https://antigravity.google/product/antigravity-cli), [Dual Run](https://docs.cloud.google.com/mainframe-dual-run/docs/dual-run-overview) |  [Cloud Run](https://docs.cloud.google.com/run/docs) or [GKE](https://docs.cloud.google.com/kubernetes-engine/docs) |  [Automated mainframe code conversion](https://docs.cloud.google.com/docs/migration/scenarios/automated-conversion)  
**Mainframe lift and shift (Emulation)** | IBM z/OS or IBM i workloads requiring minimal code changes |  Partner emulation runtimes, [Mainframe Connector](https://docs.cloud.google.com/mainframe-connector/docs) |  [Compute Engine](https://docs.cloud.google.com/compute/docs), [Cloud SQL](https://docs.cloud.google.com/sql/docs) |  [Mainframe workload lift and shift](https://docs.cloud.google.com/docs/migration/scenarios/mainframe-lift-shift)  
**Data offloading and analytics** | EBCDIC batch datasets, VSAM files, and DB2 tables |  [Mainframe Connector](https://docs.cloud.google.com/mainframe-connector/docs) |  [BigQuery](https://docs.cloud.google.com/bigquery/docs), [Cloud Storage](https://docs.cloud.google.com/storage/docs) |  [Mainframe Connector configurations](https://docs.cloud.google.com/mainframe-connector/docs/configurations)  
  
## Key capabilities

Google Cloud provides the following tools and services for each phase of mainframe modernization:

  * **Automated application assessment** : [Mainframe Assessment Tool (MAT)](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview) reverse-engineers source code (COBOL, PL/I, JCL), maps program and data dependencies, and extracts embedded business rules.
  * **AI-assisted forward engineering** : [Antigravity CLI](https://antigravity.google/product/antigravity-cli) and [Antigravity](https://antigravity.google/) assist developers in converting extracted business rules into modern, cloud-native services in target languages, such as Java or Go, running on [GKE](https://docs.cloud.google.com/kubernetes-engine/docs) or [Cloud Run](https://docs.cloud.google.com/run/docs).
  * **Data modernization** : [Mainframe Connector](https://docs.cloud.google.com/mainframe-connector/docs) transcodes and moves mainframe datasets (EBCDIC) into Google Cloud services such as [BigQuery](https://docs.cloud.google.com/bigquery/docs) and [Cloud Storage](https://docs.cloud.google.com/storage/docs).
  * **Functional validation** : [Dual Run](https://docs.cloud.google.com/mainframe-dual-run/docs/dual-run-overview) runs production workloads simultaneously on the mainframe and Google Cloud to verify data consistency and functional parity before cutover.



## Reverse and forward engineering

Mainframe modernization relies on the following dual-discipline approach to extract logic and rebuild applications safely:

  1. **Reverse engineering** : analyzes existing mainframe applications to understand the codebase before modernization begins. By using Mainframe Assessment Tool (MAT), you map application dependencies and extract business rules from legacy code (COBOL, PL/I). MAT uses generative AI to produce technical specifications and catalog data structures.
  2. **Forward engineering** : transforms high-level business requirements and extracted rules into modern application code. In mainframe modernization, forward engineering uses automated tools and Antigravity CLI to convert business rules into functional specifications, product requirements documents (PRDs), user stories, and cloud services on Google Cloud.



## Modernization workflow

The following diagram illustrates the five phases of the mainframe modernization process:

![Workflow diagram showing the five mainframe planning workflow phases: Phase 1 Ingest and reverse engineer, Phase 2 Extract business rules, Phase 3 Decompose monolith, Phase 4 Author PRD and data model, and Phase 5 Wave sequencing and validation.](https://docs.cloud.google.com/docs/migration/images/mainframe-planning-workflow.svg)

### Phase 1: Ingest and reverse engineer source code

In Phase 1, you use [Mainframe Assessment Tool (MAT)](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview) to analyze your existing mainframe applications across the following capabilities:

  * **Source code ingestion** : inventory and parse COBOL, PL/I, Assembler, JCL batch jobs, copybooks, and database schemas.
  * **Data dependency mapping** : identify relationships across DB2 tables, VSAM files, IMS databases, and flat files.
  * **Call tree creation** : generate visual program call graphs showing batch sequences and online Customer Information Control System (CICS) transaction flows to establish migration waves.



For more information, see [Set up Mainframe Assessment Tool in Modernization Hub](https://docs.cloud.google.com/modernize/hub/setup-mat), [Create an assessment](https://docs.cloud.google.com/mainframe-assessment-tool/docs/perform-assessment), and [Review assessment results](https://docs.cloud.google.com/mainframe-assessment-tool/docs/review-results).

### Phase 2: Extract embedded business rules

Before you generate modern applications, isolate and verify critical business logic from complex legacy COBOL or PL/I code blocks:

  * **AI-assisted rule extraction** : Mainframe Assessment Tool uses Gemini to analyze source code line by line and translate complex conditional logic into plain-English business rules.
  * **Rule isolation** : extract domain-specific validation, interest calculation, or transaction logic from procedural code.
  * **Human-in-the-loop review** : domain experts and business analysts review, refine, and certify the extracted business rules.
  * **Documentation generation** : automatically compile up-to-date technical specifications for legacy programs.



For more information, see [Extract business rules](https://docs.cloud.google.com/mainframe-assessment-tool/docs/business-rules-extraction).

### Phase 3: Decompose monoliths into business domains

Before you deploy microservices, partition monolithic mainframe codebases into bounded contexts and decoupled, migratable business domains:

  * **Domain mapping** : segment code assets into logical business domains (such as accounts, billing, and payments).
  * **Shared dataset decoupling** : identify shared VSAM or DB2 data structures that must be split into service-specific databases.
  * **Interface definition** : define REST or gRPC API boundaries for extracted services.



For more information, see [Review AI-generated insights for your business domains](https://docs.cloud.google.com/mainframe-assessment-tool/docs/review-results#analyze-domain).

### Phase 4: Author PRDs, data models, and modern code

Use the [Antigravity CLI](https://antigravity.google/product/antigravity-cli) to transform extracted assessment outputs into structured specifications, target architectures, and modern application code on Google Cloud:

  * **PRD and user story generation** : synthesize assessment data into functional specifications, product requirements documents (PRDs) detailing Critical User Journeys (CUJs) and operational SLAs, and agile engineering tasks.
  * **Target cloud architecture** : choose target compute runtimes ([Cloud Run](https://docs.cloud.google.com/run/docs), [GKE](https://docs.cloud.google.com/kubernetes-engine/docs), or [Compute Engine](https://docs.cloud.google.com/compute/docs)).
  * **Target data modeling** : design data structures (relational, file, key-value) and choose modern cloud database schemas based on your workload: 
    * Relational global scale: [Spanner](https://docs.cloud.google.com/spanner/docs)
    * Enterprise PostgreSQL: [AlloyDB](https://docs.cloud.google.com/alloydb/docs) or [Cloud SQL](https://docs.cloud.google.com/sql/docs)
    * Analytics and reporting: [BigQuery](https://docs.cloud.google.com/bigquery/docs)
  * **Automated code generation** : sequence implementation blueprints and generate application code in target languages, such as Java or Go, that implements the extracted business rules and target data models.



For instructions on configuring exported `AGENTS.md` files, enabling the Mainframe Assessment Tool MCP server, and verifying generated code, see [Modernize and validate](https://docs.cloud.google.com/mainframe-assessment-tool/docs/modernize-validate).

### Phase 5: Sequence migration waves and validate parity

Before production switchover, migrate datasets in structured waves and validate functional parity:

  * **Mainframe data modernization** : configure [Mainframe Connector](https://docs.cloud.google.com/mainframe-connector/docs) for high-volume transcoding of legacy EBCDIC datasets to [Cloud Storage](https://docs.cloud.google.com/storage/docs) and [BigQuery](https://docs.cloud.google.com/bigquery/docs).
  * **Incremental wave cutover** : schedule modernization waves by business domain rather than executing a full-system cutover.
  * **Functional parity testing** : use [Dual Run](https://docs.cloud.google.com/mainframe-dual-run/docs/dual-run-overview) to replay live mainframe transactions in parallel against Google Cloud to validate modernized applications and verify functional parity before retiring legacy code.
  * **Deployment and operations** : deploy modernized workloads to production and monitor performance by using Google Cloud Observability.



For more information, see [Transcode and migrate data](https://docs.cloud.google.com/mainframe-connector/docs/agentic-tools-to-transcode-and-migrate-data) and [Validate functional parity](https://docs.cloud.google.com/mainframe-dual-run/docs/dual-run-overview).

## What's next

  * [Mainframe application refactoring](https://docs.cloud.google.com/docs/migration/scenarios/mainframe-refactor.md)
  * [Automated mainframe code conversion](https://docs.cloud.google.com/docs/migration/scenarios/automated-conversion.md)
  * [Mainframe workload lift and shift](https://docs.cloud.google.com/docs/migration/scenarios/mainframe-lift-shift.md)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
