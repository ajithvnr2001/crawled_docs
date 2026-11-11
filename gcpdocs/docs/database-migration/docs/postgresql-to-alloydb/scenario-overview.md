---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview/
title: Database Migration Service for PostgreSQL to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:33:43.476391+00:00
---

# Database Migration Service for PostgreSQL to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview)



Send feedback 

#  Database Migration Service for PostgreSQL to AlloyDB for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

You can migrate PostgreSQL databases to AlloyDB for PostgreSQL clusters with Database Migration Service. This page provides an overview of the key Database Migration Service features for homogeneous PostgreSQL to AlloyDB for PostgreSQL migrations:

  * Supported source and destination lists all PostgreSQL source offerings supported by Database Migration Service.

  * Data flow for standard migrations provides an end-to-end overview of how your data moves during the continuous migration process.

  * Quick-start migrations describes a unique migration flow that leverages `pgnative` replication and significantly simplifies networking configuration for PostgreSQL workloads.

  * Monitoring gives an introduction to logs and metrics that can help you observe the progress and health of your migration job.




## Supported source and destination databases

You can use Database Migration Service to migrate between the same PostgreSQL version, or from earlier versions of PostgreSQL to later versions supported in AlloyDB for PostgreSQL.

The following table lists all supported PostgreSQL source and destination database offerings. For the full list of exact versions and cross-version support, see [ Supported sources and versions](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest).

Source databases | Destination databases  
---|---  
Amazon RDS | AlloyDB for PostgreSQL cluster  
Amazon Aurora  
Cloud SQL for PostgreSQL  
Self-managed PostgreSQL (on premises or on any cloud VM that you fully control)  
  
## Data flow for standard migrations

For homogeneous PostgreSQL migrations to AlloyDB for PostgreSQL, Database Migration Service connects to the _destination_ AlloyDB for PostgreSQL cluster primary instance and then manages the migration process on its behalf. The destination primary instance establishes the connection to your source instance, while Database Migration Service orchestrates and monitors the continuous replication flow. An AlloyDB for PostgreSQL cluster consists of a primary instance and optional read pool instances that provide read scalability and high availability.

![PostgreSQL migration flow overview](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/alloydb/alloydb_hmm_end2end_flow.svg) **Figure 1.** Data movement during Database Migration Service for PostgreSQL migrations. (click to enlarge) ![PostgreSQL migration flow overview](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/alloydb/alloydb_hmm_end2end_flow.svg)

Standard continuous migrations use PostgreSQL logical decoding and the `pglogical` extension to stream data changes from the source instance to the destination cluster in near real time. Your data is first loaded from an initial snapshot dump, and then continuously updated based on change data capture (CDC) stream information.

For a detailed walkthrough of all migration phases, see [ Migration types and phases](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-types).

## Quick-start migrations (Preview)

Database Migration Service provides quick-start migrations to help you migrate PostgreSQL workloads to AlloyDB for PostgreSQL clusters with minimal manual setup. In a quick-start migration, Database Migration Service automates the configuration of the migration path by provisioning a Private Service Connect-enabled destination cluster and orchestrating connectivity to your private source database through Private Service Connect network attachments.

Key capabilities of quick-start migrations include:

  * **Automated setup** : Database Migration Service eliminates the need to install the `pglogical` extension on the source database and automates connection profile and private connectivity setup in the Google Cloud console.
  * **Simplified networking** : Connect securely to private source databases without managing complex VPNs or public IP allowlists.
  * **Pre-migration validation** : Built-in verification checks ensure your source environment is fully prepared before data replication begins.



For more information, see [ About quick-start migrations](https://docs.cloud.google.com/database-migration/docs/about-quick-start-migrations) and the [ Quick-start migrations guide](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/quick-start-migrations-guide).

## Monitoring

Database Migration Service provides extensive logging and observability capabilities to help you monitor migration progress. These features include real-time diagnostics for replication delay, as well as detailed Cloud Monitoring metrics for destination AlloyDB for PostgreSQL cluster health and migration job state.

![Example diagrams for migration job metrics in Database Migration Service.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/hmm_mysql_pgsql_alloydb_standard_metrics.png) **Figure 2.** Sample observability diagrams in Database Migration Service (click to enlarge). ![Example diagrams for migration job metrics in Database Migration Service.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/hmm_mysql_pgsql_alloydb_standard_metrics.png)

For more details, see [ Migration job metrics](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-job-metrics).

## What's next

  * To learn more about PostgreSQL data and feature support in Database Migration Service, see [ Known limitations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations).

  * To review the end-to-end migration walkthroughs, see:

    * [ Get started with AlloyDB for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/get-started-with-alloydb-migrations)
    * [ Migrate to a new AlloyDB for PostgreSQL cluster](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/guide-to-new-instance)
    * [ Migrate to an existing AlloyDB for PostgreSQL cluster](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/guide-to-existing-instance)
    * [ Quick-start migrations guide](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/quick-start-migrations-guide)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
