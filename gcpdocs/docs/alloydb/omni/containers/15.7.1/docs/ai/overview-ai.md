---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/
title: Build generative AI applications using AlloyDB AI \u00a0|\u00a0 AlloyDB Omni for containers: 15.7.1 \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:27:14.334857+00:00
---

# Build generative AI applications using AlloyDB AI  |  AlloyDB Omni for containers: 15.7.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/

[ Skip to main content ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/)
  * [Deutsch](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/?hl=de)
  * [Español](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/?hl=es-419)
  * [Français](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/?hl=id)
  * [Italiano](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/?hl=it)
  * [Português](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/?hl=ja)
  * [한국어](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Falloydb%2Fomni%2Fcontainers%2F15.7.1%2Fdocs%2Fai%2Foverview-ai%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/alloydb-color.svg) ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/overview)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/overview)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Store, index, and query vectors](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/#store-index-query-vectors)
  * [Tune your vector query performance](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/#tune-vectors)
  * [Generate embeddings and text predictions](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/#generate_embeddings_and_text_predictions_2)
    * [Use models in the cloud with Vertex AI](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/#use-cloud-models)
  * [What's next](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/#whats_next_2)


This page documents AlloyDB Omni version **15.7.1** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/overview)


Was this helpful?
Send feedback 
#  Build generative AI applications using AlloyDB AI Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Store, index, and query vectors](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/#store-index-query-vectors)
  * [Tune your vector query performance](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/#tune-vectors)
  * [Generate embeddings and text predictions](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/#generate_embeddings_and_text_predictions_2)
    * [Use models in the cloud with Vertex AI](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/#use-cloud-models)
  * [What's next](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai/#whats_next_2)


Select a documentation version:  15.7.1keyboard_arrow_down
  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/ai/overview-ai)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/overview-ai)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/ai/overview-ai)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/ai/overview-ai)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/ai/overview-ai)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/ai/overview-ai)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/ai/overview-ai)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/ai/overview-ai)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/ai/overview-ai)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/ai/overview-ai)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/ai/overview-ai)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/ai/overview-ai)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/ai/overview-ai)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/ai/overview-ai)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/ai/overview-ai)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/ai/overview-ai)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/overview-ai)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/ai/overview-ai)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/ai/overview-ai)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/ai/overview-ai)

AlloyDB AI is a suite of features included with AlloyDB for PostgreSQL and AlloyDB Omni that let you apply the semantic and predictive power of machine learning (ML) models to your data. This page provides an overview of the ML-powered AI functions that are available through AlloyDB. 
## Store, index, and query vectors
The stock [`pgvector` PostgreSQL extension](https://github.com/pgvector/pgvector?tab=readme-ov-file#indexing) extension is customized for AlloyDB, and referred to as `vector`. It supports storing generated embeddings in a vector column. The extension also adds support for scalar quantization feature to create `IVF` indexes. You can also create an `IVFFlat` index or `HSNW` index that are available with stock `pgvector`.
For more information about storing vectors, see [Store vector embeddings](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/store-embeddings).
In addition to the customized `vector` extension, AlloyDB includes the `alloydb_scann` extension that implements a highly efficient nearest-neighbor index powered by the [ScaNN algorithm](https://github.com/google-research/google-research/blob/master/scann/docs/algorithms.md).
For more information about creating indexes and querying vectors, see [Create indexes and query vectors](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/store-index-query-vectors).
## Tune your vector query performance
You can tune your indexes for a balance between query-per-second (QPS) and recall with your queries. For more information about tuning your indexes, see [Tune vector query performance](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/tune-indexes).
## Generate embeddings and text predictions
AlloyDB AI extends PostgreSQL syntax with two functions for querying models using the `google_ml_integration` extension:
  * [Invoke predictions](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/invoke-predictions) to call a model using SQL within a transaction.
  * [Generate embeddings](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/work-with-embeddings) to have an LLM translate text prompts into numerical vectors.
You can use the [`embedding()` function](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/work-with-embeddings) to query Vertex AI models, while the [`google_ml.embedding()` function](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/model-endpoint-overview) can be used to query registered Vertex AI, hosted, and third-party models.
You can then apply these vector embeddings as input to `pgvector` functions. This includes methods to compare and sort samples of text according to their relative semantic distance.


### Use models in the cloud with Vertex AI
You can [configure AlloyDB Omni to work with Vertex AI](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/install-with-alloydb-ai).
This gives your applications the following benefits:
  * Your applications can invoke predictions using any model stored in the [ Vertex AI Model Garden](https://cloud.google.com/model-garden) that they have access to.
  * Your applications can generate embeddings using [the `text-embedding-005` English models](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/model-reference/text-embeddings) LLM.


## What's next
  * [Install AlloyDB Omni with AlloyDB AI](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/install-with-alloydb-ai).
  * [Create indexes and query vectors](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/store-index-query-vectors).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
