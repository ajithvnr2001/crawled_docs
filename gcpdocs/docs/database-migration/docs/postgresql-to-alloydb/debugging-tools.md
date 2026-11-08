---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/debugging-tools/
title: Debugging and other tools \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T09:08:32.658014+00:00
---

# Debugging and other tools  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/debugging-tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview)



Send feedback 

#  Debugging and other tools Stay organized with collections  Save and categorize content based on your preferences. 

This page includes scripts that help with debugging and using PostgreSQL.

## Migrate UPDATE and DELETE operations for non-primary key tables

For tables that don't have primary keys, in standard migrations Database Migration Service supports migration of the initial snapshot and `INSERT` statements during the change data capture (CDC) phase. However, `UPDATE` and `DELETE` statements aren't automatically replicated for non-primary key tables in standard migrations (quick-start migrations support replicating `UPDATE` and `DELETE` operations when you configure `REPLICA IDENTITY`).

To detect and manually synchronize missing `UPDATE` and `DELETE` operations in standard migrations, complete the procedures in the following sections.

### Detect missing data between source and AlloyDB for PostgreSQL destination cluster

  1. Identify which tables in your source database don't have primary keys: 
         
         SELECT tab.table_schema,
                tab.table_name
         FROM information_schema.tables tab
         LEFT JOIN information_schema.table_constraints tco 
                   ON tab.table_schema = tco.table_schema
                   AND tab.table_name = tco.table_name 
                   AND tco.constraint_type = 'PRIMARY KEY'
         WHERE tab.table_type = 'BASE TABLE'
               AND tab.table_schema NOT IN ('pg_catalog', 'information_schema', 'pglogical')
               AND tco.constraint_name IS NULL
         ORDER BY table_schema,
                  table_name;

  2. Before starting the migration job, for all tables without primary keys, record their modification statistics: 
         
         SELECT schemaname,
                relname,
                n_tup_ins,
                n_tup_upd,
                n_tup_del
         FROM pg_stat_user_tables
         WHERE schemaname NOT IN ('pglogical', 'pg_catalog', 'information_schema');

Where: 
     * `n_tup_ins`: number of rows inserted
     * `n_tup_upd`: number of rows updated (includes HOT updated rows)
     * `n_tup_del`: number of rows deleted
  3. Save these baseline statistics to a table or file.
  4. After the migration setup is complete and before promoting the migration job, run the query again.
  5. Compare the initial statistics with the latest statistics. If `n_tup_upd` or `n_tup_del` changed during migration, updates or deletes occurred on the source that weren't captured by CDC.

**Note:** Running the `pg_stat_reset()` function resets statistics in `pg_stat_user_tables`. If this function is executed on the source, the statistics won't reflect historical counts.

### Manually migrate data from source to destination AlloyDB for PostgreSQL cluster

If you detect discrepancies on tables without primary keys, you can synchronize the data using one of the following options:

  * **Option 1** : Manually compare data between the source database and the destination AlloyDB for PostgreSQL cluster using checksum queries or delta scripts, and execute appropriate SQL updates for divergent records.
  * **Option 2** : Run `pg_dump` and `pg_restore` specifically for the tables without primary keys during application maintenance cutover.
  * **Option 3** : Use the PostgreSQL `COPY` command to export and import table data. See the [PostgreSQL documentation](https://www.postgresql.org/docs/current/sql-copy.html) for more information.

**Note:** For **Option 2** and **Option 3** , if data was already migrated to the replica, truncate or clear existing records in those specific tables on the destination cluster before running `pg_restore` or `COPY` commands to avoid duplicate entries.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
