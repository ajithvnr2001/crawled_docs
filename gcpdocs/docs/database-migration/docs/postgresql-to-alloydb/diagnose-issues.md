---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/diagnose-issues/
title: Diagnose issues in PostgreSQL to AlloyDB for PostgreSQL migrations \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T11:34:55.591366+00:00
---

# Diagnose issues in PostgreSQL to AlloyDB for PostgreSQL migrations  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/diagnose-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview)



Send feedback 

#  Diagnose issues in PostgreSQL to AlloyDB for PostgreSQL migrations Stay organized with collections  Save and categorize content based on your preferences. 

The migration job process might incur errors during runtime.

  * Some errors, such as a bad password on the source database, are recoverable, meaning they can be fixed and the migration job resumes automatically.
  * Some are unrecoverable, such as data corruption or schema incompatibilities, meaning the migration job needs to be restarted from the beginning.



When an error occurs, the migration job status changes to `Failed`, and the substatus reflects the last status before failure.

To troubleshoot an error, navigate to the failed migration job to view the error and follow the steps outlined in the error message.

To view more details about the error, navigate to Cloud Monitoring using the link on the migration job. The logs are filtered to the specific migration job.

The following table lists common issues and their solutions:

For this problem... | The issue might be... | Try this...  
---|---|---  
When you migrate to [an existing destination cluster](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-existing-instance), you receive the following error message: `The destination cluster contains existing data or user defined entities (for example databases, tables, or functions). You can only migrate to empty clusters. Clear your destination cluster and retry the migration job.` |  Your destination AlloyDB for PostgreSQL cluster contains extra user data. You can only migrate to existing clusters that are empty. See [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations#existing-instance-limitations).  | Clear the conflicting or extra data from your destination cluster and retry the migration job. See Clear extra data from your existing destination cluster.   
Failure connecting to the source database instance.  | There was a connectivity issue between the source database instance and the destination AlloyDB for PostgreSQL cluster. | Follow the steps in [Debugging connectivity](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/debugging-connectivity).  
Failure running migration job due to incompatible source and destination database versions.  | The source and destination database versions aren't a supported combination. Specifically, the source database version provided is incompatible with the destination database version. | Make sure that the [destination database version](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest) is the same or a later supported major version than the source database version. Then, create a new migration job.  
Data definition languages (DDLs) or data manipulation languages (DMLs) are blocked on the source.  | DDLs that require the `ACCESS EXCLUSIVE` [lock](https://www.postgresql.org/docs/10/explicit-locking.html#LOCKING-TABLES) and are running during the full dump phase are blocked. | During the initial sync process (full dump), DDLs or programs requiring `ACCESS EXCLUSIVE` [locks](https://www.postgresql.org/docs/10/explicit-locking.html#LOCKING-TABLES) such as `ALTER TABLE` or `DROP TABLE` should be avoided on the tables. Otherwise, the DDLs or programs wait until the initial sync finishes. For example, if a table is still in the initial sync process and an `ALTER TABLE` command is executed on the same table, then the command won't run and subsequent DDL and DML commands are blocked until the initial sync finishes.  
Error Message: `No pglogical extension installed on databases (X)` | One or more source databases doesn't have `pglogical` installed. | Follow [these guidelines](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database) to install `pglogical` on the databases on the source instance.  
When migrating to PostgreSQL version 15, after multiple subsequent connection retry attempts one of the following symptoms occurs: 

  * You receive a `Cannot connect to invalid database` error message. 
  * The [Total destination storage usage migration job metric](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-job-metrics) shows no progress after a long time when the migration job is performing the full database dump. 

|  This problem is often attributed to the deadlock issue in the `pglogical` extension. For more information, see the [`pglogical` issue tracker in GitHub](https://github.com/2ndQuadrant/pglogical/issues/418).  | Retry the migration job, or migrate to an intermediate PostgreSQL version first. For more details, see Error message: `Cannot connect to invalid database`.   
Error Message: `Replication user 'x' doesn't have sufficient privileges.` | The user who is using Database Migration Service doesn't have the required privileges to perform the designated operation. | Follow [these guidelines](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database) to ensure that this user has the required privileges.  
Error Message: `Unable to connect to source database server.` | Database Migration Service can't establish a connection to the source database server. | Make sure that the source and destination database instances can communicate with each other, and that you've completed all of the required prerequisites that appeared when you [defined your settings for the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job).  
Error Message: `The source database 'wal_level' configuration must be equal to 'logical'.` | The `wal_level` for the source database is set to a value other than `logical`. | Set the `wal_level` to `logical`. See [WAL level configuration](https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-WAL-LEVEL).  
Error Message: `The source database 'max_replication_slots' configuration is not sufficient.` | The `max_replication_slots` parameter wasn't configured correctly. | Follow [these guidelines](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database) to set this parameter correctly.  
Error Message: `The source database 'max_wal_senders' configuration is not sufficient.` | The `max_wal_senders` parameter wasn't configured correctly. | Follow [these guidelines](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database) to set this parameter correctly.  
Error Message: `The source database 'max_worker_processes' configuration is not sufficient.` | The `max_worker_processes` parameter wasn't configured correctly. | Follow [these guidelines](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database) to set this parameter correctly.  
Error Message: `Cleanup may have failed on source due to error: generic::unknown: failed to connect to on-premises database.` OR  Error Message: `Error promoting EM replica: finished drop replication with errors.` | The settings needed for replication can't be cleaned up during the promotion of a migration job. | For each database, run commands as a user with the `superuser` privilege. For more information about which commands to run, see Clean up replication slots.  
Error Message: `x509 certificate signed by unknown authority.` | The source CA certificate provided to Database Migration Service might contain only the root certificate. However, the source certificate requires both the root certificate and any intermediate certificates. For example, for Amazon RDS, using a standalone root certificate instead of a certificate bundle might result in this issue. | Create a combined source CA certificate that contains both the root certificate and all required intermediate certificates. For Amazon RDS sources, use a certificate bundle that includes both the intermediate and root certificates. For more information, see [Download certificate bundles](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html#UsingWithRDS.SSL.CertificatesDownload) in the Amazon RDS documentation.  
Error Message: `ERROR: Out of shared memory HINT: You might need to increase max_locks_per_transaction.` | The value set for the [`max_locks_per_transaction`](https://www.postgresql.org/docs/13/runtime-config-locks.html) parameter isn't sufficient. | Set the value for this parameter to be at least {`max_number_of_tables_per_database`}/(`max_connections` \+ `max_prepared_transactions`).  
Error Message: `ERROR: no data left in message.` | The pglogical package isn't installed correctly on the source instance. | For more information on how to install this package properly, see [Configure your source database](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database).  
Error Message: `Cannot assign TransactionIds during recovery.` | The source that is configured is in recovery mode. | Configure a source that isn't in recovery mode.  
The full dump is slow. | The AlloyDB for PostgreSQL destination cluster primary instance might be slow in importing large data from the source database. | 

  * Choose a higher machine tier for the destination AlloyDB for PostgreSQL primary instance to get maximum available network bandwidth and CPU capacity.
  * Tune the destination's [`max_wal_size`](https://www.postgresql.org/docs/current/static/runtime-config-wal.html#GUC-MAX-WAL-SIZE) flag. Typically, 32 GB or 64 GB is a good value to set for this flag. Updating this flag doesn't require you to restart the database server.

  
Error Message: `subscriber {subscriber_name} initialization failed during nonrecoverable step (d), please try the setup again` | The migration job failed during the full dump phase and the job isn't recoverable. The source database instance was restarted or in recovery mode, or the replication connections ended because of an insufficient value set for the [`wal_sender_timeout`](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-WAL-SENDER-TIMEOUT) parameter. To find the root cause of the problem:

  1. Go to the [Logs Explorer](https://console.cloud.google.com/logs/query) page in the Google Cloud console.
  2. From the resource list, select your AlloyDB for PostgreSQL instance. A list of the most recent logs for the instance appears.
  3. From the log file names, select `postgres.log`.
  4. Set the log's severity level to all levels above `Warning`. The first error logs may be the root cause of the failure.

| 

  * Make sure that Database Migration Service can always connect to the source database instance during the full dump phase.
  * Check if the value of the `wal_sender_timeout` parameter is set to a larger number (for example, `0`) on the source database instance.
  * Restart the migration job, and then try again.

  
Error Message: `ERROR: unknown column name {column_name}` | A column was added to a replicated table on the primary node but not on the replica node. |  Only data manipulation language (DML) changes are updated automatically during continuous migrations. You must manage data definition language (DDL) changes so that the source and destination databases remain compatible. You can achieve this in two ways:

  * Stop writes to the source database and run the DDL commands on both source and destination. Before running the DDL commands on the destination, grant the `alloydbexternalsync` role to the AlloyDB for PostgreSQL user applying the DDL changes.
  * Use `pglogical.replicate_ddl_command` to allow DDL commands to run on the source and destination at a consistent point. The user running the commands must have the same username on both the source and the destination, and should be the superuser or the owner of the artifact being migrated (for example, the table, sequence, view, or database).

See [Continuous migration](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-fidelity#continuous_migration) to find examples of using `pglogical.replicate_ddl_command`.  
Error Message: `ERROR: cannot truncate a table referenced in a foreign key constraint` | A user tried to truncate a table that has a foreign key constraint. |  Remove the foreign key constraint first, and then truncate the table.  
Error Message: `ERROR: connection to other side has died` | The replication connection ended because of an insufficient value set for the `wal_sender_timeout` parameter. The error usually occurs during the replication phase after the success of the initial dump. |  Consider increasing the [`wal_sender_timeout`](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-WAL-SENDER-TIMEOUT) parameter value or disable the timeout mechanism by setting its value to `0` on the source database instance.  
Warning Message: `migration job test configuration has returned the following warnings: Some table(s) have limited support.` | Source has tables with limited support, for example tables without primary keys. |  This is a warning message. You can proceed with the migration, but note that in standard migrations, tables without primary keys replicate only the initial snapshot and `INSERT` statements during the change data capture (CDC) phase; `UPDATE` and `DELETE` statements aren't replicated. For more information, review [Configure your source database](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database).   
When you migrate selected databases and the migration job is unable to replicate data to one or more databases, a **Failed** status is displayed in the list of databases. | Various migration job errors. | In the **Errors** column, click **View errors** and fix them. You can also remove the failed databases from the migration job. For more information about removing a failed database from a migration job, see [Manage migration jobs](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-job-actions).  
  
* * *

### Clear extra data from your existing destination cluster

When you migrate to [an existing destination cluster](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-existing-instance), you receive the following error message: `The destination cluster contains existing data or user defined entities (for example databases, tables, or functions). You can only migrate to empty clusters. Clear your destination cluster and retry the migration job.`

This issue can occur if your destination cluster contains extra data. You can only migrate to existing clusters that are empty. See [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations#existing-instance-limitations).

#### Things to try

Clear the conflicting or extra data from your destination cluster and start the migration job again by performing the following steps:

  1. [Stop the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-job-actions).
  2. [Connect to your destination AlloyDB for PostgreSQL cluster](https://docs.cloud.google.com/alloydb/docs/connection-overview) primary instance using `psql` or AlloyDB Studio.
  3. Remove extra data from your destination cluster databases. Your destination can only contain system configuration data. Destination databases can't contain user data (such as user-defined tables or routines). There are different SQL statements you can run on your databases to find non-system data: 

#### Example SQL statement to retrieve non-system databases (click to expand)
         
         SELECT datname FROM pg_catalog.pg_database
         WHERE datname NOT IN ('alloydbadmin', 'template1', 'template0', 'postgres');

#### Example SQL statement to retrieve non-system data in the `postgres` database (click to expand)

The `postgres` database is a system database, but it can contain non-system data. Make sure you run these statements on the `postgres` database. If you use the `psql` client to connect to the destination cluster, you can switch to another database without resetting your connection by using the [`\connect {database_name_here}`](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-META-COMMAND-C-LC) command.
         
         SELECT table_schema, table_name FROM information_schema.tables
         WHERE table_schema != 'information_schema' AND table_schema not like 'pg\_%';
         
         SELECT routine_schema, routine_name FROM information_schema.routines
         WHERE routine_schema != 'information_schema' AND routine_schema not like 'pg\_%';
         
         SELECT extname FROM pg_extension WHERE extname NOT IN ('plpgsql', 'alloydb_utility');
             

  4. Drop any non-system databases, user tables, and user-defined functions identified in the previous step.
  5. [Start the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-job-actions).



* * *

### Clean up replication slots

You see one of the following messages: 

  * `Cleanup may have failed on source due to error: generic::unknown: failed to connect to on-premises database.`
  * `Error promoting EM replica: finished drop replication with errors.`



#### The issue might be

When promoting an AlloyDB for PostgreSQL destination cluster, if the source instance isn't reachable from the AlloyDB for PostgreSQL cluster (for example, the source instance isn't running, or you removed the AlloyDB for PostgreSQL cluster from the allowlist of source instances), then the settings needed for replication can't be cleaned up during the promotion of a migration job. You must clean up the replication slots manually.

#### Things to try

For each database, run the following commands as a user with the `superuser` privilege:

  1. Get the replication slot names from the error message, and then run the following command to drop the slots, one by one:
         
         SELECT pg_drop_replication_slot('slot_name');

  2. If the replication slot names aren't available in the error message, then run the following command to query for the existing replication slots:
         
         SELECT pg_drop_replication_slot(slot_name) FROM pg_replication_slots WHERE slot_name LIKE '%alloydb%' AND active = 'f';

  3. If there are no AlloyDB for PostgreSQL replicas using the source instance, then run the following command to clean up `pglogical` settings:
         
         SELECT pglogical.drop_node(node_name) FROM pglogical.node WHERE node_name LIKE '%alloydb%';

  4. If the `pglogical` extension isn't needed anymore, then run the following command to uninstall the extension:
         
         DROP EXTENSION IF EXISTS pglogical;




* * *

### Error message: `Cannot connect to invalid database`

When migrating to PostgreSQL version 15, after multiple subsequent connection retry attempts one of the following symptoms occurs:

  * You receive a `Cannot connect to invalid database` error message. 
  * The [Total destination storage usage migration job metric](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-job-metrics) shows no progress after a long time when the migration job is performing the full database dump. 



#### The issue might be

This problem is often attributed to the deadlock issue in the `pglogical` extension. For more information, see the [`pglogical` issue tracker in GitHub](https://github.com/2ndQuadrant/pglogical/issues/418).

#### Things to try

##### Perform the migration job again with a new destination cluster

Try deleting the destination cluster where you experienced the issue and recreate your migration job. Follow these steps:

  1. Delete the failed migration job. See [Review a migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-job-actions).
  2. Delete the destination cluster where you experienced the problem. See [AlloyDB cluster management](https://docs.cloud.google.com/alloydb/docs/overview).
  3. Recreate your migration job. See [Create a migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job).



##### Migrate to an intermediate version

Consider migrating to an earlier PostgreSQL version, such as PostgreSQL 14. After a successful migration, you can upgrade to the desired PostgreSQL 15 instance. See [Upgrade a database major version](https://docs.cloud.google.com/alloydb/docs/cluster-upgrade) in the AlloyDB for PostgreSQL documentation.

* * *

### Delete orphaned AlloyDB for PostgreSQL clusters in bootstrapping mode

In rare edge cases, you might find that your migration job has been deleted, while the associated AlloyDB for PostgreSQL cluster hasn't, and is still in bootstrapping mode. You can delete the cluster using the `gcloud alloydb clusters delete` command with the `--force` option:
    
    
    gcloud alloydb clusters delete CLUSTER_ID \
        --region=REGION_ID \
        --force

Note that deleting a bootstrapping cluster while it is being used by an active migration job results in undefined behavior.

* * *

### Manage users and roles

#### Migrate existing users

Currently, Database Migration Service doesn't support automatically migrating existing users and roles from a source instance into a destination AlloyDB for PostgreSQL cluster. You can manage this migration by [creating the users in AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/database-users/about) manually.

#### About the `alloydbexternalsync` user

During a standard migration, all database objects on the AlloyDB for PostgreSQL replica are owned by the `alloydbexternalsync` user (quick-start migrations use the `postgres` user). After the data is migrated and the migration job is promoted, you can modify ownership of the objects to other application users by completing the following steps:

  * Run the `GRANT alloydbexternalsync TO USER;` command.
  * On each database, run the `REASSIGN OWNED BY alloydbexternalsync TO USER;` command.
  * To remove the `alloydbexternalsync` user, run the `DROP ROLE alloydbexternalsync;` command.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
