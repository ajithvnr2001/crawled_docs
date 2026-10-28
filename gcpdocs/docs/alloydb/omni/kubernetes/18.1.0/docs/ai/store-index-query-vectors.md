---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/
title: Create indexes and query vectors \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:46:40.236475+00:00
---

# Create indexes and query vectors  |  AlloyDB Omni using the container orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/

[ Skip to main content ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?resource=scann#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/)
  * [Deutsch](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?hl=es-419)
  * [Français](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?hl=id)
  * [Italiano](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?hl=ja)
  * [한국어](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Falloydb%2Fomni%2Fkubernetes%2F18.1.0%2Fdocs%2Fai%2Fstore-index-query-vectors%2F%3Fresource%3Dscann&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/alloydb-color.svg) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?resource=scann#before-you-begin)
  * [Create an index](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?resource=scann#create-index)
    * [Create a ScaNN index](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?resource=scann#create-scann-index)
    * [Analyze your indexed table](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?resource=scann#analyze-indexed-table)
    * [Build indexes in parallel](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?resource=scann#build-index-parallel)
  * [Run a query](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?resource=scann#query)
  * [What's next](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?resource=scann#whats-next)


This page documents AlloyDB Omni version **18.1.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview)


Was this helpful?
Send feedback 
#  Create indexes and query vectors Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?resource=scann#before-you-begin)
  * [Create an index](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?resource=scann#create-index)
    * [Create a ScaNN index](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?resource=scann#create-scann-index)
    * [Analyze your indexed table](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?resource=scann#analyze-indexed-table)
    * [Build indexes in parallel](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?resource=scann#build-index-parallel)
  * [Run a query](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?resource=scann#query)
  * [What's next](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?resource=scann#whats-next)


Select a documentation version:  18.1.0keyboard_arrow_down
  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/store-index-query-vectors)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/ai/store-index-query-vectors)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/ai/store-index-query-vectors)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/ai/store-index-query-vectors)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/ai/store-index-query-vectors)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/store-index-query-vectors)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/ai/store-index-query-vectors)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/ai/store-index-query-vectors)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/ai/store-index-query-vectors)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/ai/store-index-query-vectors)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/ai/store-index-query-vectors)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/ai/store-index-query-vectors)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/ai/store-index-query-vectors)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/ai/store-index-query-vectors)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/ai/store-index-query-vectors)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/store-index-query-vectors)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/ai/store-index-query-vectors)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/ai/store-index-query-vectors)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/ai/store-index-query-vectors)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/ai/store-index-query-vectors)


This document shows you how to use stored embeddings to generate indexes and query embeddings. For more information about storing embedding, see [Store vector embeddings](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-embeddings).
You can create `ScaNN`, `IVF`, `IVFFlat`, and `HNSW` indexes with AlloyDB.
## Before you begin
Before you can start creating indexes, you must complete the following prerequisites.
  * [Embedding vectors are added to a table](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-embeddings) in your AlloyDB database.
  * The `vector` extension version `0.5.0` or later that is based on `pgvector`, extended by Google for AlloyDB is installed.

```
CREATE EXTENSION IF NOT EXISTS vector;

```

  * To generate `ScaNN` indexes, install the `alloydb_scann` extension in addition to the `vector` extension.

```
CREATE EXTENSION IF NOT EXISTS alloydb_scann;

```



