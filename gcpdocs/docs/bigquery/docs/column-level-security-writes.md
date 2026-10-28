---
url: https://docs.cloud.google.com/bigquery/docs/column-level-security-writes/
title: Impact on writes from column-level access control \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: httpx+scrapegraph (scrapling: scrapling status 429 | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 1299 in create_browser_context (../../../../usr/local/lib/python3.10/dist-packages/crawl4ai/browser_manager.py):
Error: Browser is not available. It may have been closed, crashed, or not yet started. Ensure the browser is running before creating new contexts.

Code context:
1294                   raise RuntimeError(
1295                       "Cannot create new browser contexts when using "
1296                       "use_persistent_context=True. Persistent context uses a "
1297                       "single shared context."
1298                   )
1299 →             raise RuntimeError(
1300                   "Browser is not available. It may have been closed, crashed, "
1301                   "or not yet started. Ensure the browser is running before "
1302                   "creating new contexts."
1303               )
1304           # Base settings)
fetched_at: 2026-10-27T16:23:01.684600+00:00
---

# Impact on writes from column-level access control  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/column-level-security-writes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Impact on writes from column-level access control

This page explains the impact to writes when you use BigQuery column-level access control to restrict access to data at the column level. For general information about column-level access control, see [Introduction to BigQuery column-level access control](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro).

Column-level access control requires a user to have read permission for columns that are protected by policy tags. Some write operations need to read column data before actually writing into a column. For those operations, BigQuery checks the user's read permission to ensure the user has access to the column. For example, if a user is updating data that includes writing to a protected column, the user must have read permission for the protected column. If the user is inserting a new data row that includes writing to a protected column, the user doesn't need read access for the protected column. But, the user who writes such a row won't be able to read the newly written data unless the user has read permission for the protected columns.

The following sections provide details about different types of write operations. The examples in this topic use `customers` tables with the following schema:

Field name | Type | Mode | Policy tag  
---|---|---|---  
`user_id` | STRING | REQUIRED | `policy-tag-1`  
`credit_score` | INTEGER | NULLABLE | `policy-tag-2`  
`ssn` | STRING | NULLABLE | `policy-tag-3`  
  
## Using BigQuery data manipulation language (DML)

### Inserting data

For an `INSERT` statement, BigQuery does not check Fine-Grained Reader permission on the policy tags on either the scanned columns or the updated columns. This is because an `INSERT` does not require reading any of the column data. But, even if you successfully insert values into columns where you don't have read permission, once inserted, the values are protected as expected.

### Deleting, updating, and merging data

For `DELETE`, `UPDATE`, and `MERGE` statements, BigQuery checks for the Fine-Grained Reader permission on the scanned columns. Columns aren't scanned by these statements unless you include a [`WHERE` clause](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#where_clause), or some other clause or subquery that requires the query to read data.

### Loading data

When loading data (for example, from Cloud Storage or local files) to a table, BigQuery does not check the Fine-Grained Reader permission on the columns of the destination table. This is because loading data does not require reading content from the destination table.

Streaming into BigQuery is similar to `LOAD` and `INSERT`. BigQuery lets you stream data into a destination table column, even if you don't have the Fine-Grained Reader permission.

### Copying data

For a copy operation, BigQuery checks whether the user has the Fine-Grained Reader permission on the source table. BigQuery does not check whether the user has the Fine-Grained Reader permission to the columns in the destination table. Like `LOAD`, `INSERT`, and streaming, once the copy is complete, you won't be able to read the data that was just written, unless you have the Fine-Grained Reader permission to the destination table's columns.

## DML examples

### `INSERT`

**Example:**
    
    
    INSERT INTO customers VALUES('alice', 85, '123-456-7890');
    

| Source columns | Update columns  
---|---|---  
Policy tags checked for Fine-Grained Reader? | N/A | No  
Columns checked | N/A | `user_id`  
`credit_score`  
`ssn`  
  
### `UPDATE`

**Example:**
    
    
    UPDATE customers SET credit_score = 0
      WHERE user_id LIKE 'alice%' AND credit_score < 30
    

| Source columns | Update columns  
---|---|---  
Policy tags checked for Fine-Grained Reader? | Yes | No  
Columns checked | `user_id`  
`credit_score` | `credit_score`  
  
### `DELETE`

**Example:**
    
    
    DELETE customers WHERE credit_score = 0
    

| Source columns | Update columns  
---|---|---  
Policy tags checked for Fine-Grained Reader? | Yes | No  
Columns checked | `credit_score` | `user_id`  
`credit_score`  
`ssn`  
  
## Load examples

### Loading from a local file or Cloud Storage

**Example:**
    
    
    load --source_format=CSV samples.customers \
      ./customers_data.csv \
      ./customers_schema.json
    

| Source columns | Update columns  
---|---|---  
Policy tags checked for Fine-Grained Reader? | N/A | No  
Columns checked | N/A | `user_id`  
`credit_score`  
`ssn`  
  
### Streaming

No policy tags are checked when streaming with the BigQuery Storage Write API (REST) or the Storage Write API (gRPC). For [BigQuery change data capture ingestion](https://docs.cloud.google.com/bigquery/docs/change-data-capture), the policy tags are checked on the primary key columns.

## Copy examples

### Appending data to an existing table

**Example:**
    
    
    cp -a samples.customers samples.customers_dest
    

| Source columns | Update columns  
---|---|---  
Policy tags checked for Fine-Grained Reader? | Yes | No  
Columns checked | `customers.user_id`  
`customers.credit_score`  
`customers.ssn` | `customers_dest.user_id`  
`customers_dest.credit_score`  
`customers_dest.ssn`  
  
### Saving query results to a destination table

**Example:**
    
    
    query --use_legacy_sql=false \
    --max_rows=0 \
    --destination_table samples.customers_dest \
    --append_table "SELECT * FROM samples.customers LIMIT 10;"
    

| Source columns | Update columns  
---|---|---  
Policy tags checked for Fine-Grained Reader? | Yes | No  
Columns checked | `customers.user_id`  
`customers.credit_score`  
`customers.ssn` | `customers_dest.user_id`  
`customers_dest.credit_score`  
`customers_dest.ssn`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
