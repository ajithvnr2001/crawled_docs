---
url: https://docs.cloud.google.com/architecture/migration-from-azure-get-started/
title: Migrate from Azure to Google Cloud: Get started \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:01:46.878878+00:00
---

# Migrate from Azure to Google Cloud: Get started  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/migration-from-azure-get-started/

[ Skip to main content ](https://docs.cloud.google.com/architecture/migration-from-azure-get-started/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/architecture/migration-from-azure-get-started/)
  * [Deutsch](https://docs.cloud.google.com/architecture/migration-from-azure-get-started/?hl=de)
  * [Español](https://docs.cloud.google.com/architecture/migration-from-azure-get-started/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/architecture/migration-from-azure-get-started/?hl=es-419)
  * [Français](https://docs.cloud.google.com/architecture/migration-from-azure-get-started/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/architecture/migration-from-azure-get-started/?hl=id)
  * [Italiano](https://docs.cloud.google.com/architecture/migration-from-azure-get-started/?hl=it)
  * [Português](https://docs.cloud.google.com/architecture/migration-from-azure-get-started/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/architecture/migration-from-azure-get-started/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/architecture/migration-from-azure-get-started/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/architecture/migration-from-azure-get-started/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/architecture/migration-from-azure-get-started/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/architecture/migration-from-azure-get-started/?hl=ja)
  * [한국어](https://docs.cloud.google.com/architecture/migration-from-azure-get-started/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/static/site-assets/images/cloud.svg) ](https://docs.cloud.google.com/architecture)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [What's next](https://docs.cloud.google.com/architecture/migration-from-azure-get-started/#whats_next)
  * [Contributors](https://docs.cloud.google.com/architecture/migration-from-azure-get-started/#contributors)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)


Was this helpful?
Send feedback 
#  Migrate from Azure to Google Cloud: Get started Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [What's next](https://docs.cloud.google.com/architecture/migration-from-azure-get-started/#whats_next)
  * [Contributors](https://docs.cloud.google.com/architecture/migration-from-azure-get-started/#contributors)


Last reviewed 2025-09-18 UTC
Google Cloud provides tools, products, guidance, and professional services to help you migrate workloads, data, and processes from Azure to Google Cloud. This document introduces a discussion about how to design, implement, and validate a plan to migrate from Azure to Google Cloud.
The discussion is intended for cloud administrators who want details about how to plan and implement a migration process. It's also intended for decision-makers who are evaluating the opportunity to migrate and who want to explore what migration looks like.
Google Cloud offers robust capabilities and support for running Microsoft stack-based workloads, with potential cost savings, depending on your specific needs. For example, Cloud Run provides a serverless environment that scales automatically based on demand for your .NET workloads, and Cloud SQL for SQL Server offers a fully managed, SQL Server-compatible database experience.
Migrating your workloads, data, and processes from Azure to Google Cloud can be a challenging task and can take days, weeks, or months to complete, depending on the scope and size of the migration.
Azure and Google Cloud products that target similar use cases might seem similar in the way you provision, configure, and use the resources that they provide. However, despite similarities, these resources might differ significantly in the way they work and in their requirements. We therefore recommend that you assess the ways in which similar Azure and Google Cloud resources work before you plan your migration.
This series provides guidance about the following migration journeys:
  * Get started (this document)
  * **From Azure compute services to Google Cloud**
    * [Migrate from Azure Virtual Machines to Compute Engine](https://googlecloudplatform.github.io/cloud-solutions/migrate-from-azure-to-google-cloud/migrate-from-azure-vms-to-compute-engine)
    * [Migrate from Azure Kubernetes Service to Google Kubernetes Engine](https://googlecloudplatform.github.io/cloud-solutions/migrate-from-azure-to-google-cloud/migrate-from-aks-to-gke)
  * **From Azure data storage services to Google Cloud**
    * [Migrate from Azure Blob Storage to Cloud Storage](https://googlecloudplatform.github.io/cloud-solutions/migrate-from-azure-to-google-cloud/migrate-from-azure-blob-storage-to-cloud-storage)
  * **From Azure database services to Google Cloud**
    * [Migrate from Azure SQL Managed Instance to Cloud SQL for SQL Server](https://googlecloudplatform.github.io/cloud-solutions/migrate-from-azure-to-google-cloud/migrate-azure-sql-managed-instance-to-cloud-sql-sql-server)
    * [Migrate from Azure SQL Database to Cloud SQL for SQL Server](https://googlecloudplatform.github.io/cloud-solutions/migrate-from-azure-to-google-cloud/migrate-azure-sql-database-to-cloud-sql-sql-server)
    * [Migrate from Azure Database for MySQL to Cloud SQL for MySQL](https://googlecloudplatform.github.io/cloud-solutions/migrate-from-azure-to-google-cloud/migrate-azure-database-mysql-to-cloud-sql-mysql)
    * [Migrate from Azure Database for PostgreSQL to Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL](https://googlecloudplatform.github.io/cloud-solutions/migrate-from-azure-to-google-cloud/migrate-azure-database-postgresql-to-cloud-sql-and-alloydb-postgresql)
    * [Migrate SQL Server to Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL](https://googlecloudplatform.github.io/cloud-solutions/migrate-from-azure-to-google-cloud/migrate-sql-server-to-cloud-sql-and-alloydb-postgresql)


## What's next
  * Read about [migrating and modernizing Microsoft workloads on Google Cloud](https://cloud.google.com/windows).
  * Learn how to [compare AWS and Azure services to Google Cloud](https://docs.cloud.google.com/free/docs/aws-azure-gcp-service-comparison).
  * Read about [other migration journeys to Google Cloud](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started).
  * Learn where to [find help for your migrations](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#finding_help).
  * Take the [Google Skills training course on migrating to Google Cloud](https://www.skills.google/course_templates/1561).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 


## Contributors
Authors: 
  * [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect
  * [Ido Flatow](https://www.linkedin.com/in/idoflatow) | Cloud Solutions Architect
  * [Alex Cârciu](https://www.linkedin.com/in/alex-carciu) | Solutions Architect


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-09-18 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-18 UTC."],[],[]] 
