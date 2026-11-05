---
url: https://docs.cloud.google.com/alloydb/docs/tune-sql-queries-ai/
title: Tune SQL queries using AI \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-05T00:18:17.774471+00:00
---

# Tune SQL queries using AI  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/tune-sql-queries-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Tune SQL queries using AI Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To optimize AlloyDB for PostgreSQL database query performance, you can tune your SQL queries by using AI-driven insights. By analyzing your query execution plans, the `ai.tune_sql` function—powered by a large language model (LLM)—identifies complex bottlenecks and provides recommendations that you can act on for optimization.

**Note** : The `ai.tune_sql` function is available starting with version 1.6.2 of the `google_ml_integration` extension ([Preview](https://docs.cloud.google.com/products#product-launch-stages)). 

When you invoke the `ai.tune_sql` function, it analyzes your query and provides query insights and recommendations in the following areas:

  * **Query summary** : analyzes query performance bottlenecks.
  * **Query rewrite** : suggests optimization techniques to rewrite the original query into an equivalent, more efficient query.
  * **Index recommendations** : recommends index types such as indexes on expressions, Generalized Inverted Index (GIN) indexes, and Scalable Nearest Neighbors (ScaNN) indexes.
  * **Statistics collection recommendations** : recommends table [`ANALYZE`](https://www.postgresql.org/docs/18/sql-analyze.html) and statistics collection on multiple columns based on the query execution plan.
  * **Grand Unified Configuration (GUC) flags tuning** : recommends new GUC values by analyzing the execution plan and system information such as memory and buffer usage and size.
  * **Analyze and vacuum** : recommends running `ANALYZE` and `VACUUM` on tables based on the analyze and vacuum history and the live and dead tuple counts.



## Limitations

SQL query tuning has the following limitations:

  * **Prepared and parameterized statements** : for prepared and parameterized statements, `ai.tune_sql` doesn't provide query rewrite recommendations, although it still provides other tuning recommendations. To receive query rewrite recommendations for a query that contains parameter placeholders, such as `$1` or `$2` copied from Query Insights or `pg_stat_statements`, replace the placeholders with representative literal values before running `ai.tune_sql`.
  * **Read-only`SELECT` statements only when `explain_analyze` is `TRUE`**: only single, read-only `SELECT` statements are supported when `explain_analyze` is set to `TRUE`. Running `ai.tune_sql` with `explain_analyze` set to `TRUE` on other statements—such as `INSERT`, `UPDATE`, `DELETE`, `SELECT INTO`, or `SELECT FOR UPDATE`—returns an error message.



## Before you begin

Verify that you have the following:

  * An AlloyDB instance running PostgreSQL 18 or later. For more information, see [Create a cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create).
  * A [`psql` client connected to your instance](https://docs.cloud.google.com/alloydb/docs/connect-psql), or [access to AlloyDB Studio](https://docs.cloud.google.com/alloydb/docs/manage-data-using-studio).
  * [Vertex AI integration enabled](https://docs.cloud.google.com/alloydb/docs/ai/configure-vertex-ai).
  * [Version 1.6.2 or later of the `google_ml_integration` extension installed](https://docs.cloud.google.com/alloydb/docs/ai/configure-vertex-ai#verify-installed-extension), and the `google_db_advisor` and `hypopg` extensions enabled. To enable the `hypopg` extension, which `ai.tune_sql` uses to evaluate and generate index recommendations, run `CREATE EXTENSION IF NOT EXISTS hypopg;`.



## Enable SQL tuning

Register an LLM and enable the required database flags.

  1. Create a [Gemini model](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/models) endpoint for the `ai.tune_sql` function by registering either a global model endpoint or a regional model endpoint in your instance region:

     * To register a global model endpoint when the model isn't available in your instance region—for example, `gemini-3.5-flash` on `locations/global`—run the following statement:
           
           CALL google_ml.create_model(
             model_id => 'gemini-3.5-flash-global',
             model_request_url => 'https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/publishers/google/models/gemini-3.5-flash:generateContent',
             model_qualified_name => 'gemini-3.5-flash',
             model_provider => 'google',
             model_type => 'llm',
             model_auth_type => 'alloydb_service_agent_iam');
           

Replace `PROJECT_ID` with the ID of the project where the model is available.

     * To register a regional model endpoint in your instance region—for example, `gemini-2.5-pro` on `locations/REGION_ID`—run the following statement:
           
           CALL google_ml.create_model(
             model_id => 'gemini-2.5-pro',
             model_request_url => 'https://REGION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION_ID/publishers/google/models/gemini-2.5-pro:generateContent',
             model_qualified_name => 'gemini-2.5-pro',
             model_provider => 'google',
             model_type => 'llm',
             model_auth_type => 'alloydb_service_agent_iam');
           

Replace the following:

       * `REGION_ID`: the region of your AlloyDB instance—for example, `us-central1`.
       * `PROJECT_ID`: the ID of the project where the model is available.
  2. Set the model ID for SQL query tuning recommendations in your current database session. Specify the `model_id` that you registered in the previous step, such as `'gemini-3.5-flash-global'` or `'gemini-2.5-pro'`:
         
         SET google_db_advisor.llm_model_id = 'gemini-3.5-flash-global';
         

  3. Turn on SQL query tuning for your current database session by setting the `google_db_advisor.enable_ai_tune_sql` flag:
         
         SET google_db_advisor.enable_ai_tune_sql = on;
         

Because `SET` applies only to the current database session, you can persist these settings across sessions by running `ALTER DATABASE DATABASE_NAME SET FLAG_NAME = VALUE;` for both flags, or by [configuring the instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).




## Manually tune SQL queries

To manually tune SQL queries, run the `ai.tune_sql` function by using a `SELECT` statement.

  1. [Connect a `psql` client](https://docs.cloud.google.com/alloydb/docs/connect-psql) to an AlloyDB instance or [open AlloyDB Studio](https://docs.cloud.google.com/alloydb/docs/manage-data-using-studio).

If you used `SET` to configure `google_db_advisor.llm_model_id` and `google_db_advisor.enable_ai_tune_sql`, run those `SET` statements in the same database session before calling `ai.tune_sql`.

  2. To tune SQL queries, run the `ai.tune_sql` function. This function retrieves the query-related schema and sends it, along with the query, to the LLM for performance analysis:
         
         SELECT ai.tune_sql(query => 'SQL_QUERY', explain_analyze => TRUE);
         

Replace `SQL_QUERY` with the SQL query that you want to analyze.

By default, the execution parameter (`explain_analyze`) is set to `TRUE`. When set to `TRUE`, the function runs `EXPLAIN ANALYZE` to execute the query and capture the execution plan. This approach provides more accurate and useful query tuning advice. If you set `explain_analyze` to `FALSE`, the function only runs `EXPLAIN` to generate a plan without executing the query.




### View query plans with performance recommendations

The output first shows the standard query plan, followed by the detailed AI-generated recommendations. The recommendations include a query summary, suggested rewrites, and recommendations for statistics collection, GUC flag tuning, and vacuuming. The `ai.tune_sql` function can take two to four minutes to generate recommendations.

The following example shows the `ai.tune_sql` output for an anti-join query:
    
    
    SELECT ai.tune_sql(
      'SELECT *
       FROM store_sales
       WHERE ss_customer_sk NOT IN (
         SELECT sr_customer_sk
         FROM store_returns
         WHERE sr_item_sk = ss_item_sk)');
    
                         tune_sql
    --------------------------------------------------
     NOTE
     --------------------------------------------------
     Advices generated with the assistance of an LLM. Independent verification of these advices is required due to the potential for inaccuracies.
     --------------------------------------------------
     ORIGINAL QUERY PLAN
     --------------------------------------------------
     Seq Scan on store_sales  (cost=0.00..111292742.52 rows=1440384 width=115) (actual time=0.092..103093.207 rows=1306312.00 loops=1)
       Filter: (NOT (ANY (ss_customer_sk = (SubPlan 1).col1)))
       Rows Removed by Filter: 1574198
       Buffers: shared hit=72987539
       SubPlan 1
         ->  Index Scan using idx_sr_item_sk on store_returns  (cost=0.42..76.74 rows=18 width=4) (actual time=0.005..0.034 rows=19.38 loops=2880510)
               Index Cond: (sr_item_sk = store_sales.ss_item_sk)
               Index Searches: 2880510
               Buffers: shared hit=72933670
     Planning Time: 0.257 ms
     --------------------------------------------------
     QUERY SUMMARY
     --------------------------------------------------
     The original query plan shows a Sequential Scan on store_sales with a correlated SubPlan for the NOT IN condition. For each of the 1.44 million rows in store_sales, it executes an Index Scan on store_returns, resulting in over 2.88 million index searches. This nested loop execution is the primary bottleneck, taking over 103 seconds. Converting the correlated NOT IN subquery to an anti-join (NOT EXISTS) will allow the optimizer to use a Hash Anti Join, processing both tables in bulk and significantly reducing execution time.
     --------------------------------------------------
     AI SUGGESTED QUERY 1
     --------------------------------------------------
     SELECT * FROM store_sales WHERE NOT EXISTS (SELECT 1 FROM store_returns WHERE store_returns.sr_item_sk = store_sales.ss_item_sk AND (store_returns.sr_customer_sk = store_sales.ss_customer_sk OR store_returns.sr_customer_sk IS NULL OR store_sales.ss_customer_sk IS NULL));
     Reason: The original query uses a NOT IN subquery which is executed as a correlated subquery (SubPlan), leading to millions of index scans. Rewriting to NOT EXISTS allows the optimizer to use a Hash Anti Join, which is much more efficient for large datasets. The OR IS NULL conditions ensure strict semantic equivalence with NOT IN when dealing with NULL values.
     --------------------------------------------------
     REWRITTEN QUERY PLAN
     --------------------------------------------------
     Gather  (cost=8541.96..139088.40 rows=154194 width=115)
       Workers Planned: 2
       ->  Parallel Hash Anti Join  (cost=7541.96..122669.00 rows=64248 width=115)
             Hash Cond: (store_sales.ss_item_sk = store_returns.sr_item_sk)
             Join Filter: ((store_returns.sr_customer_sk = store_sales.ss_customer_sk) OR (store_returns.sr_customer_sk IS NULL) OR (store_sales.ss_customer_sk IS NULL))
             ->  Parallel Seq Scan on store_sales  (cost=0.00..65872.20 rows=1200320 width=115)
             ->  Parallel Hash  (cost=6044.76..6044.76 rows=119776 width=8)
                   ->  Parallel Seq Scan on store_returns  (cost=0.00..6044.76 rows=119776 width=8)
     --------------------------------------------------
     AI SUGGESTED INDEX 1
     --------------------------------------------------
     CREATE INDEX idx_sr_item_customer ON store_returns (sr_item_sk, sr_customer_sk);
     Reason: A composite index on (sr_item_sk, sr_customer_sk) allows index-only scans for the subquery or early aggregation, reducing table access and speeding up the anti-join condition evaluation.
     Note: Indexes are suggested solely based on the given query, but they don't consider the overall system workload.
               The suggested indexes improve the performance of the original query.
     --------------------------------------------------
     GUC FLAGS TUNING
     --------------------------------------------------
     SET work_mem = '64MB'; The current work_mem of 4MB is too small for a Hash Anti Join on tables with hundreds of thousands of rows. Increasing it to 64MB allows the hash table for store_returns to fit entirely in memory, preventing costly disk spills during the join.
    
     Execution Time: 103167.475 ms
    (50 rows)
    

## What's next

  * [Learn about query insights](https://docs.cloud.google.com/alloydb/docs/query-insights-overview).
  * [Apply index recommendations](https://docs.cloud.google.com/alloydb/docs/use-index-advisor).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
