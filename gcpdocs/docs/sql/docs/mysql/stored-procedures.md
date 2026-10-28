---
url: https://docs.cloud.google.com/sql/docs/mysql/stored-procedures/
title: Cloud SQL stored procedures \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T02:29:36.832406+00:00
---

# Cloud SQL stored procedures  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/stored-procedures/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  Cloud SQL stored procedures Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/stored-procedures "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/stored-procedures "View this page for the SQL Server database engine")

This section describes stored procedures for Cloud SQL instances.

A stored procedure contains SQL code that you can reuse.

You cannot drop or alter system stored procedures.

To execute a stored procedure, you use the `CALL` command and replace the following variable:

  * procedure_name is the name of the stored procedure.


    
    
    CALL procedure_name(parameters);

For more information, see the [CALL statement](https://dev.mysql.com/doc/refman/8.0/en/call.html) reference page. 

To create a stored procedure, see [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/8.0/en/create-procedure.html). Cloud SQL doesn't support the `CREATE FUNCTION` statement. For more information, see [Unsupported MySQL features for Cloud SQL](https://docs.cloud.google.com/sql/docs/features#unsupported-statements). 

**Note:** You cannot run some stored procedures because they require a `sysadmin` role, which isn't available in Cloud SQL. 

## Managed replica indexes stored procedures

You can use the following stored procedures to create, manage, and drop managed replica indexes for your replicas. When your replicas are re-created, these indexes are restored automatically.

Each stored procedure call executes a `COMMIT` statement that finalizes the changes in your current session. As a result, data manipulation language (DML) statements executed using these stored procedures can't be rolled back within a transaction.

For more information, see [Managed replica indexes](https://docs.cloud.google.com/sql/docs/mysql/replication/read-replica-indexes#managed-replica-indexes).

### mysql.cloudsql_replica_idx_defn_create

**Syntax**
    
    
    mysql.cloudsql_replica_idx_defn_create(IDXNAME, CREATESTMT)

**Description**

Creates a definition for a secondary index. Run this stored procedure on the primary instance, which replicates the index definition to the replicas.

The stored procedure returns an `IDXID`, a unique integer identifier of the secondary index definition.

  * IDXNAME – Name for the index definition.
  * CREATESTMT – SQL statement to create the index. Must be a schema-prefixed (for example, `schema_name.table_name`) DDL statement.



### mysql.cloudsql_replica_idx_defn_drop

**Syntax**
    
    
    mysql.cloudsql_replica_idx_defn_drop(IDXID)

**Description**

Drops a secondary index definition. Run this stored procedure on the primary instance.

**Note:** You can't delete an index definition if it is part of a replica group. Remove the index definition from all replica groups using `mysql.cloudsql_replica_idx_group_drop` before deleting it. 

  * IDXID – Unique integer identifier of the index definition of the deleted index.



### mysql.cloudsql_replica_idx_group_add

**Syntax**
    
    
    mysql.cloudsql_replica_idx_group_add(IDXID, GRPNAME)

**Description**

Adds a secondary index definition to a replica group. Run this stored procedure on the primary instance.

  * IDXID – Unique integer ID of the index definition.
  * GRPNAME – Name of the replica group. GRPNAME is a custom name that you select. If that replica group doesn't exist, then Cloud SQL creates a new one.



### mysql.cloudsql_replica_idx_group_drop

**Syntax**
    
    
    mysql.cloudsql_replica_idx_group_drop(IDXID, GRPNAME)

**Description**

Drops a secondary index from a replica group mapping. Run this stored procedure on the primary instance.

  * IDXID – Unique integer ID of the index definition.
  * GRPNAME – Name of the replica group.



### mysql.cloudsql_replica_idx_show_status

**Syntax**
    
    
    mysql.cloudsql_replica_idx_show_status()

**Description**

Shows the status and progress of ongoing index creation or drop operations on a replica instance.

To view a detailed progress report, you must enable the MySQL Performance Schema on the instance. In addition, you must enable the stage instruments and consumers by running the following SQL commands:

  1. Enable the stage instruments:
         
         UPDATE performance_schema.setup_instruments
         SET ENABLED = 'YES'
         WHERE NAME LIKE 'stage/innodb/alter%';

  2. Enable the stage event consumers:
         
         UPDATE performance_schema.setup_consumers
         SET ENABLED = 'YES'
         WHERE NAME LIKE 'events_stages_%';




For more information, see the [ALTER TABLE Monitoring Example Using Performance Schema](https://dev.mysql.com/doc/refman/8.4/en/monitor-alter-table-performance-schema.html).

### mysql.cloudsql_replica_idx_show_errors

**Syntax**
    
    
    mysql.cloudsql_replica_idx_show_errors()

**Description**

Lists index re-creation attempts that failed in their last execution, showing error messages and retry counts on a replica instance. A failure on one index doesn't block the execution of subsequent indexes in the queue.

### mysql.cloudsql_replica_idx_show_all

**Syntax**
    
    
    mysql.cloudsql_replica_idx_show_all()

**Description**

Lists the status, retry counts, execution duration, and error messages for all replica secondary index re-creation records in the metadata status table. Run this stored procedure on a replica instance.

## Self-managed replica indexes stored procedures

The following stored procedures let you add and drop secondary indexes directly on a replica, but these indexes don't persist if the replica is re-created.

### mysql.addSecondaryIdxOnReplica

**Syntax**
    
    
    mysql.addSecondaryIdxOnReplica(IDXTYPE, IDXNAME, TABLENAME, IDXDEFINITION, IDXOPTION)

**Description**

Adds a secondary index on the database. This stored procedure is a wrapper for the [CREATE INDEX](https://dev.mysql.com/doc/refman/8.0/en/create-index.html) DDL statement.

  * IDXTYPE – Type of index to create. For example, pass `UNIQUE` to create a unique index.
  * IDXNAME – Name of the index.
  * TABLENAME – Name of the table in the format of `schema_name.table_name`.
  * IDXDEFINITION – Definition of the index. Don't include outer parentheses.
  * IDXOPTION – Any additional options to pass on index creation. For example, in MySQL 8.0, an option could pass `INVISIBLE` for an invisible index.



### mysql.dropSecondaryIdxOnReplica

**Syntax**
    
    
    mysql.dropSecondaryIdxOnReplica(IDXNAME, TABLENAME, IDXOPTION)

**Description**

Drops a secondary index on the database. This stored procedure is a wrapper for the [DROP INDEX](https://dev.mysql.com/doc/refman/8.0/en/drop-index.html) DDL statement.

  * IDXNAME – Name of the index.
  * TABLENAME – Name of the table in the format of `schema_name.table_name`.
  * IDXOPTION – Any additional options to pass when dropping an index. For example, an algorithm option such as `INPLACE`.



## External server replication stored procedures

You can use the following stored procedure during external server replication.

### mysql.skipReplicationError

**Syntax**
    
    
    mysql.skipReplicationError()

**Description**

Skips a replication error encountered during [external server replication](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server) and then resumes replication.

You can run this stored procedure only if you've encountered a replication error and the I/O and SQL threads are stopped.

This stored procedure does the following:

  1. Determines whether GTID-based or binary log position-based replication is used.

  2. If parallel replication is being used, then the stored procedure first calls [`START_SLAVE_UNTIL_SQL_AFTER_MTS_GAPS`](https://dev.mysql.com/doc/refman/8.0/en/start-slave.html) or [`START_REPLICA UNTIL_SQL_AFTER_MTS_GAPS`](https://dev.mysql.com/doc/refman/8.4/en/start-replica.html) to ensure that there are no gaps in applied transactions up to the failed transaction. The procedure then temporarily sets the replication configuration to single-threaded.

  3. For binary log position-based replication, the procedure sets [`SQL_SLAVE_SKIP_COUNTER`](https://dev.mysql.com/doc/refman/8.0/en/replication-options-replica.html#sysvar_sql_replica_skip_counter) or [`SQL_REPLICA_SKIP_COUNTER = 1`](https://dev.mysql.com/doc/refman/8.4/en/replication-options-replica.html#sysvar_sql_replica_skip_counter) to skip the current transaction.

  4. For GTID-based replication, the stored procedure determines the GTID of the current failed transaction based on information in the `gtid_executed` status variable. The procedure then inserts an empty transaction to backfill that GTID.

  5. If parallel replication was previously disabled, then the stored procedure re-enables parallel replication.

  6. The stored procedure resumes replication.




The table `mysql.skip_replication_error_history` logs all invocations of this stored procedure.

## What's next

  * Learn how to [add and drop indexes on Cloud SQL read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/read-replica-indexes).
  * Learn how to [create and manage read replica indexes](https://docs.cloud.google.com/sql/docs/mysql/replication/create-manage-read-replica-indexes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
