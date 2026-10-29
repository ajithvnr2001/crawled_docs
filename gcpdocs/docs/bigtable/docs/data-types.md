---
url: https://docs.cloud.google.com/bigtable/docs/data-types/
title: Data type enforcement in Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T10:18:43.833172+00:00
---

# Data type enforcement in Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/data-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data type enforcement in Bigtable

**Note:** This page includes features that are available only in the Enterprise Plus edition. For more information, see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview).

Bigtable's flexible schema lets you store data of any type – strings, dates, numbers, JSON documents, or even images or PDFs – in a Bigtable table.

This document describes when Bigtable enforces type, requiring you to encode or decode it in your application code. For a list of Bigtable data types, see [Type](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#type_1) in the Data API reference documentation.

## Enforced types

Data type is enforced for the following data:

  * Aggregate column families (counters)
  * Timestamps
  * Continuous materialized views
  * Structured row keys



### Aggregates

For the _aggregate_ data type, encoding depends on the aggregation type. When you create an aggregate column family, you must specify an aggregation type.

This table shows the input type and encoding for each aggregation type.

**Aggregate type** |  **Input type** |  **Encoding**  
---|---|---  
Sum  |  Int64  |  `[BigEndianBytes](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#google.bigtable.v2.Type.Int64.Encoding.BigEndianBytes)`  
Min  |  Int64  |  `[BigEndianBytes](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#google.bigtable.v2.Type.Int64.Encoding.BigEndianBytes)`  
Max  |  Int64  |  `[BigEndianBytes](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#google.bigtable.v2.Type.Int64.Encoding.BigEndianBytes)`  
HLL  |  Bytes  |  [Zetasketch HLL++](https://github.com/google/zetasketch)  
  
When you query the data in aggregate cells using SQL, SQL automatically incorporates type information.

When you read the data in aggregate cells using the Data API's `ReadRows` method, Bigtable returns bytes, so your application must decode the values using the encoding that Bigtable used to map the typed data to bytes.

You can't convert a column family that contains non-aggregate data into an aggregate column family. Columns in aggregate column families can't contain non-aggregate cells, and standard column families can't contain aggregate cells.

For more information about creating tables with aggregate column families, see [Create a table](https://docs.cloud.google.com/bigtable/docs/managing-tables#create-table). For code samples that show how to increment an aggregate cell with encoded values, see [Increment a value](https://docs.cloud.google.com/bigtable/docs/writing-data#increment-append).

### Timestamps

Each Bigtable cell has an `Int64` timestamp that represents the number of microseconds since the [Unix epoch](https://wikipedia.org/wiki/Unix_time), `1970-01-01 00:00:00 UTC`.

#### Timestamp origin

Every timestamp in a Bigtable table has an origin that indicates how the timestamp was set. Bigtable recognizes the following timestamp origins:

  * **User-specified** : timestamps set by you or by an application.
  * **Bigtable-generated** : timestamps set by the client library that uses the client's local system clock or server-generated that use the server's current time.



#### Timestamp granularity and precision

Bigtable supports the following levels of timestamp granularity:

  * **Millisecond granularity (default)** : the timestamp must be a microsecond value with at most millisecond precision, such as `3023483279876000`. Bigtable rejects user-specified timestamps with microsecond precision and truncates Bigtable-generated timestamps with microsecond precision to millisecond precision.
  * **Microsecond granularity** : the timestamp can have full microsecond precision, such as `3023483279876543`. Bigtable accepts user-specified and Bigtable-generated timestamps with microsecond precision.



You set timestamp granularity when you [create a table](https://docs.cloud.google.com/bigtable/docs/managing-tables#create-table).

#### Timestamp limitations

The following limitations apply to tables with microsecond timestamp granularity:

  * Only the [Bigtable client library for Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/overview) version 2.82.0 or later supports microsecond timestamp granularity. Read or write requests that use another client fail.
  * Microsecond timestamp granularity is available only for instances in the Enterprise Plus edition.
  * You can't change the timestamp granularity of a table after it's created.
  * You can't create [continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views) on tables with microsecond granularity.
  * You can't create [logical views](https://docs.cloud.google.com/bigtable/docs/create-manage-logical-views) on tables with microsecond granularity.
  * You can't downgrade an instance from Enterprise Plus to Enterprise if it contains any tables with microsecond granularity. You must delete these tables before you start a downgrade.
  * Backups of tables with microsecond granularity can only be restored to Enterprise Plus instances.



### Continuous materialized views

Continuous materialized views are read-only resources that you can read by using SQL or with a `ReadRows` Data API call. Data in a materialized view is typed based on the query that defines it. For an overview, see [Continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views).

When you use SQL to query a continuous materialized view, SQL automatically incorporates type information.

When you [read from a continuous materialized view](https://docs.cloud.google.com/bigtable/docs/reads#reads-continuous-materialized-views) using a Data API `ReadRows` request, you must know each column's type and decode it in your application code.

Aggregated values in a continuous materialized view are stored using encoding described in the following table, based on the output type of the column from the view definition. 

**Type** | **Encoding**  
---|---  
BOOL | 1 byte value, 1 = true, 0 = false  
BYTES | No encoding  
INT64 (or INT, SMALLINT, INTEGER, BIGINT, TINYINT, BYTEINT) | 64-bit big-endian  
FLOAT64 | 64-bit IEEE 754, excluding NaN and +/-inf  
STRING | UTF-8  
TIME/TIMESTAMP | 64-bit integer representing the number of microseconds since the Unix epoch (consistent with GoogleSQL)  
For more information, see [ Encoding](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#encoding_1) in the Data API reference. 

### Structured row keys

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Structured row keys let you access your data using multi-column keys, similar to composite keys in relational databases.

The type and encoding for structured row keys are defined by a _row key schema_ that you can optionally add to a Bigtable table. Structured row key data is stored as bytes, but GoogleSQL for Bigtable automatically uses the type and encoding defined in the row key schema when you execute a SQL query on the table.

Using a row key schema to query a table with a `ReadRows` request isn't supported. A continuous materialized view has a row key schema by default. For more information about structured row keys, see [Manage row key schemas](https://docs.cloud.google.com/bigtable/docs/manage-row-key-schemas).

## Unenforced types

If no type information is provided, then Bigtable treats each cell as bytes with an unknown encoding.

When querying column families that are created without type enforcement, you must provide type information at read time to ensure that the data is read correctly. This is relevant with database functions whose behavior depends on the data type. GoogleSQL for Bigtable offers [CAST](https://docs.cloud.google.com/bigtable/docs/reference/sql/conversion_functions#cast) functions to do type conversions at query time. These functions convert from bytes to the types that various functions expect.

While Bigtable doesn't enforce types, certain operations assume a data type. Knowing this helps you ensure that your data is written in a way that can be processed within the database. The following are examples:

  * Increments using `ReadModifyWriteRow` assume the cell contains a 64-bit big-endian signed integer.
  * The `TO_VECTOR64` function in SQL expects the cell to contain a byte array that's a concatenation of the big-endian bytes of 64-bit floating point numbers.
  * The `TO_VECTOR32` function in SQL expects the cell to contain a byte array that's a concatenation of the big-endian bytes of 32-bit floating point numbers.



## What's next

  * [Reads](https://docs.cloud.google.com/bigtable/docs/reads)
  * [GoogleSQL for Bigtable overview](https://docs.cloud.google.com/bigtable/docs/googlesql-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
