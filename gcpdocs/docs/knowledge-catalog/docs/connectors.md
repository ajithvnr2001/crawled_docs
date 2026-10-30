---
url: https://docs.cloud.google.com/knowledge-catalog/docs/connectors/
title: About metadata connectors \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:40:17.440395+00:00
---

# About metadata connectors  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/connectors/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  About metadata connectors Stay organized with collections  Save and categorize content based on your preferences. 

As data landscapes grow more complex, metadata can become siloed across different platforms, making it difficult for teams to find, trust, and manage their data. Knowledge Catalog (formerly Dataplex Universal Catalog) connectors help solve this by letting you automatically import technical, operational, business, and semantic metadata from third-party data sources directly into Google Cloud.

Through these connectors, you can let analysts search external data assets without switching tools, let data stewards enforce centralized governance across a multi-cloud environment, and monitor cross-platform data quality in one place. By scheduling recurring runs, you can keep your catalog synchronized with your source systems so that your teams have an accurate, up-to-date view of your data ecosystem.

## Supported data sources

You can import metadata from the following sources using Knowledge Catalog connectors:

  * Databricks Unity Catalog
  * dbt Core and Cloud
  * MySQL
  * Oracle
  * PostgreSQL
  * Snowflake Horizon
  * SQL Server

**Note:** If you want to run SQL queries or Spark jobs against remote Databricks or Snowflake catalogs, use a [Lakehouse cross-cloud connection](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access). Use Knowledge Catalog connectors to copy Databricks or Snowflake metadata into Google Cloud and centrally govern it alongside other automatically ingested and imported metadata.

### Integrations with data governance partners

You can also integrate Knowledge Catalog with other data cataloging and governance platforms. Instead of pulling from raw data sources, these integrations let parallel catalog tools share information. You can enrich metadata within Knowledge Catalog or export Knowledge Catalog metadata to view it within those third-party tools.

The following partners provide integrations for Knowledge Catalog:

  * [AbInitio](https://www.abinitio.com/events/google-metadata-connector)
  * [Anomalo](https://engage.anomalo.com/google-dataplex-connector)
  * [Atlan](https://docs.atlan.com/apps/connectors/data-governance/knowledge-catalog)
  * [Collibra](https://productresources.collibra.com/docs/collibra/latest/Content/Catalog/GCS/to_gcp.htm)
  * [Datahub](https://docs.datahub.com/docs/automations/knowledge-catalog-metadata-sync)



The remainder of this page describes importing metadata through connectors. For more information about partner integrations, see the linked partner pages.

## How it works

Knowledge Catalog connectors use prebuilt integrations to connect to your data sources and automatically extract metadata. [BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/dts-introduction) manages these transfers and maps the extracted metadata to a specific Knowledge Catalog entry group that you choose.

The connectors extract the following types of metadata:

  * **Technical metadata** : Schema, data type, and column name definitions.
  * **Operational metadata** : Created and modified timestamps, lineage, usage statistics, and data quality results.
  * **Business metadata** : Tags, owners, and annotations.
  * **Semantic metadata** : Dimensions, measures, metrics, golden queries, and relationships.



After you configure a connector, Knowledge Catalog schedules metadata import runs on the schedule that you specify, ensuring that the catalog stays synchronized with the source system. Each time a metadata import run occurs, it performs a **full overwrite** of the entries in the destination entry group managed by that configuration. Metadata objects that are no longer present in the source are removed from the entry group, and new objects are added. Objects in the entry group that aren't imported by the connector configuration are unaffected.

## Terminology

The following terms are used in this documentation:

  * **Metadata import configuration** : The settings for a scheduled or on-demand task that uses BigQuery Data Transfer Service to extract metadata from a source and load it into Knowledge Catalog.
  * **Run** : A single execution instance of a metadata import configuration.
  * **Entry group** : A resource in Knowledge Catalog that contains metadata entries. When you configure a connector, you designate an entry group as the destination for the imported metadata.
  * **Entry** : A resource in Knowledge Catalog that represents a data asset, such as a table or view.



## Pricing

There are no additional charges from Knowledge Catalog or BigQuery Data Transfer Service for importing metadata using connectors.

Standard charges apply for other Knowledge Catalog usage (such as metadata storage). For more information, see [Knowledge Catalog pricing](https://cloud.google.com/products/knowledge-catalog/pricing).

## Limitations

  * Only metadata is imported, not the underlying data from the source tables or views. To transfer the underlying data, you can use the [BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/dts-introduction).
  * Each run performs a full overwrite of connector-managed entries in the destination entry group. Incremental metadata updates are not supported.
  * Run history is retained for 90 days.



## What's next

  * Learn how to [Import metadata from Databricks Unity Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/databricks-unity-transfer).
  * Learn how to [Import metadata from dbt Core and Cloud](https://docs.cloud.google.com/knowledge-catalog/docs/dbt-transfer).
  * Learn how to [Import metadata from MySQL](https://docs.cloud.google.com/knowledge-catalog/docs/mysql-transfer).
  * Learn how to [Import metadata from Oracle](https://docs.cloud.google.com/knowledge-catalog/docs/oracle-transfer).
  * Learn how to [Import metadata from PostgreSQL](https://docs.cloud.google.com/knowledge-catalog/docs/postgresql-transfer).
  * Learn how to [Import metadata from Snowflake Horizon](https://docs.cloud.google.com/knowledge-catalog/docs/snowflake-horizon-transfer).
  * Learn how to [Import metadata from SQL Server](https://docs.cloud.google.com/knowledge-catalog/docs/sql-server-transfer).
  * Learn how to [Manage connector configurations](https://docs.cloud.google.com/knowledge-catalog/docs/manage-connector-jobs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
