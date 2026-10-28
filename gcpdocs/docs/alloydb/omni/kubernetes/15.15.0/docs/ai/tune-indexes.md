---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/
title: Tune vector query performance in AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 15.15.0 \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:33:54.209698+00:00
---

# Tune vector query performance in AlloyDB Omni  |  AlloyDB Omni using the container orchestrator: 15.15.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/

[ Skip to main content ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?resource=scann#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/)
  * [Deutsch](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?hl=es-419)
  * [Français](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?hl=id)
  * [Italiano](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?hl=ja)
  * [한국어](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/alloydb-color.svg) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/overview)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/overview)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?resource=scann#before-you-begin)
  * [Tune a ScaNN index](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?resource=scann#tune-scann-indexes)
  * [Analyze your queries](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?resource=scann#explain-analyze)
  * [View vector index metrics](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?resource=scann#vector-index-metrics)
  * [What's next](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?resource=scann#whats_next_2)


This page documents AlloyDB Omni version **15.15.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/overview)


Was this helpful?
Send feedback 
#  Tune vector query performance in AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?resource=scann#before-you-begin)
  * [Tune a ScaNN index](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?resource=scann#tune-scann-indexes)
  * [Analyze your queries](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?resource=scann#explain-analyze)
  * [View vector index metrics](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?resource=scann#vector-index-metrics)
  * [What's next](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?resource=scann#whats_next_2)


Select a documentation version:  15.15.0keyboard_arrow_down
  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/tune-indexes)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/ai/tune-indexes)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/ai/tune-indexes)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/tune-indexes)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/ai/tune-indexes)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/ai/tune-indexes)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/tune-indexes)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/ai/tune-indexes)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/ai/tune-indexes)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/ai/tune-indexes)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/ai/tune-indexes)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/ai/tune-indexes)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/ai/tune-indexes)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/ai/tune-indexes)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/ai/tune-indexes)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/ai/tune-indexes)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/ai/tune-indexes)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/ai/tune-indexes)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/ai/tune-indexes)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/ai/tune-indexes)


This document describes how to tune your indexes to achieve faster query performance and better recall in AlloyDB Omni.
ScaNN IVF IVFFlat HNSW
## Before you begin
Before you build a `ScaNN` index, complete the following:
  * Make sure that a table with your data is already created.
  * To avoid issues while generating the index, make sure that the value you set for the `maintenance_work_mem` and the `shared_buffers` flag is less than total machine memory.


## Tune a `ScaNN` index
Use the following guidance to choose between a two-level and three-level ScaNN index:
  * Choose a two-level index if the number of vector rows is less than 10 million rows.
  * Choose a three-level index if the number of vector rows exceeds 100 million rows.
  * Choose a three-level index to optimize for index build time or choose a two-level index to optimize for search recall if the number of vector rows lies between 10 million and 100 million rows.


Consider the following examples for two-level and three-level `ScaNN` indexes that show how tuning parameters are set for a table with 1000000 rows:
[Two-level index](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?resource=scann#two-level-index)[Three-level index](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes/?resource=scann#three-level-index) More

```
-- Setting num_leaves to 1000 as power(1000000, 1/2) for two-level index
BEGIN;

SET LOCAL maintenance_work_mem = '300MB';

CREATE INDEX my_scann_index ON my_table
  USING scann (vector_column cosine)
  WITH (num_leaves = 1000);
END;

```

```
-- Setting num_leaves to 10000 as power(1000000, 2/3) for three-level index
BEGIN;

SET LOCAL maintenance_work_mem = '500MB';

CREATE INDEX my_scann_index ON my_table
  USING scann (vector_column cosine)
  WITH (num_leaves = 10000, max_num_levels = 2);
END;

```

## Analyze your queries
Use the `EXPLAIN ANALYZE` command to analyze your query insights as shown in the following example SQL query.

```
  EXPLAIN ANALYZE SELECT result_column
  FROM my_table
  ORDER BY EMBEDDING_COLUMN <=> embedding('text-embedding-005', 'What is a database?')::vector
  LIMIT 1;

```

The example response `QUERY PLAN` includes information such as the time taken, the number of rows scanned or returned, and the resources used.

```
Limit  (cost=0.42..15.27 rows=1 width=32) (actual time=0.106..0.132 rows=1 loops=1)
  ->  Index Scan using my_scann_index on my_table  (cost=0.42..858027.93 rows=100000 width=32) (actual time=0.105..0.129 rows=1 loops=1)
        Order By: (embedding_column <=> embedding('text-embedding-005', 'What is a database?')::vector(768))
        Limit value: 1
Planning Time: 0.354 ms
Execution Time: 0.141 ms

```

## View vector index metrics
You can use the vector index metrics to review performance of your vector index, identify areas for improvement, and tune your index based on the metrics, if needed.
To view all vector index metrics, run the following SQL query, which uses the `pg_stat_ann_indexes` view:

```
SELECT * FROM pg_stat_ann_indexes;

```

For more information about the complete list of metrics, see [Vector index metrics](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/vector-index-metrics).
## What's next
  * [An example embedding workflow](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/example-embeddings)


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
