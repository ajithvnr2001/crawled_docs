---
url: https://docs.cloud.google.com/alloydb/docs/access-iceberg-data-from-alloydb/
title: Access Iceberg data from AlloyDB \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T10:16:11.787212+00:00
---

# Access Iceberg data from AlloyDB  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/access-iceberg-data-from-alloydb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Access Iceberg data from AlloyDB Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Direct Iceberg access**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Direct Iceberg access in AlloyDB for PostgreSQL lets you query data stored in [Apache Iceberg](https://iceberg.apache.org/) table format in Cloud Storage from your AlloyDB instance. You can access Iceberg datasets using [Cloud Storage](https://docs.cloud.google.com/storage/docs/overview) bucket URIs or using the [Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/about-lakehouse-catalogs). To accelerate analytical workloads, AlloyDB provides a built-in [columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/about) that optimizes scans, joins, and aggregations. By integrating with the columnar engine, direct Iceberg access lets you run high-performance analytical queries on your data lakehouse without building, managing, or maintaining complex extract, transform, and load (ETL) data pipelines.

You can query Iceberg tables using standard SQL commands, join Iceberg datasets with operational tables in AlloyDB, and populate Iceberg tables into the in-memory columnar engine for accelerated query performance.

## Benefits

Direct Iceberg access provides the following benefits:

  * Zero-ETL lakehouse access: query external Iceberg datasets in place without copying or moving data into separate analytical systems.
  * Unified transactional and analytical queries: join live, operational data stored in AlloyDB heap tables with massive historical data stored in Iceberg tables on Cloud Storage.
  * Flexible catalog integration: access Iceberg table metadata from Cloud Storage bucket paths or through Lakehouse runtime catalog.
  * Columnar query acceleration: cache and populate Iceberg tables into the AlloyDB columnar engine memory for sub-second analytical processing.
  * Standard SQL interface: use familiar PostgreSQL syntax to query and analyze Iceberg tables.



## How direct Iceberg access works

Direct Iceberg access uses the PostgreSQL Table Access Method (TAM) interface (`USING iceberg`) and integrates with the AlloyDB columnar engine planner and execution framework.

When you query an Iceberg table, AlloyDB operates in one of the following modes:

  * Direct scan (for streaming reads): AlloyDB reads the latest metadata and data files directly from Cloud Storage. The columnar engine processes the data in a streaming fashion.
  * Columnar engine acceleration (for in-memory cached reads): when you populate an Iceberg table into the AlloyDB columnar engine using the `google_columnar_engine_add()` function, the table is loaded into the columnar store in memory. Subsequent queries read from the columnar engine memory, maximizing query throughput and minimizing latency.



### Snapshot serving and cache refresh

The Iceberg table snapshot that AlloyDB queries depends on the read mode:

  * Direct scan: AlloyDB runs queries at the latest Iceberg snapshot. When a query starts, AlloyDB determines the latest available Iceberg table snapshot and reads data from that snapshot, even within a `REPEATABLE READ` or `SERIALIZABLE` transaction. AlloyDB doesn't support snapshot pinning and point-in-time queries across transactions.

For example, when you query a table using direct scan, each statement in a transaction reads from the latest available snapshot:
        
        BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
        SELECT * FROM customer_orders;
        -- If an external process commits a new Iceberg snapshot:
        SELECT * FROM customer_orders; -- Returns results from the new snapshot.
        COMMIT;
        

  * Columnar engine acceleration: AlloyDB runs queries at the snapshot that is populated in the columnar engine. If AlloyDB writes new data to the underlying Iceberg table in Cloud Storage after population, the underlying Iceberg table in Cloud Storage after population, queries might return stale data. To get up-to-date data after DML operations on the underlying table, refresh the cache using the `google_columnar_engine_refresh()` function.




## Supported data types

When you define an Iceberg table in AlloyDB, the column names and data types in your DDL statement must match the types in the underlying Iceberg schema.

