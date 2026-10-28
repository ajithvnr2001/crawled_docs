---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/
title: Supported source and destination databases \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:12:05.706022+00:00
---

# Supported source and destination databases  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/

[ Skip to main content ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/)
  * [Deutsch](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/?hl=de)
  * [Español](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/?hl=es-419)
  * [Français](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/?hl=id)
  * [Italiano](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/?hl=it)
  * [Português](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/?hl=ja)
  * [한국어](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fdatabase-migration%2Fdocs%2Fpostgresql-to-alloydb%2Fmigration-src-and-dest%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Overview](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/#overview)
    * [Supported source databases](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/#supported-source-databases)
    * [Supported destination databases](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/#supported_destination_databases)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest)


Was this helpful?
Send feedback 
#  Supported source and destination databases Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Overview](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/#overview)
    * [Supported source databases](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/#supported-source-databases)
    * [Supported destination databases](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest/#supported_destination_databases)


  

[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/migration-src-and-dest) | [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/migration-src-and-dest) | PostgreSQL to AlloyDB
  

## Overview
Database Migration Service supports continuous migrations from source databases to AlloyDB for PostgreSQL.
### Supported source databases
  * Amazon RDS 9.6.10+, 10.5+, 11.1+, 12, 13, 14, 15, 16, 17
  * Amazon Aurora 10.11+, 11.6+, 12.4+, 13.3+, 14, 15, 16, 17
  * Self-managed PostgreSQL (on premises or on any cloud VM that you fully control) 9.4, 9.5, 9.6, 10, 11, 12, 13, 14, 15, 16, 17
  * Cloud SQL 9.6, 10, 11, 12, 13, 14, 15, 16, 17


There are several schemas that can't be migrated. See [ Known limitations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations) for more information about these schemas.
### Supported destination databases
  * AlloyDB for PostgreSQL 14, 15, 16, 17, 18


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
