---
url: https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/
title: Migrate data to AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni for containers: 17.5.0 \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:53:59.765097+00:00
---

# Migrate data to AlloyDB Omni  |  AlloyDB Omni for containers: 17.5.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/

[ Skip to main content ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/)
  * [Deutsch](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/?hl=de)
  * [Español](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/?hl=es-419)
  * [Français](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/?hl=id)
  * [Italiano](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/?hl=it)
  * [Português](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/?hl=ja)
  * [한국어](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/alloydb-color.svg) ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/overview)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/overview)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [PostgreSQL to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/#migrate-postgres)
  * [Oracle to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/#migrate-oracle)


This page documents AlloyDB Omni version **17.5.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/overview)


Send feedback 
#  Migrate data to AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [PostgreSQL to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/#migrate-postgres)
  * [Oracle to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/#migrate-oracle)


Select a documentation version:  17.5.0keyboard_arrow_down
  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/migrate-data)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/migrate-data)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/migrate-data)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/migrate-data)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/migrate-data)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/migrate-data)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/migrate-data)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/migrate-data)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/migrate-data)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/migrate-data)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/migrate-data)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/migrate-data)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/migrate-data)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/migrate-data)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/migrate-data)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/migrate-data)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/migrate-data)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/migrate-data)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/migrate-data)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/migrate-data)

This page outlines the process to migrate data from PostgreSQL or Oracle to AlloyDB Omni. 
  * [PostgreSQL to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/#migrate-postgres)
  * [Oracle to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/migrate-data/#migrate-oracle)


## PostgreSQL to AlloyDB Omni
Use the following tools based on your migration complexity and downtime to migrate data from PostgreSQL to AlloyDB Omni:  
| Migration type  | Tool  |  
| --- | --- |  
| Simple migration with sufficient downtime  |  [pg_dump](https://www.postgresql.org/docs/16/app-pgdump.html) to backup the existing database and [pg_restore](https://www.postgresql.org/docs/16/app-pgrestore.html) to restore the backup to the new database.  |  
| Complex migration with sufficient downtime  |  [pgloader](https://pgloader.readthedocs.io/en/latest/) to stream data from the source to the destination.  |  
| Complex migration with minimal downtime  |  [pglogical](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/about-pglogical) to replicate data from the source to the destination.  |  
## Oracle to AlloyDB Omni
If you have sufficient downtime to move the volume of data in Oracle and convert all Oracle resident application logic to PostgreSQL, use [Ora2Pg](https://ora2pg.darold.net/) for schema conversion, data movement, and code conversion.
If you have minimal downtime for the migration, use the following tools:  
| To migrate  | Use  |  
| --- | --- |  
| Code and schema  |  [Google Cloud Database Migration Service](https://cloud.google.com/database-migration) to migrate the schema and code  
Ora2Pg for schema conversion, data movement, and code conversion  
Change Data Capture (CDC) tool as required to identify and captures data from, Oracle relational tables, and makes the change data available for use by applications.  |  
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
