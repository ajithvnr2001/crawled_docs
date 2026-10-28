---
url: https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration/
title: Verify a migration \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:10:37.758693+00:00
---

# Verify a migration  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration/

[ Skip to main content ](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration/)
  * [Deutsch](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration/?hl=de)
  * [Español](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration/?hl=es-419)
  * [Français](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration/?hl=id)
  * [Italiano](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration/?hl=it)
  * [Português](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration/?hl=ja)
  * [한국어](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)


[Start free](https://console.cloud.google.com/freetrial)
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview)


Send feedback 
#  Verify a migration Stay organized with collections  Save and categorize content based on your preferences.
This page describes how to confirm that your migrated data is complete and accurate. At a minimum, you should verify that your tables exist in the migrated Cloud SQL database instance.
  1. Connect to your Cloud SQL instance with a tool where you can run SQL commands against your migrated databases (for example, Cloud SQL Studio in the Google Cloud console or `psql`). 
For more information on connecting to Cloud SQL instances, see [ Connection options](https://docs.cloud.google.com/sql/docs/postgres/connect-overview#tools_for_connecting_to) in Cloud SQL documentation.
  2. Run SQL queries to verify your migrated data: List all databases
Run the following query to verify that your destination Cloud SQL instance contains all the source databases you migrated:

```
SELECT datname FROM pg_database
WHERE datistemplate = false;
```
List all tables in a database
Run the following query to list all user tables in your database:

```
SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_schema NOT IN ('pg_catalog', 'information_schema')
  AND table_type = 'BASE TABLE'
ORDER BY table_schema, table_name;
```
Check table column definitions and data types
Run the following query to verify the column names, data types, and nullability for a specific table:

```
SELECT
  column_name,
  data_type,
  character_maximum_length,
  is_nullable,
  column_default
FROM information_schema.columns
WHERE table_name = 'TABLE_NAME'
ORDER BY ordinal_position;
```
Check table row counts and sample data
Run the following queries to verify row counts and inspect sample rows in a specific table:
    1. Verify the total row count: 
```
SELECT COUNT(*) FROM TABLE_NAME;
```

    2. View a sample of migrated records: 
```
SELECT * FROM TABLE_NAME LIMIT 10;
```

Verify primary keys and constraints
Run the following query to verify that primary keys, foreign keys, and unique constraints were created correctly:

```
SELECT
  table_schema,
  table_name,
  constraint_name,
  constraint_type
FROM information_schema.table_constraints
WHERE table_schema NOT IN ('pg_catalog', 'information_schema')
ORDER BY table_schema, table_name, constraint_type;
```
Verify indexes
Run the following query to verify that indexes were created on your migrated tables:

```
SELECT
  schemaname,
  tablename,
  indexname,
  indexdef
FROM pg_indexes
WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
ORDER BY schemaname, tablename, indexname;
```
Verify sequences
Run the following query to verify that sequences exist in your migrated database:

```
SELECT
  sequence_schema,
  sequence_name,
  data_type
FROM information_schema.sequences
ORDER BY sequence_schema, sequence_name;
```

  3. Compare the results of these queries with your source database to ensure that all objects, row counts, and schema structures match.


If everything you check is as you expect, then Database Migration Service has migrated the data correctly.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
