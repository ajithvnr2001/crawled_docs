---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/networking-methods/
title: Network connectivity for Cloud SQL for SQL Server migrations \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T10:17:29.205616+00:00
---

# Network connectivity for Cloud SQL for SQL Server migrations  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/networking-methods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Network connectivity for Cloud SQL for SQL Server migrations Stay organized with collections  Save and categorize content based on your preferences. 

The network connectivity configuration required for homogeneous SQL Server migrations in Database Migration Service depends on the type of migration you perform:

  * Network connectivity for backup and restore migrations
  * Network connectivity for Distributed Availability Group (DAG) migrations



## Network connectivity for backup and restore migrations

Database Migration Service moves your SQL Server backup and transaction log files from the dedicated Cloud Storage bucket to your destination Cloud SQL for SQL Server instance.

All the entities that participate in data movement are co-located in Google Cloud, so Database Migration Service automatically handles all networking setup. No additional configuration is required.

## Network connectivity for Distributed Availability Group (DAG) migrations

If you migrate from a self-managed SQL Server instance by using a Distributed Availability Group (DAG) instead of Cloud Storage backup files, Database Migration Service streams data directly over the network between your source SQL Server instance and your destination Cloud SQL for SQL Server instance.

For DAG migrations, you must configure bidirectional private IP connectivity (using Private Services Access or Private Service Connect) on both the SQL Server database port (default `1433`) and the Database Mirroring (`DBM`) endpoint port (default `5022`). For setup instructions, see [Migrate from self-managed SQL Server using Distributed Availability Groups](https://docs.cloud.google.com/database-migration/docs/sqlserver/dag-migration-guide).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
