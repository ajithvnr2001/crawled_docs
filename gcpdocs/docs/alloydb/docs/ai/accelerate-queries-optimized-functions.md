---
url: https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/
title: Accelerate queries using optimized functions \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:57:32.157986+00:00
---

# Accelerate queries using optimized functions  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/

[ Skip to main content ](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/)
  * [Deutsch](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/?hl=es-419)
  * [Français](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/?hl=id)
  * [Italiano](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/?hl=ja)
  * [한국어](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/alloydb-color.svg) ](https://docs.cloud.google.com/alloydb/docs)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/#before-you-begin)
  * [Use optimized functions](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/#use-optimized-functions)
  * [Retrain a proxy model](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/#retrain-proxy-model)
  * [Limitations](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/#limitations)
  * [What's next](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/#whats-next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)


Send feedback 
#  Accelerate queries using optimized functions Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/#before-you-begin)
  * [Use optimized functions](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/#use-optimized-functions)
  * [Retrain a proxy model](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/#retrain-proxy-model)
  * [Limitations](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/#limitations)
  * [What's next](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions/#whats-next)


Optimized functions in AlloyDB for PostgreSQL let you use a smaller, faster proxy model to process most of your SQL queries that use AI functions, falling back to a larger large language model (LLM) only when necessary. This approach reduces operational costs and improves query responsiveness by minimizing remote LLM calls for row-by-row classification or filtering tasks.
AlloyDB AI functions like `ai.if()` can have high latency due to remote calls to large language models (LLMs). Optimized functions address this latency issue by using smaller, locally-trained proxy models to process your queries. These models are trained on a sample of your data, using the LLM's output as the source of truth.
Accuracy checks are performed at runtime on a sample of rows using the LLM. To perform this check, AlloyDB uses the LLM to generate labels for the sample rows and compares them with the proxy model's predictions to verify accuracy. If the accuracy check fails, the query falls back to using the LLM.
When you use an optimized function, AlloyDB does the following:
  1. Trains a proxy model: AlloyDB trains a lightweight proxy model on a sample of your data. This happens in the background when you use the `PREPARE` statement with `ai.if()` function to train the model for optimized queries.
  2. Executes the query: when you use the `EXECUTE` statement, AlloyDB uses the trained proxy model to process the query locally.
  3. Falls back to the LLM: if the accuracy of the model is low, or if AlloyDB can't find a model, AlloyDB automatically falls back to using the LLM.


![Optimized functions flow diagram](https://docs.cloud.google.com/alloydb/images/cost-optimized-functions-flow.png)
## Before you begin
Before you use the optimized functions, do the following:
  * [Connect to your database using psql](https://docs.cloud.google.com/alloydb/docs/connect-psql) or AlloyDB Studio as the `postgres` user or as a user that has access to the table where the data resides.
  * Verify that the `google_ml_integration` extension is installed and available on version 1.5.8 or higher.

```
SELECT extversion FROM pg_extension WHERE extname = 'google_ml_integration';
extversion
------------
1.5.8
(1 row)

```

  * Configure AlloyDB to work with Gemini Enterprise Agent Platform. For more information, see [Integrate your database with Agent Platform](https://docs.cloud.google.com/alloydb/docs/ai/configure-vertex-ai).
  * Ensure that the following database flags are enabled. For more information, see [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).
    * `google_ml_integration.enable_model_support`
    * `google_ml_integration.enable_ai_query_engine`
    * `google_ml_integration.enable_cost_optimized_ai_functions`
  * Generate embeddings for the table that you want to query. For more information, see [Generate and manage automatic embeddings for tables](https://docs.cloud.google.com/alloydb/docs/ai/generate-manage-auto-embeddings-for-tables).
  * Consider the following:
    * The source data column must be of type `TEXT` or `VARCHAR`.
    * The embedding column that provides input to the optimized AI function must be of type `REAL[]` or `VECTOR`.
    * Optimized functions are available only in regions where Agent Platform generative models are available. For a list of available regions, see [Deployments and endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations).


## Use optimized functions
To use an optimized function, use the `PREPARE` and `EXECUTE` statements with the `ai.if()` function. The following is an example of how to use an optimized function:
  1. Create a `restaurant_reviews` table. The `review` column that holds the source data is of type `TEXT`, and the `review_embedding` column used for queries is of type `VECTOR(768)`.

```
CREATE TABLE restaurant_reviews (
    id SERIAL,
    name VARCHAR(64),
    city VARCHAR(64),
    review TEXT,
    review_embedding VECTOR(768)
);

```

  2. Use a `PREPARE` statement with the `ai.if()` function to indicate that the query must use an optimized function. This statement triggers the asynchronous training of the model in the background.
The model is trained only under the following conditions:
     * There is exactly one `ai.if()` function in the query.
     * `ai.if()` is not inside a subquery.

```
PREPARE positive_reviews_query AS
SELECT r.name, r.city
FROM restaurant_reviews r
WHERE ai.if('Is the following a positive review? Review: ' || r.review, r.review_embedding)
GROUP BY r.name, r.city
HAVING COUNT(*) > 500;

```

  3. Run the query using the `EXECUTE` statement. Because the `PREPARE` statement is specific to the current session, you must run `EXECUTE` statement on the same connection:

```
EXECUTE positive_reviews_query;

```

```
conn2=> SELECT r.name, r.city
    FROM restaurant_reviews r
    WHERE ai.if('Is the following a positive review? Review: ' || r.review, r.review_embedding)
    GROUP BY r.name, r.city
    HAVING COUNT(*) > 500;

```

The trained proxy model isn't used if any of the following conditions are met:
     * The content or embedding column referenced in `ai.if()` changes. Both columns must belong to the same table.
     * The prompt provided to the content column changes.
     * The structure of the query changes, resulting in a different `query_id`.
     * The query fails to meet the accuracy check threshold at the beginning of the query.
In these cases, the query falls back to using the LLM, and AlloyDB returns a warning.
  4. Optional. To disable the accuracy validation check for the entire database environment, which is required because accuracy checks are also performed during model training, run the following command.

```
ALTER DATABASE DATABASE_NAME SET google_ml_integration.proxy_models_enable_accuracy_check = off;

```

Replace `DATABASE_NAME` with the name of your database.


## Retrain a proxy model
If your underlying table data changes significantly, you can retrain the proxy model by running the `PREPARE` statement again. Re-preparing a query replaces the existing proxy model by initiating a new training request.
## Limitations
If you change the source content column, the embedding column, or the prompt supplied to `ai.if()` function, you must issue a new `PREPARE` statement. AlloyDB trains the optimized function to approximate the behavior of a unique combination of prompt and input data.
## What's next
  * [Troubleshoot optimized functions](https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-optimized-func).


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
