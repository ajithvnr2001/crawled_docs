---
url: https://docs.cloud.google.com/lakehouse/docs/key-concepts/
title: Key concepts \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:49:32.985354+00:00
---

# Key concepts  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/key-concepts/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Key concepts Stay organized with collections  Save and categorize content based on your preferences. 

Understanding core borderless Lakehouse terminology helps you evaluate lakehouse architectures and configure catalogs, tables, query engines, and governance on Google Cloud. Each entry defines a key concept used throughout the Lakehouse documentation and links to detailed guides. For an end-to-end view of how these components fit together, see [How borderless Lakehouse works](https://docs.cloud.google.com/lakehouse/docs/lakehouse-basics).

## Lakehouse fundamentals

The following concepts form the foundation of Google Cloud's Lakehouse architecture.

### Data lakehouse

A data lakehouse brings together the cost savings and flexibility of a data lake with the data management and performance of a data warehouse. It lets you store data in open formats on Cloud Storage and use BigQuery features, such as precise security controls and fast queries.

### Medallion architecture

A common design pattern in a data lakehouse is the medallion architecture, which logically organizes data into progressive layers of structure and quality:

  * **Bronze (raw) layer:** Ingests and stores raw data in open formats such as Apache Iceberg on Cloud Storage.
  * **Silver (cleansed) layer:** Cleanses, filters, and enriches the raw data into standardized tables.
  * **Gold (curated) layer:** Delivers fully curated, aggregated business-level tables. BigQuery is often used to serve the gold layer for high-performance consumption, reporting, and analytics.



### Open interoperability

Open interoperability is the ability for multiple analytical and transactional systems—such as BigQuery, Apache Spark, Apache Flink, and Trino—to operate on a single copy of data in open formats such as Apache Iceberg. This eliminates the need for data duplication and provides a consistent view of data across tools.

### Lakehouse runtime catalog

The _Lakehouse runtime catalog_ is a centralized, serverless metadata service that acts as the single source of truth for Google Cloud's Lakehouse. It lets multiple engines, such as Apache Spark, Apache Flink, Trino, and BigQuery, discover and query the same tables simultaneously. Engines connect to it through catalog endpoints. For more information, see [About the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/about-lakehouse-catalogs).

## Resource hierarchy

The Lakehouse runtime catalog organizes metadata in a hierarchy that aligns with Apache Iceberg standards and maps logical identities to physical storage paths.

### Catalog

A catalog is the top-level logical container in the Lakehouse runtime catalog. It defines where table data can be stored and which region serves its metadata. For more information, see [Create a catalog](https://docs.cloud.google.com/lakehouse/docs/create-catalog).

#### Catalog types

When you create a catalog, you choose between two storage models:

  * **Multiple-bucket catalog (recommended):** Lets you name your catalog independently and configure a default storage location (`default_location`) and up to 128 additional Cloud Storage buckets or subpaths in `restricted_locations`. When configuring client query engines (such as Spark or Trino), set the warehouse path to `bl://projects/PROJECT_ID/catalogs/CATALOG_ID`.
  * **Single-bucket catalog:** A legacy configuration where the catalog is locked to a single Cloud Storage bucket and inherits the bucket's name. When configuring client query engines, set the warehouse path to `gs://CLOUD_STORAGE_BUCKET_NAME`.



For more information, see [Catalogs and storage locations](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint#warehouse-storage-locations).

### Namespace

A namespace is a logical grouping of tables within a catalog. For users familiar with BigQuery, a namespace is functionally similar to a _dataset_. Namespaces inherit the region of their parent catalog and don't support nesting.

### Table

A table is the entity that points to data in Cloud Storage. For Apache Iceberg tables, the table metadata contains the schema, partitioning information, and a pointer to the current table state through a `metadata.json` file. For the table types that Lakehouse supports, see Table types.

### P.C.N.T naming convention

The P.C.N.T naming convention is the four-part convention used to uniquely identify and query tables in the Lakehouse runtime catalog from BigQuery. It stands for **Project.Catalog.Namespace.Table** :

  * **Project** : The Google Cloud project ID.
  * **Catalog** : The name of the catalog in the Lakehouse runtime catalog.
  * **Namespace** : The logical grouping for tables (similar to a dataset).
  * **Table** : The name of the data table.



## Catalog endpoints

A catalog endpoint is a protocol interface that query engines use to connect to the Lakehouse runtime catalog. The endpoint you use determines which table formats and engines you can work with.

### Apache Iceberg REST catalog endpoint

The Apache Iceberg REST catalog endpoint implements the open standard [Iceberg REST Catalog API](https://iceberg.apache.org/rest-catalog-spec/). It's the recommended endpoint for new workloads and provides read and write interoperability between open source engines and BigQuery. It supports multiple-bucket catalogs, credential vending, and cross-region replication (Preview). For more information, see the [Apache Iceberg REST catalog endpoint overview](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint).

### Apache Hive catalog endpoint

The Apache Hive catalog endpoint provides compatibility for open source workloads that depend on the Apache Hive metastore (HMS) interface. Because the Lakehouse runtime catalog serves this endpoint, you can run Apache Hive or Spark workloads without maintaining a self-hosted Hive metastore. The endpoint manages standard Hive and Spark tables rather than Apache Iceberg tables, and supports customer-managed encryption keys (CMEK) for data in Cloud Storage. For more information, see [About the Hive catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/about-spark-hive-metastore).

### Custom Apache Iceberg catalog for BigQuery

The custom Apache Iceberg catalog for BigQuery is an earlier integration that uses a catalog plugin (`BigQueryMetastoreCatalog`) to let open source engines store Apache Iceberg table definitions in BigQuery. Namespaces map to BigQuery datasets, so you query these tables with standard BigQuery dataset syntax. For new workloads, use the Apache Iceberg REST catalog endpoint instead. For more information, see [Custom Apache Iceberg catalog for BigQuery](https://docs.cloud.google.com/lakehouse/docs/about-custom-iceberg-catalog-endpoint).

## Table types

Google Cloud's Lakehouse supports several table types, depending on the engine used to manage the data and the catalog endpoint you use. For a detailed comparison, see [Compare table types](https://docs.cloud.google.com/lakehouse/docs/lakehouse-tables).

### Apache Iceberg tables in the Lakehouse runtime catalog

These are Apache Iceberg tables that the Lakehouse runtime catalog manages and serves through the Apache Iceberg REST catalog endpoint, with data stored in Cloud Storage. Open source engines have read and write access to these tables. BigQuery has read access, and write access (Preview) when you enable BigQuery DML. This is the recommended option for most open lakehouse workloads. For more information, see [Manage Apache Iceberg tables](https://docs.cloud.google.com/lakehouse/docs/manage-tables).

### Apache Hive tables

These are standard Apache Hive and Spark tables, in formats such as Parquet, ORC, Avro, and Delta Lake, that the Lakehouse runtime catalog manages through the Apache Hive catalog endpoint. Open source engines have read and write access, and BigQuery has read-only access. To use Delta Lake tables, you create them with a Delta-compatible engine such as Apache Spark and register them in the metastore. For more information, see [Supported storage formats and types](https://docs.cloud.google.com/lakehouse/docs/spark-hive-formats-types).

### BigQuery tables

These tables are managed with BigQuery.

#### Apache Iceberg managed tables

These are Apache Iceberg tables that you create from BigQuery and store in Cloud Storage. BigQuery handles all data layout and optimization. While multiple engines can read these tables, BigQuery is the only engine that can directly write to them. These tables are distinct from Apache Iceberg tables in the Lakehouse runtime catalog. For more information, see [Apache Iceberg managed tables](https://docs.cloud.google.com/bigquery/docs/biglake-iceberg-tables-in-bigquery).

#### Native tables

These tables are managed by BigQuery and store data in BigQuery storage. You can connect these tables to the Lakehouse runtime catalog.

#### External tables

External tables reside outside of the Lakehouse runtime catalog. Their data and metadata are self-managed in storage such as Cloud Storage, Amazon S3, or Azure Blob Storage, and BigQuery accesses them through connections. BigQuery can only read from these tables.

## Table features and options

The following features apply to Apache Iceberg tables in the Lakehouse runtime catalog unless otherwise noted.

### Apache Iceberg table versions

The Lakehouse runtime catalog supports Apache Iceberg V2 tables and V3 tables ([Preview](https://cloud.google.com/products#product-launch-stages)). V3 tables support binary deletion vectors, which let you delete specific rows without rewriting entire data files. Iceberg V1 tables aren't supported; you must [upgrade them to V2](https://docs.cloud.google.com/lakehouse/docs/update-tables) first. For more information, see [Use binary deletion vectors in Iceberg V3 tables](https://docs.cloud.google.com/lakehouse/docs/use-iceberg-v3-binary-deletion-vectors).

### Table evolution

Table evolution lets you change a table's schema or partition spec over time without rewriting the table data or recreating the table. Apache Iceberg tables in the Lakehouse runtime catalog also support [flexible column names](https://docs.cloud.google.com/bigquery/docs/schemas#flexible-column-names) by default, so column names can contain characters such as spaces and international characters.

### Time travel

Time travel lets you query a table's data as it existed at a specific point in time or snapshot ID. This is useful for auditing, reproducing experiments, or restoring data after an accidental deletion. Open source engines can time travel within the retention configured in table properties, while BigQuery time travel is limited to seven days.

### Table options

Table options are table properties that turn on Google-managed capabilities for individual Apache Iceberg tables. For more information, see [Configure table options](https://docs.cloud.google.com/lakehouse/docs/table-options).

#### BigQuery DML

BigQuery DML is in [Preview](https://cloud.google.com/products#product-launch-stages). When you set the `gcp.biglake.bigquery-dml.enabled` table property, BigQuery can create, alter, and modify the table by using GoogleSQL DDL and DML statements (`INSERT`, `UPDATE`, `DELETE`, and `MERGE`), while open source engines continue to read and write the same table.

#### Table management

Table management ([Preview](https://cloud.google.com/products#product-launch-stages)) automates storage maintenance for Apache Iceberg tables. When you set the `gcp.biglake.table-management.enabled` table property, Lakehouse runs background compaction (coalesce), snapshot expiration, and garbage collection to maintain query performance and storage efficiency. Table management requires the catalog to use credential vending. For more information, see [Enable table management](https://docs.cloud.google.com/lakehouse/docs/table-options#enable-table-management).

### Change history

Change history lets you use the GoogleSQL `APPENDS` table-valued function to track rows appended to Apache Iceberg managed tables over a specified time range. You can use it to incrementally maintain replicas, audit data additions, or trigger downstream pipelines without full table scans. For more information, see [Work with change history](https://docs.cloud.google.com/lakehouse/docs/change-history).

### Metadata caching

Metadata caching accelerates query performance for BigQuery external tables. It stores a copy of the table's metadata in BigQuery storage, reducing the need to read metadata files from Cloud Storage during query execution.

## Data ingestion and migration

Lakehouse provides several paths for loading data into Apache Iceberg tables and moving metadata from existing metastores.

### Batch table imports

Dataflow job builder templates let you import existing [Apache Iceberg](https://docs.cloud.google.com/lakehouse/docs/import-iceberg-tables), [Delta Lake tables](https://docs.cloud.google.com/lakehouse/docs/import-delta-lake-tables), and [Parquet files](https://docs.cloud.google.com/lakehouse/docs/import-parquet-tables) into Apache Iceberg tables managed by Lakehouse without writing code.

### Streaming ingestion

You can stream data into Apache Iceberg tables by using open source engines (such as Spark or Kafka), Dataflow, or the [BigQuery Storage Write API (gRPC)](https://docs.cloud.google.com/lakehouse/docs/bigquery-storage-api), which provides transactional, exactly-once writes. You can also write the output of [BigQuery continuous queries](https://docs.cloud.google.com/bigquery/docs/continuous-queries-introduction) directly into Apache Iceberg managed tables.

### Change data capture (CDC)

CDC ingestion keeps Apache Iceberg tables synchronized with source systems by applying inserts, updates, and deletes instead of reloading full tables. Apache Iceberg managed tables support [BigQuery CDC ingestion](https://docs.cloud.google.com/lakehouse/docs/change-data-capture) (Preview), and you can use Dataflow to migrate CDC logs from [Apache Iceberg](https://docs.cloud.google.com/lakehouse/docs/migrate-iceberg-cdc) and [Delta Lake](https://docs.cloud.google.com/lakehouse/docs/migrate-delta-lake-cdc) tables (Preview).

### Metastore migration

Metastore migration moves table metadata from existing metastores into the Lakehouse runtime catalog without copying data files. You can run a one-time migration or dry run from [Dataproc Metastore](https://docs.cloud.google.com/lakehouse/docs/migrate-dataproc-metastore) to the Apache Iceberg REST catalog endpoint or the Apache Hive catalog endpoint, or migrate from [external metastores](https://docs.cloud.google.com/lakehouse/docs/external-metastore-migration) such as Hive metastore (Preview).

## Cross-cloud data access

Cross-cloud data access lets you query data stored in other clouds and SaaS platforms directly from Google Cloud, without migrating files or building ETL pipelines. For more information, see [About cross-cloud data access](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access).

### Federated catalog

A federated catalog is a catalog in the Lakehouse runtime catalog that connects to a remote catalog provider and exposes its tables through the Apache Iceberg REST catalog endpoint. You can then query those tables with BigQuery, Managed Service for Apache Spark, or Apache Spark. Supported remote catalog providers include Databricks Unity Catalog, AWS Glue Data Catalog, Snowflake Horizon Catalog, Workday Data Lake, and SAP Business Data Cloud (SAP BDC). For more information, see [Query remote data](https://docs.cloud.google.com/lakehouse/docs/query-remote-data).

### Background metadata refresh

Background metadata refresh is the process by which a federated catalog periodically synchronizes namespace and table metadata from the remote catalog, based on a refresh interval. Lakehouse authenticates to the remote catalog by using OIDC token federation or credentials stored in Secret Manager.

### Cross-cloud transport

Cross-cloud data access separates background metadata refresh from query data transport. You can route either or both over the public internet or privately over Cross-Cloud Interconnect to meet security and cost requirements. To restrict data exfiltration, you can also protect federated catalog endpoints with [VPC Service Controls](https://docs.cloud.google.com/lakehouse/docs/vpc-sc-federated-catalogs).

### Cross-cloud caching

Cross-cloud caching stores file blocks read from remote object storage locally in the Google Cloud region where queries run, so repeated queries read from the cache instead of the remote cloud. Caching helps reduce cross-cloud egress costs and is disabled by default; you opt in on a federated catalog or a BigQuery cross-cloud connection. For more information, see [Intelligent caching](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access#intelligent-caching).

### Identity mode

Identity mode determines which identity runs queries against a remote catalog:

  * **Service identity (default):** Background metadata refresh and queries run as the catalog's service account.
  * **User identity federation:** Queries run as the end user's identity, which lets the remote catalog enforce its own permissions and attribute audit logs to individual users. This mode is supported for [Databricks Unity Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-databricks#configure-user-identity-federation).



### SAP BDC integration

The SAP BDC integration works in two directions. Federation synchronizes SAP BDC shares into Lakehouse by using the Delta Sharing protocol so you can query them from BigQuery. Publishing shares Apache Iceberg tables or Knowledge Catalog data products with SAP BDC without migrating data. For more information, see [About SAP BDC integration](https://docs.cloud.google.com/lakehouse/docs/sap-bdc-overview).

### Public datasets

Borderless Lakehouse hosts public datasets served through the Apache Iceberg REST catalog endpoint, providing read-only access for exploration and testing without managing infrastructure. Google pays for storage, and you pay only for the queries that you run. For more information, see [Public datasets](https://docs.cloud.google.com/lakehouse/docs/public-datasets).

## Security and governance

Lakehouse combines Identity and Access Management (IAM), storage access delegation, and network controls to secure your lakehouse.

### Resource-level access control

IAM policies on catalogs, namespaces, and tables control who can view and modify Lakehouse resources. For more information, see [Manage catalog, namespace, and table ACLs](https://docs.cloud.google.com/lakehouse/docs/manage-tables-acl) and [Roles and permissions](https://docs.cloud.google.com/lakehouse/docs/iam-roles).

### Credential vending

Credential vending is a security mechanism that tightens access control when using the Lakehouse runtime catalog. Instead of granting users direct bucket permissions, the Apache Iceberg REST catalog endpoint vends short-lived, downscoped storage credentials with access restricted to the specific table paths that a query needs. Credential vending is also required for table management. For more information, see [Credential vending](https://docs.cloud.google.com/lakehouse/docs/credential-vending).

### Connections

A connection is a BigQuery resource that stores credentials for accessing external data. In Google Cloud's Lakehouse, connections delegate access to Cloud Storage by letting the connection's service account access the storage bucket on your behalf.

### VPC Service Controls

VPC Service Controls service perimeters help prevent data exfiltration by restricting access to the Lakehouse API (`biglake.googleapis.com`) and the Cloud Storage buckets that store table data. For more information, see [Use VPC Service Controls with credential vending](https://docs.cloud.google.com/lakehouse/docs/credential-vending#vpc-sc).

### Regional endpoints

Regional endpoints restrict requests so that they proceed only if the target catalog resource exists in the location specified by the endpoint, which helps you meet data residency requirements. For more information, see [Regional endpoints](https://docs.cloud.google.com/lakehouse/docs/regional-endpoints).

### Audit logging

Cloud Audit Logs record administrative and data access activity on Lakehouse resources. For more information, see [View audit logs](https://docs.cloud.google.com/lakehouse/docs/view-audit-logs).

### Unified governance

Unified governance lets you define and enforce security and data management policies centrally through integration with [Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/introduction). When you register tables in the Lakehouse runtime catalog, the system automatically registers corresponding entries in Knowledge Catalog, enabling search and discovery, data lineage, data profiling, and AI-generated [data insights](https://docs.cloud.google.com/lakehouse/docs/dataplex-insights-support) (Preview) across engines without moving or copying files.

## Query engines and tools

Google Cloud's Lakehouse decouples storage from compute, so various analytics engines can work with the same open tables.

### Open source engines

Open source engines connect to the Lakehouse runtime catalog through the Apache Iceberg REST catalog endpoint by using standard Apache Iceberg client configuration. For engine-specific setup, see [Apache Spark](https://docs.cloud.google.com/lakehouse/docs/spark-support), [Apache Flink](https://docs.cloud.google.com/lakehouse/docs/flink-support), and [Trino](https://docs.cloud.google.com/lakehouse/docs/trino-support). You can also manage Lakehouse resources with [Terraform](https://docs.cloud.google.com/lakehouse/docs/terraform-support).

### Managed Service for Apache Spark

Managed Service for Apache Spark (formerly Dataproc Serverless) provides a fully managed runtime for processing open table formats like Apache Iceberg. It supports two primary modes of execution:

  * **Serverless batches:** Designed for automated, non-interactive data processing pipelines and ETL workloads. This pay-per-execution model eliminates cluster management, removes resource contention between jobs, and automates infrastructure maintenance.
  * **Serverless interactive sessions:** Designed for exploratory data analysis, data engineering, and data science experimentation. Interactive sessions power Apache Spark notebooks using Spark Connect or remote Spark kernels, providing an autoscaling environment with no infrastructure setup.



#### Service tiers

When you run Apache Spark workloads on Managed Service for Apache Spark, you can select between service tiers:

  * **Standard tier:** The default execution tier suitable for standard batch processing workloads.
  * **Premium tier:** Provides advanced capabilities, including support for serverless interactive notebook sessions and performance-accelerating features such as the Lightning Engine.



#### Session templates

Session templates simplify the configuration of serverless interactive sessions. They let administrators define and persist common environment settings (such as catalog properties, network configurations, and runtime versions), which promotes consistency and minimizes repeated setup. You can create and manage session templates by using the Google Cloud console, the `gcloud` CLI, the REST API, or Terraform.

### conversational analytics

[conversational analytics](https://docs.cloud.google.com/lakehouse/docs/conversational-analytics) (Preview) lets you query tables in the Lakehouse runtime catalog, including cross-cloud sources, by using natural language prompts in BigQuery.

## Reliability

The Lakehouse runtime catalog provides managed disaster recovery for catalogs that use the Apache Iceberg REST catalog endpoint (Preview). For more information, see [About cross-region replication and disaster recovery](https://docs.cloud.google.com/lakehouse/docs/about-managed-disaster-recovery).

### Cross-region replication

Cross-region replication copies catalog metadata from a primary region to a secondary region when the catalog uses a dual-region or multi-region Cloud Storage bucket, which keeps the catalog available during regional outages. Cloud Storage replicates the underlying table data.

### Failover

Failover switches the primary and secondary regions for a catalog and all of its namespaces and tables. A _soft failover_ waits for all data to synchronize before the new primary accepts writes, which prevents data loss and suits planned testing. A _hard failover_ prioritizes availability and lets the new primary take over even if the previous primary is unreachable.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
