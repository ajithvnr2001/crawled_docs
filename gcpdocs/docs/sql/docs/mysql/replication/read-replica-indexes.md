---
url: https://docs.cloud.google.com/sql/docs/mysql/replication/read-replica-indexes/
title: Read replica indexes overview \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T02:29:37.039264+00:00
---

# Read replica indexes overview  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/replication/read-replica-indexes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Read replica indexes overview Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This document describes concepts and mechanisms for managing [secondary indexes](https://dev.mysql.com/doc/refman/8.4/en/innodb-index-types.html) on Cloud SQL read replicas across both [Cloud SQL Enterprise edition and Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/mysql/editions-intro). In MySQL, you can create two main types of indexes on a table:

  * **Clustered index** : the main index on a MySQL table that physically orders the rows on disk. When you define a primary key on a table, MySQL uses it as the clustered index. A table can have only one clustered index.
  * **Secondary index** : an additional index on a MySQL table that optimizes query performance.

While a replica is normally read-only, you can create secondary indexes on tables for reporting purposes. Cloud SQL supports two methods for creating replica secondary indexes:

    * **Managed replica indexes (Recommended)** : Cloud SQL stores index definitions on the primary instance and rebuilds secondary indexes automatically after replica crashes or re-creation. Google recommends managed indexes over self-managed indexes to prevent index loss and avoid manual index restoration.
    * **Self-managed replica indexes** : let you add and drop secondary indexes directly on a replica, but these indexes don't persist after the replica crashes or replica re-creation. If you're using self-managed indexes, then you can [migrate to using managed replica indexes](https://docs.cloud.google.com/sql/docs/mysql/replication/create-manage-read-replica-indexes#migrate-from-self-managed-to-managed).



## Compare replica index methods

The following table compares managed replica indexes and self-managed replica indexes in Cloud SQL:

Feature | Managed replica indexes | Self-managed replica indexes  
---|---|---  
Persistence across replica re-creation | Automatically rebuilt | Dropped (manual rebuild required)  
Configuration model | Centralized metadata on the primary instance | Direct DDL on the target read replica  
Execution mechanism | Periodic background process  
(approximately every five minutes) | Immediate execution  
Replication lag guardrail | Automatically pauses index creation if replication lag exceeds 20 minutes | None (user-managed)  
Supported editions | Cloud SQL Enterprise edition and Cloud SQL Enterprise Plus edition | Cloud SQL Enterprise edition and Cloud SQL Enterprise Plus edition  
Supported database versions | Cloud SQL for MySQL  
(maintenance version `R20260726.00_05` or later) | Cloud SQL for MySQL  
(all supported versions)  
External server replica support | Not supported | Supported  
  
## Managed replica indexes

To prevent index loss after replica re-creation, Cloud SQL supports managed replica indexes. Google recommends this method of index creation and retention. Cloud SQL enables this method by default.

Managed replica indexes require Cloud SQL maintenance version `R20260726.00_05` or later.

The following sections describe how Cloud SQL maintains replica indexes, their benefits, and how they behave during lifecycle events.

### How Cloud SQL maintains managed replica indexes

With this method, you define replica secondary indexes, group them, and designate which replicas can maintain those index groups. Cloud SQL runs a background process on the replica to create and drop the required indexes automatically and maintain the indexes over time. When Cloud SQL creates a managed replica index, it prepends a `[SIC_X_Y]` tag to the index comment, where X and Y are integers. This tag is used solely for internal management and has no functionality.

Cloud SQL performs managed replica index maintenance, such as creating and dropping indexes, in batches. After the Cloud SQL index maintenance process picks up a group of `CREATE` or `DROP` actions, it creates a `PENDING` status entry for each secondary index. It then serially executes each data definition language (DDL) statement. A failure on one index doesn't block the execution of subsequent indexes in the queue. Cloud SQL then picks up the next batch after approximately five minutes.

### Benefits and use cases

Managed replica indexes provide the following benefits:

  * **Automated index retention** : when Cloud SQL re-creates a read replica (such as after an instance crash), Cloud SQL automatically rebuilds the secondary indexes mapped to that replica. You don't need to run manual stored procedures or maintain external schema tracking scripts to restore missing indexes.
  * **Consistent query performance** : by automatically rebuilding secondary indexes after replica recovery, Cloud SQL maintains query throughput and prevents query latency spikes and high CPU utilization caused by unindexed queries.
  * **Group-based configuration** : you define secondary indexes once on the primary instance and organize them into named replica groups. You can then assign an index group containing hundreds of indexes to a read replica by setting a single database flag (`cloudsql_index_recreate_replica_group`). This eliminates the need to execute individual stored procedures across multiple replicas.
  * **Selective index assignment by replica role** : you can assign index groups specifically to reporting and analytics read replicas to accelerate read queries, while keeping disaster recovery (DR) read replicas unindexed and identical to the primary instance schema. This prevents write transaction overhead and replication lag on DR instances.
  * **Primary instance performance isolation** : secondary indexes on read replicas optimize read and reporting queries without consuming storage or adding write transaction latency to the primary instance.
  * **Built-in observability** : dedicated stored procedures let you monitor index creation progress, execution duration, and error logs on the read replica.
  * **Non-disruptive migration and coexistence** : managed replica indexes safely coexist with existing self-managed replica indexes on the same instance and table. You can adopt managed replica indexes incrementally without downtime, or interrupting active read query workloads.



### Replica promotion

Cloud SQL maintains managed replica indexes only on read replica instances. If you promote a read replica to a primary instance, then Cloud SQL automatically drops any secondary indexes created as managed replica indexes. A delay of approximately five minutes can occur before Cloud SQL executes the drop.

Although Cloud SQL drops the secondary indexes and removes database flags from the promoted instance, the primary instance retains the secondary index definitions and group mappings.

### Disaster recovery (DR) switchover

During a DR switchover, when you promote the DR replica to the new primary instance, Cloud SQL automatically drops all secondary indexes created on the DR replica. Cloud SQL doesn't automatically create these secondary indexes on the old primary instance when it becomes a replica.

To create secondary indexes on the old primary instance after switchover, set the `cloudsql_index_recreate_replica_group` database flag on that instance.

### Replication lag

Cloud SQL pauses secondary index creation operations if the replication lag exceeds 20 minutes. If managed replica index creation is already in progress when the lag exceeds 20 minutes, Cloud SQL lets the operation complete. Replication lag doesn't pause managed replica index drop operations.

### Limitations

When you use managed replica indexes, the following limitations apply:

  * **You can't create managed replica indexes on external server replicas** : Cloud SQL doesn't support creating managed replica indexes for external server replicas.
  * **Maximum of 1,000 indexes per replica group** : you can assign a maximum of 1,000 secondary indexes to a replica group.
  * **Updating or altering index metadata isn't supported** : you can't update or alter existing index metadata. To modify an index, you must delete the existing index definition and create a new one.



## Self-managed replica indexes

Self-managed replica indexes are secondary indexes that you create and drop directly on individual Cloud SQL read replicas. Like managed replica indexes, they optimize read query performance—such as for reporting and analytics workloads—without consuming storage or affecting write latency on the primary instance.

### Self-managed index management

You manage self-managed replica indexes directly on the read replica by using the following stored procedures in the `mysql` schema:

  * `mysql.addSecondaryIdxOnReplica`: adds a secondary index on a specified table on the read replica. This stored procedure is a wrapper for the `CREATE INDEX` DDL statement.
  * `mysql.dropSecondaryIdxOnReplica`: drops a previously created secondary index from the read replica. This stored procedure is a wrapper for the `DROP INDEX` DDL statement.



Running these stored procedures requires the `cloudsqlsuperuser` role.

When you create a self-managed index, Cloud SQL records basic metadata in the `mysql.cloudsql_replica_index` table on the replica, including the database name, table name, and index name. Unlike managed replica indexes, self-managed indexes aren't registered on the primary instance and aren't maintained by the Cloud SQL background replication process.

For syntax details and usage examples, see [Self-managed replica indexes](https://docs.cloud.google.com/sql/docs/mysql/replication/create-manage-read-replica-indexes#self-managed-replica-indexes).

### Benefits and use cases

Self-managed replica indexes provide the following benefits for specific workflows:

  * **Primary instance performance isolation** : secondary indexes on read replicas optimize read and reporting queries without consuming storage or adding write transaction latency to the primary instance.
  * **Immediate execution** : stored procedure calls execute immediately as DDL statements on the replica, without waiting for the periodic background maintenance cycle (approximately every five minutes) required by managed replica indexes.
  * **Isolated testing and experimentation** : you can test query performance and validate index optimizations on an individual read replica before creating managed replica indexes across a replica group.



### Limitations

Self-managed replica indexes have significant operational limitations:

  * **Lack of persistence across replica re-creation** : if Cloud SQL re-creates a read replica (such as during instance recovery, maintenance, or hardware failure), all self-managed secondary indexes on that replica are dropped and aren't restored automatically.
  * **Manual restoration overhead** : Cloud SQL can't reconstruct and rebuild the indexes. You must manually re-create the indexes by running `mysql.addSecondaryIdxOnReplica` again.
  * **Query performance degradation** : read queries might experience performance degradation after replica re-creation until you manually rebuild the missing indexes.



Because managed replica indexes automatically persist and rebuild across replica re-creation events, Google recommends using managed replica indexes for production workloads. If you have existing self-managed indexes, then [migrate them to managed replica indexes](https://docs.cloud.google.com/sql/docs/mysql/replication/create-manage-read-replica-indexes#migrate-from-self-managed-to-managed).

## Coexistence of replica index types

Self-managed replica indexes (created using `mysql.addSecondaryIdxOnReplica`) and managed replica indexes can coexist on the same Cloud SQL read replica instance and on the same table. This lets you adopt managed replica indexes incrementally without disrupting existing database workloads.

When you use both index management methods, consider the following behaviors:

  * **Independent operation** : self-managed indexes that you create directly on the read replica continue to function alongside managed replica indexes.
  * **Periodic evaluation** : the Cloud SQL background maintenance process periodically (approximately every five minutes) evaluates index definitions mapped to the replica group that you assign to the replica.
  * **Name conflict handling** : if you register a managed replica index definition with the same name as an existing self-managed index on the read replica, the background process detects that an index with that name already exists. The process records a `FAILED` status in the `mysql.cloudsql_replica_idx_status` table. This error doesn't affect database traffic, create table locks, or affect the existing self-managed index.
  * **Automatic resolution upon re-creation** : when the read replica is re-created, Cloud SQL drops the existing self-managed index as part of the instance re-creation and automatically creates the managed replica index from the registered definition.



## What's next

  * Learn how to [create and manage read replica indexes](https://docs.cloud.google.com/sql/docs/mysql/replication/create-manage-read-replica-indexes).
  * Learn how to [manage read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas).
  * Learn how to [create read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica).
  * Learn about [replication in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/replication).
  * Learn about [replication lag](https://docs.cloud.google.com/sql/docs/mysql/replication/replication-lag).
  * Learn how to [configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags).
  * Learn about [stored procedures for Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/stored-procedures).
  * Learn about [advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/mysql/use-advanced-disaster-recovery).
  * Learn how to [connect using a MySQL client](https://docs.cloud.google.com/sql/docs/mysql/connect-admin-ip).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
