---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings/
title: Store vector embeddings \u00a0|\u00a0 AlloyDB Omni using containers: 15.15.0 \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:04:22.860946+00:00
---

# Store vector embeddings  |  AlloyDB Omni using containers: 15.15.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings/

[ Skip to main content ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings/)
  * [Deutsch](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings/?hl=es-419)
  * [Français](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings/?hl=id)
  * [Italiano](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings/?hl=ja)
  * [한국어](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/alloydb-color.svg) ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/overview)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/overview)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Required database extension](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings/#required-extension)
  * [Store generated embeddings](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings/#store-vector-embeddings)
  * [What's next](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings/#whats_next_2)


This page documents AlloyDB Omni version **15.15.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/overview)


Was this helpful?
Send feedback 
#  Store vector embeddings Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Required database extension](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings/#required-extension)
  * [Store generated embeddings](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings/#store-vector-embeddings)
  * [What's next](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings/#whats_next_2)


Select a documentation version:  15.15.0keyboard_arrow_down
  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/ai/store-embeddings)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/store-embeddings)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/ai/store-embeddings)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/ai/store-embeddings)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/ai/store-embeddings)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/ai/store-embeddings)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/ai/store-embeddings)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/ai/store-embeddings)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/ai/store-embeddings)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/ai/store-embeddings)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/ai/store-embeddings)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/ai/store-embeddings)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/ai/store-embeddings)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/ai/store-embeddings)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/ai/store-embeddings)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/ai/store-embeddings)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/ai/store-embeddings)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/ai/store-embeddings)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/store-embeddings)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/ai/store-embeddings)

This page shows you how to use AlloyDB as a vector database with the `vector` extension that includes `pgvector` functions and operators. These functions and operators let you store embeddings as vector values. 
## Required database extension
Use the `vector` extension, version `0.5.0.google-1` or later, which includes `pgvector` functions and operators, to store generated embeddings as `vector` values. This is a version of `pgvector` that Google has extended with optimizations specific to AlloyDB.

```
CREATE EXTENSION IF NOT EXISTS vector;

```

## Store generated embeddings
Ensure that you have already created a table in your AlloyDB database.
To store vector embeddings, follow these steps:
  1. Create a `vector[]` column in your table to store your embeddings:

```
ALTER TABLE TABLE ADD COLUMN EMBEDDING_COLUMN vector(DIMENSIONS);

```

Replace the following:
     * `TABLE`: the table name.
     * `EMBEDDING_COLUMN`: the name of the new embedding column.
     * `DIMENSIONS`: the number of dimensions that the model supports.
For example, if you are using one of the `text-embedding`English models—for example, `text-embedding-005` with Vertex AI, specify `768`.
  2. Copy the vectors to the vector column. The following example assumes that your embeddings are available in a CSV file:

```
COPY TABLE (EMBEDDING_COLUMN) FROM 'PATH_TO_VECTOR_CSV (FORMAT CSV);

```

Replace the following:
     * `PATH_TO_VECTOR_CSV`: the full path of where you stored your CSV file.


After you store the embeddings, you can use the `vector` extension or the `alloydb_scann` extension to create indexes for faster query performance.
## What's next
  * [Create indexes and query vectors](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-index-query-vectors).
  * Learn [an example embedding workflow](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/example-embeddings).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
