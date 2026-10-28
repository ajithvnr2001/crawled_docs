---
url: https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/
title: Query Explain report reference \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:05:49.808962+00:00
---

# Query Explain report reference  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/

[ Skip to main content ](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/)
  * [Deutsch](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/?hl=de)
  * [Español](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/?hl=es-419)
  * [Français](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/?hl=id)
  * [Italiano](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/?hl=it)
  * [Português](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/?hl=ja)
  * [한국어](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fdatastore%2Fdocs%2Fquery-explain-analyze-report-reference%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/datastore/docs)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Plan records](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/#plan_records)
    * [Indexes used](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/#query-analyze-reference-indexes-used)
  * [Execution statistics](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/#query-analyze-reference-execution-stats)
    * [Debug statistics](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/#query-analyze-reference-debug-stats)
  * [What's next](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Guides ](https://docs.cloud.google.com/datastore/docs/concepts/overview)


Was this helpful?
Send feedback 
#  Query Explain report reference Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Plan records](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/#plan_records)
    * [Indexes used](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/#query-analyze-reference-indexes-used)
  * [Execution statistics](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/#query-analyze-reference-execution-stats)
    * [Debug statistics](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/#query-analyze-reference-debug-stats)
  * [What's next](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/#whats_next)


The following values are returned as results to operations performed with [Query Explain](https://docs.cloud.google.com/datastore/docs/query-explain-analyze).
## Plan records  
| Key  | Type  | Subject to change?  | Description  |  
| --- | --- | --- | --- |  
| indexes_used   | List of [Generic Structs](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)  | Yes, the contents in the Struct response are subject to change.   | List of indexes selected for this query. See [below](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/#query-analyze-reference-indexes-used).   |  
### Indexes used
The contents of indexes used are subject to change as Datastore mode evolves.  
| Key  | Type  | Description  |  
| --- | --- | --- |  
| query_scope   | String   | The scope at which a query is run. For example `Collection`, `Collection Group` and `Includes Ancestors`.   |  
| properties   | String   | The index fields in a format, for example `(age ASC, __name__ ASC)`.   |  
## Execution statistics
Aggregated execution statistics for the query.  
| Key   | Type   | Field subject to change?   | Description   |  
| --- | --- | --- | --- |  
| results_returned   | long   | No   | Total number of results returned, including entities, projections, aggregation results, keys.   |  
| execution_duration   | Duration   | No   | Total time to execute the query in the backend.   |  
| read_operations   | long   | No   | Total billable read operations.   |  
| debug_stats   | Generic Struct   | Yes, the contents in the Struct response are subject to change.   | Debugging statistics from the execution of the query. See [below](https://docs.cloud.google.com/datastore/docs/query-explain-analyze-report-reference/#query-analyze-reference-debug-stats).   |  
### Debug statistics
The following results are helpful for debugging use cases and analysis of raw, optional statistics.
The contents of debug stats are subject to change as Datastore mode evolves.  
| Key   | Type   | Description   |  
| --- | --- | --- |  
| index_entries_scanned   | String   | Total number of index entries inspected during the query.   |  
| documents_scanned   | String   | Total number of documents scanned during the query.   |  
| billing_details   | Generic Struct   | Billing details including metrics like: "documents_billable", "index_entries_billable", "min_query_cost".   |  
## What's next
  * [Learn more about running queries with explain and analyze](https://docs.cloud.google.com/datastore/docs/query-explain-analyze)
  * [Learn more about optimizing queries and indexes](https://docs.cloud.google.com/datastore/docs/concepts/optimize-indexes)


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
