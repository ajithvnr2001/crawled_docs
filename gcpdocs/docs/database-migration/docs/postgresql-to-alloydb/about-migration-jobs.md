---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/about-migration-jobs/
title: About migration jobs \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-05T11:11:11.593083+00:00
---

# About migration jobs  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/about-migration-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview)



Send feedback 

#  About migration jobs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the migration jobs available in Database Migration Service for homogeneous PostgreSQL to AlloyDB for PostgreSQL migrations: for pre-existing destination clusters, and ones that Database Migration Service creates on your behalf during migration job configuration.

Migration jobs represent data movement managed by Database Migration Service. They let you configure settings specific to a particular migration process, monitor progress, and safely finalize the data movement.

For homogeneous migrations to AlloyDB for PostgreSQL, Database Migration Service exclusively supports continuous migrations. Continuous migrations perform an initial full dump of your source database, followed by continuous replication of ongoing data changes (CDC) until you promote the migration job.

## Destination clusters created by Database Migration Service

When you want to migrate to a new AlloyDB for PostgreSQL cluster, Database Migration Service can create the cluster and its primary instance for you as part of the migration job creation flow.

If you want Database Migration Service to create the destination database cluster for you, follow the guidance in [ Create a migration job to a new destination cluster](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job).

## Destination clusters created outside Database Migration Service

You can create your destination AlloyDB for PostgreSQL cluster outside of Database Migration Service before you configure the migration job. This approach is especially useful when you plan to use Terraform or other infrastructure as code tools to manage your infrastructure.

There are certain limitations that you should consider when you want to migrate to a destination cluster created outside of Database Migration Service. For more information, see [ Known limitations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations#existing-instance-limitations).

If you want to migrate to a destination database created outside of Database Migration Service, follow the guidance in [ Create a migration job to an existing destination cluster](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-existing-instance).

## What's next

To get a complete, step-by-step migration walkthrough for homogeneous AlloyDB for PostgreSQL migrations, see [ Get started with AlloyDB for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/get-started-with-alloydb-migrations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