Direct Iceberg access supports the following Apache Iceberg data types and their corresponding AlloyDB types:

Apache Iceberg data type | AlloyDB data type | Description  
---|---|---  
`boolean` | `BOOLEAN` | Vectorized conversion to byte-packed format  
`int` | `INT` / `INTEGER` | 32-bit signed integer  
`long` | `BIGINT` | 64-bit signed integer  
`float` | `REAL` / `FLOAT4` | 32-bit single-precision floating point  
`double` | `DOUBLE PRECISION` / `FLOAT8` | 64-bit double-precision floating point  
`decimal(P, S)` | `NUMERIC(P, S)` / `DECIMAL(P, S)` | Fixed-point numeric value with precision `P` and scale `S`  
`string` | `TEXT` / `VARCHAR` | UTF-8 string values  
`date` | `DATE` | Calendar date (year, month, day)  
`timestamp` | `TIMESTAMP` | Timestamp without time zone  
`timestamptz` | `TIMESTAMPTZ` | Timestamp with time zone  
  
## Limitations

Direct Iceberg access has the following limitations:

  * PostgreSQL version availability: AlloyDB supports direct Iceberg access on PostgreSQL 18 and later.
  * User permissions: only database users with the [`alloydbsuperuser`](https://docs.cloud.google.com/alloydb/docs/database-users/overview#alloydbsuperuser) role can create Iceberg tables. After a table is created, you can grant `SELECT` permissions to other users to query the Iceberg table.
  * Read-only operations: AlloyDB supports only `SELECT` queries (DQL) on Iceberg tables. It doesn't support write operations (`INSERT`, `UPDATE`, `DELETE`, `TRUNCATE`).
  * Apache Iceberg specification version: AlloyDB doesn't support Iceberg v2 delete files (positional and equality deletes) or Iceberg v3 deletion vectors.
  * File format support: direct Iceberg access supports Parquet data files, and JSON and Avro metadata files. It doesn't support ORC data files.
  * Snapshot versioning: direct scan queries run at the latest Iceberg table snapshot, and columnar-accelerated queries run at the populated snapshot. AlloyDB doesn't support point-in-time queries.
  * Schema evolution: AlloyDB doesn't support `ALTER TABLE` operations on Iceberg tables. The underlying Iceberg table must not have undergone a schema migration.
  * Metadata catalog support: direct Iceberg access supports direct Cloud Storage bucket paths (`gs://`) and Lakehouse runtime catalog paths (`bl://`). For Lakehouse runtime catalog, AlloyDB supports only end-user credentials mode. It doesn't support credential vending mode or other REST catalogs.
  * Requester Pays buckets: AlloyDB doesn't support Cloud Storage buckets that use [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays).
  * Full population constraint: AlloyDB doesn't support partial columnar population for Iceberg tables. Tables must fit into the columnar engine memory or SSD space.
  * Population heap memory: populating an Iceberg table that contains large Parquet row groups might exceed the per-worker population heap memory limit, especially on instances with fewer vCPUs. To resolve this issue, see Columnar engine population heap is full.



## Before you begin

Before you create and query Iceberg tables, make sure that you complete the following:

  1. Create an AlloyDB cluster running **PostgreSQL 18 or later** on Google Cloud. For more information, see [Create a cluster](https://docs.cloud.google.com/alloydb/docs/cluster-create).
  2. Host an Apache Iceberg table in Cloud Storage or registered in Lakehouse runtime catalog: 
     * For Cloud Storage paths, the bucket directory structure must follow the standard Apache Iceberg layout containing `data/` and `metadata/` subdirectories, including metadata JSON files and `version-hint.text`. For more information, see [Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
     * For Lakehouse runtime catalog, create and register your Iceberg catalog in end-user credentials mode. For more information, see [Set up the Apache Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/set-up-lakehouse-iceberg-rest-catalog).
  3. Set up database credentials for a user with the `alloydbsuperuser` role. For more information, see [`alloydbsuperuser` group role](https://docs.cloud.google.com/alloydb/docs/database-users/overview#alloydbsuperuser).



### Required roles

To enable AlloyDB to read Iceberg data and metadata, you must grant the required IAM roles to the AlloyDB cluster service account:

  * **Cloud Storage access** : grant the Storage Object Viewer ([`roles/storage.objectViewer`](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)) role on the Cloud Storage bucket containing your Iceberg data and metadata.
  * **BigLake access** (if using Lakehouse runtime catalog): grant the BigLake Viewer ([`roles/biglake.viewer`](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer)) role on the project hosting your BigLake catalog.



To find the cluster service account, run the [`gcloud beta alloydb clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/clusters/describe) command:
    
    
    gcloud beta alloydb clusters describe CLUSTER_ID --region=REGION_ID

Replace the following:

  * `CLUSTER_ID`: the AlloyDB cluster ID.
  * `REGION_ID`: the location of the AlloyDB cluster. For example, `us-east1`. For a full list of regions, see [AlloyDB locations](https://docs.cloud.google.com/alloydb/docs/locations).



The output contains a `serviceAccountEmail` field, which is the service account for this cluster. In the Google Cloud console, you can find the service account on the **Cluster overview** page.

To grant the Storage Object Viewer role using gcloud CLI, run:
    
    
    gcloud storage buckets add-iam-policy-binding \
        gs://BUCKET_NAME \
        --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
        --role="roles/storage.objectViewer"

If you use Lakehouse runtime catalog, grant the BigLake Viewer role:
    
    
    gcloud projects add-iam-policy-binding LAKEHOUSE_PROJECT_ID \
        --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
        --role="roles/biglake.viewer"

Replace the following:

  * `BUCKET_NAME`: the name of your Cloud Storage bucket.
  * `LAKEHOUSE_PROJECT_ID`: the Google Cloud project ID where your Lakehouse runtime catalog is hosted.
  * `SERVICE_ACCOUNT_EMAIL`: the cluster service account email that you found in the `serviceAccountEmail` field.



### Configure database flags

To enable the columnar engine and direct Iceberg access, you can configure database flags on your AlloyDB instance. Set the following database flags on your instance:

Database flag | Value | Description  
---|---|---  
`google_columnar_engine.enabled` | `on` | Enables the AlloyDB columnar engine.  
`google_columnar_engine.enable_iceberg_reads` | `on` | Enables direct Iceberg access. Requires an instance restart.  
`google_columnar_engine.memory_size_in_mb` | SIZE_IN_MB | (Optional) Allocates memory to the columnar engine. Recommended if you plan to populate Iceberg tables in memory.  
  
To configure these flags using gcloud CLI, run the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command:
    
    
    gcloud alloydb instances update INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --database-flags=google_columnar_engine.enabled=on,google_columnar_engine.enable_iceberg_reads=on

Replace the following:

  * `INSTANCE_ID`: the ID of your AlloyDB instance.
  * `CLUSTER_ID`: the ID of your AlloyDB cluster.
  * `REGION_ID`: the region ID of your AlloyDB cluster.



## Create an Iceberg table in AlloyDB

To expose an Apache Iceberg dataset in AlloyDB, connect as a user with `alloydbsuperuser` privileges. Then, create a table using the `USING iceberg` table access method.
    
    
    CREATE TABLE TABLE_NAME (
        COLUMN_NAME DATA_TYPE [, ...]
    )
    USING iceberg
    WITH (
        uri = 'LOCATION_URI'
    );
    

Replace the following:

  * `TABLE_NAME`: the name of the table to create in AlloyDB.
  * `COLUMN_NAME` and `DATA_TYPE`: the column definitions. Column names and types must match the schema of the underlying Iceberg table.
  * `LOCATION_URI`: the location of the Iceberg table metadata. Specify one of the following formats: 
    * Direct Cloud Storage path: `gs://BUCKET_NAME/PATH_TO_ICEBERG_TABLE`
    * Lakehouse runtime catalog URI: `bl://projects/PROJECT_ID/catalogs/CATALOG_NAME/databases/DATABASE_NAME/tables/TABLE_NAME`



### Examples

The following examples show you how to create Iceberg tables in AlloyDB.

#### Create a table from a Cloud Storage path

The following example creates a table named `customer_orders` backed by an Iceberg dataset located in a Cloud Storage bucket:
    
    
    CREATE TABLE customer_orders (
        order_id BIGINT,
        customer_id INT,
        order_status TEXT,
        total_amount DOUBLE PRECISION,
        order_date DATE,
        is_completed BOOLEAN
    )
    USING iceberg
    WITH (
        uri = 'gs://my-iceberg-analytics-bucket/datasets/sales/customer_orders'
    );
    

#### Create a table from Lakehouse runtime catalog

The following example creates a table referencing an Iceberg table managed by Lakehouse runtime catalog:
    
    
    CREATE TABLE customer_orders (
        order_id BIGINT,
        customer_id INT,
        order_status TEXT,
        total_amount DOUBLE PRECISION,
        order_date DATE,
        is_completed BOOLEAN
    )
    USING iceberg
    WITH (
        uri = 'bl://projects/my-analytics-project/catalogs/sales_catalog/databases/retail_db/tables/customer_orders'
    );
    

## Query Iceberg data

After you create the table in AlloyDB, you can query it using standard SQL `SELECT` statements with `alloydbsuperuser` privileges. Optionally, you can grant read permissions to a user without `alloydbsuperuser` privileges by using the `GRANT` statement. For example, `GRANT SELECT ON customer_orders TO normal_user`.

### Query data

The following example shows you how to run a query:
    
    
    SELECT
        customer_id,
        COUNT(order_id) AS total_orders,
        SUM(total_amount) AS total_spent
    FROM customer_orders
    WHERE is_completed = true
      AND order_date >= '2026-01-01'
    GROUP BY customer_id
    ORDER BY total_spent DESC
    LIMIT 10;
    

### Query joint Iceberg data with operational data

You can combine real-time operational data residing in AlloyDB with historical data residing in Iceberg:
    
    
    SELECT
        c.customer_name,
        c.account_tier,
        COUNT(o.order_id) AS total_orders,
        SUM(o.total_amount) AS historical_spend
    FROM customer_orders o
    JOIN customers c ON o.customer_id = c.customer_id
    WHERE o.is_completed = true
    GROUP BY c.customer_name, c.account_tier
    ORDER BY historical_spend DESC;
    

### Import data into a local table

To create an independent, writable copy of the Iceberg data in local AlloyDB storage, execute `CREATE TABLE ... AS SELECT`, as shown in the following example:
    
    
    CREATE TABLE local_customer_orders AS
    SELECT * FROM customer_orders
    WHERE order_date >= '2026-01-01';
    

## Accelerate queries using the columnar engine

For analytical workloads requiring ultra-low latency, you can populate the Iceberg table directly into the AlloyDB columnar engine memory.

### Populate Iceberg table into the columnar store

To populate all columns of an Iceberg table into the AlloyDB columnar engine, use the `google_columnar_engine_add()` function. For example:
    
    
    SELECT google_columnar_engine_add('customer_orders');
    

To populate only specific columns that your queries use, pass a comma-separated list of column names as the second argument. For example:
    
    
    SELECT google_columnar_engine_add('customer_orders', 'customer_id,order_status');
    

For more information, see [Add columns using SQL functions](https://docs.cloud.google.com/alloydb/docs/columnar-engine/manage-content-manually#by-function).

### Refresh populated data

If you write new snapshots to the underlying Iceberg dataset, refresh the table to reload the latest data into the columnar engine so that queries return up-to-date results:
    
    
    SELECT google_columnar_engine_refresh('customer_orders');
    

### Remove a table from the columnar store

To remove an Iceberg table from the columnar store and revert to direct scanning:
    
    
    SELECT google_columnar_engine_drop('customer_orders');
    

## Monitor and verify query execution

You can monitor how AlloyDB executes queries against Iceberg tables and verify whether queries use the in-memory columnar engine. Use system views to check cache population status, and use `EXPLAIN` to inspect query execution plans.

### Verify columnar caching status

To verify whether an Iceberg table is populated in the columnar engine, query the `g_columnar_relations` system view:
    
    
    SELECT relation_name, status
    FROM g_columnar_relations
    WHERE relation_name = 'customer_orders';
    

A `status` value of `USABLE` confirms that the table is cached in columnar engine memory.

### Inspect query execution plans with `EXPLAIN`

To verify whether a query leverages the columnar engine, use the `EXPLAIN` statement:
    
    
    EXPLAIN (ANALYZE, COSTS OFF)
    SELECT SUM(total_amount)
    FROM customer_orders
    WHERE is_completed = true;
    

The output indicates columnar execution through a `Custom Scan (ColumnarScan)` node on the table:
    
    
    Custom Scan (ColumnarScan) on customer_orders
      Filter: (is_completed = true)
    

## Troubleshooting

This section describes how to resolve common issues when you configure and query Iceberg tables in AlloyDB.

### `google_columnar_engine.enable_iceberg_reads` flag is disabled

Cause: The database flag for direct Iceberg access is disabled.

Recommended fix: set the database flags `google_columnar_engine.enabled=on` and `google_columnar_engine.enable_iceberg_reads=on` in your instance, and restart the instance.

### Permission denied accessing Cloud Storage

Cause: The AlloyDB cluster service account lacks read access to the Cloud Storage bucket.

Recommended fix: grant the `roles/storage.objectViewer` role to the cluster service account on the bucket.

### Permission denied accessing Lakehouse runtime catalog

Cause: The AlloyDB cluster service account lacks read access to the Lakehouse runtime catalog.

Recommended fix: grant the `roles/biglake.viewer` role to the cluster service account on the Google Cloud project hosting the Lakehouse runtime catalog.

### Columnar population fails

Cause: The Iceberg table size exceeds the available memory and SSD space in the columnar engine.

Recommended fix: increase the memory allocated to the columnar engine using the `google_columnar_engine.memory_size_in_mb` flag on your instance, or increase the columnar engine storage cache size using the `google_columnar_engine.storage_cache_size` flag. For more information, see [Configure storage cache for the columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/configure#configure-storage-cache).

### Columnar engine population heap is full

Error message:
    
    
    ERROR: Columnar engine population heap is full during population. Set
    google_columnar_engine.population_heap_size_in_mb to a bigger value.
    

Cause: The memory required to populate a large Parquet row group exceeds the per-worker population heap limit.

Recommended fix: reduce the number of parallel population workers so that the population process can use a larger heap. In the SQL session where you populate the table, set the [`google_job_scheduler.max_parallel_workers_per_job`](https://docs.cloud.google.com/alloydb/docs/reference/columnar-engine-flags#max-parallel-workers-per-job) flag to `0` before calling the `google_columnar_engine_add()` function:
    
    
    SET google_job_scheduler.max_parallel_workers_per_job = 0;
    SELECT google_columnar_engine_add('TABLE_NAME');
    

Replace `TABLE_NAME` with the name of the Iceberg table in AlloyDB.

## What's next

  * Learn about the [AlloyDB columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/about).
  * Learn how to [configure the columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/configure).
  * [Choose how to access BigQuery data from AlloyDB](https://docs.cloud.google.com/alloydb/docs/choose-access-bigquery-data-from-alloydb).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
