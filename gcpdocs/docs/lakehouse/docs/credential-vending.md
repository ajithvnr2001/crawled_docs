---
url: https://docs.cloud.google.com/lakehouse/docs/credential-vending/
title: Credential vending overview \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:39:05.772138+00:00
---

# Credential vending overview  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/credential-vending/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Credential vending overview Stay organized with collections  Save and categorize content based on your preferences. 

Credential vending for the Lakehouse runtime catalog lets you delegate Cloud Storage access to query engines and enforce fine-grained Identity and Access Management (IAM) policies at the catalog, namespace, and table levels using the Google Cloud console or the Google Cloud CLI. Credential vending is also required to enable automatic [table management](https://docs.cloud.google.com/lakehouse/docs/table-options#enable_table_management) for background maintenance tasks such as compaction, snapshot expiration, and garbage collection.

## How credential vending works

When you use credential vending, the sequence of operations changes slightly to enforce policies before storage is accessed. The following diagram illustrates how query engines obtain downscoped storage tokens from the catalog to securely read and write data directly in Cloud Storage:

![Query engines obtain downscoped storage tokens from the Lakehouse runtime catalog to read and write data in Cloud Storage.](https://docs.cloud.google.com/static/lakehouse/images/credential-vending-diagram.svg)Credential vending workflow delegating Cloud Storage access.

The sequence of operations shown in the preceding diagram is as follows:

  1. **Request** : A user submits a SQL statement, such as a query, DML, or DDL operation, to a supported engine such as Apache Spark or BigQuery.
  2. **Metadata lookup** : The engine sends a request to the Lakehouse runtime catalog to resolve the table.
  3. **Authentication and policy** : The catalog authenticates the user and checks their IAM permissions on Lakehouse resources.
  4. **Response** : Because credential vending is enabled, the catalog returns the metadata and a short-lived **storage token** (downscoped storage credentials) to the engine. The token is scoped to the paths associated with the table and downscoped to the minimum required permissions (for example, read-only access for queries that don't need to write files).
  5. **Access** : The engine uses this token to read or write the specific authorized files directly from Cloud Storage.
  6. **Compute** : The engine processes the data or executes the operation, and returns the results.



When automatic [table management](https://docs.cloud.google.com/lakehouse/docs/table-options#enable_table_management) (`gcp.biglake.table-management.enabled`) is enabled, background maintenance tasks such as compaction, snapshot expiration, and garbage collection use the catalog's auto-provisioned service account to authenticate directly to Cloud Storage and update the underlying data files.

## Supported engines

To use credential vending with query engines, you must configure the Apache Iceberg REST catalog endpoint in your Lakehouse runtime catalog to support credential vending. Credential vending isn't supported for Apache Hive catalog endpoints.

  * **Open source engines** : Supported engines like Spark and Trino use short-lived storage tokens vended by the catalog. Your client application must specify support for credential vending in the `X-Iceberg-Access-Delegation` header.
  * **BigQuery** : BigQuery uses vended credentials for Cloud Storage access instead of end-user credentials.



## Required service account permissions

When credential vending is enabled, ensure the following service accounts have the necessary roles:

  * **Auto-provisioned Lakehouse runtime catalog service account** : You must grant the Storage Object User role (`roles/storage.objectUser`) to this account on all associated Cloud Storage buckets. Without this access, vended credentials can't read or write to storage. If you use the Google Cloud console, clicking **Set bucket permissions** verifies this role. For the gcloud CLI, Terraform, or the API, you must grant this role manually.
  * **Query engine service accounts** : Service accounts running query engine jobs (such as Managed Service for Apache Spark, Managed Service for Apache Spark, or Dataflow) require the BigLake Editor role (`roles/biglake.editor`) to obtain vended credentials with write scope.

**Note:** Creation of the auto-provisioned catalog service account is eventually consistent. This means that it takes time for the service account to propagate through the system. If you try to grant roles to the service account immediately after creation, the request might fail. To learn how long it takes, on average, for access changes to propagate, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

## What's next

  * Learn how to [create a catalog in credential vending mode](https://docs.cloud.google.com/lakehouse/docs/set-up-lakehouse-iceberg-rest-catalog#create_a_catalog).
  * Learn how to [enable credential vending for an existing catalog using the Google Cloud console](https://docs.cloud.google.com/lakehouse/docs/enable-credential-vending). 
    * Learn how to [configure your client application for credential vending](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog#configure-catalog).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
