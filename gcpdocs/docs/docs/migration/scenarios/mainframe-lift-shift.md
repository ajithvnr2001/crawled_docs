---
url: https://docs.cloud.google.com/docs/migration/scenarios/mainframe-lift-shift/
title: Mainframe workload lift and shift \u00a0|\u00a0 Migration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:39:07.528604+00:00
---

# Mainframe workload lift and shift  |  Migration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/migration/scenarios/mainframe-lift-shift/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Guides ](https://docs.cloud.google.com/docs/migration/overview/migrate-modernize-overview)



Send feedback 

#  Mainframe workload lift and shift Stay organized with collections  Save and categorize content based on your preferences. 

This page provides architectural guidance and emulation strategies for migrating legacy mainframe workloads (such as IBM z/OS or IBM i) to Google Cloud with minimal code modifications.

If you are a cloud architect, mainframe engineer, or infrastructure specialist, use the information on this page to evaluate emulation runtimes, re-platform mainframe workloads to Compute Engine, reduce mainframe MIPS licensing costs, and stream batch data to BigQuery by using Mainframe Connector.

Before you read this page, you should understand your mainframe workload MIPS consumption, application dependencies, and target emulation runtime requirements.

## Mainframe lift and shift architecture

A mainframe lift-and-shift migration replaces physical mainframe hardware with cloud virtual infrastructure, running legacy COBOL or PL/I programs in an emulation runtime environment on Compute Engine.

Alongside compute emulation, you can use [Mainframe Connector](https://docs.cloud.google.com/mainframe-connector/docs/overview) to offload CPU-intensive reporting workloads and reduce mainframe MIPS consumption. Mainframe Connector lets you complete the following tasks:

  * Transcode EBCDIC datasets (QSAM and VSAM) into ORC, JSON, or CSV formats.
  * Move data to Cloud Storage and BigQuery.
  * Submit BigQuery jobs directly from Job Control Language (JCL).



The following diagram illustrates the mainframe lift-and-shift architecture:

![Architecture diagram showing legacy COBOL and CICS programs running in a
partner emulation runtime environment on Compute Engine with data
ingestion into BigQuery and
Cloud Storage.](https://docs.cloud.google.com/docs/migration/images/mainframe-lift-shift-arch.svg)

## Key components

A mainframe lift-and-shift architecture includes the following components:

  * **Compute emulation runtimes** : deploy partner emulation engines, such as Micro Focus, NTT DATA, or LzLabs, on Compute Engine to run COBOL or CICS binaries without rewriting business logic.
  * **Dataset transcoding** : transcode EBCDIC datasets into ORC, JSON, or CSV formats and ingest high-volume mainframe batch files directly into BigQuery or Cloud Storage by using [Mainframe Connector](https://docs.cloud.google.com/mainframe-connector/docs).
  * **Database emulation** : re-platform DB2 or IMS data to managed cloud relational databases such as Cloud SQL or Spanner.



## What's next

  * [Mainframe Connector documentation](https://docs.cloud.google.com/mainframe-connector/docs)
  * [Mainframe Assessment Tool documentation](https://docs.cloud.google.com/mainframe-assessment-tool/docs)
  * [Dual Run documentation](https://docs.cloud.google.com/mainframe-dual-run/docs)
  * [Compute Engine documentation](https://docs.cloud.google.com/compute/docs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
