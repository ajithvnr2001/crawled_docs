---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/dag-migration-overview/
title: About Distributed Availability Group (DAG) migrations \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:38:57.283375+00:00
---

# About Distributed Availability Group (DAG) migrations  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/dag-migration-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  About Distributed Availability Group (DAG) migrations Stay organized with collections  Save and categorize content based on your preferences. 

In addition to the standard Cloud Storage backup and restore migration flow, Database Migration Service supports migrating self-managed SQL Server databases to Cloud SQL for SQL Server by using [ SQL Server Distributed Availability Groups (DAG)](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/distributed-availability-groups).

Instead of exporting and uploading backup and transaction log files to a Cloud Storage bucket, Database Migration Service configures a Distributed Availability Group between your source Availability Group and a managed secondary Availability Group on your destination Cloud SQL for SQL Server instance. This configuration streams both the initial full load and ongoing database changes directly over a private network connection.

This page covers the following topics:

  * When to use DAG migrations
  * How DAG migrations work
  * Supported source and destination databases
  * Known limitations for DAG migrations



## When to use DAG migrations

The following table compares standard backup and restore migrations with Distributed Availability Group (DAG) migrations to help you choose the best approach for your workload:

Feature or requirement | Standard backup and restore migrations ([Standard migration guide](https://docs.cloud.google.com/database-migration/docs/sqlserver/guide)) | Distributed Availability Group (DAG) migrations ([DAG migration guide](https://docs.cloud.google.com/database-migration/docs/sqlserver/dag-migration-guide))  
---|---|---  
**Supported sources** | Self-managed SQL Server, Amazon RDS, and Cloud SQL for SQL Server. | Self-managed SQL Server (Enterprise Edition) with Always On availability groups.  
**Data movement mechanism** | Full backup (`.bak`), optional differential backup (`.diff`), and transaction log (`.trn`) files staged in Cloud Storage. | Direct network streaming over a SQL Server Database Mirroring (`DBM`) endpoint (no backup files or Cloud Storage buckets required).  
**Network connectivity** | No connectivity required between source and destination. | Bidirectional private IP connectivity required on the SQL Server database port (default `1433`) and Database Mirroring port (default `5022`).  
**Destination database access during migration** | Databases remain in `RESTORING` mode (inaccessible to queries) until promotion. | Databases are accessible in **read-only mode** during the continuous replication (`CDC`) phase.  
**Post-promotion failback** | Not supported (one-way promotion). | Built-in reverse replication (`FAILBACK` phase) from Cloud SQL for SQL Server back to the source SQL Server instance after promotion, with support for zero-data-loss failback switchover.  
  
## How DAG migrations work

During a DAG migration, Database Migration Service orchestrates data replication between your source Availability Group and a managed secondary Availability Group on your destination Cloud SQL for SQL Server instance.

### Network communication channels

Database Migration Service uses two private network communication channels between your source SQL Server instance and destination Cloud SQL for SQL Server instance:

  1. **SQL Server Linked Server (database port, default`1433`):** Database Migration Service uses a Linked Server configured on the destination Cloud SQL for SQL Server instance to execute administrative and orchestration queries on the source SQL Server instance.
  2. **Database Mirroring (`DBM`) endpoint (default `5022`):** The source Availability Group and the destination Cloud SQL for SQL Server Availability Group exchange certificate-authenticated initial full load data and ongoing database changes directly over the `DBM` port.



### Migration lifecycle phases

A DAG migration job progresses through four lifecycle phases:

  1. **Initial full load (`FULL_DUMP`):** When you start the migration job, Database Migration Service configures the Distributed Availability Group to stream the initial full copy of all databases in the source Availability Group over the network to the destination Cloud SQL for SQL Server instance.
  2. **Continuous replication (`CDC`):** As each database finishes its initial full load, it transitions to the `CDC` phase. Ongoing changes made to the source databases replicate continuously over the `DBM` endpoint, and you can connect to the destination Cloud SQL for SQL Server instance to run read-only verification queries against the replicating databases.
  3. **Promotion and reverse replication (`FAILBACK`):** When you promote the migration job (`promote` without the `--failback` flag), Database Migration Service synchronizes both Availability Groups, flips their roles so that the destination Cloud SQL for SQL Server instance becomes the read/write **Primary** and your original source SQL Server instance becomes the **Secondary** , and transitions the migration job phase to `FAILBACK` (`PHASE_FAILBACK` in Google Cloud CLI and API responses). While in the `FAILBACK` phase, the migration job stays in the `Running` state and replicates new writes from Cloud SQL for SQL Server back to your source SQL Server instance.
  4. **Failback switchover, stopping, or completion (`Stop` and `Delete`):**
     * If you need to revert your cutover during the `FAILBACK` phase, you can run the `promote` command with the `--failback` flag (`failback = true` in the API) to perform a zero-data-loss failback switchover that restores your original source SQL Server instance as the Primary, demotes Cloud SQL for SQL Server back to the Secondary, and returns the migration job to the `CDC` phase.
     * You can run `stop` to halt data replication for a defined, short period (updates continue to accumulate in the transaction logs while replication is halted). From a `Stopped` state, you can either run `resume` to resume data replication, or run `delete` to complete the migration and perform the necessary cleanup.
     * Once you confirm that your cutover to Cloud SQL for SQL Server is permanent, you **delete** (`delete`) the migration job (either directly or from the `Stopped` state). Deleting the migration job completes the migration, drops the Distributed Availability Group and certificates on both instances, and lets you enable Cloud SQL for SQL Server features that are blocked during the migration, such as Point-in-time recovery (PITR) and read replicas.



## Supported source and destination databases

DAG migrations support the following source and destination database editions and versions:

  * **Source databases:** Self-managed SQL Server **Enterprise Edition** (versions 2017, 2019, 2022, and 2025) with the [Always On availability groups](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/enable-and-disable-always-on-availability-groups-sql-server) feature enabled (on Windows or [Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-availability-group-configure-ha)).
  * **Destination databases:** Cloud SQL for SQL Server **Enterprise Edition** (versions 2017, 2019, 2022, and 2025).



## Known limitations for DAG migrations

Consider the following limitations before you configure a DAG migration:

  * Creating DAG connection profiles and creating, verifying, starting, promoting, or deleting DAG migration jobs is supported only through Google Cloud CLI or the Database Migration Service API. You can monitor DAG migration job progress, per-database status, and metrics in the Google Cloud console.
  * Both the source SQL Server instance and the destination Cloud SQL for SQL Server instance must run **Enterprise Edition**. Amazon RDS and Cloud SQL for SQL Server sources aren't supported for DAG migrations.
  * Each DAG migration job migrates all databases contained in a single source Availability Group (up to the limit of 100 databases per Distributed Availability Group). System databases (`master`, `model`, `msdb`, `tempdb`) and the Database Migration Service helper database (`gcp_dms_db`) aren't migrated.
  * All databases in the source Availability Group must store their data files (`.mdf` and `.ndf`) in the default SQL Server data directory.
  * Database ownership requirements: 
    * Source databases can't be owned by the `sa` login. Before starting the migration job, change the database owner from `sa` to another SQL login or Windows user.
    * If a source database is owned by a Windows Active Directory user, you must either change the source database owner to a SQL login before migrating, or [integrate your destination Cloud SQL for SQL Server instance with Active Directory](https://docs.cloud.google.com/sql/docs/sqlserver/ad) so that Database Migration Service can automatically create the corresponding Windows login on the destination instance when the migration job starts.
    * For SQL-authenticated database owners, Database Migration Service automatically creates a corresponding login on the destination Cloud SQL for SQL Server instance prefixed with `gcp_dms_`, a 6-character identifier, and the source owner name (for example, `gcp_dms_a1b2c3_myowner`) to own the migrated database.
  * Public IP connectivity isn't supported. You must configure private IP connectivity between the source SQL Server instance and the destination Cloud SQL for SQL Server instance using Private Services Access or Private Service Connect.
  * Destination Cloud SQL for SQL Server restrictions while the DAG migration job exists: From the moment you start a DAG migration job until you **delete** the migration job (including while the job is in the post-promotion `FAILBACK` phase): 
    * [Point-in-time recovery (PITR)](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/pitr) must be disabled on the destination Cloud SQL for SQL Server instance.
    * Read replicas and read pools aren't supported on the destination Cloud SQL for SQL Server instance.
    * Near-zero downtime planned maintenance isn't supported on the destination Cloud SQL for SQL Server instance.
    * Do not manually modify the `cloud sql enable dag support` database flag on the destination Cloud SQL for SQL Server instance; Database Migration Service enables this flag automatically when the migration job starts, and you can remove it after you delete the migration job.
  * Adding or removing databases during migration: 
    * You can dynamically add or remove databases in your source Availability Group while the migration job is in the `CDC` phase. Database Migration Service automatically detects newly added databases, validates them, and performs their initial full load to the destination Cloud SQL for SQL Server instance.
    * Removing a database from the source Availability Group stops replication for that database, removes it from the migration job's tracked objects, and leaves the database in `RESTORING` state on the destination Cloud SQL for SQL Server instance (it isn't recovered when the job is promoted).
    * Adding new databases directly on the destination Cloud SQL for SQL Server instance during the post-promotion `FAILBACK` phase isn't supported (the destination Availability Group isn't updated with new databases created on Cloud SQL).
  * Caveats for stopping, resuming, and restarting DAG migration jobs: 
    * Stopping (`stop`) a DAG migration job halts data replication, causing updates to accumulate in the transaction logs while replication is halted. Only stop a DAG migration job for a defined, short period so that transaction log disks don't fill up. From the `Stopped` state, you can either run `resume` to resume data replication, or run `delete` to complete the migration and perform the necessary cleanup.
    * Restarting (`restart`) a failed or stopped DAG migration job deletes the migrated databases on the destination Cloud SQL for SQL Server instance and re-runs the initial full load (`FULL_DUMP`) over the network.



## What's next

  * [Migrate from self-managed SQL Server using Distributed Availability Groups](https://docs.cloud.google.com/database-migration/docs/sqlserver/dag-migration-guide)
  * [Migrate your SQL Server databases using Cloud Storage backup files](https://docs.cloud.google.com/database-migration/docs/sqlserver/guide)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