## Create an index
You can create one of the following index types for tables in your database.
ScaNN IVF IVFFlat HNSW
### Create a `ScaNN` index
AlloyDB `alloydb_scann`, a PostgreSQL extension developed by Google that implements a highly efficient nearest-neighbor index powered by [the ScaNN algorithm](https://github.com/google-research/google-research/blob/master/scann/docs/algorithms.md).
The `ScaNN` index is a tree-based quantization index for approximate nearest neighbor search. It provides lower index building time and smaller memory footprint as compared to `HNSW`. In addition, it provides faster QPS in comparison to `HNSW` based on the workload.
#### Two-level tree `ScaNN` index
To apply a two-level tree index using the ScaNN algorithm to a column containing stored vector embeddings, run the following DDL query:

```
CREATE INDEX INDEX_NAME ON TABLE
  USING scann (EMBEDDING_COLUMN DISTANCE_FUNCTION)
  WITH (num_leaves=NUM_LEAVES_VALUE);

```

Replace the following:
  * `INDEX_NAME`: the name of the index you want to create—for example, `my-scann-index`. The index names are shared across your database. Ensure that each index name is unique to each table in your database.
  * `TABLE`: the table to add the index to.
  * `EMBEDDING_COLUMN`: the column that stores `vector` data.
  * `DISTANCE_FUNCTION`: the distance function to use with this index. Choose one of the following:
    * **L2 distance:** `l2`
    * **Dot product:** `dot_product`
    * **Cosine distance:** `cosine`
  * `NUM_LEAVES_VALUE`: the number of partitions to apply to this index. Set to any value between 1 and 100 million for PostgreSQL 17 and higher, or between 1 and 30 million for PostgreSQL 16 and lower. For more information about how to decide this value, see [Tune a `ScaNN` index](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/tune-indexes).


#### Three-level tree `ScaNN` index
To create a three-level tree index using the ScaNN algorithm to a column containing stored vector embeddings, run the following DDL query:

```
CREATE INDEX INDEX_NAME ON TABLE
  USING scann (EMBEDDING_COLUMN DISTANCE_FUNCTION)
  WITH (num_leaves=NUM_LEAVES_VALUE, max_num_levels = MAX_NUM_LEVELS);

```

Replace the following:
  * `MAX_NUM_LEVELS`: the maximum number of levels of the K-means clustering tree. Set to `1`(default) for two-level tree-based quantization and to `2` for three-level tree-based quantization.


After you create the index, you can run nearest-neighbor search queries that make use of the index by following the instructions in [Make a nearest-neighbor query with given text](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors/?resource=scann#query).
The index parameters must be set to strike a right balance between QPS and recall. For more information about tuning the `ScaNN` index, see [Tune a `ScaNN` index](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/tune-indexes).
To create this index on an embedding column that uses the `real[]` data type instead of `vector`, cast the column into the `vector` data type:

```
CREATE INDEX INDEX_NAME ON TABLE
  USING scann (CAST(EMBEDDING_COLUMN AS vector(DIMENSIONS)) DISTANCE_FUNCTION)
  WITH (num_leaves=NUM_LEAVES_VALUE, max_num_levels = MAX_NUM_LEVELS);

```

Replace `DIMENSIONS` with the dimensional width of the embedding column. For more information about how to find the dimensions, see the `vector_dims` function in [Vector functions](https://github.com/pgvector/pgvector?tab=readme-ov-file#vector-functions).
To view the indexing progress, use the `pg_stat_progress_create_index` view:

```
SELECT * FROM pg_stat_progress_create_index;

```

The `phase` column shows the current state of your index creation, and the `building index: tree training` phase disappears after the index is created.
To tune your index for a target recall and QPS balance, see [Tune a `ScaNN` index](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/tune-indexes).
### Analyze your indexed table
After you create the `ScaNN` index, you must run the `ANALYZE` command to update statistics about your data.

```
ANALYZE TABLE;

```

### Build indexes in parallel
AlloyDB might automatically spawn multiple parallel workers, depending on your dataset and the type of index you choose to build your index faster.
The parallel index build is often triggered when you create a 3-level ScaNN index or if your dataset exceeds 100M rows.
Although AlloyDB automatically optimizes the number of parallel workers, you can tune the parallel workers using the [`max_parallel_maintenance_workers`](https://www.postgresql.org/docs/15/runtime-config-resource.html#GUC-MAX-PARALLEL-MAINTENANCE-WORKERS), [`max_parallel_workers`](https://www.postgresql.org/docs/15/runtime-config-resource.html#GUC-MAX-PARALLEL-WORKERS), and the [`min_parallel_table_scan_size`](https://www.postgresql.org/docs/current/runtime-config-query.html#GUC-MIN-PARALLEL-TABLE-SCAN-SIZE) PostgreSQL query planning parameters.
## Run a query
After you have stored and indexed embeddings in your database, you can start querying using the [`pgvector` query functionality](https://github.com/pgvector/pgvector#querying). You cannot run bulk search queries using the `alloydb_scann` extension.
To find the nearest semantic neighbors for an embedding vector, you can run the following example query, where you set the same distance function that you used during the index creation.

```
  SELECT * FROM TABLE
    ORDER BY EMBEDDING_COLUMN DISTANCE_FUNCTION_QUERY '[EMBEDDING]'
    LIMIT ROW_COUNT;

```

Replace the following:
  * `TABLE`: the table containing the embedding to compare the text to.
  * `EMBEDDING_COLUMN`: the column containing the stored embeddings.
  * `DISTANCE_FUNCTION_QUERY`: the distance function to use with this query. Choose one of the following based on the distance function used while creating the index:
    * **L2 distance:** `<->`
    * **Inner product:** `<#>`
    * **Cosine distance:** `<=>`
  * `EMBEDDING`: the embedding vector you want to find the nearest stored semantic neighbors of.
  * `ROW_COUNT`: the number of rows to return.
Specify `1` if you want only the single best match.


For more information about other query examples, see [Querying](https://github.com/pgvector/pgvector?tab=readme-ov-file#querying).
You can use also use the [`embedding()`](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/work-with-embeddings) function to translate the text into a vector. You apply the vector to one of the `pgvector` nearest-neighbor operator, `<->` for L2 distance, to find the database rows with the most semantically similar embeddings.
Because `embedding()` returns a `real` array, you must explicitly cast the `embedding()` call to `vector` in order to use these values with `pgvector` operators.

```
  CREATE EXTENSION IF NOT EXISTS google_ml_integration;
  CREATE EXTENSION IF NOT EXISTS vector;

  SELECT * FROM TABLE
    ORDER BY EMBEDDING_COLUMN
    <-> embedding('MODEL_IDVERSION_TAG', 'TEXT')::vector
    LIMIT ROW_COUNT;

```

Replace the following:
  * `MODEL_ID`: the ID of the model to query.
If you are using the Vertex AI Model Garden, then specify `text-embedding-005` as the model ID. These are the cloud-based models that AlloyDB can use for text embeddings. For more information, see [Text embeddings](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/text-embeddings-api).
  * Optional: `VERSION_TAG`: the version tag of the model to query. Prepend the tag with `@`.
If you are using one of the `text-embedding` English models with Vertex AI, then specify one of the version tags—for example, `text-embedding-005`, listed in [Model versions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/text-embeddings-api#model_versions).
Google strongly recommends that you always specify the version tag. If you don't specify the version tag, then AlloyDB always uses the latest model version, which might lead to unexpected results.


  * `TEXT`: the text to translate into a vector embedding.


## What's next
  * See [an example embedding workflow](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/example-embeddings).
  * [Tune vector query performance](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/tune-indexes).
  * See [vector index metrics](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/vector-index-metrics).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
