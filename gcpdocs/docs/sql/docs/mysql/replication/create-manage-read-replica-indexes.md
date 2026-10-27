---
url: https://docs.cloud.google.com/sql/docs/mysql/replication/create-manage-read-replica-indexes/
title: Create and manage read replica indexes \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T05:37:17.290688+00:00
---

# Create and manage read replica indexes  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/replication/create-manage-read-replica-indexes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Create and manage read replica indexes Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This document describes how to create, maintain, and monitor secondary indexes on Cloud SQL read replicas.

For conceptual information about how managed replica indexes work, see [Read replica indexes overview](https://docs.cloud.google.com/sql/docs/mysql/replication/read-replica-indexes).

## Managed replica indexes

The following table summarizes the workflow for creating, configuring, and monitoring managed replica indexes:

Step | Stored procedure or database flag | Where to perform the step  
---|---|---  
Create index definition | `CALL mysql.cloudsql_replica_idx_defn_create('INDEX_DEFINITION_NAME', 'CREATE_INDEX_STATEMENT');` This stored procedure returns a unique integer identifier for the index definition, `INDEX_DEFINITION_ID`. | Primary instance  
Map definition to group | `CALL mysql.cloudsql_replica_idx_group_add(INDEX_DEFINITION_ID, 'GROUP_NAME');` `GROUP_NAME` is a custom name that you can select. If that group doesn't exist, then Cloud SQL creates a new one. | Primary instance  
Assign group to replica | Database flag: `cloudsql_index_recreate_replica_group = GROUP_NAME` | Read replica instance  
Check status | `CALL mysql.cloudsql_replica_idx_show_status();` | Read replica instance  
Audit errors | `CALL mysql.cloudsql_replica_idx_show_errors();` | Read replica instance  
  
Each stored procedure call executes a `COMMIT` statement that finalizes the changes in your current session. As a result, data manipulation language (DML) statements executed using these stored procedures can't be rolled back within a transaction.

Cloud SQL doesn't support updating or altering existing index metadata. To modify a managed replica index, you must drop the existing index definition (or remove it from the replica group) and create a new index definition. For more information, see Modify managed replica indexes.

### Required role and privileges

You must use a database user account that's assigned the `cloudsqlsuperuser` role to execute stored procedures for managed replica indexes.

### Create managed replica indexes

To create and maintain managed replica indexes on your read replicas, follow these steps:

  1. **Create an index definition on the primary instance:**

Call the `mysql.cloudsql_replica_idx_defn_create` stored procedure on your database primary instance:
         
         CALL mysql.cloudsql_replica_idx_defn_create
         ('INDEX_DEFINITION_NAME', 'CREATE_INDEX_STATEMENT');

Replace the following:

     * `INDEX_DEFINITION_NAME`: the name of the index definition.
     * `CREATE_INDEX_STATEMENT`: the SQL statement that creates the secondary index (for example, `CREATE INDEX idx_age ON university.students (age)`). Note that this statement must be schema-prefixed.

Take note of the returned `idx_id` (a unique integer identifier for the definition) from the procedure output. Cloud SQL stores this data in `mysql.cloudsql_replica_idx_defn`, and you can retrieve the `idx_id` later by querying this table.

  2. **Add the index definition to a replica group:**

Map the index definition to a designated replica group name by calling `mysql.cloudsql_replica_idx_group_add` on the primary instance:
         
         CALL mysql.cloudsql_replica_idx_group_add
         (INDEX_DEFINITION_ID, 'GROUP_NAME');

Replace the following:

     * `INDEX_DEFINITION_ID`: the unique integer ID returned when you ran the `mysql.cloudsql_replica_idx_defn_create` stored procedure to create the secondary index.
     * `GROUP_NAME`: the name of the replica group mapping (for example, `reporting_group`). The `GROUP_NAME` is a custom name that you can select. If that group doesn't exist, then Cloud SQL creates a new one.

Cloud SQL stores this data in `mysql.cloudsql_replica_idx_group_map`, and you can retrieve group mappings later by querying this table.

**Note:** You can add the same index definition to multiple replica groups. 
  3. **Assign the group to your replica instance:**

Enable the designated group on your read replica by setting the database flag `cloudsql_index_recreate_replica_group` to your group name (for example, `reporting_group`).

  4. **Verify the restoration progress:**

Connect to your read replica instance, and check the creation progress and status of your indexes.

     * Check ongoing index creation progress:
           
           CALL mysql.cloudsql_replica_idx_show_status();
           

     * Check failed attempts and error messages:
           
           CALL mysql.cloudsql_replica_idx_show_errors();
           

     * List the status, retry details, and durations for all managed indexes:
           
           CALL mysql.cloudsql_replica_idx_show_all();
           




### Check managed replica index status

To check index operation status, connect to your read replica instance and query the `mysql.cloudsql_replica_idx_status` table:
    
    
    SELECT * FROM mysql.cloudsql_replica_idx_status;

The output is similar to the following:
    
    
    +--------+----------------------------------------------------+--------+-----------+---------------------+---------------------+-------------+---------+--------------------+---------+
    | idx_id | create_stmt                                        | action | thread_id | start_time          | end_time            | retry_count | err_msg | comment_tag        | status  |
    +--------+----------------------------------------------------+--------+-----------+---------------------+---------------------+-------------+---------+--------------------+---------+
    |      2 | CREATE INDEX t1_fname ON sampletest.t1(first_name) | CREATE |      8140 | 2026-08-26 10:52:13 | NULL                |           0 | NULL    | [SIC_4_1787741231] | RUNNING |
    |      4 | CREATE INDEX t2_lname ON sampletest.t2(last_name)  | DROP   |      NULL | 2026-08-26 10:52:13 | 2026-08-26 10:53:15 |           0 | NULL    | [SIC_4_1787741533] | DONE    |
    |      5 | CREATE INDEX t1_lname ON sampletest.t1(last_name)  | CREATE |      8142 | 2026-08-26 10:53:14 | NULL                |           0 | NULL    | [SIC_5_1787741594] | RUNNING |
    +--------+----------------------------------------------------+--------+-----------+---------------------+---------------------+-------------+---------+--------------------+---------+
    

Cloud SQL performs managed replica index maintenance in batches. When Cloud SQL picks up a group of `CREATE` or `DROP` actions, it creates a `PENDING` status entry for each index, and then serially executes each data definition language (DDL) statement. A failure on one index doesn't block the execution of subsequent indexes in the queue. Cloud SQL then picks up the next batch after approximately five minutes.

If an index creation fails, then Cloud SQL marks the status as `FAILED` and automatically retries the operation after one hour.

The `mysql.cloudsql_replica_idx_status` table contains all index operation status entries and includes the following columns:

  * **`idx_id`** : the unique integer identifier for the index definition.
  * **`create_stmt`** : the `CREATE INDEX` SQL statement.
  * **`action`** : the operation being performed (`CREATE` or `DROP`).
  * **`thread_id`** : the MySQL thread ID executing the operation.
  * **`start_time`** : the timestamp when the operation started.
  * **`end_time`** : the timestamp when the operation completed.
  * **`retry_count`** : the number of retry attempts for the operation. Cloud SQL retries failed index creations after one hour.
  * **`err_msg`** : the error message of the last failed operation.
  * **`comment_tag`** : the `[SIC_X_Y]` tag prepended to the index comment. This tag is used solely for internal management and has no functionality.
  * **`status`** : the current status of the operation: 
    * `PENDING`: the index operation has been added to the queue.
    * `RUNNING`: the index operation execution has started.
    * `DONE`: the index operation completed successfully.
    * `FAILED`: the index operation failed. Cloud SQL retries failed index creations after one hour.



### Drop managed replica indexes

To remove an index from a replica group or delete an index definition entirely, call the corresponding stored procedure on your primary instance:

  * **Remove an index definition from a replica group:**

Call `mysql.cloudsql_replica_idx_group_drop` on the primary instance:
        
        CALL mysql.cloudsql_replica_idx_group_drop
        (INDEX_DEFINITION_ID, 'GROUP_NAME');

Replace the following:

    * `INDEX_DEFINITION_ID`: the unique integer ID returned when you created the secondary index definition.
    * `GROUP_NAME`: the name of the replica group mapping (for example, `reporting_group`).
  * **Delete an index definition:**

Call `mysql.cloudsql_replica_idx_defn_drop` on the primary instance:
        
        CALL mysql.cloudsql_replica_idx_defn_drop
        (INDEX_DEFINITION_ID);

Replace the following:

    * `INDEX_DEFINITION_ID`: the unique integer ID of the index definition to delete.
**Note:** You can't delete an index definition if it is part of a replica group. Remove the index definition from all replica groups using `mysql.cloudsql_replica_idx_group_drop` before deleting it. 



For more information about stored procedures, see [Managed replica indexes stored procedures](https://docs.cloud.google.com/sql/docs/mysql/stored-procedures#managed-replica-indexes-sps).

### Modify managed replica indexes

Cloud SQL doesn't support updating or altering existing index metadata. You can't modify an existing index definition or its SQL statement directly.

To modify a managed replica index (for example, to change indexed columns or index options), you must remove or delete the existing index definition, and then create a new index definition.

To modify a managed replica index, follow these steps:

  1. **Remove or delete the existing index definition on the primary instance:**

     * To remove the index definition from a replica group, call `mysql.cloudsql_replica_idx_group_drop`:
           
           CALL mysql.cloudsql_replica_idx_group_drop
           (INDEX_DEFINITION_ID, 'GROUP_NAME');

     * To delete the index definition completely, call `mysql.cloudsql_replica_idx_defn_drop`:
           
           CALL mysql.cloudsql_replica_idx_defn_drop
           (INDEX_DEFINITION_ID);

Replace the following:

     * `INDEX_DEFINITION_ID`: the unique integer ID of the index definition to remove or delete.
     * `GROUP_NAME`: the name of the replica group mapping (for example, `reporting_group`).
  2. **Create a new index definition on the primary instance:**

Call `mysql.cloudsql_replica_idx_defn_create` with the updated index statement:
         
         CALL mysql.cloudsql_replica_idx_defn_create
         ('INDEX_DEFINITION_NAME', 'CREATE_INDEX_STATEMENT');

Replace the following:

     * `INDEX_DEFINITION_NAME`: the name of the new index definition.
     * `CREATE_INDEX_STATEMENT`: the updated SQL statement that creates the secondary index (for example, `CREATE INDEX idx_age ON university.students (age, name)`).

Take note of the new `idx_id` returned in the stored procedure output.

  3. **Map the new index definition to the replica group:**

Call `mysql.cloudsql_replica_idx_group_add` on the primary instance:
         
         CALL mysql.cloudsql_replica_idx_group_add
         (INDEX_DEFINITION_ID, 'GROUP_NAME');

Replace the following:

     * `INDEX_DEFINITION_ID`: the new unique integer ID returned in step 2.
     * `GROUP_NAME`: the name of the replica group mapping (for example, `reporting_group`).



After you map the new index definition to the replica group, the background maintenance process drops the existing index from the read replica and then creates the new index on the replica using the updated definition.

### Database configuration flags for managed replica indexes

You can customize managed replica index behavior dynamically by using the following global database flags:

  * **`cloudsql_index_recreate_enable`** : enables or disables the re-creation process. By default, the flag is set to `on`. Setting the flag to `off` immediately terminates ongoing index maintenance operations.

**Caution** : Turning off this flag while an index is actively being created terminates the operation immediately. Rolling back an in-progress index creation on a large table can cause performance issues and degrade overall database responsiveness. 
  * **`cloudsql_index_recreate_replica_group`** : designated replica group name for the replica (default is `NULL`). A replica can be assigned to only one replica group at a time. Replicas build all indexes mapped to this replica group name.




## Self-managed replica indexes

Cloud SQL includes two stored procedures in the `mysql` schema that you can use to add and drop secondary indexes on a MySQL read replica. Note that while these stored procedures can run on a primary source instance, they're designed for read replicas.

These indexes don't persist if the replica is re-created.

mysql.addSecondaryIdxOnReplica
    Adds a secondary index on the database. This stored procedure is a wrapper for the [CREATE INDEX](https://dev.mysql.com/doc/refman/8.0/en/create-index.html) DDL statement. 

#### Parameters:

  * **`idxType`** : type of index to create. For example, pass `UNIQUE` to create a unique index.
  * **`idxName`** : name of the index.
  * **`tableName`** : name of the table in the format of `schema.name`.
  * **`idxDefinition`** : definition of the index. Don't include the outer parentheses.
  * **`idxOption`** : any additional options to pass on index creation. For example, in MySQL 8.0, you can pass the `INVISIBLE` option for an invisible index.



#### Syntax:
    
    
    mysql.addSecondaryIdxOnReplica(idxType, idxName, tableName, idxDefinition, idxOption)
         

mysql.dropSecondaryIdxOnReplica
    Drops a secondary index on the database. This stored procedure is a wrapper for the [DROP INDEX](https://dev.mysql.com/doc/refman/8.0/en/drop-index.html) DDL statement. 

#### Parameters:

  * **`idxName`** : name of the index.
  * **`tableName`** : name of the table in the format of `schema.name`.
  * **`idxOption`** : any additional options to pass when dropping an index. For example, an algorithm option such as `INPLACE`.



#### Syntax:
    
    
    mysql.dropSecondaryIdxOnReplica(idxName, tableName, idxOption)
          

For the `idxType` and `idxOption` parameters, consult the documentation for the major version of MySQL running on the Cloud SQL instance.

### Examples

This section provides examples of how you might correctly or incorrectly add or drop self-managed replica indexes.

#### Correct usage

Here are some example invocations of the procedures. Suppose you have a table with the following definition:
    
    
    CREATE TABLE sampletest.t1(
       id int(10) unsigned NOT NULL AUTO_INCREMENT,
       first_name varchar(64) NOT NULL,
       last_name varchar(64) NOT NULL,
       license_id int NOT NULL,
       PRIMARY KEY (id),
       KEY idx_fname (first_name)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    

If you want to create a regular index named `t1_fname_lname` on the `first_name` and `last_name` columns, run the following statement:
    
    
    CALL mysql.addSecondaryIdxOnReplica('', 't1_fname_lname', 'sampletest.t1', 'first_name, last_name', '')
    

If you also want to create a unique index named `t1_license_id` on the `license_id` column with the comment "unique license ID", run the following statement:
    
    
    CALL mysql.addSecondaryIdxOnReplica('unique', 't1_license_id', 'sampletest.t1', 'license_id', 'comment "unique license ID"')
    

If you want to drop the `t1_fname_lname` index, run the following statement:
    
    
    CALL mysql.dropSecondaryIdxOnReplica('t1_fname_lname', 'sampletest.t1', '')
    

#### Incorrect usage

The following attempt to create an index on the `first_name` and `last_name` columns fails due to the outer parentheses in the `idxDefinition` parameter:
    
    
    CALL mysql.addSecondaryIdxOnReplica('', 't1_extra_parenthesis', 'sampletest.t1', '(first_name, last_name)', '')
    

You can only add indexes on customer-created tables. The following attempt to create an index on the `host` column of the `mysql.servers` table fails:
    
    
    CALL mysql.addSecondaryIdxOnReplica('', 'idx_invalid', 'mysql.servers', 'host', '')
    

You can only use the `dropSecondaryIdxOnReplica` procedure to drop indexes previously created using the `addSecondaryIdxOnReplica` procedure. For example, the following call to drop the existing `idx_fname` index fails:
    
    
    CALL mysql.dropSecondaryIdxOnReplica('idx_fname', 'sampletest.t1', '')
    

SQL injection in these procedure calls fails. For example, the following SQL injection with a comment sequence fails:
    
    
    CALL mysql.addSecondaryIdxOnReplica("user 'a'@'%' --", 'idx_fname', 'sampletest.t1', 'first_name', '')
    

Similarly, this SQL injection attempt with a delimiter fails:
    
    
    CALL mysql.addSecondaryIdxOnReplica('', 'idx_fname', 'sampletest.t1', 'first_name', ';flush status')
    

## Migrate from self-managed to managed replica indexes

Although both managed replica indexes and self-managed replica indexes can coexist on the same instance, you can migrate to managed replica indexes.

To migrate from self-managed to managed replica indexes, follow these steps:

  1. **Register index definitions on the primary instance:**

Call `mysql.cloudsql_replica_idx_defn_create` on your primary instance for each secondary index:
         
         CALL mysql.cloudsql_replica_idx_defn_create
         ('INDEX_DEFINITION_NAME',
         'CREATE INDEX INDEX_NAME ON DATABASE.TABLE (COLUMNS)');

Take note of the returned `idx_id` (a unique integer identifier for the definition) from the procedure output.

  2. **Add the index definition to a replica group:**

Map the index definition to a designated replica group name by calling `mysql.cloudsql_replica_idx_group_add` on the primary instance:
         
         CALL mysql.cloudsql_replica_idx_group_add
         (INDEX_DEFINITION_ID, 'REPLICA_GROUP');

  3. **Configure the replica group flag on the read replica:**

Set the `cloudsql_index_recreate_replica_group` database flag on your read replica instance to target the group name:
         
         gcloud sql instances patch REPLICA_INSTANCE_NAME \
         --database-flags=EXISTING_FLAGS,cloudsql_index_recreate_replica_group=REPLICA_GROUP

Make sure that the group name provided in the `cloudsql_index_recreate_replica_group` database flag matches the group name specified in `mysql.cloudsql_replica_idx_group_add` exactly.

  4. **Verify or transition the existing indexes:**

Because the index already exists on the read replica, you might see errors with a `FAILED` status in `mysql.cloudsql_replica_idx_status` when the background process attempts to create the index. You can choose one of the following approaches:

     * **Wait for replica re-creation** : you can safely ignore the `FAILED` status in the status table. Cloud SQL automatically re-creates the secondary index using the managed replica index method after a replica re-creation event.
     * **Transition immediately** : if you want Cloud SQL to manage the index immediately without waiting for a replica re-creation, connect to the read replica and remove the self-managed index by using the `mysql.dropSecondaryIdxOnReplica` stored procedure:
           
           CALL mysql.dropSecondaryIdxOnReplica('INDEX_NAME', 'DATABASE.TABLE', '');

During the next background maintenance cycle (approximately every five minutes), Cloud SQL automatically re-creates and tracks the managed replica index.

**Caution** : If you use this method, then read query performance might degrade during the interval between dropping the self-managed index and creating the managed replica index. 



## Troubleshoot replica indexes

To troubleshoot replica indexes, verify the following:

  * **Verify that managed replica indexes are enabled for the replica instance:**

If you're using managed replica indexes, make sure that the `cloudsql_index_recreate_enable` database flag is set to `on` on the read replica.

For more information about configuring database flags, see [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags).

  * **Check operation status and errors:**

Connect to the read replica and query `mysql.cloudsql_replica_idx_status` or run `CALL mysql.cloudsql_replica_idx_show_errors();` to view error messages for any failed operations. A failure on one index doesn't block the execution of subsequent indexes in the queue.




## What's next

  * Learn more about [read replica indexes](https://docs.cloud.google.com/sql/docs/mysql/replication/read-replica-indexes).
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
