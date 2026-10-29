---
url: https://docs.cloud.google.com/bigtable/docs/create-manage-avro-schemas/
title: Create and manage Avro schemas \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T10:19:19.597453+00:00
---

# Create and manage Avro schemas  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/create-manage-avro-schemas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and manage Avro schemas

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Apache Avro schemas in Bigtable let you query individual fields within Avro records that Bigtable stores as serialized bytes in your columns. To query these fields, upload your JSON-formatted Avro schemas in a _schema bundle_ , a table-level resource that contains one or more of your Avro record schemas. For more information about Apache Avro schemas, see [Apache Avro documentation](https://avro.apache.org/docs/).

Uploading an Avro schema bundle doesn't change how you write data to Bigtable. You continue to write Avro records as serialized bytes. The cell payload must contain only the raw bytes, without an embedded schema or schema fingerprint.

After you upload a schema bundle to Bigtable, you can query your Avro data using GoogleSQL for Bigtable, [continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views), or [logical views](https://docs.cloud.google.com/bigtable/docs/create-manage-logical-views).

## Before you begin

Before you create and manage Avro schema bundles, do the following:

  1. Install the [Google Cloud CLI](https://docs.cloud.google.com/bigtable/docs/installing-cloud-sdk).
  2. Initialize the gcloud CLI:
         
         gcloud init
         

  3. Make sure that you have a Bigtable instance and table.

  4. Enable the Cloud Bigtable API and Cloud Bigtable Admin API:
         
         gcloud services enable bigtable.googleapis.com bigtableadmin.googleapis.com
         




## Required roles

To get the permissions that you need to create and manage schema bundles, ask your administrator to grant you the **Bigtable Administrator** (`roles/bigtable.admin`) Identity and Access Management (IAM) role on the table.

To get read-only access to schema bundles and query Avro records using GoogleSQL for Bigtable, ask your administrator to grant you the **Bigtable Reader** (`roles/bigtable.reader`) or **Bigtable User** (`roles/bigtable.user`) role on the table.

These predefined roles contain the permissions that you need to work with schema bundles and query Avro data. To see the required permissions, expand the **Required permissions** section:

### Required permissions

To create and manage schema bundles, you need the following permissions at the table or schema bundle level, depending on the operation:

  * `bigtable.schemaBundles.create`: create schema bundles for a table
  * `bigtable.schemaBundles.update`: update a schema bundle definition
  * `bigtable.schemaBundles.delete`: delete a schema bundle
  * `bigtable.schemaBundles.get`: get information about a schema bundle
  * `bigtable.schemaBundles.list`: list schema bundles in a table
  * `bigtable.schemaBundles.getIamPolicy`: get the IAM policy for a schema bundle
  * `bigtable.schemaBundles.setIamPolicy`: set the IAM policy for a schema bundle



To read or filter Avro records using GoogleSQL for Bigtable, you need the following permissions:

  * `bigtable.tables.readRows`
  * `bigtable.instances.executeQuery`



You can also get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

For more information about Bigtable roles and permissions, see [Access control with IAM](https://docs.cloud.google.com/bigtable/docs/access-control).

## Prepare Avro schema files

Before you create an Avro schema bundle, prepare one or more JSON-formatted Avro schema files in the AVSC or JSON file format. Each file must contain a valid, self-contained Avro `record` schema at the top level with all dependencies inlined. If multiple files in a bundle inline the same `record` or `enum` in the same namespace, the definitions must match, including `doc` and `aliases`.

## Create an Avro schema bundle

To create an Avro schema bundle in a table, use the [`gcloud bigtable schema-bundles create`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/schema-bundles/create) command:
    
    
    gcloud bigtable schema-bundles create SCHEMA_BUNDLE_ID \
        --instance=INSTANCE_ID \
        --table=TABLE_ID \
        --avro-schema-path=AVRO_SCHEMA_PATH
    

Replace the following:

  * `SCHEMA_BUNDLE_ID`: a unique ID for the schema bundle. The ID must be 1 to 50 characters long, can contain only letters, numbers, underscores, and hyphens, can't start with a hyphen, and can't contain a period (`.`) character.
  * `INSTANCE_ID`: the ID of the instance that contains the table.
  * `TABLE_ID`: the ID of the table in which to create the schema bundle.
  * `AVRO_SCHEMA_PATH`: the path to a JSON-formatted Avro schema file, or to a directory that contains one or more Avro schema files. Each file must be a self-contained JSON object with all dependencies inlined.



## View information about schema bundles

You can view information about schema bundles in a table by retrieving the definition of a single schema bundle or by listing all schema bundles in the table.

### Get an Avro schema bundle definition

To retrieve the JSON-formatted Avro schema definition for a schema bundle, use the [`gcloud bigtable schema-bundles describe`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/schema-bundles/describe) command:
    
    
    gcloud bigtable schema-bundles describe SCHEMA_BUNDLE_ID \
        --instance=INSTANCE_ID \
        --table=TABLE_ID
    

Replace the following:

  * `SCHEMA_BUNDLE_ID`: the ID of the schema bundle
  * `INSTANCE_ID`: the ID of the instance
  * `TABLE_ID`: the ID of the table



### List schema bundles in a table

To list the IDs of all schema bundles in a table, including both Avro and protobuf schema bundles, use the [`gcloud bigtable schema-bundles list`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/schema-bundles/list) command:
    
    
    gcloud bigtable schema-bundles list \
        --instance=INSTANCE_ID \
        --table=TABLE_ID
    

Replace the following:

  * `INSTANCE_ID`: the ID of the instance
  * `TABLE_ID`: the ID of the table



To inspect the underlying schema definitions for a specific schema bundle from the list, run the [`gcloud bigtable schema-bundles describe`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/schema-bundles/describe) command.

## Update an Avro schema bundle

To update an Avro schema bundle, use the [`gcloud bigtable schema-bundles update`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/schema-bundles/update) command. You can only add new Avro record or enum definitions to an existing Avro schema bundle, and you can't change the type of a schema bundle between Avro and protobuf. When you update the bundle, you must pass a file or directory that includes both the new schemas and all existing schemas.

**Warning:** After you register an Avro record or enum definition in a schema bundle, you can't modify or remove it. To prevent runtime query failures, data corruption, or incorrectly mapped fields, you must read Avro records using the exact schema that you used to write them.
    
    
    gcloud bigtable schema-bundles update SCHEMA_BUNDLE_ID \
        --instance=INSTANCE_ID \
        --table=TABLE_ID \
        --avro-schema-path=AVRO_SCHEMA_PATH
    

Replace the following:

  * `SCHEMA_BUNDLE_ID`: the ID of the schema bundle to update
  * `INSTANCE_ID`: the ID of the instance that contains the schema bundle
  * `TABLE_ID`: the ID of the table that contains the schema bundle
  * `AVRO_SCHEMA_PATH`: the path to a JSON-formatted Avro schema file, or to a directory that contains one or more Avro schema files



## Delete an Avro schema bundle

If a continuous materialized view or a logical view references a schema bundle, then you can't delete the bundle. Before deleting the bundle, delete any continuous materialized views that reference it. For any logical views that reference the bundle, either update the views to remove the reference or delete them. For more information, see [Create and manage continuous materialized views](https://docs.cloud.google.com/bigtable/docs/manage-continuous-materialized-views) or [Create and manage logical views](https://docs.cloud.google.com/bigtable/docs/create-manage-logical-views).

**Warning:** After you delete an Avro schema bundle, you can't retrieve it.

To delete an Avro schema bundle, use the [`gcloud bigtable schema-bundles delete`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/schema-bundles/delete) command:
    
    
    gcloud bigtable schema-bundles delete SCHEMA_BUNDLE_ID \
        --instance=INSTANCE_ID \
        --table=TABLE_ID
    

Replace the following:

  * `SCHEMA_BUNDLE_ID`: the ID of the schema bundle to delete
  * `INSTANCE_ID`: the ID of the instance that contains the schema bundle
  * `TABLE_ID`: the ID of the table that contains the schema bundle



## Pricing

There's no additional charge to create or manage Avro schema bundles. Standard network bandwidth charges apply for requests and responses. If you use [Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview) serverless compute to read data from Bigtable, then you pay for the compute resources that your queries consume. For more information, see [Bigtable pricing](https://docs.cloud.google.com/bigtable/pricing).

## Limitations

Avro schema bundles have the following limitations:

  * You can read and query a column as Avro records using GoogleSQL for Bigtable, continuous materialized views, and logical views. The Bigtable [`ReadRows`](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#google.bigtable.v2.Bigtable.ReadRows) API and BigQuery external tables don't support server-side Avro parsing.
  * You can create up to 10 schema bundles per table. This limit applies to both Avro and protobuf schema bundles.
  * The total size of the JSON-formatted Avro schemas within a single schema bundle can't exceed 4 MB. Bigtable also converts the bundle into an internal protobuf descriptor set, which can't exceed 4 MB.
  * Bigtable doesn't support the following Avro schema types, structures, and naming patterns: 
    * The `fixed` type and logical types, such as `date`, `duration`, `time-micros`, and `uuid`.
    * Multi-branch unions with more than one non-null type. Only nullable unions, such as `["null", "string"]`, are supported.
    * Nested collections, such as arrays or maps, that contain other arrays or maps.
    * Arrays with nullable elements. Maps with nullable values, such as `{"type": "map", "values": ["null", "string"]}`, are supported.
    * Arrays with empty, zero-field record elements.
    * Cyclic or recursive record definitions, or record references and complex JSON objects, such as inline records, arrays, maps, and enums, nested deeper than 32 levels.
    * Underscores (`_`) in Avro `namespace` values.
    * Duplicate `enum` symbol names across different `enum` types within the same namespace.
    * Multiple `map` fields in the same record whose names convert to the same upper camel case string, such as `my_map`, `myMap`, and `my__map`.
  * When querying data, Bigtable ignores certain Avro schema attributes, such as field default values (`default`), `aliases`, `doc`, and sort order (`order`). However, if multiple files in a bundle define the same `record` or `enum` in the same namespace, their definitions must match, including `doc` and `aliases`.



## What's next

  * Learn how to [query Avro data](https://docs.cloud.google.com/bigtable/docs/query-avro-data).
  * Learn how to [create and manage protobuf schemas](https://docs.cloud.google.com/bigtable/docs/create-manage-protobuf-schemas).
  * Read the [GoogleSQL for Bigtable overview](https://docs.cloud.google.com/bigtable/docs/googlesql-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
