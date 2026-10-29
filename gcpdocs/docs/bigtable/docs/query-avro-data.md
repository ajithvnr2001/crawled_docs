---
url: https://docs.cloud.google.com/bigtable/docs/query-avro-data/
title: Query Avro data \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T10:18:52.741376+00:00
---

# Query Avro data  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/query-avro-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Query Avro data

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

GoogleSQL for Bigtable lets you query, filter, and project individual fields from serialized Apache Avro records that Bigtable tables store. By referencing an Avro schema bundle in your SQL queries, you can cast byte columns into structured Avro records and extract nested fields.

Before you query Avro fields, you must upload your Avro schemas in a schema bundle, as described in [Create and manage Avro schemas](https://docs.cloud.google.com/bigtable/docs/create-manage-avro-schemas). To learn how GoogleSQL queries map to Bigtable table schemas and how to reference columns in SQL statements, see the [GoogleSQL for Bigtable overview](https://docs.cloud.google.com/bigtable/docs/googlesql-overview).

To query Avro data with GoogleSQL in Java, use the `executeQuery` method in the Cloud Bigtable client library. For examples of running SQL queries with client libraries, see [Client libraries](https://docs.cloud.google.com/bigtable/docs/googlesql-overview#client-libraries).

## Avro data type mappings

When you cast serialized `BYTES` to an Avro record, GoogleSQL for Bigtable maps the Avro schema types to SQL-accessible types, as follows:

Avro type | GoogleSQL representation | Description  
---|---|---  
`int`, `long` | `INT64` | 32-bit and 64-bit signed integers map to 64-bit integers.  
`float` | `FLOAT32` | A single-precision floating-point value  
`double` | `FLOAT64` | A double-precision floating-point value  
`boolean` | `BOOL` | A boolean value (`TRUE` or `FALSE`)  
`string` | `STRING` | A Unicode character sequence  
`bytes` | `BYTES` | A sequence of raw bytes  
`record` | Message object | Access nested fields using the dot notation (for example, `record.field`).  
`enum` | `ENUM` | An enumerated symbol set  
`array` | `ARRAY` | A repeated field. Bigtable doesn't support nested arrays.  
`map<T>` | Repeated key-value entries | Avro maps have `STRING` keys. Bigtable supports maps with nullable values, such as `{"type": "map", "values": ["null", "string"]}`. You can transform the maps into an `ARRAY<STRUCT<key STRING, value T>>` by using the `ARRAY_TRANSFORM` function.  
`union` | Nullable field | Bigtable maps a union with null and one non-null type to a standard nullable field.  
`fixed` | Bigtable doesn't support the `fixed` type. | A fixed-length byte sequence.   
  
## Example data

The examples on this page use an Avro schema bundle with the `my_avro` ID. This bundle contains the following `Transaction` record schema in the `com.example.billing` namespace:
    
    
    {
      "type": "record",
      "namespace": "com.example.billing",
      "name": "Transaction",
      "fields": [
        {"name": "product_name", "type": "string"},
        {"name": "product_category", "type": "string"},
        {"name": "configs", "type": {"type": "map", "values": "string"}}
      ]
    }
    

A Bigtable table named `table` stores the serialized Avro records in the `cf` column family and the `product` column qualifier (`cf['product']`):

Row key | Column `cf['product']` (stored as serialized `BYTES`, shown as JSON for readability)  
---|---  
`row1` | `{"product_name": "Chips", "product_category": "yummy food", "configs": {"size": "large", "flavor": "BBQ"}}`  
`row2` | `{"product_name": "Apple", "product_category": "yummy food", "configs": {}}`  
`row3` | `{"product_name": "Book", "product_category": "reading", "configs": {"author": "Jane Doe"}}`  
  
## Example queries

After you upload your Avro schema bundle, you can use the `CAST` operator in GoogleSQL for Bigtable to interpret `BYTES` values as an Avro record.

**Caution:** You must query Avro data using the exact schema that you used to write it. Bigtable doesn't support reading Avro records with a mismatched schema because this can cause runtime query failures, data corruption, or incorrectly mapped fields.

### Cast a column and project a field

To cast a `BYTES` value to an Avro record, specify the full record name in the following format:

`SCHEMA_BUNDLE_ID.FULLY_QUALIFIED_RECORD_NAME`

Replace the following:

  * `SCHEMA_BUNDLE_ID`: the ID of the schema bundle
  * `FULLY_QUALIFIED_RECORD_NAME`: the full name of the Avro record, including the namespace defined in your Avro schema—for example, `com.example.billing.Transaction`



If the specified schema bundle or record name doesn't exist, then the query fails with an `INVALID_ARGUMENT` status and a `type not found` error message. If the provided schema can't parse the cell bytes, then the query fails with a `FAILED_PRECONDITION` or `INVALID_ARGUMENT` status.

The following query casts the `cf['product']` column to the `com.example.billing.Transaction` record in the `my_avro` schema bundle and projects the `product_name` field:
    
    
    SELECT
      CAST(cf['product'] AS my_avro.com.example.billing.Transaction).product_name
    FROM
      table;
    

The query returns the following result:

`product_name` (`STRING`)  
---  
Chips  
Apple  
Book  
  
### Filter based on Avro fields

You can use a `WHERE` clause to filter rows based on the values of fields within an Avro record.

The following query filters rows where the `product_category` field equals `"yummy food"`:
    
    
    SELECT
      CAST(cf['product'] AS my_avro.com.example.billing.Transaction).product_name
    FROM
      table
    WHERE
      CAST(cf['product'] AS my_avro.com.example.billing.Transaction).product_category = "yummy food";
    

The query returns the following result:

`product_name` (`STRING`)  
---  
Chips  
Apple  
  
### Access map fields

You can use the `ARRAY_TRANSFORM` function to project key-value pairs from an Avro `map` field as an array of `STRUCT` elements.

The following query projects `product_name` and transforms the `configs` map field into an array of `STRUCT<key STRING, value STRING>` elements:
    
    
    SELECT
      CAST(cf['product'] AS my_avro.com.example.billing.Transaction).product_name,
      ARRAY_TRANSFORM(
        CAST(cf['product'] AS my_avro.com.example.billing.Transaction).configs,
        e -> STRUCT(e.key, e.value)
      ) AS map_array
    FROM
      table;
    

The query returns the following result:

`product_name` (`STRING`) | `map_array` (`ARRAY<STRUCT<key STRING, value STRING>>`)  
---|---  
Chips | `[{"key": "size", "value": "large"}, {"key": "flavor", "value": "BBQ"}]`  
Apple | `[]`  
Book | `[{"key": "author", "value": "Jane Doe"}]`  
  
### Use with views

You can reference Avro schema bundles in [continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views) and [logical views](https://docs.cloud.google.com/bigtable/docs/create-manage-logical-views).

If a continuous materialized view or a logical view references an Avro schema bundle, then you can't delete the bundle. Before you delete the bundle, you must delete any continuous materialized views that reference it. For any logical views that reference the bundle, you must either update the views to remove the reference or delete them.

The following command creates a continuous materialized view that aggregates transaction counts by `product_name`:
    
    
    gcloud bigtable materialized-views create MATERIALIZED_VIEW_ID \
        --instance=INSTANCE_ID \
        --query="SELECT CAST(cf['product'] AS my_avro.com.example.billing.Transaction).product_name AS product, COUNT(*) AS transaction_count FROM table GROUP BY product;"
    

Replace the following:

  * `MATERIALIZED_VIEW_ID`: the ID of the continuous materialized view that references the schema bundle
  * `INSTANCE_ID`: the ID of the Bigtable instance



## What's next

  * Learn how to [create and manage Avro schemas](https://docs.cloud.google.com/bigtable/docs/create-manage-avro-schemas).
  * Learn how to [query protobuf data](https://docs.cloud.google.com/bigtable/docs/query-protobuf-data).
  * Read about [schema design best practices](https://docs.cloud.google.com/bigtable/docs/schema-design).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
