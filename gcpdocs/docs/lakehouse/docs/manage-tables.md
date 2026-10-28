---
url: https://docs.cloud.google.com/lakehouse/docs/manage-tables/
title: Overview of Apache Iceberg tables \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:57:37.573252+00:00
---

# Overview of Apache Iceberg tables  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/manage-tables/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Overview of Apache Iceberg tables Stay organized with collections  Save and categorize content based on your preferences. 

Apache Iceberg tables managed by the [Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/about-lakehouse-catalogs) and served through the [Apache Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog) let you work with open and interoperable data that adheres to the [open source Apache Iceberg Table specification](https://iceberg.apache.org/spec/). You can read and write these tables by using BigQuery or any Iceberg-compatible processing engine.

This document refers to these tables as _managed Apache Iceberg tables_ or _Iceberg tables_. To compare table types, see [Compare table types](https://docs.cloud.google.com/lakehouse/docs/lakehouse-tables).

## Table options

You can opt in and enable the following capabilities by [configuring table options](https://docs.cloud.google.com/lakehouse/docs/table-options):

  1. **Read/write interoperability (Preview)** : Seamless read and write support for multiple engines, including BigQuery, Managed service for Apache Spark, Iceberg-compatible engines such as open source engines (Apache Spark, Apache Flink, and Trino), and third-party engines (such as Snowflake).
  2. **Automatic table management (Preview)** : Automatic table management (storage optimization) such as compaction and garbage collection.



In addition to the preceding capabilities, the following capabilities are also supported by default for Apache Iceberg tables managed by Lakehouse:

  1. **BigQuery Data definition language (Preview)** : You can also create or update Iceberg tables by using BigQuery DDL statements (for example, `CREATE TABLE`, `ALTER TABLE`, and `DROP TABLE`), in addition to creating or updating tables by using Iceberg-compatible engines such as Spark, Flink, and Trino. After the tables are created, they are available for reads and writes in those engines and in BigQuery, and are part of the same catalog and namespace construct, managed by the Lakehouse runtime catalog.
  2. **Credential vending support for BigQuery** : BigQuery supports using [credential vending](https://docs.cloud.google.com/lakehouse/docs/credential-vending) for authentication when reading or writing Iceberg tables in the Lakehouse runtime catalog. You can set credential vending at the catalog level.



## Management actions

You can perform the following management actions on your Apache Iceberg tables:

  * **[Create a table](https://docs.cloud.google.com/lakehouse/docs/create-table):** Create an Apache Iceberg table within a catalog namespace using the Google Cloud console, Spark, Trino, gcloud, BigQuery (Preview), or the Iceberg REST Catalog API (`CreateIcebergTable`).
  * **[Register a table](https://docs.cloud.google.com/lakehouse/docs/register-table):** Register an existing Apache Iceberg table within a catalog namespace using gcloud or the Iceberg REST Catalog API (`RegisterIcebergTable`).
  * **[List tables](https://docs.cloud.google.com/lakehouse/docs/list-tables):** View table identifiers within a namespace using the Google Cloud console, Spark, Trino, gcloud, BigQuery (Preview), or the Iceberg REST Catalog API (`ListIcebergTableIdentifiers`).
  * **[Get table details](https://docs.cloud.google.com/lakehouse/docs/get-table-details):** Inspect table schema, properties, and credentials using the Google Cloud console, Spark, Trino, gcloud, BigQuery (Preview), or the Iceberg REST Catalog API (`GetIcebergTable`, `LoadIcebergTableCredentials`).
  * **[Insert data](https://docs.cloud.google.com/lakehouse/docs/insert-data):** Append data rows to your Iceberg tables using Spark, Trino, or BigQuery (Preview).
  * **[Query a table](https://docs.cloud.google.com/lakehouse/docs/query-table):** Execute queries against your Iceberg tables from Spark, Trino, or BigQuery using four-part table naming.
  * **[Modify data with DML](https://docs.cloud.google.com/lakehouse/docs/modify-data-dml):** Update, delete, or merge data rows in your Iceberg tables using DML statements from BigQuery (Preview), Spark, or Trino.
  * **[Alter a table](https://docs.cloud.google.com/lakehouse/docs/alter-table):** Evolve table schema and update metadata properties using the Google Cloud console, Spark, Trino, gcloud, BigQuery (Preview), or the Iceberg REST Catalog API (`UpdateIcebergTable`).
  * **[Configure table options](https://docs.cloud.google.com/lakehouse/docs/table-options):** Configure properties to enable BigQuery (Preview) DML and automatic table management.
  * **[Manage table ACLs](https://docs.cloud.google.com/lakehouse/docs/manage-tables-acl#apply-acl-tables):** View and update IAM policies on your Iceberg tables to control access for specific principals (`get-iam-policy`, `set-iam-policy`).
  * **[Upgrade Iceberg V1 tables to V2](https://docs.cloud.google.com/lakehouse/docs/update-tables):** Upgrade your existing Iceberg V1 tables to the supported V2 format.
  * **[Use Binary Deletion Vectors in Iceberg V3 tables](https://docs.cloud.google.com/lakehouse/docs/use-iceberg-v3-binary-deletion-vectors):** Enable binary deletion vectors for optimized deletion performance in Iceberg V3 tables.
  * **[Delete a table](https://docs.cloud.google.com/lakehouse/docs/delete-table):** Drop a table registration from the catalog without purging underlying storage files using the Google Cloud console, Spark, Trino, gcloud, BigQuery (Preview), or the Iceberg REST Catalog API (`DeleteIcebergTable`).



## What's next

  * See [Set up the Apache Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/set-up-lakehouse-iceberg-rest-catalog).
  * Learn how to [query a table](https://docs.cloud.google.com/lakehouse/docs/query-table).
  * Learn how to [manage table ACLs](https://docs.cloud.google.com/lakehouse/docs/manage-tables-acl#apply-acl-tables).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
