---
url: https://docs.cloud.google.com/lakehouse/docs/use-catalog-federation/
title: Query BigQuery tables through the Apache Iceberg REST catalog endpoint \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T09:59:51.907339+00:00
---

# Query BigQuery tables through the Apache Iceberg REST catalog endpoint  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/use-catalog-federation/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)



Send feedback 

#  Query BigQuery tables through the Apache Iceberg REST catalog endpoint Stay organized with collections  Save and categorize content based on your preferences. 

**Warning:** For most workloads, we recommend using [Lakehouse runtime catalogs](https://docs.cloud.google.com/lakehouse/docs/about-lakehouse-catalogs) instead of routing requests directly to the BigQuery catalog.

_Lakehouse_ provides interoperability with BigQuery by routing requests through the Apache Iceberg REST catalog endpoint to the BigQuery catalog. This capability lets you expose tables managed by BigQuery, for example Iceberg managed tables, to external open source (OSS) engines such as Apache Spark and Trino.

Instead of creating a dedicated Lakehouse catalog container to store metadata, the Apache Iceberg REST catalog endpoint acts purely as a proxy gateway. When external engines connect using the `bq://` warehouse prefix, the gateway routes their catalog requests directly to BigQuery's internal catalog. This lets you create and manage tables directly within BigQuery using standard BigQuery DDL or APIs, while giving external OSS engines read-only access to query those tables through the REST catalog endpoint.

## How querying BigQuery tables through the REST catalog endpoint works

Routing requests to the BigQuery catalog lets you expose BigQuery tables—such as Iceberg managed tables and BigQuery metastore tables—through the Lakehouse runtime catalog Apache Iceberg REST catalog endpoint.

The workflow operates as follows:

  1. **Create a table in the BigQuery catalog** : You create an Iceberg managed table in BigQuery using [DDL statements](https://docs.cloud.google.com/bigquery/docs/biglake-iceberg-tables-in-bigquery#create-iceberg-tables). This table exists in the BigQuery catalog, is governed by BigQuery access control lists (ACLs), and functions as a BigQuery REST resource.
  2. **Federate into the BigQuery warehouse from the Lakehouse runtime catalog** : Using the Lakehouse runtime catalog Apache Iceberg REST API, you federate into a warehouse specified by the `bq://projects/PROJECT_ID` warehouse path format (or the regional version, `bq://projects/PROJECT_ID/locations/LOCATION`). This lets you access the BigQuery table from compute engines like Apache Spark through the Apache Iceberg REST Catalog API. In this configuration, you get a read-only experience from Spark, but a read-write experience from BigQuery.



### Considerations

  * Because routing requests to the BigQuery catalog does not create a dedicated Lakehouse catalog resource, other catalog-level concepts and configurations—such as the resource hierarchy, bucket and catalog regions, and the four-part P.C.N.T naming structure—do not apply to this method. In the underlying API, this corresponds to the `CATALOG_TYPE_BIGQUERY` configuration. Storage access delegation (credential vending) isn't supported when routing requests to the BigQuery catalog.

  * Exposing BigQuery tables through the REST catalog endpoint is distinct from accessing cross-cloud data. While this workflow exposes Google Cloud tables to external OSS engines, Lakehouse connects Google Cloud to remote external catalogs, such as Databricks Unity Catalog, to query data stored in other cloud providers directly from BigQuery and OSS engines without migrating data. For more information about that workflow, see [About cross-cloud data access](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access).




### Comparison with tables managed by the Apache Iceberg REST catalog endpoint

Exposing BigQuery tables through the REST catalog endpoint differs from workflows where the Lakehouse runtime catalog uses the [Apache Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/set-up-lakehouse-iceberg-rest-catalog) in the following ways:

  * **Resource management and catalog storage** : Tables in the BigQuery catalog reside there as BigQuery REST resources, and the Lakehouse runtime catalog acts as a proxy gateway. When the Lakehouse runtime catalog uses the Apache Iceberg REST catalog endpoint to manage tables directly, those tables are stored as Lakehouse REST resources.
  * **Access control** : Tables in the BigQuery catalog use BigQuery IAM permissions and access control lists (ACLs). Tables managed directly in the Lakehouse runtime catalog use Lakehouse ACLs.
  * **Engine read and write capabilities** : Iceberg managed tables provide read-write access through BigQuery, and read-only access from external engines such as Spark. Tables managed directly in the Lakehouse runtime catalog through the Apache Iceberg REST catalog endpoint support read-write operations from both BigQuery and external engines such as Spark.



## Before you begin

  1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)




### Required roles

To get the permissions that you need to query BigQuery tables through the Apache Iceberg REST catalog endpoint, ask your administrator to grant you the following IAM roles: 

  * Read catalog resources and query table data: 
    * [BigLake Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`) on the project
    * [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) on the Cloud Storage bucket
  * Create namespaces or modify external-engine-created tables: 
    * [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`) on the project
    * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) on the Cloud Storage bucket



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

