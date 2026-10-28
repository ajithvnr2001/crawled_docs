---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/
title: Create a HNSW index \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:44:51.596107+00:00
---

# Create a HNSW index  |  AlloyDB Omni using the container orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/

[ Skip to main content ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/)
  * [Deutsch](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/?hl=es-419)
  * [Français](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/?hl=id)
  * [Italiano](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/?hl=ja)
  * [한국어](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Falloydb%2Fomni%2Fkubernetes%2F18.1.0%2Fdocs%2Fai%2Fcreate-hnsw-index%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/alloydb-color.svg) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/#before-you-begin)
  * [Create an HNSW index](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/#create-hnsw-index)
  * [Run a query](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/#query)
  * [What's next](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/#whats-next)


This page documents AlloyDB Omni version **18.1.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview)


Was this helpful?
Send feedback 
#  Create a HNSW index Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/#before-you-begin)
  * [Create an HNSW index](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/#create-hnsw-index)
  * [Run a query](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/#query)
  * [What's next](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index/#whats-next)


Select a documentation version:  18.1.0keyboard_arrow_down
  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/create-hnsw-index)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/ai/create-hnsw-index)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/ai/create-hnsw-index)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-hnsw-index)


This page describes how to use stored embeddings to generate indexes and query embeddings using an `HNSW` index with AlloyDB Omni. For more information about storing embedding, see [Store vector embeddings](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-embeddings).
## Before you begin
Before you can start creating indexes, you must complete the following prerequisites.
  * [Embedding vectors are added to a table](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-embeddings) in your AlloyDB Omni database.
  * The `vector` extension version `0.5.0` or later that is based on `pgvector`, extended by Google for AlloyDB Omni is installed.

```
CREATE EXTENSION IF NOT EXISTS vector;

```



## Create an `HNSW` index
AlloyDB Omni supports creating a graph-based `hnsw` index available with stock `pgvector` using the AlloyDB Omni `pgvector` extension. Using an `hnsw` index results in a greedy search that moves through the graph constantly looking for neighbor closest to the query vector until it finds an optimum result. It provides faster query performance but slower build times when compared to `IVF`.
For more information about the HNSW algorithm, see [Hierarchical Navigable Small World graphs](https://arxiv.org/abs/1603.09320).
To create an `hnsw` index, run the following query:

```
CREATE INDEX INDEX_NAME ON TABLE
  USING hnsw (EMBEDDING_COLUMN DISTANCE_FUNCTION)
  WITH (m = NUMBER_OF_CONNECTIONS, ef_construction = CANDIDATE_LIST_SIZE);

```

Replace the following:
  * `INDEX_NAME`: the name of the index that you want to create—for example, `my-hnsw-index`.
  * `TABLE`: the table to add the index to.
  * `EMBEDDING_COLUMN`: the column that stores `vector` data.
  * `DISTANCE_FUNCTION`: the distance function to use with this index. Choose one of the following:
    * **L2 distance:** `vector_l2_ops`
    * **Inner product:** `vector_ip_ops`
    * **Cosine distance:** `vector_cosine_ops`
  * `NUMBER_OF_CONNECTIONS`: the maximum number of connections per from a node in the graph. You can start with the default value as `16` and experiment with higher values based on the size of your dataset.
  * `CANDIDATE_LIST_SIZE`: the size of a candidate list maintained during graph construction, which constantly updates the current best candidates for nearest neighbors for a node. Set this value to any value higher than twice of the `m` value—for example, `64`.


To view the indexing progress, use the `pg_stat_progress_create_index` view:

```
SELECT * FROM pg_stat_progress_create_index;

```

The `phase` column shows the current state of your index creation, and the `building graph` phase disappears after the index is created.
To tune your index for a target recall and QPS balance, see [Tune an `hnsw` index](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/tune-indexes).
## Run a query
After you store and index the embeddings in your database, you can start querying using the [`pgvector` query functionality](https://github.com/pgvector/pgvector#querying).
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
You can also use the [`embedding()`](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/work-with-embeddings) function to translate the text into a vector. You apply the vector to one of the `pgvector` nearest-neighbor operators, `<->` for L2 distance, to find the database rows with the most semantically similar embeddings.
Because `embedding()` returns a `real` array, you must explicitly cast the `embedding()` call to `vector` in order to use these values with `pgvector` operators.
## What's next
  * [Create a ScaNN index](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-scann-index)

* [Perform vector search](/alloydb/omni/kubernetes/18.1.0/docs/ai/perform-vector-search) 
  * [Tune vector query performance](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/tune-indexes)

* [Vector index metrics](/alloydb/omni/kubernetes/18.1.0/docs/reference/vector-index-metrics) 
  * [Learn how to build a smart shopping assistant with AlloyDB, pgvector, and model endpoint management](https://codelabs.developers.google.com/smart-shop-agent-alloydb#0).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
