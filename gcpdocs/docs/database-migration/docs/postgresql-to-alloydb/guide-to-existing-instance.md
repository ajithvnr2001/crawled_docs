---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/guide-to-existing-instance/
title: Migrate to an existing destination cluster \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T12:42:57.918446+00:00
---

# Migrate to an existing destination cluster  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/guide-to-existing-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview)



Send feedback 

#  Migrate to an existing destination cluster Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to migrate your databases to a pre-existing AlloyDB for PostgreSQL cluster created directly in AlloyDB for PostgreSQL.

This path is useful for scenarios where your destination cluster is managed by a different team, or if you need to create the cluster outside Database Migration Service to configure specific custom flags, pre-allocated IP ranges, or complex VPC network topologies. If your migration has different requirements, consider following a different migration flow. For more information, see [ Get started with PostgreSQL to AlloyDB for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/get-started-with-alloydb-migrations).

At a high level, the continuous migration follows these steps:

  1. Configure the source database to allow Database Migration Service to replicate your data.
  2. Set up network connectivity between your source database and Google Cloud.
  3. Prepare and configure your existing destination AlloyDB for PostgreSQL cluster.
  4. Create the source connection profile and the continuous migration job.
  5. Start and monitor the continuous migration job.
  6. Promote the migration job and move your application to use the new databases.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * AlloyDB for PostgreSQL (See [ AlloyDB for PostgreSQL pricing](https://docs.cloud.google.com/alloydb/pricing).)
  * If used for storing Customer-managed Encryption Keys (CMEK): Cloud Storage (See [ Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing).) 



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

## Before you begin

  1. Verify if this migration path can fully support your scenario. See the following pages: 
     * [ Supported sources and destinations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview) on the _Scenario overview_ page lists all supported source and destination versions. 
     * [ Known limitations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations) describes operational boundaries, supported data types, and performance limits. Database Migration Service for AlloyDB for PostgreSQL supports continuous migrations. 
  2. Consider in which region you want to create the destination cluster. Database Migration Service is a fully regional product, meaning all entities related to your migration (source connection profiles, migration jobs, and destination clusters) must reside in a single Google Cloud region. 
  3. In the Google Cloud console, on the project selector page, select or [ create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. Enable the Database Migration Service, AlloyDB for PostgreSQL, and Compute Engine APIs. 

[ Enable the APIs](https://console.cloud.google.com/flows/enableapi?apiid=datamigration.googleapis.com,alloydb.googleapis.com,compute.googleapis.com)




### Required roles

To get the permissions that you need to perform homogeneous PostgreSQL migrations to AlloyDB for PostgreSQL with Database Migration Service, ask your administrator to grant you the required IAM roles on your project:

  * [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
  * [ AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`) 



For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the Identity and Access Management documentation. 

These predefined roles contain the permissions required to perform homogeneous PostgreSQL migrations with Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to perform homogeneous PostgreSQL migrations to an existing AlloyDB for PostgreSQL cluster with Database Migration Service: 

  * `datamigration.*`
  * `alloydb.clusters.get`
  * `alloydb.clusters.list`
  * `alloydb.clusters.update`
  * `alloydb.instances.get`
  * `alloydb.instances.list`
  * `alloydb.instances.update`
  * `alloydb.operations.get`
  * `alloydb.users.list`
  * `alloydb.users.get`
  * `alloydb.users.create`
  * `alloydb.users.update`



You might also be able to get these permissions with [ custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [ predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). 

## Prepare your source database

To prepare your source database for migration, follow these steps:

  1. [ Choose and configure your source network connectivity method](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods). 
  2. Configure your source database instance. At a high level, this includes the following steps: 
     1. Install the `pglogical` PostgreSQL extension (version 2.2.1 or later) on the source database and on all databases to be migrated.
     2. Configure PostgreSQL parameters: set `wal_level = logical`, and ensure adequate values for `max_replication_slots`, `max_wal_senders`, and `max_worker_processes`.
     3. Grant replication privileges to your migration user, and configure `pg_hba.conf` to permit incoming connections from the destination AlloyDB for PostgreSQL cluster. 

For detailed instructions, see [ Configure your source database](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database). 

  3. [ Create the source connection profile](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-connection-profiles). 



## Prepare and configure your destination cluster

When migrating to an existing AlloyDB for PostgreSQL cluster (such as a cluster pre-provisioned by another team or managed with Terraform), ensure that the cluster satisfies all Database Migration Service prerequisites before creating your migration job:

  1. **Cluster readiness and data state** : 
     * The destination cluster must be in the `RUNNABLE` state and must have an active primary instance.
     * The cluster must reside in the same Google Cloud region as your migration job and connection profiles.
     * The cluster can only be associated with one active migration job at a time.
     * The destination cluster must contain only the default system databases (`postgres`, `template0`, `template1`) with no user tables. 
  2. **Database flag configuration** : Enable the `alloydb.enable_pglogical` flag on your destination AlloyDB for PostgreSQL cluster. This flag is required for logical replication decoding and ingestion. For instructions on updating flags, see [ Configure database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags) in the AlloyDB for PostgreSQL documentation. 
  3. **Database user credentials and permissions** : Ensure that the administrative user account `postgres` (or a dedicated migration account granted the `alloydbsuperuser` role) exists on your destination cluster. Database Migration Service connects to your destination with administrative rights to manage replication subscribers and synchronize schemas. 
  4. **Network connectivity requirements** : Verify that your destination cluster's networking is properly configured to communicate with your source database according to your chosen connectivity method: 
     * **Private Service Connect** : If your destination cluster is Private Service Connect-enabled, verify that the cluster is configured with the appropriate Private Service Connect network attachments and routing to reach your source network. For more information, see [ Configure Private Service Connect](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect) in the AlloyDB for PostgreSQL documentation. 
     * **Virtual Private Cloud peering (Private Services Access / Private IP)** : The destination cluster must have private services access configured on the Virtual Private Cloud network that peers with or routes to your source database (such as with Cloud VPN or Cloud Interconnect). For more information, see [ Configure private services access](https://docs.cloud.google.com/alloydb/docs/configure-connectivity) in the AlloyDB for PostgreSQL documentation. 
     * **Public IP allowlist** : If your source database is accessible over the public internet, ensure that your source firewall allows incoming connections from your destination AlloyDB for PostgreSQL primary instance's outgoing IP address. 
     * **Reverse SSH tunnel or TCP proxy VM** : If your source database resides outside Google Cloud without direct private peering, ensure that your intermediate Compute Engine VM (bastion host or TCP proxy) is deployed in a subnet reachable by the destination cluster's Virtual Private Cloud network. For details, see [ Networking methods](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods). 
  5. **Primary instance demotion and write lock notice** : 
     * Database Migration Service demotes the existing destination primary instance to function as an external replication subscriber during the migration process. You must confirm this demotion when configuring the migration job in the Google Cloud console by entering the destination cluster ID. 
     * Demoting the primary instance doesn't place the databases into strict read-only mode, but you must avoid write operations on tables or databases participating in the migration to prevent replication conflicts and data drift. For more information, see [ Limitations for migrations to existing destination clusters](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations#existing-instance-limitations). 



## Create and run the migration job

To configure and run your continuous migration to an existing destination cluster, perform the following steps:

  1. Optional: If you want to manage your own certificates or encryption keys for the migration job, [ prepare the necessary encryption keys](https://docs.cloud.google.com/alloydb/docs/use-cmek). 
  2. [ Create and run the migration job for an existing destination cluster](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-existing-instance). 

You can monitor the migration progress, as well as your destination cluster health with Database Migration Service observability features. See [ Migration job metrics](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-job-metrics). 




## Finalize the migration

When you decide to switch your application traffic to the new AlloyDB for PostgreSQL cluster, finalize the migration by following these steps:

  1. Stop all write operations on your source database. You can configure the source database to read-only mode to maintain availability for queries while preventing new modifications.
  2. [ Promote the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/promote-migration). Promoting the migration job synchronizes all remaining CDC transactions, terminates replication from the source, and promotes the AlloyDB for PostgreSQL primary instance to a standalone, fully operational primary cluster. 
  3. Optional: [ Verify migration data](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/verify-migration) for completeness and row integrity. 



## What's next

Learn more about AlloyDB for PostgreSQL features and management capabilities. See [ AlloyDB for PostgreSQL overview](https://docs.cloud.google.com/alloydb/docs/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
