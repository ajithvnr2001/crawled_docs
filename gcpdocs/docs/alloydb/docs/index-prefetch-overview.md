---
url: https://docs.cloud.google.com/alloydb/docs/index-prefetch-overview/
title: Index prefetch overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T05:47:26.873095+00:00
---

# Index prefetch overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/index-prefetch-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Index prefetch overview Stay organized with collections  Save and categorize content based on your preferences. 

AlloyDB for PostgreSQL uses index prefetch to speed up queries that read a range of rows through a B-tree index. Index prefetch is enabled by default on AlloyDB and AlloyDB Omni instances that run PostgreSQL 17 and later. You don't need to set any flags, rebuild indexes, or change your application or SQL queries to benefit from it.

## How index prefetch works

When a query scans a range of values through an index—for example, a `BETWEEN` predicate or an `ORDER BY ... LIMIT` clause on an indexed column—the scan reads index pages and the table pages that the index entries point to. Those table pages are often scattered across storage. In standard PostgreSQL, the scan reads these pages one at a time, so when the pages aren't already in memory, the query spends most of its time waiting for storage I/O.

With index prefetch, AlloyDB looks ahead of the running scan on both the index and the table, and reads the pages that the scan is about to need in parallel. AlloyDB stages the prefetched pages in the instance's local SSD cache, so that when the scan requests a page, the page is served from fast local storage instead of from remote storage. Prefetched pages are staged outside of the PostgreSQL shared buffers, so prefetching doesn't reduce the buffer cache that's available to other sessions.

Index prefetch includes the following safeguards so that it doesn't add overhead to queries that can't benefit from it:

  * Prefetching stops at the boundary of a `LIMIT` clause, so the scan doesn't read pages past the rows that the query returns.
  * For index-only scans on covering indexes, AlloyDB prefetches only index pages and doesn't read table pages.
  * Queries that return a single row, such as primary key lookups, don't trigger prefetching.



## Benefits for workloads

Index prefetch helps most when your working set is larger than the instance's memory and your queries read many rows through a B-tree index. The following are examples of queries that benefit:

  * Range queries on indexed timestamp, date, or numeric columns, such as reports over a time window.
  * Queries that return many rows for one key, such as the order history for a customer.
  * Joins where the inner side is an index scan that returns many rows.
  * Analytical queries that read large ranges from row-oriented tables.



Queries whose data is already in shared buffers, and single-row lookups, perform the same with or without prefetching.

## Prefetching in execution plans

To see the effect of index prefetch on a query, run the query with `EXPLAIN (ANALYZE, BUFFERS)`. Pages that prefetching loads into the local SSD cache appear as `ultra fast cache hit` counts on the index scan nodes of the plan. For more information about reading these counters, see [Get and analyze execution plans](https://docs.cloud.google.com/alloydb/docs/get-analyze-execution-plans).

## What's next

  * [Get and analyze execution plans](https://docs.cloud.google.com/alloydb/docs/get-analyze-execution-plans)
  * [Indexing strategies](https://docs.cloud.google.com/alloydb/docs/reference/indexing-strategies)
  * [Index advisor overview](https://docs.cloud.google.com/alloydb/docs/index-advisor-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
