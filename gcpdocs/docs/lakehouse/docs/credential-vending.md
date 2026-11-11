---
url: https://docs.cloud.google.com/lakehouse/docs/credential-vending/
title: Credential vending overview \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T08:30:35.937416+00:00
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

Credential vending mode in the Lakehouse runtime catalog lets you delegate Cloud Storage access to query engines and enforce fine-grained Identity and Access Management (IAM) policies at the catalog, namespace, and table levels for Apache Iceberg tables. Instead of granting direct bucket permissions, you configure the Apache Iceberg REST catalog endpoint to vend short-lived, downscoped storage tokens for authorized table paths. This mode is also required for automatic [table management](https://docs.cloud.google.com/lakehouse/docs/table-options#enable-table-management).

## When to use credential vending

The following are some common use cases:

  * **Enforce table-level access without bucket-level roles** : grant analysts and workloads access to specific Apache Iceberg tables while preventing direct access to underlying Cloud Storage buckets or sibling table directories.
  * **Centralize access governance across multiple query engines** : apply consistent IAM policies across BigQuery, Managed Service for Apache Spark, open-source Apache Spark, and Trino using short-lived, path-scoped tokens.
  * **Isolate warehouse buckets inside a service perimeter** : store table data in Cloud Storage buckets protected by VPC Service Controls while authorizing storage reads and writes through a single catalog endpoint service account.



## How credential vending works

When you use credential vending mode, the sequence of operations enforces IAM policies before storage is accessed. The following diagram illustrates how query engines obtain downscoped storage tokens from the Lakehouse runtime catalog to securely read and write data directly in Cloud Storage:

![Query engines obtain downscoped storage tokens from the Lakehouse runtime catalog to read and write data in Cloud Storage.](https://docs.cloud.google.com/static/lakehouse/images/credential-vending-diagram.svg)Credential vending workflow delegating Cloud Storage access.

The sequence of operations shown in the preceding diagram is as follows:

  1. **Request** : A user submits a SQL statement, such as a query, DML, or DDL operation, to a supported engine, such as Spark or BigQuery.
  2. **Metadata lookup** : The engine sends a request to the Lakehouse runtime catalog to resolve the table.
  3. **Authentication and policy** : The Lakehouse runtime catalog authenticates the user and checks their IAM permissions on Lakehouse resources.
  4. **Response** : Because credential vending mode is enabled, the Lakehouse runtime catalog returns the metadata and a short-lived **storage token** (downscoped storage credentials) to the engine. The token is scoped to the paths associated with the table and downscoped to the minimum required permissions (for example, read-only access for queries that don't need to write files).
  5. **Access** : The engine uses this token to read or write the specific authorized files directly from Cloud Storage.
  6. **Compute** : The engine processes the data or executes the operation, and returns the results.



When automatic [table management](https://docs.cloud.google.com/lakehouse/docs/table-options#enable-table-management) (`gcp.biglake.table-management.enabled`) is enabled, background maintenance tasks such as compaction, snapshot expiration, and garbage collection use the catalog's auto-provisioned service account to authenticate directly to Cloud Storage and update the underlying data files.

## Supported engines

To use credential vending with query engines, you must configure the Apache Iceberg REST catalog endpoint in your Lakehouse runtime catalog in credential vending mode. Credential vending isn't supported for Apache Hive catalog endpoints.

  * **Open-source engines** : Supported engines such as Spark and Trino use short-lived storage tokens vended by the Lakehouse runtime catalog. Your client application must specify support for credential vending in the `X-Iceberg-Access-Delegation` header.
  * **BigQuery** : BigQuery uses vended credentials for Cloud Storage access instead of end-user credentials.



## Required service account permissions

When credential vending mode is enabled, ensure that the following service accounts have the necessary roles:

  * **Auto-provisioned catalog endpoint service account** : You must grant the Storage Object User role (`roles/storage.objectUser`) to this account on all associated Cloud Storage buckets. Without this access, vended credentials can't read or write to storage. If you use the Google Cloud console, clicking **Set bucket permissions** verifies this role. For the Google Cloud CLI, Terraform, or the REST API, you must grant this role manually.
  * **Query engine service accounts** : Service accounts running query engine jobs (such as Managed Service for Apache Spark or Dataflow) require the BigLake Editor role (`roles/biglake.editor`) to obtain vended credentials with write scope.

**Note:** Creation of the auto-provisioned catalog endpoint service account is eventually consistent. It takes time for the service account to propagate through the system. If you try to grant roles to the service account immediately after creation, the request might fail. To learn how long it takes, on average, for access changes to propagate, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

## Use VPC Service Controls with credential vending

When you use the Apache Iceberg REST catalog endpoint in credential vending mode with Cloud Storage buckets inside a [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) service perimeter, you can support the following use cases:

  * **Create and modify Apache Iceberg tables in protected buckets** : run `CREATE TABLE` or DML statements from BigQuery, Managed Service for Apache Spark, Spark, or Trino when warehouse buckets reside inside a service perimeter.
  * **Delegate fine-grained table reads inside a storage perimeter** : enforce table-level IAM policies using short-lived, downscoped storage tokens without granting end users or query runtimes direct IAM roles on perimeter-protected buckets.



In credential vending mode, query engines and Lakehouse authenticate to Cloud Storage using credentials issued for the catalog endpoint's auto-provisioned service account (`blirc-PROJECT_NUMBER-ID@gcp-sa-biglakerestcatalog.iam.gserviceaccount.com`). Because this service agent belongs to a Google-managed project outside your service perimeter, Cloud Storage evaluates requests authenticated with its credentials as perimeter ingress whenever the bucket project's perimeter restricts `storage.googleapis.com`. This evaluation applies even when the catalog endpoint, query job, and bucket are in the same project and service perimeter.

To allow access, configure an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) in Access Context Manager on the perimeter that protects the bucket project with the following settings:

  * **Source identity** : `serviceAccount:blirc-PROJECT_NUMBER-ID@gcp-sa-biglakerestcatalog.iam.gserviceaccount.com`
  * **Target project** : The bucket project (`projects/BUCKET_PROJECT_NUMBER`)
  * **Service** : `storage.googleapis.com` with all methods (`'*'`), or specific [supported service methods](https://docs.cloud.google.com/vpc-service-controls/docs/supported-method-restrictions)



The following `ingress.yaml` example allows the catalog endpoint's service account to access `storage.googleapis.com` in the bucket project:
    
    
    - ingressFrom:
        identities:
        - serviceAccount:CATALOG_ENDPOINT_SERVICE_ACCOUNT
        sources:
        - accessLevel: '*'
      ingressTo:
        operations:
        - serviceName: storage.googleapis.com
          methodSelectors:
          - method: '*'
        resources:
        - projects/BUCKET_PROJECT_NUMBER
    

Replace the following:

  * `CATALOG_ENDPOINT_SERVICE_ACCOUNT`: your catalog endpoint's auto-provisioned service account email address (`blirc-PROJECT_NUMBER-ID@gcp-sa-biglakerestcatalog.iam.gserviceaccount.com`). To retrieve this email address, describe the catalog endpoint:
        
        gcloud biglake iceberg catalogs describe CATALOG_ID \
            --project=PROJECT_ID \
            --format='value(biglake-service-account)'
        

In this command, `CATALOG_ID` is the ID of your catalog endpoint and `PROJECT_ID` is the ID of the project that contains the catalog endpoint.

  * `BUCKET_PROJECT_NUMBER`: the numeric project number of the project that contains the Cloud Storage bucket.




If a table creation or query request is blocked by VPC Service Controls, then the error message includes a `vpcServiceControlsUniqueIdentifier` value. Search [Policy Denied audit logs](https://docs.cloud.google.com/logging/docs/audit#policy_denied) in Cloud Audit Logs by matching `protoPayload.metadata.vpcServiceControlsUniqueId` to that identifier, and inspect `ingressViolations` for the `blirc-...` principal. For more information, see [Retrieve VPC Service Controls errors from audit logs](https://docs.cloud.google.com/vpc-service-controls/docs/retrieve-troubleshoot-errors).

## What's next

  * [Create a catalog endpoint in credential vending mode](https://docs.cloud.google.com/lakehouse/docs/set-up-lakehouse-iceberg-rest-catalog#create_a_catalog).
  * [Enable credential vending for an existing catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/enable-credential-vending).
  * [Configure your client application for credential vending](https://docs.cloud.google.com/lakehouse/docs/set-up-lakehouse-iceberg-rest-catalog#configure-catalog).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-11 UTC."],[],[]] 
