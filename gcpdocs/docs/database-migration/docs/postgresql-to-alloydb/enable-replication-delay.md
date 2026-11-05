---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/enable-replication-delay/
title: Enable replication delay monitoring for PostgreSQL versions earlier than 9.6 \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-05T11:11:15.230513+00:00
---

# Enable replication delay monitoring for PostgreSQL versions earlier than 9.6  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/enable-replication-delay/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview)



Send feedback 

#  Enable replication delay monitoring for PostgreSQL versions earlier than 9.6 Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable replication delay monitoring when you migrate from a source instance running PostgreSQL versions earlier than 9.6 to AlloyDB for PostgreSQL. For complete source database configuration instructions, see [ Configure source database](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-source-database).

For source instances running PostgreSQL versions earlier than 9.6, the replication delay metric isn't available by default because non-superusers can't access replication statistics in the `pg_stat_replication` view. You can use the following approaches if you want to monitor replication delay for such sources.

## Create a security definer function

The recommended option to track replication delay for sources running PostgreSQL versions earlier than 9.6 is to create a security definer function allowing Database Migration Service to query replication delay statistics. Follow these steps:

  1. Connect to your source database using a superuser account and define the `pg_stat_replication_user()` function: 
         
         CREATE OR REPLACE FUNCTION pg_stat_replication_user()
         RETURNS TABLE (
           pid               integer,
           usesysid          oid,
           username          name,
           application_name  text,
           client_addr       inet,
           client_hostname   text,
           client_port       integer,
           backend_start     timestamp with time zone,
           backend_xmin      xid,
           state             text,
           sent_location     pg_lsn,
           write_location    pg_lsn,
           flush_location    pg_lsn,
           replay_location   pg_lsn,
           sync_priority     integer,
           sync_state        text
         )
         LANGUAGE SQL
         SECURITY DEFINER
         AS $$
           SELECT * FROM pg_catalog.pg_stat_replication;
         $$;

  2. Revoke public execution rights from the function and grant execute permissions exclusively to your dedicated migration user account: 
         
         REVOKE EXECUTE ON FUNCTION pg_stat_replication_user() FROM public;
         GRANT EXECUTE ON FUNCTION pg_stat_replication_user() TO "MIGRATION_USER_ACCOUNT_NAME";




## For self-hosted instances: use SUPERUSER privileges

For self-hosted PostgreSQL instances, you can grant the `SUPERUSER` privilege directly to your dedicated migration user account:
    
    
    ALTER USER MIGRATION_USER_ACCOUNT_NAME WITH SUPERUSER;

**Note:** Granting superuser privileges directly to user accounts isn't supported for managed database offerings such as Cloud SQL for PostgreSQL, Amazon RDS, or Amazon Aurora.

## Monitor replication delay manually

You can also monitor replication delay manually on the source instance using the following query:

**Note:** When you use a direct query to monitor replication delay, Database Migration Service doesn't display replication delay metrics in the Google Cloud console or in API responses.
    
    
    SELECT current_timestamp, application_name,
      pg_xlog_location_diff(pg_current_xlog_location(), pg_stat_replication.sent_location) AS sent_location_lag,
      pg_xlog_location_diff(pg_current_xlog_location(), pg_stat_replication.write_location) AS write_location_lag,
      pg_xlog_location_diff(pg_current_xlog_location(), pg_stat_replication.flush_location) AS flush_location_lag,
      pg_xlog_location_diff(pg_current_xlog_location(), pg_stat_replication.replay_location) AS replay_location_lag
    FROM pg_stat_replication;

## What's next

  * For complete, step-by-step migration walkthroughs, see [ Get started with AlloyDB for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/get-started-with-alloydb-migrations).

  * To plan network connectivity between your source and destination instances, see [ Networking considerations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-considerations).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
