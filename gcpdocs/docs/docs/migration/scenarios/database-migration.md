---
url: https://docs.cloud.google.com/docs/migration/scenarios/database-migration/
title: Database migration \u00a0|\u00a0 Migration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:39:44.526919+00:00
---

# Database migration  |  Migration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/migration/scenarios/database-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Guides ](https://docs.cloud.google.com/docs/migration/overview/migrate-modernize-overview)



Send feedback 

#  Database migration Stay organized with collections  Save and categorize content based on your preferences. 

This page provides architectural guidance and migration strategies for migrating relational and non-relational databases to Google Cloud.

If you are a database administrator, cloud architect, or data engineer, use the information on this page to evaluate database migration patterns, choose the right tools, ensure high data fidelity, minimize transaction replication lag, and control downtime during cutover.

Before you read this page, you should have completed an initial source assessment and have an understanding of your database schemas, sizing, and application network dependencies.

## Database migration options

When planning database migrations, use the following table to choose a destination service and tool based on your source database engine:

Source database | Destination platform | Recommended tool | Migration pattern  
---|---|---|---  
**MySQL, PostgreSQL, or SQL Server** |  [Cloud SQL](https://docs.cloud.google.com/sql/docs) or [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs) |  [Database Migration Service](https://docs.cloud.google.com/database-migration/docs) | Continuous CDC replication  
**Oracle** |  [AlloyDB](https://docs.cloud.google.com/alloydb/docs) or [Bare Metal Solution](https://docs.cloud.google.com/bare-metal/docs) |  [Google Cloud Modernization Hub](https://docs.cloud.google.com/modernize/hub/overview#database-workloads), [Database Migration Service Schema Conversion](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/scenario-overview) | Homogeneous or heterogeneous migration  
**Cassandra, MongoDB, or HBase** |  [Bigtable](https://docs.cloud.google.com/bigtable/docs), [Spanner](https://docs.cloud.google.com/spanner/docs), or [Firestore](https://docs.cloud.google.com/firestore/native/docs) |  [Dataflow](https://docs.cloud.google.com/dataflow/docs) or open-source connectors  | Batch or stream ingestion  
  
## Migrate databases by using Database Migration Service

[Database Migration Service](https://docs.cloud.google.com/database-migration/docs) provides serverless migration jobs to move relational databases to Google Cloud.

### Key capabilities of Database Migration Service

Database Migration Service provides the following capabilities:

  * **Serverless architecture** : you don't need to provision or manage dedicated replication VMs or migration infrastructure.
  * **Continuous change data capture (CDC)** : replicates transactions by using source binary logs (`binlog` for MySQL, `wal2json` for PostgreSQL, and CDC for SQL Server) to keep target databases synchronized with minimal lag.
  * **Flexible private connectivity** : connects securely to source databases through [VPC Network Peering](https://docs.cloud.google.com/database-migration/docs/postgres/configure-connectivity-vpc-peering), [reverse SSH tunnels](https://docs.cloud.google.com/database-migration/docs/postgres/configure-connectivity-reverse-ssh-tunnel), [Cloud VPN](https://docs.cloud.google.com/database-migration/docs/postgres/configure-connectivity-vpns), or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).



For information about the end-to-end migration workflow, see [Database Migration Service overview](https://docs.cloud.google.com/database-migration/docs/overview).

## What's next

  * [Unstructured data and storage migration](https://docs.cloud.google.com/docs/migration/scenarios/data-storage-migration)
  * [Containerized application migration](https://docs.cloud.google.com/docs/migration/scenarios/container-migration)
  * [Multi-cloud workload migration](https://docs.cloud.google.com/docs/migration/scenarios/multi-cloud-migration)
  * [Database workloads in Modernization Hub](https://docs.cloud.google.com/modernize/hub/overview#database-workloads)
  * [Migrate MySQL to Cloud SQL](https://docs.cloud.google.com/database-migration/docs/mysql/get-started-with-mysql-migrations)
  * [Migrate PostgreSQL to Cloud SQL or AlloyDB](https://docs.cloud.google.com/database-migration/docs/postgres/quickstart)
  * [Migrate Oracle to PostgreSQL or AlloyDB](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/scenario-overview)
  * [Migrate Cassandra to Bigtable](https://docs.cloud.google.com/bigtable/docs/migrate-from-cassandra)
  * [Migrate Cassandra to Spanner](https://docs.cloud.google.com/spanner/docs/non-relational/migrate-from-cassandra-to-spanner)
  * [Database migration principles: Part 1](https://docs.cloud.google.com/architecture/database-migration-concepts-principles-part-1)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
