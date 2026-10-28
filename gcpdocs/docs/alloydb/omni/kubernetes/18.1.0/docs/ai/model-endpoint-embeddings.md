---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/
title: Generate vector embeddings with model endpoint management \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:38:18.670324+00:00
---

# Generate vector embeddings with model endpoint management  |  AlloyDB Omni using the container orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/

[ Skip to main content ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/)
  * [Deutsch](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/?hl=es-419)
  * [Français](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/?hl=id)
  * [Italiano](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/?hl=ja)
  * [한국어](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/alloydb-color.svg) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/#before-begin)
  * [Generate embeddings](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/#generate-embeddings)
  * [Examples](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/#examples)
    * [Text embedding models with built-in support](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/#models-builtin)


This page documents AlloyDB Omni version **18.1.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview)


Was this helpful?
Send feedback 
#  Generate vector embeddings with model endpoint management Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/#before-begin)
  * [Generate embeddings](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/#generate-embeddings)
  * [Examples](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/#examples)
    * [Text embedding models with built-in support](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings/#models-builtin)


Select a documentation version:  18.1.0keyboard_arrow_down
  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/model-endpoint-embeddings)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/ai/model-endpoint-embeddings)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/ai/model-endpoint-embeddings)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/model-endpoint-embeddings)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/ai/model-endpoint-embeddings)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/ai/model-endpoint-embeddings)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/model-endpoint-embeddings)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/ai/model-endpoint-embeddings)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/ai/model-endpoint-embeddings)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/ai/model-endpoint-embeddings)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/ai/model-endpoint-embeddings)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/ai/model-endpoint-embeddings)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/ai/model-endpoint-embeddings)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/ai/model-endpoint-embeddings)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/ai/model-endpoint-embeddings)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/ai/model-endpoint-embeddings)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/model-endpoint-embeddings)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/ai/model-endpoint-embeddings)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/ai/model-endpoint-embeddings)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/ai/model-endpoint-embeddings)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/ai/model-endpoint-embeddings)

This page describes how to generate embeddings using registered model endpoints. 
## Before you begin
Make sure that you have registered your model endpoint with Model endpoint management. For more information, see [Register and call remote AI models in AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/register-model-endpoint).
## Generate embeddings
Use the `google_ml.embedding()` SQL function to call the registered model endpoint with the text embedding model type to generate embeddings.
To call the model and generate embeddings, use the following SQL query:

```
SELECT
  google_ml.embedding(
    model_id => 'MODEL_ID',
    content => 'CONTENT');

```

Replace the following:
  * `MODEL_ID`: the model ID you defined when registering the model endpoint.
  * `CONTENT`: the text to translate into a vector embedding.


## Examples
Some examples for generating embeddings using registered model endpoint are listed in this section.
### Text embedding models with built-in support
To generate embeddings for a registered `text-embedding-005` model endpoint, run the following statement:

```
    SELECT
      google_ml.embedding(
        model_id => 'text-embedding-005',
        content => 'AlloyDB is a managed, cloud-hosted SQL database service');

```

To generate embeddings for a registered `text-embedding-3-small` or `text-embedding-3-large` model endpoint by OpenAI, run the following statement:

```
  SELECT
    google_ml.embedding(
      model_id => 'text-embedding-3-small',
      content => 'Vector embeddings in AI');

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
