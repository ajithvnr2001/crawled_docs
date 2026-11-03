---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/get-started-with-alloydb-migrations/
title: Get started with PostgreSQL to AlloyDB for PostgreSQL migrations \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T05:44:30.624353+00:00
---

# Get started with PostgreSQL to AlloyDB for PostgreSQL migrations  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/get-started-with-alloydb-migrations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview)



Send feedback 

#  Get started with PostgreSQL to AlloyDB for PostgreSQL migrations Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service provides flexible continuous migration flows for your homogeneous PostgreSQL to AlloyDB for PostgreSQL migrations. Depending on your database architecture, networking configuration, downtime tolerance, and resource management practices, you can choose from different workflows designed to meet your migration goals. Detailed networking and configuration prerequisites are described in each migration guide.

The following table provides an overview of each migration workflow:

Migration workflow | Best suited for | Description  
---|---|---  
[Migrate to a new destination cluster](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/guide-to-new-instance) | Standard migrations where you want Database Migration Service to create a clean target cluster tailored for the migration workload. | Database Migration Service automatically creates a new destination AlloyDB for PostgreSQL cluster and primary instance using configuration options that you select, and continuously replicates source schemas and data.  
[Migrate to an existing destination cluster](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/guide-to-existing-instance) | Scenarios where destination cluster parameters must be pre-configured, custom private IP or VPC configurations are required, or clusters are provisioned through Terraform or infrastructure-as-code (IaC). | Migrate data into an AlloyDB for PostgreSQL cluster that you have already created and configured. The destination cluster must be in a `RUNNABLE` state and must contain only default system databases (`postgres`, `template0`, `template1`) with no user tables.  
[Use quick-start migrations (Preview)](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/quick-start-migrations-guide) | Rapid setup and streamlined migrations with `pgnative` replication and Private Service Connect network attachments to simplify network configuration.  | Perform an automated continuous migration using predefined configurations and private connectivity to migrate your PostgreSQL databases to AlloyDB for PostgreSQL. Learn more in [About quick-start migrations](https://docs.cloud.google.com/database-migration/docs/about-quick-start-migrations).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-02 UTC."],[],[]] 
