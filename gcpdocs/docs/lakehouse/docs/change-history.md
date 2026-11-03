---
url: https://docs.cloud.google.com/lakehouse/docs/change-history/
title: Work with change history \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T05:44:09.820107+00:00
---

# Work with change history  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/change-history/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Work with change history Stay organized with collections  Save and categorize content based on your preferences. 

Change history lets you track the history of rows appended to [Apache Iceberg managed tables (formerly BigLake tables for Apache Iceberg in BigQuery)](https://docs.cloud.google.com/bigquery/docs/biglake-iceberg-tables-in-bigquery). You can use the GoogleSQL [`APPENDS`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/time-series-functions#appends) table-valued function (TVF) to view all rows appended to a table during a specified time range, such as rows added through `CREATE TABLE` DDL statements, `INSERT` and `MERGE` DML statements, batch load jobs, and streaming ingestion.

Apache Iceberg managed tables use [BigQuery change history concepts and capabilities](https://docs.cloud.google.com/bigquery/docs/change-history) to let you process incremental additions made to your tables. Understanding what rows have been appended to a table can help you incrementally maintain a table replica outside of BigQuery, audit historical data additions, or trigger downstream pipelines without requiring full table scans or costly copies.

## Required permissions

To view the change history on an Apache Iceberg managed table, you need the following permissions:

  * The `bigquery.tables.getData` permission on the table. This permission is included in the following predefined Identity and Access Management (IAM) roles: 
    * `roles/bigquery.dataViewer`
    * `roles/bigquery.dataEditor`
    * `roles/bigquery.dataOwner`
    * `roles/bigquery.admin`
  * The `bigquery.connections.delegate` permission on the Google Cloud resource connection associated with the table. This permission is included in the [BigQuery Connection User (`roles/bigquery.connectionUser`)](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.connectionUser) role.
  * In addition, the service account associated with the Google Cloud resource connection must have the [`roles/storage.objectUser`](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#storage.objectUser) and `roles/storage.legacyBucketReader` roles on the underlying Cloud Storage bucket.



For additional permission requirements when a table uses row-level or column-level security, see [Required permissions](https://docs.cloud.google.com/bigquery/docs/change-history#required_permissions) in the BigQuery change history documentation.

## Limitations

Apache Iceberg managed tables support change history, and leverage the same concepts and capabilities as standard BigQuery change history. When working with change history on Apache Iceberg managed tables, the following limitations apply:

  * Change history is only supported for [Apache Iceberg managed tables (formerly BigLake tables for Apache Iceberg in BigQuery)](https://docs.cloud.google.com/bigquery/docs/biglake-iceberg-tables-in-bigquery).
  * The [`CHANGES` table-valued function (TVF)](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/time-series-functions#changes) isn't supported for Apache Iceberg managed tables. Only the [`APPENDS`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/time-series-functions#appends) TVF is supported.
  * The [limitations for Apache Iceberg managed tables](https://docs.cloud.google.com/bigquery/docs/biglake-iceberg-tables-in-bigquery#limitations) also apply.
  * The limitations for the [`APPENDS`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/time-series-functions#appends) change history function also apply.



## What's next

For more information, see the following BigQuery documentation:

  * [Work with change history](https://docs.cloud.google.com/bigquery/docs/change-history)
  * [`APPENDS` TVF reference](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/time-series-functions#appends)
  * [Create and use Apache Iceberg managed tables](https://docs.cloud.google.com/bigquery/docs/biglake-iceberg-tables-in-bigquery)
  * [Learn how to use a BigQuery continuous query to read real-time data from Apache Iceberg managed tables](https://docs.cloud.google.com/bigquery/docs/continuous-queries)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-02 UTC."],[],[]] 
