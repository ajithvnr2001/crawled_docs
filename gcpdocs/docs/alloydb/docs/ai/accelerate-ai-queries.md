---
url: https://docs.cloud.google.com/alloydb/docs/ai/accelerate-ai-queries/
title: Accelerate performance for queries with AI functions \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:49:33.122225+00:00
---

# Accelerate performance for queries with AI functions  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/ai/accelerate-ai-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Accelerate performance for queries with AI functions Stay organized with collections  Save and categorize content based on your preferences. 

Smart batching for AI functions lets you optimize performance when you run queries that use AI functions in AlloyDB for PostgreSQL. It provides the same or better performance than [array-based functions](https://docs.cloud.google.com/alloydb/docs/ai/evaluate-semantic-queries-ai-operators#filter-batch-arrays), without requiring you to rewrite queries into complex array structures. For more information about AI functions, see [AI functions overview](https://docs.cloud.google.com/alloydb/docs/ai/ai-query-engine-landing).

In standard PostgreSQL, evaluating an AI function row-by-row incurs network latency on each individual row. With smart batching in AlloyDB, eligible AI operations are automatically batched and offloaded for asynchronous evaluation, letting you write standard, easy-to-read SQL queries. Standard relational filters are evaluated before AI functions, ensuring optimal performance and model usage.

## Supported AI functions

AlloyDB smart batching supports the following AI functions which are available across both the `ai` and `google_ml` schemas:

Function | Description | Extension version  
---|---|---  
`ai.if(prompt text, ...)` / `google_ml.if(...)` | Evaluates a natural-language boolean prompt, returning `true` or `false`. Supported across `SELECT` projections, `WHERE` filters, and `JOIN` clauses. | All  
`ai.rank(prompt text, ...)` / `google_ml.rank(...)` | Computes a numerical relevance score (`float`) indicating how closely an input matches given criteria. Supported across `WHERE` filters, `ORDER BY`, `SELECT`, and `JOIN` clauses. | All  
`ai.generate(prompt text, ...)` / `google_ml.generate(...)` | Generates natural language responses or structured text using foundation models. Supported across `SELECT` projections, `WHERE` filters, and `JOIN` clauses. | All  
`ai.analyze_sentiment(input text, ...)` / `google_ml.analyze_sentiment(...)` | Analyzes the sentiment of input text and returns `'positive'`, `'negative'`, or `'neutral'`. Supported across `SELECT` projections, `WHERE` filters, and `JOIN` clauses. | 1.6.3  
`ai.summarize(input text, ...)` / `google_ml.summarize(...)` | Summarizes the input text. Supported across `SELECT` projections, `WHERE` filters, and `JOIN` clauses. | 1.6.4  
`ai.agg_summarize(column_name text, ...)` / `google_ml.agg_summarize(...)` | Aggregates and summarizes text values across multiple rows into a single summary. | 1.6.4  
`ai.extract(input text, output_schema text, ...)` / `google_ml.extract(...)`   
  
(in [Preview](https://cloud.google.com/products#product-launch-stages); requires setting `google_ml_integration.enable_preview_ai_functions=on`) | Extracts structured entities or key-value attributes from text. Supported across `SELECT` projections, `WHERE` filters, and `JOIN` clauses. | 1.6.1  
`ai.classify(input text, categories text[][], ...)` / `google_ml.classify(...)`   
  
(in [Preview](https://cloud.google.com/products#product-launch-stages); requires setting `google_ml_integration.enable_preview_ai_functions=on`) | Classifies text into specified category labels. Supported across `SELECT` projections, `WHERE` filters, and `JOIN` clauses. | 1.6.1  
  
For more information about the syntax and parameters of AI functions, see [Model endpoint management reference](https://docs.cloud.google.com/alloydb/docs/reference/model-endpoint).

### Supported clauses

AI function acceleration works across major SQL clauses, either individually or in combination:

  * `WHERE` clauses: filters rows using boolean AI evaluations (`ai.if`) after evaluating selective non-AI relational predicates.
  * `ORDER BY` clauses: computes AI relevance scores (`ai.rank`) in batches before performing sort or limit operations.
  * `SELECT` projections: batches scalar AI functions (`ai.if`, `ai.rank`, `ai.generate`, `ai.analyze_sentiment`, `ai.summarize`, `ai.extract`, and `ai.classify`) across result rows, and aggregates and summarizes text across rows using `ai.agg_summarize`.
  * `JOIN ... ON` conditions: evaluates cross-table AI conditions in `INNER JOIN` operations using smart batching.
  * DML statements: accelerates AI functions in `WHERE` predicates, target lists, and `SET` expressions across `UPDATE`, `DELETE`, and `INSERT ... SELECT` operations (for example, `INSERT INTO ... SELECT ai.generate(...)` and `UPDATE ... SET col = ai.generate(...)`).



### Supported argument expressions

Prompt arguments support standard SQL expressions, including:

  * Column references (for example, `r.review`)
  * String literals concatenated with column references (for example, `'Is this a positive review? Review: ' || r.review`)
  * Concatenation of multiple columns (for example, `r.name || ' ' || r.review`)
  * Scalar SQL expressions and functions (for example, `COALESCE(r.review, '')`, `LOWER(r.comments)`, `SUBSTRING(description FROM 1 FOR 500)`, and `CASE` statements)



## Before you begin

To use smart batching for AI functions in AlloyDB, make sure the following prerequisites are met:

  1. PostgreSQL version: use PostgreSQL version 17 or later.
  2. Integrate with Gemini Enterprise Agent Platform: complete the steps in [Integrate with Gemini Enterprise Agent Platform](https://docs.cloud.google.com/alloydb/docs/ai/configure-vertex-ai).
  3. Regional availability: smart batching is available in regions that support the default model (`gemini-2.5-flash-lite`) or the model configured using `google_ml_integration.default_llm_model`. For more information, see [Supported regions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash-lite#supported-regions).



## Enable smart batching for AI functions

In PostgreSQL 18 or later, smart batching for AI functions is enabled by default. In PostgreSQL 17, it is disabled by default and must be enabled explicitly. You can configure its behavior globally through database flags at the instance level, or per session using SQL `SET` commands.

### Configuration parameters

Parameter name | Type | Default | Scope | Description  
---|---|---|---|---  
`google_ml_integration.enable_ai_function_acceleration` | Boolean | PostgreSQL 18: `on`   
PostgreSQL 17: `off` | Session, user, or instance | Controls whether the query planner and executor offload eligible AI operations for smart batching. When set to `off`, queries execute using standard PostgreSQL row-by-row execution.  
  
**Additional settings:**

  * Preview functions: to enable smart batching for AI functions in [Preview](https://cloud.google.com/products#product-launch-stages) such as `ai.extract` and `ai.classify`, set `google_ml_integration.enable_preview_ai_functions` to `on`.
  * Model selection: to specify a different model instead of the default `gemini-2.5-flash-lite`, set `google_ml_integration.default_llm_model` to your target model ID, or pass the `model_id` parameter in the AI function.



### Configure at the instance level

To configure database flags at the instance level across your AlloyDB cluster, use the `gcloud alloydb instances update` command:
    
    
    gcloud alloydb instances update INSTANCE_ID \
      --database-flags google_ml_integration.enable_ai_function_acceleration=on \
      --region=REGION_ID \
      --cluster=CLUSTER_ID \
      --project=PROJECT_ID

Replace the following:

  * `INSTANCE_ID`: the ID of the instance you want to update.
  * `REGION_ID`: the ID of the region where the cluster is located. For more information, see [Supported regions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-flash-lite#supported-regions).
  * `CLUSTER_ID`: the ID of the cluster.
  * `PROJECT_ID`: the ID of the project.



For more information, see [Configure database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

### Configure at the session level

To tune or toggle smart batching parameters for your session, use the `SET` command:
    
    
    -- Disable smart batching for the current session (runs standard row-by-row execution)
    SET google_ml_integration.enable_ai_function_acceleration = off;
    
    -- Re-enable smart batching
    SET google_ml_integration.enable_ai_function_acceleration = on;
    
    -- Enable preview functions (ai.extract, ai.classify)
    SET google_ml_integration.enable_preview_ai_functions = on;
    

## Verify smart batching for AI functions

To verify that smart batching for AI functions is enabled, you can use the `EXPLAIN` statement to analyze your query.

When smart batching is enabled, the execution plan includes a `Custom Scan (AIFunctionApply)` or `Parallel Custom Scan (AIFunctionApply)` node. The presence of this node indicates that eligible AI function calls are extracted from standard row-by-row and executed in high-throughput asynchronous batches. If this node isn't present, the query is executed using standard PostgreSQL row-by-row evaluation.

### Verify AI filtering in WHERE clauses

When you use an AI boolean function (such as `ai.if`) in a `WHERE` clause alongside standard relational SQL predicates, AlloyDB evaluates selective relational filters first using index scans or table scans. Then, AlloyDB accelerates only the candidate rows for AI evaluation. For example:
    
    
    EXPLAIN (COSTS OFF)
    SELECT r.name, r.review
    FROM restaurant_reviews r
    WHERE ai.if('Is the following a positive review? Review: ' || r.review)
      AND r.city = 'Los Angeles';
    

When you use the `EXPLAIN` statement to analyze your query, the query plan shows a `Custom Scan (AIFunctionApply)` node:
    
    
                                           QUERY PLAN
    ----------------------------------------------------------------------------------------
     Custom Scan (AIFunctionApply)
       Filter: ai.if(('Is the following a positive review? Review: '::text || review), NULL::character varying)
       ->  Index Scan using idx_restaurant_reviews_city on restaurant_reviews r
             Index Cond: ((city)::text = 'Los Angeles'::text)
    

The relational filter (`city = 'Los Angeles'`) evaluates first on the index, and only matching rows are batched and sent to the model for `ai.if` evaluation.

### Verify AI projection with parallel query execution

AI scoring and generation functions in the `SELECT` target list accelerate automatically. When queries scan large tables, smart acceleration integrates with PostgreSQL [parallel query](https://www.postgresql.org/docs/current/parallel-query.html), distributing batch evaluation across parallel background workers:
    
    
    EXPLAIN (COSTS OFF)
    SELECT ai.generate('Summarize the customer sentiment for: ' || r.review) AS review_summary
    FROM restaurant_reviews r
    WHERE ai.if('Does this review mention food safety concerns? ' || r.review);
    

Example query plan output:
    
    
                                QUERY PLAN
    ------------------------------------------------------------------------------------------------------
     Gather
       Workers Planned: 4
       ->  Custom Scan (AIFunctionApply)
             ->  Parallel Custom Scan (AIFunctionApply)
                   Filter: ai.if(('Does this review mention food safety concerns? '::text || r.review), NULL::character varying)
                   ->  Parallel Seq Scan on restaurant_reviews r
    (6 rows)
    

## Fallback behavior

Smart batching provides safe fallback semantics. If a query contains a construct or pattern that can't safely accelerate, then the query doesn't fail. Instead, AlloyDB safely executes the query using standard PostgreSQL row-by-row execution.

### Diagnose fallbacks with `DEBUG2`

To check why a query used standard execution rather than smart batching, set `client_min_messages` to `DEBUG2` and execute `EXPLAIN`:
    
    
    SET client_min_messages TO DEBUG2;
    EXPLAIN SELECT ...;
    RESET client_min_messages;
    

Inspect the output for diagnostic messages prefixed with: `AI function acceleration is not applied`.

### Unsupported query patterns

The following query patterns can't be accelerated and automatically fall back to standard row-by-row execution:

  * Nested AI functions: AI functions can't take another AI function call as an argument (for example, `ai.if(ai.if(...))`).
  * Outer join `ON` clauses: AI functions placed in `LEFT`, `RIGHT`, or `FULL OUTER JOIN` conditions. A workaround is to place the AI filter in the `WHERE` clause or in a subquery.
  * Aggregates wrapping AI functions: direct aggregates over AI functions (for example, `AVG(ai.rank(...))`). A workaround is to compute the AI function in a CTE or subquery first, then aggregate.
  * Volatile function arguments: argument expressions that contain volatile functions (for example, `random()` or `clock_timestamp()`).
  * Non-constant arguments: all arguments following the initial text input (such as `output_schema`, `categories`, and `model_id`) must be constant literals, not column references or expressions.
  * Correlated subqueries or outer parameters: AI expressions that reference variables from an outer query block.
  * Non-base relations: scans over foreign tables (`postgres_fdw`) or materialized CTEs (`WITH ... AS MATERIALIZED`).
  * More than five distinct AI functions: a single table scan supports up to five distinct AI function calls.



## Tune performance

You can tune your AlloyDB instance and session parameters to maximize throughput and minimize latency for AI workloads.

### Batch group size

The parameter `google_ml_integration.ai_function_acceleration_group_size` sets the maximum number of rows batched into a single remote RPC call to Vertex AI:

  * Default value: `4000` (Range: `1` to `20000`)
  * Scope: Session, user, or database level


    
    
    SET google_ml_integration.ai_function_acceleration_group_size = 10000;
    

#### Workload sizing guidelines:

  * Interactive queries (for online transaction processing (OLTP) or low latency): set `group_size` between `50` and `100`. Smaller batch sizes return the first batch of results more quickly for queries with `LIMIT` clauses.
  * Bulk processing or analytical pipelines (for online analytical processing (OLAP) or extract, transform, and load (ETL) workloads): set `group_size` between `5000` and `20000`. Larger batches maximize model throughput and minimize overall query execution time across large datasets.

**Note:** Memory consumption per batch scales proportionally with `group_size` and is strictly bounded by PostgreSQL's `work_mem` setting. If accumulated row arguments reach the `work_mem` threshold before the full `group_size` is collected, AlloyDB dynamically dispatches the batch early to maximize throughput while preventing out-of-memory conditions.

### Manage concurrency and workers

Parallel query execution distributes batch evaluation across background workers under a `Gather` node. To optimize parallel throughput, consider the following:

  * For heavy analytical scans, ensure `max_parallel_workers_per_gather` and `max_parallel_workers` are set appropriately to maximize parallel throughput.
  * For interactive workloads or environments with strict Vertex AI rate limits, reducing worker counts prevents concurrent queries from competing for model quota.



### Manage memory

Smart batching automatically bounds memory usage using PostgreSQL's `work_mem` setting, dynamically dispatching batches when memory thresholds are reached to prevent excessive resource consumption. Ensure `work_mem` is appropriately sized if processing very large text prompts or batches.

### Optimize costs

Only rows that pass all non-AI relational predicates are sent to the model. Whenever query semantics permit, applying selective relational SQL filters, such as date ranges, status codes, or categorical filters, reduces the number of candidate rows sent to the model. This reduces model invocation costs and execution latency.

## Troubleshoot

The following sections describe common issues and remediation steps when running accelerated AI queries.

### Query not using acceleration

If your query isn't using smart batching, but you expect it to, consider the following:

  * Check extension flag: verify that `SHOW google_ml_integration.enable_ai_function_acceleration;` returns `on`.
  * Inspect unsupported patterns: verify that your query doesn't contain any unsupported query patterns.
  * Run `DEBUG2` diagnosis: run `SET client_min_messages TO DEBUG2;` followed by `EXPLAIN SELECT ...;` to view the specific reason AI function acceleration was skipped. Make sure to run `RESET client_min_messages;` immediately after running `EXPLAIN` to prevent your session from being flooded with debug messages during normal query operations. For example:
        
        SET client_min_messages TO DEBUG2;
        EXPLAIN SELECT ...;
        RESET client_min_messages;
        

  * Prepared statements: PostgreSQL caches query plans for prepared statements. If you toggled acceleration flags, run `DEALLOCATE ALL;` to recompile cached plans.




### Handle quota exhaustion

If you experience `HTTP 429` or rate limit errors, this is likely because smart batching is processing too many rows concurrently and increasing API consumption. To avoid quota exhaustion, consider the following:

  * Token quotas (TPM): make sure that your Google Cloud project has adequate Tokens Per Minute (TPM) quota for your target model in the target region. To increase your TPM quota, see [Request a TPM quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota).
  * Agent Platform API rate limits: make sure that your Google Cloud project has sufficient Agent Platform API quota. To request a quota increase for your Agent Platform model, see [Request an API quota increase](https://docs.cloud.google.com/docs/quotas/help/request_increase).
  * Parallel queries: If parallel workers exhaust Agent Platform quotas, then reduce parallelism for the session:
        
        SET max_parallel_workers_per_gather = 0;
        

  * Non-parallel queries: for non-parallel queries experiencing rate limits, reduce the batch group size:
        
        SET google_ml_integration.ai_function_acceleration_group_size = 500;
        




## What's next

  * [Perform intelligent SQL queries using AI functions](https://docs.cloud.google.com/alloydb/docs/ai/evaluate-semantic-queries-ai-operators).
  * [Accelerate AI queries using optimized functions](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions).
  * [Configure Vertex AI integration](https://docs.cloud.google.com/alloydb/docs/ai/configure-vertex-ai).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