If you use external query engines such as Managed Service for Apache Spark to create namespaces or modify tables created from external engines, grant these roles to the service account that runs jobs in that engine (Iceberg managed tables are read-only from external engines).

## Configure your client for the BigQuery warehouse

To connect to the BigQuery warehouse, configure your client (such as Apache Spark or Trino) with the `bq://projects/PROJECT_ID` warehouse format in the `WAREHOUSE_PATH` field in the client configuration examples in [Configure client application](https://docs.cloud.google.com/lakehouse/docs/set-up-lakehouse-iceberg-rest-catalog#configure-catalog).

You can also choose to include a BigQuery location to restrict future requests to a single location using the `bq://projects/PROJECT_ID/locations/LOCATION` format.

Because these resources are managed by BigQuery, you must have the applicable [required permissions](https://docs.cloud.google.com/bigquery/docs/biglake-iceberg-tables-in-bigquery#required-roles).

### Create namespaces in the BigQuery warehouse

After you configure your client, you can create a namespace for your tables.

###  Spark 

To create a namespace in the BigQuery warehouse, include the `LOCATION` and `DBPROPERTIES` clauses:
    
    
    spark.sql("CREATE NAMESPACE IF NOT EXISTS NAMESPACE_NAME LOCATION 'gs://BUCKET_NAME/NAMESPACE_NAME' WITH DBPROPERTIES ('gcp-region' = 'LOCATION');")
    spark.sql("USE NAMESPACE_NAME;")

Replace the following:

  * `NAMESPACE_NAME`: a name for your namespace.
  * `BUCKET_NAME`: the Cloud Storage bucket that you're using with your catalog.
  * `LOCATION`: a [BigQuery location](https://docs.cloud.google.com/bigquery/docs/locations). The default value is the `US` multi-region.



###  Trino 

To create a schema in the BigQuery warehouse, include the `LOCATION` and `gcp-region` properties:
    
    
    CREATE SCHEMA IF NOT EXISTS  CATALOG_NAME.SCHEMA_NAME WITH ( LOCATION = 'gs://BUCKET_NAME/SCHEMA_NAME', "gcp-region" = 'LOCATION');
    USE CATALOG_NAME.SCHEMA_NAME;

Replace the following:

  * `CATALOG_NAME`: the name of your Trino catalog using the Apache Iceberg REST catalog endpoint.
  * `SCHEMA_NAME`: a name for your schema.
  * `BUCKET_NAME`: the Cloud Storage bucket that you're using with your catalog.
  * `LOCATION`: a [BigQuery location](https://docs.cloud.google.com/bigquery/docs/locations). The default value is the `US` multi-region.



## Query tables in BigQuery

Tables that you create in the BigQuery warehouse are visible in BigQuery and can be queried directly using standard BigQuery SQL (without needing a four-part P.C.N.T name):
    
    
    SELECT * FROM `NAMESPACE_NAME.TABLE_NAME`;

Replace the following:

  * `NAMESPACE_NAME`: the name of your namespace.
  * `TABLE_NAME`: the name of your table.



## What's next

  * Learn how to [manage catalogs in the Google Cloud console](https://docs.cloud.google.com/lakehouse/docs/manage-catalogs).
  * Learn about [Apache Iceberg tables supported by the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/lakehouse-catalog-tables).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
