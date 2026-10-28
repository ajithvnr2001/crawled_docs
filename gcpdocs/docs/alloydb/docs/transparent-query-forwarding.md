---
url: https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/
title: Optimize resources and isolate read queries with transparent query forwarding \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:42:43.439281+00:00
---

# Optimize resources and isolate read queries with transparent query forwarding  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/

[ Skip to main content ](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/)
  * [Deutsch](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/?hl=es-419)
  * [Français](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/?hl=id)
  * [Italiano](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/?hl=ja)
  * [한국어](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/alloydb-color.svg) ](https://docs.cloud.google.com/alloydb/docs)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/#before-you-begin)
    * [Required roles](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/#required-roles)
  * [Enable transparent query forwarding](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/#enable-transparent-query-forwarding)
    * [Enable at the session level](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/#enable-session)
    * [Enable at the database level](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/#enable-database)
  * [Query eligibility conditions](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/#query-eligibility-conditions)
  * [Verify query eligibility with EXPLAIN](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/#verify-query-eligibility)
  * [Monitor query forwarding metrics](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/#monitor-query-forwarding-metrics)
  * [What's next](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/#whats-next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)


Was this helpful?
Send feedback 
#  Optimize resources and isolate read queries with transparent query forwarding Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/#before-you-begin)
    * [Required roles](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/#required-roles)
  * [Enable transparent query forwarding](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/#enable-transparent-query-forwarding)
    * [Enable at the session level](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/#enable-session)
    * [Enable at the database level](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/#enable-database)
  * [Query eligibility conditions](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/#query-eligibility-conditions)
  * [Verify query eligibility with EXPLAIN](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/#verify-query-eligibility)
  * [Monitor query forwarding metrics](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/#monitor-query-forwarding-metrics)
  * [What's next](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/#whats-next)


To offload read traffic from your primary instance without sacrificing read-your-writes consistency or modifying application connection endpoints, you can enable, configure, and monitor transparent query forwarding in your AlloyDB for PostgreSQL instances. Transparent query forwarding intercepts read-only queries on the primary node and selectively routes them to underutilized [read pool instances](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create), returning results consistent with primary node execution.
![transparent query forwarding](https://docs.cloud.google.com/alloydb/images/tqf-diag.png?dcb_=0.6566335171101625)
Transparent query forwarding is best-suited for the following scenarios:
  * Hybrid workloads (HTAP): you run reporting or analytical queries, with read-your-writes consistency, on the same database that handles transactions, and you want to prevent expensive reads from impacting write latency.
  * Monolithic applications: You want to use read pool capacity without refactoring your application to use separate reader and writer endpoints, while still requiring strict read-your-writes consistency.
  * Dynamic load management: You experience unpredictable spikes in read traffic and you want the database to automatically offload work to read pool nodes when the primary node is under heavy load with read-your-writes consistency.


## Before you begin
  * Make sure your AlloyDB cluster is compatible with PostgreSQL 17 or 18.
  * You must have at least one active read pool instance configured in your AlloyDB cluster. For information about creating or verifying read pool instances, see [Create a read pool instance in a cluster](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create) and [View instance details](https://docs.cloud.google.com/alloydb/docs/instance-view).


### Required roles
  * Make sure that you connect using a [built-in database user](https://docs.cloud.google.com/alloydb/docs/database-users/built-in-authentication), such as `postgres`. [IAM-based authentication](https://docs.cloud.google.com/alloydb/docs/database-users/iam-authentication) isn't supported.


## Enable transparent query forwarding
Transparent query forwarding is disabled by default. You can enable it dynamically at the session level or the database level without restarting the database.
### Enable at the session level
To enable transparent query forwarding for your current session, run the following SQL command:

```
SET alloydb.enable_query_forwarding = TRUE;

```

### Enable at the database level
To enable transparent query forwarding for a specific database, run the following SQL command:

```
ALTER DATABASE DATABASE_NAME SET alloydb.enable_query_forwarding = ON;

```

Replace `DATABASE_NAME` with the name of your database.
## Query eligibility conditions
  * Transparent query forwarding applies only to read-only `SELECT` statements.
  * The query must not take any row-level locks, such as those used in `SELECT ... FOR UPDATE`.
  * Transparent query forwarding has limited support for `SELECT` statements within multi-statement transactions.
  * Queries cannot reference temporary, unlogged, or catalog tables.
  * The query must adhere to the following function constraints: 
    * The query must not contain volatile functions or any user-defined functions (UDFs).
    * The query must not contain SQL value functions such as `CURRENT_DATE`, `LOCALTIME`, `USER`, or `CURRENT_SCHEMA`.
    * The query must not contain `NEXTVAL()` expressions.
    * The query cannot contain any SQL procedures or SQL functions.
  * All result columns must use data types that implement binary send and receive functions.
  * A query is only eligible for forwarding if its overhead cost is minimal compared to the query's total cost. This means queries using index scans are typically excluded, as their overhead usually exceeds the cost of the query itself.
  * Forwarding to a AlloyDB hot standby node is not supported. A AlloyDB hot standby node is a dedicated secondary node for high availability (HA) primary instances.
  * The query must use the [simple query protocol](https://www.postgresql.org/docs/17/protocol-flow.html#PROTOCOL-FLOW-SIMPLE-QUERY). Extended query protocol is not supported.


## Verify query eligibility with EXPLAIN
In the following example, `large_table` is a table in a database with many rows. To check whether a specific query is eligible for forwarding under your current configuration, run the `EXPLAIN` command:

```
EXPLAIN SELECT count(*) FROM large_table t1, large_table t2;

```

If the query is eligible, the output includes a query forwarding status statement after the standard Postgres execution plan. If this statement is missing, then the query is not eligible for query forwarding and executes locally on the primary.

```
Aggregate  (cost=25000.00..25000.01 rows=1 width=8)
  ->  Nested Loop  (cost=0.00..20000.00 rows=1000000 width=0)
        ... [Standard Postgres Plan Steps] ...
Query Forwarding: Eligible. (overhead=1250.02)

```

In the output response, `Eligible` indicates that the query meets standard read-only SQL criteria and the cost-benefit analysis favors routing it to a read pool instance. The `overhead` parameter indicates the calculated planner cost of forwarding the query to a read pool instance, including the overhead of establishing the connection and restoring snapshots on the replica.
## Monitor query forwarding metrics
To verify that transparent query forwarding is working across your workload, you can track the following metric in Cloud Monitoring:  
| Metric  | Description  | Details  |  
| --- | --- | --- |  
| `alloydb.googleapis.com/internal/database/postgresql/workload/distributed/tqf_query_count`  | The cumulative count of queries handled by transparent query forwarding.  |  **Display Name:** TQF query count  
**Metric Kind:** CUMULATIVE  
**Value Type:** INT64  
**Labels:**  
`status`: Query handling if transparent query forwarding is enabled. This label records one of the following values: 
  * `completed`: executed on a read pool instance.
  * `fallback`: executed on the primary.
  * `disqualified`: couldn't be forwarded.

 |  
## What's next
  * [Create a read pool instance in a cluster](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create)
  * [Monitor instances](https://docs.cloud.google.com/alloydb/docs/monitor-instance)


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
