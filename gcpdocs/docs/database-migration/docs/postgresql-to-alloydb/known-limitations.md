---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations/
title: Known limitations \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T12:43:05.399574+00:00
---

# Known limitations  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview)



Send feedback 

#  Known limitations Stay organized with collections  Save and categorize content based on your preferences. 

Before you choose to migrate your databases to AlloyDB for PostgreSQL, consider known limitations for this migration scenario.

**Note:** You can also use Google Cloud Migration Center to discover gaps in feature support. See [ Discover and import databases](https://docs.cloud.google.com/migration-center/docs/discover-import-databases) in the Migration Center documentation.

Known limitations for using a PostgreSQL database as a source include:

  * The `pglogical` extension doesn't support the replication of [ generated columns](https://www.postgresql.org/docs/current/ddl-generated-columns.html) for PostgreSQL 12+.

  * Changes to table structures (DDL) aren't replicated through standard DDL commands, but only with commands executed using the `pglogical` extension used for replication. This includes [changes to `enum` types](https://www.postgresql.org/docs/current/sql-altertype.html).

    * For example, `pglogical` provides the `pglogical.replicate_ddl_command` function that allows DDL to be run on both the source database and replica at a consistent point. The user running this command on the source must already exist on the replica.
    * In order to replicate data for newly created tables, you must use the `pglogical.replication_set_add_table` command to add new tables to existing replication sets.
    * To learn more about DDL replication while the migration is in progress, see [Migration fidelity](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-fidelity).
  * Object limitations:

    * Foreign tables aren't replicated by logical replication.
    * `UNLOGGED` and `TEMPORARY` tables aren't and can't be replicated.
    * Large Object data type (`oid` referencing `pg_largeobject`) isn't supported by PostgreSQL logical decoding.
    * Database Migration Service doesn't migrate data from materialized views, just the view schema. To populate the views on the destination database, run: `REFRESH MATERIALIZED VIEW view_name;`.
    * The `SEQUENCE` states (for example, `last_value`) on the destination might vary from the source during ongoing CDC. Sequence values are synchronized during the final promotion step.
  * For tables that don't have primary keys, Database Migration Service supports migration of the **initial snapshot and`INSERT` statements during the change data capture (CDC) phase**. Migrating `UPDATE` and `DELETE` statements is different for:

    * _Standard migrations_ : `UPDATE` and `DELETE` statements aren't migrated for tables without primary keys. You must add primary keys for your columns before you migrate, or migrate `UPDATE` and `DELETE` statements manually.
    * _Quick-start migrations_ : With quick-start migrations, primary keys aren't required to replicate `UPDATE` and `DELETE` operations if you set the replica identity to `INDEX` or `FULL`. Configuring `REPLICA IDENTITY FULL` increases write-ahead log (WAL) volume and resource overhead. Adding a primary key is recommended where feasible. For more information, see the [ PostgreSQL Replica Identity documentation](https://www.postgresql.org/docs/current/logical-replication-publication.html#LOGICAL-REPLICATION-PUBLICATION-REPLICA-IDENTITY) and [ Quick-start migrations guide](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/quick-start-migrations-guide).
  * Only extensions and extension versions that AlloyDB for PostgreSQL supports for PostgreSQL can be migrated. Database Migration Service doesn't migrate extensions that are unsupported by AlloyDB for PostgreSQL, and if extensions exist in the source database whose versions aren't supported by AlloyDB for PostgreSQL, testing or starting the migration job might fail. To ensure a smooth migration, verify that your source extensions are supported and that your applications don't reference unsupported extensions. For the list of supported extensions, see [ Supported extensions](https://docs.cloud.google.com/alloydb/docs/reference/extensions) in the AlloyDB for PostgreSQL documentation.

  * The `pg_cron` extension (or any cron jobs configured within the extension) isn't migrated by Database Migration Service, but is supported in AlloyDB for PostgreSQL destinations. If you use `pg_cron` in your source databases, reinstall the extension and configure your cron jobs on the destination cluster after the migration is complete.

  * Database Migration Service doesn't support migrating from read replicas that are in recovery mode.

  * Database Migration Service doesn't support Amazon RDS sources where the AWS SCT extension pack is applied.

  * User-defined functions written in C can't be migrated, except for functions that are installed when creating extensions supported by AlloyDB for PostgreSQL.

  * Databases that are added to the source instance after the migration job has started aren't migrated.

  * You can select specific databases when you migrate by using Database Migration Service. All tables and schemas from the selected databases are migrated, excluding:

    * The information schema (`information_schema`).
    * Any schemas beginning with `pg_` (for example, `pg_catalog`, `pg_toast`, `pg _temp_ *`). For the full list of PostgreSQL catalogs that begin with `pg_`, see [ PostgreSQL system catalogs](https://www.postgresql.org/docs/current/catalogs.html) in the PostgreSQL documentation.
    * User login credentials and roles.
  * If encrypted databases require customer-managed encryption keys (CMEK) to decrypt data, and Database Migration Service doesn't have access to the keys, the databases can't be migrated. However, data encrypted with the [ `pgcrypto` extension](https://docs.cloud.google.com/alloydb/docs/reference/extensions) can be migrated because AlloyDB for PostgreSQL supports `pgcrypto`. Database Migration Service also supports migrating from encrypted Amazon Aurora or Amazon RDS databases because AWS handles decryption transparently. For more information, see [ Encrypting Amazon Aurora resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html) and [Encrypting Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html).

  * **Migrating databases aren't write-protected during migration** : AlloyDB for PostgreSQL doesn't run the destination instance in read-only mode during migration. Although you can connect to the destination cluster to [create and manage database users](https://docs.cloud.google.com/alloydb/docs/database-users/about) or apply necessary schema changes (DDL), don't perform write operations (such as `INSERT`, `UPDATE`, or `DELETE`) on databases or tables that are being migrated. Writing to migrating data can cause [ replication conflicts](https://www.postgresql.org/docs/current/logical-replication-conflicts.html) or migration failures.

  * Trigger behavior depends on trigger configuration. By default, triggers don't fire on the replica during replication unless configured with `ALTER EVENT TRIGGER` or `ALTER TABLE ... ENABLE ALWAYS TRIGGER`.

  * Custom tablespaces are mapped to the default `pg_default` tablespace in AlloyDB for PostgreSQL.

  * The [ Private Service Connect interfaces connectivity method](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods#psc-interfaces) is only supported for migrating to existing destination clusters. If you want to use private IP connectivity and migrate to a new destination cluster in a standard migration, use VPC peering.

  * Identity and Access Management database authentication for destination clusters isn't supported. Database Migration Service connects to the destination database using database user authentication. For more information about IAM, see [ Manage IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth) in the AlloyDB for PostgreSQL documentation.




### Security definer functions

Functions defined with `SECURITY DEFINER` run with the privileges of the user that owns the function rather than the user who executes it.

During continuous migration to AlloyDB for PostgreSQL, routines defined with `SECURITY DEFINER` become owned by the internal migration service user `alloydbexternalsync` on the destination primary instance. Because `alloydbexternalsync` possesses elevated administrative privileges, including the `alloydbsuperuser` and `alloydbreplica` roles, any user authorized to execute these functions runs them with full `alloydbsuperuser` rights. This creates an unintended privilege escalation risk.

To remediate this risk, audit all `SECURITY DEFINER` functions on your destination cluster and revoke public execution privileges immediately after migration:
    
    
    REVOKE EXECUTE ON FUNCTION SCHEMA_NAME.FUNCTION_NAME(ARGUMENT_TYPES) FROM PUBLIC;
    GRANT EXECUTE ON FUNCTION SCHEMA_NAME.FUNCTION_NAME(ARGUMENT_TYPES) TO "AUTHORIZED_USER";

### Collation and locale alignment

AlloyDB for PostgreSQL defaults to `C.UTF-8` and `en_US.utf8` locales provided by `libc`. All other locales in AlloyDB for PostgreSQL use International Components for Unicode (ICU) collations.

If your source database uses a default collation based on another `libc` locale, that default doesn't automatically carry over. To ensure consistent sorting for queries using `ORDER BY`, you might need to update your tables with explicit ICU collations after migration. For more information, see [ Supported locales for imported data](https://docs.cloud.google.com/alloydb/docs/migration-overview#locales) in the AlloyDB for PostgreSQL documentation.

### Limitations for migrations to existing destination clusters

  * You can configure only one active migration job per destination cluster.
  * **Destination cluster demotion for standard migrations** : For standard migrations to existing AlloyDB for PostgreSQL clusters, Database Migration Service demotes the standalone cluster to configure it as an external replica of the source database. 
    * You must confirm demotion when creating the migration job in the Google Cloud console by entering the destination cluster ID (or by running `gcloud database-migration migration-jobs demote-destination`). 
    * [Quick-start migrations](https://docs.cloud.google.com/database-migration/docs/about-quick-start-migrations) use PostgreSQL `pgnative` logical replication and don't require or perform destination cluster demotion. 
  * For standard migrations, your existing destination cluster must be empty or contain only default system configuration data. Migrating to an existing destination cluster that contains user data (such as tables) isn't supported for standard migrations. 

If you encounter issues due to extra data in your existing destination cluster, clear the databases in your destination cluster and retry the migration job. See [ Clear extra data from your existing destination cluster](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/diagnose-issues#clear-ext-instance-data-steps).

  * Migrating to clusters with read pool instances **is supported**. For more information on AlloyDB for PostgreSQL clusters and instances, see [AlloyDB for PostgreSQL overview](https://docs.cloud.google.com/alloydb/docs/overview). 



### Data dump parallelism considerations

When you [create a migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job), you can increase the number of parallel subscriptions to accelerate the initial data dump and ongoing change data capture (CDC) replication. Using higher data dump parallelism settings also increases connection and resource utilization on both your source database and your destination AlloyDB for PostgreSQL cluster.

  * Ensure that your source database has sufficient CPU, memory, and I/O headroom before you use **Maximum** parallelism.
  * When using adjusted data dump parallelism, you must configure higher values for `max_replication_slots`, `max_wal_senders`, and `max_worker_processes` on your source database. For detailed parameter calculations, see [Configure your source database](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database).
  * The `pglogical` extension replicates data at the table level during the initial full dump. A single non-partitioned table is assigned to one subscription and isn't split across multiple parallel subscriptions or worker threads.
  * The `pglogical` extension replicates individual leaf partitions as separate tables and can distribute multiple leaf partitions across parallel subscriptions during the initial full dump. A single large leaf partition can't be split across multiple subscriptions and is copied by a single thread.
  * Database Migration Service sorts tables by size and distributes them across parallel subscriptions. Database Migration Service creates up to 2 subscriptions per database (and up to 2 total across all databases) for **Optimal** parallelism, and up to 4 subscriptions per database (and up to 4 total across all databases) for **Maximum** parallelism, with at least 1 subscription per migrated database. For example, if a database has one 1 TB table and several small tables, Database Migration Service isolates the 1 TB table in one subscription and distributes the smaller tables across the remaining subscriptions. Even with multiple subscriptions active, the overall initial dump speed is still bounded by the time required to copy the single 1 TB table.
  * Database Migration Service assigns tables without primary keys to dedicated insert-only replication sets (one per parallel subscription). Multiple tables without primary keys can be distributed across parallel subscriptions, but during the initial full dump each individual table is copied as a single table stream within one subscription and isn't split across multiple parallel threads.



### Quotas

  * Up to 2,000 connection profiles and 1,000 migration jobs can exist at any given time. To create space for more, delete unused migration jobs and connection profiles. For more details, see [Quotas and limits](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/quotas).



### PostgreSQL extension version compatibility during major version upgrades

When you migrate to a higher PostgreSQL major version, Database Migration Service uses the `pg_restore` utility, which installs the default extension version of the target PostgreSQL major version. You can't specify an exact extension version for the `pg_restore` utility.

If your source database uses an extension version that is schema-incompatible with the default version installed on the target PostgreSQL major version, the migration might fail due to a schema mismatch or internal errors.

To avoid migration failures, verify schema compatibility. Before you migrate, upgrade the extensions on your source database to a version compatible with the target PostgreSQL major version.

## What's next

  * For complete, step-by-step migration walkthroughs, see [ Get started with AlloyDB for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/get-started-with-alloydb-migrations).

  * To plan network connectivity between your source and destination instances, see [ Networking considerations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-considerations).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
