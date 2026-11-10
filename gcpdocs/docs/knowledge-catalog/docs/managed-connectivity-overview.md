---
url: https://docs.cloud.google.com/knowledge-catalog/docs/managed-connectivity-overview/
title: Managed connectivity overview \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:46:18.489157+00:00
---

# Managed connectivity overview  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/managed-connectivity-overview/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Managed connectivity overview Stay organized with collections  Save and categorize content based on your preferences. 

Managed connectivity pipelines let you extract and import metadata at scale from third-party data sources into Knowledge Catalog (formerly Dataplex Universal Catalog) by using custom connectors and Workflows. You can run these pipelines on demand or on a recurring schedule to keep your catalog synchronized and discover, search, and govern external assets in one place.

## How managed connectivity works

The following diagram shows a managed connectivity pipeline.

![A managed connectivity pipeline.](https://docs.cloud.google.com/static/knowledge-catalog/images/managed-connectivity-diagram.png)

At a high level, here's how managed connectivity works:

  1. You [build a custom connector](https://docs.cloud.google.com/knowledge-catalog/docs/develop-custom-connector) to extract metadata from various third-party data sources, including MySQL, SQL Server, Oracle, Snowflake, and Databricks. Alternatively, you can use community-contributed custom connectors for a wider range of sources.

The connector must be an Artifact Registry image that can run on Managed Service for Apache Spark.

  2. You [run the managed connectivity pipeline](https://docs.cloud.google.com/knowledge-catalog/docs/import-using-workflows-custom-source) in Workflows, an orchestration platform. 

  3. The managed connectivity pipeline performs the following actions:

     1. Creates a target Knowledge Catalog entry group in your Google Cloud project based on your configuration, if the entry group doesn't exist.
     2. Runs the connector. The connector extracts the metadata from your data source and generates a metadata import file that can be imported into Knowledge Catalog.
     3. Monitors the progress of the metadata extraction.
     4. Runs a metadata import job to import the metadata into Knowledge Catalog.
     5. Monitors the progress of the metadata import job.



The managed connectivity pipeline uses Managed Service for Apache Spark to run the connector, and Knowledge Catalog metadata import API methods to run the metadata import job.

The metadata that you import consists of Knowledge Catalog entries and their aspects. For more information about Knowledge Catalog metadata, see [About metadata management in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview).

## Community-contributed custom connectors

To import metadata from third-party sources, you can use custom connectors that are contributed by the community. See each connector's README file for setup instructions and more information about the connector.

**Note:** These connectors are not officially supported by Google.Data source | Repository  
---|---  
AWS Glue Data Catalog | [aws-glue-connector](https://github.com/GoogleCloudPlatform/cloud-dataplex/tree/main/managed-connectivity/community-contributed-connectors/aws-glue-connector)  
Databricks Unity Catalog | [databricks-connector](https://github.com/GoogleCloudPlatform/cloud-dataplex/tree/main/managed-connectivity/community-contributed-connectors/databricks-connector)  
MySQL | [mysql-connector](https://github.com/GoogleCloudPlatform/cloud-dataplex/tree/main/managed-connectivity/community-contributed-connectors/mysql-connector)  
Oracle | [oracle-connector](https://github.com/GoogleCloudPlatform/cloud-dataplex/tree/main/managed-connectivity/community-contributed-connectors/oracle-connector)  
PostgreSQL | [postgresql-connector](https://github.com/GoogleCloudPlatform/cloud-dataplex/tree/main/managed-connectivity/community-contributed-connectors/postgresql-connector)  
Snowflake | [snowflake-connector](https://github.com/GoogleCloudPlatform/cloud-dataplex/tree/main/managed-connectivity/community-contributed-connectors/snowflake-connector)  
Snowflake Horizon Catalog | [snowflake-horizon-connector](https://github.com/GoogleCloudPlatform/cloud-dataplex/tree/main/managed-connectivity/community-contributed-connectors/snowflake-horizon-connector)  
SQL Server | [sql-server-connector](https://github.com/GoogleCloudPlatform/cloud-dataplex/tree/main/managed-connectivity/community-contributed-connectors/sql-server-connector)  
  
## What's next

  * [Import metadata from a custom source using Workflows](https://docs.cloud.google.com/knowledge-catalog/docs/import-using-workflows-custom-source)
  * [Develop a custom connector for metadata import](https://docs.cloud.google.com/knowledge-catalog/docs/develop-custom-connector)
  * [Import metadata using a custom pipeline](https://docs.cloud.google.com/knowledge-catalog/docs/import-metadata)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
